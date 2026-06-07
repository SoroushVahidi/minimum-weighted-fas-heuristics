# Results Asset Provenance

- Generated at (UTC): `2026-06-07T00:36:40.095797+00:00`
- Script: `paper/scripts/build_paper_results_assets.py`

## Source files

- `digest_json`: `experiments/combined/summary/manuscript_results_digest.json`
- `exp1b_stats`: `experiments/exp1b_core_benchmark_full_wmsf_seed/summary/exp1b_core_benchmark_stats.json`
- `exp2_stats`: `experiments/exp2_ablation/summary/exp2_ablation_stats.json`
- `exp3_stats`: `experiments/exp3_exact_small/summary/exp3_exact_stats.json`
- `exp4_stats`: `experiments/exp4_external_baselines/summary/exp4_external_stats.json`
- `exp4_table`: `experiments/exp4_external_baselines/tables/exp4_external_paper_summary.csv`
- `exp5_stats`: `experiments/exp5_lolib_dense/summary/exp5_lolib_stats.json`
- `exp5_table`: `experiments/exp5_lolib_dense/tables/exp5_lolib_paper_summary.csv`
- `exp5_report`: `experiments/exp5_lolib_dense/summary/exp5_final_report.md`

## Verification checks

| Check | Observed | Expected | Status |
|---|---:|---:|---|
| EXP1b instances | `105` | `105` | ok |
| EXP1b nonempty errors | `0` | `0` | ok |
| EXP1b incumbent violations | `0` | `0` | ok |
| EXP2 successful runs | `80` | `80` | ok |
| EXP3 standard instances | `57` | `57` | ok |
| EXP3 IPSNS optimal | `56/57 (98.2%)` | `56/57 (98.2%)` | ok |
| EXP3 IPSNS mean gap pct | `0.0006%` | `0.0006%` | ok |
| EXP4 standard instances | `97` | `97` | ok |
| EXP4 IPSNS complete | `97` | `97` | ok |
| EXP4 DRMaciver complete | `93` | `93` | ok |
| EXP4 DRMaciver relative gap pct | `21.61` | `21.61` | ok |
| EXP5 instances | `50` | `50` | ok |
| EXP5 IPSNS best count | `5` | `5` | ok |
| EXP5 DRMaciver best count | `45` | `45` | ok |
| EXP5 DRMaciver mean BW | `571687.0` | `571687.0` | ok |
| EXP5 family rows parsed | `['IO', 'RandA1', 'SGB']` | `['IO', 'RandA1', 'SGB']` | ok |

## Generated files

- `paper/tables/table_experiment_overview.tex`
- `paper/tables/table_sparse_external_baselines.tex`
- `paper/tables/table_exact_validation.tex`
- `paper/tables/table_ablation.tex`
- `paper/tables/table_lolib_scope.tex`
- `paper/figures/exp4_relative_bw.pdf`
- `paper/figures/exp4_win_counts.pdf`
- `paper/figures/exp5_lolib_scope.pdf`

## Notes

- EXP4 tables and figures are generated from the committed paper summary CSV.
- EXP5 overall metrics are generated from the committed paper summary CSV.
- EXP5 per-family DRMaciver and IPSNS means/best counts are parsed from the committed final report because the compact paper summary CSV does not include the family-level DRMaciver rows.
- No experiment values are inferred from uncommitted files.
