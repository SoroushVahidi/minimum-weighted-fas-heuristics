# IPSNS Code Audit
**File:** `src/mwfas/ipsns.py` (~914 lines including EXP10 instrumentation)  
**Date:** 2026-06-11

---

## 1. Algorithm Overview

IPSNS (Incumbent-Protected SCC Neighborhood Search):
1. Construct WMSF seed (full pipeline, best of L1/L2 for single-SCC)
2. Construct LR-TA seed (cycle reduction + minimize add-back)
3. Take better as incumbent
4. LNS loop: select SCC by BW-weighted random from top-K; destroy+repair; accept only if strict improvement
5. Restore best snapshot on completion

**Guarantee:** output BW ≤ min(WMSF_BW, LR-TA_BW) under nonneg weights.

## 2. Seed Construction

### WMSF Seed

| Item | Verdict |
|------|---------|
| Uses `wmsf_seed_solution_full` when `wmsf_seed_mode="full"` (default) | **CORRECT** |
| `wmsf_seed_solution_full` mirrors standalone `wmsf_ranking_from_dimacs_fast` exactly | **CORRECT** — same per-SCC pipeline, same L1/L2 trial for single-SCC |
| Consistency: IPSNS WMSF seed = standalone WMSF result | **VERIFIED** — smoke tests confirm identical values |

### LR-TA Seed

| Item | Verdict |
|------|---------|
| Uses `lr_seed_solution`: cycle reduction + minimize add-back | **CORRECT** |
| Uses `wmsf_minimize_global` for add-back (heavy-first, acyclicity-safe) | **CORRECT** |
| Mutable weight array `W_B` independent from `W0` | **CORRECT** — `W_B = list(W_init)` |

### Incumbent Selection

| Item | Verdict |
|------|---------|
| Takes minimum of two seeds | **CORRECT** — `if bw_A <= bw_B: best_bw = bw_A` else `best_bw = bw_B` |
| Snapshot correctly captures `(active, F)` of winning seed | **CORRECT** — `best_snapshot = (bytearray(active_A), set(F_A))` |
| Working state initialized from best seed | **CORRECT** — `active = bytearray(active_A)` or `bytearray(active_B)` |

## 3. LNS Loop

### SCC Selection

| Item | Verdict |
|------|---------|
| SCCs computed once before loop on original graph | **CORRECT** — `comps, comp_id = kosaraju_scc(n, edges_indexed)` before loop |
| SCC list is fixed (original SCCs, not updated dynamically) | **CORRECT** — `scc_list` populated once; reused each iteration |
| BW of each SCC recomputed each iteration using current `rank` | **CORRECT** — `score_scc_backward_weight(e_list, rank)` called inside loop body |
| Only non-zero BW SCCs are candidates | **CORRECT** — `scored = [(bw_scc, v, e) for ... if bw_scc > 0]` |
| Top-K selection with BW-weighted random | **CORRECT** — `pool = scored[:min(topK_scc, len(scored))]`; `random.choices(pool, weights=[x[0] for x in pool])` |
| `scc_select_mode="random"` ablation: uniform random from all non-zero SCCs | **CORRECT** — `random.choices(scored, k=1)[0]` (no weights) |

### Destroy-and-Repair (`lns_step_on_scc`, lines 591–662)

| Item | Verdict |
|------|---------|
| Destroy A: reactivate fraction of removed (heavy) edges in SCC | **CORRECT** — `removed_in_scc = sorted([eid in F], key=(-W0,...)); k_add = int(frac × len); for eid in [:k_add]: active[eid]=1` |
| Destroy B: force-remove fraction of active (light) edges in SCC | **CORRECT** — `active_in_scc = sorted([active], key=(W0,...)); k_rem = int(frac × len); for eid in [:k_rem]: F.add(eid)` |
| Destroy ops are restricted to SCC edges only | **CORRECT** — `internal_eids = [eid for (_, _, _, eid) in scc_edges]` |
| Old state saved before destroy | **CORRECT** — `old_states = [(eid, 1 if active[eid] else 0, 1 if (eid in F) else 0) for eid in internal_eids]` |
| Repair 1: SCC-restricted LR repair | **CORRECT** — `local_ratio_repair_inside_scc(...)` using `allowed_nodes`, `allowed_eids` masks |
| Repair 2: SCC-restricted minimize add-back | **CORRECT** — `minimize_addback_inside_scc(...)` |
| Rollback on repair failure | **CORRECT** — `for eid, a0, f0 in old_states: active[eid] = 1 if a0 else 0; ...` |
| Returns `False` on failure (caller reverts) | **CORRECT** |

