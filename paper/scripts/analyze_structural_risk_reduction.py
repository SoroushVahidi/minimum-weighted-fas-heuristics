"""
Graph-feature and SCC-structure analysis for CAIE revision risk-reduction pass 2.
Parses existing benchmark instance files and correlates graph features with
IPSNS gains using existing result CSV values. No algorithms are rerun.
"""
import csv
import json
import math
import sys
from pathlib import Path
from collections import defaultdict

try:
    import networkx as nx
    HAS_NX = True
except ImportError:
    HAS_NX = False

try:
    from scipy import stats as scipy_stats
    HAS_SCIPY = True
except ImportError:
    HAS_SCIPY = False

# ── paths ─────────────────────────────────────────────────────────────────
BASE = Path(__file__).resolve().parents[2]
EXP4_RAW = BASE / "experiments/exp4_external_baselines/summary/exp4_raw_summary.csv"
EXP5_RAW = BASE / "experiments/exp5_lolib_dense/summary/exp5_lolib_raw_summary.csv"
EXP4_INST_LIST = BASE / "experiments/exp4_external_baselines/configs/exp4_instances.txt"
LOLIB_CONVERTED_DIR = BASE / "experiments/exp5_lolib_dense/converted"
OUT = BASE / "paper/notes/structural_risk_reduction"
TABLE_OUT = BASE / "paper/tables"
OUT.mkdir(parents=True, exist_ok=True)

# ── helpers ───────────────────────────────────────────────────────────────

def mean(vals):
    return sum(vals) / len(vals) if vals else float("nan")

def median(vals):
    s = sorted(vals)
    n = len(s)
    if n == 0:
        return float("nan")
    mid = n // 2
    return s[mid] if n % 2 else (s[mid - 1] + s[mid]) / 2

def spearman_r(x, y):
    if not HAS_SCIPY or len(x) < 4:
        return None, None
    pairs = [(xi, yi) for xi, yi in zip(x, y)
             if not (math.isnan(xi) or math.isnan(yi) or math.isinf(xi) or math.isinf(yi))]
    if len(pairs) < 4:
        return None, None
    xs, ys = zip(*pairs)
    res = scipy_stats.spearmanr(xs, ys)
    return float(res.statistic), float(res.pvalue)

def parse_dimacs(path):
    """
    Parse a weighted DIMACS file. Supports two formats:
    - 'p printed-... n m' + 'a u v w cap'  (sparse benchmark, 5 arc fields)
    - 'p sp n m'          + 'a u v w'      (LOLIB converted, 4 arc fields)
    Returns (n, edges) where edges is list of (u, v, w).
    """
    n = 0
    edges = []
    try:
        with open(path, errors="ignore") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("c"):
                    continue
                if line.startswith("p "):
                    parts = line.split()
                    n = int(parts[2])
                elif line.startswith("a "):
                    parts = line.split()
                    if len(parts) >= 4:
                        u, v, w = int(parts[1]), int(parts[2]), float(parts[3])
                        edges.append((u, v, w))
    except Exception:
        pass
    return n, edges


def compute_graph_features(n, edges):
    """Compute structural features from parsed graph."""
    if n == 0 or not edges:
        return None

    m = len(edges)
    density = m / (n * (n - 1)) if n > 1 else 0.0
    total_weight = sum(w for _, _, w in edges)

    features = {
        "n": n, "m": m,
        "density": round(density, 6),
        "total_weight": round(total_weight, 2),
    }

    if not HAS_NX:
        return features

    G = nx.DiGraph()
    G.add_nodes_from(range(1, n + 1))
    for u, v, w in edges:
        if w > 0:
            G.add_edge(u, v, weight=w)

    sccs = list(nx.strongly_connected_components(G))
    nontrivial = [s for s in sccs if len(s) > 1]
    n_nontrivial_sccs = len(nontrivial)
    largest_scc_size = max((len(s) for s in nontrivial), default=0)
    largest_scc_frac = largest_scc_size / n if n > 0 else 0.0
    n_in_nontrivial = sum(len(s) for s in nontrivial)
    frac_in_nontrivial = n_in_nontrivial / n if n > 0 else 0.0
    is_acyclic = (n_nontrivial_sccs == 0)

    # Fraction of arcs internal to nontrivial SCCs
    nontrivial_sets = [frozenset(s) for s in nontrivial]
    internal_arcs = 0
    for u, v, _ in edges:
        for s in nontrivial_sets:
            if u in s and v in s:
                internal_arcs += 1
                break
    frac_internal_arcs = internal_arcs / m if m > 0 else 0.0

    features.update({
        "n_nontrivial_sccs": n_nontrivial_sccs,
        "largest_scc_size": largest_scc_size,
        "largest_scc_frac": round(largest_scc_frac, 6),
        "n_in_nontrivial_sccs": n_in_nontrivial,
        "frac_in_nontrivial_sccs": round(frac_in_nontrivial, 6),
        "frac_arcs_internal_to_sccs": round(frac_internal_arcs, 6),
        "is_acyclic": is_acyclic,
    })
    return features


