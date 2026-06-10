# COAP IPSNS Parameter Sensitivity — Results

**Source artifacts:** `experiments/coap_ipsns_sensitivity/`  
**Canonical table:** `summary/canonical_runs.csv` (SHA-256 `e962f5cdc9adf2a7860115c5d3eab929221a8ab1db0bf25276b11f5da1c4a316`)  
**Analysis JSON:** `summary/analysis_summary.json`  
**Post-process script:** `scripts/postprocess_coap_ipsns_sensitivity.py`

## Validation summary

Independent matrix check (2026-06-10):

| Check | Result |
|---|---|
| Expected runs | 140 |
| Valid checkpoints | 140 |
| `runs.jsonl` lines | 140 (unique keys) |
| Failures | 0 |
| Manifest ↔ checkpoint consistency | exact match |

Fields **not recorded** in stage 1: `accepted_moves`, `attempted_moves`, `first_improvement_iteration`, `last_improvement_iteration` (driver used `return_info=False`).

---

## E. Iteration budget

Compared to **baseline_default** (400 iterations, default destroy/top-K) on each instance.

| Budget | Mean final BW | Median final BW | W/T/L vs baseline-400 | Mean runtime vs baseline |
|---:|---:|---:|---|---:|
| 100 | 4239.2 | 877.0 | 0 / 10 / 0 | ~0.16× |
| 200 | 4239.2 | 877.0 | 0 / 10 / 0 | ~0.32× |
| 400 (baseline) | 4239.2 | 877.0 | — | 1.00× |
| 600 | 4239.2 | 877.0 | 0 / 10 / 0 | ~1.16× |

### Per-instance budget behavior

- **Eight small instances (`bad*`, `bad`):** IPSNS never improves over best seed; all budgets tie baseline backward weight.
- **`grid`:** All tested budgets (100–600) match best observed BW **32954**; baseline row at 400 iterations is **32954** (EXP2 IPSNS-400 was 32954; sensitivity baseline checkpoint is consistent).
- **`r1000`:** Dedicated `iters` sweep rows (100, 200, 600) all yield **4055**, matching EXP2 IPSNS-400. Improvement over best seed (4375 → 4055) is achieved by **100 iterations**; larger budgets do not change BW on this instance.

### Smallest budget matching best observed BW (iteration sweep only)

| Instance | Min budget among {100,200,400,600} |
|---|---:|
| 9/10 small + grid | **100** |
| r1000 | **100** (ties at 200, 400, 600) |

**All 10 instances:** best iteration-sweep BW matched at **100** iterations (≥90% threshold satisfied at 100, not uniquely at 400).

### Improvement timing (inferred from EXP2 + stage-1)

| Window | Evidence on EXP2 subset |
|---|---|
| Before 10 | No separate 10-iter arm in stage 1; EXP6 on a different 20-instance subset shows gains by 10 iterations |
| 10–50 | EXP2: `r1000` reaches 4055 by **50** iterations |
| 50–100 | Stage-1: 100-iter arm ties 400-iter arm on all instances |
| After 100 | No BW gain on stage-1 subset; runtime grows ~linearly (`r1000`: 15s @100 → 47s @400 → 87s @600) |

**No instance** shows a **larger** budget beating the best observed BW in the dedicated `iters` sweep. Runtime continues to increase after quality saturates.

---

## F. Top-K (`topk_scc`)

| Value | W/T/L vs baseline (n=10 each) | Mean ΔBW | Runtime ratio vs baseline |
|---:|---|---:|---:|
| 5 | 0 / 10 / 0 | 0.0 | 0.80× |
| 10 | 0 / 10 / 0 | 0.0 | 0.80× |
| 20 | 0 / 10 / 0 | 0.0 | 0.80× |

**Conclusion:** No backward-weight effect on this subset; modest runtime reduction vs baseline (fewer/top-weighted pool operations).

---

## G. Destroy fractions

### Heavy reactivation (`destroy_addback_frac`)

| Value | W/T/L (n=10) | Mean ΔBW | Notes |
|---:|---|---:|---|
| 0.15 | 1 / 8 / 1 | −3.1 | One win, one loss on heavy instances |
| 0.25 | 1 / 8 / 1 | −7.3 | Best mean delta; still tie-dominated |
| 0.35 | 0 / 9 / 1 | +5.3 | One loss vs baseline |

Aggregate: **2 wins, 25 ties, 3 losses** across 30 comparisons. Effects are **small** and concentrated on **`grid` / `r1000`**; several “losses” are +3 BW (`grid`) or minor regressions, not incumbent violations vs **best seed**.

### Light removal (`destroy_remove_frac`)

| Value | W/T/L (n=10) | Mean ΔBW |
|---:|---|---:|
| 0.01 | 1 / 9 / 0 | −2.8 |
| 0.05 | 0 / 9 / 1 | +0.4 |

**Conclusion:** Weak, instance-specific effects; OAT cannot rule out interaction with budget or top-K.

---

## H. Tolerance

**Not tested.** All 140 runs used `tol = 1e-12`.

Benchmark weights are **integer-valued** in these instances; deactivation follows floating-point comparisons in code, but no alternate tolerance arm was executed. **No claim** about tolerance robustness is supported beyond noting inactivity of varying tolerance in this study.

---

## I. Random seed replication

| Scope | Seeds used | Result |
|---|---|---|
| Baseline config only | 1, 2, 3 | **20/20 ties** vs seed-1 baseline BW; mean BW identical (4239.2) |
| All other configs | 1 only | **No replication** |

**Honest assessment:** Stage 1 is **not** a stochastic-robustness study except for a three-seed check on the baseline configuration, which showed **zero variability** on this subset.

---

## J. Representativeness assessment

| Question | Assessment |
|---|---|
| Representative of 97-instance benchmark? | **No** — 10/97 instances, skewed to EXP2 ablation mix |
| Enough improving instances? | **No** — only `grid` and `r1000` show seed improvements in EXP2 |
| Large/slow cases included? | **Partially** — `r1000` and `grid` yes; missing `rd_big`, ISCAS-large, etc. |
| Independent of ablation subset? | **No** — identical 10 instances |
| OAT adequate with interactions? | **No** |
| Enough RNG replication? | **No** (except baseline ×3) |
| Justify changing global default? | **No** |
| Support robustness manuscript claim? | **No** |

---

## K. Sufficiency decision

**Conclusion B:** Sufficient **only as preliminary screening**; **broader holdout validation is required** before changing defaults or claiming parameter robustness.

Supporting facts:

- Quality saturates at **≤100 iterations** on all ten instances in the dedicated budget sweep.
- Top-K and RNG (baseline) show **no meaningful BW movement** on this subset.
- Destroy fractions show **tiny, tie-dominated** effects with plausible but **untested** interactions.
- Subset is **not independent** and **not representative** of the full benchmark.

**Not conclusion D:** Parameters do matter for runtime and can induce **small** BW changes on heavy instances; the refinement mechanism is not uniformly inactive.

---

## Stage-2 follow-up

See `experiments/coap_ipsns_holdout/config/holdout_plan.yaml` and `COAP_DEFAULT_SELECTION_DECISION.md`.
