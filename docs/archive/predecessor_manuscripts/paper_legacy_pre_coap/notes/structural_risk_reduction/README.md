# Structural Risk-Reduction Pass — README

## What was computed
- Graph features extracted from 95 sparse benchmark instances
  (benchmark_sources/graph-benchmarks/) and 50 LOLIB converted DIMACS files.
- Features: n, m, density, n nontrivial SCCs, largest SCC fraction, fraction in nontrivial SCCs,
  fraction of arcs internal to SCCs, acyclicity.
- Spearman correlations of IPSNS gain (vs LR-TA and vs DRMacIver/FAS) with graph features.
- Quantile summaries of IPSNS gain by largest-SCC-fraction quartile.
- Sparse vs dense structural comparison table.

## What was NOT recomputed
- No algorithm runs were performed.
- All BW and runtime values are from committed EXP4/EXP5 result CSVs.

## Missing instance files
- Sparse: 0 instances in EXP4 set had no matching file
  (these are likely instances excluded from the standard set or deduplication cases).
- LOLIB: 0 missing.

## Files generated
- graph_features_sparse.csv — per-instance features for sparse benchmark
- graph_features_lolib.csv — per-instance features for LOLIB benchmark
- ipsns_gain_feature_correlation.json/.md — Spearman correlations and quantile summaries
- sparse_dense_structural_diagnostic.json/.md — aggregate comparison
- paper/tables/table_structural_diagnostic.tex — compact LaTeX table

## Manuscript files updated
(see parent analysis for details)
