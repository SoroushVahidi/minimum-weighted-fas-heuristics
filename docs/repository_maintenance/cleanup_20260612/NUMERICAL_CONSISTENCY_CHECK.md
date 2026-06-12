# Numerical Consistency Check

**Date:** 2026-06-12  
**Purpose:** Verify that committed experiment summaries match manuscript claims.

## Principal manuscript claims vs. committed summaries

### EXP1b — Main benchmark (105 instances)

| Claim | Manuscript | Summary (`exp1b_core_benchmark_stats.json`) | Match |
|-------|-----------|----------------------------------------------|-------|
| Incumbent violations | 0 | `incumbent_protection_violations_external: 0` | ✓ |
| IPSNS improves LR-TA | 16/105 | `ipsns_improves_lrta: 16` | ✓ |
| IPSNS improves WMSF | 36/105 | `ipsns_improves_wmsf: 36` | ✓ |
| IPSNS ≥ both seeds | all 105 | `ipsns_no_worse_than_lrta_count: 105` | ✓ |

### EXP3 — Exact small-instance validation (57 standard instances)

| Claim | Manuscript | Summary (`exp3_exact_stats.json`) | Match |
|-------|-----------|-----------------------------------|-------|
| IPSNS optimal | 56/57 (98.2%) | `ipsns_optimal: "56/57 (98.2%)"` | ✓ |
| LR-TA optimal | 55/57 (96.5%) | `lrta_optimal: "55/57 (96.5%)"` | ✓ |
| WMSF optimal | 51/57 (89.5%) | `wmsf_optimal: "51/57 (89.5%)"` | ✓ |
| Only near-miss | r20_60 | Consistent with per-instance data | ✓ |

### EXP4 — External baseline comparison (97 standard instances)

| Claim | Manuscript | Summary (`exp4_external_stats.json`) | Match |
|-------|-----------|---------------------------------------|-------|
| IPSNS wins | 96/97 | `n_standard: 97`, IPSNS best on 96 | ✓ |
| IPSNS mean BW | 37,698 | `mean_bw: 37697.5052` | ✓ |
| DRMacIver mean BW | ~53,173 | `"drmaciver_fas": {"mean_bw": 53173...}` | ✓ |
| DR excess | ~21.6% | Consistent with paired comparison | ✓ |

### EXP10 — Stochastic robustness (93 instances, 20 reps each)

| Claim | Manuscript | Summary (`FINAL_CONCLUSIONS.md`) | Match |
|-------|-----------|----------------------------------|-------|
| IPSNS wins | 38 | Q7: 38/55/0 | ✓ |
| Ties | 55 | Q7: 38/55/0 | ✓ |
| IPSNS losses | 0 | Q7: 38/55/0 | ✓ |
| DR excess | 21.60% | Q9: 21.60% | ✓ |
| IPSNS zero variance | all 93 | Q4: 0/93 variance | ✓ |
| r20_60 median | IPSNS=1688, DR=1698 | Q8: IPSNS=1688.0, DR=1698.0 | ✓ |

### EXP11 — Topological extraction sensitivity (6 nonneg instances)

| Claim | Manuscript | Summary (`exp11_aggregate.json`) | Match |
|-------|-----------|----------------------------------|-------|
| All rules tied | Yes ("all matched") | `instances_improved_nonneg: 0` | ✓ |
| Instances tested | 6 | `n_instances_nonneg: 6` | ✓ |
| Median extraction gap | 0 | `median_extraction_gap_wF_minus_bw: 0.0` | ✓ |

### Upload artifact checksums

| File | MANIFEST.sha256 | SHA-256 (measured) |
|------|----------------|---------------------|
| Vahidi_COAP_Manuscript.pdf | `97eb6123…` | Verified ✓ |
| Vahidi_COAP_Cover_Letter.pdf | `df6622bd…` | Verified ✓ |
| Vahidi_Online_Resource_1_MWFAS.pdf | `8cc1479f…` | Verified ✓ |
| Vahidi_Online_Resource_1_MWFAS.zip | `5dc3875a…` | Verified ✓ |
| Vahidi_COAP_Manuscript_Source.zip | `0fd2b2c1…` | Verified ✓ |
| Vahidi_Related_Manuscripts_Statement.pdf | `7e5ee12c…` | Verified ✓ |

### Abstract word count

Target: 238 words (COAP guideline: 150–250).
Verified: 238 words in `paper_coap/main.tex` and in `EDITORIAL_MANAGER_COPY_READY_TEXT.md`.

### Manuscript page count

Verified: 45 pages (`paper_coap/main.pdf`).

## EXP11 inconsistency resolved

Prior to this second-pass cleanup, the committed repository had an internal inconsistency
in EXP11 summaries:
- `exp11_aggregate.json`: `n_instances: 6`, `instances_improved: 0`
- `EXP11_RESULTS.md`: `Instances: 8`, `instances improved / tied: 2 / 6`

The RESULTS.md values were carried over from a run that included 2 Peterson negative-weight
instances (which were excluded from the publication subset). The values have been corrected
to match the aggregate JSON and per-instance CSV (6 nonneg, 0 improved, consistent with
manuscript claim "all matched the repository rule on every tested instance").

## Verdict

**All principal manuscript numerical claims verified against committed summaries.
No numerical value changed. All upload artifact checksums confirmed.**
