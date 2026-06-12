# Demetrescu–Finocchi vs. LR-TA Operational Comparison

**Audit date:** 2026-06-11  
**Authoritative sources:** `src/mwfas/lrta.py` (code), `src/mwfas/ipsns.py` (code), JOCO predecessor ZIP `main.tex`, COAP `sections/04_formal_analysis.tex`, Demetrescu & Finocchi, IPL 86(3):129–136, 2003.

---

## 1. Scope of this comparison

This document compares DF03's published local-ratio algorithm for weighted FAS against the
LR-TA implementation in the current canonical code. It addresses four specific mandated items:
add-back ordering, cycle detection mechanism, complexity, and approximation guarantee
inheritance.

---

## 2. Algorithm mechanisms side-by-side

| Property | DF03 (theoretical) | LR-TA (canonical code) | Evidence |
|---|---|---|---|
| **Cycle selection** | A directed cycle; DF03 paper does not restrict to simple cycles but the standard formulation assumes a simple cycle for the local-ratio decomposition | Any directed cycle found by first-encounter iterative DFS; no simplicity guarantee | `lrta.py` `find_any_cycle_eids`, lines 54–122 |
| **Weight reduction step** | Subtract `ε = min{w(e) : e ∈ C}` from all edges on cycle | Same: subtract `eps = min(W[eid] for eid in cyc)` using current reduced weights `W[]` | `lrta.py` lines 243–258 |
| **Zero-edge removal** | Described as simultaneous removal of all newly zero-weight edges | Serial: when `eps ≤ tol`, deactivates only the first cycle edge (`cyc[0]`); when `eps > tol`, deactivates all edges reaching `≤ tol` in the same iteration | `lrta.py` lines 245–259; the `eps ≤ tol` branch explicitly selects `cyc[0]` only |
| **Add-back goal** | Produces an inclusion-minimal FAS (any edge that can be reinserted without creating a cycle is reinserted) | Heavy-first: sorts by original weight `(-W0[eid], U[eid], V[eid])`; does NOT guarantee inclusion minimality — a light-weight edge blocked by a prior reactivation is left in the FAS | `lrta.py` line 265 |
| **Add-back acceptance: forward** | Accept if reinsertion cannot create a cycle | Accept immediately if `rank[u] < rank[v]` (sufficient condition; not a necessary-and-sufficient iff) | `lrta.py` line 273 |
| **Add-back acceptance: backward** | Reachability test | Reachability test from `v` to `u`, pruned to nodes with `rank ≤ rank[u]` | `lrta.py` lines 278–282 |
| **Topo order maintenance** | Not the focus of DF03 | Full Kahn topo-sort recomputed after each accepted backward candidate; NOT updated after forward acceptance | `lrta.py` lines 279–281 (`topo_order_active` called only after `not reachable`) |
| **Add-back ordering weight** | DF03 does not specify an ordering; inclusion-minimality does not depend on ordering | **Original weights `W0[eid]`** (not reduced/residual weights `W[eid]`) | `lrta.py` line 265: `key=lambda eid: (-W0[eid], U[eid], V[eid])` |
| **Weights used for reduction** | Mutable (reduced) weights | Mutable `W[]` in Phase I; original `W0[]` only in Phase II add-back sort | `lrta.py` lines 244, 265 |
| **Dynamic transitive closure** | DF03 cites incremental reachability data structure as a theoretical tool | Not used; plain DFS reachability on the current active graph | No dynamic TC structure in `lrta.py` |
| **Data structure** | Not specified (theoretical paper) | Edge-ID active-flag arrays; `bytearray` activity flags; Kahn heap-based topo sort | `lrta.py` lines 19–47 |
| **Approximation guarantee** | Proved under specific conditions (see §5) | Not established for current implementation | See §5 below |

---

## 3. Topological-rank shortcut — exact mechanism

**What the code actually does (Phase II add-back):**

```
for each removed edge (u, v) in heavy-first order:
    if rank[u] < rank[v]:          # SUFFICIENT condition for acyclicity
        activate(u,v)              # O(1) accept, no reachability needed
        remove from FAS
    else:
        if not reachable(v, u, rank_limit=rank[u]):   # full reachability test
            activate(u,v)
            remove from FAS
            rank = recompute_full_topo_sort()          # O(n+m) recompute
        # else: leave in FAS
```

**What this is not:**

- It is **not** the case that `rank[u] < rank[v]` is a necessary condition (the current topo order can have `rank[u] > rank[v]` for an edge that could still be reinstated without a cycle).
- It is **not** "adding (u→v) preserves acyclicity iff rank(u) < rank(v)." That claim is false.
- The forward-rank test is a **sufficient** fast path only; the reachability test handles the remainder.

**Why rank recomputation is needed after backward acceptance:**

After reinstating a backward edge (one where `rank[u] ≥ rank[v]`), the existing topological order becomes stale: subsequent rank comparisons and reachability bounds depend on a valid topological order of the updated DAG. The code calls `topo_order_active` to produce a fresh order before processing the next candidate.

---

## 4. Cycle detection and complexity

### 4.1 DF03's theoretical implementation
DF03 analyzes the local-ratio framework theoretically. The paper cited the possibility of using
dynamic transitive-closure data structures (e.g., those achieving O(mn) total update time over
all insertions and deletions) to implement incremental reachability efficiently.

### 4.2 LR-TA's actual implementation

