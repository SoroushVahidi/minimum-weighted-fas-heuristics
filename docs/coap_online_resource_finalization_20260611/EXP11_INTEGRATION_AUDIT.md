# EXP11 Integration Audit

## Protocol

- Post-hoc calibration study (not part of original main benchmark).
- Six nonnegative instances from topological-extraction counterexample set.
- Rules: repository Kahn min-vertex-id; max-id; weighted net-score; one-pass precedence-preserving insertion refinement.
- Broader exploratory run stopped; final frozen protocol uses fast calibration subset only.

## Results (frozen)

| Metric | Value |
|---|---|
| Instances evaluated | 6 |
| Backward-weight improvements | 0 |
| Headline changes | 0 |
| \(w(F)-\mathrm{bw}(\pi)\) | 0 on all evaluated instances |
| `instances_improved_nonneg` | 0 in `exp11_aggregate.json` |

## Supporting files

- `results/exp11/summary/exp11_aggregate.json`
- `results/exp11/summary/exp11_per_instance.csv`
- `results/exp11/tables/` (if present)
- Manuscript `table_exp11_extraction.tex`
- OR1 §S12

## Code

- `src/mwfas/topo_extraction.py` — post-processing utilities only; not part of headline IPSNS solver path.
- Repository rule remains `topo_order_active` in `lrta.py`.

## Status

**EXP11 fully incorporated.**
