"""
Build manuscript-ready consolidated tables and a results digest from EXP1b–EXP5.

Reads committed summary/table files; does not require raw per-run directories.
Writes to experiments/combined/tables/ and experiments/combined/summary/.
"""

import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
OUT_TABLES = Path(__file__).resolve().parent / "tables"
OUT_SUMMARY = Path(__file__).resolve().parent / "summary"
OUT_TABLES.mkdir(parents=True, exist_ok=True)
OUT_SUMMARY.mkdir(parents=True, exist_ok=True)

missing_or_unparsed: list[str] = []


def _load_json(path: Path) -> dict | None:
    if not path.exists():
        missing_or_unparsed.append(str(path))
        return None
    with open(path) as f:
        return json.load(f)


def _load_csv(path: Path) -> list[dict] | None:
    if not path.exists():
        missing_or_unparsed.append(str(path))
        return None
    with open(path) as f:
        return list(csv.DictReader(f))


def _write_csv(path: Path, rows: list[dict], fieldnames: list[str]):
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)
    print(f"  wrote {path.relative_to(ROOT)}")


# ---------------------------------------------------------------------------
# Table 1: Core sparse benchmark (EXP1b)
# ---------------------------------------------------------------------------

def build_table_core_sparse():
    src = ROOT / "experiments/exp1b_core_benchmark_full_wmsf_seed/summary/exp1b_core_benchmark_stats.json"
    stats = _load_json(src)
    if stats is None:
        return None

    mean_rt = stats.get("mean_runtime_by_algorithm", {})
    rows = [
        {
            "algorithm": "IPSNS",
            "label": "IPSNS (ours)",
            "n_instances": stats["n_instances"],
            "n_incumbent_violations": stats.get("incumbent_protection_violations_external", 0),
            "improves_over_lrta": stats.get("ipsns_improves_lrta", "N/A"),
            "improves_over_wmsf": stats.get("ipsns_improves_wmsf", "N/A"),
            "mean_rel_gain_pct": round(stats.get("mean_relative_gain_over_best_seed", 0) * 100, 4),
            "mean_runtime_s": round(mean_rt.get("ipsns", 0), 3),
            "note": "0 incumbent violations; best-seed improvement on 36/105",
        },
        {
            "algorithm": "LR-TA",
            "label": "LR-TA (ours)",
            "n_instances": stats["n_instances"],
            "n_incumbent_violations": "N/A",
            "improves_over_lrta": "N/A",
            "improves_over_wmsf": "N/A",
            "mean_rel_gain_pct": "N/A",
            "mean_runtime_s": round(mean_rt.get("lrta", 0), 4),
            "note": "seed algorithm; used as incumbent lower bound",
        },
        {
            "algorithm": "WMSF",
            "label": "WMSF (ours, seed)",
            "n_instances": stats["n_instances"],
            "n_incumbent_violations": "N/A",
            "improves_over_lrta": "N/A",
            "improves_over_wmsf": "N/A",
            "mean_rel_gain_pct": "N/A",
            "mean_runtime_s": round(mean_rt.get("wmsf", 0), 4),
            "note": "seed algorithm (reimplementation of paper049 pipeline)",
        },
    ]
    fields = ["algorithm", "label", "n_instances", "n_incumbent_violations",
              "improves_over_lrta", "improves_over_wmsf",
              "mean_rel_gain_pct", "mean_runtime_s", "note"]
    out = OUT_TABLES / "manuscript_table_core_sparse.csv"
    _write_csv(out, rows, fields)
    return {"source": str(src.relative_to(ROOT)), "rows_written": len(rows)}


# ---------------------------------------------------------------------------
# Table 2: External baseline comparison (EXP4)
# ---------------------------------------------------------------------------

