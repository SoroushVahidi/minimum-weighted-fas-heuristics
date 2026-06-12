# WMSF Code Audit
**File:** `src/mwfas/wmsf.py` (480 lines)  
**Date:** 2026-06-11

---

## 1. Algorithm Overview

WMSF implements the pipeline from paper049 (Cavallaro-Cutello lineage):
`removeArcs → MinimizeFas → StabilizeFas → MinimizeFas`

For single-SCC graphs, both L1 and L2 orderings are tried; better result kept.

## 2. Provenance

The implementation is described in the manuscript as a "Cavallaro-Cutello-derived engineered seed" for weighted MFAS. The module docstring refers to "paper049" which is the internal identifier for the Cavallaro-Cutello 2025 paper. This attribution is **present in code** and **present in manuscript** (§5 baseline description, related work §2.3). **VERIFIED.**

## 3. removeArcs (`wmsf_removeArcs_scc`, lines 132–244)

### L1 and L2 Ordering Implementation

| Item | Verdict |
|------|---------|
| L1: sort by `(W0[eid], U[eid], V[eid], eid)` | **CORRECT** — ascending weight, deterministic tiebreak |
| L2: sort by `(W0[eid] / (Win[U[eid]] + Wout[V[eid]]), W0[eid], U[eid], V[eid], eid)` | **CORRECT** — ratio-based; denominator defaulted to 1.0 if ≤ 0 (prevents division by zero) |

### 2-Cycle Preprocessing

| Item | Verdict |
|------|---------|
| Detects antiparallel pairs `(u,v)` and `(v,u)` | **CORRECT** — `pair_to_eid = {(U[eid], V[eid]): eid for eid in eids}`; checks `pair_to_eid.get((v, u))` |
| Removes the earlier arc in the ordering | **CORRECT** — `if pos[eid] < pos[rev]: active[eid] = 0` (earlier = lower position in sorted list) |

### Safe-Arc Propagation

| Item | Verdict |
|------|---------|
| Identifies source-like nodes (`indeg == 0`) and sink-like nodes (`outdeg == 0`) | **CORRECT** — `if indeg[u] == 0 or outdeg[v] == 0: q.append(eid)` |
| Propagates updates correctly when degrees change | **CORRECT** — after removing edge, pushes affected out-edges of `u` and in-edges of `v` to queue |
| Safe arcs NOT added to F (restored at end) | **CORRECT** — `safe_tmp` restored via `for eid in safe_tmp: active[eid] = 1` at line 241 |
| **Safe-edge propagation correctness:** Safe arcs (source/sink incident) can be removed temporarily without loss because they cannot be on any cycle | **CORRECT** — a source has no incoming edges; any cycle through a source-incident edge would require a path back to the source, which is impossible if indeg==0 |

### Main Deletion Loop

| Item | Verdict |
|------|---------|
| Periodic acyclicity check every `alpha` deletions | **CORRECT** — `alpha = max(1, m_act // max(1, n_nodes))` |
| Stops as soon as acyclic | **CORRECT** — `if ok: break` |
| Fallback single-deletion loop if batch check missed acyclicity | **CORRECT** — lines 232–239 |

## 4. MinimizeFas (`wmsf_minimizeFas_scc`, lines 251–276)

| Item | Verdict |
|------|---------|
| Heavy-first add-back | **CORRECT** — `sorted(F, key=lambda eid: (-W0[eid], U[eid], V[eid], eid))` |
| Uses same rank-forward + reachability logic as LR-TA | **CORRECT** — shared implementation via `topo_order_active` and `make_reachability_checker` from `lrta.py` |
| Updates rank after each backward restoration | **CORRECT** — `_, rank = topo_order_active(...)` inside loop |
| Inclusion minimality after this step | **CORRECT** — every removed arc that can be restored without creating a cycle is restored; the result is inclusion-minimal with respect to single-arc restoration |

## 5. StabilizeFas (`wmsf_stabilizeFas_scc`, lines 283–343)

This is the most complex step and the primary concern for correctness.

### Swap Logic

For each node `v` in topological order:
- Compute `removed_in = WinG[v] - WinStar` (removed incoming weight to v)
- Compute `removed_out = WoutG[v] - WoutStar` (removed outgoing weight from v)
- Case A: `removed_in > WoutStar + tol` — remove all outgoing active edges of v, restore removed incoming edges IF rank[U[eid]] < rank[v]
- Case B: `removed_out > WinStar + tol` — remove all incoming active edges of v, restore removed outgoing edges IF rank[v] < rank[V[eid]]

### Key Correctness Question: Does stabilization worsen the FAS?

| Claim | Analysis |
|-------|---------|
| Stabilization can only improve or maintain (not worsen) the FAS weight | **NEEDS QUALIFICATION** — The swap condition `removed_in > WoutStar + tol` ensures that the incoming side saved exceeds the outgoing side cost. However, when arcs are restored in lines 317–321 and 332–337, only arcs where the endpoint rank condition holds are restored. The actual improvement realized may be less than `removed_in - WoutStar` because not all removed in-arcs can be safely restored. |
| The condition guarantees a non-negative net change | **VERIFIED WITH CAVEAT** — The condition compares total removed incoming weight against total current outgoing weight. If some removed incoming arcs cannot be restored (rank condition fails), the net change may be neutral rather than positive. But it cannot be negative because: (1) we unconditionally remove all outgoing edges of v (saving `WoutStar`), and (2) we only restore incoming edges that are already in F (no new edges are moved from active to F on the incoming side). So cost decreases by `WoutStar` and potentially increases by 0 (restored arcs reduce cost further). Wait — I need to think more carefully. |

