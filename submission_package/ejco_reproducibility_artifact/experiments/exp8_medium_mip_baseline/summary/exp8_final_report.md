# EXP8 MIP Baseline — Final Report

## Summary
- Instances: 15 total, 15 completed
- Proven optimal: 7
- Time limit hit: 8
- Errors / skipped: 0 / 0
- Mean runtime: 68.4 s

## IPSNS vs MIP Incumbent
- IPSNS matches MIP incumbent (gap < 0.001%): 6/7
- IPSNS better than MIP incumbent: 0/7

| Instance | n | Mode | MIP BW | IPSNS BW | Gap% | Optimal |
|---|---|---|---|---|---|---|
| stg | 20 | MIP | 5.0 | 5.0 | 0.0000 | Yes |
| r20_60 | 20 | MIP | 1685.0 | 1688.0 | 0.1780 | Yes |
| gr10 | 47 | MIP | 58481.0 | 58481.0 | 0.0000 | Yes |
| s27 | 54 | MIP | 1905.0 | 1905.0 | 0.0000 | Yes |
| s208 | 83 | MIP | 2829.0 | 2829.0 | 0.0000 | Yes |
| s420 | 101 | MIP | 158.0 | 158.0 | 0.0000 | Yes |
| mm4a | 170 | MIP | 4053.0 | 4053.0 | 0.0000 | Yes |

## IPSNS vs LP/MIP Lower Bound
| Instance | Mode | IPSNS Gap to Bound (%) |
|---|---|---|
| stg | MIP | 0.0000 |
| r20_60 | MIP | 0.1780 |
| gr10 | MIP | 0.0000 |
| s27 | MIP | 0.0000 |
| s208 | MIP | 0.0000 |
| s420 | MIP | 0.0000 |
| mm4a | MIP | 0.0000 |

## Interpretation
- 7 instance(s) proven optimal; IPSNS matches optimal on 6 of those.
- LP relaxation bounds available for LP-mode instances (n > 200).
