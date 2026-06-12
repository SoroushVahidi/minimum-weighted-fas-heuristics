#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
FAIL=0

echo "=== OR1 artifact validation ==="

for f in README.md LICENSE MANIFEST.sha256 supplement/online_resource_1.tex \
         provenance/source_commit.txt provenance/claim_to_artifact_map.csv \
         src/mwfas/topo_extraction.py results/exp11/summary/exp11_aggregate.json; do
  if [[ ! -f "$f" ]]; then echo "MISSING: $f"; FAIL=1; else echo "OK: $f"; fi
done

PATH_HITS=$(grep -rl "/home/soroush" --include='*.md' --include='*.txt' --include='*.csv' --include='*.json' --include='*.tex' --include='*.sh' --include='*.py' . 2>/dev/null | grep -v MANIFEST.sha256 | grep -v finalize_or1.py | grep -v validate_artifact.sh || true)
if [[ -n "$PATH_HITS" ]]; then
  echo "FAIL: absolute /home/soroush paths in: $PATH_HITS"
  FAIL=1
else
  echo "OK: no /home/soroush paths"
fi

if find . \( -name '__pycache__' -o -name '.pytest_cache' -o -name '*.pyc' \) 2>/dev/null | head -1 | grep -q .; then
  echo "FAIL: cache files present"; FAIL=1
else
  echo "OK: no cache files"
fi

python3 - <<'PY'
import json, sys
from pathlib import Path
for p in Path('.').rglob('*.json'):
    if any(x in p.parts for x in ('.pytest_cache', '__pycache__')): continue
    json.loads(p.read_text())
print('OK: JSON parse')
PY
[[ $? -ne 0 ]] && FAIL=1

if ! grep -qE '79 passed, 7 skipped|90 passed, 1 skipped' README.md 2>/dev/null; then
  echo "WARN: README test count"
fi

if ./scripts/reproduce_smoke.sh; then echo "OK: smoke"; else echo "FAIL: smoke"; FAIL=1; fi
if ./scripts/reproduce_tests.sh; then echo "OK: tests"; else echo "FAIL: tests"; FAIL=1; fi
if ./scripts/reproduce_principal_tables.sh; then echo "OK: tables"; else echo "FAIL: tables"; FAIL=1; fi

if [[ $FAIL -eq 0 ]]; then echo "=== VALIDATION PASSED ==="; else echo "=== VALIDATION FAILED ==="; exit 1; fi
