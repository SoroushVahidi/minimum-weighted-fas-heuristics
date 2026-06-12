# EXP10 Integration Audit

## Frozen values verified in OR1

| Quantity | Value | Supporting file |
|---|---|---|
| Instances | 93 | `results/exp10/summary/statistical_tests.json` |
| IPSNS seeds | 20 | protocol JSON / summaries |
| DRMacIver repetitions | 20 | protocol JSON / summaries |
| Valid IPSNS runs | 1860/1860 | `results/exp10/summary/ipsns_validation_summary.json` |
| Valid DRMacIver runs | 1860/1860 | validation summaries |
| Median comparison | 38 wins, 55 ties, 0 losses (IPSNS) | `statistical_tests.json` |
| Mean relative excess (DR) | 21.60% (21.601773263726717 in JSON) | `statistical_tests.json` |
| IPSNS objective variance | 0 on all 93 instances | `ipsns_phase_conclusions.md` |
| DRMacIver spread | 40/93 instances with >1 distinct objective | validation summaries |

## Manuscript / supplement alignment

- Main Table EXP10 and OR1 §S11 use identical counts.
- `reproduce_principal_tables.sh` checks median wins, ties, DR wins, and mean excess.
- Supplement discloses: not equal-time comparison; zero observed IPSNS variation is not mathematical determinism; r20_60 single-run reversal under median comparison.

## Raw outputs

Full EXP10 raw JSON checkpoints (1860×2) are **not** bundled. Validated summaries and manifests in `results/exp10/summary/` support all headline claims.

## Status

**EXP10 fully incorporated.**
