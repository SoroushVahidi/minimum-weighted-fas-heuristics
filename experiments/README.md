# Experiments

This directory contains all experimental packages for the MWFAS paper.
Each experiment is self-contained with its own configs, logs, raw outputs, summary, and tables.

Raw outputs and logs are **gitignored** (regenerable). Summary CSVs/JSONs/MDs and paper tables are committed.

---

## Experiment Table

| Experiment | Purpose | Status | Summary path |
|---|---|---|---|
| **EXP1b** | Main benchmark with full WMSF seed | Complete | `exp1b_core_benchmark_full_wmsf_seed/summary/` |
| **EXP2** | Ablation study: 8 component variants | Complete | `exp2_ablation/summary/` |
| **EXP3** | Exact small-instance optimality check | Complete | `exp3_exact_small/summary/` |
| **EXP4** | External baseline comparison | Complete | `exp4_external_baselines/summary/` |
| **EXP5** | LOLIB dense benchmark | Planned | — |
| EXP1 | Legacy core benchmark (superseded) | Archived | `exp1_core_benchmark/summary/` |

---

## EXP1b — Main Benchmark (Definitive)

**Purpose:** Run LR-TA, WMSF, and IPSNS on the full 123-instance benchmark using the
full WMSF seed mode (`wmsf_seed_mode="full"`). This is the definitive benchmark for
the paper's main claims.

**Instance set:** 105 unique instances (123 listed, 18 duplicates removed)  
**Key result:** IPSNS ≥ LR-TA and IPSNS ≥ WMSF on all 105 instances (0 incumbent violations).
IPSNS improves over LR-TA on 16/105 instances (mean 0.71%); over WMSF on 36/105 (mean 2.06%).

**Outputs (committed):**
- `summary/exp1b_raw_summary.csv` — per-instance raw results
- `summary/exp1b_core_benchmark_stats.json` — aggregate statistics
- `summary/exp1b_core_benchmark_summary.md` — narrative summary
- `tables/exp1b_core_benchmark_paper_summary.csv` — paper-ready table
- `tables/exp1b_core_benchmark_wide_summary.csv` — wide-format table

**Raw/logs:** Gitignored (`experiments/exp1b_core_benchmark_full_wmsf_seed/logs/`, `raw/`)

---

## EXP2 — Ablation Study

**Purpose:** Measure the contribution of each component: add-back phase (LR-TA Phase 2),
WMSF seed quality, and LNS iterations. Run on 10 representative instances.

**Variants:** `lr_no_addback`, `lrta_full`, `wmsf_seed`, `best_seed_no_lns`,
`ipsns_no_scc_priority`, `ipsns_50iters`, `ipsns_100iters`, `ipsns_full`

**Key result:** Add-back reduces mean BW by ~5.9% (`lr_no_addback` → `lrta_full`).
Full LNS (IPSNS) further reduces by ~0.8%.

**Outputs (committed):**
- `summary/exp2_ablation_stats.json`
- `tables/exp2_ablation_summary.csv`

---

## EXP3 — Exact Small-Instance Optimality Check

**Purpose:** Verify near-optimality of LR-TA, WMSF, and IPSNS against exact bitmask DP
solutions on all instances with n ≤ 20 nodes.

**Instance set:** 57 standard (non-negative-weight) instances, n ≤ 20

**Key result:** IPSNS achieves exact optimality on **56/57 (98.2%)** standard instances.
Only near-miss: `r20_60` (n=20, 0.03% gap). LR-TA: 55/57 (96.5%). WMSF: 51/57 (89.5%).

**Outputs (committed):**
- `summary/exp3_exact_report.md`
- `summary/exp3_exact_stats.json`
- `tables/exp3_exact_summary.csv`

---

## EXP4 — External Baseline Comparison

**Purpose:** Compare IPSNS against publicly available FAS algorithms to demonstrate
the quality advantage of the LR-TA + WMSF + IPSNS framework.

**Algorithms:** ipsns_full, lrta_full, wmsf_seed (ours) vs. borda_net_score,
weighted_eades, random_multistart, igraph_approx_eades, drmaciver_fas (baselines)

**Instance set:** 97 standard non-negative-weight instances (105 unique, 8 negative-weight excluded)

**Key result:** IPSNS achieves the global minimum BW on **96/97 standard instances**.
Closest external competitor: DRMaciver (mean BW 53,173 vs IPSNS 37,698; +21.6%).
Only loss: `r20_60`, DRMaciver wins by 3 units (0.18%) — same instance as EXP3's near-miss.

**Known errors (expected):**
- `drmaciver_fas`: 2 empty-tournament failures on `gr00`, `gr7` (DAG instances);
  2 timeouts on `s38417`, `s38584` (n > 30K)
- `weighted_eades`: fails on negative-weight instances (all excluded from standard set)

**Outputs (committed):**
- `summary/exp4_raw_summary.csv` — all 984 rows (before deduplication)
- `summary/exp4_external_stats.json`
- `summary/exp4_external_summary.md`
- `summary/exp4_external_report.md` — full narrative report
- `summary/external_access_report.md` — which external tools were available
- `tables/exp4_external_paper_summary.csv`
- `tables/exp4_external_wide_summary.csv`

**Raw/logs:** Gitignored (`experiments/exp4_external_baselines/logs/`, `raw/`,
`external_tools/`)

---

## EXP5 — LOLIB Dense Benchmark (Planned)

**Purpose:** Evaluate LR-TA, WMSF, and IPSNS on dense tournament graphs from the
LOLIB benchmark set. LOLIB instances are denser than the alidasdan graph-benchmarks
set and test scalability on difficult dense instances.

**Status:** Not yet started. Next cloud task after this cleanup pass.

---

## EXP1 — Legacy Core Benchmark (Superseded)

**Purpose:** Initial run of LR-TA, WMSF, and IPSNS using the old (legacy) WMSF seed mode.
Superseded by EXP1b which uses the corrected full WMSF seed.

**Do not cite EXP1 in the paper.** The 1 incumbent violation in EXP1 was an artifact
of the legacy seed mismatch, resolved in EXP1b (0 violations).

**Preserved for:** historical completeness and to document the seed fix.
See `experiments/seedfix_full_wmsf/seedfix_report.md` for the diagnostic.
