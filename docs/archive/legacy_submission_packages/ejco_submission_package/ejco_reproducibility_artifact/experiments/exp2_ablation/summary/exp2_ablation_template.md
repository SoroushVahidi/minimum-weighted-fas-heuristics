# EXP2 Ablation Study — Results Template

> **Fill in after running `run_exp2_ablation_tmux.sh`.**
> This template will be replaced by the auto-generated summary when the script completes.

## Run metadata

| Field | Value |
|---|---|
| Git commit | _(fill)_ |
| Date | _(fill)_ |
| Machine | _(fill)_ |
| Python | _(fill)_ |
| Instance count | 10 |
| Instance list | `experiments/exp2_ablation/configs/exp2_ablation_instances.txt` |

## Per-variant backward weight (lower is better)

| Instance | lr_no_addback | lrta_full | wmsf_seed | best_seed_no_lns | ipsns_no_scc_priority | ipsns_50iters | ipsns_100iters | ipsns_full |
|---|---|---|---|---|---|---|---|---|
| bad1 | TODO | | | | TODO | | | |
| bad2 | TODO | | | | TODO | | | |
| bad3 | TODO | | | | TODO | | | |
| bad4 | TODO | | | | TODO | | | |
| bad5 | TODO | | | | TODO | | | |
| bad6 | TODO | | | | TODO | | | |
| bad7 | TODO | | | | TODO | | | |
| bad | TODO | | | | TODO | | | |
| grid | TODO | | | | TODO | | | |
| r1000 | TODO | | | | TODO | | | |

## Aggregate statistics

| Variant | Mean BW | Median BW | Mean Runtime (s) | Improves over LR-TA | Improves over WMSF |
|---|---|---|---|---|---|
| lr_no_addback | TODO | TODO | TODO | — | — |
| lrta_full | | | | — | — |
| wmsf_seed | | | | — | — |
| best_seed_no_lns | | | | — | — |
| ipsns_no_scc_priority | TODO | TODO | TODO | | |
| ipsns_50iters | | | | | |
| ipsns_100iters | | | | | |
| ipsns_full | | | | | |

## Incumbent protection check

IPSNS variants must satisfy `BW(ipsns_variant) <= min(BW(lrta_full), BW(wmsf_seed))`.

| Variant | Violations |
|---|---|
| ipsns_no_scc_priority | TODO |
| ipsns_50iters | _(fill)_ |
| ipsns_100iters | _(fill)_ |
| ipsns_full | _(fill)_ |

## Key findings

_(Fill after reviewing results.)_

- Add-back contribution (lrta_full vs. lr_no_addback): 
- WMSF vs. LR-TA on this subset:
- Best seed vs. full IPSNS gap:
- SCC priority contribution (ipsns_full vs. ipsns_no_scc_priority):
- Iteration budget effect (50 vs. 100 vs. 400):

## Paper narrative

_(Draft sentences for the ablation section of the merged paper.)_