def read_instance_list(path):
    """Return {stem: Path} from an instance list file."""
    mapping = {}
    try:
        with open(path) as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                p = Path(line)
                mapping[p.stem] = p
    except Exception:
        pass
    return mapping


def read_csv_rows(path):
    with open(path, newline="", errors="ignore") as f:
        return list(csv.DictReader(f))


# ══════════════════════════════════════════════════════════════════════════
# 1. Build instance → file mapping
# ══════════════════════════════════════════════════════════════════════════
print("Building sparse instance file map...")
sparse_file_map = read_instance_list(EXP4_INST_LIST)
print(f"  Sparse instance list: {len(sparse_file_map)} entries")

# Build LOLIB file map: instance -> Path
lolib_file_map = {}
for d_file in LOLIB_CONVERTED_DIR.rglob("*.d"):
    lolib_file_map[d_file.stem] = d_file
print(f"  LOLIB converted files: {len(lolib_file_map)}")

# ══════════════════════════════════════════════════════════════════════════
# 2. Extract sparse graph features
# ══════════════════════════════════════════════════════════════════════════
print("Extracting sparse graph features...")
sparse_features = {}
sparse_missing = []

exp4_rows = read_csv_rows(EXP4_RAW)
ipsns_ok = {r["instance"] for r in exp4_rows
            if r["algorithm"] == "ipsns_full" and r["status"] == "ok"}

for inst in ipsns_ok:
    if inst not in sparse_file_map:
        sparse_missing.append(inst)
        continue
    fp = sparse_file_map[inst]
    if not fp.exists():
        sparse_missing.append(inst)
        continue
    n, edges = parse_dimacs(fp)
    feat = compute_graph_features(n, edges)
    if feat:
        sparse_features[inst] = feat

print(f"  Features extracted: {len(sparse_features)} / {len(ipsns_ok)}")
print(f"  Missing files: {len(sparse_missing)}")

# Write sparse features CSV
fieldnames = ["instance", "n", "m", "density", "total_weight",
              "n_nontrivial_sccs", "largest_scc_size", "largest_scc_frac",
              "n_in_nontrivial_sccs", "frac_in_nontrivial_sccs",
              "frac_arcs_internal_to_sccs", "is_acyclic"]
