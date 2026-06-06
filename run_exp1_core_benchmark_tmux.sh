#!/usr/bin/env bash
set -u
set -o pipefail

cd ~/minimum-weighted-fas-heuristics

EXP_DIR="experiments/exp1_core_benchmark"
LOG="$EXP_DIR/exp1_core_benchmark.log"

mkdir -p "$EXP_DIR"/{logs,configs,raw,summary,tables}

exec > >(tee -a "$LOG") 2>&1

echo "============================================================"
echo "EXP1 CORE BENCHMARK FOR MERGED MWFAS PAPER"
echo "Started: $(date)"
echo "Repository: $(pwd)"
echo "============================================================"
echo

echo "=== Git state ==="
git status
git rev-parse HEAD
git log -1 --oneline
echo

echo "=== Pull latest repo ==="
git pull || true
echo

echo "=== System information ==="
hostname || true
uname -a || true
lscpu | head -40 || true
free -h || true
echo

echo "=== Python environment ==="
which python || true
python --version || true
python -m pip --version || true
echo

echo "=== Install package and requirements ==="
python -m pip install -e .
python -m pip install -r requirements.txt
python -m pip freeze > "$EXP_DIR/configs/pip_freeze.txt"
echo

echo "=== Locate benchmark instances ==="
if [ -f configs/benchmark_instances_found_all.txt ]; then
  cp configs/benchmark_instances_found_all.txt "$EXP_DIR/configs/benchmark_instances_found_all.txt"
else
  find ~ -name "*.d" | sort > "$EXP_DIR/configs/benchmark_instances_found_all.txt" || true
fi

COUNT=$(wc -l < "$EXP_DIR/configs/benchmark_instances_found_all.txt" || echo 0)
echo "Initial .d instance count: $COUNT"

if [ "$COUNT" -lt 3 ]; then
  echo "Fewer than 3 .d files found; cloning graph-benchmarks."
  mkdir -p ~/benchmark_sources
  cd ~/benchmark_sources
  if [ ! -d graph-benchmarks ]; then
    git clone https://github.com/alidasdan/graph-benchmarks.git
  fi
  cd ~/minimum-weighted-fas-heuristics
  find ~/benchmark_sources/graph-benchmarks -name "*.d" | sort > "$EXP_DIR/configs/benchmark_instances_found_all.txt"
fi

COUNT=$(wc -l < "$EXP_DIR/configs/benchmark_instances_found_all.txt" || echo 0)
echo "Final .d instance count: $COUNT"
echo "First 30 instances:"
head -30 "$EXP_DIR/configs/benchmark_instances_found_all.txt"
echo

