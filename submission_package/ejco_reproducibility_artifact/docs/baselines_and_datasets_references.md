# Baselines and Datasets References

This document records the exact software versions, dataset sources, and fairness notes
for all external tools, baselines, and benchmark datasets used in this paper.
All information has been verified against local installation and repository inspection.

---

## Benchmark Datasets

### alidasdan/graph-benchmarks (EXP1b, EXP2, EXP3, EXP4)

| Field | Value |
|-------|-------|
| Repository | https://github.com/alidasdan/graph-benchmarks |
| Format | DIMACS `.d` arc format (weighted directed graphs) |
| Instances used | 123 files listed; 105 unique (18 duplicates removed by path dedup) |
| Standard (non-negative-weight) | 97 of 105 |
| Negative-weight excluded | k3_3, ku, peterson, peterson1, peterson2, gerez, howard-max, stg0 |
| Local path | `[graph-benchmarks root]/` |
| Instance list | `configs/benchmark_instances.txt` |

**Fairness note:** All DIMACS instances are public, widely used in FAS/graph benchmarking.
The alidasdan benchmark set is derived from real-world circuits, dependency graphs, and
other combinatorial instances; it is not synthetic.

### LOLIB 2010 Archive (EXP5)

| Field | Value |
|-------|-------|
| Primary page | https://grafo.etsii.urjc.es/optsicom/lolib.html |
| Author page | https://www.uv.es/~rmarti/paper/lop.html |
| Download (working) | https://www.dropbox.com/s/fk105g63jmi3i1d/lolib_2010.zip?dl=1 |
| Archive size | 10.7 MB (lolib_2010.zip) |
| Downloaded | 2026-06-06 |
| Families used | SGB (n=75), IO (n=44-79), RandA1 (n=100/150/200) |
| Instances used | 50 of ~275 in archive |
| Families not used | MB, RandA2, RandB, Spec, xLOLIB |
| Converted to | DIMACS `.d` in `experiments/exp5_lolib_dense/converted/` |

**Note:** The canonical grafo.etsii.urjc.es ZIP links return 404 (GitHub Pages; files
not committed to repo). Marti's Dropbox mirror is the working source as of 2026-06-06.

**Primary reference for LOLIB:**
Martí, R., Laguna, M., & Glover, F. (2008). Principles of scatter search.
*European Journal of Operational Research*, 169(2), 359–372.

Martí, R., Reinelt, G., & Duarte, A. (2011). A computational study of several
metaheuristics for the linear ordering problem. *Computational Optimization and
Applications*, 49(2), 245–264.

---

## External Baseline Algorithms

### DRMacIver/Feedback-Arc-Set

| Field | Value |
|-------|-------|
| Repository | https://github.com/DRMacIver/Feedback-Arc-Set |
| Commit used | 16ff24a92fde886e58819180a9fe686e60991c5c |
| Language | C (compiled to binary `feedbackarcset`) |
| Algorithm | Tournament FAS heuristic using local search |
| Input format | DIMACS arc list |
| Randomness | `srand(time|pid)` — non-deterministic; results vary slightly between runs |
| Used in | EXP4, EXP5 |
| Wrapper | `scripts/run_drmaciver_fas.py` |
| Clone path | `experiments/exp4_external_baselines/external_tools/Feedback-Arc-Set/` |

**Fairness note:** Results reported for DRMacIver use a single run per instance
(not multi-restart). The algorithm may produce slightly different results if rerun
due to randomized initialization. This matches standard practice for heuristic comparisons.

### python-igraph (`igraph_approx_eades`)

| Field | Value |
|-------|-------|
| Package | python-igraph |
| Version | 1.0.0 |
| Install | `pip install python-igraph` |
| Docs | https://python.igraph.org/en/stable/api/igraph.Graph.html#feedback_arc_set |
| Method used | `Graph.feedback_arc_set(weights=..., method="eades")` |
| Algorithm | Eades heuristic — score-based greedy ordering |
| Used in | EXP4, EXP5 |
| Wrapper | `scripts/run_igraph_eades.py` |

**Fairness note:** The igraph Eades method is deterministic for fixed graph input.
The `method="ip"` (ILP exact) was not used in heuristic comparisons.

### Weighted Eades (our implementation)

| Field | Value |
|-------|-------|
| Implementation | `src/mwfas/baselines.py::weighted_eades_ordering_from_dimacs` |
| Algorithm | Eades (1993) score heuristic adapted to weighted digraphs |
| Randomness | None — deterministic |
| Used in | EXP4, EXP5 |

**Reference:**
Eades, P., Lin, X., & Smyth, W. F. (1993). A fast and effective heuristic for the
feedback arc set problem. *Information Processing Letters*, 47(6), 319–323.

**Weighted adaptation caveat:** The original Eades (1993) method is defined for
unweighted digraphs. Our `weighted_eades_ordering_from_dimacs` implementation
(in `src/mwfas/baselines.py`) adapts the node-score formula to use net weighted
out-degree (Σw_out − Σw_in). This weighted adaptation is **not** from the original
paper and should be described as "a weighted adaptation of Eades (1993)" in the
manuscript, not attributed to the original authors.

### Borda Net Score

| Field | Value |
|-------|-------|
| Implementation | `src/mwfas/baselines.py::order_by_borda_net_score_from_dimacs` |
| Algorithm | Sort nodes by Σ(w_out − w_in) — net weighted out-degree |
| Randomness | None — deterministic |
| Used in | EXP4, EXP5 |