### Rollback in Main Loop

| Item | Verdict |
|------|---------|
| `active_before = bytearray(active)` — deep copy | **CORRECT** |
| `F_before = set(F)` — deep copy | **CORRECT** |
| `rank_before = list(rank)` — deep copy | **CORRECT** |
| All three reverted on LNS failure | **CORRECT** — `active = active_before; F = F_before; rank = rank_before` |
| All three reverted on topo failure | **CORRECT** — same three lines |
| All three reverted on non-improvement | **CORRECT** — same three lines in the `else` branch |

### Acceptance

| Item | Verdict |
|------|---------|
| Accept only if `_bw < best_bw - 1e-12` (strict improvement) | **CORRECT** |
| Update `best_snapshot` and `best_bw` on acceptance | **CORRECT** |
| Rollback to `active_before/F_before/rank_before` on rejection | **CORRECT** — note this is NOT rolling back to `best_snapshot`; it rolls back to the pre-move state, which is the current working state (which may differ from best_snapshot) |
| This rollback policy means: working state tracks last accepted or initial state | **CORRECT** — each iteration starts from the post-previous-rejection state, not from the snapshot. This is correct LNS behavior (allows exploration from non-best states) |

**Critical: incumbent guarantee holds because:**
- `best_snapshot` is only updated when `_bw < best_bw`
- `best_bw` is a monotonically non-increasing sequence
- Final output always taken from `best_snapshot`, not from current working state

### Final Output

| Item | Verdict |
|------|---------|
| Restores `best_snapshot` before output | **CORRECT** — `active_best, F_best = best_snapshot` |
| Recomputes topo order from `active_best` | **CORRECT** — `_, rank = topo_order_active(n, out_adj, V, active_best)` |
| Computes BW from recomputed scores | **CORRECT** — `compute_forward_backward(edges_indexed, scores_best)` |

## 4. Reproducibility

| Item | Verdict |
|------|---------|
| `random.seed(rng_seed)` at function start | **CORRECT** — line 721 |
| No other random state modified (no numpy.random, etc.) | **CORRECT** — only `random.choices` used |
| Deterministic for fixed `rng_seed`, input, and parameters | **CORRECT** — all other operations are deterministic |
| Different seeds produce different results | Expected; verified in EXP10 smoke tests |

## 5. EXP10 Diagnostic Instrumentation

The uncommitted changes add 7 counter variables before the LNS loop:
```python
_n_accepted = 0
_n_rejected = 0
_n_failed_repair = 0
_n_topo_failed = 0
_n_noop = 0
_best_iter = 0
_time_to_best = 0.0
```

All increments are inside `if return_info:` guards. Since `return_info=False` by default and all production runs (EXP1–EXP9, holdout, sensitivity) use the default, **this instrumentation has zero impact on any reported results.** The counters are purely additive and cannot change the algorithm's decisions.

## 6. Edge Cases

| Case | Verdict |
|------|---------|
| No SCCs with positive BW (DAG input or already optimal seed) | `scored` is empty; `_n_noop += 1`; breaks immediately; returns best seed | CORRECT |
| Single-node SCCs | Filtered out by `if len(verts) > 1` in `scc_list` construction | CORRECT |
| `iters=0` | Loop body never executes; returns best seed unchanged | CORRECT (verified in smoke tests) |
| All LNS moves fail (fail-repair or no-improvement) | Always returns best seed | CORRECT |

## 7. Objective Recomputation

| Item | Verdict |
|------|---------|
| `compute_forward_backward` called on final `scores_best` | **CORRECT** |
| This independently recomputes BW from the ranking | **CORRECT** |
| `info["final_bw"]` matches independent recomputation | **VERIFIED** in EXP10 smoke tests (objective_match=True for all runs) |

## 8. Incumbent Guarantee Formal Verification

The manuscript states (Prop. 3): `bw(π^(t+1)) ≤ bw(π^(t)) ≤ bw(π^(0))`.

Code evidence:
- `best_bw` initialized to `min(bw_A, bw_B)` = `bw(π^(0))`
- `best_snapshot` stores the corresponding `(active, F)`
- `best_bw` updated only when `_bw < best_bw - 1e-12`
- Final output from `best_snapshot`

**Guarantee holds.** EXP1b confirms: zero incumbent violations across 105 instances.

## 9. Overall Verdict

**IPSNS is correctly implemented.** The incumbent guarantee is enforced at the code level. Rollback is correct and complete. Reproducibility is achieved via `random.seed`. The diagnostic instrumentation is safe and additive. All formal propositions in the manuscript accurately reflect the implementation.