def build_table_external_sparse():
    src_json = ROOT / "experiments/exp4_external_baselines/summary/exp4_external_stats.json"
    src_csv  = ROOT / "experiments/exp4_external_baselines/tables/exp4_external_paper_summary.csv"
    stats = _load_json(src_json)
    csv_rows = _load_csv(src_csv)
    if stats is None and csv_rows is None:
        return None

    # Build from CSV rows (more complete)
    rows = []
    if csv_rows:
        col_map = {r["algorithm"]: r for r in csv_rows}
        display_order = [
            ("ipsns_full",         "IPSNS (ours)"),
            ("lrta_full",          "LR-TA (ours)"),
            ("wmsf_seed",          "WMSF (ours, seed)"),
            ("drmaciver_fas",      "DRMaciver [external]"),
            ("igraph_approx_eades","igraph Eades [external]"),
            ("weighted_eades",     "Weighted Eades [external]"),
            ("borda_net_score",    "Borda net score [external]"),
            ("random_multistart",  "Random multistart [external]"),
        ]
        for alg, label in display_order:
            r = col_map.get(alg)
            if r is None:
                continue
            rows.append({
                "algorithm": alg,
                "label": label,
                "n_complete": r.get("n_complete", ""),
                "n_total": r.get("n_total", "97"),
                "mean_bw": r.get("mean_bw", ""),
                "median_bw": r.get("median_bw", ""),
                "mean_fw_ratio": r.get("mean_fw_ratio", ""),
                "mean_runtime_s": r.get("mean_runtime_s", ""),
                "n_times_best": r.get("n_times_best", ""),
                "mean_rel_gain_ipsns_pct": r.get("mean_rel_gain_ipsns_pct", "0.0"),
                "source_type": r.get("source_type", ""),
            })
    elif stats:
        # Fallback: build from JSON
        pa = stats.get("per_algorithm", {})
        display_order = ["ipsns_full", "lrta_full", "wmsf_seed",
                         "drmaciver_fas", "igraph_approx_eades",
                         "weighted_eades", "borda_net_score", "random_multistart"]
        for alg in display_order:
            d = pa.get(alg, {})
            rows.append({
                "algorithm": alg,
                "label": alg,
                "n_complete": d.get("n_complete", ""),
                "n_total": stats["n_standard"],
                "mean_bw": round(d.get("mean_bw", 0), 4) if d.get("mean_bw") else "",
                "median_bw": "",
                "mean_fw_ratio": "",
                "mean_runtime_s": "",
                "n_times_best": "",
                "mean_rel_gain_ipsns_pct": round(d.get("mean_rel_gain_ipsns_pct", 0), 4),
                "source_type": "",
            })

    fields = ["algorithm", "label", "n_complete", "n_total", "mean_bw", "median_bw",
              "mean_fw_ratio", "mean_runtime_s", "n_times_best",
              "mean_rel_gain_ipsns_pct", "source_type"]
    out = OUT_TABLES / "manuscript_table_external_sparse.csv"
    _write_csv(out, rows, fields)
    used = str(src_csv.relative_to(ROOT)) if csv_rows else str(src_json.relative_to(ROOT))
    return {"source": used, "rows_written": len(rows)}


# ---------------------------------------------------------------------------
# Table 3: Exact small-instance validation (EXP3)
# ---------------------------------------------------------------------------

def build_table_exact_small():
    src_json = ROOT / "experiments/exp3_exact_small/summary/exp3_exact_stats.json"
    src_csv  = ROOT / "experiments/exp3_exact_small/tables/exp3_exact_summary.csv"
    stats = _load_json(src_json)

    std = stats.get("standard_instances", {}) if stats else {}
    rows = [
        {
            "algorithm": "IPSNS",
            "label": "IPSNS (ours)",
            "n_instances": 57,
            "n_optimal": 56,
            "pct_optimal": "98.2%",
            "mean_gap_pct": std.get("ipsns_mean_gap_pct", "0.0006%"),
            "note": "only near-miss: r20_60 (n=20, 0.03% gap)",
        },
        {
            "algorithm": "LR-TA",
            "label": "LR-TA (ours)",
            "n_instances": 57,
            "n_optimal": 55,
            "pct_optimal": "96.5%",
            "mean_gap_pct": std.get("lrta_mean_gap_pct", "0.0590%"),
            "note": "",
        },
        {
            "algorithm": "WMSF",
            "label": "WMSF (ours, seed)",
            "n_instances": 57,
            "n_optimal": 51,
            "pct_optimal": "89.5%",
            "mean_gap_pct": std.get("wmsf_mean_gap_pct", "0.0961%"),
            "note": "",
        },
    ]
    fields = ["algorithm", "label", "n_instances", "n_optimal",
              "pct_optimal", "mean_gap_pct", "note"]
    out = OUT_TABLES / "manuscript_table_exact_small.csv"
    _write_csv(out, rows, fields)
    used = str(src_json.relative_to(ROOT)) if stats else str(src_csv.relative_to(ROOT))
    return {"source": used, "rows_written": len(rows)}


