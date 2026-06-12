"""EXP5 LOLIB Dense Benchmark — Postprocessor.

Reads experiments/exp5_lolib_dense/summary/exp5_lolib_raw_summary.csv and
produces:
  tables/exp5_lolib_paper_summary.csv
  tables/exp5_lolib_wide_summary.csv
  summary/exp5_lolib_stats.json
  summary/exp5_lolib_summary.md

Usage:
    python postprocess_exp5_lolib.py
"""
import csv
import json
import os
import sys
from collections import defaultdict

import pandas as pd
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SUMMARY_IN = os.path.join(HERE, "summary", "exp5_lolib_raw_summary.csv")
TABLES_DIR = os.path.join(HERE, "tables")
SUMMARY_DIR = os.path.join(HERE, "summary")

os.makedirs(TABLES_DIR, exist_ok=True)

ALG_ORDER = [
    "ipsns_full",
    "lrta_full",
    "wmsf_seed",
    "drmaciver_fas",
    "igraph_approx_eades",
    "weighted_eades",
    "borda_net_score",
    "random_multistart",
]

FAMILY_ORDER = ["SGB", "IO", "RandA1"]


def load_raw(path):
    df = pd.read_csv(path)
    df = df.drop_duplicates(subset=["instance", "algorithm"], keep="first").copy()
    df["backward_weight"] = pd.to_numeric(df["backward_weight"], errors="coerce")
    df["forward_weight"] = pd.to_numeric(df["forward_weight"], errors="coerce")
    df["forward_ratio"] = pd.to_numeric(df["forward_ratio"], errors="coerce")
    df["runtime"] = pd.to_numeric(df["runtime"], errors="coerce")
    df["n"] = pd.to_numeric(df["n"], errors="coerce")
    return df


def compute_global_best(df):
    """For each instance, mark which algorithm(s) achieve the minimum backward_weight."""
    ok = df[df["status"] == "ok"].copy()
    best_bw = ok.groupby("instance")["backward_weight"].min()
    ok["is_global_best"] = ok.apply(
        lambda r: r["backward_weight"] <= best_bw[r["instance"]] + 1e-9, axis=1
    )
    return ok