echo "=== Save scripts/config snapshots ==="
cp scripts/reproduce_all.py "$EXP_DIR/configs/reproduce_all.py.snapshot" || true
cp scripts/run_lrta.py "$EXP_DIR/configs/run_lrta.py.snapshot" || true
cp scripts/run_wmsf.py "$EXP_DIR/configs/run_wmsf.py.snapshot" || true
cp scripts/run_ipsns.py "$EXP_DIR/configs/run_ipsns.py.snapshot" || true
cp configs/*.yaml "$EXP_DIR/configs/" 2>/dev/null || true
echo

echo "=== Inspect reproduce_all.py CLI ==="
python scripts/reproduce_all.py --help || true
echo

echo "=== Smoke test on first 3 real benchmark instances ==="
head -3 "$EXP_DIR/configs/benchmark_instances_found_all.txt" > "$EXP_DIR/configs/smoke_instances.txt"
cat "$EXP_DIR/configs/smoke_instances.txt"
echo

python scripts/reproduce_all.py --instances "$EXP_DIR/configs/smoke_instances.txt" --results-dir "$EXP_DIR/raw/smoke_test"
SMOKE_STATUS=$?
echo "Smoke test exit status: $SMOKE_STATUS"
echo

echo "=== Smoke test output files ==="
find "$EXP_DIR/raw/smoke_test" -type f | sort
echo

echo "=== Smoke test CSV previews ==="
for f in $(find "$EXP_DIR/raw/smoke_test" -name "*.csv" | sort); do
  echo "--- $f ---"
  head -20 "$f"
done
echo

if [ "$SMOKE_STATUS" -ne 0 ]; then
  echo "Smoke test failed. Stopping before full EXP1 run."
  grep -R "Traceback\|Error\|Exception\|nan\|NaN\|None" -n "$EXP_DIR" || true
  echo "Finished with failure: $(date)"
  exit 1
fi

echo "=== Full core benchmark run on all discovered .d instances ==="
python scripts/reproduce_all.py --instances "$EXP_DIR/configs/benchmark_instances_found_all.txt" --results-dir "$EXP_DIR/raw/full_benchmark"
FULL_STATUS=$?
echo "Full benchmark exit status: $FULL_STATUS"
echo

echo "=== Full benchmark output files ==="
find "$EXP_DIR/raw/full_benchmark" -type f | sort | head -300
echo

echo "=== Build paper-ready EXP1 summary ==="
python - <<'PY'
from pathlib import Path
import pandas as pd
import numpy as np
import json
import re
import os

EXP = Path("experiments/exp1_core_benchmark")
root = EXP / "raw" / "full_benchmark"
summary_dir = EXP / "summary"
tables_dir = EXP / "tables"
summary_dir.mkdir(parents=True, exist_ok=True)
tables_dir.mkdir(parents=True, exist_ok=True)

csvs = sorted(root.rglob("*.csv"))
print(f"CSV files under full_benchmark: {len(csvs)}")

# Prefer existing summary-like CSV from reproduce_all.py.
summary_candidates = [p for p in csvs if "summary" in p.name.lower()]
print("Summary candidates:", [str(p) for p in summary_candidates[:10]])

if summary_candidates:
    src = summary_candidates[0]
    df = pd.read_csv(src)
    print(f"Using existing summary CSV: {src}")
else:
    # Fallback: make an index of output CSVs.
    rows = []
    for p in csvs:
        try:
            d = pd.read_csv(p)
            rows.append({"file": str(p), "columns": "|".join(d.columns), "n_rows": len(d)})
        except Exception as e:
            rows.append({"file": str(p), "columns": f"READ_ERROR:{e}", "n_rows": None})
    df = pd.DataFrame(rows)
    print("No summary CSV found; created file-index summary.")

raw_summary = summary_dir / "exp1_raw_summary.csv"
df.to_csv(raw_summary, index=False)
print(f"Wrote raw summary: {raw_summary}")

# Normalize columns if possible.
df2 = df.copy()
lower = {c.lower().strip(): c for c in df2.columns}

def find_col(candidates):
    for cand in candidates:
        for lc, orig in lower.items():
            if cand in lc:
                return orig
    return None

instance_col = find_col(["instance", "file", "path", "name"])
lr_bw = find_col(["lrta_backward", "lr-ta backward", "lrta_bw", "lr-ta_bw", "lr_bw", "local_ratio_backward"])
wm_bw = find_col(["wmsf_backward", "wmsf_bw"])
ip_bw = find_col(["ipsns_backward", "ipsns_bw", "lns_backward"])
lr_rt = find_col(["lrta_runtime", "lr-ta runtime", "lrta_time", "lr_time"])
wm_rt = find_col(["wmsf_runtime", "wmsf_time"])
ip_rt = find_col(["ipsns_runtime", "ipsns_time", "lns_runtime", "lns_time"])

paper = pd.DataFrame()
if instance_col:
    paper["instance"] = df2[instance_col].astype(str)
else:
    paper["instance"] = np.arange(len(df2))

for new, old in [
    ("lrta_bw", lr_bw),
    ("wmsf_bw", wm_bw),
    ("ipsns_bw", ip_bw),
    ("lrta_runtime", lr_rt),
    ("wmsf_runtime", wm_rt),
    ("ipsns_runtime", ip_rt),
]:
    if old:
        paper[new] = pd.to_numeric(df2[old], errors="coerce")

if {"lrta_bw", "wmsf_bw", "ipsns_bw"}.issubset(paper.columns):
    paper["ipsns_improves_lrta"] = paper["ipsns_bw"] < paper["lrta_bw"]
    paper["ipsns_improves_wmsf"] = paper["ipsns_bw"] < paper["wmsf_bw"]
    paper["ipsns_no_worse_than_both"] = paper["ipsns_bw"] <= paper[["lrta_bw", "wmsf_bw"]].min(axis=1)
    paper["best_seed_bw"] = paper[["lrta_bw", "wmsf_bw"]].min(axis=1)
    paper["ipsns_gain_over_best_seed"] = paper["best_seed_bw"] - paper["ipsns_bw"]
    paper["ipsns_rel_gain_over_best_seed"] = paper["ipsns_gain_over_best_seed"] / paper["best_seed_bw"].replace(0, np.nan)

    stats = {
        "n_instances": int(len(paper)),
        "ipsns_improves_lrta": int(paper["ipsns_improves_lrta"].sum()),
        "ipsns_improves_wmsf": int(paper["ipsns_improves_wmsf"].sum()),
        "incumbent_protection_violations": int((~paper["ipsns_no_worse_than_both"]).sum()),
        "mean_gain_over_best_seed": float(paper["ipsns_gain_over_best_seed"].mean()),
        "median_gain_over_best_seed": float(paper["ipsns_gain_over_best_seed"].median()),
        "mean_relative_gain_over_best_seed": float(paper["ipsns_rel_gain_over_best_seed"].mean(skipna=True)),
        "median_relative_gain_over_best_seed": float(paper["ipsns_rel_gain_over_best_seed"].median(skipna=True)),
    }
else:
    stats = {
        "n_rows": int(len(paper)),
        "warning": "Could not identify lrta_bw, wmsf_bw, ipsns_bw columns automatically.",
        "columns_in_raw_summary": list(df2.columns),
    }

paper_summary = tables_dir / "exp1_core_benchmark_paper_summary.csv"
paper.to_csv(paper_summary, index=False)
print(f"Wrote paper summary: {paper_summary}")

stats_path = summary_dir / "exp1_core_benchmark_stats.json"
stats_path.write_text(json.dumps(stats, indent=2))
print(f"Wrote stats: {stats_path}")
print(json.dumps(stats, indent=2))

# Also write a short markdown summary.
md = ["# EXP1 Core Benchmark Summary", ""]
for k, v in stats.items():
    md.append(f"- **{k}**: {v}")
md.append("")
md.append(f"Raw summary: `{raw_summary}`")
md.append(f"Paper summary: `{paper_summary}`")
(summary_dir / "exp1_core_benchmark_summary.md").write_text("\n".join(md))
PY
echo

echo "=== Search EXP1 outputs for errors ==="
grep -R "Traceback\|Error\|Exception\|nan\|NaN\|None" -n "$EXP_DIR" || true
echo

echo "=== Show final EXP1 stats ==="
cat "$EXP_DIR/summary/exp1_core_benchmark_stats.json" || true
echo
cat "$EXP_DIR/summary/exp1_core_benchmark_summary.md" || true
echo

echo "=== Preview paper-ready summary CSV ==="
head -20 "$EXP_DIR/tables/exp1_core_benchmark_paper_summary.csv" || true
echo

echo "=== Git status ==="
git status
echo

echo "=== Commit small EXP1 files, not huge raw outputs ==="
git add run_exp1_core_benchmark_tmux.sh "$EXP_DIR/configs" "$EXP_DIR/summary" "$EXP_DIR/tables" || true
git commit -m "Add EXP1 core benchmark results" || true
git push || true
echo

echo "=== Final commit ==="
git log -1 --oneline
echo

echo "============================================================"
echo "EXP1 CORE BENCHMARK FINISHED"
echo "Finished: $(date)"
echo "Log: $LOG"
echo "Paper summary CSV: $EXP_DIR/tables/exp1_core_benchmark_paper_summary.csv"
echo "Stats JSON: $EXP_DIR/summary/exp1_core_benchmark_stats.json"
echo "GitHub: private repository SoroushVahidi/minimum-weighted-fas-heuristics"
echo "============================================================"
