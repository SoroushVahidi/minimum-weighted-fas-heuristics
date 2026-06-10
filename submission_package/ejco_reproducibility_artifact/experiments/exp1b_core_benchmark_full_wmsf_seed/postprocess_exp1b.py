#!/usr/bin/env python3
"""
Postprocessing for EXP1b: pivot long-format summary to wide, compute stats,
check external incumbent-protection violations.
"""
from pathlib import Path
import pandas as pd
import numpy as np
import json

EXP = Path(__file__).parent
ROOT = EXP.parent.parent

summary_dir = EXP / "summary"
tables_dir  = EXP / "tables"
raw_dir     = EXP / "raw" / "full_benchmark"
summary_dir.mkdir(parents=True, exist_ok=True)
tables_dir.mkdir(parents=True, exist_ok=True)

# ── Locate raw summary CSV ────────────────────────────────────────────────────
candidates = sorted(raw_dir.rglob("summary.csv"))
if not candidates:
    raise FileNotFoundError(f"No summary.csv found under {raw_dir}")
src = candidates[0]
print(f"Loading raw summary: {src}")
df = pd.read_csv(src)
print(f"  Rows: {len(df)}, columns: {df.columns.tolist()}")

# Save as canonical raw summary
raw_summary_path = summary_dir / "exp1b_raw_summary.csv"
df.to_csv(raw_summary_path, index=False)
print(f"  Raw summary saved: {raw_summary_path}")

# ── Dedup: instances run twice from overlapping lists ─────────────────────────
before = len(df)
df = df.drop_duplicates(subset=["instance", "algorithm"], keep="first")
print(f"  After dedup: {len(df)} rows (dropped {before - len(df)} duplicates)")

# ── Per-algorithm run counts ──────────────────────────────────────────────────
algo_counts = df["algorithm"].value_counts().to_dict()
n_lrta  = algo_counts.get("lrta", 0)
n_wmsf  = algo_counts.get("wmsf", 0)
n_ipsns = algo_counts.get("ipsns", 0)
print(f"  lrta={n_lrta}  wmsf={n_wmsf}  ipsns={n_ipsns}")

# ── Pivot to wide ─────────────────────────────────────────────────────────────
# Graph properties come from the lrta row (same graph for all three)
graph_cols = ["n", "m", "total_weight"]
graph = (
    df[df["algorithm"] == "lrta"][["instance"] + graph_cols]
    .drop_duplicates("instance")
    .set_index("instance")
)

wide = graph.copy()
for algo in ["lrta", "wmsf", "ipsns"]:
    sub = df[df["algorithm"] == algo].drop_duplicates("instance").set_index("instance")
    wide[f"{algo}_bw"]    = sub["backward_weight"]
    wide[f"{algo}_fw"]    = sub["forward_weight"]
    wide[f"{algo}_fr"]    = sub.get("forward_ratio", pd.Series(dtype=float))
    wide[f"{algo}_time"]  = sub["time_sec"]
    wide[f"{algo}_error"] = sub["error"] if "error" in sub.columns else pd.NA

wide = wide.reset_index()

# ── Comparison columns ────────────────────────────────────────────────────────
wide["best_seed_bw"]            = wide[["lrta_bw", "wmsf_bw"]].min(axis=1)
wide["ipsns_improves_lrta"]     = wide["ipsns_bw"] < wide["lrta_bw"]
wide["ipsns_improves_wmsf"]     = wide["ipsns_bw"] < wide["wmsf_bw"]
wide["ipsns_no_worse_than_lrta"] = wide["ipsns_bw"] <= wide["lrta_bw"] + 1e-9
wide["ipsns_no_worse_than_wmsf"] = wide["ipsns_bw"] <= wide["wmsf_bw"] + 1e-9
wide["ipsns_no_worse_than_both"] = wide["ipsns_bw"] <= wide["best_seed_bw"] + 1e-9
wide["ipsns_gain_over_best_seed"] = wide["best_seed_bw"] - wide["ipsns_bw"]
wide["ipsns_rel_gain_over_best_seed"] = (
    wide["ipsns_gain_over_best_seed"]
    / wide["best_seed_bw"].replace(0, np.nan)
)

# ── Complete triplets (all three algorithms ran without error) ─────────────────
has_all = wide["lrta_bw"].notna() & wide["wmsf_bw"].notna() & wide["ipsns_bw"].notna()
n_complete = int(has_all.sum())
complete = wide[has_all]

# ── External violations ───────────────────────────────────────────────────────
violations = complete[~complete["ipsns_no_worse_than_both"]]
n_violations = len(violations)
if n_violations > 0:
    viol_path = summary_dir / "exp1b_external_violations.csv"
    violations.to_csv(viol_path, index=False)
    print(f"  VIOLATIONS ({n_violations}): saved to {viol_path}")
