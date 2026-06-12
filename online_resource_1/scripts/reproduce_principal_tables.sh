#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
python3 - <<'PY'
import json, sys
from pathlib import Path

root = Path('.')
checks = []

def check(name, path, key=None, expected=None, tol=0.05):
    p = root / path
    ok = p.exists()
    obs = None
    if ok and key and p.suffix == '.json':
        data = json.loads(p.read_text())
        obs = data
        for k in key.split('.'):
            obs = obs[k]
        if expected is not None:
            if isinstance(obs, (int, float)):
                ok = abs(float(obs) - float(expected)) <= tol
            else:
                ok = obs == expected
    checks.append((name, ok, obs))
    print(f"{'PASS' if ok else 'FAIL'}: {name} -> {obs}")

check('EXP4 DR rel gap', 'results/exp4/summary/exp4_external_stats.json',
      'per_algorithm.drmaciver_fas.mean_rel_gain_ipsns_pct', 21.6076)
check('EXP3 IPSNS optimal', 'results/exp3/summary/exp3_exact_stats.json',
      'standard_instances.ipsns_optimal', '56/57 (98.2%)')
check('EXP10 median wins', 'results/exp10/summary/statistical_tests.json',
      'primary_paired_median.n_ipsns_wins', 38)
check('EXP10 ties', 'results/exp10/summary/statistical_tests.json',
      'primary_paired_median.n_ties', 55)
check('EXP10 DR wins', 'results/exp10/summary/statistical_tests.json',
      'primary_paired_median.n_dr_wins', 0)
check('EXP10 mean rel excess', 'results/exp10/summary/statistical_tests.json',
      'primary_paired_median.mean_rel_excess_dr_over_ipsns_pct', 21.60, tol=0.05)
check('EXP11 median improvement', 'results/exp11/summary/exp11_aggregate.json',
      'median_improvement_best_alt', 0.0)
check('EXP11 instances improved (nonneg)', 'results/exp11/summary/exp11_aggregate.json',
      'instances_improved_nonneg', 0)
check('Digest exists', 'results/combined/summary/manuscript_results_digest.json')
check('Combined external table', 'results/combined/tables/manuscript_table_external_sparse.csv')

failed = [c for c in checks if not c[1]]
if failed:
    print(f"\n{len(failed)} checks FAILED")
    sys.exit(1)
print("\nAll principal table checks PASSED")
PY
