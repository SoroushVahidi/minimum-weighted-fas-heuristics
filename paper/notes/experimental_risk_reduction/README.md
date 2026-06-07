# Experimental Risk-Reduction Pass — README

## Purpose
Postprocessing analysis using existing committed result CSVs only.
No algorithms were rerun. No result values were fabricated or modified.

## Files read
- `experiments/exp4_external_baselines/summary/exp4_raw_summary.csv` — per-instance sparse results (984 rows, 8 algorithms)
- `experiments/exp5_lolib_dense/summary/exp5_lolib_raw_summary.csv` — per-instance LOLIB dense results (400 rows, 8 algorithms)
- `experiments/combined/tables/manuscript_table_external_sparse.csv` — aggregate sparse comparison summary

## Analyses computed from existing results
1. **Paired statistical tests** (`paired_sparse_tests.json/.md`): Wilcoxon signed-rank and sign test comparing IPSNS against each baseline on common completed sparse instances. scipy was available; Wilcoxon p-values are exact.
2. **IPSNS gain concentration** (`ipsns_gain_concentration.json/.md`): Distribution of per-instance improvement of IPSNS over LR-TA on the 105-instance internal set.
3. **Runtime-quality summary** (`runtime_quality_summary.json/.md`): Mean/median BW and runtime for each algorithm on completed EXP4 sparse instances.
4. **Sparse vs dense diagnostic** (`sparse_dense_diagnostic.json/.md`): Head-to-head IPSNS vs DRMacIver/FAS win counts and mean BW on sparse (EXP4) and dense LOLIB (EXP5) benchmarks, with per-family LOLIB breakdown.

## What was NOT recomputed
- No algorithm runs were performed.
- SCC counts per instance are not pre-computed in committed files; SCC-based feature correlation was not possible.
- A true quality-vs-iteration-budget curve for IPSNS is not available from existing outputs (only one iteration setting per experiment).

## Manuscript files updated
- `paper/sections/05_experimental_design.tex` — added two sentences about paired tests in the Evaluation Metrics subsection.
- `paper/sections/06_results.tex` — added statistical support paragraph and `\input{tables/table_paired_sparse_tests}` after the sparse external comparison.
- `paper/sections/07_discussion.tex` — added one sentence on runtime-quality tradeoff and IPSNS gain concentration.
- `paper/tables/table_paired_sparse_tests.tex` — new compact paired-test table.
- `paper/tables/table_runtime_quality_tradeoff.tex` — new runtime-quality table (not yet included in manuscript body; available for reviewer response).

## Analyses impossible due to missing data
- **SCC-feature correlation**: SCC counts not pre-computed; requires a new graph-feature extraction pass.
- **Quality-vs-budget curve**: Only one IPSNS iteration budget per experiment; a dedicated multi-budget run is needed.
- **DRMacIver/FAS 4 incomplete sparse instances**: No partial results available; reported as incomplete.
