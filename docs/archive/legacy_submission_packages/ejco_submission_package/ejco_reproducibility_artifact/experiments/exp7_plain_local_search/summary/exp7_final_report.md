# EXP7 Plain Local Search Comparator — Final Report

## Subset
18 non-negative instances from EXP6/EXP7 20-instance representative subset.
Excluded from comparison: peterson1, peterson2 (negative-weight arcs, outside main benchmark scope).

## Methods
- LR-TA seed: reference, no local search
- IPSNS full (400 iters): reference from EXP4
- lrta_adj_swap_ls: adjacent-swap LS until local optimum or 20 passes, seeded from LR-TA
- lrta_insert_ls: single-vertex insertion LS until local optimum, 200 moves, or 60s, seeded from LR-TA
- bestseed_insert_ls: insertion LS from best(LR-TA, WMSF) seed

## Summary (non-negative instances only)

| Method | n | Mean BW | Mean RT (s) | W/T/L vs LR-TA | W/T/L vs IPSNS | Mean moves |
|---|---:|---:|---:|:---:|:---:|---:|
| LR-TA (seed) | 18 | 97,184.9 | --- | 0/18/0 | 0/11/7 | --- |
| IPSNS (EXP4 full) | 18 | 94,127.4 | --- | 7/11/0 | 0/18/0 | --- |
| Adj-swap LS from LR-TA | 18 | 97,184.9 | 0.026 | 0/18/0 | 0/11/7 | 0.0 |
| Insertion LS from LR-TA | 18 | 95,778.6 | 0.234 | 4/14/0 | 1/12/5 | 0.9 |
| Insertion LS from best seed | 18 | 95,617.3 | 0.383 | 7/11/0 | 1/14/3 | 0.6 |

## Key findings

1. Adjacent-swap LS (lrta_adj_swap_ls) finds NO improving swaps on any of the 18
   non-negative instances. LR-TA already produces an adjacent-swap local optimum.

2. Insertion LS (lrta_insert_ls) from LR-TA achieves:
   - 4 wins, 14 ties, 0 losses vs LR-TA
   - 1 wins, 12 ties, 5 losses vs IPSNS full (EXP4)
   - On 5 large instances (dsip, rd_1024_2048_1, rd_big, s5378, s9234) where IPSNS gains most:
     insertion LS is still outperformed by IPSNS.
   - On gr10 (n=47): insertion LS matches IPSNS with only 2 moves.
   - On grid (n=1001): insertion LS beats IPSNS by 6 BW units (32948 vs 32954).

3. Best-seed insertion LS improves over LR-TA insertion LS by using the better WMSF seed
   on instances where WMSF is stronger (s5378, s9234). Still loses to IPSNS on dsip,
   rd_1024_2048_1, and rd_big.

## Interpretation for manuscript
- IPSNS is NOT simply generic local search: adjacent swap LS is uniformly ineffective,
  and insertion LS matches IPSNS only on small/medium instances where both find the
  same local optimum from LR-TA.
- On large sparse instances with nontrivial cyclic structure, IPSNS's SCC-local
  destroy-repair finds improvements that exhaustive single-vertex insertion misses.
- The result supports positioning IPSNS as a targeted refinement beyond seed quality:
  it concentrates search on the cyclic core rather than trying all order-local moves.
- Honest caveat: insertion LS ties or beats IPSNS on 13 of 18 instances,
  so IPSNS's advantage is concentrated on the hardest large-instance cases.
