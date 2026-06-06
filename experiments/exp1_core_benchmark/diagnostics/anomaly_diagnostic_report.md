# EXP1 Anomaly Diagnostic Report

**Date:** 2026-06-06  
**Branch:** main  
**Affected instances:** `gr10`, `gr00`, `gr7`

---

## Instance Paths

| Instance | Path |
|----------|------|
| `gr00` | `/home/soroush/benchmark_sources/graph-benchmarks/core/gr00.d` |
| `gr7`  | `/home/soroush/benchmark_sources/graph-benchmarks/core/gr7.d` |
| `gr10` | `/home/soroush/benchmark_sources/graph-benchmarks/core/gr10.d` |

---

## 1. `gr10` — Apparent Incumbent-Protection Violation

### Symptom
EXP1 stats reported `incumbent_protection_violations = 1` for `gr10`:
- IPSNS final bw = **58,839**
- Standalone WMSF bw = **58,481** (used as `best_seed_bw` in stats)

### Diagnosis: comparison mismatch, NOT a true violation

The EXP1 stats compared IPSNS final against the **standalone** WMSF result, but the
incumbent protection guarantee only applies to the **internal seeds** computed inside
`lns_merge_wmsf_lr_best_incumbent`.

Diagnostic run revealed the actual internal seed values:

| Seed | Internal BW |
|------|-------------|
| IPSNS internal WMSF seed (L2-only, global, no stabilize) | **58,839** |
| IPSNS internal LR-TA seed | **62,435** |
| Best internal incumbent selected | **58,839** (WMSF) |
| IPSNS final (after 400 LNS iterations, no improvement found) | **58,839** |

The LNS did not improve the incumbent at any of 400 iterations.
Final output == best internal seed → **0 true violations**.

### Why standalone WMSF is stronger (58,481 < 58,839)

The standalone WMSF (`wmsf_ranking_from_dimacs_fast`) uses a more powerful algorithm:
1. **Runs both L1 and L2 orderings** and keeps the better result.
2. Applies the full per-SCC pipeline: `removeArcs → Minimize → Stabilize → Minimize`.

The IPSNS internal WMSF seed (`wmsf_seed_solution` in `ipsns.py`) uses only:
1. **L2 ordering only** (passed as `seed_ordering="L2"`).
2. `wmsf_removeArcs_global + wmsf_minimize_global` — no stabilize step, global (not per-SCC).

For `gr10` (47 nodes, 83 edges, 13 SCCs) the WMSF L1 ordering gives bw=58,708
and L2 gives bw=58,481 (the standalone picks L2). But the internal seed's simplified
global variant with L2 gives bw=58,839, worse than the standalone L2. This is a known
algorithmic difference between the two implementations.

### Code locations
- Standalone WMSF: `src/mwfas/wmsf.py` — `wmsf_ranking_from_dimacs_fast()`
- IPSNS internal WMSF seed: `src/mwfas/ipsns.py` — `wmsf_seed_solution()` (calls
  `wmsf_removeArcs_global` + `wmsf_minimize_global`, no stabilize, no L1 fallback)

### Correction to EXP1 stats
- `incumbent_protection_violations` (vs standalone) remains **1** (correct as a
  comparison statistic between IPSNS final and standalone WMSF).
- `true_incumbent_violations_vs_internal_seeds` = **0** (the algorithm guarantee holds).

---

## 2. `gr00` and `gr7` — IPSNS Float Division by Zero

### Symptom
EXP1 raw summary recorded `error = "float division by zero"` for both instances,
with all IPSNS numeric fields set to NaN and `output_csv = None`.

### Root cause: reporting bug in `ipsns.py`, line 787

Both `gr00` and `gr7` are **empty graphs** (n=0, m=0, total_weight=0.0).  
All three algorithms correctly return bw=0, fw=0 for empty graphs.

The IPSNS function crashed at:
```python
# src/mwfas/ipsns.py, line 787 (original)
print(f"Forward Ratio: {fw/total_w:.6f}")   # ZeroDivisionError when total_w == 0
```

This line always executes (it is NOT inside any `if log_every:` guard).
The crash happened **after** the ranking CSV was written (line 776) but **before**
the function returned, so `reproduce_all.py` caught the exception and stored
`output_csv=None, error="float division by zero"`.

The ranking CSVs on disk contain only the header row (no nodes to list), which is
correct for empty graphs.

### Algorithm failure? No.
The IPSNS algorithm itself ran correctly and completed in ~0.001s.
The LNS loop exited immediately at iteration 1 (no non-trivial SCCs).
bw=0, fw=0 is the mathematically correct answer for an empty graph.

### Fix applied
`src/mwfas/ipsns.py`, line 787 — guard the division:
```python
# Before (crashes for empty graphs):
print(f"Forward Ratio: {fw/total_w:.6f}")

# After:
print(f"Forward Ratio: {fw/total_w:.6f}" if total_w > tol else "Forward Ratio: 0.000000 (empty graph)")
```

The `tol` variable is already in scope at this point (defined as a parameter).

### Verification
After the fix:
- `gr00` IPSNS: bw=0.0, fw=0.0, n=0, m=0 — **SUCCESS**
- `gr7`  IPSNS: bw=0.0, fw=0.0, n=0, m=0 — **SUCCESS**

EXP1 raw summary rows corrected to reflect the true values (bw=0 for all three
algorithms), and no error entries remain.

---

## Summary of Changes

### Code changes
| File | Line | Change |
|------|------|--------|
| `src/mwfas/ipsns.py` | 787 | Guard `fw/total_w` division for empty graphs |

### Data corrections
| File | Change |
|------|--------|
| `experiments/exp1_core_benchmark/summary/exp1_raw_summary.csv` | gr00, gr7 IPSNS rows: NaN → correct zero values |
| `experiments/exp1_core_benchmark/summary/exp1_core_benchmark_stats.json` | `n_ipsns_errors`: 2→0; `ipsns_below_standalone_min_violations`: 1 (was mislabeled as true violation); `true_incumbent_violations_vs_internal_seeds`: 0 added |
| `experiments/exp1_core_benchmark/tables/exp1_core_benchmark_paper_summary.csv` | Regenerated with corrected values |
| `experiments/exp1_core_benchmark/summary/exp1_core_benchmark_summary.md` | Regenerated |

### Corrected EXP1 key counts

| Metric | Value |
|--------|-------|
| Unique instances | 105 |
| IPSNS errors (after fix) | **0** |
| IPSNS improves over LR-TA | 16 / 105 |
| IPSNS improves over WMSF | 36 / 105 |
| True incumbent violations (vs internal seeds) | **0** |
| IPSNS below standalone-min violations | 1 (`gr10`, algorithmic mismatch only) |

---

## Diagnostic files

```
experiments/exp1_core_benchmark/diagnostics/
  gr10/gr10_diagnostic_raw.txt   — internal seed bw vs standalone WMSF comparison
  gr10/gr10_rerun.txt            — verbose IPSNS rerun confirming 0 LNS improvement
  gr10/gr10_ipsns_ranking.csv    — IPSNS output (47 nodes ranked)
  gr00/gr00_diagnostic_raw.txt   — crash reproduction and graph inspection
  gr00/gr00_rerun.txt            — successful rerun after fix
  gr00/gr00_ipsns_ranking.csv    — IPSNS output (empty, header only)
  gr7/gr7_rerun.txt              — successful rerun after fix
  gr7/gr7_ipsns_ranking.csv      — IPSNS output (empty, header only)
  anomaly_diagnostic_report.md   — this file
```
