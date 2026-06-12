# Claim Safety Audit — Post EXP10 Integration

## Safe claims (supported)

| Claim | Evidence |
|-------|----------|
| IPSNS median ≤ DRMacIver on 93-instance subset (38/55/0) | EXP10 paired medians |
| Mean relative excess ~21.6% persists | statistical_tests.json |
| Wilcoxon/sign tests p<0.001 | statistical_tests.json |
| IPSNS zero cross-seed objective variation | ipsns_phase_conclusions.md |
| DRMacIver restart variability on 40 instances | drmaciver_phase_conclusions.md |
| EXP4 single-run DR win on r20_60 does not persist under median | exp4_vs_exp10.csv |

## Claims avoided (per constraints)

- "State of the art" / "best known"
- "Mathematically deterministic" IPSNS
- Equal-time superiority
- Universal dominance beyond sparse scope

## Qualifications included in manuscript

- IPSNS zero variance ≠ determinism proof
- Quality-focused comparison (not equal-time)
- DRMacIver intermediate solutions unavailable
- Results scoped to sparse nonnegative weighted digraphs

## Production defects from test gate

None (78-test gate; no result-affecting defects).
