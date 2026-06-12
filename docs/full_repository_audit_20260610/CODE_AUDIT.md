# Code Architecture Audit

**Audit date:** 2026-06-10  
**Scope:** `src/mwfas/`, key scripts  
**Mode:** Read-only

## Architecture summary

Three-tier design:
1. **LR-TA** — global local-ratio cycle reduction + heavy-first topological add-back (`lrta.py`)
2. **WMSF** — Kosaraju SCC decomposition + per-SCC removeArcs/minimize/stabilize pipeline (`wmsf.py`)
3. **IPSNS** — dual-seed (WMSF full + LR) incumbent protection + SCC-scored destroy-repair LNS (`ipsns.py`)

Shared: DIMACS I/O (`io.py`), objective (`evaluation.py`), tolerance default `1e-12`.

## Module map

See subagent audit for full function lists. Key public entry points:

| Module | Public API |
|---|---|
| `lrta.py` | `local_ratio_fas_fast`, `topo_order_active`, `make_reachability_checker`, `paper_fas_ranking_from_dimacs_fast` |
| `wmsf.py` | `kosaraju_scc`, `wmsf_ranking_from_dimacs_fast` |
| `ipsns.py` | `lns_merge_wmsf_lr_best_incumbent` |
| `exact.py` | `exact_min_fas_dp`, `exact_min_fas_from_dimacs` |
| `baselines.py` | Borda, weighted Eades, random multistart |

## Algorithm flow highlights

### LR-TA
- Cycle: first DFS back-edge (`find_any_cycle_eids`, `lrta.py` ~54–122)
- Reduction: subtract min cycle weight; deactivate ≤ tol (`local_ratio_fas_fast` ~238–259)
- Add-back: heavy-first; forward rank O(1); backward needs reachability; re-topo after backward (~264–281)

### WMSF
- Per-SCC pipeline: removeArcs → minimize → stabilize (≤ log₂ n passes) → minimize (`_wmsf_pipeline_scc`)
- Single-SCC whole graph: run L1 and L2 orderings, pick lower BW

### IPSNS
- Seeds: WMSF full + LR reduction + global minimize; pick lower BW incumbent
- SCC selection: score by backward weight; weighted sample from top-K
- Destroy: deterministic fractions (`int(frac * n)`)
- Accept: strict improvement `bw < best_bw - 1e-12`; else rollback to pre-step snapshot
- Output: always `best_snapshot` (never worse than best seed)

## Issues found

| ID | Severity | Finding | Evidence |
|---|---|---|---|
| C-01 | Moderate | **~4× duplicated logic** (cycle find, removeArcs, minimize, reachability) across `lrta`, `wmsf`, `ipsns` | Parallel functions in three modules |
| C-02 | Moderate | **Private API coupling**: `ipsns` imports `wmsf._is_acyclic_active`, `_wmsf_pipeline_scc`, etc. | `ipsns.py` imports |
| C-03 | Moderate | **Global `random.seed`** in IPSNS — not thread-safe; differs from baselines using `Random(seed)` | `ipsns.py` ~721 |
| C-04 | Minor | Unused imports: `compute_forward_backward` in `lrta.py`, `exact.py` | Static inspection |
| C-05 | Minor | Unused parameter `U` in `find_any_cycle_eids` | `lrta.py` |
| C-06 | Minor | `lr_no_addback_ranking_from_dimacs_fast` not exposed in `run_lrta.py` | Ablation uses direct import |
| C-07 | Minor | Tie-break in standalone LR add-back sort omits `eid` (WMSF/IPSNS include it) | `lrta.py` ~265 |
| C-08 | Moderate | **Negative weights not rejected** in core algorithms (only Eades baseline checks) | `baselines.py` vs core modules |
| C-09 | Low | Crash mid-run loses work until checkpoint resume (COAP drivers) | Sensitivity/holdout drivers |
| C-10 | Low | IPSNS prints metrics even when `log_every=0` | `ipsns.py` ~865–872 |
| C-11 | Moderate | **No tests** for theorem-critical paths | No `tests/` directory |

## Scalability

- Phase I cycle finding: O(m) per iteration, up to m iterations — acceptable for sparse graphs
- IPSNS per iteration: O(m) SCC scoring + one repair — dominant on large instances (e.g. `s38417`)
- Exact DP: exponential — correctly limited to n≤20

## Serialization / checkpoint

COAP drivers write per-run JSON checkpoints with `status`, `backward_weight`, config hash. Resume skips valid checkpoints. Failures write `*.FAILED.json`. Holdout results in untracked `results/runs.jsonl`.

## Hard-coded paths

None in `src/mwfas/`. Tracked CSV configs contain `/home/soroush/benchmark_sources/...` — portability issue, not algorithm bug.

## Recommendations (deferred)

1. Add focused unit tests for add-back, rollback, tolerance, SCC repair
2. Refactor duplicated cycle/minimize into shared module (post-submission)
3. Replace `random.seed` with local `Random` instance in IPSNS
4. Add `eid` to LR-TA add-back sort for consistency
