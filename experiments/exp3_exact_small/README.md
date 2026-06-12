# EXP3: Exact Small-Instance Optimality Validation

**Status:** COMPLETE

## Purpose

Validates heuristic quality against exact bitmask dynamic-programming optimal solutions
on instances with n ≤ 20 vertices.

## Benchmark set

67 instances total; 64 DP succeeded; 57 standard nonnegative instances (5 negative-weight
excluded: k3_3, ku, peterson, peterson1, peterson2).

## Methods

LR-TA, WMSF, IPSNS, and exact bitmask DP (`exact.py`, n ≤ 20 limit).

## Key results (standard nonnegative instances)

| Method | Optimal | Mean gap |
|--------|---------|----------|
| IPSNS  | 56/57 (98.2%) | 0.0006% |
| LR-TA  | 55/57 (96.5%) | 0.059% |
| WMSF   | 51/57 (89.5%) | 0.096% |

Only IPSNS near-miss: `r20_60` (also the sole EXP4 DRMacIver win; corrected in EXP10 median).

## Manuscript use

Exact-validation table; confirms near-optimality of IPSNS on small instances.

## Canonical summary

`summary/exp3_exact_stats.json`

## Raw output

Gitignored; regenerable with exact DP solver on the same instances.

## Rerun

```bash
PYTHONPATH=src python3 experiments/exp3_exact_small/scripts/run_exp3_exact.py
```
