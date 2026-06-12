# LR-TA Code Audit
**File:** `src/mwfas/lrta.py` (347 lines)  
**Date:** 2026-06-11

---

## 1. Algorithm Overview

LR-TA implements two phases:
- **Phase 1 (cycle reduction):** Iterative local-ratio cycle reductions until the active graph is a DAG.
- **Phase 2 (add-back):** Heavy-first arc restoration that preserves acyclicity.

## 2. Line-by-Line Verification Results

### Cycle Detection (`find_any_cycle_eids`, lines 54–122)

| Claim | Verdict |
|-------|---------|
| Returns a simple directed cycle | **CORRECT** — walks `parent[]` chain from back edge to cycle start `v`; stops when `cur == v`; guards against infinite loop via `cur == -1` break |
| Iterative DFS (no recursion limit) | **CORRECT** — explicit stack, not recursive |
| Resets only touched nodes | **CORRECT** — `visited_nodes` list cleared in `reset()` |
| Returns `None` if acyclic | **CORRECT** — returns `None` after exhausting all nodes |
| Handles disconnected graph | **CORRECT** — outer loop over all `s` where `state[s] == 0` |

**Note:** If `cur != v` at the end of chain tracing (due to malformed parent chain), `None` is returned — this is a defensive fallback. In practice `cur == v` always holds for valid DFS parent assignments.

### Weight Reduction (Phase 1, lines 238–259)

| Claim | Verdict |
|-------|---------|
| Subtracts minimum cycle weight from all cycle arcs | **CORRECT** — `eps = min(W[eid] for eid in cyc)` |
| Removes arcs at `w <= tol` | **CORRECT** — `if new_w <= tol and active[eid]: active[eid] = 0` |
| Handles `eps <= tol` case (near-zero cycle) | **CORRECT** — deactivates `cyc[0]` directly, preventing infinite loop |
| All zeroed edges removed | **CORRECT** — deactivated once `w <= tol` |
| Nonnegative weight assumption | Not enforced with assertion but behavior is correct for nonneg inputs; negative weights can cause non-termination (documented exclusion) |
| Phase 1 terminates in ≤ m iterations | **CORRECT** — each iteration deactivates ≥1 arc; finite active arcs |

### Add-Back Phase (lines 264–282)

| Claim | Verdict |
|-------|---------|
| Add-back order uses original weights W0 (not reduced W) | **CORRECT** — `sorted(removed_eids, key=lambda eid: (-W0[eid], U[eid], V[eid]))` |
| Tie-breaking deterministic | **CORRECT** — secondary keys `U[eid], V[eid]` ensure deterministic sort |
| Rank-forward fast path correct | **CORRECT** — `if rank[u] < rank[v]: restore` — forward arc cannot create a cycle |
| Reachability fallback correct | **CORRECT** — `not reachable(v, u, rank=rank, rank_limit=rank[u])` tests whether v can reach u; if not, arc is safe |
| Topological order refreshed after backward add-back | **CORRECT** — `_, rank = topo_order_active(...)` called after each backward restoration |
| Forward arcs do NOT refresh topo order | **CORRECT** — safe omission; forward arcs cannot invalidate rank ordering |

### Topological Sort (`topo_order_active`, lines 129–165)

| Claim | Verdict |
|-------|---------|
| Kahn's algorithm, correct | **CORRECT** — indegree computation, min-heap for determinism, count check |
| Deterministic via min-heap | **CORRECT** — `heapq` ensures consistent ordering for equal-indegree nodes |
| Raises RuntimeError if not acyclic | **CORRECT** — `if len(order) != n_nodes: raise RuntimeError(...)` |

### Reachability Checker (`make_reachability_checker`, lines 172–209)

| Claim | Verdict |
|-------|---------|
| Stamp-based visited (no reset cost) | **CORRECT** — `stamp` incremented each call |
| Pruned by `rank_limit` | **CORRECT** — `if rank[y] > rank_limit: continue` |
| `src == target` returns True | **CORRECT** |
| Rank pruning correctness | **CORRECT** — only need to check nodes with rank ≤ rank[u]; any path v→u cannot go through a node ranked > u in the current topological order |

## 3. Specific Manuscript Claims vs. Code

| Manuscript Claim | Code Evidence | Verdict |
|-----------------|---------------|---------|
| "at least one arc on the cycle reaches weight ≤ τ" | `eps = min(W[eid])` ensures at least one arc hits 0 after subtraction | CORRECT |
| "Phase I performs at most m iterations" | Each iteration deactivates ≥1 arc; finite m | CORRECT |
| "topological add-back reactivates an arc only after certifying acyclicity" | rank-forward path or reachability test required | CORRECT |
| "add-back uses original weights" | `W0[eid]` used in sort key | CORRECT |
| "deterministic output for fixed input" | No randomness; min-heap topo sort; sorted order | CORRECT |

## 4. Edge Cases

| Case | Handled? |
|------|---------|
| Empty graph (n=0 or m=0) | `find_any_cycle_eids` returns `None`; `topo_order_active` produces empty order — correct |
| Self-loops | Detected as 1-cycle (a→a); min-weight = w(a→a); deactivated in Phase 1 — correct |
| Parallel arcs | Aggregated by `read_graph_dimacs_agg`; treated as one edge — correct |
| Zero-weight edges | `if w > tol: active[eid] = 1` — zero-weight edges start inactive; excluded from cycles — correct |
| Disconnected graph | DFS outer loop handles all components — correct |
| DAG input | Phase 1 immediately returns; Phase 2 runs add-back on empty removed set (no-op) — correct |

## 5. Complexity (per manuscript §4.4)

| Phase | Worst-case | Notes |
|-------|-----------|-------|
| Phase 1 | O(m × (n + m)) | m iterations × O(n + m) DFS each |
| Phase 2 | O(m × (n + m)) | m add-back candidates × O(n + m) reachability/topo each |
| Total | O(m(n + m)) | Consistent with manuscript claims |

## 6. Overall Verdict

**LR-TA is correctly implemented.** No bugs found. Formal propositions in §4 (Prop. 1, 2) accurately reflect the code. The implementation is deterministic, self-contained, and handles all documented edge cases correctly.
