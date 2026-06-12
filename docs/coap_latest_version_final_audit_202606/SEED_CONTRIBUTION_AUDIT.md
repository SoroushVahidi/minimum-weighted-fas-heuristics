# Seed Contribution Audit

Source: `experiments/exp1b_core_benchmark_full_wmsf_seed/tables/exp1b_core_benchmark_paper_summary.csv`

## Comparator definition

On each instance, seed BW = `min(lrta_bw, wmsf_bw)` stored as `best_seed_bw`. Recomputation confirmed **0 comparator mismatches** across 97 standard instances.

## Primary outcome (97 standard nonnegative instances)

| Outcome | Count |
|---|---:|
| Strict improvements | **14** |
| Ties | **83** |
| Regressions | **0** |

Tolerance: `ipsns_gain_over_best_seed` with threshold \(10^{-9}\).

## Distribution summary

| Statistic | Value |
|---|---:|
| Mean absolute improvement (BW) | 570.9 |
| Median absolute improvement | 0 |
| Maximum absolute improvement | 35,707 (`rd_big`) |
| Mean relative improvement (%) | 0.42 |
| Median relative improvement (%) | 0.0 |
| Instances with nonzero improvement | 14 |

## Distinction from DRMacIver repeated-run result

| Comparison | Protocol | Result |
|---|---|---|
| IPSNS vs better seed | Single run, 97 instances | **14 / 83 / 0** |
| IPSNS vs DRMacIver/FAS | 20 runs, median BW, 93 common instances | **38 / 55 / 0** |

These are reported separately in the abstract, Table seed contribution, and Table repeated-run.

## Accepted-move logging

EXP10 run-level logs on the 93 common instances: **12/93** instances ever improved over seed; **87.1%** of IPSNS runs had zero accepted moves. Mean accepted-move count and time-to-best were **not logged** in primary EXP1b runs (stated in Table seed contribution).
