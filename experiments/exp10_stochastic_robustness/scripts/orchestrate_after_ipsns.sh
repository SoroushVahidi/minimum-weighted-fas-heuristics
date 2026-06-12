#!/bin/bash
# EXP10 post-IPSNS orchestration.
# Waits for PID $1 (IPSNS runner) to exit, then:
#   1. validates IPSNS runs
#   2. generates IPSNS summaries
#   3. runs DRMacIver preflight
#   4. launches DRMacIver full run if preflight passes
# Usage: bash orchestrate_after_ipsns.sh <IPSNS_PID>

set -euo pipefail

IPSNS_PID="${1:-24482}"
REPO_ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"
EXP_DIR="$REPO_ROOT/experiments/exp10_stochastic_robustness"
LOG_DIR="$EXP_DIR/logs"
SUMMARY_DIR="$EXP_DIR/summary"
SCRIPTS_DIR="$EXP_DIR/scripts"

mkdir -p "$LOG_DIR" "$SUMMARY_DIR"
ORCH_LOG="$LOG_DIR/orchestration.log"

log() { echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] $*" | tee -a "$ORCH_LOG"; }

log "=== EXP10 Orchestrator started ==="
log "Waiting for IPSNS runner PID $IPSNS_PID..."

# Wait for IPSNS runner to exit
while kill -0 "$IPSNS_PID" 2>/dev/null; do
    DONE=$(ls "$EXP_DIR/checkpoints/" | grep -c '^ipsns.*\.done$' || true)
    log "IPSNS progress: $DONE/1860"
    sleep 30
done

log "IPSNS PID $IPSNS_PID has exited. Checking exit..."

# Count final done files
IPSNS_DONE=$(ls "$EXP_DIR/checkpoints/" | grep -c '^ipsns.*\.done$' || true)
log "IPSNS done files: $IPSNS_DONE / 1860"

# Give checkpoint writes a moment to flush
sleep 2

# Step 1: If incomplete, try to resume
if [ "$IPSNS_DONE" -lt 1860 ]; then
    log "IPSNS incomplete ($IPSNS_DONE/1860). Attempting resume..."
    cd "$REPO_ROOT"
    python3 "$SCRIPTS_DIR/run_ipsns_repetitions.py" \
        >> "$LOG_DIR/ipsns_full_run.log" 2>&1
    IPSNS_DONE=$(ls "$EXP_DIR/checkpoints/" | grep -c '^ipsns.*\.done$' || true)
    log "After resume: $IPSNS_DONE / 1860"
fi

if [ "$IPSNS_DONE" -lt 1860 ]; then
    log "ERROR: IPSNS still incomplete after resume attempt. Manual intervention required."
    exit 1
fi

log "IPSNS phase complete."

# Step 2: Validate IPSNS runs
log "Running IPSNS validation..."
cd "$REPO_ROOT"
if python3 "$SCRIPTS_DIR/validate_ipsns_runs.py" >> "$ORCH_LOG" 2>&1; then
    log "IPSNS validation PASSED."
else
    log "ERROR: IPSNS validation FAILED. Check $SUMMARY_DIR/ipsns_validation_summary.json"
    exit 1
fi

# Step 3: Generate IPSNS summaries
log "Generating IPSNS phase summaries..."
if python3 "$SCRIPTS_DIR/summarize_ipsns_phase.py" >> "$ORCH_LOG" 2>&1; then
    log "IPSNS summaries generated."
else
    log "WARNING: IPSNS summary generation had errors (non-fatal)."
fi

# Update progress
python3 "$SCRIPTS_DIR/update_progress.py" >> "$ORCH_LOG" 2>&1 || true

# Step 4: DRMacIver preflight
log "Running DRMacIver preflight..."
if python3 "$SCRIPTS_DIR/drmaciver_preflight.py" >> "$ORCH_LOG" 2>&1; then
    log "Preflight PASSED."
else
    log "ERROR: DRMacIver preflight FAILED. Check $SUMMARY_DIR/drmaciver_preflight_report.md"
    exit 1
fi

# Step 5: Launch DRMacIver
DR_LOG="$LOG_DIR/drmaciver_runner.log"
log "Launching DRMacIver full run..."
log "Command: python3 $SCRIPTS_DIR/run_drmaciver_repetitions.py"
log "Log: $DR_LOG"

python3 "$SCRIPTS_DIR/run_drmaciver_repetitions.py" \
    > "$DR_LOG" 2>&1

DR_DONE=$(ls "$EXP_DIR/checkpoints/" | grep -c '^drmaciver.*\.done$' || true)
log "DRMacIver runner exited. Done files: $DR_DONE / 1860"

# Update progress
python3 "$SCRIPTS_DIR/update_progress.py" >> "$ORCH_LOG" 2>&1 || true

if [ "$DR_DONE" -eq 1860 ]; then
    log "DRMacIver phase COMPLETE."
else
    log "DRMacIver incomplete ($DR_DONE/1860). May need resume. Check log: $DR_LOG"
fi

log "=== Orchestration complete. ==="
