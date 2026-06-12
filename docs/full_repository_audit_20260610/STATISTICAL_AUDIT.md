# Statistical Analysis Audit

**Audit date:** 2026-06-10

## Methods used (observed)

| Analysis | Location | Test type |
|---|---|---|
| Paired sparse comparison | `paper_coap/tables/table_paired_sparse_tests.tex`, `06_results.tex` | Wilcoxon signed-rank + sign test, two-sided |
| Win/tie/loss counts | `06_results.tex` | Descriptive |
| Exact validation gap | EXP3 summaries | Mean relative gap ~0.0006% |
| Ablation | EXP2 tables | Per-instance comparisons |
| Budget curve | EXP6 | Iteration vs BW |

## Verified properties

| Property | Status | Evidence |
|---|---|---|
| Paired tests for EXP4 | **Yes** | Instance-level paired differences |
| Instance dependence respected | **Yes** | Per-instance units |
| Tie handling in sign test | Documented in table caption | `table_paired_sparse_tests.tex` |
| Missing-run handling | DRMacIver: 93/97 paired | Caption notes exclusions |
| Multiple comparisons | **Partial** | Several baselines tested; no explicit multiplicity correction |
| Normalized vs raw BW | Mostly raw BW | Holdout plan uses normalized improvement for tuning |

## Weaknesses

| ID | Severity | Finding |
|---|---|---|
| S-01 | Major | Heavy reliance on **win counts and means**; limited reporting of full BW distributions |
| S-02 | Major | **No confidence intervals** on aggregate gaps |
| S-03 | Moderate | **Single rng_seed** for main benchmark (seed 1) — stage-1 showed invariance for baseline on 10 instances only |
| S-04 | Major | **Parameter tuning vs final claims**: stage-1 on EXP2 subset overlaps ablation instances — not independent |
| S-05 | Moderate | Holdout designed but **incomplete** — cannot support default-change claims yet |
| S-06 | Moderate | Wilcoxon p-values reported but **effect sizes** not standardized |
| S-07 | Minor | No seed-variability table for IPSNS on full 97 instances |
| S-08 | Moderate | EXP5 dense comparison lacks same paired-test depth as EXP4 |
| S-09 | Low | No compute-matched runtime comparison across methods |
| S-10 | **Moderate** | **DRMacIver uses `srand(time\|pid)`** — non-deterministic; one run per instance in EXP4; variability undisclosed in manuscript. Added 2026-06-11. See B-07 in MASTER_ISSUE_REGISTER. |
| S-11 | Low | **21.6% DRMacIver figure denominator unclear** — `mean_rel_gain_ipsns_pct` in EXP4 CSV may be computed only on the 37-instance IPSNS-wins subset, not on the 93-instance overall mean. Must verify postprocessing script. See EC-02 in EMPIRICAL_CLAIM_SAFETY_REGISTER. Added 2026-06-11. |
| S-12 | Low | **No explicit multiplicity-correction acknowledgment** for 8-method multi-comparison table. Standard practice allows no correction, but acknowledgment should be added. Added 2026-06-11. See B-11. |

## Recommendations

1. Complete holdout; report 5-seed dispersion on holdout split only
2. Add per-instance normalized gap CIs for key comparisons (bootstrap on instances)
3. Report medians alongside means in supplementary tables
4. Keep tuning/holdout separation explicit in parameter section
5. Do not upgrade stage-1 screening to "robust default selection" without holdout

## Tuning vs holdout separation (COAP study)

| Stage | Instances | Purpose | Manuscript use |
|---|---|---|---|
| Stage 1 | 10 (EXP2 overlap) | OAT screening | Notes only; conclusion B |
| Stage 2 tuning | 18 | Config selection | Pending |
| Stage 2 holdout | 25 (includes r20_60) | Confirmation | Pending |

Pre-registered rules in `holdout_plan.yaml` and `COAP_DEFAULT_SELECTION_DECISION.md`.
