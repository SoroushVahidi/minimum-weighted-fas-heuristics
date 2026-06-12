# Source ZIP Verification

**File:** `Vahidi_COAP_Manuscript_Source.zip`  
**SHA-256:** `0fd2b2c138c31798ff334a47f7d5c917fd32ec83aa5b05b932c82c20a32f7b38`  
**Size:** 145,760 bytes  

## Extraction check

Extracted to `/tmp/coap_source_verify/extracted/paper_coap/`

| Item | Present | Notes |
|---|---|---|
| `main.tex` | ✓ | Main LaTeX driver |
| `sections/` | ✓ | 9 section files (01–08 + 04_formal_analysis) |
| `figures/` | ✓ | PDF plots (exp6 budget curve) + TikZ framework_overview.tex |
| `bibliography/references.bib` | ✓ | Bibliography |
| `declarations/statements_and_declarations.tex` | ✓ | Declarations |
| `tables/` | ✓ | LaTeX table source files |
| `sn-jnl.cls` | ✓ | Springer journal class |
| `sn-mathphys-num.bst` | ✓ | Bibliography style |
| `submission/README_BUILD.txt` | ✓ | Build instructions |

## Forbidden items check

| Check | Result |
|---|---|
| `.git/` directory | NOT PRESENT ✓ |
| Audit reports | NOT PRESENT ✓ |
| Stale manuscript PDFs | NOT PRESENT ✓ |
| `__pycache__/` or `.pyc` | NOT PRESENT ✓ |
| `.env` or credential files | NOT PRESENT ✓ |
| Private correspondence | NOT PRESENT ✓ |
| Log files | NOT PRESENT ✓ |
| `/home/soroush/` absolute paths in .tex files | NOT PRESENT ✓ |
| Unrelated experiment files | NOT PRESENT ✓ |

## LaTeX build status

**LaTeX compiler (pdflatex/xelatex) not available in local environment.**

Prior verified build: The upload manuscript PDF (`97eb6123...`, 45 pages) was built from this ZIP
source at commit `04ca3ad` ("chore: sync manuscript PDF with submission upload bundle") and verified
by SHA-256. CI confirmed passing at that commit. The paper_coap/main.tex matches the extracted
source. No changes were made to the manuscript source since that build.

Content comparison (partial):
- `main.tex` title matches: "SCC-Local Destroy-and-Repair Heuristics for Minimum Weighted Feedback Arc Set on Sparse Digraphs" ✓
- ORCID `0000-0003-1934-6282` present ✓
- Springer `sn-jnl.cls` is the current Springer journal class ✓

## Figure check

- `figures/exp6_ipsns_budget_curve.pdf` — generated data figure ✓
- `figures/framework_overview.tex` — TikZ vector figure (no AI-generated images) ✓

All figures deterministic (no generative AI artwork in source). ✓

## Verdict

**SOURCE ZIP: APPROVED FOR UPLOAD**  
(LaTeX rebuild not performed in local environment; content and structure verified clean)
