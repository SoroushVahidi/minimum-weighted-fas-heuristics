# EXP8 Medium MIP Baseline — Paper Notes

## Purpose
Supplementary time-capped MIP validation on medium sparse instances where
bitmask DP is no longer feasible. Provides additional exact-quality evidence
to complement the small-instance exact validation (57 instances, n≤20).

## Key aggregate results
- Instances selected: 15 (n=20–318, all from graph-benchmarks)
- Proven optimal: 7/15 (HiGHS MIP solved within 120 s)
- Time-limited, no incumbent: 8/15 (LP relaxation mode, n≥273)
- IPSNS matches MIP optimum: 6/7
- IPSNS mean gap on proven-optimal: 0.025%
- IPSNS max gap on proven-optimal: 0.178% (r20_60)

## Interpretation notes
- The 8 time-limited cases are **incomplete solver evidence only**; they do
  not certify gaps and are not counted as IPSNS failures.
- The single exception (r20_60, gap 0.178%) is the same instance that is the
  only IPSNS near-miss in the small exact-validation study.
- The MIP solver used is scipy.optimize.milp (HiGHS 1.17.1).

## Files
- `experiments/exp8_medium_mip_baseline/summary/exp8_mip_raw_summary.csv` — 15 rows
- `experiments/exp8_medium_mip_baseline/summary/exp8_mip_summary.json` — aggregate JSON
- `experiments/exp8_medium_mip_baseline/summary/exp8_final_report.md` — human-readable report
- `paper/tables/table_medium_mip_baseline.tex` — LaTeX table for manuscript