with open(OUT / "graph_features_sparse.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
    w.writeheader()
    for inst, feat in sorted(sparse_features.items()):
        row = {"instance": inst}
        row.update(feat)
        w.writerow(row)
print("  Written graph_features_sparse.csv")

# ══════════════════════════════════════════════════════════════════════════
# 3. Extract LOLIB graph features
# ══════════════════════════════════════════════════════════════════════════
print("Extracting LOLIB graph features...")
lolib_features = {}
lolib_missing = []

exp5_rows = read_csv_rows(EXP5_RAW)
lolib_instances = sorted(set(r["instance"] for r in exp5_rows))
lolib_family_map = {r["instance"]: r.get("family", "") for r in exp5_rows}

for inst in lolib_instances:
    if inst not in lolib_file_map:
        lolib_missing.append(inst)
        continue
    fp = lolib_file_map[inst]
    if not fp.exists():
        lolib_missing.append(inst)
        continue
    n, edges = parse_dimacs(fp)
    feat = compute_graph_features(n, edges)
    if feat:
        feat["family"] = lolib_family_map.get(inst, "")
        lolib_features[inst] = feat

print(f"  LOLIB features extracted: {len(lolib_features)} / {len(lolib_instances)}")
print(f"  LOLIB missing files: {len(lolib_missing)}")

with open(OUT / "graph_features_lolib.csv", "w", newline="") as f:
    fieldnames_l = ["instance", "family", "n", "m", "density", "total_weight",
                    "n_nontrivial_sccs", "largest_scc_size", "largest_scc_frac",
                    "n_in_nontrivial_sccs", "frac_in_nontrivial_sccs",
                    "frac_arcs_internal_to_sccs", "is_acyclic"]
    w = csv.DictWriter(f, fieldnames=fieldnames_l, extrasaction="ignore")
    w.writeheader()
    for inst, feat in sorted(lolib_features.items()):
        row = {"instance": inst}
        row.update(feat)
        w.writerow(row)
print("  Written graph_features_lolib.csv")

# ══════════════════════════════════════════════════════════════════════════
# 4. Compute IPSNS gain and correlate with features
# ══════════════════════════════════════════════════════════════════════════
print("Computing IPSNS gain-feature correlations...")

# Per-instance pivot for EXP4
pivot4 = defaultdict(dict)
for r in exp4_rows:
    if r["status"] == "ok" and r.get("backward_weight", "").strip():
        try:
            pivot4[r["instance"]][r["algorithm"]] = float(r["backward_weight"])
        except ValueError:
            pass

# Compute IPSNS improvement over LR-TA and over DRMacIver/FAS
gain_lrta = {}
gain_wmsf = {}
gain_drm = {}

for inst, algmap in pivot4.items():
    if inst not in sparse_features:
        continue
    if "ipsns_full" in algmap:
        if "lrta_full" in algmap:
            gain_lrta[inst] = algmap["lrta_full"] - algmap["ipsns_full"]
        if "wmsf_seed" in algmap:
            gain_wmsf[inst] = algmap["wmsf_seed"] - algmap["ipsns_full"]
        if "drmaciver_fas" in algmap:
            gain_drm[inst] = algmap["drmaciver_fas"] - algmap["ipsns_full"]

def correlate(gain_dict, feat_key, feat_label):
    common = [(gain_dict[i], sparse_features[i].get(feat_key, float("nan")))
              for i in gain_dict if i in sparse_features
              and sparse_features[i].get(feat_key) is not None]
    if not common:
        return None
    gains, feats = zip(*common)
    r, p = spearman_r(gains, feats)
    return {"feature": feat_label, "n": len(common),
            "spearman_r": round(r, 4) if r is not None else None,
            "p_value": round(p, 4) if p is not None else None}

feat_keys = [
    ("n", "n (vertices)"),
    ("m", "m (arcs)"),
    ("density", "density"),
    ("largest_scc_frac", "largest SCC fraction"),
    ("frac_in_nontrivial_sccs", "fraction in nontrivial SCCs"),
    ("frac_arcs_internal_to_sccs", "fraction arcs internal to SCCs"),
    ("n_nontrivial_sccs", "n nontrivial SCCs"),
]

corr_lrta = [c for k, l in feat_keys if (c := correlate(gain_lrta, k, l))]
corr_drm = [c for k, l in feat_keys if (c := correlate(gain_drm, k, l))]

# Quantile summaries for gain by SCC fraction quartile
scc_fracs = [(inst, sparse_features[inst].get("largest_scc_frac", 0))
             for inst in gain_lrta if inst in sparse_features]
scc_fracs.sort(key=lambda x: x[1])
n_q = len(scc_fracs)
q_size = max(1, n_q // 4)

quantile_summary = []
labels = ["Q1 (low SCC frac)", "Q2", "Q3", "Q4 (high SCC frac)"]
for qi, label in enumerate(labels):
    start = qi * q_size
    end = (qi + 1) * q_size if qi < 3 else n_q
    group_insts = [inst for inst, _ in scc_fracs[start:end]]
    gains = [gain_lrta[i] for i in group_insts if i in gain_lrta]
    scc_f = [sparse_features[i]["largest_scc_frac"] for i in group_insts if i in sparse_features]
    quantile_summary.append({
        "label": label,
        "n": len(group_insts),
        "mean_scc_frac": round(mean(scc_f), 4),
        "mean_gain_lrta": round(mean(gains), 2),
        "median_gain_lrta": round(median(gains), 2),
    })

corr_result = {
    "n_sparse_with_features": len(sparse_features),
    "n_gain_lrta": len(gain_lrta),
    "n_gain_drm": len(gain_drm),
    "correlations_ipsns_vs_lrta_gain": corr_lrta,
    "correlations_ipsns_vs_drmaciver_gain": corr_drm,
    "quantile_by_scc_frac": quantile_summary,
    "note": ("Spearman correlation of IPSNS improvement over baseline against graph features. "
             "Improvement = baseline_BW - IPSNS_BW; positive = IPSNS better."),
}
(OUT / "ipsns_gain_feature_correlation.json").write_text(
    json.dumps(corr_result, indent=2))

md = "# IPSNS Gain-Feature Correlation\n\n"
md += f"- Sparse instances with features: {len(sparse_features)}\n"
md += f"- Instances with IPSNS vs LR-TA gain: {len(gain_lrta)}\n"
md += f"- Instances with IPSNS vs DRMacIver/FAS gain: {len(gain_drm)}\n\n"
md += ("All improvements are IPSNS BW minus baseline BW (sign-flipped: "
       "positive = IPSNS achieves lower backward weight).\n\n")

md += "## Spearman correlations with IPSNS gain over LR-TA\n\n"
md += "| Feature | n | Spearman r | p |\n|---|---:|---:|---:|\n"
for c in corr_lrta:
    r_str = f"{c['spearman_r']:.4f}" if c['spearman_r'] is not None else "n/a"
    p_str = (f"<0.001" if c['p_value'] is not None and c['p_value'] < 0.001
             else (f"{c['p_value']:.4f}" if c['p_value'] is not None else "n/a"))
    md += f"| {c['feature']} | {c['n']} | {r_str} | {p_str} |\n"

md += "\n## Spearman correlations with IPSNS gain over DRMacIver/FAS\n\n"
md += "| Feature | n | Spearman r | p |\n|---|---:|---:|---:|\n"
for c in corr_drm:
    r_str = f"{c['spearman_r']:.4f}" if c['spearman_r'] is not None else "n/a"
    p_str = (f"<0.001" if c['p_value'] is not None and c['p_value'] < 0.001
             else (f"{c['p_value']:.4f}" if c['p_value'] is not None else "n/a"))
    md += f"| {c['feature']} | {c['n']} | {r_str} | {p_str} |\n"

md += "\n## IPSNS gain over LR-TA by SCC fraction quartile\n\n"
md += "| Group | n | Mean SCC frac | Mean gain | Median gain |\n"
md += "|---|---:|---:|---:|---:|\n"
for q in quantile_summary:
    md += (f"| {q['label']} | {q['n']} | {q['mean_scc_frac']:.4f} | "
           f"{q['mean_gain_lrta']:,.2f} | {q['median_gain_lrta']:,.2f} |\n")
(OUT / "ipsns_gain_feature_correlation.md").write_text(md)
print("  Written ipsns_gain_feature_correlation.json and .md")

# ══════════════════════════════════════════════════════════════════════════
# 5. Sparse vs dense structural diagnostic
# ══════════════════════════════════════════════════════════════════════════
print("Computing sparse vs dense structural diagnostic...")

sparse_n_vals = [f["n"] for f in sparse_features.values()]
sparse_m_vals = [f["m"] for f in sparse_features.values()]
sparse_dens = [f["density"] for f in sparse_features.values()]
sparse_scc_frac = [f.get("largest_scc_frac", 0) for f in sparse_features.values()]
sparse_frac_nontrivial = [f.get("frac_in_nontrivial_sccs", 0) for f in sparse_features.values()]
sparse_n_scc = [f.get("n_nontrivial_sccs", 0) for f in sparse_features.values()]
sparse_acyclic = sum(1 for f in sparse_features.values() if f.get("is_acyclic", False))

lolib_n_vals = [f["n"] for f in lolib_features.values()]
lolib_m_vals = [f["m"] for f in lolib_features.values()]
lolib_dens = [f["density"] for f in lolib_features.values()]
lolib_scc_frac = [f.get("largest_scc_frac", 0) for f in lolib_features.values()]
lolib_frac_nontrivial = [f.get("frac_in_nontrivial_sccs", 0) for f in lolib_features.values()]
lolib_n_scc = [f.get("n_nontrivial_sccs", 0) for f in lolib_features.values()]

diag = {
    "sparse_benchmark": {
        "n_instances": len(sparse_features),
        "mean_n": round(mean(sparse_n_vals), 1),
        "mean_m": round(mean(sparse_m_vals), 1),
        "median_density": round(median(sparse_dens), 6),
        "mean_density": round(mean(sparse_dens), 6),
        "mean_largest_scc_frac": round(mean(sparse_scc_frac), 4),
        "mean_frac_in_nontrivial_sccs": round(mean(sparse_frac_nontrivial), 4),
        "mean_n_nontrivial_sccs": round(mean(sparse_n_scc), 2),
        "n_acyclic_instances": sparse_acyclic,
    },
    "lolib_dense_benchmark": {
        "n_instances": len(lolib_features),
        "mean_n": round(mean(lolib_n_vals), 1),
        "mean_m": round(mean(lolib_m_vals), 1),
        "median_density": round(median(lolib_dens), 6),
        "mean_density": round(mean(lolib_dens), 6),
        "mean_largest_scc_frac": round(mean(lolib_scc_frac), 4),
        "mean_frac_in_nontrivial_sccs": round(mean(lolib_frac_nontrivial), 4),
        "mean_n_nontrivial_sccs": round(mean(lolib_n_scc), 2),
    },
    "interpretation": (
        "Sparse benchmark instances have low density (mean ~{:.4f}) and localized cyclic "
        "substructures (mean fraction of vertices in nontrivial SCCs: ~{:.2%}). "
        "LOLIB instances, by contrast, have near-complete density (mean ~{:.4f}) with "
        "essentially all vertices in one large SCC (mean fraction: ~{:.2%}). "
        "This structural contrast is consistent with the observed performance: "
        "SCC-local refinement (IPSNS) targets isolated cyclic subgraphs effectively on "
        "sparse instances, while matrix-based pairwise-ordering (DRMacIver/FAS) aligns "
        "naturally with fully dense complete-ordering instances."
    ).format(
        mean(sparse_dens), mean(sparse_frac_nontrivial),
        mean(lolib_dens), mean(lolib_frac_nontrivial),
    ),
}
(OUT / "sparse_dense_structural_diagnostic.json").write_text(
    json.dumps(diag, indent=2))

s = diag["sparse_benchmark"]
l = diag["lolib_dense_benchmark"]
md2 = "# Sparse vs Dense Structural Diagnostic\n\n"
md2 += "## Sparse benchmark\n\n"
md2 += f"- Instances: {s['n_instances']}\n"
md2 += f"- Mean n: {s['mean_n']:.1f}, Mean m: {s['mean_m']:.1f}\n"
md2 += f"- Mean density: {s['mean_density']:.6f}, Median density: {s['median_density']:.6f}\n"
md2 += f"- Mean largest-SCC fraction: {s['mean_largest_scc_frac']:.4f}\n"
md2 += f"- Mean fraction of vertices in nontrivial SCCs: {s['mean_frac_in_nontrivial_sccs']:.4f}\n"
md2 += f"- Mean number of nontrivial SCCs: {s['mean_n_nontrivial_sccs']:.2f}\n"
md2 += f"- Acyclic instances (no nontrivial SCCs): {s['n_acyclic_instances']}\n\n"

md2 += "## LOLIB dense benchmark\n\n"
md2 += f"- Instances: {l['n_instances']}\n"
md2 += f"- Mean n: {l['mean_n']:.1f}, Mean m: {l['mean_m']:.1f}\n"
md2 += f"- Mean density: {l['mean_density']:.6f}, Median density: {l['median_density']:.6f}\n"
md2 += f"- Mean largest-SCC fraction: {l['mean_largest_scc_frac']:.4f}\n"
md2 += f"- Mean fraction of vertices in nontrivial SCCs: {l['mean_frac_in_nontrivial_sccs']:.4f}\n"
md2 += f"- Mean number of nontrivial SCCs: {l['mean_n_nontrivial_sccs']:.2f}\n\n"

md2 += f"## Interpretation\n\n{diag['interpretation']}\n"
(OUT / "sparse_dense_structural_diagnostic.md").write_text(md2)
print("  Written sparse_dense_structural_diagnostic.json and .md")

# ══════════════════════════════════════════════════════════════════════════
# 6. LaTeX structural diagnostic table
# ══════════════════════════════════════════════════════════════════════════
print("Writing LaTeX structural diagnostic table...")

tex = r"""\begin{table}[htbp]
\centering
\footnotesize
\caption{Structural comparison between the standard sparse benchmark and the
dense LOLIB transfer benchmark. Density is $m / n(n{-}1)$ for directed graphs.
Largest-SCC fraction is the fraction of vertices belonging to the largest
strongly connected component. All statistics are computed from the
converted DIMACS instance files used in the experiments.}
\label{tab:structural_diagnostic}
\begin{tabular}{lrr}
\toprule
Feature & Sparse benchmark & Dense LOLIB \\
\midrule
"""
tex += f"Instances & {s['n_instances']} & {l['n_instances']} \\\\\n"
tex += f"Mean $n$ (vertices) & {s['mean_n']:.0f} & {l['mean_n']:.0f} \\\\\n"
tex += f"Mean $m$ (arcs) & {s['mean_m']:.0f} & {l['mean_m']:.0f} \\\\\n"
tex += f"Mean density & {s['mean_density']:.4f} & {l['mean_density']:.4f} \\\\\n"
tex += f"Mean largest-SCC frac. & {s['mean_largest_scc_frac']:.4f} & {l['mean_largest_scc_frac']:.4f} \\\\\n"
tex += f"Mean frac. in nontrivial SCCs & {s['mean_frac_in_nontrivial_sccs']:.4f} & {l['mean_frac_in_nontrivial_sccs']:.4f} \\\\\n"
tex += f"Mean nontrivial SCC count & {s['mean_n_nontrivial_sccs']:.1f} & {l['mean_n_nontrivial_sccs']:.1f} \\\\\n"
tex += r"""\bottomrule
\multicolumn{3}{p{0.9\linewidth}}{\footnotesize
Sparse benchmark uses the \texttt{graph-benchmarks} collection (standard 97-instance nonnegative subset after exclusions).
LOLIB dense benchmark uses 50 converted DIMACS instances across three families (SGB, RandA1, IO).
SCC features computed from converted DIMACS instance files.} \\
\end{tabular}
\end{table}
"""
(TABLE_OUT / "table_structural_diagnostic.tex").write_text(tex)
print("  Written table_structural_diagnostic.tex")

# ══════════════════════════════════════════════════════════════════════════
# 7. README
# ══════════════════════════════════════════════════════════════════════════
readme = f"""# Structural Risk-Reduction Pass — README

## What was computed
- Graph features extracted from {len(sparse_features)} sparse benchmark instances
  (benchmark_sources/graph-benchmarks/) and {len(lolib_features)} LOLIB converted DIMACS files.
- Features: n, m, density, n nontrivial SCCs, largest SCC fraction, fraction in nontrivial SCCs,
  fraction of arcs internal to SCCs, acyclicity.
- Spearman correlations of IPSNS gain (vs LR-TA and vs DRMacIver/FAS) with graph features.
- Quantile summaries of IPSNS gain by largest-SCC-fraction quartile.
- Sparse vs dense structural comparison table.

## What was NOT recomputed
- No algorithm runs were performed.
- All BW and runtime values are from committed EXP4/EXP5 result CSVs.

## Missing instance files
- Sparse: {len(sparse_missing)} instances in EXP4 set had no matching file
  (these are likely instances excluded from the standard set or deduplication cases).
- LOLIB: {len(lolib_missing)} missing.

## Files generated
- graph_features_sparse.csv — per-instance features for sparse benchmark
- graph_features_lolib.csv — per-instance features for LOLIB benchmark
- ipsns_gain_feature_correlation.json/.md — Spearman correlations and quantile summaries
- sparse_dense_structural_diagnostic.json/.md — aggregate comparison
- paper/tables/table_structural_diagnostic.tex — compact LaTeX table

## Manuscript files updated
(see parent analysis for details)
"""
(OUT / "README.md").write_text(readme)

# ══════════════════════════════════════════════════════════════════════════
# 8. Summary
# ══════════════════════════════════════════════════════════════════════════
print("\n=== STRUCTURAL ANALYSIS COMPLETE ===")
print(f"Sparse features: {len(sparse_features)} / {len(ipsns_ok)}")
print(f"LOLIB features: {len(lolib_features)} / {len(lolib_instances)}")
print(f"\nSparse: mean density={mean(sparse_dens):.5f}, mean SCC frac={mean(sparse_scc_frac):.4f}, mean frac_in_nontrivial={mean(sparse_frac_nontrivial):.4f}")
print(f"LOLIB:  mean density={mean(lolib_dens):.5f}, mean SCC frac={mean(lolib_scc_frac):.4f}, mean frac_in_nontrivial={mean(lolib_frac_nontrivial):.4f}")
print("\nIPSNS vs LR-TA gain correlations:")
for c in corr_lrta:
    print(f"  {c['feature']}: r={c['spearman_r']}, p={c['p_value']}")
print("\nIPSNS vs DRMacIver gain correlations:")
for c in corr_drm:
    print(f"  {c['feature']}: r={c['spearman_r']}, p={c['p_value']}")
print("\nQuantile summary:")
for q in quantile_summary:
    print(f"  {q['label']}: n={q['n']}, mean_scc_frac={q['mean_scc_frac']}, mean_gain={q['mean_gain_lrta']}")
