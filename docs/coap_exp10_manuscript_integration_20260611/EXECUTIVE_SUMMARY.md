# Executive Summary — EXP10 Finalization and Manuscript Integration

**Date:** 2026-06-12  
**Branch:** `main` / **HEAD:** `80b3144d5fdbbe250faed8a4fe671dde2da76c89`

## EXP10 status

| Item | Result |
|------|--------|
| DRMacIver production complete | **1860/1860** |
| IPSNS production complete | **1860/1860** |
| Validation | **PASSED** (0 fail, 0 duplicate, 0 missing) |
| COMPLETED.ok | **Created** |
| Runner active | **No** |

## Primary paired median result (93 instances)

| Metric | Value |
|--------|-------|
| IPSNS wins / ties / DR wins | **38 / 55 / 0** |
| Mean relative excess (DR over IPSNS) | **21.60%** |
| Wilcoxon p (two-sided) | **7.74×10⁻⁸** |
| Sign test p (two-sided) | **7.28×10⁻¹²** |
| Cohen's d_z | **-0.31** |

## Key conclusions

1. EXP10 **confirms and strengthens** EXP4: median comparison eliminates the sole DRMacIver single-run win on `r20_60`.
2. IPSNS showed **zero objective variation** across 20 seeds (empirical stability, not determinism proof).
3. DRMacIver showed variability on **40/93** instances; benefits from restarts on a small subset.
4. **No additional major experiment** required before initial COAP submission.
5. Manuscript integrated at all 6 former `% EXP10-INTEGRATION` anchors; PDF builds cleanly (**44 pages**).

## Next task

**Construct Online Resource 1** (test suite, EXP10 full tables/figures, reproducibility bundle).
