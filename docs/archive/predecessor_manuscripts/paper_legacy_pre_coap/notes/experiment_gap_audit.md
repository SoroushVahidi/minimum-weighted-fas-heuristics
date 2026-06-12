# Experiment Gap Audit

Date: 2026-06-06

This audit is conservative. "Run now" is reserved for experiments that appear essential from locally verified evidence. None met that bar.

| Possible missing experiment | Concern it answers | Do EXP1b--EXP5 already answer it? | Cost / risk | Recommendation |
|---|---|---|---|---|
| Additional graph families beyond sparse DIMACS and dense LOLIB | benchmark breadth / reviewer request for more families | Partially. EXP4 covers the main sparse benchmark and EXP5 adds dense LOLIB, but predecessor JOCO limitations still show broader family coverage as an open limitation. | Medium implementation and writing cost; risk of scope drift and new fairness disputes. | Do not run now. State the current scope honestly. |
| IPSNS parameter sensitivity expansion | parameter justification | Largely yes. EXP2 already shows convergence by 50 iterations on the ablation subset and negligible SCC-priority effect there. | Low-to-medium run cost, but easy to overinterpret from a small subset. | Do not run now. Use EXP2 carefully and avoid universal tuning claims. |
| Topological tie-breaking / add-back extraction ablation | topological-order dependence | Only indirectly. Deterministic extraction is documented, but no dedicated experiment isolates tie-breaking effects. | Small-to-medium cost if implemented cleanly; would require careful reporting and may tempt code changes. | Not essential now. Mention as a limitation unless a referee explicitly asks. |
| Exact validation beyond `n <= 20` | theory depth / solution quality | Mostly yes for CAIE. EXP3 already gives strong near-optimal evidence where exact DP is feasible. | Medium-to-high cost because exact scaling gets expensive quickly. | Do not run now. |
| More dense LOLIB coverage | dense-ordering weakness / transfer robustness | Enough for current purpose. EXP5 already establishes the dense-scope boundary. | Medium cost; likely strengthens DRMaciver more than IPSNS. | Do not run now. |
| GNNRank or other learned ranking baselines | baseline modernity / scientific significance | No direct answer, but CAIE notes and current scope support omitting learned methods if stated clearly. | High setup and fairness cost; risk of becoming a different paper. | Do not run now for CAIE. Mention as future work. |
| Unweighted datasets or Cavallaro-style additional graph collections | dataset breadth / relation to prior papers | Partially. Current sparse benchmark overlaps the main claim-bearing setting; EXP5 broadens structure. | Medium acquisition and fairness cost; could reopen problem-definition mismatch. | Do not run now. |
| Stronger exact ILP / Gurobi / SCIP comparison | exact-method competitiveness | Enough for current target. EXP3 already uses exact DP on feasible sizes. | High environment and solver cost; external licensing risk. | Do not run now. |
| Runtime profiling or memory analysis | practical significance / engineering depth | Partially. Existing reports contain runtimes, but not a polished profiling narrative. | Low-to-medium if just summarized; higher if instrumented deeply. | Optional only if a short table can be produced from existing logs without reruns. Not essential. |

## Bottom line

- No missing experiment is clearly essential for CAIE from the locally verified record.
- The highest-value work is manuscript completion: Experimental Design, Results, and Discussion should explicitly map EXP2--EXP5 to the concern classes above.
- The one concern that is only weakly answered experimentally is topological extraction dependence, but that is better handled as a stated limitation unless a reviewer specifically demands a dedicated ablation.
