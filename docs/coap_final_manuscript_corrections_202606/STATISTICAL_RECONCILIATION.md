# Statistical Reconciliation

All values below are from tracked experiment outputs; none were invented.

## Primary sparse comparison (Panel A, 93 common instances)

| Method | Mean BW | Best (tie-credited) | IPSNS reduction vs method (%) |
|---|---:|---:|---:|
| IPSNS | 29,586 | 92 | 0.00 |
| LR-TA | 30,197 | 78 | 0.70 |
| WMSF seed | 31,535 | 59 | 1.96 |
| DRMacIver/FAS | 53,173 | 56 | 21.14 |

## 97-instance tie analysis

- Minimum observed among evaluated methods (tie-credited): **96 / 97**
- Unique best (IPSNS alone): **14**
- Strict wins over all other evaluated methods: **14**

## IPSNS vs best seed (97 standard instances, EXP1b)

- Strict improvements: **14**
- Ties: **83**
- Regressions: **0**

## Exact validation (57 standard instances, n>0, nonnegative)

Mean optimum-normalized gap (%):

| Method | Mean gap | Optimal count |
|---|---:|---:|
| IPSNS | 0.003 | 56/57 |
| LR-TA | 0.003 | 56/57 |
| WMSF | 0.003 | 56/57 |

## Repeated-run comparison (93 instances × 20 runs, EXP10)

- IPSNS vs DRMacIver/FAS (paired medians): **38 / 55 / 0** (W/T/L)
- Mean comparator-normalized reduction: **21.60%**
- Wilcoxon: SciPy 1.17.1, `alternative="two-sided"`, `zero_method="wilcox"`, W=0, p<0.001
- Sign test p<0.001; Cohen's d_z = −0.31

## Zero-variance interpretation (EXP10 IPSNS)

- One distinct BW value on all 93 instances under fixed configuration.
- Zero objective variance reported as stable final objectives, not proof of identical search trajectories.
