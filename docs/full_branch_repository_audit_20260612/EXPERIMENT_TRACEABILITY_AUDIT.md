# Experiment Traceability Audit

**Register:** `EXPERIMENT_MASTER_REGISTER.csv` (16 rows)  
**HEAD:** `6c04ff1`

## Manuscript number → canonical file traceability

| Manuscript claim | Experiment | Canonical summary file | Verified |
|---|---|---|---|
| 96/97 best observed sparse (IPSNS) | EXP4 | `experiments/exp4_external_baselines/summary/exp4_external_stats.json` | Yes |
| 21.6% DRMacIver mean excess | EXP4 | same | Yes |
| 38/55/0 median wins (EXP10) | EXP10 | `experiments/exp10_stochastic_robustness/summary/ipsns_validation_summary.json` | Yes |
| 56/57 exact DP matches | EXP3 | `experiments/exp3_exact_small/summary/exp3_exact_stats.json` | Yes |
| 0 incumbent violations (105 inst.) | EXP1b | `experiments/exp1b_core_benchmark_full_wmsf_seed/summary/exp1b_core_benchmark_stats.json` | Yes |
| Ablation 5.9% / 0.75% | EXP2 | `experiments/exp2_ablation/summary/exp2_ablation_stats.json` | Yes |
| LOLIB 45/50 DRMacIver wins | EXP5 | `experiments/exp5_lolib_dense/summary/exp5_lolib_stats.json` | Yes |
| EXP11 zero median Δbw | EXP11 | `experiments/exp11_topological_extraction_sensitivity/summary/exp11_aggregate.json` | Yes |
| MIP/LP reference points | EXP8 | `experiments/exp8_medium_mip_baseline/summary/exp8_final_report.md` | Yes |
| Budget curve flat on subset | EXP6 | `experiments/exp6_ipsns_budget_curve/summary/exp6_final_report.md` | Yes |

## Supersession chain

```
EXP1 (legacy WMSF seed) ──superseded by──► EXP1b (full WMSF seed)
seedfix_full_wmsf ──motivates──► EXP1b rerun
EXP4 primary sparse ──subset──► EXP10 (93 common instances, 20 reps)
LR-TA/IPSNS DAG outputs ──post-hoc──► EXP11 (extraction sensitivity)
coap_ipsns_sensitivity (OAT) ──feeds narrative──► holdout (partial checkpoints)
```

**EXP1 must not be cited** in COAP manuscript; EXP1b is canonical for internal benchmark safety.

## Raw output and checkpoint policy

| Experiment | Raw tracked? | Checkpoints tracked? | Summaries tracked? |
|---|---|---|---|
| EXP1b–EXP9 | No (gitignored) | Mostly no | Yes |
| EXP10 | No (local ~3720+ JSON files) | Local `.done` files | Yes |
| EXP11 | N/A (uses prior DAGs) | No | Yes |
| coap_ipsns_sensitivity | Checkpoints committed | Yes | Yes |
| coap_ipsns_holdout | Partial | Yes | **No summary/** |

## Reproducibility levels

| Level | Supported experiments |
|---|---|
| **A – Smoke/tests** | All via pytest + OR1 scripts |
| **B – Table regen from summaries** | EXP3–5, EXP10, EXP11 via OR1 `reproduce_principal_tables.sh` |
| **C – Re-run from configs** | EXP1b–EXP9 scripts; requires external benchmarks |
| **D – Full EXP10 raw rerun** | Requires DRMacIver binary + compute; summaries suffice for paper |

## Unresolved traceability gaps

1. **`experiments/combined/summary/manuscript_results_digest.json`** — predates EXP6–11; not authoritative for newest claims.
2. **Holdout** — checkpoints exist; no committed aggregate summary JSON/MD.
3. **EXP10 `experiment_progress.json`** — `status: NONFINAL` despite `completed_ok: true` (metadata only).

## Verdict

All **manuscript-reported numbers trace to committed summary artifacts**. Raw reruns are optional for verification, not required for submission integrity.
