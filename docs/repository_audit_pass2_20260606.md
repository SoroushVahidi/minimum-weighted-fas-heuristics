# Repository Audit — Pass 2
**Date:** 2026-06-06  
**Auditor:** Claude Sonnet 4.6 (automated)  
**Working directory:** `~/minimum-weighted-fas-heuristics`  
**Prior audit:** `docs/repository_audit_20260606.md` (written at commit `7129e76`)  
**Current HEAD:** `7c741d7` — "Add EXP4 external baseline comparisons"

---

## Executive Summary

Since the prior audit (at EXP1b, commit `7129e76`), three major experiments have been completed and committed:

| Experiment | Status |
|---|---|
| EXP2 — ablation (8 variants, 10 instances) | **Complete** — committed at `d9fe537`, `40ff00e` |
| EXP3 — exact small-instance optimality | **Complete** — committed at `d272f47`, `c549a10` |
| EXP4 — external baseline comparison (7 algorithms, 123 instances) | **Run complete** — raw summary committed here; tables not yet postprocessed |

**Items to note:**
- The prior audit's recommendation to add explicit `wmsf_seed_mode="full"` in `reproduce_all.py` was already implemented.
- `src/mwfas/baselines.py` now exists (Borda, WeightedEades, random, igraph, DRMaciver wrappers); the prior audit incorrectly said it did not exist.
- `README.md` is outdated — does not reflect EXP2-4, new scripts, or the `experiments/` structure.
- **Recommended next action:** Run `postprocess_exp4_external.py` to generate EXP4 tables.

---

## 1. Git State

| Field | Value |
|---|---|
| Branch | `main` |
| HEAD | `7c741d7` |
| Sync with origin | Up-to-date after fetch |
| Untracked (before this commit) | `experiments/exp4_external_baselines/summary/exp4_raw_summary.csv`, `results/` |

---

## 2. EXP4 External Baselines — Run Complete

**Session:** `mwfas_exp4_external` (started 17:03, completed 17:59, 2026-06-06)

| Metric | Value |
|---|---|
| Total instances | 123 |
| Total rows in raw summary | 984 (= 123 instances × 8 algorithms) |
| OK rows | 972 |
| Error rows | 12 |
| Algorithms | lrta_full, wmsf_seed, ipsns_full, borda_net_score, weighted_eades, random_multistart, igraph_approx_eades, drmaciver_fas |

### Error breakdown (12 errors — all expected)

| Algorithm | Count | Cause |
|---|---|---|
| `weighted_eades` | 8 | `negative_weights_detected` — Weighted Eades is undefined for negative-weight edges; affected instances: `gerez`, `howard-max`, `k3_3`, `ku`, `peterson`, `peterson1`, `peterson2`, `stg0` |
| `drmaciver_fas` | 2 | `fas exited 1: Empty tournament` — DRMaciver binary fails on DAG instances with no feedback arcs; affected: `gr00`, `gr7` |
| `drmaciver_fas` | 2 | Timeout (>300 s) — the two largest instances: `s38417` (n=41,336) and `s38584` (n=31,861) |

All errors are well-understood. The three core algorithms (lrta_full, wmsf_seed, ipsns_full) have 0 errors across all 123 instances.

### Postprocessing status

`experiments/exp4_external_baselines/summary/exp4_raw_summary.csv` — **complete, committed here**.  
`experiments/exp4_external_baselines/tables/` — **empty; postprocess not yet run.**

**Recommended next action:** Run `python experiments/exp4_external_baselines/postprocess_exp4_external.py` to generate final comparison tables.

---

## 3. Changes Since Prior Audit

### Prior audit findings (status update)

| Prior Issue | Resolved? |
|---|---|
| EXP2 ablation not yet run | ✅ All 8 variants completed (`d9fe537`, `40ff00e`) |
| `reproduce_all.py` relies on implicit `wmsf_seed_mode` | ✅ Already fixed — line 37 has `"wmsf_seed_mode": "full"` explicit |
| `.gitignore` lacks `*.log` | ✅ Already added — `.gitignore` now includes `*.log` |
| `.gitignore` lacks `venv/` | ✅ Already present — `.gitignore` has `venv/` and `.venv/` |
| EXP2 TODO variants need code changes | ✅ Both `lr_no_addback` and `ipsns_no_scc_priority` were implemented and run |
| `baselines.py` does not exist | ✅ Now exists: `src/mwfas/baselines.py` |

### New since prior audit

- `src/mwfas/baselines.py` — Borda, WeightedEades, random multistart, igraph approx Eades, DRMaciver wrappers for EXP4
- `scripts/run_borda.py`, `run_drmaciver_fas.py`, `run_exact.py`, `run_igraph_eades.py`, `run_random_baseline.py`, `run_weighted_eades.py` — new standalone scripts for external algorithms
- `experiments/exp2_ablation/` — ablation results committed
- `experiments/exp3_exact_small/` — exact small-instance check committed
- `experiments/exp4_external_baselines/` — full external baseline comparison committed (run + raw summary)

---

## 4. EXP2 Ablation Results (Summary)

