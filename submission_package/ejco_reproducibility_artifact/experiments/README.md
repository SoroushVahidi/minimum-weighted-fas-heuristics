# Experiments

This directory contains the anonymous experiment materials bundled with the reproducibility
artifact. Raw outputs, logs, downloads, and external cloned tools are intentionally omitted;
the artifact instead includes selected configs, committed summaries, and manuscript-facing tables.

## Included experiment packages

| Experiment | Purpose | Included materials |
|---|---|---|
| **EXP1b** | Main sparse benchmark with full WMSF seed | configs, postprocessor, summaries, paper/wide tables |
| **EXP2** | Ablation study | README, configs, launcher, summaries, table |
| **EXP3** | Exact small-instance validation | config, launcher, summaries, table |
| **EXP4** | External baseline comparison on standard sparse instances | registry, launchers, postprocessor, summaries, paper/wide tables |
| **EXP5** | LOLIB dense transfer test | README, configs, launcher, postprocessor, summaries, paper/wide tables |

## Combined manuscript-facing tables

- `combined/tables/manuscript_table_core_sparse.csv`
- `combined/tables/manuscript_table_ablation.csv`
- `combined/tables/manuscript_table_exact_small.csv`
- `combined/tables/manuscript_table_external_sparse.csv`
- `combined/tables/manuscript_table_lolib_dense.csv`

## Notes

- Standard benchmark claims use the nonnegative-weight subset only.
- LOLIB is included as a dense transfer test rather than the primary sparse benchmark.
- Scripts for later manuscript diagnostics and the application-facing public ordering example
  are provided under `../scripts/`, but their large raw outputs are not bundled here.