### Random Multistart

| Field | Value |
|-------|-------|
| Implementation | `src/mwfas/baselines.py::random_multistart_ordering_from_dimacs` |
| Algorithm | Random permutations (best of N restarts) |
| Restarts | 100 (EXP4, EXP5) |
| Seed | 42 (EXP5), 1 (EXP4) |
| Used in | EXP4, EXP5 |

---

## Our Algorithms

### LR-TA (Local-Ratio Topological Add-Back)

| Field | Value |
|-------|-------|
| Module | `src/mwfas/lrta.py::paper_fas_ranking_from_dimacs_fast` |
| Script | `scripts/run_lrta.py` |
| Novel contribution | Topological Add-Back phase (Phase 2) |
| Prior art component | Local-ratio framework (Bar-Yehuda et al.) |

**Reference (local-ratio prior art):**
Bar-Yehuda, R., Geiger, D., Naor, J., & Roth, R. M. (1998). Approximation algorithms
for the feedback vertex set problem with applications to constraint satisfaction and
Bayesian inference. *SIAM Journal on Computing*, 27(4), 942–959.

### WMSF (Weighted Minimum Spanning Forest)

| Field | Value |
|-------|-------|
| Module | `src/mwfas/wmsf.py::wmsf_ranking_from_dimacs_fast` |
| Script | `scripts/run_wmsf.py` |
| Note | Reimplementation of pipeline from predecessor paper (paper049) |

### IPSNS (Incumbent-Protected SCC Neighborhood Search)

| Field | Value |
|-------|-------|
| Module | `src/mwfas/ipsns.py::lns_merge_wmsf_lr_best_incumbent` |
| Script | `scripts/run_ipsns.py` |
| Key parameter | `--wmsf-seed-mode full` (required for incumbent protection) |
| Iterations | 200 (EXP5), 400 (EXP4), varies (EXP1b) |
| Seed | 1 (EXP4), 1 (EXP5 per-call, 42 for random baseline) |

**Incumbent protection guarantee:**
IPSNS is guaranteed to produce backward weight ≤ min(LR-TA BW, WMSF BW) on every instance.
This is enforced algorithmically: the incumbent is initialized to the better seed and
updates only if a strictly improving solution is found.

---

## Not Used / Explicitly Excluded

| Tool | Reason |
|------|--------|
| fas-smartAE | Requires `networkit` (not installed); unweighted only |
| R igraph `feedback_arc_set` | R not installed on this machine |
| LOP_MA-EDM | Accessible at https://github.com/carlossegurag/LOP_MA-EDM (checked 2026-06-06); **not built or run**; DRMacIver used instead as the strong external FAS baseline |
| GNNRank | Not started; optional comparison for future work |
| SNAP graphs | Excluded by design (unweighted, different problem setting) |
| PrefLib instances | Excluded by design |
| Cavallaro synthetic | Excluded by design |
| Gurobi-based solvers | Gurobi not installed |

---

## Scope Boundary Note (for Manuscript)

All algorithmic claims in this paper apply to **non-negative-weight directed graphs**.
The IPSNS incumbent protection guarantee does not hold for negative-weight instances
(the local-ratio decomposition is undefined). Negative-weight instances are clearly
flagged and excluded from all standard comparisons.

**LOLIB scope note:** LOLIB instances are dense complete tournaments, fundamentally
different from the sparse DIMACS benchmark (EXP1b–EXP4). EXP5 serves as a
transfer/generalization test. On LOLIB, DRMacIver (a tournament-native algorithm)
is competitive or stronger than IPSNS on larger instances. This is not a failure of
IPSNS — it reflects the different structure of the problem. The paper's primary claims
remain grounded in the sparse DIMACS benchmark where IPSNS dominates external baselines.

---

## Exact Manuscript Fairness Wording

Use the following exact wording in the manuscript when describing external baselines:

- **DRMacIver:** "We use the open-source DRMacIver/Feedback-Arc-Set heuristic
  (commit 16ff24a, https://github.com/DRMacIver/Feedback-Arc-Set), a tournament-native
  FAS algorithm. We invoke it via a single-run wrapper (`scripts/run_drmaciver_fas.py`);
  multi-restart results may differ."

- **igraph Eades:** "We use the Eades heuristic as implemented in python-igraph v1.0.0
  (`Graph.feedback_arc_set(weights=..., method='eades')`), a deterministic score-based
  greedy ordering method."

- **Weighted Eades:** "We implement a weighted adaptation of Eades et al. (1993),
  using net weighted out-degree as the node score. This adaptation is our own and is
  not from the original paper."

- **Borda:** "Borda net score orders nodes by Σw_out − Σw_in (net weighted out-degree).
  This is a standard ranking heuristic used as a simple baseline."

- **WMSF:** "WMSF is a reimplementation of the removeArcs/Minimize/Stabilize pipeline
  from our predecessor work. It is used as a seed and baseline, not as a novel
  contribution of this paper."

- **Negative-weight instances:** "Instances with negative-weight edges
  (k3_3, ku, peterson, peterson1, peterson2, gerez, howard-max, stg0) are excluded
  from all standard comparisons; the local-ratio decomposition is not defined for
  negative weights and the incumbent protection guarantee does not apply."
