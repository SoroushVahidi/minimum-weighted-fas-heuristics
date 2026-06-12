# Test Results

**Final run:** 2026-06-11  
**Command:**

```bash
PYTHONPATH=src python3 -m pytest --ignore=experiments/exp4_external_baselines/external_tools -q
```

**Log:** `logs/pytest_final_full.log`

## Summary

| Metric | Count |
|--------|-------|
| Collected | **78** |
| Passed | **77** |
| Failed | **0** |
| Skipped | **1** (`test_no_stale_tmp_during_active_run` — runner inactive) |
| Errors | **0** |
| Warnings | 2 (EXP10 `datetime.utcnow` deprecation via import side effect) |
| Duration | ~2.3 s |

## By category

| Category | Tests |
|----------|-------|
| unit | 46 |
| property | 8 |
| regression | 24 |

## Key behavioral conclusions

- LR-TA returns acyclic FAS on all tested supported inputs.
- LR-TA add-back yields inclusion-minimal FAS on tested graphs.
- WMSF `removeArcs` + `minimizeFas` yields feasible FAS; safe edges restored.
- WMSF stabilization **not** asserted non-worsening (manuscript scope).
- IPSNS final objective ≤ both seeds on tested instances.
- Seeded IPSNS reproducible on tested instances.
- Exact DP matches brute force for n ≤ 8 and all fixture graphs.
- EXP10 smoke archive integrity verified read-only (7 tests; 1 skip).
