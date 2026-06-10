# COAP IPSNS Default Selection — Decision Record

**Date:** 2026-06-10  
**Stage-1 evidence:** `experiments/coap_ipsns_sensitivity/` (140/140 runs)  
**Manuscript baseline commit:** `92e9c5a`

## Decision

| Item | Status |
|---|---|
| **Sufficiency conclusion** | **B** — preliminary screening only |
| **Change implementation defaults now?** | **No** |
| **Change manuscript defaults now?** | **No** |
| **Stage-2 holdout experiment** | **Required — designed and launched** |

## What stage 1 established

1. On the EXP2 ten-instance subset, **iteration budget ≥100** matches the best observed backward weight among {100, 200, 400, 600} for every instance in the dedicated sweep.
2. **`topk_scc ∈ {5,10,20}`** does not change backward weight vs default 15 on this subset.
3. **`rng_seed ∈ {1,2,3}`** on the baseline configuration produces **identical** backward weights on all ten instances.
4. **Destroy fractions** produce at most **small, instance-specific** changes (chiefly `grid` / `r1000`); OAT cannot assess interactions.
5. **Tolerance** was not varied; no tolerance claim is supported.

## What stage 1 did not establish

- Generalization to the **97-instance** nonnegative sparse benchmark
- Behavior on **`r20_60`** and other structurally distinct cases
- **Multi-seed robustness** for non-baseline configurations
- **Interaction-safe** selection among destroy/top-K/budget parameters
- **Accepted-move / early-stop** statistics (not logged in stage 1)

## Recommended default (interim, not for implementation yet)

**Do not adopt a new global default from stage 1 alone.**

**Working hypothesis for stage 2** (to be confirmed on tuning/holdout splits):

| Parameter | Hypothesis |
|---|---|
| Iteration budget | Reduce from **400** toward **50–100** if holdout confirms saturation and incumbent safety |
| `topk_scc` | Retain **15** unless holdout shows consistent gains for alternatives |
| `destroy_addback_frac` | Retain **0.30**; optional confirm **0.25** on holdout |
| `destroy_remove_frac` | Retain **0.02** |
| Random seed | Fixed seed for reproducibility; report **5-seed** dispersion on holdout |

Legacy **400-iteration** default remains the manuscript reference until stage 2 completes.

## Stage-2 pre-registered design

**Directory:** `experiments/coap_ipsns_holdout/`  
**Driver:** `scripts/run_coap_ipsns_holdout.py`  
**Session:** `coap_ipsns_holdout`

| Split | Count | Selection |
|---|---:|---|
| Tuning | 18 | Stratified from 87 eligible instances (exclude EXP2 ten); see `config/tuning_instances.csv` |
| Holdout | 25 | Disjoint stratified set; **includes `r20_60`**; see `config/holdout_instances.csv` |

**Candidate configurations (6) × seeds (5) × instances (43) = 1290 runs**

| Config ID | iters | Other overrides |
|---|---:|---|
| `seed_only` | 0 | — |
| `iters_10` | 10 | — |
| `iters_50` | 50 | — |
| `iters_400` | 400 | legacy default |
| `iters_50_topk5` | 50 | topK=5 |
| `iters_50_addback25` | 50 | addback=0.25 |

**Post-hoc selection rules** (pre-registered in `holdout_plan.yaml`):

1. Primary metric on **tuning split:** median normalized improvement vs best seed (`return_info.best_seed_bw`).
2. **Zero incumbent violations** vs best seed on every tuning instance and seed.
3. Prefer **smallest iteration budget** among configs tied within 1e-9 absolute BW on ≥90% of tuning instances.
4. **Holdout split** used for confirmation only; finalists = top 3 tuning configs plus legacy `iters_400`.

## Manuscript policy (this pass)

- **No** default or prose changes until stage 2 validates.
- Stage 1 may be cited only as **EXP2-aligned screening**, not as universal tuning evidence.

## Next pass after stage 2 completes

1. Validate `logs/coap_ipsns_holdout/COMPLETED.ok`
2. Post-process holdout checkpoints (`return_info=True`)
3. Apply selection rules → final default recommendation
4. Update implementation defaults, manuscript parameter text, and runtime claims consistently
