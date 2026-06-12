# Production Source Code Audit

**Scope:** `src/mwfas/*.py` (canonical); cross-checked against OR1 mirror.  
**HEAD:** `6c04ff1`

## Package overview

| Module | Lines (approx.) | Purpose |
|---|---|---|
| `lrta.py` | ~320 | LR-TA: local-ratio cycle reduction + topological heavy-first add-back |
| `wmsf.py` | ~410 | WMSF-style removeArcs / minimize / stabilize on SCCs |
| `ipsns.py` | ~700 | IPSNS: SCC scoring, destroy/repair, dual-seed merge |
| `topo_extraction.py` | ~220 | Linear extensions of active DAG; EXP11 rules |
| `exact.py` | ~110 | Bitmask DP exact solver |
| `evaluation.py` | ~30 | Forward/backward weight from scores |
| `io.py` | ~55 | DIMACS reader with parallel-arc aggregation |
| `baselines.py` | ~200 | Borda, weighted Eades, random multistart, igraph |
| `__init__.py` | minimal | Package marker |

## Cross-cutting behavior (verified in code)

| Topic | Implementation |
|---|---|
| **Nonnegative weights** | Assumed throughout; negative instances excluded in experiments |
| **Tolerance** | Default `1e-12` in LR-TA, WMSF, IPSNS |
| **Parallel edges** | Aggregated at read time in `io.py` |
| **Self-loops** | Not specially filtered in reader; benchmark instances typically none |
| **RNG** | IPSNS: seeded SCC selection; `random_multistart` baseline uses seeds |
| **Tie-breaking** | Deterministic sorts on vertex IDs / edge IDs in topo and add-back |
| **Negative-weight handling** | No reformulation; excluded from standard comparisons |

## Module notes

### `lrta.py` (LR-TA)

- **Provenance:** Demetrescu–Finocchi local-ratio cycle reduction + engineered add-back.
- **Public API:** `local_ratio_fas_fast`, `paper_fas_ranking_from_dimacs_fast`, `lr_no_addback_ranking_from_dimacs_fast`.
- **Tests:** `tests/unit/test_lrta.py`, known instances, CLI smoke.
- **Manuscript:** §4, Proposition feasibility; not claimed as novel theory.
- **Debt:** Low; well-covered.

### `wmsf.py` (WMSF-style)

- **Provenance:** Cavallaro–Cutello minimal-and-stable pipeline (engineered variant).
- **Public API:** `wmsf_ranking_from_dimacs_fast`; internal SCC helpers.
- **L1/L2:** `ordering="L2"` default for removeArcs.
- **Tests:** `test_wmsf.py`, `test_wmsf_safe_edge.py`.
- **Debt:** Moderate complexity in stabilize; documented in OR1 S3.

### `ipsns.py` (IPSNS)

- **Provenance:** Primary novel integration in this repository.
- **Public API:** `lns_merge_wmsf_lr_best_incumbent` (main entry).
- **Incumbent protection:** Strict improvement on backward weight only.
- **Duplicate logic:** Some cycle-finding code parallels `lrta.py` (restricted vs global) — intentional for SCC-local repair.
- **Tests:** `test_ipsns.py`, `test_ipsns_rollback.py`.
- **Debt:** Large module; acceptable for research code.

### `topo_extraction.py`

- **Added for EXP11;** extraction rules: min-id, max-id, weighted-net, insertion-refine.
- **Tests:** `test_topo_extraction_math.py`.
- **Manuscript:** Problem §3 inequality; EXP11 table.

### `exact.py`

- Bitmask DP; practical limit n≤20.
- **Tests:** `test_exact.py`, brute-force cross-checks.

### `baselines.py`

- DRMacIver invoked via external subprocess in experiment scripts, not in this module.
- igraph wrapper included.

## Dead code / debugging

No active `pdb` or `print` debug blocks found in canonical modules. No `TODO`/`FIXME` in `src/mwfas/`.

## Duplication risk

| Copy | Relationship |
|---|---|
| `online_resource_1/src/mwfas/` | Synced from repo at OR1 freeze; should track `src/mwfas/` on future updates |
| `submission_package/ejco_reproducibility_artifact/src/mwfas/` | **Stale** EJCO-era snapshot |

## Verdict

Production source is **consistent with manuscript claims**, **well-tested** on core paths, and **frozen appropriately** for submission. No submission-blocking code defects identified.
