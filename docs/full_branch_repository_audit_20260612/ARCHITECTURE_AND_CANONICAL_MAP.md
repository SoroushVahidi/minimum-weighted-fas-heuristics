# Repository Architecture and Canonical Source Map

**HEAD:** `6c04ff1cc19d1887bd5b1b2bd1d1f31dc2b6924a`  
**Audit date:** 2026-06-12

## Actual architecture (as implemented)

```
minimum-weighted-fas-heuristics/
├── src/mwfas/              ← canonical algorithms (editable install)
├── scripts/                ← CLI runners (run_lrta, run_ipsns, …)
├── tests/                  ← full-repo pytest (91 collected)
├── configs/                ← benchmark instance lists
├── experiments/            ← EXP1–EXP11 + COAP sensitivity/holdout
├── paper_coap/             ← COAP manuscript (sn-jnl)
├── online_resource_1/      ← OR1 source + packaged mirror of code/tests/results
├── paper_coap/submission/  ← portal PDFs/ZIPs
├── Vahidi_Online_Resource_1_MWFAS.{pdf,zip}  ← root mirrors for convenience
├── submission_package/     ← historical EJCO era (stale for COAP)
├── paper/                  ← legacy manuscript tree (pre-COAP)
└── docs/                   ← audit corpus (12+ dated directories)
```

**Data flow:** DIMACS instances (external) → `io.read_graph_dimacs_agg` → algorithm modules → ranking CSV → `evaluation.compute_forward_backward` → experiment summaries (committed JSON/MD) → LaTeX tables → `paper_coap/main.pdf` and OR1.

## Canonical source map

| Concern | Canonical path | Duplicate / historical paths | Status | Notes |
|---|---|---|---|---|
| **LR-TA** | `src/mwfas/lrta.py` | `online_resource_1/src/mwfas/lrta.py`; `submission_package/ejco_reproducibility_artifact/src/mwfas/lrta.py` | Canonical + OR1 mirror; EJCO stale | Phase I/II cycle peel + add-back |
| **WMSF** | `src/mwfas/wmsf.py` | OR1 mirror; EJCO artifact | Same | SCC pipeline; L1/L2 ordering |
| **IPSNS** | `src/mwfas/ipsns.py` | OR1 mirror; EJCO artifact | Same | Destroy-and-repair + seeds |
| **Topological extraction** | `src/mwfas/topo_extraction.py` | OR1 mirror | Same | EXP11 rules; Kahn variants |
| **Exact DP** | `src/mwfas/exact.py` | OR1 mirror | Same | Bitmask DP, n≤20 |
| **Objective evaluation** | `src/mwfas/evaluation.py` | OR1 mirror | Same | Forward/backward weight |
| **DIMACS I/O** | `src/mwfas/io.py` | OR1 mirror | Same | Parallel-arc aggregation |
| **Baselines** | `src/mwfas/baselines.py` | OR1 mirror | Same | Borda, Eades, random, igraph wrapper |
| **CLI entry points** | `scripts/run_*.py` | `online_resource_1/scripts/run_*.py` | Canonical + OR1 | OR1 subset for reproduction |
| **Tests** | `tests/` | `online_resource_1/tests/` | Full repo 91; OR1 86 collected | OR1 omits live EXP10 infra tests |
| **EXP1 (legacy)** | `experiments/exp1_core_benchmark/` | — | **Superseded** | Legacy WMSF seed; do not cite |
| **EXP1b (main internal)** | `experiments/exp1b_core_benchmark_full_wmsf_seed/` | — | **Canonical** | 105-instance incumbent check |
| **EXP2–EXP9** | `experiments/exp{N}_*/summary/` | — | Canonical summaries | Raw gitignored |
| **EXP10** | `experiments/exp10_stochastic_robustness/summary/` | checkpoints/raw local | Complete | 1860+1860; raw not in git |
| **EXP11** | `experiments/exp11_topological_extraction_sensitivity/summary/exp11_aggregate.json` | — | Canonical | 6-instance calibration |
| **COAP sensitivity** | `experiments/coap_ipsns_sensitivity/summary/` | — | Complete | OAT screening |
| **COAP holdout** | `experiments/coap_ipsns_holdout/checkpoints/` | — | **Partial** | Checkpoints; no summary/ |
| **Manuscript** | `paper_coap/main.tex` + `sections/` | `paper/` (legacy) | COAP canonical | 45 pages |
| **Manuscript PDF (submit)** | `paper_coap/submission/final_upload/Vahidi_COAP_Manuscript.pdf` | `paper_coap/main.pdf` | Should match | SHA `97eb6123…` |
| **Online Resource** | `online_resource_1/` + root ZIP/PDF | EJCO reproducibility ZIP | OR1 canonical | 12 pages; 216 ZIP entries |
| **Cover letter** | `paper_coap/submission/cover_letter.tex` → final PDF | — | Canonical | |
| **Final upload bundle** | `paper_coap/submission/final_upload/` | Root OR1 copies | Canonical portal set | 6 files |

## Subsystems

| Subsystem | Role | Maturity |
|---|---|---|
| Production package (`src/mwfas`) | Algorithms | Frozen for submission |
| Experiment infrastructure | Batch runners, summaries | Mature; EXP10 namespace isolated |
| COAP manuscript | Publication source | Submission-ready at 6c04ff1 |
| Online Resource 1 | Supplementary reproducibility | Validated artifact gate passes |
| Submission package | Portal uploads | Current for COAP |
| `submission_package/` | EJCO historical | Stale; misleading if confused with COAP |
| Audit docs (`docs/*`) | Internal QA | Extensive; supersession chain documented below |

## Planned vs. actual gaps

| Planned / referenced | Actual state |
|---|---|
| Public GitHub during review | Repo **private**; OR1 is submission artifact |
| `experiments/combined/` digest | Exists; covers EXP1b–EXP5 only; predates EXP6–11 |
| Holdout committed summary | Checkpoints present; **no** `summary/` directory |
| EXP10 `status: FINAL` in progress JSON | Script hardcodes `NONFINAL`; `completed_ok: true` |
| EJCO `submission_package/` | Retained in repo; **not** COAP upload target |

## Maintainability assessment

**Understandable** for a single-author research codebase with clear separation: code → experiments → manuscript → OR1 → submission. **Risk areas:** (1) three copies of `src/mwfas` (repo, OR1, EJCO artifact); (2) large local-only EXP10 raw/checkpoint trees; (3) twelve `docs/*` audit directories without a single index (addressed in `DOCUMENTATION_AUDIT.md`).