# ---------------------------------------------------------------------------
# Table 4: Ablation (EXP2)
# ---------------------------------------------------------------------------

def build_table_ablation():
    src = ROOT / "experiments/exp2_ablation/summary/exp2_ablation_stats.json"
    stats = _load_json(src)
    if stats is None:
        return None

    variant_labels = {
        "lr_no_addback":       "LR (no add-back)",
        "lrta_full":           "LR-TA (add-back, no LNS)",
        "wmsf_seed":           "WMSF seed only",
        "best_seed_no_lns":    "Best seed (no LNS)",
        "ipsns_50iters":       "IPSNS 50 iters",
        "ipsns_100iters":      "IPSNS 100 iters",
        "ipsns_full":          "IPSNS full (200 iters)",
        "ipsns_no_scc_priority": "IPSNS no SCC priority",
    }
    display_order = ["lr_no_addback", "lrta_full", "wmsf_seed", "best_seed_no_lns",
                     "ipsns_50iters", "ipsns_100iters", "ipsns_full", "ipsns_no_scc_priority"]
    rows = []
    ref_bw = stats.get("lrta_full", {}).get("mean_bw")
    ipsns_bw = stats.get("ipsns_full", {}).get("mean_bw")
    for v in display_order:
        d = stats.get(v, {})
        bw = d.get("mean_bw")
        rel_vs_lrta = (
            round((bw - ref_bw) / ref_bw * 100, 3)
            if bw is not None and ref_bw
            else "N/A"
        )
        rel_vs_ipsns = (
            round((bw - ipsns_bw) / ipsns_bw * 100, 3)
            if bw is not None and ipsns_bw
            else "N/A"
        )
        rows.append({
            "variant": v,
            "label": variant_labels.get(v, v),
            "n_ok": d.get("n_ok", ""),
            "mean_bw": round(bw, 2) if bw is not None else "",
            "median_bw": d.get("median_bw", ""),
            "mean_runtime_s": round(d.get("mean_runtime", 0), 4),
            "rel_vs_lrta_pct": rel_vs_lrta,
            "rel_vs_ipsns_pct": rel_vs_ipsns,
        })
    fields = ["variant", "label", "n_ok", "mean_bw", "median_bw",
              "mean_runtime_s", "rel_vs_lrta_pct", "rel_vs_ipsns_pct"]
    out = OUT_TABLES / "manuscript_table_ablation.csv"
    _write_csv(out, rows, fields)
    return {"source": str(src.relative_to(ROOT)), "rows_written": len(rows)}


# ---------------------------------------------------------------------------
# Table 5: LOLIB dense transfer test (EXP5)
# ---------------------------------------------------------------------------

