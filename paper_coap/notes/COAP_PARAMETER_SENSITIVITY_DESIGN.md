# COAP IPSNS Parameter Sensitivity — Experimental Design

**Stage:** 1 (screening)  
**Status:** Complete (140/140 runs)  
**Driver:** `scripts/run_coap_ipsns_sensitivity.py`  
**Plan:** `experiments/coap_ipsns_sensitivity/config/sensitivity_plan.yaml`

## Purpose

Provide implementation-faithful evidence on IPSNS parameter sensitivity around the manuscript defaults, without claiming universal optimality or holdout-validated default selection.

## Design type

This is a **one-at-a-time (OAT) screening design** on the **EXP2 ablation subset** (10 instances). It is **not** an independent holdout validation, **not** a full factorial grid, and **not** a stochastic-robustness study for most parameters.

## Instance selection (10)

| Instance | Family | n | m | Density | EXP2 best-seed BW | EXP2 IPSNS-400 BW | IPSNS gain vs seed |
|---|---|---:|---:|---:|---:|---:|---:|
| bad1 | core-bad | 13 | 14 | 0.090 | 94 | 94 | 0 |
| bad2 | core-bad | 11 | 12 | 0.167 | 180 | 180 | 0 |
| bad3 | core-bad | 19 | 21 | 0.061 | 1519 | 1519 | 0 |
| bad4 | core-bad | 19 | 21 | 0.061 | 877 | 877 | 0 |
| bad5 | core-bad | 19 | 21 | 0.061 | 770 | 770 | 0 |
| bad6 | core-bad | 19 | 21 | 0.061 | 218 | 218 | 0 |
| bad7 | core-bad | 19 | 21 | 0.061 | 1724 | 1724 | 0 |
| bad | core | 10 | 10 | 0.167 | 1 | 1 | 0 |
| grid | core-big | 1001 | 3000 | 0.003 | 32957 | 32954 | 3 |
| r1000 | core-big | 999 | 3960 | 0.004 | 4375 | 4055 | 320 |

**Why these instances?** They are exactly the EXP2 ablation set used elsewhere in the manuscript for component and iteration ablations. They span small “core-bad” cases, one medium cyclic core case, and two large sparse benchmarks where IPSNS can improve (`grid`, `r1000`).

**Coverage gaps relative to the 97-instance standard benchmark:** no medium industrial ISCAS cases, no `r20_60` near-miss, no negative-weight instances (deliberately excluded), and only **2/10** instances show IPSNS improvement over the best seed in EXP2.

## Baseline (default) configuration

| Parameter | Value |
|---|---|
| Iteration budget `iters` | 400 |
| Top-K SCC pool `topk_scc` | 15 |
| Heavy reactivation fraction | 0.30 |
| Light removal fraction | 0.02 |
| Tolerance `tol` | 1e-12 |
| Random seed `rng_seed` | 1 |
| WMSF seed mode | `full` |
| Seed ordering | L2 |
| SCC selection | weighted top-K |

## Fourteen configurations per instance

One **baseline** row plus thirteen OAT variants (only one parameter differs from baseline per variant):

| # | `varied_param` | Setting | Notes |
|---|---|---|---|
| 1 | baseline | all defaults | Reference for comparisons |
| 2–4 | `iters` | 100, 200, 600 | Budget sweep |
| 5–7 | `topk_scc` | 5, 10, 20 | SCC pool size |
| 8–10 | `destroy_addback_frac` | 0.15, 0.25, 0.35 | Heavy-first reactivation |
| 11–12 | `destroy_remove_frac` | 0.01, 0.05 | Light-first removal |
| 13–14 | `rng_seed` | 2, 3 | **Only** on baseline config |

**Total runs:** 10 × 14 = **140**.

## Random seeds and replication

- **12/14 configuration types** use `rng_seed = 1` only.
- **Baseline only** is replicated across seeds 1, 2, and 3 (30 runs total for baseline across instances).
- This is **not** multi-seed replication for budget, top-K, or destroy-fraction sweeps.

## Omitted parameters (held fixed)

- Tolerance (always 1e-12; **not varied**)
- WMSF seed mode (`full`)
- Seed ordering (`L2`)
- SCC selection mode (`weighted`)
- Add-back / LR-TA tolerance branches
- Per-iteration trace logging (`return_info=False` in stage-1 driver)

## Comparison reference

Primary within-study reference: **baseline_default** (400 iterations, default destroy/top-K, seed 1) on the same instance.

Secondary external reference: EXP2 `best_seed_no_lns` backward weight (initial seed ceiling without refinement).

## Known limitations of this design

1. OAT cannot detect parameter **interactions** (e.g., budget × top-K).
2. Ten instances are **not structurally representative** of the full 97-instance nonnegative benchmark.
3. The subset overlaps the manuscript ablation set → **not independent** of prior reported ablation claims.
4. Most instances are **tie-dominated**; effects are concentrated on `grid` / `r1000`.
5. Stage-1 checkpoints do **not** record accepted-move traces or improvement iteration indices.

## Sufficiency expectation

This design is intended as **preliminary screening only**. Default selection or robustness claims require stage-2 tuning/holdout validation (see `COAP_DEFAULT_SELECTION_DECISION.md`).
