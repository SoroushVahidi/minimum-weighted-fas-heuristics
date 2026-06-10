# EXP2: Ablation Study

## Purpose

This experiment is part of the merged Minimum Weighted Feedback Arc Set (MWFAS) paper and directly addresses the component-contribution question that reviewers commonly raise about novelty. It answers: which parts of the combined LR-TA + WMSF + IPSNS framework actually matter, and how much does each contribute to the final objective value?

## Variants

| Variant | Status | Description |
|---|---|---|
| `lr_no_addback` | **Runnable** | LR cycle reduction only (Phase 1), without the topological add-back (Phase 2). Isolates the contribution of add-back. |
| `lrta_full` | **Runnable** | Full LR-TA: Phase 1 cycle reduction + Phase 2 add-back. |
| `wmsf_seed` | **Runnable** | WMSF pipeline only (removeArcs + minimize + stabilize). |
| `best_seed_no_lns` | **Runnable** | Best of LR-TA and WMSF seeds with no LNS refinement. Shows the ceiling for seed quality. |
| `ipsns_no_scc_priority` | **Runnable** | IPSNS with uniform random SCC selection (no BW-weighted top-K priority). Isolates the contribution of the SCC selection heuristic. |
| `ipsns_50iters` | **Runnable** | IPSNS with 50 iterations instead of 400. |
| `ipsns_100iters` | **Runnable** | IPSNS with 100 iterations instead of 400. |
| `ipsns_full` | **Runnable** | Full IPSNS with default 400 iterations. |

## Code changes needed before running TODO variants

### `lr_no_addback`

**Missing:** `local_ratio_fas_fast` in `src/mwfas/lrta.py` (line 216) runs Phase 1 and Phase 2 in a single function with no flag to skip add-back. The Phase 2 block starts at line 260 (`# Phase 2: add-back`).

**Required change:** Add an `add_back=True` parameter to `local_ratio_fas_fast`. When `False`, skip lines 260–278 and return after Phase 1. Then expose a new entry point `lr_no_addback_ranking_from_dimacs_fast` (or add `--no-addback` flag to `scripts/run_lrta.py`) that calls `local_ratio_fas_fast(..., add_back=False)`.

### `ipsns_no_scc_priority`

**Missing:** `lns_merge_wmsf_lr_best_incumbent` in `src/mwfas/ipsns.py` (line 617) hardcodes weighted-random selection from the top-K highest-BW SCCs:

```python
pool = scored[: min(topK_scc, len(scored))]
picked = random.choices(pool, weights=[x[0] for x in pool], k=1)[0]
```

**Required change:** Add a `scc_select_mode` parameter (`"weighted"` | `"random"`). When `"random"`, use the full `scored` list (all non-zero-BW SCCs) and pass `weights=None` to `random.choices` for uniform selection.

## Instance subset

`configs/exp2_ablation_instances.txt` — 10 instances (first 10 from the full 123-instance benchmark set), covering small bad-graph instances (bad1–bad7, bad) and two larger instances (grid, r1000). This subset is small enough to run all variants in <10 minutes.

## Outputs

All outputs go under `experiments/exp2_ablation/`:
- `raw/` — per-instance per-variant ranking CSVs (gitignored)
- `logs/` — per-variant run logs
- `tables/exp2_ablation_summary.csv` — main comparison table (committed)
- `summary/exp2_ablation_summary.md` — human-readable findings (committed)

## Running

```bash
tmux new-session -d -s mwfas_exp2 "cd ~/minimum-weighted-fas-heuristics && bash experiments/exp2_ablation/run_exp2_ablation_tmux.sh"
tmux attach -t mwfas_exp2
```

Do **not** start until EXP1 (`mwfas_exp1`) finishes and its results are reviewed.
