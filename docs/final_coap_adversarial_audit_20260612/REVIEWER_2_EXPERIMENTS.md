# Simulated Reviewer 2 — Experiments and Statistics

**Profile:** Skeptical computational optimization reviewer.

## Audit summary

| Area | Status |
|---|---|
| Benchmark provenance | Pass — graph-benchmarks repo cited; preprocessing in OR1 |
| Primary sparse benchmark | Pass — 97 standard nonnegative instances |
| Exact DP subset | Pass — 57 instances, n≤20, 56/57 match |
| HiGHS MIP study | Pass — time-capped, scoped |
| External baselines | Pass — DRMacIver/FAS, igraph Eades; exclusions documented |
| DRMacIver representation | Pass — matrix-based pairwise ordering; timeouts reported |
| igraph behavior | Pass — documented as library baseline |
| In-repo adapted baselines | Pass — Borda, weighted Eades, random multistart |
| WMSF comparison | Pass — internal seed, not external literature rerun |
| EXP10 repeated runs | Pass — 1860/1860 per method; production namespace |
| EXP11 calibration | Pass — 6 instances; median improvement 0 |
| Holdout | Pass — parameter interpretation support |
| Sensitivity / ablation | Pass |
| LOLIB | Pass — constructive negative transfer result |
| Failures and timeouts | Pass — retained, not hidden |
| Runtime fairness | Pass — non-equal-time limitation explicit |
| Statistical tests | Pass — Wilcoxon, sign, bootstrap CI; scoped to paired subsets |
| Multiplicity | Pass — primary confirmatory framing on medians |
| Seed handling | Pass — documented |
| Objective recomputation | Pass — bw(π) from ranking |
| Common-subset comparisons | Pass — 93-instance DRMacIver subset |
| Claim wording | Pass — no global superiority |

## Ten explicit questions

1. **Two external baselines sufficient for scoped claim?** **Yes** — claim is “among evaluated methods” on sparse digraphs; exclusions (GNNRank, LOP_MA-EDM, CC25 external rerun) stated.
2. **Lack of another exact solver fatal?** **No** — bitmask DP + time-capped MIP adequate for scope.
3. **External-baseline ecosystem explained honestly?** **Yes** — DRMacIver strengths/limitations, igraph role, wrapper timeouts.
4. **21.60% statistic defined clearly?** **Yes** — mean relative excess (DR−IPSNS)/DR×100 on completed sparse subset; EXP4 convention cited.
5. **EXP10 38/55/0 interpreted correctly?** **Yes** — per-instance medians over 20 runs; ties at 1e−9; corroborative not standalone primary claim.
6. **Zero IPSNS objective variance overclaimed?** **No** — manuscript reports distinct objective counts where relevant; EXP10 notes DRMacIver variability.
7. **Non-equal-time limitation explicit?** **Yes** — runtime tradeoff discussed.
8. **EXP11 enough for extraction issue?** **Yes** for scoped calibration claim; not a full sensitivity study (appropriately bounded).
9. **LOLIB negative result constructive?** **Yes** — scope boundary, not buried.
10. **Any table/sentence imply global superiority?** **No** — “best observed among evaluated methods,” LOLIB counterexample.

## Verdict

**No experimental blocker.** Reviewer 2 may request more baselines in revision but not at desk-reject level given explicit scoping.
