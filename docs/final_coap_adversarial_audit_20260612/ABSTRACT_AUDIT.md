# Abstract Independent Audit

**Manuscript:** `paper_coap/main.tex`  
**Post-correction audit date:** 2026-06-12

## COAP length constraint

Per `paper_coap/COAP_TEMPLATE_AND_GUIDELINES_AUDIT.md` (sourced from COAP submission guidelines, accessed 2026-06-10): **150–250 words**.

Springer Nature general support page states abstracts should not exceed **350 words**; COAP-specific guidance in this repository audit is **150–250**. Both are noted; the stricter COAP figure governs portal entry.

## Pre-correction defect

| Metric | Pre-correction | Post-correction |
|---|---|---|
| Words | 271 | **238** |
| Characters (plain) | ~2,079 | ~1,890 |
| Sentences | 10 | 10 |
| Acronyms defined at first use | MWFAS, IPSNS, LR-TA, SCC | same |

**Action taken:** Minimal trim in `paper_coap/main.tex` (no numerical or scientific claim changes).

## Self-contained checklist

| Criterion | Status |
|---|---|
| Problem introduced without relying on title | Pass — MWFAS defined in first sentence |
| MWFAS defined sufficiently | Pass |
| No undefined acronym | Pass — IPSNS expanded at first use; LR-TA, SCC, WMSF contextualized |
| IPSNS described clearly | Pass — destroy-and-repair, SCC scoring, top-K, incumbent protection |
| Inherited seeds not overemphasized | Pass — one sentence on LR-TA/WMSF framework |
| Sparse scope stated | Pass |
| Benchmark scale stated accurately | Pass — 96/97, 93-instance median study |
| Strongest result stated safely | Pass — “best observed among compared methods” |
| Exact/MIP evidence summarized usefully | Pass — 56/57 DP, MIP reference points |
| Limitations not excessive | Pass — LOLIB scope boundary one sentence |
| No citations | Pass |
| Length within COAP 150–250 | **Pass (post-correction)** |
| No “state of the art” language | Pass |
| No “fully reproducible” language | Pass |

## Acronym inventory

MWFAS, IPSNS, SCC, LR-TA, WMSF (style seed), DRMacIver/FAS (in results sentence).

## Verdict

**Self-contained after correction.** Portal abstract field must be updated to match trimmed text in `main.tex` (not the stale 271-word copy in `docs/coap_cover_letter_and_upload_20260612/EDITORIAL_MANAGER_COPY_READY_TEXT.md`).
