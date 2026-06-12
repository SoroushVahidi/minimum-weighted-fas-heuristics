# EXP3 Exact-Validation Mean Gap (0.0006%)

**Date:** 2026-06-12  
**Purpose:** Reconcile the manuscript exact-validation mean gap with the `r20_60` near-miss and the separate 0.178% optimum-normalized figure.

## Data source

- Per-instance table: `experiments/exp3_exact_small/tables/exp3_exact_summary.csv`
- Committed aggregate: `experiments/exp3_exact_small/summary/exp3_exact_stats.json`
- Generator logic: `experiments/exp3_exact_small/run_exp3_exact_tmux.sh` (embedded postprocess)

## Standard subset (57 instances)

Include rows with:

- `exact_status == ok`
- `n > 0`
- `exact_bw >= 0`
- exclude negative-weight instances: `k3_3`, `ku`, `peterson`, `peterson1`, `peterson2`

## Per-instance gap formula

For each instance with total weight `W > 0`:

\[
\text{gap\_rel} = \frac{\text{ipsns\_bw} - \text{exact\_bw}}{W}
\]

Committed CSV column: `ipsns_gap_rel`.

## Aggregation formula

\[
\text{mean\_gap\_pct} = 100 \times \frac{1}{57}\sum_{i=1}^{57} \text{gap\_rel}_i
\]

Rounded to four decimal places in the committed stats JSON (`:.4f%`).

## Reproduced result (2026-06-12)

| Quantity | Value |
|---|---|
| IPSNS optimal | 56/57 (98.2%) |
| IPSNS mean gap | **0.0006%** |
| LR-TA mean gap | 0.0590% |
| WMSF mean gap | 0.0961% |

Only non-optimal IPSNS case: `r20_60` with `exact_bw=1685`, `ipsns_bw=1688`, `gap_abs=3`, `total_weight=9234`.

## Why 0.0006% is not the same as 0.178%

These are different normalizations for the same near-miss:

| Normalization | Formula for `r20_60` | Value |
|---|---|---|
| Table mean-gap convention | `gap_abs / total_weight` | `3 / 9234 = 0.0325%` contribution to mean |
| Optimum-normalized (manuscript prose) | `gap_abs / exact_bw` | `3 / 1685 = 0.178%` |

The table mean averages `gap_abs / total_weight` across all 57 standard instances. Because 56 instances contribute exactly zero, the mean is dominated by the single `r20_60` contribution:

\[
\frac{3/9234}{57} \times 100 \approx 0.000570\% \rightarrow 0.0006\% \text{ (rounded)}
\]

The 0.178% figure is reported separately when describing the sole near-miss relative to the certified optimum or MIP incumbent on `r20_60`. It is not the exact-validation mean-gap statistic.

## Verdict

**Conclusion A:** `0.0006%` is correct under the committed total-weight mean-gap convention. The manuscript table footnote and Section 6.2 prose already distinguish this from the 0.178% optimum-normalized gap on `r20_60`.
