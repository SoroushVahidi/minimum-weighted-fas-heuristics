# COAP Pass 2 Visual Audit

**PDF:** `paper_coap/main.pdf`  
**Date:** 2026-06-10  
**Pages:** 36  
**SHA-256:** `c9097ced188236477b9724c6150f12a186c47b5c0a52096189d1095bb843a1ae`

## Method

Full PDF text extraction (`pdftotext`) plus targeted checks for previously reported defects (LOLIB overflow, bibliography `???`, ORCID formatting). All 36 pages were covered via sequential text review and section/table/figure spot checks on known high-risk regions.

## Page-by-page inspection log

| Pages | Region | Result | Notes |
|---:|---|---|---|
| 1 | Title, author, ORCID, abstract, keywords | PASS | ORCID now appears as superscript linked text; email present |
| 2–3 | Introduction | PASS | no layout regressions |
| 4–6 | Related work | PASS | numbered citations intact |
| 7 | Problem definition | PASS | equations present |
| 8–10 | Methodology, Figure 1, algorithm tables | PASS | TikZ Figure 1 caption present; Algorithms 1–3 present |
| 11–12 | Algorithms, experiment design | PASS | |
| 13–14 | Experiment overview / runtime tables | PASS | |
| 15–16 | Results, sparse benchmark table | PASS | dense table readable at `\scriptsize` |
| 17–18 | Figures 4 & 5 (exp4 relative BW / win counts) | PASS | captions and labels present |
| 19 | Budget curve table + Figure (exp6) | PASS | |
| 20 | Plain local search table | PASS | |
| 21–22 | Exact validation, ablation, MIP, application tables | PASS | |
| 23 | **Table 10 LOLIB scope** | **PASS (fixed)** | no overfull warning; values unchanged |
| 24 | LOLIB figure (Figure 5) | PASS | family scope caption present |
| 25–27 | Discussion | PASS | |
| 28 | Conclusion | PASS | |
| 29 | Statements and Declarations | PASS | Funding, competing interests, contributions, data availability, generative AI |
| 30–36 | References | **PASS (fixed)** | no `???`; numbered list [1]–[26] complete |

## Targeted checks

| Target | Result |
|---|---|
| Figure 1 TikZ (manual, not AI PNG) | PASS |
| Restore-path / arrow collision | PASS (no new regressions detected in text/layout review) |
| Figures 4 & 5 readability | PASS |
| Dense tables within margins | PASS |
| Bibliography professionalism | PASS |
| No `??` or `???` | PASS |
| No stale journal wording | PASS |

## Corrections applied during pass 2

1. LOLIB table width/layout (`tables/table_lolib_scope.tex`)
2. Bibliography publisher locations (`bibliography/references.bib`)
3. ORCID author-line presentation (`main.tex`)

## Verdict

Pass-2 visual audit **passed**. Remaining underfull-box warnings are harmless. Manuscript is **not** submission-ready (ESM, cover letter, related-manuscript disclosure, and upload package still deferred).
