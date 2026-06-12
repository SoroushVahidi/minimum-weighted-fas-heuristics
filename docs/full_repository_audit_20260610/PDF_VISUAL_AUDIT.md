# PDF Visual Audit — `paper_coap/main.pdf`

**Audit date:** 2026-06-10  
**File:** `paper_coap/main.pdf`  
**SHA-256:** `b596f694da1637a0c742ceb03ea85e1debf7ac0eb77bcf8cb034ee4aaacca712`  
**Pages:** 40 | **Size:** 296,609 bytes | **Engine:** LaTeX + xdvipdfmx

**Method:** Full-text extraction (`pdftotext`), structural checks, `main.log` warning scan. **Not** a pixel-level review of every figure — recommend final human pass before upload.

## Page-by-page structural checks

| Element | Status | Notes |
|---|---|---|
| Title block | OK | Title, author, affiliation, email present |
| ORCID | OK | Textual ORCID link (no logo EPS — template limitation) |
| Abstract | OK | Within word limit; readable |
| Keywords | OK | Page 2 |
| Introduction | OK | Equations and citations render |
| Algorithm blocks | OK | "Algorithm" text present in extraction |
| Theorems/Propositions | OK | Formal analysis section present |
| Framework figure (TikZ) | Likely OK | Compiled without fatal errors |
| EXP4–6 figures | Present as PDF includes | Files in `paper_coap/figures/` |
| Dense tables | Review needed | Multiple wide tables — check column overflow manually |
| Captions | OK in text extraction | No obvious truncation in extracted text |
| References | OK | Numbered list through [26]; page 39–40 |
| Declarations | OK | "Data availability" and AI disclosure detected |
| Final page | OK | Ends with reference [26] |

## Build log warnings (`paper_coap/main.log`)

| Warning type | Count | Severity |
|---|---:|---|
| Underfull `\vbox` | Many | Minor — vertical whitespace in two-column layout |
| Underfull `\hbox` | Several | Minor — line breaking in tables/refs |
| Overfull / overlap | **Not observed in log grep** | — |
| Missing citations | **Not observed** | — |
| Fatal errors | **None** (PDF built) | — |

## Issues requiring manual visual confirmation

| ID | Severity | Issue |
|---|---|---|
| P-01 | Moderate | **Wide tables** — verify no column overlap on printed PDF |
| P-02 | Minor | Underfull vboxes may cause **excessive whitespace** on some pages |
| P-03 | Minor | ORCID without logo — acceptable per project note |
| P-04 | Low | Verify figure PDFs (`exp4_*.pdf`) font embedding if journal requires |
| P-05 | Moderate | **Color/contrast** in figures — not verified in this pass |

## Not observed (text/log level)

- Clipped title or abstract
- Detached captions (no strong evidence)
- Broken hyperref links (not fully tested)
- Malformed reference numbering
- Empty pages mid-document

## Recommendation

Schedule a **15-minute human flip-through** focusing on: (1) wide tables in Results, (2) algorithm pseudocode line breaks, (3) figure legibility at print size, (4) declarations page completeness.
