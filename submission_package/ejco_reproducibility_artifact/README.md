# Anonymous Reproducibility Artifact

This package supports the EJCO manuscript
``Local-Ratio Seeding and SCC-Based Refinement for the Minimum Weighted
Feedback Arc Set Problem''.
It contains the implementation, experiment support scripts, selected committed
summaries, manuscript-facing CSV tables, and documentation needed to inspect
the reported results without exposing author identity.

## Included

- `src/mwfas/` core implementation modules
- `scripts/` command-line wrappers for the reported methods
- selected experiment configs, postprocessors, committed summaries, and manuscript-facing tables
- dataset and baseline reference notes

## Excluded

- Git history and repository metadata
- raw experiment outputs, logs, downloads, and external cloned tools
- manuscript PDFs and TeX build artifacts
- private paths, personal identifiers, and submission files outside this package

## Dependency setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

## Inspect committed summaries

- `experiments/combined/tables/` contains the manuscript-facing CSV tables.
- experiment-specific `summary/` and `tables/` directories contain the committed supporting files.
- EXP1b through EXP9 are represented across the bundled experiment directories,
  with EXP6--EXP9 included for the later-budget, local-search, medium-MIP, and
  application-case studies.

## Optional reruns

Time-consuming reruns are documented in `REPRODUCE.md`. Full reruns are optional and may
depend on external tools, dataset access, and the local software environment.

## Public dataset and tool sources

- graph-benchmarks: https://github.com/alidasdan/graph-benchmarks
- LOLIB: https://grafo.etsii.urjc.es/optsicom/lolib.html
- python-igraph: https://python.igraph.org/
- DRMacIver/FAS: https://github.com/DRMacIver/Feedback-Arc-Set

No author-identifying information is intentionally included in this artifact.
A public repository and archival release will be provided after acceptance.
