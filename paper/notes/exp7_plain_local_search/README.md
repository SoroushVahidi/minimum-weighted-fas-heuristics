# EXP7 Plain Local Search Comparator — Notes

## Purpose
Test whether IPSNS improvements over LR-TA can be matched by generic order-local
improvement heuristics (adjacent swap, single-vertex insertion).

## Key results (18 non-negative instances)
- Adjacent-swap LS: 0 improvements over LR-TA on all instances (LR-TA is already
  an adjacent-swap local optimum).
- Insertion LS from LR-TA: 4 wins vs LR-TA, 12 ties vs IPSNS,
  5 losses vs IPSNS (on large sparse instances).
- Best-seed insertion LS: 1 wins, 14 ties, 3 losses vs IPSNS.

## Interpretation
IPSNS is not simply generic local search. On large sparse instances (n>=1000),
IPSNS's SCC-local destroy-repair consistently outperforms insertion LS. On small
instances (n<=47), insertion LS can match IPSNS by finding the same improvements
from the LR-TA seed. This supports the claim that IPSNS concentrates search effort
on the cyclic core in a way that generic order-local moves cannot replicate at scale.

## Files
- exp7_raw_summary.csv -- per-instance per-method raw results (60 rows)
- exp7_method_summary.csv -- aggregated by method (non-negative instances)
- exp7_final_report.md -- full analysis report
- paper/tables/table_plain_local_search.tex -- LaTeX comparison table
