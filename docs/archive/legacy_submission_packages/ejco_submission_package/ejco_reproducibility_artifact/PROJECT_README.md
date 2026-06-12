# Project Overview

This artifact packages the anonymous code and benchmark-facing experiment
materials used to support the manuscript's reported results for the EJCO paper
``Local-Ratio Seeding and SCC-Based Refinement for the Minimum Weighted
Feedback Arc Set Problem''.

## Included components

- `src/mwfas/`: LR-TA, WMSF, IPSNS, exact DP, evaluation, and I/O helpers
- `scripts/`: command-line entry points for the reported methods and external wrappers
- `experiments/`: selected configs, postprocessors, committed summaries, and manuscript-facing tables
- `docs/baselines_and_datasets_references.md`: dataset and baseline provenance notes

## Scope

The bundled experiment materials cover EXP1b-EXP9. Public benchmark data are not
redistributed here; instead, the artifact includes the instance lists, conversion
utilities, and committed summary tables used to support the manuscript-facing
results. Later experiments are included in summarized form, with configs and
processed outputs retained and raw inputs omitted where the public datasets can
be obtained separately.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
python -m compileall src/mwfas scripts
```

See `README.md`, `REPRODUCE.md`, and `experiments/README.md` for inspection and rerun guidance.
