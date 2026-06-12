# Baseline Audit

**Audit date:** 2026-06-10

## Baseline taxonomy (counts)

| Category | Count |
|---|---:|
| Independent executable external heuristics | **2** |
| External exact methods (run in experiments) | **0** |
| External exact (documented, not run) | **1** (igraph `method="ip"`) |
| Local adaptations | **3** |
| Local simple baselines (EXP7 LS) | **3** |
| Literature-only / excluded | **5+** |
| Planned not implemented | **2** (`sfas`, igraph exact_ip) |

## Runnable baselines

### External heuristics (EXP4/EXP5)

| ID | Source | Weighted | General digraph | Wrapper |
|---|---|---|---|---|
| `drmaciver_fas` | DRMacIver/Feedback-Arc-Set | Yes (converted) | Yes | `scripts/run_drmaciver_fas.py` |
| `igraph_approx_eades` | python-igraph 1.0.0 | Unweighted approx | Yes | `scripts/run_igraph_eades.py` |

### Local adaptations (`src/mwfas/baselines.py`)

| ID | Method | Notes |
|---|---|---|
| `borda_net_score` | Weighted out−in score | Simple score heuristic |
| `weighted_eades` | Weighted Eades–Lin–Smyth | Rejects negative weights |
| `random_multistart` | Best of trials | Calibration anchor |

### Exact methods

| ID | Location | Used in |
|---|---|---|
| Bitmask DP | `src/mwfas/exact.py` | EXP3 |
| HiGHS MIP | `scripts/run_exp8_medium_mip_baseline.py` | EXP8 (15 instances, time cap) |

### EXP7 local search (not in baselines.py)

`lrta_adj_swap_ls`, `lrta_insert_ls`, `bestseed_insert_ls` — controls vs IPSNS structure.

## Literature-only / excluded (manuscript or registry)

| Method | Status |
|---|---|
| GNNRank | Cited; not compared (different problem setting) |
| LOP_MA-EDM | Not installed |
| Baharev et al. exact MWFAS | Cited in related work; not baseline |
| Simpson et al. web-scale FAS | Cited; not reproduced |
| Cavallaro & Cutello 2025 | Cited; not run |
| fas-smartAE / networkit | Documented unavailable |
| R igraph | Not installed |
| Demetrescu–Finocchi | Cited; no reproduction |
| sfas | Planned |
| igraph exact_ip | Planned |

## Misleading labels / fairness notes

| Issue | Detail |
|---|---|
| `igraph_approx_eades` | Unweighted approximation on weighted instances — manuscript discusses scope; igraph Eades weight guarantee not stated explicitly (B-08 new) |
| DRMacIver incompletions | 4 instances excluded from paired tests (93 not 97) — correctly handled |
| "External baseline" count in prose | Must distinguish 2 external heuristics vs 3 local adaptations |
| WMSF/LR-TA/IPSNS | Internal methods, not independent baselines |
| borda_net_score label | Not clearly labeled "in-repo adaptation" vs "external" in all manuscript locations (B-09) |
| DRMacIver non-determinism | Uses `srand(time\|pid)` — one run per instance; results may vary between runs; NOT disclosed in manuscript (B-07 new) |

## Completeness

EXP4 summary committed. External tools gitignored — reruns need clone documented in `external_access_report.md`.

## Random seeds / time limits

- IPSNS/LR/WMSF: deterministic given inputs (except IPSNS SCC sampling with `rng_seed`)
- DRMacIver: **NON-DETERMINISTIC** — uses `srand(time|pid)`; one run per instance in EXP4; variability undisclosed (B-07)
- MIP: time-capped per EXP8 config
- Random multistart: seeded trials in baselines.py

## 2026-06-11 updates

- sfas identity unresolved — see `BASELINE_EXECUTION_READINESS_AUDIT.md` §B
- igraph exact_ip classified as exact validation (EXP3-scope) not heuristic comparison — see `EXACT_BASELINE_FEASIBILITY.md`
- fas-smartAE confirmed doubly disqualified: unweighted + unavailable (networkit missing)
- New issues added to MASTER_ISSUE_REGISTER.csv: B-06 (sfas), B-07 (DRMacIver non-determinism), B-08 (igraph Eades weight), B-09 (borda labeling), B-10 (DRMacIver runtime missing), B-11 (multiplicity)
- EC-02 flagged for denominator verification: 21.6% figure may be 37-instance gain subset not 93-instance overall mean

## Manuscript alignment

`paper_coap/tables/table_sparse_external_baselines.tex` and `table_paired_sparse_tests.tex` trace to `experiments/exp4_external_baselines/tables/`.
