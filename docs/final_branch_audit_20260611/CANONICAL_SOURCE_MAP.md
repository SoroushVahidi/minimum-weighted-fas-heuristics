# Canonical Source Map
**Date:** 2026-06-11

---

## 1. Primary Algorithm Files

| Role | Canonical File | SHA-256 (first 16) | Status |
|------|---------------|--------------------|--------|
| LR-TA algorithm | `src/mwfas/lrta.py` | `see validate_environment.py output` | Committed, definitive |
| WMSF algorithm | `src/mwfas/wmsf.py` | `see validate_environment.py output` | Committed, definitive |
| IPSNS algorithm | `src/mwfas/ipsns.py` | — (uncommitted EXP10 changes) | Modified, needs commit |
| Exact DP solver | `src/mwfas/exact.py` | `see validate_environment.py output` | Committed, definitive |
| Objective evaluation | `src/mwfas/evaluation.py` | `see validate_environment.py output` | Committed, definitive |
| DIMACS parser | `src/mwfas/io.py` | `see validate_environment.py output` | Committed, definitive |

## 2. Supporting Scripts

| Role | Canonical File | Status |
|------|---------------|--------|
| EXP1b postprocessing | `experiments/exp1b_core_benchmark_full_wmsf_seed/postprocess_exp1b.py` | Committed |
| EXP4 postprocessing | `experiments/exp4_external_baselines/postprocess_exp4_external.py` | Committed |
| EXP4 runner | `experiments/exp4_external_baselines/run_exp4_benchmark.py` | Committed |
| EXP10 IPSNS runner | `experiments/exp10_stochastic_robustness/scripts/run_ipsns_repetitions.py` | Untracked |
| EXP10 DRMacIver runner | `experiments/exp10_stochastic_robustness/scripts/run_drmaciver_repetitions.py` | Untracked |
| EXP10 postprocessor | `experiments/exp10_stochastic_robustness/scripts/postprocess.py` | Untracked |
| EXP10 validator | `experiments/exp10_stochastic_robustness/scripts/validate_environment.py` | Untracked |
| DRMacIver FAS binary | `experiments/exp4_external_baselines/external_tools/Feedback-Arc-Set/fas` | Committed binary (commit 16ff24a) |

## 3. Benchmark Manifests

| Role | Canonical File | Status |
|------|---------------|--------|
| EXP4 instance paths | Derived from `benchmark_sources/` in scripts | Machine-local |
| EXP10 93-instance list | `experiments/exp10_stochastic_robustness/config/common_93_instances.txt` | Untracked; contains absolute paths |
| EXP10 25-instance diagnostic | `experiments/exp10_stochastic_robustness/config/diagnostic_subset.txt` | Untracked |
| EXP10 seed schedule | `experiments/exp10_stochastic_robustness/config/seed_schedule.txt` | Untracked |

## 4. Result Summaries (Manuscript Sources)

| Role | Canonical File | Status |
|------|---------------|--------|
| EXP1b raw results | `experiments/exp1b_core_benchmark_full_wmsf_seed/summary/exp1b_raw_summary.csv` | Committed |
| EXP4 raw results | `experiments/exp4_external_baselines/summary/exp4_raw_summary.csv` | Committed |
| EXP4 stats JSON | `experiments/exp4_external_baselines/summary/exp4_external_stats.json` | Committed |
| EXP3 report | `experiments/exp3_exact_small/summary/exp3_exact_report.md` | Committed |
| EXP8 report | `experiments/exp8_medium_mip_baseline/summary/exp8_final_report.md` | Committed |
| Combined digest | `experiments/combined/summary/manuscript_results_digest.md` | Committed |

## 5. Manuscript Files

| Role | Canonical File | Status |
|------|---------------|--------|
| Main document | `paper_coap/main.tex` | Committed |
| Introduction | `paper_coap/sections/01_introduction.tex` | Committed |
| Related work | `paper_coap/sections/02_related_work.tex` | Committed |
| Problem definition | `paper_coap/sections/03_problem_definition.tex` | Committed |
| Algorithmic framework | `paper_coap/sections/04_algorithmic_framework.tex` | Committed |
| Formal analysis | `paper_coap/sections/04_formal_analysis.tex` | Committed |
| Experimental design | `paper_coap/sections/05_experimental_design.tex` | Committed |
| Results | `paper_coap/sections/06_results.tex` | Committed |
| Discussion | `paper_coap/sections/07_discussion.tex` | Committed |
| Conclusion | `paper_coap/sections/08_conclusion.tex` | Committed |
| Declarations | `paper_coap/declarations/statements_and_declarations.tex` | Committed |
| Tables | `paper_coap/tables/*.tex` (14 files) | Committed |
| Figures | `paper_coap/figures/*.pdf` (4 PDFs + TikZ source) | Committed |

## 6. Stale / Duplicate Files

| File | Type | Versus canonical | Risk |
|------|------|-----------------|------|
| `submission_package/ejco_source/src/mwfas/ipsns.py` | Stale copy | Predates EXP10 instrumentation (no `_n_accepted` etc.) | **High** — if submitted as artifact, wrong version |
| `submission_package/ejco_source/src/mwfas/lrta.py` | Potentially stale | SHA not verified; EJCO era | **High** — may predate COAP changes |
| `submission_package/ejco_reproducibility_artifact/` | Stale package | EJCO-targeted artifact | **High** — should not be submitted to COAP |
| `submission_package/ejco_source.zip` | Stale archive | EJCO era | **High** — should be rebuilt for COAP |
| `submission_package/main.pdf` | Stale PDF | EJCO manuscript | **High** — should be replaced with COAP pdf |

**Critical action required:** The entire `submission_package/` directory is EJCO-era and must be rebuilt for COAP before submission. Do not submit `ejco_source.zip` or `ejco_reproducibility_artifact.zip` to COAP.

## 7. Canonical Source Summary

The definitive source of truth for all algorithms is `src/mwfas/`. No other copy should be submitted or referenced. The submission package must be rebuilt from current `src/mwfas/` state (including committed EXP10 instrumentation in `ipsns.py`).
