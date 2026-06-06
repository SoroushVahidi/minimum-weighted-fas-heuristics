#!/usr/bin/env bash
# EXP4 smoke test — runs all 8 algorithms on 4 representative instances.
set -euo pipefail

REPO="$(cd "$(dirname "$0")/../.." && pwd)"
EXP4="$REPO/experiments/exp4_external_baselines"

echo "=== EXP4 Smoke Test ==="
echo "Date:   $(date)"
echo "Host:   $(hostname)"
echo "Python: $(python3 --version 2>&1)"
echo "Git:    $(git -C "$REPO" rev-parse HEAD 2>/dev/null || echo unknown)"
echo ""

mkdir -p "$EXP4/logs" "$EXP4/summary" "$EXP4/raw"

cd "$REPO"
python3 "$EXP4/run_exp4_benchmark.py" \
    --instances "$EXP4/configs/exp4_smoke_instances.txt" \
    --out-dir   "$EXP4" \
    --log       "$EXP4/logs/exp4_smoke.log" \
    --summary   "$EXP4/summary/exp4_smoke_summary.csv" \
    --ipsns-iters 100 \
    --random-trials 100 \
    --random-seed 1

echo ""
echo "Smoke summary: $EXP4/summary/exp4_smoke_summary.csv"
echo "Smoke log:     $EXP4/logs/exp4_smoke.log"
echo "=== Smoke test complete ==="
