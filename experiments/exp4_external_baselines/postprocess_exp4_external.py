"""
Postprocess EXP4 external baselines results.

Reads: experiments/exp4_external_baselines/summary/exp4_raw_summary.csv
Produces:
  tables/exp4_external_wide_summary.csv
  tables/exp4_external_paper_summary.csv
  summary/exp4_external_stats.json
  summary/exp4_external_summary.md

Usage:
    python postprocess_exp4_external.py
    python postprocess_exp4_external.py --summary path/to/exp4_raw_summary.csv
"""
import argparse
import json
import os
import sys

import pandas as pd
import numpy as np

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
EXP4 = os.path.dirname(__file__)

NEGATIVE_WEIGHT_INSTANCES = {"k3_3", "ku", "peterson", "peterson1", "peterson2"}

ALGO_ORDER = [
    "ipsns_full", "lrta_full", "wmsf_seed",
    "borda_net_score", "weighted_eades", "random_multistart",
    "igraph_approx_eades", "drmaciver_fas",
]

SOURCE_TYPES = {
    "ipsns_full": "in-repo (ours)",
    "lrta_full": "in-repo (ours)",
    "wmsf_seed": "in-repo (ours)",
    "borda_net_score": "in-repo baseline",
    "weighted_eades": "in-repo baseline",
    "random_multistart": "in-repo baseline",
    "igraph_approx_eades": "external wrapper",
    "drmaciver_fas": "external wrapper",
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--summary",
        default=os.path.join(EXP4, "summary", "exp4_raw_summary.csv"),
    )
    args = ap.parse_args()

    if not os.path.exists(args.summary):
        print(f"Summary CSV not found: {args.summary}")
        print("Run the benchmark first.")
        sys.exit(1)

    df = pd.read_csv(args.summary)
    df["instance_name"] = df["instance"].apply(
        lambda x: os.path.splitext(os.path.basename(str(x)))[0]
    )

    # Flag negative-weight and unavailable
    df["is_negative_weight"] = df["instance_name"].isin(NEGATIVE_WEIGHT_INSTANCES)
    df["is_ok"] = df["status"].fillna("").str.lower().isin(["ok", ""])
    df.loc[df["backward_weight"].isna(), "is_ok"] = False

    os.makedirs(os.path.join(EXP4, "tables"), exist_ok=True)

    # ---- Wide summary (one row per instance, one col per algorithm) ----
    pivot_bw = df[df["is_ok"]].pivot_table(
        index="instance_name", columns="algorithm", values="backward_weight"
    )
    pivot_rt = df[df["is_ok"]].pivot_table(
        index="instance_name", columns="algorithm", values="runtime"
    )
    pivot_bw.columns = [f"bw_{c}" for c in pivot_bw.columns]
    pivot_rt.columns = [f"rt_{c}" for c in pivot_rt.columns]
    wide = pd.concat([pivot_bw, pivot_rt], axis=1).reset_index()
    wide_path = os.path.join(EXP4, "tables", "exp4_external_wide_summary.csv")
    wide.to_csv(wide_path, index=False)
    print(f"Wide summary: {wide_path}")

    # ---- Paper summary ----
    # Filter: standard non-negative instances only
    df_std = df[~df["is_negative_weight"]].copy()
    df_ok = df_std[df_std["is_ok"]].copy()

    ipsns_bw = df_ok[df_ok["algorithm"] == "ipsns_full"].set_index("instance_name")["backward_weight"]

    rows = []
    for alg in ALGO_ORDER:
        sub = df_ok[df_ok["algorithm"] == alg]
        n_complete = len(sub)
        n_total = df_std["instance_name"].nunique()

        # unavailable count
        n_unavail = df_std[
            (df_std["algorithm"] == alg) &
            df_std["status"].fillna("").str.contains("unavailable|not_installed", case=False)
        ].shape[0]

        # error count
        n_err = df_std[
            (df_std["algorithm"] == alg) &
            ~df_std["is_ok"]
        ].shape[0]

        if n_complete == 0:
            rows.append({
                "algorithm": alg,
                "source_type": SOURCE_TYPES.get(alg, ""),
                "n_complete": 0,
                "n_total": n_total,
                "n_unavailable": n_unavail,
                "n_errors": n_err,
                "mean_bw": "",
                "median_bw": "",
                "mean_fw_ratio": "",
                "mean_runtime_s": "",
                "n_times_best": "",
                "n_times_ipsns_equal": "",
                "n_ipsns_improves": "",
                "mean_abs_gain_ipsns": "",
                "mean_rel_gain_ipsns_pct": "",
            })
            continue

        sub_idx = sub.set_index("instance_name")
        common = sub_idx.index.intersection(ipsns_bw.index)
        sub_common = sub_idx.loc[common]
        ipsns_common = ipsns_bw.loc[common]

        # best = minimum bw across all algorithms on same instance
        best_bw_per_inst = df_ok.groupby("instance_name")["backward_weight"].min()
        n_best = int((
            sub_idx["backward_weight"].reindex(best_bw_per_inst.index) <=
            best_bw_per_inst + 1e-9
        ).sum())

        n_ipsns_equal = int((
            abs(sub_common["backward_weight"] - ipsns_common) <= 1e-9
        ).sum())

        n_ipsns_improves = int((
            ipsns_common < sub_common["backward_weight"] - 1e-9
        ).sum())

        abs_gain = sub_common["backward_weight"] - ipsns_common
        mean_abs = float(abs_gain.mean())

        # relative gain: only where denominator > 0
        denom = sub_common["backward_weight"]
        rel_mask = denom > 1e-9
        mean_rel = float(
            (abs_gain[rel_mask] / denom[rel_mask] * 100).mean()
        ) if rel_mask.any() else 0.0

        rows.append({
            "algorithm": alg,
            "source_type": SOURCE_TYPES.get(alg, ""),
            "n_complete": n_complete,
            "n_total": n_total,
            "n_unavailable": n_unavail,
            "n_errors": n_err,
            "mean_bw": round(float(sub["backward_weight"].mean()), 4),
            "median_bw": round(float(sub["backward_weight"].median()), 4),
            "mean_fw_ratio": round(float(sub["forward_ratio"].mean()), 6) if "forward_ratio" in sub else "",
            "mean_runtime_s": round(float(sub["runtime"].mean()), 4) if "runtime" in sub else "",
            "n_times_best": n_best,
            "n_times_ipsns_equal": n_ipsns_equal,
            "n_ipsns_improves": n_ipsns_improves,
            "mean_abs_gain_ipsns": round(mean_abs, 4),
            "mean_rel_gain_ipsns_pct": round(mean_rel, 4),
        })

    paper_df = pd.DataFrame(rows)
    paper_path = os.path.join(EXP4, "tables", "exp4_external_paper_summary.csv")
    paper_df.to_csv(paper_path, index=False)
    print(f"Paper summary: {paper_path}")

    # ---- Stats JSON ----
    ipsns_row = paper_df[paper_df["algorithm"] == "ipsns_full"].iloc[0] if len(paper_df) > 0 else {}
    stats = {
        "n_instances_total": int(df["instance_name"].nunique()),
        "n_negative_weight": int(df[df["is_negative_weight"]]["instance_name"].nunique()),
        "negative_weight_instances": sorted(NEGATIVE_WEIGHT_INSTANCES),
        "n_standard": int(df[~df["is_negative_weight"]]["instance_name"].nunique()),
        "algorithms_run": ALGO_ORDER,
        "unavailable_algorithms": [
            alg for alg in ALGO_ORDER
            if df[df["algorithm"] == alg]["status"].fillna("").str.contains(
                "unavailable", case=False
            ).any()
        ],
        "per_algorithm": {
            r["algorithm"]: {
                "n_complete": r["n_complete"],
                "mean_bw": r["mean_bw"],
                "mean_rel_gain_ipsns_pct": r["mean_rel_gain_ipsns_pct"],
            }
            for r in rows
        },
    }
    stats_path = os.path.join(EXP4, "summary", "exp4_external_stats.json")
    with open(stats_path, "w") as f:
        json.dump(stats, f, indent=2)
    print(f"Stats JSON: {stats_path}")

    # ---- Summary Markdown ----
    md_lines = [
        "# EXP4 External Baselines Summary",
        "",
        f"Generated from: `{os.path.basename(args.summary)}`  ",
        f"Total instances: {stats['n_instances_total']}  ",
        f"Standard (non-negative): {stats['n_standard']}  ",
        f"Negative-weight (excluded): {', '.join(NEGATIVE_WEIGHT_INSTANCES)}  ",
        "",
        "## Availability",
        "",
    ]
    for alg in ALGO_ORDER:
        n_un = next((r["n_unavailable"] for r in rows if r["algorithm"] == alg), 0)
        ok_str = "Unavailable" if n_un > 0 else "Available"
        md_lines.append(f"- **{alg}**: {ok_str}")
    md_lines += [
        "",
        "## Per-Algorithm Results (Standard Instances)",
        "",
        "| Algorithm | Complete | Mean BW | Median BW | Mean FW Ratio | Mean RT (s) | N Best | IPSNS Improves | Mean Rel Gain (%) |",
        "|-----------|----------|---------|-----------|---------------|-------------|--------|----------------|-------------------|",
    ]
    for r in rows:
        md_lines.append(
            f"| {r['algorithm']} | {r['n_complete']}/{r['n_total']} "
            f"| {r['mean_bw']} | {r['median_bw']} "
            f"| {r['mean_fw_ratio']} | {r['mean_runtime_s']} "
            f"| {r['n_times_best']} | {r['n_ipsns_improves']} "
            f"| {r['mean_rel_gain_ipsns_pct']} |"
        )
    md_lines += [
        "",
        "## Notes",
        "",
        "- **IPSNS improves**: number of instances where IPSNS backward weight < algorithm backward weight.",
        "- **Mean rel gain**: mean (alg_bw - ipsns_bw) / alg_bw × 100% (only where alg_bw > 0).",
        "- **N Best**: number of instances where this algorithm achieves the minimum backward weight.",
        "- Negative-weight instances excluded from all statistics above.",
        "- `fas_smartAE` and `R_igraph_eades` not run: see external_access_report.md.",
        "",
    ]
    md_path = os.path.join(EXP4, "summary", "exp4_external_summary.md")
    with open(md_path, "w") as f:
        f.write("\n".join(md_lines) + "\n")
    print(f"Summary MD: {md_path}")
    print("Postprocess complete.")


if __name__ == "__main__":
    main()