def build_table_lolib_dense():
    src_json = ROOT / "experiments/exp5_lolib_dense/summary/exp5_lolib_stats.json"
    src_csv  = ROOT / "experiments/exp5_lolib_dense/tables/exp5_lolib_paper_summary.csv"
    stats = _load_json(src_json)
    csv_rows = _load_csv(src_csv)

    rows = []
    if csv_rows:
        col_map = {r["algorithm"]: r for r in csv_rows}
        display_order = [
            ("ipsns_full",         "IPSNS (ours)"),
            ("lrta_full",          "LR-TA (ours)"),
            ("wmsf_seed",          "WMSF (ours, seed)"),
            ("drmaciver_fas",      "DRMaciver [external, tournament-native]"),
            ("igraph_approx_eades","igraph Eades [external]"),
            ("weighted_eades",     "Weighted Eades [external]"),
            ("borda_net_score",    "Borda net score [external]"),
            ("random_multistart",  "Random multistart [external]"),
        ]
        for alg, label in display_order:
            r = col_map.get(alg)
            if r is None:
                continue
            rows.append({
                "algorithm": alg,
                "label": label,
                "n_complete": r.get("n_complete", ""),
                "n_total": r.get("n_total", "50"),
                "mean_bw": r.get("mean_bw", ""),
                "n_times_best": r.get("n_times_best", ""),
                "mean_rel_gap_vs_ipsns_pct": r.get("mean_rel_gain_ipsns_pct", ""),
                "note": "tournament-native; wins 45/50 overall" if alg == "drmaciver_fas" else "",
            })
    elif stats:
        # Minimal fallback from stats JSON
        pa_data = [
            ("ipsns_full", "IPSNS (ours)", stats["ipsns_global_best"],
             stats["ipsns_mean_backward_weight"], 0.0, ""),
            ("drmaciver_fas", "DRMaciver [external]", 45,
             round(stats["ipsns_mean_backward_weight"] * (1 + stats["drmaciver_mean_bw_gap_vs_ipsns_pct"] / 100), 1),
             stats["drmaciver_mean_bw_gap_vs_ipsns_pct"], "tournament-native; wins 45/50"),
        ]
        for alg, label, best, mbw, gap, note in pa_data:
            rows.append({
                "algorithm": alg,
                "label": label,
                "n_complete": 50,
                "n_total": 50,
                "mean_bw": round(mbw, 2),
                "n_times_best": best,
                "mean_rel_gap_vs_ipsns_pct": gap,
                "note": note,
            })

    # Add per-family block rows if we have stats
    if stats and rows:
        rows.append({"algorithm": "--- per-family breakdown ---",
                     "label": "", "n_complete": "", "n_total": "",
                     "mean_bw": "", "n_times_best": "", "mean_rel_gap_vs_ipsns_pct": "", "note": ""})
        for fam in stats.get("per_family", []):
            rows.append({
                "algorithm": f"ipsns_full [{fam['family']}]",
                "label": f"IPSNS (ours) — {fam['family']} family",
                "n_complete": fam["n_instances"],
                "n_total": fam["n_instances"],
                "mean_bw": fam["ipsns_mean_bw"],
                "n_times_best": fam["ipsns_global_best"],
                "mean_rel_gap_vs_ipsns_pct": "0.0",
                "note": f"DRMaciver best: {'24/25' if fam['family']=='SGB' else '6/10' if fam['family']=='IO' else '15/15'}",
            })

    fields = ["algorithm", "label", "n_complete", "n_total", "mean_bw",
              "n_times_best", "mean_rel_gap_vs_ipsns_pct", "note"]
    out = OUT_TABLES / "manuscript_table_lolib_dense.csv"
    _write_csv(out, rows, fields)
    used = str(src_csv.relative_to(ROOT)) if csv_rows else str(src_json.relative_to(ROOT))
    return {"source": used, "rows_written": len(rows)}


# ---------------------------------------------------------------------------
# Digest JSON + MD
# ---------------------------------------------------------------------------

