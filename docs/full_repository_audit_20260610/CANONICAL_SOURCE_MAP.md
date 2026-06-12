# Canonical Source Map

**Audit date:** 2026-06-10

## Authoritative sources of truth

| Concern | Canonical path | Notes |
|---|---|---|
| LR-TA implementation | `src/mwfas/lrta.py` | CLI: `scripts/run_lrta.py` |
| WMSF implementation | `src/mwfas/wmsf.py` | CLI: `scripts/run_wmsf.py` |
| IPSNS implementation | `src/mwfas/ipsns.py` | CLI: `scripts/run_ipsns.py`; entry `lns_merge_wmsf_lr_best_incumbent` |
| Objective evaluation | `src/mwfas/evaluation.py` | All arcs in aggregated graph, not active-edge filter |
| Graph I/O | `src/mwfas/io.py` | DIMACS `a u v w`; parallel edges summed |
| Configuration defaults | `configs/ipsns_default.yaml`, `configs/lrta_default.yaml`; CLI defaults in `scripts/run_ipsns.py` | COAP sensitivity uses YAML plans |
| Exact validation | `src/mwfas/exact.py` + `experiments/exp3_exact_small/` | n≤20 bitmask DP |
| MIP baseline | `scripts/run_exp8_medium_mip_baseline.py` + `experiments/exp8_medium_mip_baseline/` | HiGHS via scipy |
| Sparse benchmark (97 std) | External: `/home/soroush/benchmark_sources/graph-benchmarks/` (listed in `configs/benchmark_instances_found_all.txt`) | 8 negative-weight instances excluded |
| Core benchmark runs | `experiments/exp1b_core_benchmark_full_wmsf_seed/summary/` | 105 unique instances |
| External baselines | `experiments/exp4_external_baselines/` + wrappers in `scripts/` | Registry: `baseline_registry.md` |
| Dense LOLIB experiment | `experiments/exp5_lolib_dense/` + `converted/` | 50 instances in-repo |
| Parameter sensitivity (stage 1) | `experiments/coap_ipsns_sensitivity/summary/canonical_runs.csv` | 140 runs complete |
| Holdout (stage 2) | `experiments/coap_ipsns_holdout/config/holdout_plan.yaml` | **Running**; results untracked |
| COAP manuscript | `paper_coap/main.tex` + `sections/` | PDF: `paper_coap/main.pdf` |
| Bibliography | `paper_coap/references.bib` | Numbered via `sn-mathphys-num` |
| Figures/tables | `paper_coap/figures/`, `paper_coap/tables/` | PDF figures present for EXP4–6 |
| Reproducibility artifact | `submission_package/ejco_reproducibility_artifact/` | **EJCO-branded; not COAP ESM** |
| Submission package | `submission_package/` | **EJCO only** — no COAP upload bundle |

## Default parameter authority (IPSNS)

| Parameter | Code default | Manuscript reference | Evidence status |
|---|---:|---|---|
| `iters` | 400 | Ablation + budget curve | Holdout pending |
| `topk_scc` | 15 | Ablation | Stage-1: no effect on 10 instances |
| `destroy_addback_frac` | 0.30 | Ablation | Stage-1: tiny effects; holdout pending |
| `destroy_remove_frac` | 0.02 | Ablation | Not varied in stage 1 |
| `rng_seed` | 1 | Reproducibility | Stage-1 baseline: invariant across seeds 1–3 |
| `tol` | 1e-12 | Formal analysis | Not sensitivity-tested |
| `wmsf_seed_mode` | `full` | Algorithm section | Matches standalone WMSF |

**Policy:** Do not change defaults until holdout post-processing (`COAP_DEFAULT_SELECTION_DECISION.md`).

## Duplicate / stale copies

| Copy | Status | Risk |
|---|---|---|
| `submission_package/ejco_reproducibility_artifact/src/` | Synchronized with live `src/` | Low if used as frozen artifact |
| `submission_package/ejco_source/` | Stale vs `paper_coap/` (no formal analysis) | **Medium** — wrong manuscript for COAP |
| `paper/` | CAIE/EJCO lineage | **Medium** — wrong venue/template |
| `notebooks/local_ratio_original/`, `notebooks/ipsns_original/` | Historical | **High if run** — paths and APIs obsolete |
| `archive/predecessor_projects/*.zip` | Frozen | Low |
| `submission_files_for_download/` | Old anonymized PDFs | **Medium** — may not match COAP PDF |

## Experiment launch provenance

| Experiment | Launch commit | Clean tree |
|---|---|---|
| COAP sensitivity | `90af464` (per `logs/coap_ipsns_sensitivity/LAUNCH_METADATA.md`) | Yes |
| COAP holdout | `90af464` (per `logs/coap_ipsns_holdout/LAUNCH_METADATA.md`) | Yes |
| Manuscript formal analysis | `92e9c5a` | Committed |

Holdout code frozen at `90af464`; HEAD is `80b3144` (instance CSV gitignore fix only).
