# Statistical Audit

Source: `experiments/exp10_stochastic_robustness/summary/statistical_tests.json` and `scripts/finalize_exp10.py`.

## Repeated-run primary comparison (IPSNS vs DRMacIver/FAS)

| Item | Value |
|---|---|
| Instances | 93 common sparse subset |
| Runs per method | 20 |
| Unit | per-instance median BW |
| Tie tolerance | \(10^{-9}\) |
| Wins / ties / losses | **38 / 55 / 0** |
| Nonzero paired differences | 38 |
| Mean paired BW difference (IPSNS − DR) | −23,964 |
| Median paired difference | 0 |
| Mean comparator-normalized reduction | 21.60% |
| Median comparator-normalized reduction | 0.0% |

## Wilcoxon signed-rank test

| Parameter | Value |
|---|---|
| SciPy version | 1.17.1 |
| Function | `scipy.stats.wilcoxon` |
| Alternative | two-sided |
| zero_method | wilcox |
| method | default `auto` (not archived in JSON) |
| Statistic W | 0 |
| p-value (two-sided) | 7.74×10⁻⁸ |

## Sign test

| Item | Value |
|---|---|
| IPSNS better | 38 |
| DR better | 0 |
| Ties excluded | 55 |
| p-value (two-sided) | 7.28×10⁻¹² |

## Effect size

Cohen's \(d_z = -0.31\); bootstrap 95% CI for mean paired difference: [−41,787, −10,718].

## Presentation

Table repeated-run reports tests at comparison level, not attached to individual method rows.
