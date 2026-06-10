# COAP Formal Analysis Change Report

**Date:** 2026-06-10  
**Base commit:** `76a3412`  
**Scope:** Formal correctness/complexity pass only (no experiments, results, or conclusions rewritten)

## Propositions added

| Label | Title | Location |
|---|---|---|
| `prop:lrta-feasibility` | LR-TA feasibility and termination | `sections/04_formal_analysis.tex` |
| `prop:addback-correctness` | Correctness of the add-back shortcut | same |
| `prop:ipsns-monotonicity` | IPSNS feasibility and monotonicity | same |
| `prop:ipsns-termination` | IPSNS termination | same |

## Assumptions used

- Nonnegative aggregated arc weights in the intended experimental setting
- Numerical tolerance \(\tau>0\) (implementation default \(10^{-12}\))
- Sparse edge-indexed adjacency representation as implemented
- IPSNS iteration budget \(T\) and top-\(K\) pool are finite user parameters
- Floating-point deactivation follows the code branches for `eps <= tau` and `W[eid] <= tau`

## Final complexity statements (worst-case, implementation-faithful)

| Component | Bound stated in manuscript |
|---|---|
| LR-TA Phase I | \(O(m(n+m))\) |
| LR-TA Phase II | \(O(r\log r + r(n+m))\) |
| WMSF-style seed | \(O(n+m + \sum_S(m_S\log m_S + r_S(k+m_S) + \log(k)\,m_S))\) (conservative SCC sum) |
| IPSNS initialization | LR-TA + WMSF seed + \(O(m)\) evaluation |
| IPSNS per iteration | \(O(m + s\log s + c_S(n_S+m_S) + r_S\log r_S + r_S(n_S+m_S))\) |
| IPSNS total | Seed costs + sum over \(T'\le T\) iterations of per-iteration SCC-local terms |
| Space | \(O(n+m)\) global sparse storage plus \(O(n)\)/\(O(n+m)\) scratch |

## Code locations supporting claims

| Claim | Primary code |
|---|---|
| LR-TA Phase I progress/termination | `lrta.py`: `local_ratio_fas_fast`, `find_any_cycle_eids` |
| Add-back rules | `lrta.py`, `wmsf.py` (`wmsf_minimizeFas_scc`, `wmsf_minimize_global`), `ipsns.py` (`minimize_addback_inside_scc`) |
| IPSNS monotonicity | `ipsns.py`: `lns_merge_wmsf_lr_best_incumbent` accept/reject + `best_snapshot` |
| IPSNS termination | finite `for it in range(1, iters+1)` + early break on empty scored SCC list |
| Backward-weight evaluation | `evaluation.py`: `compute_forward_backward` |

## Manuscript/code discrepancies

**None requiring scientific correction.** Verified alignment on:

- forward add-back without topo recompute;
- backward add-back with reachability \(v\leadsto u\) and topo refresh;
- tolerance-based deactivation;
- IPSNS rollback and incumbent snapshot semantics;
- full WMSF seed mode inside IPSNS.

## Exact prose / pseudocode changes

| File | Change |
|---|---|
| `sections/04_formal_analysis.tex` | **New** formal subsection with 4 propositions, proofs, complexity paragraphs |
| `sections/04_algorithmic_framework.tex` | Insert `\input{sections/04_formal_analysis}`; invariants subsection now cites Propositions~\ref{prop:ipsns-monotonicity}, `\ref{prop:lrta-feasibility}`, `\ref{prop:addback-correctness}` |
| `sections/01_introduction.tex` | Contribution list rebalanced: formal properties + complexity characterization added; removed vague “correctness guarantees” bullet |

**Unchanged:** Algorithms 1–2 pseudocode, all numerical results, experiment text, tables, figures, conclusion substance.

## Consistency check

Searched manuscript for conflicting runtime/optimality claims. No edits required outside Section 4 and the introduction contribution list. Existing discussion language already states that monotonicity is not an approximation guarantee and that EXP7 “adjacent-swap local optimum” refers to a baseline method, not IPSNS.

## Intentionally conservative / unproved

- Approximation ratios or PTAS/integrality claims
- IPSNS convergence to local/global optimum
- Independence from floating-point tolerance in exact arithmetic sense
- Uniform superiority of SCC-local repair cost over global repair on every instance
- Practical runtime predictions from asymptotics alone
