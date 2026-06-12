# Final layout QA — pre-submission polish (2026-06-12)

Build: `paper_coap/main.pdf` after removing the one-row repeated-run table and title-page corrections.

## Manuscript changes

| Item | Action |
|---|---|
| One-row repeated-run table (`tab:exp10-stochastic-robustness`) | Removed from main text; `\input` deleted from Section 6.3 |
| Section 6.3 statistics | Integrated into two concise prose paragraphs (38/55/0, 21.60%, Wilcoxon, sign test, Cohen's \(d_z\), bootstrap CI) |
| Table numbering | Former Table 8 (repeated-run) removed; dense LOLIB table renumbered **Table 8** (was Table 9) |
| Title-page address | Corrected to **Newark, NJ 07102, USA** |
| Corresponding author email | Restored **sv96@njit.edu** (fixed missing `\global\advance\emailcnt` in custom `\email` hook) |
| ORCID | Unchanged: **0000-0003-1934-6282** with hyperlink |

## Blank page — cause and fix

**Cause:** The removed repeated-run table used `[t]` float placement at the start of Section 6.3 immediately after the exact-validation subsection. LaTeX deferred the top float to the next page while the preceding page had insufficient room for following text, producing a fully blank intervening page.

**Fix:** Remove the float entirely and let Section 6.3 prose flow continuously from Section 6.2. No `\clearpage`, `\newpage`, or negative `\vspace` hacks were applied.

## Page-by-page visual QA

Method: `pdftoppm` render at 120 dpi plus per-page `pdftotext` word counts.

| Page | Content | Result |
|---|---|---|
| 1 | Title, affiliation, ORCID, email, abstract start | OK |
| 2–10 | Introduction through formal analysis | OK |
| 11 | Table 1 (methods) | OK — readable |
| 12 | Table 2 (experiment overview) | OK |
| 13–14 | Section 5 experimental design | OK |
| 15 | Table 4 (IPSNS defaults) | OK |
| 16 | Table 5 (primary sparse comparison) | OK |
| 17 | Table 6 (IPSNS vs seed) | OK |
| 18 | Section 6.2 holdout + Section 6.3 repeated-run prose | OK — no blank page |
| 19 | Table 8 (dense LOLIB) | OK — full width, readable |
| 20 | Section 6.5 LOLIB discussion + Section 7 start | OK |
| 21–22 | Conclusion, declarations, data availability | OK |
| 23–24 | References | OK — no overflow |

**Blank pages:** none (all 24 pages have substantive text).

**Unresolved references:** none detected in PDF text.

## Final build metadata

- **Pages:** 24
- **Title:** IPSNS for Minimum Weighted Feedback Arc Set on Sparse Digraphs
- **Abstract:** 229 words
- **Keywords:** 6
- **PDF SHA-256:** `aebdf183f3a1c794b42b5b8a362524e396eaf7f7c8dd379c6c5b48f4a23bca77`
