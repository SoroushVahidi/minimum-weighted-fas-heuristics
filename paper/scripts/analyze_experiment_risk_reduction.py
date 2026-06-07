"""
Postprocessing analysis for CAIE revision risk-reduction pass.
Reads existing committed result CSVs; does NOT rerun any algorithm.
"""
import csv
import json
import math
import sys
from pathlib import Path
from collections import defaultdict

# ── optional dependencies ──────────────────────────────────────────────────
try:
    import pandas as pd
    HAS_PANDAS = True
except ImportError:
    HAS_PANDAS = False

try:
    from scipy import stats as scipy_stats
    HAS_SCIPY = True
except ImportError:
    HAS_SCIPY = False

# ── paths ─────────────────────────────────────────────────────────────────
BASE = Path(__file__).resolve().parents[2]
EXP4_RAW = BASE / "experiments/exp4_external_baselines/summary/exp4_raw_summary.csv"
EXP5_RAW = BASE / "experiments/exp5_lolib_dense/summary/exp5_lolib_raw_summary.csv"
COMBINED_EXT_SPARSE = BASE / "experiments/combined/tables/manuscript_table_external_sparse.csv"
OUT = BASE / "paper/notes/experimental_risk_reduction"
TABLE_OUT = BASE / "paper/tables"
OUT.mkdir(parents=True, exist_ok=True)
TABLE_OUT.mkdir(parents=True, exist_ok=True)

# ── label map ─────────────────────────────────────────────────────────────
LABEL = {
    "ipsns_full": "IPSNS",
    "lrta_full": "LR-TA",
    "wmsf_seed": "WMSF",
    "drmaciver_fas": "DRMacIver/FAS",
    "igraph_approx_eades": "igraph Eades",
    "weighted_eades": "Weighted Eades",
    "borda_net_score": "Borda",
    "random_multistart": "Random MS",
}

# ── helpers ───────────────────────────────────────────────────────────────

def read_csv(path):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def median(vals):
    s = sorted(vals)
    n = len(s)
    if n == 0:
        return float("nan")
    mid = n // 2
    return s[mid] if n % 2 else (s[mid - 1] + s[mid]) / 2


def mean(vals):
    if not vals:
        return float("nan")
    return sum(vals) / len(vals)


