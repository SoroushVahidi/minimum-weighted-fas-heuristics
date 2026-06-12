# Code Correctness Audit (Overview)
**Date:** 2026-06-11

This document synthesizes findings from LRTA_AUDIT.md, WMSF_AUDIT.md, IPSNS_AUDIT.md, and EXACT_SOLVER_AUDIT.md, and also covers evaluation.py and io.py.

---

## 1. Per-File Summary

| File | Lines | Verdict | Issues |
|------|-------|---------|--------|
| `src/mwfas/lrta.py` | 347 | **CORRECT** | None |
| `src/mwfas/wmsf.py` | 480 | **CORRECT with note** | Stabilization may temporarily worsen FAS (by design; not a bug) |
| `src/mwfas/ipsns.py` | ~914 | **CORRECT** | EXP10 instrumentation uncommitted (safe) |
| `src/mwfas/exact.py` | 146 | **CORRECT** | None |
| `src/mwfas/evaluation.py` | 25 | **CORRECT** | None |
| `src/mwfas/io.py` | 55 | **CORRECT** | None |

## 2. evaluation.py Audit

```python
def compute_forward_backward(edges_indexed, scores):
    total_w = 0.0; fw = 0.0
    for u, v, w in edges_indexed:
        total_w += w
        if scores[u] < scores[v]:
            fw += w
    bw = total_w - fw
    return total_w, fw, bw
```

| Item | Verdict |
|------|---------|
| Forward definition: `scores[u] < scores[v]` | CORRECT — consistent with manuscript definition |
| Self-loops: `scores[u] < scores[u]` = False → backward | CORRECT |
| Parallel arcs: counted per edge after aggregation | CORRECT |
| No mutation of inputs | CORRECT |
| BW = total - FW | CORRECT |

## 3. io.py Audit

```python
def read_graph_dimacs_agg(file_path):
    agg = defaultdict(float)
    # ... parses 'a u v w' lines, aggregates parallel arcs
    node_list = sorted(node_ids)
    edges_indexed = [(node_to_index[u], node_to_index[v], float(w_sum)) ...]
    edges_indexed.sort(key=lambda e: (e[0], e[1]))
    return edges_indexed, node_to_index, index_to_node
```

| Item | Verdict |
|------|---------|
| Parallel arc aggregation | CORRECT — `agg[(u,v)] += w` sums all (u,v) arcs |
| Self-loops | CORRECT — `agg[(u,u)]` accumulates self-loop weight; included in output |
| Deterministic output | CORRECT — `sorted(node_ids)` + edge sort by (src, dst) |
| Node index stability | CORRECT — same input always gives same index assignment |
| Handles `c` and `p` comment/header lines | CORRECT — skipped |
| Handles malformed lines | CORRECT — `if len(parts) < 4: continue` |
| Float parsing | CORRECT — `float(parts[3])`; ValueError caught and skipped |

## 4. Cross-Module Consistency

| Property | Verdict |
|----------|---------|
| All modules use the same `edges_indexed` format `(u_idx, v_idx, w)` | CORRECT |
| All modules use the same node index system from `read_graph_dimacs_agg` | CORRECT |
| `scores` dict `{node_idx: rank}` used consistently | CORRECT |
| `topo_order_active` shared between lrta.py and wmsf.py via import | CORRECT — `from .lrta import topo_order_active, make_reachability_checker` |
| IPSNS imports `_build_local_scc_graph`, `_wmsf_pipeline_scc` from wmsf.py | CORRECT — these are the same exact functions used in standalone WMSF |

## 5. Global State and Concurrency

| Item | Status |
|------|--------|
| Global random state in `random` module | **Present** — `random.seed(rng_seed)` in IPSNS sets global Python random state. This affects any concurrent code using `random`. **For single-process execution (the norm), this is correct.** |
| numpy.random state | Not used |
| Thread safety | Not designed for multi-threading; single-process use only |

**Note:** The use of Python's global `random.seed()` means that if IPSNS is called multiple times in the same process without re-seeding, results will depend on call order. This is correctly handled by EXP10 runner (each call passes its seed explicitly). For standalone use, this is the documented behavior.

## 6. Dead Code / Unused Functions

| Item | Assessment |
|------|-----------|
| `lr_no_addback_ranking_from_dimacs_fast` in lrta.py | Used in ablation study (EXP2); not dead |
| `wmsf_seed_solution` (legacy mode) in ipsns.py | Used when `wmsf_seed_mode="legacy"` (ablation); not dead |
| `wmsf_removeArcs_global` in ipsns.py | Called by `wmsf_seed_solution` (legacy path); not dead |

## 7. Hard-Coded Values

| Value | Location | Assessment |
|-------|----------|-----------|
| `tol=1e-12` default | All algorithms | Appropriate and consistent |
| `n > 20` limit | `exact.py:43` | Documented design limit |
| `topK_scc=15` default | `ipsns.py:675` | Default parameter; documented |
| `iters=400` default | `ipsns.py:674` | Default parameter; documented |

## 8. Error Handling

| Location | Mechanism | Assessment |
|----------|-----------|-----------|
| `topo_order_active` | `RuntimeError` on cycle | Correct — caught in IPSNS for rollback |
| `exact.py` n>20 | `ValueError` | Correct |
| `io.py` malformed lines | `continue` | Correct — silently skips |
| `io.py` float parse failure | `except ValueError: continue` | Correct |
| `run_one` in runners | `except Exception as e` | Correct — records error in JSON |

## 9. Type Annotations and Comments

No formal type annotations in source files (consistent with Python 3.8+ project without strict typing). Docstrings present on all public functions. Comments are sparse and targeted (which the project guidelines require). **Acceptable.**

## 10. Performance Notes

| Bottleneck | Location | Severity |
|-----------|----------|---------|
| DFS cycle detection: O(n+m) per iteration | lrta.py:54 | Expected; unavoidable |
| Topo sort recomputed on every backward add-back | Multiple | Necessary for correctness |
| Full SCC list rescored every iteration | ipsns.py:794 | Minor — could cache; acceptable at current scale |
| `list(rank)` copy every LNS iteration | ipsns.py:815 | Low overhead on current instance sizes |

## 11. Final Verdict

All six production source files are correctly implemented. The code is consistent across modules, handles edge cases appropriately, and implements the formal properties claimed in the manuscript. The only uncommitted change (`ipsns.py` EXP10 instrumentation) is provably safe. No security vulnerabilities, no injection risks (no shell calls in algorithm code), no memory leaks (Python garbage collection).