PILLARS = [
    {
        "pillar": 1,
        "name": "Sparse weighted graph-benchmarks",
        "experiments": ["EXP1b", "EXP4"],
        "dataset": "alidasdan/graph-benchmarks (DIMACS .d)",
        "n_instances": {"EXP1b": 105, "EXP4": 97},
        "algorithms": ["IPSNS", "LR-TA", "WMSF", "DRMaciver", "igraph Eades",
                        "Weighted Eades", "Borda", "Random"],
        "main_metric": "backward_weight",
        "main_result": (
            "IPSNS achieves global minimum BW on 96/97 standard non-negative instances. "
            "DRMaciver (external) is closest competitor at +21.6% mean BW. "
            "IPSNS has 0 incumbent-protection violations on 105 EXP1b instances."
        ),
        "key_numbers": {
            "EXP1b_n_instances": 105,
            "EXP1b_incumbent_violations": 0,
            "EXP1b_ipsns_improves_lrta": 16,
            "EXP1b_ipsns_improves_wmsf": 36,
            "EXP1b_mean_rel_gain_pct": 0.42,
            "EXP4_n_standard": 97,
            "EXP4_ipsns_mean_bw": 37697.51,
            "EXP4_lrta_mean_bw": 38326.94,
            "EXP4_wmsf_mean_bw": 40005.06,
            "EXP4_drmaciver_mean_bw": 53173.38,
            "EXP4_ipsns_n_best": 96,
            "EXP4_drmaciver_rel_gap_pct": 21.61,
        },
        "claim_allowed": (
            "On standard non-negative sparse weighted graph-benchmarks, IPSNS outperforms "
            "all tested internal and external baselines and achieves the global minimum "
            "backward weight on 96/97 standard instances."
        ),
        "claim_not_allowed": (
            "IPSNS is universally state-of-the-art for all FAS/LOP instances."
        ),
    },
    {
        "pillar": 2,
        "name": "Exact small-instance validation",
        "experiments": ["EXP3"],
        "dataset": "alidasdan/graph-benchmarks, n<=20 subset",
        "n_instances": {"EXP3": 57},
        "algorithms": ["IPSNS", "LR-TA", "WMSF", "Exact DP"],
        "main_metric": "gap_from_optimal_pct",
        "main_result": (
            "IPSNS achieves exact optimality on 56/57 (98.2%) standard non-negative instances. "
            "Only near-miss: r20_60 (n=20), 0.0006% mean relative gap. "
            "LR-TA: 55/57 (96.5%), WMSF: 51/57 (89.5%)."
        ),
        "key_numbers": {
            "n_standard": 57,
            "ipsns_optimal": "56/57",
            "ipsns_pct_optimal": 98.2,
            "ipsns_mean_gap_pct": 0.0006,
            "lrta_optimal": "55/57",
            "lrta_pct_optimal": 96.5,
            "lrta_mean_gap_pct": 0.059,
            "wmsf_optimal": "51/57",
            "wmsf_pct_optimal": 89.5,
            "wmsf_mean_gap_pct": 0.0961,
        },
        "claim_allowed": (
            "On small non-negative instances where exact optimization is feasible, "
            "IPSNS is near-optimal (98.2% exact, mean gap 0.0006%)."
        ),
        "claim_not_allowed": (
            "IPSNS has an approximation guarantee or always reaches optimum."
        ),
    },
    {
        "pillar": 3,
        "name": "Ablation study",
        "experiments": ["EXP2"],
        "dataset": "alidasdan/graph-benchmarks (10 representative instances)",
        "n_instances": {"EXP2": 10},
        "algorithms": ["lr_no_addback", "lrta_full", "wmsf_seed", "best_seed_no_lns",
                        "ipsns_50iters", "ipsns_100iters", "ipsns_full", "ipsns_no_scc_priority"],
        "main_metric": "mean_backward_weight",
        "main_result": (
            "Add-back phase reduces mean BW by 5.9% (lr_no_addback 4525.1 -> lrta_full 4271.5). "
            "IPSNS full reduces further by 0.75% (lrta_full 4271.5 -> ipsns_full 4239.2). "
            "Convergence reached at 50 iterations (ipsns_50iters == ipsns_full on this subset). "
            "SCC priority has negligible effect on 10-instance subset."
        ),
        "key_numbers": {
            "lr_no_addback_mean_bw": 4525.1,
            "lrta_full_mean_bw": 4271.5,
            "wmsf_seed_mean_bw": 4332.5,
            "ipsns_full_mean_bw": 4239.2,
            "ipsns_no_scc_priority_mean_bw": 4239.1,
            "addback_reduction_pct": 5.9,
            "lns_further_reduction_pct": 0.75,
            "convergence_iters": 50,
        },
        "claim_allowed": (
            "EXP2 supports the contribution of the add-back phase (−5.9% BW) "
            "and incumbent-protected refinement (−0.75% further)."
        ),
        "claim_not_allowed": (
            "All design choices are universally optimal or generalize beyond the 10-instance subset."
        ),
    },
    {
        "pillar": 4,
        "name": "Dense LOLIB transfer test",
        "experiments": ["EXP5"],
        "dataset": "LOLIB 2010 (SGB n=75, IO n=44-79, RandA1 n=100/150/200)",
        "n_instances": {"EXP5": 50},
        "algorithms": ["IPSNS", "LR-TA", "WMSF", "DRMaciver", "igraph Eades",
                        "Weighted Eades", "Borda", "Random"],
        "main_metric": "backward_weight",
        "main_result": (
            "DRMaciver (tournament-native) achieves global best on 45/50 instances. "
            "IPSNS best on 5/50 (4 IO + 1 SGB). "
            "DRMaciver mean BW 571,688 vs IPSNS 582,354 (−3.88% advantage for DRMaciver). "
            "IPSNS retains 0 incumbent violations. "
            "Per-family: SGB DRMaciver 24/25, IO IPSNS 4/10 vs DRMaciver 6/10, RandA1 DRMaciver 15/15. "
            "Scope boundary: IPSNS is not a dense-native LOP algorithm."
        ),
        "key_numbers": {
            "n_instances": 50,
            "ipsns_n_best": 5,
            "drmaciver_n_best": 45,
            "ipsns_mean_bw": 582353.56,
            "drmaciver_mean_bw_gap_vs_ipsns_pct": -3.88,
            "incumbent_violations": 0,
            "SGB_ipsns_best": 1,
            "SGB_drmaciver_best": 24,
            "IO_ipsns_best": 4,
            "IO_drmaciver_best": 6,
            "RandA1_ipsns_best": 0,
            "RandA1_drmaciver_best": 15,
        },
        "claim_allowed": (
            "LOLIB shows IPSNS transfers reasonably as a general weighted digraph heuristic "
            "but is not a dense-native LOP state-of-the-art method. "
            "Incumbent protection holds. IPSNS is competitive on structured IO instances (4/10)."
        ),
        "claim_not_allowed": (
            "IPSNS beats dense-native ordering solvers on complete dense LOP benchmarks."
        ),
    },
]

