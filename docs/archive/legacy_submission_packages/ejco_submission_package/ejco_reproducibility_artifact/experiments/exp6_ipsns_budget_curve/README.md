# EXP6: IPSNS Budget Curve

## Purpose
Produce a quality-vs-runtime curve for IPSNS across multiple iteration budgets
on a representative sparse subset. EXP4 uses the full 400-iteration budget.
This experiment tests 10, 25, 50, 100, 200, 400 iterations on 20 selected
instances to show where quality saturates relative to runtime cost.

## Budgets tested
10, 25, 50, 100, 200, 400 (iterations)

## Subset-selection rule
Deterministic selection of 20 instances from the 97-instance standard sparse set:
- Top-5 IPSNS-gain instances (highest IPSNS improvement over LR-TA from EXP4)
- 5 zero-gain/tie instances (IPSNS = LR-TA)
- 5 instances from density quartiles (one per quantile range)
- 5 instances from size (n) quantiles
- De-duplicated; instances with missing source files excluded.

## Metrics
For each budget: mean BW, mean/median improvement over LR-TA, W/T/L vs LR-TA,
mean/median runtime, relative excess vs full-budget result.

## Expected runtime
~15–30 minutes for 20 instances × 6 budgets on a single CPU.

## How to rerun
```
python3 scripts/select_exp6_ipsns_budget_instances.py
python3 scripts/run_exp6_ipsns_budget_curve.py --budgets 10,25,50,100,200,400
python3 scripts/postprocess_exp6_ipsns_budget_curve.py
```

## Note
EXP1b–EXP5 are not modified. EXP4 results are used as baselines for
LR-TA, WMSF, and full-IPSNS on the selected subset.