**Phase I — cycle detection:**
- Uses iterative DFS (`find_any_cycle_eids`, `lrta.py` lines 54–122)
- Each DFS runs in O(n + m_active) where m_active ≤ m is the number of currently active edges
- DFS is reset only over visited nodes (stamp pattern)
- At most m iterations of Phase I (each removes ≥ 1 edge)
- **Conservative Phase I bound: O(m(n + m))**

**Phase II — add-back:**
- Sort: O(r log r) where r = |removed|
- Per-candidate cost:
  - Forward accept: O(1)
  - Backward reachability: O(n + m) worst case (pruned by rank interval)
  - Backward accept → topo recompute: O(n + m)
- **Conservative Phase II bound: O(r log r + r(n + m))**

**Overall LR-TA bound:** O(m(n + m) + r(n + m)) = **O(m(n + m))**

This matches the COAP formal analysis section exactly. It is a **conservative upper bound**, not a tight bound. In practice, Phase I shrinks the active graph rapidly, and the DFS restarts benefit from reset-only-touched-nodes optimization.

### 4.3 Why DF03's O(mn) bound does not transfer automatically

DF03's O(mn) is derived using a dynamic reachability structure with amortized O(n) update cost per edge deletion. LR-TA uses plain DFS, whose per-iteration cost can be O(n + m) even after many deletions, since the DFS re-traverses from scratch (though only over active edges). The same O(m(n+m)) bound results from different analysis. In the worst case (e.g., one edge removed per iteration), LR-TA's Phase I is O(m(n+m)), matching DF03's O(mn) only when m = O(n).

---

## 5. Approximation guarantee — status assessment

### 5.1 What DF03 proves

DF03 proves that their local-ratio procedure on directed FAS produces a FAS with
weight at most twice the optimal (a 2-approximation) under the following conditions (paraphrased):
1. The reduced graph is solved optimally for the remaining zero-weight edges.
2. The add-back step produces an **inclusion-minimal** FAS.
3. The local-ratio decomposition is valid across the full weight space.
4. Non-negative weights.

### 5.2 Proof-critical deviations in LR-TA

| Requirement | LR-TA implementation | Gap |
|---|---|---|
| Inclusion-minimal add-back | Heavy-first add-back does NOT guarantee inclusion minimality (a light edge later in order may be unnecessarily kept) | **YES — gap** |
| Simultaneous removal of all zero-weight edges | When `eps ≤ tol`, only `cyc[0]` is removed (serial, not simultaneous) | **YES — potential gap** |
| Simple cycle selection | `find_any_cycle_eids` may find a non-simple cycle (the DFS back-edge traversal traces parent pointers, but the cycle found is the back-edge cycle which is simple in terms of DFS; however, the DFS does not guarantee minimum weight or any specific structural property) | **Partial — unclear** |
| Non-negative weights | Code supports nonneg weights; negative weights not excluded by code but results undefined | Nonneg: **OK**; negative: **undefined** |
| Use of original vs. reduced weights in add-back | Add-back uses W0 (original) for ordering; DF03's proof does not specify ordering | **Not a formal gap, but diverges from DF03** |
| Zero-weight edge handling | Edges with W0 ≤ tol are never activated (filtered at build_eid_graph); zero-weight arcs excluded | Does not affect approximation reasoning; **OK for nonneg** |

### 5.3 Classification

**Category 3: Not currently established for the implementation.**

The heavy-first add-back does not guarantee inclusion-minimality, which is a key requirement for
the DF03 approximation argument. Additionally, the serial zero-edge removal (one arc when
eps ≤ tol) may diverge from the simultaneous removal assumed in the theoretical proof.

**What the COAP manuscript correctly claims:** The introduction explicitly disclaims a new
approximation theorem. The related-work section says: "The local-ratio step in the present work
is inherited in spirit from that line of research." Formal analysis Proposition 1 does not
claim an approximation ratio. This is the correct, defensible position.

**What must NOT be claimed:** That LR-TA inherits DF03's 2-approximation guarantee.

**What would be required for inheritance:** A separate argument showing that:
(a) heavy-first add-back produces inclusion-minimal FAS (false in general), or
(b) the proof survives non-inclusion-minimal add-back with a different ratio, or
(c) a new approximation theorem for the Phase-I-only output (without add-back).

---

## 6. WMSF and IPSNS approximation status

**WMSF:** Reimplementation of CC25. CC25 does not claim an approximation ratio; it is a heuristic.
The WMSF add-back (`wmsf_minimizeFas_scc`) uses the same heavy-first, original-weight ordering as
LR-TA Phase II. No approximation guarantee.

**IPSNS:** Pure heuristic with a monotonicity invariant (Prop. 3 of COAP formal analysis). The
monotonicity guarantee ensures the output is no worse than the best seed. This is not an
approximation guarantee relative to the optimum.

---

## 7. Summary of corrections

| Prior claim / assumption | Correction |
|---|---|
| "rank(u) < rank(v) iff adding (u→v) preserves acyclicity" | False. rank(u) < rank(v) is SUFFICIENT, not necessary-and-sufficient. |
| "LR-TA uses residual-weight ordering for add-back" | False. Add-back sorts by original weight W0, not reduced weight W. |
| "DF03 O(mn) complexity transfers to LR-TA" | Not automatic; LR-TA uses plain DFS, yielding O(m(n+m)) by separate analysis. |
| "LR-TA inherits DF03's approximation guarantee" | Not established; heavy-first add-back does not guarantee inclusion minimality required by the DF03 proof. |
| "IPSNS or WMSF inherit any approximation guarantee" | False. Both are heuristics. IPSNS has only a monotonicity invariant vs. its own seeds. |
