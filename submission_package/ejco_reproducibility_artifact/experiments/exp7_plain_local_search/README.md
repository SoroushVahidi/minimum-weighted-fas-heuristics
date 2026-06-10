# EXP7: Plain Local Search Comparator

## Purpose
Determine whether IPSNS gains over LR-TA can be matched by simple order-local
improvement heuristics, addressing reviewer questions about whether IPSNS merely
wraps generic local search. This experiment runs two generic ordering local-search
methods (adjacent-swap LS and single-vertex insertion LS) from the same LR-TA seed
used by IPSNS and compares their backward-weight outcomes against IPSNS from EXP4/EXP6.

## Selected subset
Same 20-instance representative sparse subset as EXP6:
experiments/exp6_ipsns_budget_curve/config/selected_instances.csv

Instances span density from 0.00045 (s9234) to 0.17 (peterson1/2) and
size from n=10 (gr1-acyclic, peterson1, peterson2) to n=4079 (dsip).

## Methods
A. lrta_adj_swap_ls
   - Seed: LR-TA ordering
   - Move: swap adjacent pair in the ordering if it reduces backward weight
   - Rule: best-improvement per position in each pass (accept all improving swaps in a pass)
   - Stop: local optimum (no improving swap exists) or 20 passes

B. lrta_insert_ls
   - Seed: LR-TA ordering
   - Move: remove one vertex from its position and re-insert at the globally best position
   - Rule: best-improvement (best position for each vertex), sequential vertex order per pass
   - Stop: local optimum (no improving insertion exists) or 200 accepted moves or 60 s

C. bestseed_insert_ls  (optional, included if WMSF seed is better)
   - Seed: best of LR-TA and WMSF by backward weight
   - Move: single-vertex insertion (same as B)
   - Stop: local optimum or 200 accepted moves or 60 s

## Comparison references (from EXP4/EXP6)
- LR-TA seed BW (before any LS)
- IPSNS full BW (EXP4, 400 iterations)
- WMSF BW (EXP4)

## Metrics per method
- backward_weight after LS
- runtime_seconds (total including seed)
- improvement over LR-TA (lrta_bw - ls_bw)
- win/tie/loss vs IPSNS full (EXP4)
- win/tie/loss vs LR-TA
- accepted_moves
- stopped_reason (local_optimum / max_passes / max_moves / time_limit / error)

## Expected runtime
~10-30 minutes for 20 instances × 3 methods. Large instances (n=1000-4079)
may hit the 60-second time limit for insertion LS.

## How to rerun
```
cp experiments/exp6_ipsns_budget_curve/config/selected_instances.csv \
   experiments/exp7_plain_local_search/config/selected_instances.csv
python3 scripts/run_exp7_plain_local_search.py
python3 scripts/postprocess_exp7_plain_local_search.py
```

## Note
EXP1b–EXP6 are not modified. EXP4 results supply IPSNS/WMSF/LR-TA reference
values on the selected subset. No algorithm code is modified.
