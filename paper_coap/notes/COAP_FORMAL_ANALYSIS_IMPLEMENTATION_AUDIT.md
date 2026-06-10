# COAP Formal Analysis — Implementation Audit

**Date:** 2026-06-10  
**Scope:** Source modules under `src/mwfas/` used by the COAP manuscript algorithms.

## Shared representation

| Item | Implementation |
|---|---|
| Graph input | `read_graph_dimacs_agg` in `io.py` |
| Edge storage | Parallel arrays `U`, `V`, `W0`, mutable `W` (LR/IPSNS), `active` bytearray |
| Adjacency | Outgoing lists `adj` / `out_adj`; WMSF/IPSNS also keep `in_adj` |
| Objective | `compute_forward_backward` in `evaluation.py`: one pass over edges, \(O(m)\) |
| Topological order | `topo_order_active`: Kahn with min-heap tie-breaking, \(O(n+m)\) |
| Reachability | Stamp-based DFS with rank upper bound (`make_reachability_checker`) |
| SCCs | `kosaraju_scc` in `wmsf.py`, \(O(n+m)\) |

## LR-TA (`lrta.py`)

| Topic | Functions / structures |
|---|---|
| Entry point | `local_ratio_fas_fast`, `paper_fas_ranking_from_dimacs_fast` |
| Phase I | `find_any_cycle_eids` + weight reduction loop |
| Phase II | sort removed set; `topo_order_active`; `make_reachability_checker` |
| Cycle search | Iterative DFS from vertices `0..n-1`, first cycle found |
| Deactivation | Arcs with `W[eid] <= tol` removed from active set |
| Add-back forward | `rank[u] < rank[v]` → reactivate, **no topo recompute** |
| Add-back backward | `reachable(v,u,rank_limit=rank[u])` false → reactivate + **topo recompute** |
| Data structures | Sparse outgoing adjacency only; no dense matrix |
| Practical notes | Multiple arcs may deactivate in one Phase I round; still ≤ \(m\) rounds |

## WMSF-style seed (`wmsf.py`, IPSNS seed helpers)

| Topic | Functions / structures |
|---|---|
| Standalone entry | `wmsf_ranking_from_dimacs_fast` |
| IPSNS full seed | `wmsf_seed_solution_full` in `ipsns.py` |
| SCC pipeline | `_wmsf_pipeline_scc`: removeArcs → minimize → stabilize → minimize |
| removeArcs | `wmsf_removeArcs_scc` / `wmsf_removeArcs_global`: L1 or L2 sort, 2-cycle prep, safe-arc trim, periodic acyclicity checks |
| minimize | `wmsf_minimizeFas_scc` / `wmsf_minimize_global`: same add-back rules as LR-TA |
| stabilize | `wmsf_stabilizeFas_scc`: up to \(\lfloor\log_2 n\rfloor\) passes over topo order |
| Single-SCC graphs | Both L1 and L2 pipelines run; lower backward-weight seed kept |
| Local SCC graph | `_build_local_scc_graph` reindexes vertices/edges per SCC |

## IPSNS (`ipsns.py`)

| Topic | Functions / structures |
|---|---|
| Driver | `lns_merge_wmsf_lr_best_incumbent` |
| Seeds | `wmsf_seed_solution_full` + `lr_seed_solution` (`lr_cycle_reduction_global` + `wmsf_minimize_global`) |
| SCC scoring | `score_scc_backward_weight`: sum weights of backward internal arcs |
| Selection | Top-\(K\) by score; weighted random (`weighted`) or uniform (`random`) |
| Destroy/repair | `lns_step_on_scc` |
| Restricted LR | `local_ratio_repair_inside_scc`, `find_any_cycle_eids_restricted` |
| Restricted add-back | `minimize_addback_inside_scc`, `topo_order_active_restricted` |
| Rollback | SCC snapshot restore on `RuntimeError`; global restore if topo fails or BW not improved |
| Incumbent | `best_snapshot` stores `(active, F)`; output always from snapshot |
| Default budget | `iters=400`, `topK_scc=15`, `wmsf_seed_mode="full"` |

## Manuscript/code alignment (pass 3)

| Topic | Status |
|---|---|
| Topo recompute after forward add-back | **Not performed** in code; manuscript/pseudocode consistent (forward shortcut only) |
| Reachability direction for backward add-back | Test `v → u`; consistent |
| Tolerance handling | `tol=1e-12`; special branch when `eps <= tol` |
| IPSNS rollback scope | Full incumbent restored on non-improvement; SCC-local restore on invalid repair |
| WMSF L1/L2 on single SCC | Implemented in both standalone WMSF and IPSNS full seed |

No blocking manuscript/code discrepancy required a scientific change in this pass.

## Complexity drivers (implementation-derived)

| Component | Dominant loops |
|---|---|
| LR-TA Phase I | ≤ \(m\) × cycle DFS \(O(n+m)\) |
| LR-TA Phase II | Sort \(r\) + up to \(r\) reachability/topo recomputations |
| WMSF per SCC | Sort + deletions + up to 2 minimize passes + ≤ \(\log n\) stabilize passes |
| IPSNS iteration | Score all SCCs \(O(m)\) + one SCC repair + global eval \(O(n+m)\) |

## Intentionally conservative / unproved in this pass

- Exact count of Phase I iterations when multiple deactivations occur per round (safe bound remains \(m\))
- Tight stabilization cost beyond stated conservative scan bound
- Expected-case or sparse-graph average complexity
- Convergence to local/global optimum for IPSNS
