# External Baseline Comparison Plan — EXP4

**Date:** 2026-06-06  
**Repository:** SoroushVahidi/minimum-weighted-fas-heuristics (private)

---

## Overview

EXP4 adds fair external baseline comparisons on the full 123-instance benchmark set.
All baselines run on the same weighted directed graph instances used in EXP1b (main benchmark).

---

## External Baselines Attempted

### 1. python-igraph — `igraph_approx_eades`

| Field | Value |
|-------|-------|
| URL | https://github.com/igraph/python-igraph |
| Version | 1.0.0 (python-igraph) |
| Access status | **Available** |
| Build/install | `pip install python-igraph` (already installed) |
| Weighted directed support | Yes |
| Method used | `Graph.feedback_arc_set(weights=..., method="eades")` |
| Wrapper | `scripts/run_igraph_eades.py` |
| Run in EXP4 | **Yes** |

**How the wrapper works:** Builds an igraph directed graph, calls `feedback_arc_set(method="eades")`,
removes the FAS edges, calls `topological_sorting()` on the remaining DAG to get a vertex ordering,
then computes backward weight via `compute_forward_backward`.

**Fairness notes:**
- igraph's internal Eades implementation may differ from our `weighted_eades` in tie-breaking.
- We use the official igraph library unchanged; no algorithmic modifications.
- The `method="ip"` (exact ILP) is available but not used here — EXP4 is heuristic comparison only.

**Manuscript description:**
> "igraph approx_eades: python-igraph v1.0.0 (igraph library, https://github.com/igraph/python-igraph),
> `feedback_arc_set(weights=..., method='eades')`. Official library call, unmodified."

---

### 2. DRMacIver Feedback-Arc-Set — `drmaciver_fas`

| Field | Value |
|-------|-------|
| URL | https://github.com/DRMacIver/Feedback-Arc-Set |
| Commit | 16ff24a92fde886e58819180a9fe686e60991c5c |
| Access status | **Available (built successfully)** |
| Build command | `make fas` (C compiler required) |
| Binary location | `experiments/exp4_external_baselines/external_tools/Feedback-Arc-Set/fas` |
| Weighted directed support | Yes (input W[i][j] = weight of arc i→j) |
| Wrapper | `scripts/run_drmaciver_fas.py` |
| Run in EXP4 | **Yes** |

**How the wrapper works:** Converts DIMACS `.d` format to DRMacIver input format
(`n\ni j w\n...`), calls the `fas` binary via subprocess, parses the
`Optimal ordering: ...` line (handling brackets and `||` condorcet separators).

**Algorithm properties (from README):**
- Locally optimal: no single-element move improves the score.
- O(n²) in number of items.
- Deterministic for each invocation (but uses `srand(time|pid)` — results may vary
  slightly between runs on some instances; EXP4 records one run per instance).

**Fairness notes:**
- Official external C implementation; no algorithmic modifications.
- Not cloned into the main repo — binary built from cloned source in `external_tools/`.
- Negative weights: DRMacIver README states x ≥ 0 required. Negative-weight instances
  will be excluded from comparison analysis.

**Manuscript description:**
> "DRMacIver FAS: C heuristic (https://github.com/DRMacIver/Feedback-Arc-Set, commit 16ff24a);
> locally optimal (no single-element move improvement); official implementation, unmodified."

---

### 3. fas-smartAE — NOT USED IN EXP4

| Field | Value |
|-------|-------|
| URL | https://github.com/jurepustos/fas-smartAE/ |
| Commit | e6b998f321a5040c3615a2410ca786fe01ad7af3 |
| License | MIT |
| Access status | Cloned successfully |
| Reason not used | (1) `networkit` Python package not installed; (2) algorithm appears unweighted |

**Why excluded from weighted EXP4:**
The `fas-smartAE` implementation imports `networkit` (not installed) and uses `FASGraph`
with no visible weight parameter in the primary API. Running it on unweighted projections
of our weighted instances would produce meaningless comparisons for the MWFAS paper.

**Future use:** If `networkit` is installed (`pip install networkit`) and a weighted mode
is added to `fas-smartAE`, it could serve as an unweighted-projection baseline. This is
documented as a TODO in `baseline_registry.md`.

