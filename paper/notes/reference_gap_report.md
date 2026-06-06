# Reference Gap Report

The merged `paper/references.bib` is extracted from predecessor manuscripts and needs verification before final manuscript writing.

## Must Verify or Add

- Demetrescu--Finocchi local-ratio feedback arc set reference and exact statement of inherited result.
- Eades--Lin--Smyth feedback arc set heuristic reference.
- `igraph` feedback arc set implementation citation and version-appropriate documentation.
- DRMacIver `Feedback-Arc-Set` package citation or repository reference.
- graph-benchmarks / Alidaee benchmark provenance.
- LOLIB and linear ordering benchmark source citation.
- LOP_MA-EDM / Segura dense linear ordering baseline citation if discussed.
- GNNRank ICML 2022 citation if used as a ranking baseline or contextual comparison.
- Cavallaro--Cutello--Pavone minimal stable feedback arc set citation if used.
- Simpson--Srinivasan web-scale feedback arc set citation if used.
- Baharev exact MWFAS method citation if exact methods are discussed.

## Result-Source Dependencies

- EXP1b and EXP4 sparse benchmark claims should be checked against `experiments/combined/summary/manuscript_results_digest.md`.
- EXP2 ablation claims should be checked against `experiments/combined/tables/manuscript_table_ablation.csv`.
- EXP3 exact-validation claims should be checked against `experiments/combined/tables/manuscript_table_exact_small.csv`.
- EXP5 dense LOLIB scope-boundary claims should be checked against `experiments/combined/tables/manuscript_table_lolib_dense.csv`.

## Citation Discipline

Do not cite a predecessor manuscript as authority for an algorithmic or empirical claim. Cite the original literature, official tool repositories/documentation, benchmark sources, and the new repository once it is public.
