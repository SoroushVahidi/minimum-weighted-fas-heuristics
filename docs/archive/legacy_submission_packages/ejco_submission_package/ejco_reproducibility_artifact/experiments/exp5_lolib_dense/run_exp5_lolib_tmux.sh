#!/usr/bin/env bash
# EXP5 LOLIB Dense Benchmark — tmux runner
# Launch with:
#   tmux new-session -d -s mwfas_exp5_lolib \
#     "cd ~/minimum-weighted-fas-heuristics && bash experiments/exp5_lolib_dense/run_exp5_lolib_tmux.sh"

set -euo pipefail

REPO="$(cd "$(dirname "$0")/../.." && pwd)"
EXP_DIR="$REPO/experiments/exp5_lolib_dense"
LOG="$EXP_DIR/logs/exp5_lolib_tmux.log"
SUMMARY_RAW="$EXP_DIR/summary/exp5_lolib_raw_summary.csv"

mkdir -p "$EXP_DIR/logs" "$EXP_DIR/raw" "$EXP_DIR/summary"

echo "[$(date)] EXP5 LOLIB benchmark starting" | tee "$LOG"
echo "[$(date)] Repo: $REPO" | tee -a "$LOG"

cd "$REPO"

python "$EXP_DIR/run_exp5_lolib_benchmark.py" \
  --manifest "$EXP_DIR/configs/exp5_lolib_instances.txt" \
  --out-dir "$EXP_DIR" \
  --log "$LOG" \
  --summary "$SUMMARY_RAW" \
  --ipsns-iters 200 \
  --random-trials 100 \
  --random-seed 42 \
  2>&1 | tee -a "$LOG"

echo "[$(date)] Benchmark done. Running postprocessor..." | tee -a "$LOG"

python "$EXP_DIR/postprocess_exp5_lolib.py" 2>&1 | tee -a "$LOG"

echo "[$(date)] EXP5 complete." | tee -a "$LOG"
echo "Results in: $EXP_DIR/summary/ and $EXP_DIR/tables/"
