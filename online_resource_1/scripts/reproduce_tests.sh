#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
LOG="provenance/pytest_$(date -u +%Y%m%dT%H%M%SZ).log"
export PYTHONPATH="$ROOT/src"
pip install -q -r requirements-dev.txt 2>/dev/null || true
python3 -m pytest tests/ --tb=no 2>&1 | tee "$LOG"
SUMMARY=$(grep -E '[0-9]+ passed' "$LOG" | tail -1)
echo "Summary: $SUMMARY"
if echo "$SUMMARY" | grep -qE '90 passed, 1 skipped'; then
  echo "PASS: full-repository test gate"
elif echo "$SUMMARY" | grep -qE '79 passed, 7 skipped'; then
  echo "PASS: OR1 packaged artifact gate (EXP10 live tree not bundled)"
elif echo "$SUMMARY" | grep -qE '89 passed, 2 skipped'; then
  echo "PASS: OR1 artifact with EXP10 namespace present"
else
  echo "FAIL: unexpected pytest summary: $SUMMARY"
  exit 1
fi
echo "PASS: test gate"
