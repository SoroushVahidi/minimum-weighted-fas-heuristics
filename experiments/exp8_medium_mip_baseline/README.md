# EXP8: Time-Capped MIP Baseline for Medium Sparse Instances

## Purpose

External reviewers requested a stronger exact/ILP comparator on medium instances.
EXP8 adds a time-capped MIP/LP baseline on a 15-instance deterministic medium sparse
subset, allowing us to report how close IPSNS is to solver incumbents and LP lower bounds
on instances larger than the small DP-validated subset.

## Subset Selection

15 instances from EXP4 nonneg sparse benchmark, n = 20..318, selected deterministically:
- Group 1 (ipsns_gain): instances where IPSNS strictly improves over LR-TA
- Group 2 (small_tie): n <= 75, including the near-miss r20_60
- Group 3 (medium_tie): broader n range to cover 83..318

See `config/selected_instances.csv` for the full list with n, m, BW references.

## Solver

scipy.optimize.milp (HiGHS backend), scipy 1.17.1.

## MIP Formulation

Linear ordering MIP with pair binary variables:
- x_{ij} = 1 iff vertex i precedes vertex j in the ordering (i < j index-pair)
- Objective: minimize sum_{i<j} (ew[(j,i)] - ew[(i,j)]) * x_{ij}  + constant
- Constraints: triangle transitivity for all triples (i,j,k) with i<j<k:
    A: x_{ij} + x_{jk} - x_{ik} <= 1
    B: -x_{ij} - x_{jk} + x_{ik} <= 0

For n <= 200: full MIP (integer variables), all triangle constraints.
For n > 200:  LP relaxation (continuous variables), valid lower bound.

## Time Limit

120 seconds per instance (15 instances selected).
Total worst-case runtime: ~30 minutes.

## Expected Runtime

Small instances (n <= 101): likely proves optimality within seconds.
Medium instances (n = 170): may prove optimality or timeout with good incumbent.
Large instances (n = 273..318): LP relaxation only; solves fast.

## How to Launch

```bash
cd ~/minimum-weighted-fas-heuristics
mkdir -p experiments/exp8_medium_mip_baseline/logs experiments/exp8_medium_mip_baseline/summary
tmux new-session -d -s mwfas_exp8_mip \
  "python3 scripts/run_exp8_medium_mip_baseline.py --time-limit-seconds 120 \
   > experiments/exp8_medium_mip_baseline/logs/exp8_tmux.log 2>&1; \
   python3 scripts/postprocess_exp8_medium_mip_baseline.py \
   >> experiments/exp8_medium_mip_baseline/logs/exp8_tmux.log 2>&1; \
   echo EXP8_DONE >> experiments/exp8_medium_mip_baseline/logs/exp8_tmux.log"
```

## How to Monitor

```bash
# Attach to session:
tmux attach -t mwfas_exp8_mip
# Detach: Ctrl-b then d

# Tail log:
tail -f experiments/exp8_medium_mip_baseline/logs/exp8_tmux.log
```

## Outputs (produced by tmux job)

- `summary/exp8_mip_raw_summary.csv` — one row per instance, written incrementally
- `summary/exp8_mip_summary.json` — aggregate stats
- `summary/exp8_final_report.md` — human-readable report
- `logs/exp8_tmux.log` — full console output

## Notes

- EXP1b–EXP7 are NOT modified.
- Algorithm code and result values are NOT modified.
- This experiment does NOT touch the manuscript; integration is a separate future pass.