| Variant | Mean BW | Median BW | Mean Runtime |
|---|---|---|---|
| `lr_no_addback` | 4525.1 | 1025.0 | — |
| `lrta_full` | 4271.5 | 823.5 | 0.047 s |
| `wmsf_seed` | 4332.5 | 823.5 | 0.040 s |
| `best_seed_no_lns` | 4271.5 | 823.5 | 0.069 s |
| `ipsns_50iters` | 4239.2 | 823.5 | 0.778 s |
| `ipsns_100iters` | 4239.2 | 823.5 | 1.500 s |
| `ipsns_full` | 4239.2 | 823.5 | 5.734 s |

Add-back reduces mean BW by ~5.9% (`lr_no_addback` → `lrta_full`). LNS (IPSNS) further reduces by ~0.8%.

---

## 5. EXP3 Exact Small-Instance Results (Summary)

| Subset | IPSNS optimal | LR-TA optimal | WMSF optimal |
|---|---|---|---|
| 57 standard (non-negative-weight) instances | 56/57 (98.2%) | 55/57 (96.5%) | 51/57 (89.5%) |
| 62 all-nontrivial (incl. negative-weight) | 57/62 (91.9%) | 56/62 (90.3%) | 52/62 (83.9%) |

IPSNS achieves optimality on 98.2% of standard instances.

---

## 6. Hygiene Issues Found

### 6.1 README.md — Significantly Outdated (Medium Priority)

The README was written before EXP2-4 and before the new baseline scripts were added. Issues:

1. **Repository layout section** does not show `experiments/` at all — the experiment folders are now the primary reproducibility artifact.
2. **Scripts section** only lists `run_lrta.py`, `run_wmsf.py`, `run_ipsns.py`, `reproduce_all.py`. Six new scripts are not mentioned.
3. **No mention** of EXP1b (definitive benchmark), EXP2 (ablation), EXP3 (exact check), or EXP4 (external baselines).
4. The "reproduce all" path via `reproduce_all.py` is now a legacy convenience script; the main reproducibility path is the per-experiment scripts under `experiments/`.

**Recommended fix:** Rewrite the "Repository layout" and "Usage" sections to reflect current structure and add an "Experiments" section listing completed experiments and how to reproduce them.

### 6.2 EXP4 Tables Empty (High Priority — Next Action)

`experiments/exp4_external_baselines/tables/` is empty. Run:

```bash
python experiments/exp4_external_baselines/postprocess_exp4_external.py
```

Then commit the generated tables.

### 6.3 Existing Audit Report Stale (Low Priority)

`docs/repository_audit_20260606.md` was written at commit `7129e76` (EXP1b). It is now significantly stale (EXP2 was "not yet run"; `baselines.py` reported as absent). This document (pass 2) supersedes its experiment-status sections.

### 6.4 scripts/__pycache__ Present (No Action Needed)

`scripts/__pycache__/` contains `.pyc` files for `run_drmaciver_fas.py` and `run_igraph_eades.py`. Correctly gitignored. No issue.

### 6.5 results/tables/.gitkeep Untracked (Cosmetic)

`results/tables/.gitkeep` shows as untracked. The `.gitkeep` pattern was never committed for this directory. Low importance — the directory is present and functional.

---

## 7. Recommended Next Actions

### Before paper submission (required)

1. **Run EXP4 postprocess:**
   ```bash
   python experiments/exp4_external_baselines/postprocess_exp4_external.py
   ```
   Commit and push the generated tables.

2. **Update README.md** — rewrite layout/usage sections to reflect current state (EXP2-4, new scripts, `experiments/` as the reproducibility entry point).

3. **Make repo public** before citation.

### Lower priority

4. Consider committing `results/tables/.gitkeep` to make the placeholder explicit.
5. Consider adding a top-level `experiments/README.md` summarizing all experiments (EXP1–4, their purpose, status, and how to reproduce each).

---

## 8. Committed Files Audit

| Category | Tracked correctly? |
|---|---|
| Raw `.d` benchmark files | Not in repo (correct; referenced externally) |
| Experiment raw CSVs (`experiments/*/raw/`) | Gitignored (correct) |
| Experiment summary/table CSVs | Tracked via `!experiments/*/summary/*.csv` whitelist (correct) |
| Log files | Gitignored (correct) |
| `__pycache__` / `.pyc` | Gitignored (correct) |
| ZIP files (reference papers) | Tracked — large but intentional reference copies |
| `experiments/*/external_tools/` | Gitignored (correct — cloned repos not committed) |

---

## 9. Final Verdict

| Category | Grade | Notes |
|---|---|---|
| Code correctness | ✅ Pass | All three core algorithms 0 errors across 123 instances |
| Experiment completeness | ✅ Good | EXP1b, EXP2, EXP3, EXP4 raw data complete; EXP4 tables pending postprocess |
| Git hygiene | ✅ Good | No spurious tracked files; gitignore working correctly |
| Reproducibility | ⚠️ Partial | README doesn't reflect current experiment structure |
| Manuscript-readiness | ⚠️ Nearly ready | EXP4 tables needed; README update needed; repo must go public |
| WMSF seed consistency | ✅ Pass | `wmsf_seed_mode="full"` explicit everywhere |
