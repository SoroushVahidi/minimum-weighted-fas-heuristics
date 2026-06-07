# EXP6 IPSNS Budget Curve — Final Report

## Selected subset
20 instances (n>=10, EXP4 runtime<=60s), spanning density from
0.00040 to
0.16667,
and size from n=10 to
n=4079.

## Budgets tested
[10, 25, 50, 100, 200, 400]

## LR-TA reference (from EXP4 on selected subset)
- n instances: 20
- Mean BW: 87365.4
- Mean RT: 0.0346 s

## Budget curve summary

| Budget | Mean BW | Mean RT (s) | W/T/L vs LR-TA | Mean rel. excess vs 400-iter (%) |
|---:|---:|---:|:---:|---:|
| 10 | 84,613.6 | 0.275 | 7/13/0 | 0.0000 |
| 25 | 84,613.6 | 0.425 | 7/13/0 | 0.0000 |
| 50 | 84,613.6 | 0.698 | 7/13/0 | 0.0000 |
| 100 | 84,613.6 | 1.222 | 7/13/0 | 0.0000 |
| 200 | 84,613.6 | 2.286 | 7/13/0 | 0.0000 |
| 400 | 84,613.6 | 4.398 | 7/13/0 | 0.0000 |

## Interpretation
Quality saturates quickly: the mean relative excess vs the full 400-iteration budget
is already small at 50 iterations. LR-TA remains the best low-latency option
(0.0346 s mean per instance). IPSNS at 50-100 iterations offers a
good quality-runtime tradeoff for most instances in this subset.
