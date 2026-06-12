# Claim Traceability Audit

Primary map: `online_resource_1/provenance/claim_to_artifact_map.csv`

## Major claims verified

| Claim | Value | Artifact file | Status |
|---|---|---|---|
| Sparse IPSNS best | 96/97 | `results/exp4/summary/exp4_external_stats.json` | included |
| EXP4 DR excess | 21.61% | `results/exp4/summary/exp4_external_stats.json` | included |
| EXP10 median | 38/55/0 | `results/exp10/summary/statistical_tests.json` | included |
| EXP10 runs | 1860/1860 each | `results/exp10/summary/ipsns_validation_summary.json` | included |
| EXP10 mean excess | 21.60% | `statistical_tests.json` | included |
| Exact optimum match | 56/57 | `results/exp3/summary/exp3_exact_stats.json` | included |
| EXP11 zero change | 0 improved | `results/exp11/summary/exp11_aggregate.json` | included |
| Test gate (full repo) | 90/1/0 | `tests/` + logs | included |
| LOLIB boundary | DR wins 45/50 | `results/exp5/summary/exp5_lolib_stats.json` | included |
| HiGHS | 6/7 IPSNS match on proven-optimal | `results/exp8/summary/exp8_mip_summary.json` | included |
| \(B_\pi \subseteq F\) | theory | `supplement/sections/S02_problem.tex` | included |

## Gaps

None identified for headline numerical claims. Runtime claims reference experiment logs not fully bundled (documented limitation).

## Status

**All major manuscript claims traceable** to committed summaries or supplement proofs.
