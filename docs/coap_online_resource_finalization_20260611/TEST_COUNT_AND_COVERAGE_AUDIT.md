# Test Count and Coverage Audit

## Source of truth (full repository)

```
90 passed, 1 skipped, 2 warnings in 1.34s
```

- **Collected:** 91
- **Passed:** 90
- **Skipped:** 1 (`test_no_stale_tmp_during_active_run` or EXP10 live-runner skip depending on environment)
- **Failed:** 0

## OR1 packaged artifact

```
79 passed, 7 skipped in 1.29s
```

- **Collected:** 86
- **Excluded from package:** `test_experiment_infrastructure.py` (5 tests; requires live EXP10 scripts)
- **Skipped in package:** 7 EXP10 namespace tests when `experiments/exp10_stochastic_robustness/` tree absent

## Historical arithmetic

| Stage | Count |
|---|---|
| Original gate | 78 collected |
| +13 topological-extraction / objective tests | → 91 collected |
| OR1 package | 86 collected (5 infrastructure tests omitted) |

## New test module

`tests/unit/test_topo_extraction_math.py` — 13 tests covering \(B_\pi \subseteq F\), weight inequality, equality conditions, extraction rules.

## Coverage areas

- Exact DP vs brute force
- Objective identities (`compute_forward_backward`)
- WMSF safe-edge behavior
- IPSNS incumbent rollback
- Topological extraction (EXP11 utilities)
- Experiment namespace guards (skip when trees absent)

## Status

**Test counts updated correctly** with explicit distinction between full-repo and OR1-package gates.
