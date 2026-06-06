# minimum-weighted-fas-heuristics

Code supporting the paper on **Minimum Weighted Feedback Arc Set (MWFAS)** heuristics for weighted directed graphs.

This repository consolidates code from:
- [weighted-minfas-local-ratio](https://github.com/SoroushVahidi/weighted-minfas-local-ratio)
- [weighted-minfas-codes](https://github.com/SoroushVahidi/weighted-minfas-codes)

---

## Algorithms

| Algorithm | Description |
|-----------|-------------|
| **LR-TA** | Local-Ratio cycle reduction with Topological Add-back |
| **WMSF**  | Weighted Minimum Spanning Forest baseline (paper049 pipeline) |
| **IPSNS** | Incumbent-Protected SCC-Neighborhood Search (LNS combining LR-TA and WMSF seeds) |

## Benchmarks

Instances come from [alidasdan/graph-benchmarks](https://github.com/alidasdan/graph-benchmarks).
Download and store `.d` files locally, then list their paths in `configs/benchmark_instances.txt`.

---

## Installation

```bash
pip install -r requirements.txt
pip install -e .        # installs the src/mwfas package in editable mode
```

> **Note:** `networkx`, `pyyaml`, and `tqdm` are listed in `requirements.txt` for completeness
> but are not required by the core algorithms (only `pandas` and the standard library are used).

---

## Usage

### Run a single instance

```bash
# LR-TA
python scripts/run_lrta.py --input /path/to/instance.d --output results/raw/lrta_instance.csv

# WMSF
python scripts/run_wmsf.py --input /path/to/instance.d --output results/raw/wmsf_instance.csv

# IPSNS
python scripts/run_ipsns.py --input /path/to/instance.d --output results/raw/ipsns_instance.csv
```

All scripts print: graph size, total/forward/backward weight, forward ratio, FAS size, and runtime.

### Reproduce all experiments

1. Edit `configs/benchmark_instances.txt` to list your instance file paths.
2. Run:

```bash
python scripts/reproduce_all.py \
    --instances configs/benchmark_instances.txt \
    --dataset-dir /path/to/datasets/ \
    --results-dir results/
```

A summary CSV is written to `results/processed/summary.csv`.

---

## Repository layout

```
minimum-weighted-fas-heuristics/
  README.md
  LICENSE
  .gitignore
  requirements.txt
  notebooks/
    local_ratio_original/   # original notebook from weighted-minfas-local-ratio
    ipsns_original/         # original notebook from weighted-minfas-codes
  src/
    mwfas/
      __init__.py
      io.py           # DIMACS reader
      evaluation.py   # forward/backward weight evaluation
      lrta.py         # LR-TA algorithm
      wmsf.py         # WMSF algorithm
      ipsns.py        # IPSNS algorithm
  scripts/
    run_lrta.py
    run_wmsf.py
    run_ipsns.py
    reproduce_all.py
  configs/
    benchmark_instances.txt
    lrta_default.yaml
    ipsns_default.yaml
    sensitivity.yaml
  results/
    raw/
    processed/
    tables/
  docs/
    repository_notes.md
    README_weighted-minfas-local-ratio.md
    README_weighted-minfas-codes.md
```

---

## License

MIT — see [LICENSE](LICENSE).