else:
    print(f"  No external violations — IPSNS <= min(LRTA,WMSF) for all {n_complete} complete instances.")

# ── Error count (non-empty, non-NaN) ──────────────────────────────────────────
n_nonempty_errors = int(df["error"].notna().sum()) if "error" in df.columns else 0

# ── Runtime aggregates ────────────────────────────────────────────────────────
rt = df.groupby("algorithm")["time_sec"].agg(["sum", "mean"]).to_dict()
total_rt  = {k: round(float(rt["sum"][k]), 4)  for k in rt["sum"]}
mean_rt   = {k: round(float(rt["mean"][k]), 4) for k in rt["mean"]}

# ── Stats JSON ────────────────────────────────────────────────────────────────
nonzero_seed = complete["best_seed_bw"] > 0
stats = {
    "n_instances":                   int(wide["instance"].nunique()),
    "n_complete_triplets":           n_complete,
    "n_lrta_runs":                   n_lrta,
    "n_wmsf_runs":                   n_wmsf,
    "n_ipsns_runs":                  n_ipsns,
    "n_nonempty_errors":             n_nonempty_errors,
    "ipsns_improves_lrta":           int(complete["ipsns_improves_lrta"].sum()),
    "ipsns_improves_wmsf":           int(complete["ipsns_improves_wmsf"].sum()),
    "ipsns_no_worse_than_lrta_count": int(complete["ipsns_no_worse_than_lrta"].sum()),
    "ipsns_no_worse_than_wmsf_count": int(complete["ipsns_no_worse_than_wmsf"].sum()),
    "incumbent_protection_violations_external": n_violations,
    "mean_gain_over_best_seed":      round(float(complete.loc[nonzero_seed, "ipsns_gain_over_best_seed"].mean(skipna=True)), 4),
    "median_gain_over_best_seed":    round(float(complete.loc[nonzero_seed, "ipsns_gain_over_best_seed"].median(skipna=True)), 4),
    "mean_relative_gain_over_best_seed":   round(float(complete.loc[nonzero_seed, "ipsns_rel_gain_over_best_seed"].mean(skipna=True)), 6),
    "median_relative_gain_over_best_seed": round(float(complete.loc[nonzero_seed, "ipsns_rel_gain_over_best_seed"].median(skipna=True)), 6),
    "total_runtime_by_algorithm":    total_rt,
    "mean_runtime_by_algorithm":     mean_rt,
}

stats_path = summary_dir / "exp1b_core_benchmark_stats.json"
stats_path.write_text(json.dumps(stats, indent=2))
print(f"\nStats JSON: {stats_path}")
print(json.dumps(stats, indent=2))

# ── Wide summary CSV ──────────────────────────────────────────────────────────
wide_path = tables_dir / "exp1b_core_benchmark_wide_summary.csv"
wide.to_csv(wide_path, index=False)
print(f"\nWide summary: {wide_path}  ({len(wide)} rows x {len(wide.columns)} cols)")

# ── Paper summary CSV (complete triplets only, key columns) ──────────────────
paper_cols = [
    "instance", "n", "m", "total_weight",
    "lrta_bw", "wmsf_bw", "ipsns_bw",
    "lrta_fw", "wmsf_fw", "ipsns_fw",
    "lrta_fr", "wmsf_fr", "ipsns_fr",
    "lrta_time", "wmsf_time", "ipsns_time",
    "best_seed_bw",
    "ipsns_improves_lrta", "ipsns_improves_wmsf",
    "ipsns_no_worse_than_lrta", "ipsns_no_worse_than_wmsf", "ipsns_no_worse_than_both",
    "ipsns_gain_over_best_seed", "ipsns_rel_gain_over_best_seed",
]
paper_cols = [c for c in paper_cols if c in wide.columns]
paper_df = complete[paper_cols].copy()
paper_path = tables_dir / "exp1b_core_benchmark_paper_summary.csv"
paper_df.to_csv(paper_path, index=False)
print(f"Paper summary: {paper_path}  ({len(paper_df)} rows x {len(paper_df.columns)} cols)")

# ── Markdown summary ──────────────────────────────────────────────────────────
md = ["# EXP1b Core Benchmark Summary (Full WMSF Seed)", ""]
for k, v in stats.items():
    md.append(f"- **{k}**: {v}")
md += [
    "",
    f"Raw summary (long):  `{raw_summary_path.relative_to(ROOT)}`",
    f"Wide summary:        `{wide_path.relative_to(ROOT)}`",
    f"Paper summary:       `{paper_path.relative_to(ROOT)}`",
    f"Stats JSON:          `{stats_path.relative_to(ROOT)}`",
]
(summary_dir / "exp1b_core_benchmark_summary.md").write_text("\n".join(md))
print(f"Summary MD: {summary_dir / 'exp1b_core_benchmark_summary.md'}")

print("\nPostprocessing complete.")
