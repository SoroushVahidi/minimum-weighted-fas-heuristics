# EXP3: Exact Small-Instance Optimality Check

## Summary

- Instances with n ≤ 20: **64** (exact DP successful)
- Non-trivial instances (n > 0): **62**

## Optimality Rates

| Algorithm | Optimal | Mean Rel. Gap |
|-----------|---------|---------------|
| LR-TA     | 56/62 (90.3%) | 0.8771% |
| WMSF      | 52/62 (83.9%) | 0.9112% |
| IPSNS     | 57/62 (91.9%) | 0.8233% |

## Non-Optimal IPSNS Cases

| Instance | n | m | exact_bw | ipsns_bw | gap_abs | gap_rel |
|----------|---|---|----------|----------|---------|----------|
| k3_3 | 6 | 9 | -2221.0000 | -1234.0000 | 987.0000 | 0.081476 |
| peterson | 10 | 15 | -4396.0000 | -332.0000 | 4064.0000 | 0.148788 |
| peterson1 | 10 | 15 | -4396.0000 | -332.0000 | 4064.0000 | 0.148788 |
| peterson2 | 10 | 15 | -5268.0000 | -1688.0000 | 3580.0000 | 0.131068 |
| r20_60 | 20 | 60 | 1685.0000 | 1688.0000 | 3.0000 | 0.000325 |

## Key Files

- Summary CSV: `experiments/exp3_exact_small/tables/exp3_exact_summary.csv`
- Stats JSON: `experiments/exp3_exact_small/summary/exp3_exact_stats.json`
- Raw rankings: `experiments/exp3_exact_small/raw/`