**Manuscript note:** "fas-smartAE was identified but not used due to absent weighted support
and missing networkit dependency."

---

### 4. R igraph — NOT USED IN EXP4

| Field | Value |
|-------|-------|
| URL | https://r.igraph.org/ |
| Access status | R not installed on benchmark machine |
| Reason not used | `which R` returns empty; R package cannot be loaded |

**Manuscript note:** "R igraph was not available on the benchmark machine."

---

## In-Repository Baselines (New for EXP4)

### 5. `borda_net_score`

Sort vertices by weighted out-degree minus weighted in-degree (descending).
Tie-break: ascending node index. O(m + n log n).

**Fairness:** Purely deterministic; no tuning to our instances; widely known heuristic.

**Manuscript description:** "Borda net score: vertices ranked by weighted out-degree
minus weighted in-degree (descending). Deterministic. O(m + n log n)."

### 6. `weighted_eades`

Weighted adaptation of Eades–Lin–Smyth (1993) greedy source/sink/net-score ordering.
Non-negative weights assumed; returns error on negative weights.

**Reference:** P. Eades, X. Lin, W. F. Smyth, "A fast and effective heuristic for the
feedback arc set problem," Info. Proc. Letters 47(6), 1993.

**Fairness:** This is our in-repository weighted adaptation, NOT official author code.
The manuscript must clearly state: "weighted Eades (our adaptation of Eades–Lin–Smyth 1993)."

### 7. `random_multistart`

Best of 100 uniformly random permutations, deterministic (seed=1).

**Purpose:** Random lower bound — calibrates how much structure helps vs. random.

---

## What Was Actually Run

All 8 algorithms (lrta_full, wmsf_seed, ipsns_full, borda_net_score, weighted_eades,
random_multistart, igraph_approx_eades, drmaciver_fas) were run on all 123 instances
from the EXP1b benchmark set.

- IPSNS: 400 iterations, wmsf_seed_mode="full", rng_seed=1.
- Random: 100 trials, seed=1.
- igraph: python-igraph v1.0.0, method="eades".
- DRMacIver: fas binary from commit 16ff24a.

---

## What Could Not Be Run

| Baseline | Reason |
|----------|--------|
| fas_smartAE | `networkit` not installed; algorithm unweighted |
| R igraph | R not installed |

---

## What NOT to Claim in the Manuscript

1. Do NOT claim `weighted_eades` is "the Eades 1993 algorithm" — it is our adaptation.
   Say: "weighted adaptation of Eades–Lin–Smyth (1993), our implementation."
2. Do NOT claim DRMacIver is "optimal" — it is locally optimal only.
3. Do NOT claim igraph's eades and our weighted_eades are the same algorithm.
4. Do NOT include negative-weight instances (k3_3, ku, peterson*) in MWFAS comparisons.
5. Do NOT cite DRMacIver as a peer-reviewed paper — it is an open-source C tool.

---

## Files Created

| File | Description |
|------|-------------|
| `src/mwfas/baselines.py` | borda_net_score, weighted_eades, random_multistart |
| `scripts/run_borda.py` | CLI for borda |
| `scripts/run_weighted_eades.py` | CLI for weighted_eades |
| `scripts/run_random_baseline.py` | CLI for random_multistart |
| `scripts/run_igraph_eades.py` | igraph approx_eades wrapper |
| `scripts/run_drmaciver_fas.py` | DRMacIver FAS wrapper |
| `experiments/exp4_external_baselines/baseline_registry.md` | Full baseline registry |
| `experiments/exp4_external_baselines/summary/external_access_report.md` | Access report |
| `experiments/exp4_external_baselines/configs/exp4_instances.txt` | 123-instance list |
| `experiments/exp4_external_baselines/configs/exp4_smoke_instances.txt` | 4-instance smoke list |
| `experiments/exp4_external_baselines/run_exp4_benchmark.py` | Python runner |
| `experiments/exp4_external_baselines/run_exp4_smoke.sh` | Smoke test launcher |
| `experiments/exp4_external_baselines/run_exp4_external_baselines_tmux.sh` | Full benchmark launcher |
| `experiments/exp4_external_baselines/postprocess_exp4_external.py` | Postprocessor |
