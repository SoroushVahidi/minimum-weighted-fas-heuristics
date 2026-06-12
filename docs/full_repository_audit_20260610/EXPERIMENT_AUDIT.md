# Experiment Audit

**Audit date:** 2026-06-10

## Summary matrix

| Experiment | Path | Status | Raw data | Manuscript | Provenance |
|---|---|---|---|---|---|
| Core 97-instance (via EXP1b+EXP4) | `exp1b_*`, `exp4_*` | Complete | Local gitignored | Tables + §6 | Committed summaries |
| Ablation | `exp2_ablation/` | Complete | 80 raw local | `table_ablation.tex` | OK |
| Exact DP | `exp3_exact_small/` | Complete | 265 raw local | `table_exact_validation.tex` | OK |
| MIP | `exp8_medium_mip_baseline/` | Complete | Summaries only | `table_medium_mip_baseline.tex` | OK |
| External baselines | `exp4_external_baselines/` | Complete | 828 raw local | `table_sparse_external_baselines.tex` | DRMacIver 4 incompletions |
| LOLIB dense | `exp5_lolib_dense/` | Complete | 400 raw; 51 converted tracked | `table_lolib_scope.tex` | OK |
| Budget curve | `exp6_ipsns_budget_curve/` | Complete | 120 raw local | `table_ipsns_budget_curve.tex` | OK |
| Plain LS | `exp7_plain_local_search/` | Complete | **No raw dir** | `table_plain_local_search.tex` | Summaries only |
| Application | `exp9_application_case/` | Complete | Minimal raw | `table_application_case.tex` | README says "pending" (stale) |
| Sensitivity stage 1 | `coap_ipsns_sensitivity/` | Complete (preliminary) | 140 ckpts tracked | Notes only | Conclusion B |
| Holdout stage 2 | `coap_ipsns_holdout/` | **Running ~42%** | Untracked | Notes only | Launch `90af464` |
| Legacy EXP1 | `exp1_core_benchmark/` | **Obsolete** | Local | Do not cite | Superseded by EXP1b |

## Holdout detail (at audit)

| Metric | Value |
|---|---|
| Plan | 43 instances × 6 configs × 5 seeds = 1290 |
| Pending at launch | 1286 |
| Log progress | 540/1286 |
| Checkpoints | 544 |
| Failures | None (`failures.jsonl` absent) |
| Completion marker | `COMPLETED.ok` absent |
| Post-process summary | Missing |

## Manuscript number traceability

Committed paths for verification:
- `experiments/combined/summary/manuscript_results_digest.md` (EXP1b–5)
- `experiments/exp1b_core_benchmark_full_wmsf_seed/tables/exp1b_core_benchmark_paper_summary.csv`
- `experiments/exp4_external_baselines/tables/exp4_external_paper_summary.csv`
- Per-experiment `summary/*_stats.json`

**Gap:** Combined digest excludes EXP6–9 (integrated directly in TeX).

## Raw data policy

`.gitignore` excludes `experiments/*/raw/`. **Inference:** Full raw reproduction requires local disk or rerunning drivers documented in experiment READMEs / `REPRODUCE.md` (EJCO artifact).

## Known limitations (documented)

- 8 negative-weight instances excluded from "standard 97"
- DRMacIver incomplete on 4 sparse instances
- EXP7 excludes peterson1/2
- Stage-1 sensitivity on 10 EXP2 instances only — not holdout-validated
- Parameter defaults in manuscript cite 400 iterations — holdout may change this

## Classification counts

| Class | Count |
|---|---|
| Complete and manuscript-ready | 9 (EXP1b,2,3,4,5,6,7,8,9) |
| Complete but preliminary | 1 (sensitivity) |
| Running | 1 (holdout) |
| Obsolete | 1 (EXP1) |
| Missing raw in Git | All primary benchmarks (by design) |

## 2026-06-11 baseline-audit updates

| Finding | Impact | Issue |
|---|---|---|
| EXP4 DRMacIver non-deterministic (`srand(time\|pid)`); one run per instance | Reproducibility gap; not disclosed | B-07 |
| 21.6% DRMacIver relative-excess figure verified correct | EC-02 closed — no action | CLOSED |
| igraph exact_ip reclassified: belongs to EXP3-scope exact validation, not EXP4 heuristic comparison | Phase 5 scope change | EXACT_BASELINE_FEASIBILITY.md |
| fas-smartAE confirmed unweighted + unavailable; not a viable MWFAS baseline | Confirms correct EXP4 exclusion | BASELINE_EXECUTION_READINESS_AUDIT.md |
| sfas identity unresolved — no paper/URL/code in repo | Must clarify before submission | B-06 |
| All 25 empirical claims in EXP4/EXP3/EXP8 verified safe or safe-after-minor-qualification | Confirms experimental narrative | EMPIRICAL_CLAIM_SAFETY_REGISTER.csv |
