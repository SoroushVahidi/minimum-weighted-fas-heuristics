#!/usr/bin/env bash
# EXP1b: Full core benchmark with IPSNS wmsf_seed_mode="full" (commit c787c0f+)
set -u
set -o pipefail

cd ~/minimum-weighted-fas-heuristics

EXP="experiments/exp1b_core_benchmark_full_wmsf_seed"
LOG="$EXP/logs/exp1b_core_benchmark.log"

mkdir -p "$EXP"/{raw,logs,tables,summary,configs}

exec > >(tee -a "$LOG") 2>&1

echo "============================================================"
echo "EXP1b: CORE BENCHMARK — IPSNS WITH FULL WMSF SEED"
echo "Started: $(date)"
echo "Repository: $(pwd)"
echo "============================================================"

echo "=== Git state ==="
git status
GIT_HASH=$(git rev-parse HEAD)
echo "HEAD: $GIT_HASH"
git log -3 --oneline
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
echo

echo "=== Install package ==="
python -m pip install -e . -q
python -m pip freeze > "$EXP/configs/pip_freeze.txt"
echo "pip freeze saved."
echo

echo "=== Verify IPSNS uses full WMSF seed by default ==="
python - <<'PY'
import sys; sys.path.insert(0, ".")
from mwfas.ipsns import lns_merge_wmsf_lr_best_incumbent
import inspect
sig = inspect.signature(lns_merge_wmsf_lr_best_incumbent)
mode = sig.parameters["wmsf_seed_mode"].default
print(f"  lns_merge_wmsf_lr_best_incumbent wmsf_seed_mode default = '{mode}'")
assert mode == "full", f"Expected 'full', got '{mode}'"
print("  OK: default is 'full'")
PY
echo

echo "=== Locate benchmark instances ==="
INSTANCES_LIST=""
if [ -f "experiments/exp1_core_benchmark/configs/benchmark_instances_found_all.txt" ]; then
  INSTANCES_LIST="experiments/exp1_core_benchmark/configs/benchmark_instances_found_all.txt"
  echo "Using EXP1 instance list: $INSTANCES_LIST"
elif [ -f "configs/benchmark_instances_found_all.txt" ]; then
  INSTANCES_LIST="configs/benchmark_instances_found_all.txt"
  echo "Using repo-root instance list: $INSTANCES_LIST"
else
  echo "No cached list found; searching for .d files..."
  find ~ -name "*.d" | sort > "$EXP/configs/benchmark_instances_found_all.txt" || true
  INSTANCES_LIST="$EXP/configs/benchmark_instances_found_all.txt"
fi

COUNT=$(wc -l < "$INSTANCES_LIST" || echo 0)
echo "Instance count: $COUNT"
if [ "$COUNT" -lt 3 ]; then
  echo "Fewer than 3 .d files; cloning graph-benchmarks."
  mkdir -p ~/benchmark_sources
  cd ~/benchmark_sources
  [ ! -d graph-benchmarks ] && git clone https://github.com/alidasdan/graph-benchmarks.git
  cd ~/minimum-weighted-fas-heuristics
  find ~/benchmark_sources/graph-benchmarks -name "*.d" | sort > "$EXP/configs/benchmark_instances_found_all.txt"
  INSTANCES_LIST="$EXP/configs/benchmark_instances_found_all.txt"
  COUNT=$(wc -l < "$INSTANCES_LIST")
fi

cp "$INSTANCES_LIST" "$EXP/configs/benchmark_instances_found_all.txt" 2>/dev/null || true
cp scripts/reproduce_all.py "$EXP/configs/reproduce_all.py.snapshot" || true
echo "GIT_HASH=$GIT_HASH" > "$EXP/configs/experiment_metadata.txt"
echo "STARTED=$(date -Iseconds)" >> "$EXP/configs/experiment_metadata.txt"
echo "INSTANCES_LIST=$INSTANCES_LIST" >> "$EXP/configs/experiment_metadata.txt"
echo "N_INSTANCES=$COUNT" >> "$EXP/configs/experiment_metadata.txt"
echo "WMSF_SEED_MODE=full" >> "$EXP/configs/experiment_metadata.txt"
echo

echo "=== Smoke test (first 3 instances) ==="
head -3 "$EXP/configs/benchmark_instances_found_all.txt" > "$EXP/configs/smoke_instances.txt"
cat "$EXP/configs/smoke_instances.txt"

python scripts/reproduce_all.py \
  --instances "$EXP/configs/smoke_instances.txt" \
  --results-dir "$EXP/raw/smoke_test" \
  --ipsns-iters 400 --rng-seed 1
SMOKE_STATUS=$?
echo "Smoke test exit status: $SMOKE_STATUS"

if [ "$SMOKE_STATUS" -ne 0 ]; then
  echo "SMOKE TEST FAILED. Stopping."
  exit 1
fi
echo

echo "=== Full benchmark run ==="
python scripts/reproduce_all.py \
  --instances "$EXP/configs/benchmark_instances_found_all.txt" \
  --results-dir "$EXP/raw/full_benchmark" \
  --ipsns-iters 400 --rng-seed 1
FULL_STATUS=$?
echo "Full benchmark exit status: $FULL_STATUS"
echo

echo "=== Postprocess results ==="
python "$EXP/postprocess_exp1b.py"
POST_STATUS=$?
echo "Postprocess exit status: $POST_STATUS"
echo

echo "=== Check for external violations ==="
python - <<'PY'
import json, sys
from pathlib import Path
stats = json.loads(Path("experiments/exp1b_core_benchmark_full_wmsf_seed/summary/exp1b_core_benchmark_stats.json").read_text())
v = stats.get("incumbent_protection_violations_external", "N/A")
n = stats.get("n_complete_triplets", "N/A")
print(f"  Complete triplets : {n}")
print(f"  External violations (IPSNS > min(LRTA,WMSF)): {v}")
if isinstance(v, int) and v == 0:
    print("  ALL CLEAR: guarantee holds for all instances.")
else:
    print(f"  WARNING: {v} violations — see summary/exp1b_external_violations.csv")
PY
echo

echo "=== Search for runtime errors ==="
# Exclude source-code snapshots
grep -Rn "Traceback\|^[A-Z][a-zA-Z]*Error\|^Exception" \
    "$EXP/raw/full_benchmark" \
    "$EXP/summary" \
    "$EXP/tables" 2>/dev/null \
    | grep -v ".snapshot:" | head -30 || echo "  No runtime errors found."
echo

echo "=== Commit small results files ==="
cd ~/minimum-weighted-fas-heuristics
git add \
    run_exp1b_full_wmsf_seed_tmux.sh \
    "$EXP/postprocess_exp1b.py" \
    "$EXP/configs/" \
    "$EXP/summary/" \
    "$EXP/tables/" \
    2>/dev/null || true

git commit -m "Add EXP1b full WMSF seed benchmark results" \
    --allow-empty 2>/dev/null || true
git push || true
echo

echo "=== Final git log ==="
git log -1 --oneline
echo

echo "============================================================"
echo "EXP1b FINISHED"
echo "Finished: $(date)"
echo "Log: $LOG"
echo "Paper summary: $EXP/tables/exp1b_core_benchmark_paper_summary.csv"
echo "Stats JSON:    $EXP/summary/exp1b_core_benchmark_stats.json"
echo "============================================================"
