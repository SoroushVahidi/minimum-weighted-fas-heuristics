#!/usr/bin/env bash
# EXP4 Full External Baselines Benchmark
# Runs all 8 algorithms on all 123 benchmark instances.
# Launch in tmux: tmux new-session -d -s mwfas_exp4_external "..."
set -euo pipefail

REPO="$(cd "$(dirname "$0")/../.." && pwd)"
EXP4="$REPO/experiments/exp4_external_baselines"
LOG="$EXP4/logs/exp4_external_baselines.log"
SUMMARY="$EXP4/summary/exp4_raw_summary.csv"

echo "=== EXP4 External Baselines Full Benchmark ==="
echo "Date:        $(date)"
echo "Host:        $(hostname)"
echo "CPU:         $(lscpu | grep 'Model name' | sed 's/Model name:\s*//')"
echo "Python:      $(python3 --version 2>&1)"
echo "Git hash:    $(git -C "$REPO" rev-parse HEAD 2>/dev/null || echo unknown)"
echo ""

echo "--- pip freeze ---"
pip freeze 2>/dev/null | head -40 || true
echo ""

echo "--- External access report ---"
cat "$EXP4/summary/external_access_report.md" 2>/dev/null | head -30 || true
echo ""

mkdir -p "$EXP4/logs" "$EXP4/summary" "$EXP4/raw" "$EXP4/tables"

cd "$REPO"
python3 "$EXP4/run_exp4_benchmark.py" \
    --instances "$EXP4/configs/exp4_instances.txt" \
    --out-dir   "$EXP4" \
    --log       "$LOG" \
    --summary   "$SUMMARY" \
    --ipsns-iters 400 \
    --random-trials 100 \
    --random-seed 1

echo ""
echo "=== EXP4 Full benchmark complete ==="
echo "Summary: $SUMMARY"
echo "Log:     $LOG"
echo "Date:    $(date)"
