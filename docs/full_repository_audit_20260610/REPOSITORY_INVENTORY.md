# Repository Inventory

**Audit date:** 2026-06-10  
**Machine-readable inventory:** `inventory.json`

## Top-level directory classification

| Directory | Files (approx) | Tracked | Classification |
|---|---:|---:|---|
| `src/` | 8 Python modules | Yes | **Canonical production source** |
| `scripts/` | ~20 drivers | Yes | **Canonical production scripts / experiment drivers** |
| `configs/` | YAML + instance lists | Yes | **Configuration defaults** (paths are machine-specific) |
| `experiments/` | 7000+ (many untracked raw) | Partial | **Active + archived experiments** |
| `paper_coap/` | TeX, PDF, figures, notes | Yes | **Active COAP manuscript** |
| `paper/` | EJCO/CAIE TeX tree | Yes | **Old Elsevier/EJCO submission material** |
| `submission_package/` | EJCO zips, artifact | Yes | **EJCO submission package (stale for COAP)** |
| `submission_files_for_download/` | Anonymized PDFs | Yes | **Historical download bundle** |
| `notebooks/` | 2 predecessor notebooks | Yes | **Historical notebook/prototype** |
| `archive/` | Predecessor ZIPs | Yes | **Archived historical material** |
| `docs/` | Prior audits, provenance | Yes | **Documentation** (+ this audit) |
| `logs/` | Sensitivity + holdout logs | Mostly ignored | **Temporary/log material** |
| `results/` | Gitignored | No | **Generated output** |
| `.pytest_cache/` | Cache | Ignored | **Local tool artifact** |

## `src/mwfas/` (canonical)

| Module | Role |
|---|---|
| `lrta.py` | LR-TA: local-ratio reduction + topological add-back |
| `wmsf.py` | WMSF per-SCC pipeline |
| `ipsns.py` | IPSNS incumbent-protected SCC LNS |
| `evaluation.py` | Forward/backward weight objective |
| `io.py` | DIMACS read + parallel-edge aggregation |
| `exact.py` | Bitmask DP exact solver (n≤20) |
| `baselines.py` | Borda, weighted Eades, random multistart |

## `scripts/` (canonical entry points)

| Script | Purpose |
|---|---|
| `run_lrta.py`, `run_wmsf.py`, `run_ipsns.py`, `run_exact.py` | Method CLIs |
| `reproduce_all.py` | Batch benchmark runner |
| `run_coap_ipsns_sensitivity.py` | Stage-1 sensitivity (complete) |
| `postprocess_coap_ipsns_sensitivity.py` | Stage-1 analysis |
| `select_coap_ipsns_holdout_instances.py` | Stage-2 instance selection |
| `run_coap_ipsns_holdout.py` | Stage-2 holdout (**running**) |
| `run_drmaciver_fas.py`, `run_igraph_eades.py` | External baseline wrappers |

## `experiments/` inventory

| Directory | Status | Manuscript |
|---|---|---|
| `exp1b_core_benchmark_full_wmsf_seed/` | Complete | Primary sparse benchmark |
| `exp1_core_benchmark/` | **Obsolete** | Superseded by EXP1b |
| `exp2_ablation/` | Complete | Ablation table |
| `exp3_exact_small/` | Complete | Exact validation |
| `exp4_external_baselines/` | Complete | External comparison |
| `exp5_lolib_dense/` | Complete | Dense transfer |
| `exp6_ipsns_budget_curve/` | Complete | Budget curve |
| `exp7_plain_local_search/` | Complete (no raw archive) | Plain LS comparison |
| `exp8_medium_mip_baseline/` | Complete | HiGHS MIP |
| `exp9_application_case/` | Complete | Application case |
| `coap_ipsns_sensitivity/` | Complete (preliminary) | Notes only |
| `coap_ipsns_holdout/` | **Running** | Notes only; untracked results |
| `combined/` | Complete | Digest for EXP1b–5 |
| `seedfix_full_wmsf/` | Diagnostic | Historical |

## Duplication map (hash-verified where noted)

| Pair | Relationship |
|---|---|
| `src/mwfas/*.py` vs `submission_package/ejco_reproducibility_artifact/src/mwfas/*.py` | **Synchronized** (SHA-256 match on all 7 core modules) |
| `paper_coap/` vs `paper/` | **Divergent** (COAP migrated from EJCO; formal analysis + COAP template only in `paper_coap/`) |
| `paper_coap/` vs `submission_package/ejco_source/` | **Stale EJCO copy** (no Section 4 formal analysis pass) |
| `notebooks/*` vs `src/mwfas/` | **Stale prototype** — do not execute for publication |
| `archive/predecessor_projects/` | **Frozen ZIP snapshots** |

## Git ignore impact on reproducibility

From `.gitignore`:
- `experiments/*/raw/` — raw per-run outputs **not in Git**
- `*.csv` broadly ignored with exceptions for summaries/tables/COAP configs
- `experiments/*/external_tools/` — DRMacIver clone not in Git
- LaTeX build artifacts ignored under `paper/` and `paper_coap/`

## Recent meaningful commits (last 20)

```
80b3144 Add sensitivity instance list omitted by csv gitignore
90af464 Add completed COAP IPSNS sensitivity experiment
92e9c5a Add formal correctness and complexity analysis for COAP
76a3412 Polish COAP template and manuscript layout
7e8e0b7 Create Springer COAP manuscript version
581ee35 Track final EJCO submission package
5e1fcc1 Finalize EJCO submission package
623f044 Prepare EJCO source and reproducibility packages
5c61925 Prepare EJCO title page and declarations
9bc756c Prepare EJCO cover letter and highlights
75fbc14 Replace AI-generated flowchart with TikZ figure
35bac85 Retarget manuscript framing for EJCO
b66cace Refresh anonymous reproducibility artifact
fd3c8f7 Add PDF highlights file
6934679 Replace Figure 1 with clean flowchart image
74fb082 Lightly polish manuscript tone
1baaddb Add files via upload
bc310a1 Refine Figure 1 restore-path routing
23964b6 Fix final figure layout issues
d496b8a Finalize CAIE submission package
```

## Largest tracked files (observed)

| Size (bytes) | Path |
|---:|---|
| 1,058,509 | `submission_files_for_download/main_anonymized.pdf` |
| 920,888 | `paper/figures/framework_overview_clean.png` |
| 901,814 | `paper_coap/template_reference/sn-jnl-official-dec2024.zip` |
| 296,609 | `paper_coap/main.pdf` |

## Largest untracked at audit time

| Area | Size |
|---|---|
| `experiments/coap_ipsns_holdout/` | ~18 MB (growing) |
| `experiments/exp4_external_baselines/raw/` (ignored) | ~168 MB local |
| Holdout log | ~215 KB |
