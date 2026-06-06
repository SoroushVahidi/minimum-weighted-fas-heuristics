# EXP4 Baseline Registry

Last updated: 2026-06-06

This registry describes every baseline considered for EXP4 external comparison.  
"In-repo" = implemented in this repository. "External official" = official external tool.
"External wrapper" = external tool called via a wrapper we wrote.

---

## Registry Table

| Baseline | Source/Reference | URL | Impl. Type | Weighted Directed | Output | Status | Notes |
|----------|-----------------|-----|-----------|------------------|--------|--------|-------|
| `lrta_full` | This work | — | in-repo | Yes | Ordering | Runnable (reference) | Main LR-TA method; Phase 1 + Phase 2 add-back. Not a baseline — reference only. |
| `wmsf_seed` | This work | — | in-repo | Yes | Ordering | Runnable (reference) | Per-SCC WMSF pipeline. Not a baseline — internal seed for IPSNS. |
| `ipsns_full` | This work | — | in-repo | Yes | Ordering | Runnable (reference) | Our final method; SCC-neighborhood LNS. Not a baseline — main method. |
| `borda_net_score` | Classic voting / Copeland | — | in-repo | Yes | Ordering | **Runnable** | Sort by weighted out-degree minus in-degree. Simplest sensible heuristic. Our implementation. |
| `weighted_eades` | Eades–Lin–Smyth (1993) | — | in-repo | Yes | Ordering | **Runnable** | Weighted adaptation of Eades-Lin-Smyth greedy source/sink/net-score heuristic. Our implementation; not official author code. Non-negative weights assumed. |
| `random_multistart` | — | — | in-repo | Yes | Ordering | **Runnable** | Best of 100 random permutations (deterministic seed). Random lower-bound reference. |
| `igraph_approx_eades` | igraph library | https://github.com/igraph/python-igraph | external wrapper | Yes | FAS → ordering | **Runnable** | python-igraph v1.0.0; `feedback_arc_set(weights=..., method="eades")`. Eades heuristic on weighted digraph. |
| `drmaciver_fas` | DRMacIver (2013) | https://github.com/DRMacIver/Feedback-Arc-Set | external wrapper | Yes | Ordering + score | **Runnable** | C binary (commit 16ff24a); reads weighted matrix; locally optimal. Maximizes forward weight = minimizes FAS weight. |
| `fas_smartAE` | Pustoš et al. | https://github.com/jurepustos/fas-smartAE/ | external official | **No (unweighted)** | FAS | **Unavailable** | Requires `networkit` (not installed). Unweighted algorithm — not suitable for weighted EXP4. |
| `R_igraph_eades` | igraph R package | https://r.igraph.org/ | external official | Yes | FAS | **Unavailable** | R not installed on machine. |

---

## Detailed Notes

### `borda_net_score`
- **Algorithm:** For each vertex v, compute `score(v) = sum_u w(v→u) - sum_u w(u→v)`.
  Sort all vertices descending by score; ties broken by node ID (ascending).
- **Runtime:** O(m + n log n)
- **Fairness:** Clean, deterministic, widely known heuristic. Not tuned to our instances.
- **Manuscript description:** "Borda net score: vertices ranked by weighted out-degree minus
  in-degree."

### `weighted_eades`
- **Algorithm:** Weighted Eades–Lin–Smyth greedy:
  1. Repeatedly move zero-in-weight vertices ("sources") to the left.
  2. Repeatedly move zero-out-weight vertices ("sinks") to the right.
  3. If no source/sink exists, pick vertex with maximum (weighted outdeg – weighted indeg)
     and move to the left. Ties broken by node ID.
- **Runtime:** O(n² + m) per iteration, O(n(n² + m)) worst case.
- **Restriction:** Non-negative edge weights required. Returns error on negative weights.
- **Reference:** Based on: P. Eades, X. Lin, W. F. Smyth, "A fast and effective heuristic
  for the feedback arc set problem," Info. Proc. Letters 47(6), 1993.
- **Fairness:** This is our weighted adaptation, not official author code.
- **Manuscript description:** "Weighted Eades: greedy source/sink/net-score ordering
  (weighted adaptation of Eades–Lin–Smyth 1993; our implementation)."

### `random_multistart`
- **Algorithm:** Generate `trials=100` uniformly random permutations using a fixed seed.
  Keep the permutation with minimum total backward weight.
- **Runtime:** O(trials × (n + m))
- **Purpose:** Lower bound on improvement; calibrates how much structure helps vs. random.
- **Manuscript description:** "Random multistart: best of 100 random permutations (seed=1)."

### `igraph_approx_eades`
- **Algorithm:** `igraph.feedback_arc_set(weights=..., method="eades")` returns FAS edge IDs.
  Remaining edges form a DAG; topological_sorting gives the ordering.
- **Version:** python-igraph 1.0.0
- **Commit/tag:** v1.0.0
- **Manuscript description:** "igraph approx_eades (python-igraph v1.0.0, Eades heuristic
  via official igraph library)."
- **Note:** igraph's internal Eades may differ from our `weighted_eades` implementation
  in tie-breaking and initialization.

### `drmaciver_fas`
- **Algorithm:** Proprietary heuristic (C) that finds a locally optimal ordering.
  Reads W[i][j] = weight of evidence that i < j. Locally optimal = no single-element
  move improves the score.
- **Commit:** 16ff24a92fde886e58819180a9fe686e60991c5c
- **Manuscript description:** "DRMacIver FAS (https://github.com/DRMacIver/Feedback-Arc-Set,
  commit 16ff24a; C heuristic; locally optimal)."
- **Note:** The tool's internal randomization (`srand(time|pid)`) means repeated runs
  may give slightly different results. EXP4 uses one run per instance.

### `fas_smartAE` (unavailable)
- **Reason:** `networkit` not installed (`pip install networkit` needed).
  Also, the algorithm appears unweighted — it minimizes arc count, not arc weight.
  Would require porting to weighted setting.
- **Future:** If `networkit` is installed and weighted mode added, could compare on
  unweighted projections (all weights = 1).

---

## Reference Methods (Not Baselines)

| Method | Description |
|--------|-------------|
| `lrta_full` | Local-ratio cycle reduction + add-back. Phase 1 + Phase 2. EXP1b main result. |
| `wmsf_seed` | Per-SCC WMSF pipeline used to seed IPSNS. |
| `ipsns_full` | SCC-neighborhood LNS with WMSF+LR-TA seed. 400 iterations, seed=1. |
