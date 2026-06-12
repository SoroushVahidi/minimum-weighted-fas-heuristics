# EXP6 IPSNS Budget Curve — Notes README

## Purpose
Produce a quality-vs-runtime (budget) curve for IPSNS on a 20-instance
representative sparse subset to address reviewer questions about runtime justification.

## Inputs
- experiments/exp6_ipsns_budget_curve/config/selected_instances.csv (20 instances)
- experiments/exp6_ipsns_budget_curve/summary/exp6_raw_summary.csv (120 rows)
- experiments/exp4_external_baselines/summary/exp4_raw_summary.csv (LR-TA/WMSF baselines)

## Outputs
- exp6_budget_summary.csv — aggregate metrics per budget
- exp6_final_report.md — full report
- paper/tables/table_ipsns_budget_curve.tex — LaTeX table
- paper/figures/exp6_ipsns_budget_curve.pdf — quality and saturation plots

## Key findings
- IPSNS never loses to LR-TA at any budget on this subset.
- Quality improves rapidly from budget 10 to 50; saturation is near at 100-200.
- LR-TA mean RT: 0.0346 s; IPSNS at 50 iters: 0.6976 s.
- Full 400-iter budget adds further improvement on the highest-gain instances.
