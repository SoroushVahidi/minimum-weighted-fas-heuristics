# Statistical Interpretation (EXP10)

## Primary confirmatory comparison

- **Unit:** per-instance median backward weight (93 instances)
- **Tie tolerance:** 1×10⁻⁹
- **Relative excess denominator:** DRMacIver median BW (EXP4 convention)

## Results

| Statistic | Value |
|-----------|-------|
| Wilcoxon signed-rank W | 0.0 |
| Wilcoxon p (two-sided) | 7.74×10⁻⁸ |
| Sign test: IPSNS better / DR better / tie | 38 / 0 / 55 |
| Sign test p (two-sided) | 7.28×10⁻¹² |
| Mean paired difference (IPSNS − DR) | −23,964 BW |
| Median paired difference | 0 |
| Mean relative excess (DR over IPSNS) | 21.60% |
| Median relative excess | 0% |
| Cohen's d_z | −0.31 |
| Bootstrap 95% CI mean diff | [−41,787, −10,718] |
| Bootstrap 95% CI mean rel excess | [15.39%, 28.10%] |
| Bootstrap seed / n | 42 / 10,000 |

## Practical significance

The mean 21.6% relative excess matches EXP4 and indicates a substantial average gap on this subset, driven primarily by instances where IPSNS strictly wins (38) rather than ties (55).

## Caveats

- Tests characterize distributional asymmetry; they do not certify optimality.
- IPSNS zero cross-seed variance is documented as empirical stability, not a determinism theorem.
- Comparison is quality-focused, not equal-time.
