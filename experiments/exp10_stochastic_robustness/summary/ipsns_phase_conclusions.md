# EXP10 IPSNS Phase Conclusions
**Generated:** 2026-06-11T19:00:56Z
**Instances with all 20 seeds:** 93/93
**Total valid runs analyzed:** 1860

---

## 1. Is IPSNS low variance or high variance?

**Across-seed variability:** 0/93 instances (0.0%) produce at least two distinct BW values across 20 seeds.
**Mean CV across instances:** 0.000000
**Conclusion: IPSNS is LOW VARIANCE.** The coefficient of variation is below 1% on average, indicating highly consistent results across different random seeds.

## 2. How frequently does IPSNS improve the seed?

- Global improvement rate: 240/1860 runs (12.90%) improved strictly over the initial incumbent
- Instances where ≥1 seed improved: 12/93

## 3. Are 20 seeds producing materially different solutions?

- 0 instances (0.0%) have non-constant BW across seeds
- 93 instances are completely deterministic across seeds (all seeds return identical BW)

## 4. Is the original EXP4 seed (seed=0) typical, unusually strong, or unusually weak?

- seed=0 matches the best observed BW on 93/93 instances (100.0%)
- Instances where seed=0 is WORSE than median: 0 ([])
- Instances where seed=0 is BETTER than median: 0
**Conclusion:** seed=0 is representative — it achieves the best result on ≥90% of instances.

## 5. Instances where seed choice materially changes the result

- 0 instances have any BW spread across seeds
- Top 10 by absolute BW spread:

## 6. Is the 400-iteration budget fully used before best solution is found?

- 93 instances have median best_iteration < 200 (budget likely excessive)
- 0 instances have median best_iteration ≥ 350 (budget is binding)
- For instances with any improvement: median best_iteration shown in ipsns_per_instance_summary.csv

## 7. Pathological or unstable instances

No instances with CV > 2% — IPSNS is stable across all seeds.

## 8. Notes for Manuscript

- These IPSNS-only conclusions do not yet reflect paired comparison with DRMacIver (EXP10 DRMacIver phase pending)
- EXP4 single-run result (seed=0 proxy) was representative
- Recommended manuscript wording for robustness: to be finalized after paired DRMacIver analysis
