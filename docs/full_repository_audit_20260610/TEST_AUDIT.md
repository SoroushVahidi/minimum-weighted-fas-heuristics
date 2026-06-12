# Test Audit

**Audit date:** 2026-06-10

## Inventory

| Category | Count | Location |
|---|---:|---|
| Project unit tests | **0** | No `tests/` directory |
| Project integration tests | **0** | — |
| External vendored tests | 1 | `experiments/exp4_external_baselines/external_tools/fas-smartAE/test_reductions.py` (requires networkit; not runnable here) |
| CI workflows | **0** | No `.github/workflows/` |

## Test run (safe, conservative)

**Command:**
```bash
python3 -m pytest --ignore=experiments/exp4_external_baselines/external_tools -q
```

**Result:**
| Metric | Value |
|---|---|
| Passed | 0 |
| Failed | 0 |
| Skipped | 0 |
| Errors | 0 (with ignore flag) |
| Runtime | ~0.32 s |
| Coverage | Not configured |

**Note:** Without `--ignore`, pytest errors on fas-smartAE import (`ModuleNotFoundError: networkit`).

**Impact on active holdout:** None — pytest does not import IPSNS holdout drivers when no tests collected.

## Missing tests (priority)

| Area | Rationale | Severity |
|---|---|---|
| Simple cycle extraction | Phase I correctness | Major |
| Exact tight-arc removal at tolerance | Formal analysis Prop. 1 | Major |
| Add-back acyclicity (forward/backward rules) | Prop. 2 | **Blocker** for proof confidence |
| Stale topological order handling | Manuscript claim | Major |
| Backward-set / reachability containment | Add-back safety | Major |
| SCC decomposition correctness | WMSF/IPSNS foundation | Moderate |
| Seed-selection dominance (IPSNS ≥ best seed) | Prop. 3 | **Blocker** |
| Rollback on failed repair | Prop. 3 | Major |
| Incumbent non-worsening | Core claim | **Blocker** |
| Checkpoint resume / duplicate prevention | COAP experiment integrity | Moderate |
| DIMACS conversion / parallel-edge aggregation | I/O correctness | Moderate |
| External baseline objective equivalence | EXP4 fairness | Major |
| Destroy fraction edge cases (small SCCs → int truncation) | Known code behavior | Moderate |

## Flaky tests

None observed (no project tests).

## Recommendations

1. Add `tests/` with pytest targeting `src/mwfas/` — no dependency on external_tools
2. Add GitHub Actions: `pytest`, optional `tectonic paper_coap/main.tex`
3. Mark theorem-critical tests explicitly in test module docstrings
4. Do **not** run full benchmark regression in CI (too slow)
