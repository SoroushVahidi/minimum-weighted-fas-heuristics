# minimum-weighted-fas-heuristics

A reproducible implementation and experimental framework for **Minimum Weighted Feedback Arc Set (MWFAS)** heuristics in weighted directed graphs.

This repository merges and extends two predecessor works:
[weighted-minfas-local-ratio](https://github.com/SoroushVahidi/weighted-minfas-local-ratio)
and [weighted-minfas-codes](https://github.com/SoroushVahidi/weighted-minfas-codes).
See `docs/repository_notes.md` and `docs/provenance/predecessor_project_manifest.md`.

> **Note:** Repository is currently **private** while the manuscript is under preparation.

---

## Algorithms

| Algorithm | Description | Module |
|-----------|-------------|--------|
| **LR-TA** | Local-Ratio cycle reduction + Topological Add-Back | `src/mwfas/lrta.py` |
| **WMSF** | Weighted Minimum Spanning Forest (removeArcs/Minimize/Stabilize pipeline) | `src/mwfas/wmsf.py` |
| **IPSNS** | Incumbent-Protected SCC Neighborhood Search (LNS combining LR-TA and WMSF seeds) | `src/mwfas/ipsns.py` |
| **Exact DP** | Bitmask DP exact solver for small instances (n ≤ 20) | `src/mwfas/exact.py` |
| **Baselines** | Borda score, Weighted Eades, random multistart, igraph approx Eades, DRMaciver | `src/mwfas/baselines.py` |

**Important caveat:** All algorithms and analyses assume **non-negative edge weights**.
Instances with negative-weight edges are excluded from standard paper comparisons
(see `experiments/exp4_external_baselines/summary/exp4_external_report.md`).

---

## Installation

```bash
pip install -r requirements.txt
pip install -e .        # installs src/mwfas as an editable package
```

Benchmark instances come from [alidasdan/graph-benchmarks](https://github.com/alidasdan/graph-benchmarks).
Download `.d` files and list their paths in `configs/benchmark_instances.txt`.

> `networkx`, `pyyaml`, and `tqdm` are in `requirements.txt` for completeness
> but are not required by the core algorithms (only `pandas` and the standard library are used).

---

## Quick Usage

```bash
# LR-TA
python scripts/run_lrta.py --input /path/to/instance.d --output results/raw/lrta_out.csv

# WMSF
python scripts/run_wmsf.py --input /path/to/instance.d --output results/raw/wmsf_out.csv

# IPSNS (always use --wmsf-seed-mode full)
python scripts/run_ipsns.py --input /path/to/instance.d --output results/raw/ipsns_out.csv \
    --wmsf-seed-mode full

# Exact DP (small instances only, n ≤ 20)
python scripts/run_exact.py --input /path/to/instance.d --output results/raw/exact_out.csv

# External baseline: Borda score ranking
python scripts/run_borda.py --input /path/to/instance.d --output results/raw/borda_out.csv
```

All scripts print: graph size, total/forward/backward weight, forward ratio, FAS size, and runtime.

---

## Experiments

See [`experiments/README.md`](experiments/README.md) for the full experiment table and output paths.

| Experiment | Purpose | Status |
|---|---|---|
| **EXP1b** | Main benchmark: 105 instances, full WMSF seed | Complete |
| **EXP2** | Ablation: 8 component variants, 10 instances | Complete |
| **EXP3** | Exact small-instance optimality check (n ≤ 20) | Complete |
| **EXP4** | External baseline comparison: 8 algorithms, 97 standard instances | Complete |
| **EXP5** | LOLIB dense benchmark | In Progress |

### Key headline results (EXP4, 97 standard non-negative instances)

| Algorithm | Mean BW | vs IPSNS |
|---|---|---|
| **IPSNS** | **37,698** | — |
| LR-TA | 38,327 | +0.71% |
| WMSF | 40,005 | +2.06% |
| DRMaciver (external) | 53,173 | +21.6% |
| igraph Eades (external) | 95,920 | +30.5% |

IPSNS achieves the global minimum backward weight on **96/97 standard instances**
with 0 incumbent-protection violations (guaranteed IPSNS ≤ LR-TA and IPSNS ≤ WMSF).

---

## Repository Layout

```
minimum-weighted-fas-heuristics/
  README.md
  LICENSE
  .gitignore
  requirements.txt
  setup.py
  src/
    mwfas/
      __init__.py
      io.py           # DIMACS reader
      evaluation.py   # forward/backward weight evaluation
      lrta.py         # LR-TA algorithm
      wmsf.py         # WMSF algorithm
      ipsns.py        # IPSNS algorithm
      exact.py        # bitmask DP exact solver
      baselines.py    # Borda, WeightedEades, random, igraph, DRMaciver wrappers
  scripts/
    run_lrta.py / run_wmsf.py / run_ipsns.py
    run_exact.py
    run_borda.py / run_weighted_eades.py / run_random_baseline.py
    run_igraph_eades.py / run_drmaciver_fas.py
    reproduce_all.py
  configs/
    benchmark_instances.txt
    lrta_default.yaml / ipsns_default.yaml / sensitivity.yaml
  experiments/
    exp1b_core_benchmark_full_wmsf_seed/   # definitive main benchmark (EXP1b)
    exp2_ablation/                          # ablation study (EXP2)
    exp3_exact_small/                       # exact optimality check (EXP3)
    exp4_external_baselines/                # external comparison (EXP4)
    exp1_core_benchmark/                    # legacy (superseded by EXP1b)
  notebooks/
    local_ratio_original/   # original notebook from weighted-minfas-local-ratio
    ipsns_original/         # original notebook from weighted-minfas-codes
  docs/
    repository_notes.md
    paper_status_20260606.md
    provenance/
      predecessor_project_manifest.md
  archive/
    predecessor_projects/   # LaTeX manuscript ZIPs from predecessor submissions
  results/                  # local run outputs (gitignored; regenerable)
```

---

## License

MIT — see [LICENSE](LICENSE).
