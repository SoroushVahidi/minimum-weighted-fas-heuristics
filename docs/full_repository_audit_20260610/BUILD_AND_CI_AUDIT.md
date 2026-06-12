# Build, Environment, and CI/CD Audit

**Audit date:** 2026-06-10

## Python environment

| Item | Observed |
|---|---|
| Python | 3.12.3 (pytest run) |
| Dependencies | `requirements.txt`: numpy, pandas, networkx, pyyaml, tqdm |
| Lock file | **None** |
| setup.py | Present (`pip install -e .`) |
| Conda | **None** |
| Optional deps | scipy (EXP8 MIP), python-igraph (EXP4), HiGHS via scipy |

## Other runtime requirements

| Tool | Used for |
|---|---|
| Java/C/R/C++ | **Not required** for core pipeline |
| DRMacIver FAS | C binary in external clone |
| TeX | Tectonic/latexmk for `paper_coap/main.pdf` |
| tmux | Long experiment sessions |

## Reproducibility across machines

| Risk | Detail |
|---|---|
| Unpinned numpy/pandas versions | Float summation order may differ slightly |
| Absolute dataset paths | Breaks without `/home/soroush/benchmark_sources/` |
| External tools gitignored | Manual clone required |
| No Docker/conda env | Reviewer must assemble environment |

## Clean install test

**Not performed** — would not interfere with holdout (no shared venv with experiment). `requirements.txt` install is minimal and likely insufficient for EXP4/EXP8 without extra packages.

## CI/CD

| Item | Status |
|---|---|
| GitHub Actions | **Absent** (no `.github/`) |
| Automated tests | **None** |
| PDF build workflow | **None** |
| Citation validation | **None** |
| Artifact hash checks | **None** |
| Linting | **None** |
| Release process | **None** |

## Recommendations

1. Add `requirements-dev.txt` or `pyproject.toml` with pinned versions
2. Document optional extras: `requirements-exp4.txt`, `requirements-exp8.txt`
3. GitHub Actions: pytest on push; optional tectonic build on `paper_coap/` changes
4. Pre-submission: record `pip freeze` for COAP ESM README
