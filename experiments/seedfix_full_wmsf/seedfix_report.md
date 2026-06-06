# IPSNS Full WMSF Seed Fix Report

**Date:** 2026-06-06  
**Branch:** main

---

## What Changed in IPSNS

### Problem
The IPSNS internal WMSF seed used a simplified global algorithm that differed from
standalone WMSF (`wmsf_ranking_from_dimacs_fast`):

| Property | Legacy internal seed | Standalone WMSF |
|----------|---------------------|-----------------|
| Ordering | L2 only | L2 (multi-SCC) or best of L1+L2 (single-SCC) |
| Pipeline | global removeArcs + minimize | per-SCC removeArcs → Minimize → **Stabilize** → Minimize |
| Scope | global (not per-SCC) | per-SCC with local re-indexing |

This caused `gr10` to have IPSNS internal WMSF seed = 58,839 while standalone WMSF = 58,481.
The incumbent-protection guarantee held relative to internal seeds (0 true violations),
but the paper's stated guarantee (`IPSNS ≤ min(LR-TA, WMSF)`) was not met for `gr10`.

### Fix
Added `wmsf_seed_solution_full()` to `src/mwfas/ipsns.py`. This function:
- Iterates over SCCs (same Kosaraju decomposition already computed in IPSNS)
- For each non-trivial SCC: builds local re-indexed graph, runs the full
  `_wmsf_pipeline_scc` (removeArcs → Minimize → Stabilize → Minimize)
- For whole-single-SCC graphs: tries both L1 and L2, keeps the better result
- Reuses `_build_local_scc_graph` and `_wmsf_pipeline_scc` imported from `wmsf.py`

The `lns_merge_wmsf_lr_best_incumbent` function gained two new parameters:
- `wmsf_seed_mode="full"` (default): uses the full pipeline; `"legacy"` for the old behavior
- `return_info=False`: when `True`, returns a 6th value (dict) with diagnostic keys
  `lr_seed_bw`, `wmsf_seed_bw`, `best_seed_bw`, `final_bw`, `improved`, `n_iters`, `status`

`scripts/run_ipsns.py` gained `--wmsf-seed-mode` CLI flag (default: `full`).

---

## Does IPSNS Now Use the Full Standalone WMSF Seed?

**Yes.** The `wmsf_seed_mode="full"` path calls the exact same helper functions
(`_build_local_scc_graph`, `_wmsf_pipeline_scc`) that `wmsf_ranking_from_dimacs_fast`
uses, with identical SCC decomposition and ordering logic.

---

## Diagnostic Results (gr10, gr00, gr7)

| Instance | LR-TA BW | Standalone WMSF BW | IPSNS WMSF seed BW | IPSNS final BW | Guarantee holds? |
|----------|----------|-------------------|--------------------|----------------|-----------------|
| gr10     | 62,435   | **58,481**        | **58,481** ✓       | 58,481         | **YES** |
| gr00     | 0        | 0                 | 0                  | 0              | YES |
| gr7      | 0        | 0                 | 0                  | 0              | YES |

**gr10 mismatch resolved:** IPSNS internal WMSF seed now = 58,481 (matches standalone).
IPSNS final also = 58,481; LNS found no improvement over the full WMSF seed.

**gr00 and gr7:** Still clean (empty graphs, bw=0, no division-by-zero with the earlier fix).

---

## 10-Instance Smoke Test (`exp2_ablation_instances.txt`)

Run inline (no tmux needed; total time ≈ 58s driven mostly by `r1000` at 56s).

| Instance | LR-TA BW | WMSF BW | IPSNS seed | IPSNS final | LNS improved | OK? |
|----------|----------|---------|------------|-------------|--------------|-----|
| bad1     | 94       | 94      | 94         | 94          | No           | ✓ |
| bad2     | 180      | 180     | 180        | 180         | No           | ✓ |
| bad3     | 1519     | 1632    | 1632       | 1519        | No           | ✓ |
| bad4     | 877      | 877     | 877        | 877         | No           | ✓ |
| bad5     | 770      | 770     | 770        | 770         | No           | ✓ |
| bad6     | 218      | 218     | 218        | 218         | No           | ✓ |
| bad7     | 1724     | 1724    | 1724       | 1724        | No           | ✓ |
| bad      | 1        | 1       | 1          | 1           | No           | ✓ |
| grid     | 32957    | 33294   | 33294      | **32954**   | **Yes**      | ✓ |
| r1000    | 4375     | 4535    | 4535       | **4055**    | **Yes**      | ✓ |

**10/10 pass.** No errors. Guarantee `IPSNS_final ≤ min(LR-TA, WMSF)` holds for all.  
tmux was **not** used (total time < 2 min).

Note on `bad3`: IPSNS WMSF seed = 1632 (WMSF), but IPSNS final = 1519 (= LR-TA).
This is correct — LR-TA was the better seed, so IPSNS started from LR-TA's solution.

---

## New Errors?

None. All 10 instances ran without errors.

---

## Should EXP1 Be Rerun?

**Yes, for full correctness.** With `wmsf_seed_mode="full"` as the new default,
EXP1 results may improve (or stay the same) for some instances where the legacy
WMSF seed was weaker than standalone WMSF. Any instance where standalone WMSF
beats the legacy internal seed could now see IPSNS tied with or improving on WMSF,
correcting apparent violations. A full rerun with the updated code would replace
the existing `exp1_raw_summary.csv` with results that satisfy the stronger guarantee.

---

## Changed Files

| File | Change |
|------|--------|
| `src/mwfas/ipsns.py` | Added `wmsf_seed_solution_full()`, updated imports, added `wmsf_seed_mode` and `return_info` params to `lns_merge_wmsf_lr_best_incumbent` |
| `scripts/run_ipsns.py` | Added `--wmsf-seed-mode` CLI flag |

---

## Outputs

```
experiments/seedfix_full_wmsf/
  diagnostic_seed_comparison.csv   — per-instance bw values for gr10/gr00/gr7
  diagnostic_seed_comparison_raw.txt — verbose output for diagnostic instances
  smoke_test_10inst.txt            — smoke test verbose output
  seedfix_report.md                — this file
```