SOURCE_FILES = {
    "EXP1b_stats": "experiments/exp1b_core_benchmark_full_wmsf_seed/summary/exp1b_core_benchmark_stats.json",
    "EXP1b_table": "experiments/exp1b_core_benchmark_full_wmsf_seed/tables/exp1b_core_benchmark_paper_summary.csv",
    "EXP2_stats":  "experiments/exp2_ablation/summary/exp2_ablation_stats.json",
    "EXP2_table":  "experiments/exp2_ablation/tables/exp2_ablation_summary.csv",
    "EXP3_stats":  "experiments/exp3_exact_small/summary/exp3_exact_stats.json",
    "EXP3_table":  "experiments/exp3_exact_small/tables/exp3_exact_summary.csv",
    "EXP4_stats":  "experiments/exp4_external_baselines/summary/exp4_external_stats.json",
    "EXP4_table":  "experiments/exp4_external_baselines/tables/exp4_external_paper_summary.csv",
    "EXP5_stats":  "experiments/exp5_lolib_dense/summary/exp5_lolib_stats.json",
    "EXP5_table":  "experiments/exp5_lolib_dense/tables/exp5_lolib_paper_summary.csv",
}


def build_digest():
    digest = {
        "generated_by": "experiments/combined/build_manuscript_results_digest.py",
        "date": "2026-06-06",
        "head_commit": "e5b5b96",
        "experiments_complete": ["EXP1b", "EXP2", "EXP3", "EXP4", "EXP5"],
        "n_instances_total": {
            "EXP1b": 105,
            "EXP2": 10,
            "EXP3_standard": 57,
            "EXP4_standard": 97,
            "EXP5": 50,
        },
        "source_files": SOURCE_FILES,
        "missing_or_unparsed_sources": [],
        "experimental_pillars": PILLARS,
        "strongest_allowed_claim": (
            "On standard non-negative sparse weighted directed graph benchmarks "
            "(alidasdan/graph-benchmarks), IPSNS achieves the global minimum backward weight "
            "on 96/97 instances, surpassing all tested external baselines including DRMaciver "
            "(+21.6% mean BW), with guaranteed non-worsening against both LR-TA and WMSF seeds."
        ),
        "strongest_not_allowed_claim": (
            "IPSNS is universally state-of-the-art for all weighted feedback arc set or "
            "linear ordering problem instances, including dense tournament benchmarks."
        ),
        "scope_boundary": (
            "All claims apply to non-negative-weight instances only. "
            "On dense LOLIB tournaments (EXP5), DRMaciver (tournament-native) outperforms IPSNS overall. "
            "IPSNS is designed for sparse directed graphs; EXP5 is a scope test, not the primary claim."
        ),
    }
    # Verify source files
    for key, rel in SOURCE_FILES.items():
        p = ROOT / rel
        if not p.exists():
            digest["missing_or_unparsed_sources"].append(rel)
    digest["missing_or_unparsed_sources"].extend(missing_or_unparsed)

    out_json = OUT_SUMMARY / "manuscript_results_digest.json"
    with open(out_json, "w") as f:
        json.dump(digest, f, indent=2)
    print(f"  wrote {out_json.relative_to(ROOT)}")

    # Markdown digest
    lines = [
        "# Manuscript Results Digest",
        "",
        f"**Generated:** 2026-06-06  ",
        f"**HEAD commit:** e5b5b96  ",
        f"**Experiments complete:** EXP1b, EXP2, EXP3, EXP4, EXP5",
        "",
        "---",
        "",
        "## Experimental Pillars",
        "",
    ]
    for p in PILLARS:
        lines += [
            f"### Pillar {p['pillar']}: {p['name']}",
            "",
            f"**Experiments:** {', '.join(p['experiments'])}  ",
            f"**Dataset:** {p['dataset']}  ",
            f"**N instances:** {p['n_instances']}  ",
            "",
            f"**Main result:** {p['main_result']}",
            "",
            f"**Allowed claim:** {p['claim_allowed']}",
            "",
            f"**Not allowed:** {p['claim_not_allowed']}",
            "",
        ]

    lines += [
        "---",
        "",
        "## Strongest Allowed Claim",
        "",
        f"> {digest['strongest_allowed_claim']}",
        "",
        "## Strongest Not-Allowed Claim",
        "",
        f"> {digest['strongest_not_allowed_claim']}",
        "",
        "## Scope Boundary",
        "",
        f"> {digest['scope_boundary']}",
        "",
        "---",
        "",
        "## Source Files",
        "",
    ]
    for key, rel in SOURCE_FILES.items():
        exists = "✓" if (ROOT / rel).exists() else "MISSING"
        lines.append(f"- `{rel}` [{exists}]")
    lines.append("")
    if digest["missing_or_unparsed_sources"]:
        lines += ["## Missing/Unparsed Sources", ""]
        for s in digest["missing_or_unparsed_sources"]:
            lines.append(f"- `{s}`")
        lines.append("")

    out_md = OUT_SUMMARY / "manuscript_results_digest.md"
    out_md.write_text("\n".join(lines))
    print(f"  wrote {out_md.relative_to(ROOT)}")
    return digest


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("Building manuscript results digest...")
    results = {}

    print("\n[Table 1] Core sparse benchmark (EXP1b)")
    results["table_core_sparse"] = build_table_core_sparse()

    print("\n[Table 2] External sparse comparison (EXP4)")
    results["table_external_sparse"] = build_table_external_sparse()

    print("\n[Table 3] Exact small-instance validation (EXP3)")
    results["table_exact_small"] = build_table_exact_small()

    print("\n[Table 4] Ablation (EXP2)")
    results["table_ablation"] = build_table_ablation()

    print("\n[Table 5] LOLIB dense transfer test (EXP5)")
    results["table_lolib_dense"] = build_table_lolib_dense()

    print("\n[Digest] Building JSON + MD digest")
    digest = build_digest()
    results["missing_or_unparsed"] = digest["missing_or_unparsed_sources"]

    print("\nDone.")
    if results["missing_or_unparsed"]:
        print("WARNING: missing/unparsed sources:")
        for s in results["missing_or_unparsed"]:
            print(f"  {s}")
        sys.exit(1)
    else:
        print("All source files found.")


if __name__ == "__main__":
    main()
