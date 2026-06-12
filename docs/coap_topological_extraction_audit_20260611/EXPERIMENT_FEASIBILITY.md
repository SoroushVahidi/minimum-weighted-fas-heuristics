# EXP11 feasibility

## Available artifacts

| Data | Stored? | Notes |
|------|---------|-------|
| Final rankings (CSV) | Yes | EXP4 raw |
| Backward weights | Yes | Summaries |
| Active edge flags | No | Reconstruct via `local_ratio_fas_fast` |
| Removed sets | No | Same |
| Method intermediates | No | |

## Evaluation paths

| Approach | Cost | Used |
|----------|------|------|
| Post-hoc extraction on reconstructed active DAG | Low (seconds per small instance) | **Yes (EXP11)** |
| Full IPSNS rerun | High | Not needed |
| Full EXP4 rerun | Very high | Not needed |

## Burden

EXP11 calibration (8 instances configured, 6 nonnegative analyzed): **~9 s** on LR-TA final states only.
