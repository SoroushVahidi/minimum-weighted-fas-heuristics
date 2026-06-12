# Known Limitations — Online Resource 1 (frozen 2026-06-12)

1. Sparse nonnegative weighted-digraph scope; LOLIB defines a dense scope boundary.
2. Headline comparisons are relative to the evaluated method set, not a universal SOTA claim.
3. Reported objective is ordering backward weight $\mathrm{BW}(\pi)$; $w(F)\ge \mathrm{BW}(\pi)$ in general.
4. Topological extraction uses Kahn sorting with min-vertex-id tie-breaking; EXP11 found no change on a six-instance calibration subset.
5. EXP10 raw JSON (3720 records) is not bundled; validated summaries support headline claims.
6. IPSNS zero cross-seed variance is empirical stability, not mathematical determinism.
7. DRMacIver comparisons are quality-focused, not equal-time.
8. Tests do not constitute formal verification.
9. Runtime values are hardware-dependent.
10. Remote GitHub Actions execution remains pending until branch push.
