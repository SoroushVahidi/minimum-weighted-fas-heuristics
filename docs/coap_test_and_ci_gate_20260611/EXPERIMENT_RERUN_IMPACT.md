# Experiment Rerun Impact

**Audit date:** 2026-06-11

## Summary

No result-affecting production defects were identified by the test gate. **No completed experiment must be rerun** solely on the basis of this test suite.

## Observations (not defects)

| Observation | Classification | Rerun implication |
|-------------|----------------|-------------------|
| WMSF stabilization is not guaranteed non-worsening | Documented scope / manuscript already qualified | None |
| IPSNS calls `random.seed(rng_seed)` at entry | Documented behavior | None |
| Parser accepts negative weights | Documented contract; benchmark excludes them | None |
| `src/mwfas/ipsns.py` modified in working tree (pre-existing) | Outside this task; not altered by test gate | Author should verify against EXP10 commit |

## EXP10 status at audit time

Passive inspection: **1860 DRMacIver checkpoints** and **1860 IPSNS checkpoints** present. Runner processes not active. EXP10 directories were not modified by this task.