def quartiles(vals):
    s = sorted(vals)
    n = len(s)
    if n == 0:
        return (float("nan"),) * 3
    q1 = s[n // 4]
    q2 = median(s)
    q3 = s[3 * n // 4]
    return q1, q2, q3


def sign_test(diffs):
    """Two-sided sign test; diffs positive = IPSNS better."""
    pos = sum(1 for d in diffs if d > 0)
    neg = sum(1 for d in diffs if d < 0)
    n = pos + neg
    if n == 0:
        return float("nan")
    # exact binomial two-sided under H0: p=0.5
    if HAS_SCIPY:
        result = scipy_stats.binomtest(pos, n, 0.5, alternative="two-sided")
        return float(result.pvalue)
    # fallback: normal approximation
    z = (pos - n / 2) / math.sqrt(n / 4)
    # two-sided: 2 * Phi(-|z|) via erf
    p = math.erfc(abs(z) / math.sqrt(2))
    return p


def wilcoxon_p(diffs):
    if not HAS_SCIPY:
        return None
    nonzero = [d for d in diffs if d != 0]
    if len(nonzero) < 4:
        return None
    try:
        result = scipy_stats.wilcoxon(nonzero, alternative="two-sided", zero_method="wilcox")
        return float(result.pvalue)
    except Exception:
        return None


def pivot_by_instance(rows, alg_col="algorithm", inst_col="instance",
                      bw_col="backward_weight", rt_col="runtime",
                      status_col="status"):
    """Return {instance: {alg: {bw, rt, status}}}."""
    d = defaultdict(dict)
    for r in rows:
        if r.get(status_col) == "ok" and r.get(bw_col, "").strip():
            try:
                bw = float(r[bw_col])
                rt = float(r.get(rt_col) or 0)
            except ValueError:
                continue
            d[r[inst_col]][r[alg_col]] = {"bw": bw, "rt": rt}
    return d


def paired_stats(pivot, alg_a, alg_b):
    """
    Compare alg_a vs alg_b on common completed instances.
    Positive improvement = alg_a (IPSNS) is better (lower BW).
    Returns dict of statistics.
    """
    common = [inst for inst, algmap in pivot.items()
              if alg_a in algmap and alg_b in algmap]
    if not common:
        return {"n_paired": 0, "note": "no common completed instances"}

    diffs_abs = []
    diffs_rel = []
    wins = ties = losses = 0
    for inst in common:
        bw_a = pivot[inst][alg_a]["bw"]
        bw_b = pivot[inst][alg_b]["bw"]
        d = bw_b - bw_a  # positive = A (IPSNS) is better
        diffs_abs.append(d)
        if bw_b > 0:
            diffs_rel.append(d / bw_b * 100)
        if d > 0:
            wins += 1
        elif d == 0:
            ties += 1
        else:
            losses += 1

    wp = wilcoxon_p(diffs_abs)
    sp = sign_test(diffs_abs)
    q1, q2, q3 = quartiles(diffs_abs)

    return {
        "n_paired": len(common),
        "wins": wins, "ties": ties, "losses": losses,
        "mean_improvement_bw": round(mean(diffs_abs), 4),
        "median_improvement_bw": round(median(diffs_abs), 4),
        "q1_improvement_bw": round(q1, 4),
        "q3_improvement_bw": round(q3, 4),
        "mean_rel_improvement_pct": round(mean(diffs_rel), 4) if diffs_rel else None,
        "median_rel_improvement_pct": round(median(diffs_rel), 4) if diffs_rel else None,
        "wilcoxon_p": round(wp, 6) if wp is not None else None,
        "sign_test_p": round(sp, 6) if not math.isnan(sp) else None,
        "scipy_available": HAS_SCIPY,
        "note": "Positive improvement = IPSNS (lower BW) is better. Wilcoxon and sign test are two-sided.",
    }


def fmt_p(p):
    if p is None:
        return "n/a"
    if p < 0.001:
        return "<0.001"
    return f"{p:.4f}"


# ══════════════════════════════════════════════════════════════════════════
# 1. Load EXP4 (sparse external) data
# ══════════════════════════════════════════════════════════════════════════
print("Loading EXP4 sparse data...")
exp4_rows = read_csv(EXP4_RAW)
# Restrict to the standard 97-instance set: status=ok instances that appear
# for ipsns_full (the reference algorithm)
ipsns_ok_instances = {r["instance"] for r in exp4_rows
                      if r["algorithm"] == "ipsns_full" and r["status"] == "ok"}
print(f"  IPSNS-completed instances: {len(ipsns_ok_instances)}")

# Filter to those instances only (97-instance set)
sparse_rows = [r for r in exp4_rows if r["instance"] in ipsns_ok_instances]
pivot_sparse = pivot_by_instance(sparse_rows)

# ══════════════════════════════════════════════════════════════════════════
# 2. Paired sparse tests
# ══════════════════════════════════════════════════════════════════════════
print("Computing paired sparse tests...")

pairs = [
    ("ipsns_full", "drmaciver_fas", "IPSNS vs DRMacIver/FAS"),
    ("ipsns_full", "lrta_full", "IPSNS vs LR-TA"),
    ("ipsns_full", "wmsf_seed", "IPSNS vs WMSF"),
    ("ipsns_full", "igraph_approx_eades", "IPSNS vs igraph Eades"),
    ("ipsns_full", "weighted_eades", "IPSNS vs Weighted Eades"),
]

paired_results = {}
for alg_a, alg_b, label in pairs:
    paired_results[label] = paired_stats(pivot_sparse, alg_a, alg_b)

(OUT / "paired_sparse_tests.json").write_text(
    json.dumps(paired_results, indent=2))

# Markdown report
md = "# Paired Statistical Tests — Sparse External Benchmark\n\n"
md += ("All comparisons are IPSNS vs baseline on common completed instances "
       "(standard 97-instance sparse benchmark). "
       "Positive improvement = IPSNS achieves lower backward weight. "
       "These tests provide distributional support for observed differences; "
       "they do not certify optimality.\n\n")
if HAS_SCIPY:
    md += "_scipy available: Wilcoxon signed-rank test computed._\n\n"
else:
    md += "_scipy not available: sign test (binomial normal approximation) only._\n\n"

for label, s in paired_results.items():
    md += f"## {label}\n\n"
    if s.get("n_paired", 0) == 0:
        md += f"- No common completed instances. {s.get('note','')}\n\n"
        continue
    md += f"- Paired instances: {s['n_paired']}\n"
    md += f"- Win / Tie / Loss (IPSNS better / equal / worse): {s['wins']} / {s['ties']} / {s['losses']}\n"
    md += f"- Mean improvement (BW units): {s['mean_improvement_bw']:,.4f}\n"
    md += f"- Median improvement (BW units): {s['median_improvement_bw']:,.4f}\n"
    md += f"- Q1 / Q3 improvement: {s['q1_improvement_bw']:,.4f} / {s['q3_improvement_bw']:,.4f}\n"
    if s.get("mean_rel_improvement_pct") is not None:
        md += f"- Mean relative improvement: {s['mean_rel_improvement_pct']:.4f}%\n"
        md += f"- Median relative improvement: {s['median_rel_improvement_pct']:.4f}%\n"
    md += f"- Wilcoxon signed-rank p: {fmt_p(s.get('wilcoxon_p'))}\n"
    md += f"- Sign-test p: {fmt_p(s.get('sign_test_p'))}\n\n"

(OUT / "paired_sparse_tests.md").write_text(md)
print("  Written paired_sparse_tests.json and .md")

# ══════════════════════════════════════════════════════════════════════════
# 3. IPSNS gain concentration
# ══════════════════════════════════════════════════════════════════════════
print("Computing IPSNS gain concentration...")

lrta_pivot = {}  # instance -> (ipsns_bw, lrta_bw, n, m)
for inst in ipsns_ok_instances:
    algmap = pivot_sparse.get(inst, {})
    if "ipsns_full" in algmap and "lrta_full" in algmap:
        # get n, m from a row
        meta = next((r for r in sparse_rows if r["instance"] == inst
                     and r["algorithm"] == "lrta_full"), None)
        n_nodes = int(float(meta["n"])) if meta and meta.get("n") else None
        m_arcs = int(float(meta["m"])) if meta and meta.get("m") else None
        ipsns_bw = algmap["ipsns_full"]["bw"]
        lrta_bw = algmap["lrta_full"]["bw"]
        lrta_pivot[inst] = {
            "ipsns_bw": ipsns_bw, "lrta_bw": lrta_bw,
            "n": n_nodes, "m": m_arcs,
            "improvement_abs": lrta_bw - ipsns_bw,
            "improvement_rel_pct": (lrta_bw - ipsns_bw) / lrta_bw * 100
            if lrta_bw > 0 else 0.0,
        }

improvements = [v["improvement_abs"] for v in lrta_pivot.values()]
rel_improvements = [v["improvement_rel_pct"] for v in lrta_pivot.values()]
n_ipsns_improves = sum(1 for d in improvements if d > 0)
n_ties = sum(1 for d in improvements if d == 0)
n_worse = sum(1 for d in improvements if d < 0)

top10 = sorted(lrta_pivot.items(), key=lambda x: x[1]["improvement_abs"], reverse=True)[:10]

q1, q2, q3 = quartiles(improvements)
gain_conc = {
    "n_instances": len(lrta_pivot),
    "n_ipsns_improves_over_lrta": n_ipsns_improves,
    "n_ties": n_ties,
    "n_ipsns_worse": n_worse,
    "mean_improvement_abs": round(mean(improvements), 4),
    "median_improvement_abs": round(q2, 4),
    "q1_improvement_abs": round(q1, 4),
    "q3_improvement_abs": round(q3, 4),
    "mean_improvement_rel_pct": round(mean(rel_improvements), 4),
    "median_improvement_rel_pct": round(median(rel_improvements), 4),
    "top10_instances": [
        {"instance": inst,
         "improvement_abs": round(v["improvement_abs"], 2),
         "improvement_rel_pct": round(v["improvement_rel_pct"], 4),
         "n": v["n"], "m": v["m"]}
        for inst, v in top10
    ],
    "note": ("Graph structural features (SCC counts) not pre-computed in committed files; "
             "density = m/n(n-1) available for instances with n, m."),
}

# add density info to top10
for item in gain_conc["top10_instances"]:
    n, m = item["n"], item["m"]
    if n and n > 1:
        item["density"] = round(m / (n * (n - 1)), 6)
    else:
        item["density"] = None

(OUT / "ipsns_gain_concentration.json").write_text(
    json.dumps(gain_conc, indent=2))

md2 = "# IPSNS Gain Concentration over LR-TA — Sparse Benchmark\n\n"
md2 += f"- Instances compared: {gain_conc['n_instances']}\n"
md2 += f"- IPSNS improves over LR-TA: {n_ipsns_improves} instances\n"
md2 += f"- Ties: {n_ties} instances\n"
md2 += f"- IPSNS worse: {n_worse} instances\n"
md2 += f"- Mean absolute improvement (BW units): {gain_conc['mean_improvement_abs']:,.4f}\n"
md2 += f"- Median absolute improvement: {gain_conc['median_improvement_abs']:,.4f}\n"
md2 += f"- Q1 / Q3: {gain_conc['q1_improvement_abs']:,.4f} / {gain_conc['q3_improvement_abs']:,.4f}\n"
md2 += f"- Mean relative improvement: {gain_conc['mean_improvement_rel_pct']:.4f}%\n"
md2 += f"- Median relative improvement: {gain_conc['median_improvement_rel_pct']:.4f}%\n\n"
md2 += "## Top-10 instances by absolute IPSNS improvement over LR-TA\n\n"
md2 += "| Instance | Improvement (BW) | Rel. (%) | n | m | Density |\n"
md2 += "|---|---:|---:|---:|---:|---:|\n"
for item in gain_conc["top10_instances"]:
    md2 += (f"| {item['instance']} | {item['improvement_abs']:,.2f} | "
            f"{item['improvement_rel_pct']:.4f} | {item['n']} | {item['m']} | "
            f"{item['density'] or 'n/a'} |\n")
md2 += ("\n**Note:** SCC counts not pre-computed; a future experimental pass "
        "could add SCC-based features per instance.\n")
(OUT / "ipsns_gain_concentration.md").write_text(md2)
print("  Written ipsns_gain_concentration.json and .md")

# ══════════════════════════════════════════════════════════════════════════
# 4. Runtime-quality summary
# ══════════════════════════════════════════════════════════════════════════
print("Computing runtime-quality summary...")

# Use combined external sparse table for summary stats
ext_rows = read_csv(COMBINED_EXT_SPARSE)
# Also compute per-instance runtime from EXP4 raw (completed instances)
rt_bw = {}
for alg in ["ipsns_full", "lrta_full", "wmsf_seed", "drmaciver_fas",
            "igraph_approx_eades", "weighted_eades"]:
    completed = [r for r in sparse_rows
                 if r["algorithm"] == alg and r["status"] == "ok"
                 and r.get("backward_weight","").strip()]
    if not completed:
        rt_bw[alg] = None
        continue
    bws = [float(r["backward_weight"]) for r in completed]
    rts = [float(r["runtime"]) for r in completed]
    rt_bw[alg] = {
        "n_completed": len(completed),
        "mean_bw": round(mean(bws), 4),
        "median_bw": round(median(bws), 4),
        "mean_rt_s": round(mean(rts), 6),
        "median_rt_s": round(median(rts), 6),
    }

rtq = {
    "source": "EXP4 sparse external benchmark (standard 97-instance set, status=ok only)",
    "algorithms": {LABEL.get(alg, alg): v for alg, v in rt_bw.items() if v},
    "note": ("IPSNS runtime ~22 s is the full SCC-refinement budget. "
             "LR-TA ~0.08 s is seed-only. "
             "WMSF ~1.3 s includes weighted seed construction. "
             "DRMacIver/FAS ~4 s via external wrapper on 93/97 completed. "
             "True budget curve (quality vs. iteration count) requires a new experiment."),
}
(OUT / "runtime_quality_summary.json").write_text(json.dumps(rtq, indent=2))

md3 = "# Runtime-Quality Summary — Sparse External Benchmark\n\n"
md3 += ("Based on EXP4 raw results (standard 97-instance sparse benchmark, "
        "status=ok completed instances only). Lower BW = better.\n\n")
md3 += "| Algorithm | n completed | Mean BW | Median BW | Mean RT (s) | Median RT (s) |\n"
md3 += "|---|---:|---:|---:|---:|---:|\n"
for alg, v in rt_bw.items():
    if v:
        md3 += (f"| {LABEL.get(alg,alg)} | {v['n_completed']} | "
                f"{v['mean_bw']:,.1f} | {v['median_bw']:,.1f} | "
                f"{v['mean_rt_s']:.4f} | {v['median_rt_s']:.4f} |\n")

md3 += ("\n**Note:** A true quality-vs-budget curve (varying IPSNS iteration "
        "limit) is not available from existing committed outputs and requires "
        "a dedicated future experiment.\n")
(OUT / "runtime_quality_summary.md").write_text(md3)
print("  Written runtime_quality_summary.json and .md")

# ══════════════════════════════════════════════════════════════════════════
# 5. Sparse vs dense diagnostic
# ══════════════════════════════════════════════════════════════════════════
print("Computing sparse vs dense diagnostic...")

exp5_rows = read_csv(EXP5_RAW)
pivot_dense = pivot_by_instance(exp5_rows)

def regime_stats(pivot, alg_a, alg_b):
    common = [inst for inst, am in pivot.items()
              if alg_a in am and alg_b in am]
    if not common:
        return None
    a_wins = sum(1 for i in common if pivot[i][alg_a]["bw"] < pivot[i][alg_b]["bw"])
    b_wins = sum(1 for i in common if pivot[i][alg_b]["bw"] < pivot[i][alg_a]["bw"])
    ties = len(common) - a_wins - b_wins
    mean_bw_a = mean([pivot[i][alg_a]["bw"] for i in common])
    mean_bw_b = mean([pivot[i][alg_b]["bw"] for i in common])
    mean_rt_a = mean([pivot[i][alg_a]["rt"] for i in common])
    mean_rt_b = mean([pivot[i][alg_b]["rt"] for i in common])
    return {
        "n": len(common),
        "wins_a": a_wins, "wins_b": b_wins, "ties": ties,
        "mean_bw_a": round(mean_bw_a, 2),
        "mean_bw_b": round(mean_bw_b, 2),
        "mean_rt_a_s": round(mean_rt_a, 4),
        "mean_rt_b_s": round(mean_rt_b, 4),
    }

sparse_diag = regime_stats(pivot_sparse, "ipsns_full", "drmaciver_fas")
dense_diag = regime_stats(pivot_dense, "ipsns_full", "drmaciver_fas")

# Also check families for dense
family_map = {r["instance"]: r["family"] for r in exp5_rows}
family_diag = {}
for fam in ["SGB", "RandA1", "IO"]:
    sub = {inst: am for inst, am in pivot_dense.items()
           if family_map.get(inst) == fam}
    fd = regime_stats(sub, "ipsns_full", "drmaciver_fas") if sub else None
    if fd:
        family_diag[fam] = fd

sparse_dense = {
    "sparse_benchmark": {
        "label": "Standard sparse benchmark (EXP4, 97-instance set)",
        "ipsns_vs_drmaciver": sparse_diag,
    },
    "dense_lolib": {
        "label": "Dense LOLIB benchmark (EXP5, 50 instances)",
        "ipsns_vs_drmaciver": dense_diag,
        "per_family": family_diag,
    },
    "interpretation": (
        "On the sparse benchmark IPSNS wins more instances than DRMacIver/FAS. "
        "On dense LOLIB DRMacIver/FAS wins more instances. "
        "This supports the structural narrative: IPSNS is SCC-refinement oriented "
        "(sparse), DRMacIver/FAS is matrix-based pairwise-ordering (dense-friendly)."
    ),
}
(OUT / "sparse_dense_diagnostic.json").write_text(
    json.dumps(sparse_dense, indent=2))

md4 = "# Sparse vs Dense Structural Diagnostic\n\n"
md4 += "## Sparse benchmark (EXP4 standard set)\n\n"
if sparse_diag:
    s = sparse_diag
    md4 += f"- Instances: {s['n']}\n"
    md4 += (f"- IPSNS wins / DRMacIver wins / Ties: "
            f"{s['wins_a']} / {s['wins_b']} / {s['ties']}\n")
    md4 += f"- Mean BW — IPSNS: {s['mean_bw_a']:,.2f}, DRMacIver: {s['mean_bw_b']:,.2f}\n"
    md4 += f"- Mean RT — IPSNS: {s['mean_rt_a_s']:.4f} s, DRMacIver: {s['mean_rt_b_s']:.4f} s\n\n"

md4 += "## Dense LOLIB benchmark (EXP5, 50 instances)\n\n"
if dense_diag:
    d = dense_diag
    md4 += f"- Instances: {d['n']}\n"
    md4 += (f"- IPSNS wins / DRMacIver wins / Ties: "
            f"{d['wins_a']} / {d['wins_b']} / {d['ties']}\n")
    md4 += f"- Mean BW — IPSNS: {d['mean_bw_a']:,.2f}, DRMacIver: {d['mean_bw_b']:,.2f}\n"
    md4 += f"- Mean RT — IPSNS: {d['mean_rt_a_s']:.4f} s, DRMacIver: {d['mean_rt_b_s']:.4f} s\n\n"
    md4 += "### Per-family breakdown\n\n"
    md4 += "| Family | n | IPSNS wins | DRM wins | Ties | Mean BW IPSNS | Mean BW DRM |\n"
    md4 += "|---|---:|---:|---:|---:|---:|---:|\n"
    for fam, fd in family_diag.items():
        md4 += (f"| {fam} | {fd['n']} | {fd['wins_a']} | {fd['wins_b']} | "
                f"{fd['ties']} | {fd['mean_bw_a']:,.2f} | {fd['mean_bw_b']:,.2f} |\n")

md4 += f"\n**Interpretation:** {sparse_dense['interpretation']}\n"
(OUT / "sparse_dense_diagnostic.md").write_text(md4)
print("  Written sparse_dense_diagnostic.json and .md")

# ══════════════════════════════════════════════════════════════════════════
# 6. LaTeX table: paired sparse tests
# ══════════════════════════════════════════════════════════════════════════
print("Writing LaTeX table...")

tex = r"""\begin{table}[htbp]
\centering
\caption{Paired statistical tests comparing IPSNS against each baseline on
the common completed instances of the standard sparse benchmark.
Improvement is the per-instance reduction in backward weight achieved by IPSNS;
positive values indicate IPSNS attains a lower backward weight.
The Wilcoxon signed-rank test and sign test are two-sided;
they provide distributional support for the observed differences
and do not replace exact optimality certificates.}
\label{tab:paired_sparse_tests}
\small
\begin{tabular}{lrrrrrrr}
\toprule
Comparison & $n$ & W & T & L & Median $\Delta$BW & Wilcoxon $p$ & Sign-test $p$ \\
\midrule
"""

pair_order = [
    ("IPSNS vs LR-TA", "IPSNS vs LR-TA"),
    ("IPSNS vs WMSF", "IPSNS vs WMSF"),
    ("IPSNS vs DRMacIver/FAS", "IPSNS vs DRMacIver/FAS"),
    ("IPSNS vs igraph Eades", "IPSNS vs igraph Eades"),
    ("IPSNS vs Weighted Eades", "IPSNS vs Weighted Eades"),
]

for key, display in pair_order:
    s = paired_results.get(key)
    if not s or s.get("n_paired", 0) == 0:
        tex += f"{display} & -- & -- & -- & -- & -- & -- & -- \\\\\n"
        continue
    wp = fmt_p(s.get("wilcoxon_p"))
    sp = fmt_p(s.get("sign_test_p"))
    med = s["median_improvement_bw"]
    # Format median
    if abs(med) >= 1:
        med_str = f"{med:,.0f}"
    else:
        med_str = f"{med:.2f}"
    tex += (f"{display} & {s['n_paired']} & {s['wins']} & {s['ties']} & "
            f"{s['losses']} & {med_str} & {wp} & {sp} \\\\\n")

tex += r"""\bottomrule
\end{tabular}
\begin{tablenotes}
\small
\item W\,=\,wins (IPSNS lower BW), T\,=\,ties, L\,=\,losses.
Median $\Delta$BW is in backward-weight units (lower is better for IPSNS).
"""
if not HAS_SCIPY:
    tex += r"\item scipy was unavailable; Wilcoxon p is not computed." + "\n"
tex += r"""\end{tablenotes}
\end{table}
"""

(TABLE_OUT / "table_paired_sparse_tests.tex").write_text(tex)
print("  Written table_paired_sparse_tests.tex")

# ══════════════════════════════════════════════════════════════════════════
# 7. LaTeX table: runtime-quality tradeoff
# ══════════════════════════════════════════════════════════════════════════
alg_order = ["ipsns_full", "lrta_full", "wmsf_seed",
             "drmaciver_fas", "weighted_eades", "igraph_approx_eades"]

tex2 = r"""\begin{table}[htbp]
\centering
\caption{Runtime and backward-weight quality summary for the main algorithms
on the standard sparse benchmark (EXP4, completed instances only, lower BW is better).
Runtime is wall-clock seconds; mean and median are computed over completed instances.}
\label{tab:runtime_quality_tradeoff}
\small
\begin{tabular}{lrrrrrr}
\toprule
Algorithm & $n$ compl. & Mean BW & Median BW & Mean RT (s) & Median RT (s) \\
\midrule
"""
for alg in alg_order:
    v = rt_bw.get(alg)
    if v:
        tex2 += (f"{LABEL.get(alg, alg)} & {v['n_completed']} & "
                 f"{v['mean_bw']:,.0f} & {v['median_bw']:,.0f} & "
                 f"{v['mean_rt_s']:.3f} & {v['median_rt_s']:.3f} \\\\\n")
tex2 += r"""\bottomrule
\end{tabular}
\end{table}
"""
(TABLE_OUT / "table_runtime_quality_tradeoff.tex").write_text(tex2)
print("  Written table_runtime_quality_tradeoff.tex")

# ══════════════════════════════════════════════════════════════════════════
# 8. Summary print
# ══════════════════════════════════════════════════════════════════════════
print("\n=== ANALYSIS COMPLETE ===")
print(f"Outputs written to: {OUT}")
print(f"LaTeX tables written to: {TABLE_OUT}")
print("\nKey results:")
for label, s in paired_results.items():
    if s.get("n_paired", 0) > 0:
        print(f"  {label}: n={s['n_paired']}, W/T/L={s['wins']}/{s['ties']}/{s['losses']}, "
              f"median_imp={s['median_improvement_bw']:,.1f}, "
              f"wilcoxon_p={fmt_p(s.get('wilcoxon_p'))}, "
              f"sign_p={fmt_p(s.get('sign_test_p'))}")
print(f"\nIPSNS gain concentration (vs LR-TA): {n_ipsns_improves}/{len(lrta_pivot)} instances improved, "
      f"mean={mean(improvements):,.1f} BW, median={median(improvements):,.1f} BW")
print(f"\nSparse: IPSNS wins {sparse_diag['wins_a']}/{sparse_diag['n']} vs DRMacIver; "
      f"Dense: IPSNS wins {dense_diag['wins_a']}/{dense_diag['n']} vs DRMacIver")
