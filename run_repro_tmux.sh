#!/usr/bin/env bash
set -u
set -o pipefail

cd ~/minimum-weighted-fas-heuristics

mkdir -p results/raw results/raw/smoke_test results/raw/full_benchmark results/tables configs

LOG="results/raw/reproducibility_tmux.log"
exec > >(tee -a "$LOG") 2>&1

echo "=== MWFAS reproducibility run started at $(date) ==="
echo "Repository: $(pwd)"
echo

echo "=== Git status and pull ==="
git status
git pull || true
echo

echo "=== Install package and requirements ==="
python -m pip install -e .
python -m pip install -r requirements.txt
echo

echo "=== Locate benchmark .d files ==="
find ~ -name "*.d" | sort > configs/benchmark_instances_found_all.txt || true
COUNT=$(wc -l < configs/benchmark_instances_found_all.txt || echo 0)
echo "Found $COUNT .d files before cloning."

if [ "$COUNT" -lt 3 ]; then
  echo "Fewer than 3 .d files found; cloning graph-benchmarks."
  mkdir -p ~/benchmark_sources
  cd ~/benchmark_sources
  if [ ! -d graph-benchmarks ]; then
    git clone https://github.com/alidasdan/graph-benchmarks.git
  fi
  cd ~/minimum-weighted-fas-heuristics
  find ~/benchmark_sources/graph-benchmarks -name "*.d" | sort > configs/benchmark_instances_found_all.txt
fi

COUNT=$(wc -l < configs/benchmark_instances_found_all.txt || echo 0)
echo "Final discovered .d instance count: $COUNT"
echo "First 20 discovered instances:"
head -20 configs/benchmark_instances_found_all.txt
echo

echo "=== Inspect reproduce_all.py CLI ==="
python scripts/reproduce_all.py --help || true
echo

echo "=== Smoke test on first 3 real instances ==="
head -3 configs/benchmark_instances_found_all.txt > /tmp/mwfas_smoke_instances.txt
cat /tmp/mwfas_smoke_instances.txt
echo

python scripts/reproduce_all.py --instances /tmp/mwfas_smoke_instances.txt --results-dir results/raw/smoke_test
SMOKE_STATUS=$?
echo "Smoke test exit status: $SMOKE_STATUS"
echo

echo "=== Smoke test generated files ==="
find results/raw/smoke_test -maxdepth 3 -type f | sort
echo

echo "=== Smoke test CSV previews ==="
for f in $(find results/raw/smoke_test -name "*.csv" | sort); do
  echo "--- $f ---"
  head -20 "$f"
done
echo

if [ "$SMOKE_STATUS" -ne 0 ]; then
  echo "Smoke test failed. Stopping before full benchmark."
  echo "=== Searching for errors ==="
  grep -R "Traceback\|Error\|Exception\|nan\|NaN\|None" -n results/raw || true
  echo "=== Run ended at $(date) ==="
  exit 1
fi

echo "=== Full benchmark run ==="
python scripts/reproduce_all.py --instances configs/benchmark_instances_found_all.txt --results-dir results/raw/full_benchmark
FULL_STATUS=$?
echo "Full benchmark exit status: $FULL_STATUS"
echo

echo "=== Generated full benchmark files ==="
find results/raw/full_benchmark -maxdepth 3 -type f | sort | head -200
echo

echo "=== Build/check unified reproducibility summary ==="
python - <<'PY'
from pathlib import Path
import pandas as pd
import re

root = Path("results/raw/full_benchmark")
out = Path("results/tables/unified_reproducibility_summary.csv")
out.parent.mkdir(parents=True, exist_ok=True)

csvs = sorted(root.rglob("*.csv"))
print(f"Found {len(csvs)} CSV files under {root}")

# If reproduce_all already made a summary CSV, prefer the most summary-like one.
summary_candidates = [p for p in csvs if "summary" in p.name.lower()]
if summary_candidates:
    src = summary_candidates[0]
    print(f"Using existing summary candidate: {src}")
    df = pd.read_csv(src)
    df.to_csv(out, index=False)
else:
    rows = []
    for p in csvs:
        try:
            df = pd.read_csv(p)
        except Exception:
            continue
        rows.append({
            "file": str(p),
            "columns": "|".join(df.columns),
            "n_rows": len(df),
        })
    df = pd.DataFrame(rows)
    df.to_csv(out, index=False)

print(f"Wrote {out}")

df = pd.read_csv(out)
print("Summary columns:", list(df.columns))
print(df.head(10).to_string(index=False))

# Try to verify incumbent protection if recognizable columns exist.
cols = {c.lower(): c for c in df.columns}
def find_col(options):
    for opt in options:
        for lc, orig in cols.items():
            if opt in lc:
                return orig
    return None

lr = find_col(["lrta_backward", "lr-ta backward", "lrta_bw", "lr-ta_bw", "lr_bw"])
wm = find_col(["wmsf_backward", "wmsf_bw"])
ip = find_col(["ipsns_backward", "ipsns_bw"])

if lr and wm and ip:
    d = df.copy()
    d[lr] = pd.to_numeric(d[lr], errors="coerce")
    d[wm] = pd.to_numeric(d[wm], errors="coerce")
    d[ip] = pd.to_numeric(d[ip], errors="coerce")
    violations = d[d[ip] > d[[lr, wm]].min(axis=1)]
    print(f"Incumbent-protection check using columns: {lr}, {wm}, {ip}")
    print(f"Violations: {len(violations)}")
    if len(violations):
        print(violations.to_string(index=False))
    print(f"IPSNS improves over LR-TA: {(d[ip] < d[lr]).sum()}")
    print(f"IPSNS improves over WMSF: {(d[ip] < d[wm]).sum()}")
else:
    print("Could not automatically identify LRTA/WMSF/IPSNS backward-weight columns.")
    print("Please inspect the summary CSV manually.")
PY
echo

echo "=== Search for errors in results/raw ==="
grep -R "Traceback\|Error\|Exception\|nan\|NaN\|None" -n results/raw || true
echo

echo "=== Git status after run ==="
git status
echo

echo "=== Commit small reproducibility support files if appropriate ==="
git add configs/benchmark_instances_found_all.txt results/tables/unified_reproducibility_summary.csv run_repro_tmux.sh || true
git commit -m "Run unified reproducibility verification" || true
git push || true
echo

echo "=== Final commit info ==="
git log -1 --oneline
echo "GitHub: https://github.com/SoroushVahidi/minimum-weighted-fas-heuristics"
echo "Log file: $LOG"
echo "Summary CSV: results/tables/unified_reproducibility_summary.csv"
echo "=== MWFAS reproducibility run finished at $(date) ==="
