# EXP10 Final Conclusions

**Generated:** 2026-06-12T02:24:19Z

## 1. Did DRMacIver complete all 1860 production runs?

Yes — 1860/1860 checkpoints and validated raw records.

## 2. How many runs failed or timed out?

0 non-ok records total across both algorithms.

## 3. How variable is DRMacIver?

53/93 instances with zero BW variance across 20 reps.

## 4. How variable is IPSNS?

0/93 instances showed objective variance across 20 seeds under frozen configuration.

## 5. Was IPSNS seed 0 representative?

Yes — seed 0 matched best observed IPSNS objective on all 93 instances.

## 6. Was the original EXP4 DRMacIver run representative?

See exp4_vs_exp10.csv per-instance percentile ranks.

## 7. Repeated-run median win/tie/loss?

38/55/0 (IPSNS/DR/tie) on 93 instances.

## 8. Does the original DRMacIver win (r20_60) persist?

EXP10 median: IPSNS=1688.0, DR=1698.0, winner=IPSNS

## 9. Does 21.6% relative-excess persist?

EXP10 mean (DR−IPSNS)/DR = 21.60%.

## 10. Does IPSNS remain best observed on nearly all sparse instances?

Yes on 38+55 of 93 under median comparison.

## 11. Statistically significant?

Wilcoxon p=7.739732463297963e-08.

## 12. Practically meaningful?

Mean relative excess 21.6%.

## 13. Does DRMacIver benefit from restarts?

See best_of_k.csv — compare k=1 vs k=20 expected best.

## 14. Does IPSNS benefit from multiple seeds?

No objective benefit observed (zero cross-seed variance); 12.9% of runs improved incumbent internally.

## 15. Was one DRMacIver run adequate?

See DRMacIver variability summary — depends on instance.

## 16. Strongest safe abstract claim?

On the 93-instance common sparse subset, IPSNS achieved lower or equal median backward weight than DRMacIver under a frozen repeated-run protocol.

## 17. Strongest safe results claim?

Median-based paired comparison: 38 wins, 55 ties, 0 losses vs DRMacIver (20 reps each).

## 18. Required limitation?

DRMacIver uses uncontrollable time/PID seeding; IPSNS zero variance does not prove determinism.

## 19. Additional stochastic experiment required?

No for sparse 93-instance claim; dense/holdout remain separate.

## 20. Ready for manuscript integration?

Yes, subject to author review of MANUSCRIPT_INTEGRATION_GUIDE.md.

## 21. Ready for COAP supplementary material?

Yes — run-level CSV, figures, and validation reports.

## 22. May COMPLETED.ok be created?

Yes, if validation gate passed.


## EXP4 single-run verification

Recomputed EXP4 common-subset: 37/56/8 (IPSNS/tie/DR).
