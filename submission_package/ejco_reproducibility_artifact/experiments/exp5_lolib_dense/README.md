# EXP5 — LOLIB Dense Benchmark

## Purpose

Evaluate LR-TA, WMSF, and IPSNS on **dense tournament instances** from the LOLIB benchmark,
the standard testbed for the Linear Ordering Problem (LOP). These instances are fundamentally
different from the sparse DIMACS graph-benchmarks used in EXP1b–EXP4:

- LOLIB: complete tournament (every pair of nodes has a weight in both directions)
- alidasdan: sparse graphs from real circuits, programs, and networks

EXP5 tests whether our methods remain competitive on the denser, harder instances
that are the LOP community's standard benchmark.

## LOLIB → MWFAS Conversion

Given an n×n LOLIB weight matrix C:
- Create nodes 1..n
- For every ordered pair i≠j, create arc i→j with weight C[i][j]
- Diagonal C[i][i] is ignored
- Total off-diagonal weight = Σ_{i≠j} C[i][j]
- **Forward weight** of ordering π = Σ C[i][j] where π(i) < π(j)  (LOP objective: maximize)
- **Backward weight** of ordering π = total − forward               (MWFAS objective: minimize)

The converter writes only nonzero arcs; zero-weight arcs contribute 0 to the objective.

## Data Source

Downloaded from Marti's Dropbox (accessible 2026-06-06):
`https://www.dropbox.com/s/fk105g63jmi3i1d/lolib_2010.zip?dl=1`

Archive contains families: SGB, IO, MB, RandA1, RandA2, RandB, Spec, xLOLIB.

**Note:** The canonical LOLIB hosting at `grafo.etsii.urjc.es/optsicom/lolib.html`
(GitHub Pages) returns 404 for all direct ZIP download links. Marti's page
`www.uv.es/~rmarti/paper/lop.html` provides a working Dropbox alternative.

## Selected Subset (50 instances)

| Family | n | Count | Notes |
|--------|---|-------|-------|
| SGB | 75 | 25 | All 25 instances (N-sgb75.01..25) |
| IO | 44–79 | 10 | N-be75eec/np/oi/tot, N-usa79, N-stabu70/74/75, N-tiw56n54/r54 |
| RandA1 | 100 | 5 | N-t1d100.01..05 |
| RandA1 | 150 | 5 | N-t1d150.01..05 |
| RandA1 | 200 | 5 | N-t1d200.01..05 |

n=500 RandA1 instances excluded from this run (too large for exploratory benchmark).

## Baselines

| Algorithm | Type |
|-----------|------|
| lrta_full | Ours |
| wmsf_seed | Ours |
| ipsns_full | Ours |
| borda_net_score | External baseline |
| weighted_eades | External baseline |
| random_multistart | External baseline |
| drmaciver_fas | External baseline (DRMacIver, appropriate for tournaments) |
| igraph_approx_eades | External baseline |

LOP_MA-EDM was checked but not used (see access report).

## Metrics

- **backward_weight**: MWFAS objective (minimize)
- **forward_weight**: LOP objective (maximize)
- **forward_ratio**: forward_weight / total_off_diagonal_weight
- **runtime**: wall-clock time in seconds
- **status**: success / timeout / error

Best-known solution (BKS) values for comparison: not yet loaded.
If BKS forward values are available, report gap = (BKS_forward − our_forward) / BKS_forward.

## Known Caveats

- All algorithms assume nonneg weights; LOLIB standard instances are all nonneg.
- drmaciver_fas uses tournament-specific routines; expected to perform well here.
- IPSNS uses `--wmsf-seed-mode full` (required for incumbent protection guarantee).
- Dense instances (n=200, n*n=40000 arcs) may be slower than sparse DIMACS instances.

## Directory Layout

```
exp5_lolib_dense/
  README.md               (this file)
  configs/
    exp5_lolib_plan.yaml  — experiment plan
    exp5_lolib_instances.txt — selected instance manifest
    tiny_lolib_test.lop   — tiny 4×4 synthetic test
  converted/
    SGB/  IO/  RandA1/  tiny/   — DIMACS .d + .meta.json per instance
  downloads/              — (gitignored) lolib_2010.zip
  raw/                    — (gitignored) per-run ordering CSVs
  logs/                   — (gitignored) tmux run log
  external_tools/         — (gitignored) LOP_MA-EDM clone
  summary/
    exp5_lolib_access_report.md
    exp5_lolib_raw_summary.csv  (after run)
    exp5_lolib_stats.json       (after postprocess)
    exp5_lolib_summary.md       (after postprocess)
  tables/
    exp5_lolib_paper_summary.csv  (after postprocess)
    exp5_lolib_wide_summary.csv   (after postprocess)
  run_exp5_lolib_benchmark.py
  postprocess_exp5_lolib.py
  run_exp5_lolib_tmux.sh
```

## Status

- [x] Directory structure created
- [x] LOLIB archive downloaded (lolib_2010.zip, 10.7 MB)
- [x] Converter implemented (scripts/convert_lolib_to_dimacs.py)
- [x] Evaluator implemented (scripts/evaluate_order_lop.py)
- [x] Tiny 4×4 synthetic test passed
- [x] 50 target instances converted to DIMACS
- [ ] Smoke test (3–5 instances)
- [ ] Full EXP5 run in tmux
- [ ] Postprocessing
