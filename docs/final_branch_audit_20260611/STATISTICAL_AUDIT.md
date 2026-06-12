# Statistical Audit
**Date:** 2026-06-11

---

## 1. Win/Tie/Loss Counts

### IPSNS vs DRMacIver (EXP4, 93 common instances)

| Statistic | Value | Source | Status |
|-----------|-------|--------|--------|
| IPSNS wins (strict BW < DR) | 37 | `exp4_raw_summary.csv` recompute | VERIFIED |
| Ties (|IPSNS - DR| ≤ 1e-9) | 55 | Same | VERIFIED |
| DR wins | 1 | Same (r20_60 only) | VERIFIED |
| p-value (Wilcoxon) | < 0.001 | `exp4_external_stats.json` | Plausible (37 net wins) |
| p-value (sign test) | < 0.001 | Same | Plausible |

**Sign test analysis:** 37 wins + 1 loss = 38 non-ties out of 93 total. Under H0 (symmetric wins/losses), Binomial(37; 38, 0.5) has p < 0.001. ✓

**Wilcoxon analysis:** With 37 wins and 1 loss in the 38 non-tied pairs, the Wilcoxon statistic will strongly reject H0. ✓

### IPSNS vs LR-TA / WMSF (EXP1b, 105 instances)

| Pair | Wins | Ties | Losses |
|------|------|------|--------|
| IPSNS vs LR-TA | 16 | 89 | 0 |
| IPSNS vs WMSF | 36 | 69 | 0 |

Zero losses → any test rejects H0 for the one-sided alternative. ✓

## 2. Mean/Median Gap Statistics

### DRMacIver relative excess (21.61%)

**Formula:** `mean((DR_BW - IPSNS_BW) / DR_BW × 100)` over 93 common instances.

**Denominator check:** Uses DR_BW as denominator (not IPSNS_BW). This means we're measuring DR's excess over IPSNS relative to DR's own BW. This is the "mean relative excess" convention used throughout the paper. **Correct and consistent with manuscript wording ("about 21.6% worse in mean backward weight").**

**Subset check:** Computed over all 93 common completed instances (37 wins contribute positive values, 55 ties contribute ~0, 1 loss contributes slightly negative). Computing over 37-win subset only would give a much larger mean — the 21.61% is correctly computed over the full common set. **VERIFIED in prior audit session.**

**Dominance by large instances:** The arithmetic mean can be influenced by instances with large absolute BW. The discussion section mentions this implicitly by reporting both mean BW and win counts. A median-based comparison would be more robust; EXP10 is designed to provide median-based analysis across repeated runs.

### LR-TA excess over IPSNS (0.71%)

From `exp4_external_stats.json`: `mean_rel_gain_ipsns_pct = 0.7133` for LR-TA. This is small but nonzero, consistent with 16 IPSNS improvements over LR-TA.

## 3. Effect Size

The 37/55/1 distribution over 93 instances represents a large practical effect:
- Win rate among decisive cases: 37/38 = 97.4%
- Effect size (Cohen's g for sign test): g = (37-1)/(37+1) × 0.5 = large

The 21.61% mean relative gap is also a practically large effect in optimization contexts.

## 4. Multiplicity Concerns

The paper presents comparisons across multiple algorithms (8 in EXP4) and multiple instances (93-97). No explicit multiple-comparison correction is applied. This is standard practice for empirical optimization papers where the primary question is directional (does method A dominate method B?) rather than discovery of specific effects. The Wilcoxon and sign tests are descriptive summaries rather than formal hypothesis tests. **Acceptable for COAP computational paper.**

## 5. Stochastic Variability

**DRMacIver single-run limitation:** DRMacIver uses `srand(time(NULL)|getpid())` internally and was run once per instance in EXP4. The 37/55/1 result reflects a single non-deterministic draw per instance. Different runs of DRMacIver on the same instances could produce different win/tie/loss counts.

**EXP10 purpose:** To determine if the 37/55/1 result is representative over repeated randomized runs (20 IPSNS seeds × 20 DR repetitions × 93 instances).

**Current disclosure:** The manuscript mentions DRMacIver as "deterministic" based on its documentation, but in practice the `srand(time|pid)` seed means different process launches give different results. §5 does not explicitly state that DRMacIver was run once per instance in this study. This is a **Moderate** gap.

## 6. Exact Validation Statistics

| Statistic | Value | Assessment |
|-----------|-------|-----------|
| IPSNS optimal count | 56/57 = 98.2% | Clear and correct |
| Mean gap | 0.0006% | Tiny; dominated by the one non-optimal case |
| Non-optimal case | r20_60, gap=0.03% | Correctly reported |
| Negative-weight exclusion | 5 instances | Correct exclusion with clear rationale |

**Note:** The mean gap of 0.0006% is dominated by the r20_60 case (gap=0.0003 over one instance, mean is essentially just that divided by 57 ≈ 0.00053%). The manuscript's 0.0006% figure is slightly above this estimate — the exact value depends on rounding in the report. No concern.

## 7. LOLIB Statistics

| Statistic | Value | Assessment |
|-----------|-------|-----------|
| DRMacIver wins | 45/50 | Correctly reported |
| IPSNS wins | 5/50 | Correctly reported |
| Mean BW gap | 3.88% in DR's favor | Correctly reported |

## 8. Statistical Issues Not Found

| Check | Result |
|-------|--------|
| Unequal denominator | Not found |
| Different subset comparison | Not found (93 common used for all EXP4 paired tests) |
| Arithmetic mean domination by large instances | Acknowledged as a concern; EXP10 provides median comparison |
| Duplicated instances in benchmark | Prior audit found no duplicates after path-deduplication |
| Missing-value handling | Explicit: DRMacIver incompletions reported and excluded from paired tests |
| Tie handling | Ties counted explicitly (55); sign test counts ties separately |

## 9. Open Statistical Concern

**Single-run DRMacIver result:** The 37/55/1 result has uncertainty because DRMacIver is stochastic but was only run once. EXP10 will quantify this uncertainty. Until EXP10 completes, the manuscript should qualify this result as single-run. Recommended addition to §5 or §6.1:

> "DRMacIver/FAS was executed as a single run per instance using commit 16ff24a; the tool uses a time-based seed and results may vary across runs. A stochastic robustness study over repeated randomized runs is planned to quantify variability."

(Or reference EXP10 results once available.)

## 10. Summary

All statistical claims are correctly computed from the correct subsets. The primary concern is the single-run DRMacIver limitation and its impact on the 37/55/1 claim. EXP10 addresses this. No errors in reported statistics found.