def main():
    if not os.path.exists(SUMMARY_IN):
        print(f"ERROR: {SUMMARY_IN} not found. Run the benchmark first.")
        sys.exit(1)

    df = load_raw(SUMMARY_IN)
    print(f"Loaded {len(df)} rows, {df['instance'].nunique()} instances, "
          f"{df['algorithm'].nunique()} algorithms")

    ok = compute_global_best(df)
    total_instances = df["instance"].nunique()
    ok_instances = ok["instance"].nunique()

    # Per-algorithm statistics (over completed instances only)
    alg_stats = []
    for alg in ALG_ORDER:
        sub = ok[ok["algorithm"] == alg]
        if len(sub) == 0:
            continue
        n_complete = len(sub)
        n_best = sub["is_global_best"].sum()
        mean_bw = sub["backward_weight"].mean()
        median_bw = sub["backward_weight"].median()
        mean_fw = sub["forward_weight"].mean()
        mean_ratio = sub["forward_ratio"].mean()
        mean_rt = sub["runtime"].mean()
        n_errors = len(df[(df["algorithm"] == alg) & (df["status"] != "ok")])

        # Incumbent protection check (IPSNS ≤ both seeds)
        if alg == "ipsns_full":
            ipsns_bw = sub.set_index("instance")["backward_weight"]
            lrta_bw = ok[ok["algorithm"] == "lrta_full"].set_index("instance")["backward_weight"]
            wmsf_bw = ok[ok["algorithm"] == "wmsf_seed"].set_index("instance")["backward_weight"]
            common = ipsns_bw.index.intersection(lrta_bw.index).intersection(wmsf_bw.index)
            n_violates_lrta = (ipsns_bw[common] > lrta_bw[common] + 1e-9).sum()
            n_violates_wmsf = (ipsns_bw[common] > wmsf_bw[common] + 1e-9).sum()
        else:
            n_violates_lrta = n_violates_wmsf = 0

        alg_stats.append({
            "algorithm": alg,
            "n_complete": n_complete,
            "n_errors": n_errors,
            "n_global_best": int(n_best),
            "n_instances": total_instances,
            "mean_backward_weight": round(mean_bw, 4) if not np.isnan(mean_bw) else "",
            "median_backward_weight": round(median_bw, 4) if not np.isnan(median_bw) else "",
            "mean_forward_weight": round(mean_fw, 4) if not np.isnan(mean_fw) else "",
            "mean_forward_ratio": round(mean_ratio, 6) if not np.isnan(mean_ratio) else "",
            "mean_runtime_s": round(mean_rt, 4) if not np.isnan(mean_rt) else "",
            "incumbent_violations_vs_lrta": int(n_violates_lrta),
            "incumbent_violations_vs_wmsf": int(n_violates_wmsf),
        })

    paper_csv = os.path.join(TABLES_DIR, "exp5_lolib_paper_summary.csv")
    with open(paper_csv, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(alg_stats[0].keys()))
        writer.writeheader()
        writer.writerows(alg_stats)
    print(f"Paper summary: {paper_csv}")

    # Wide format: instances × algorithms
    wide = ok.pivot_table(
        index=["instance", "family", "n"],
        columns="algorithm",
        values="backward_weight",
        aggfunc="first",
    ).reset_index()
    wide_csv = os.path.join(TABLES_DIR, "exp5_lolib_wide_summary.csv")
    wide.to_csv(wide_csv, index=False)
    print(f"Wide summary: {wide_csv}")

    # Per-family breakdown
    family_rows = []
    for family in FAMILY_ORDER:
        fdf = ok[ok["family"] == family]
        if len(fdf) == 0:
            continue
        n_inst = fdf["instance"].nunique()
        ipsns = fdf[fdf["algorithm"] == "ipsns_full"]
        n_best = ipsns["is_global_best"].sum() if len(ipsns) > 0 else 0
        mean_bw_ipsns = ipsns["backward_weight"].mean() if len(ipsns) > 0 else float("nan")
        family_rows.append({
            "family": family,
            "n_instances": n_inst,
            "ipsns_global_best": int(n_best),
            "ipsns_mean_bw": round(mean_bw_ipsns, 2) if not np.isnan(mean_bw_ipsns) else "",
        })

    # Stats JSON
    ipsns_stats = next((s for s in alg_stats if s["algorithm"] == "ipsns_full"), {})
    drmaciver_stats = next((s for s in alg_stats if s["algorithm"] == "drmaciver_fas"), {})

    ipsns_bw = ok[ok["algorithm"] == "ipsns_full"]["backward_weight"]
    dr_bw = ok[ok["algorithm"] == "drmaciver_fas"]["backward_weight"]
    common_idx = ok[ok["algorithm"] == "ipsns_full"].set_index("instance").index \
        .intersection(ok[ok["algorithm"] == "drmaciver_fas"].set_index("instance").index)
    if len(common_idx) > 0:
        ipsns_bw_c = ok[(ok["algorithm"] == "ipsns_full") & (ok["instance"].isin(common_idx))]\
            .set_index("instance")["backward_weight"]
        dr_bw_c = ok[(ok["algorithm"] == "drmaciver_fas") & (ok["instance"].isin(common_idx))]\
            .set_index("instance")["backward_weight"]
        nonzero = ipsns_bw_c[ipsns_bw_c > 0]
        if len(nonzero) > 0:
            gaps = (dr_bw_c[nonzero.index] - nonzero) / nonzero * 100
            mean_gap_drmaciver_vs_ipsns = round(gaps.mean(), 2)
        else:
            mean_gap_drmaciver_vs_ipsns = None
    else:
        mean_gap_drmaciver_vs_ipsns = None

    stats = {
        "n_instances_total": total_instances,
        "n_instances_with_any_ok": ok_instances,
        "algorithms_run": ALG_ORDER,
        "ipsns_global_best": ipsns_stats.get("n_global_best", 0),
        "ipsns_incumbent_violations_vs_lrta": ipsns_stats.get("incumbent_violations_vs_lrta", ""),
        "ipsns_incumbent_violations_vs_wmsf": ipsns_stats.get("incumbent_violations_vs_wmsf", ""),
        "ipsns_mean_backward_weight": ipsns_stats.get("mean_backward_weight", ""),
        "ipsns_mean_forward_ratio": ipsns_stats.get("mean_forward_ratio", ""),
        "drmaciver_mean_bw_gap_vs_ipsns_pct": mean_gap_drmaciver_vs_ipsns,
        "per_family": family_rows,
    }

    stats_json = os.path.join(SUMMARY_DIR, "exp5_lolib_stats.json")
    with open(stats_json, "w") as f:
        json.dump(stats, f, indent=2)
    print(f"Stats JSON: {stats_json}")

    # Narrative Markdown
    lines = [
        "# EXP5 LOLIB Dense Benchmark — Results",
        "",
        f"**Instances:** {total_instances} total ({ok_instances} with at least one successful run)",
        f"**Families:** {', '.join(FAMILY_ORDER)}",
        f"**Algorithms:** {', '.join(ALG_ORDER)}",
        "",
        "## Per-Algorithm Summary",
        "",
        "| Algorithm | Completed | Global Best | Mean BW | Mean Forward Ratio | Mean RT (s) |",
        "|---|---|---|---|---|---|",
    ]
    for s in alg_stats:
        lines.append(
            f"| **{s['algorithm']}** | {s['n_complete']}/{total_instances} | "
            f"{s['n_global_best']}/{total_instances} | {s['mean_backward_weight']} | "
            f"{s['mean_forward_ratio']} | {s['mean_runtime_s']} |"
        )

    lines += [
        "",
        "## Incumbent Protection",
        "",
        f"IPSNS violations vs LR-TA: **{ipsns_stats.get('incumbent_violations_vs_lrta', 'N/A')}**  ",
        f"IPSNS violations vs WMSF:  **{ipsns_stats.get('incumbent_violations_vs_wmsf', 'N/A')}**",
        "",
        "## Per-Family Breakdown",
        "",
        "| Family | Instances | IPSNS Global Best | IPSNS Mean BW |",
        "|---|---|---|---|",
    ]
    for fr in family_rows:
        lines.append(
            f"| {fr['family']} | {fr['n_instances']} | "
            f"{fr['ipsns_global_best']}/{fr['n_instances']} | {fr['ipsns_mean_bw']} |"
        )

    if mean_gap_drmaciver_vs_ipsns is not None:
        lines += [
            "",
            "## IPSNS vs DRMacIver",
            "",
            f"DRMacIver mean BW gap vs IPSNS: **+{mean_gap_drmaciver_vs_ipsns:.2f}%**",
        ]

    lines += ["", f"Generated by `postprocess_exp5_lolib.py`. Source: `{SUMMARY_IN}`"]

    summary_md = os.path.join(SUMMARY_DIR, "exp5_lolib_summary.md")
    with open(summary_md, "w") as f:
        f.write("\n".join(lines) + "\n")
    print(f"Narrative summary: {summary_md}")

    print("\n=== Key Results ===")
    for s in alg_stats[:4]:
        print(f"  {s['algorithm']:30s}: best={s['n_global_best']:3d}/{total_instances} "
              f"mean_bw={s['mean_backward_weight']}")


if __name__ == "__main__":
    main()