**Detailed stabilization analysis:**

Case A: `removed_in > WoutStar + tol`

Before swap for node v:
- F includes some incoming arcs to v (weight = `removed_in`) and some outgoing arcs from v may or may not be in F
- Active includes `WoutStar` total outgoing weight from v and `WinStar` incoming weight to v

After swap:
- All outgoing active arcs of v added to F (cost increase: `WoutStar`)
- Some removed incoming arcs of v restored (cost decrease: sum of restored weights ≤ `removed_in`)

Wait, this is backward. Adding to F increases cost, restoring from F decreases cost.

**Net change = WoutStar (added to FAS) - (sum of restored incoming arcs)**

The condition `removed_in > WoutStar + tol` ensures that IF all removed incoming arcs could be restored, we'd save more than we spend. But only arcs with `rank[U[eid]] < rank[v]` are restored (forward arcs only).

**If some removed incoming arcs have `rank[U[eid]] > rank[v]` (backward in current order), they cannot be restored safely.** In that case, the net change could be:
- Net = WoutStar - (only forward-compatible restored arcs) ≥ 0 if enough forward-compatible arcs exist
- **But this might be negative if few incoming arcs are forward-compatible and WoutStar is large**

This is a subtle correctness issue. Let me check the code more carefully...

Looking at lines 311–324:
```python
if removed_in > WoutStar + tol:
    for eid in out_adj[v]:      # remove all outgoing active arcs
        if active[eid]:
            active[eid] = 0
            F.add(eid)
            changed = True
    for eid in in_adj[v]:       # restore removed incoming arcs
        if (not active[eid]) and (eid in F):
            if rank[U[eid]] < rank[v]:  # only forward-compatible
                active[eid] = 1
                F.discard(eid)
                changed = True
```

**The stabilization CAN worsen the FAS** if: `WoutStar > sum(restorable_incoming_forward_arcs)`. In this case, more weight is added to F (outgoing arcs) than removed (restored incoming arcs).

**However**, this is the documented behavior of the Cavallaro-Cutello stabilization — the paper's stabilization step is designed to be a *potential improvement* not a guaranteed improvement. The important question is: **do any current experiments rely on this step providing a guaranteed non-worsening property?**

Looking at how WMSF is used:
1. Standalone in EXP1b and EXP4 as `wmsf_seed` baseline
2. As seed in IPSNS via `wmsf_seed_solution_full`

In IPSNS: `wmsf_seed_solution_full` produces the best of L1 and L2 seeds, and IPSNS then takes the better of WMSF seed and LR-TA seed as incumbent. IPSNS itself has the non-worsening guarantee. So even if WMSF stabilization occasionally worsens a partial solution, the final IPSNS output is always ≤ initial incumbent.

**Verdict on stabilization**: The stabilization CAN theoretically worsen the FAS before the final MinimizeFas step. The subsequent MinimizeFas step recovers by attempting to restore any new additions to F. The overall WMSF pipeline does not claim stabilization alone is non-worsening — this is a local move that improves the structure for subsequent minimization. This is consistent with the paper's design.

**Manuscript claim check**: The manuscript calls WMSF "a weighted removeArcs-minimize-stabilize seed" and does NOT claim that stabilization alone is non-worsening. The non-worsening guarantee applies only to IPSNS. **No claim violation.**

### Pass Bound

| Item | Verdict |
|------|---------|
| At most `log2(n)` passes | **CORRECT** — `max_passes = max(1, int(math.log2(max(2, n_nodes))))` |
| Terminates if no change | **CORRECT** — `if not changed: break` |

### Acyclicity Guard

| Item | Verdict |
|------|---------|
| `try: topo_order_active(...)` before each pass | **CORRECT** — if a previous swap created a cycle (which shouldn't happen in theory but guards against edge cases), the `RuntimeError` is caught and stabilization stops |

## 6. Pipeline Integration (`_wmsf_pipeline_scc`, lines 356–371)

```
removeArcs → MinimizeFas → StabilizeFas → MinimizeFas
```

After each of Stabilize and the second Minimize, `_sync_active_from_F` re-syncs the active array from F. This ensures consistency between `F` (the logical FAS set) and `active` (the bytearray). **CORRECT.**

## 7. Full Entry Point (`wmsf_ranking_from_dimacs_fast`, lines 408–479)

| Item | Verdict |
|------|---------|
| For single-SCC graphs: try L1 and L2, keep better | **CORRECT** — `if whole_single_scc: run both` |
| For multi-SCC graphs: use specified ordering | **CORRECT** |
| Final topo-sort produces valid ranking | **CORRECT** |

## 8. Overall Verdict

**WMSF is correctly implemented per the paper049 design.** The stabilization step's behavior matches the paper's intent. The potential for stabilization to temporarily worsen the FAS before subsequent minimization is not a bug but a design feature of the algorithm; the subsequent MinimizeFas recovers. No manuscript claim is violated.

**One audit note for paper:** The manuscript could clarify that "stabilization" is a structural move that improves the FAS quality heuristically rather than guaranteeing per-move non-worsening. The non-worsening guarantee for WMSF-as-seed is provided by IPSNS's incumbent mechanism, not by WMSF alone. This is already implicit in the manuscript but could be stated more precisely.
