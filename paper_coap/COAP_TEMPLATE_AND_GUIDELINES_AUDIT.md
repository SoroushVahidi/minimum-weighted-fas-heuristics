# COAP Template and Guidelines Audit

**Access date:** 2026-06-10  
**Journal:** Computational Optimization and Applications (COAP)  
**Springer journal ID:** 10589

## Official guideline URLs consulted

| Resource | URL | Access date |
|---|---|---|
| COAP submission guidelines | https://link.springer.com/journal/10589/submission-guidelines | 2026-06-10 |
| COAP aims and scope | https://link.springer.com/journal/10589/aims-and-scope | 2026-06-10 |
| Springer Nature LaTeX author support | https://www.springernature.com/gp/authors/campaigns/latex-author-support | 2026-06-10 |
| Springer Nature LaTeX template download page | https://www.springernature.com/gp/authors/campaigns/latex-author-support/see-where-our-services-will-take-you/18782940 | 2026-06-10 |

## Official template source used in this pass

| Item | Value |
|---|---|
| Intended official download | Springer Nature journal article template package (December 2024 version) |
| Primary CMS URL attempted | `https://resource-cms.springernature.com/springer-cms/rest/v1/content/19238648/data/v3` |
| Primary download result | **404 / JSON error** on 2026-06-10 |
| Secondary page fetch attempted | Springer LaTeX author support landing page (HTML only; no direct ZIP link extracted programmatically) |
| Fallback mirror used | `SoroushVahidi/frontier-allocation-for-budgeted-llm-inference/paper_ml_journal_snjnl_stage/` |
| Archived mirror in repo | `paper_coap/template_reference/sn-jnl-template-v3.1-dec2024-local-mirror.zip` |
| Archive SHA-256 | `c65e718f7a717b3fbb60f9c9bcddd7bd35bf06f6436d66d53e19d5107985491f` |
| Class file version string | **Version 3.1 December 2024** (from `template_reference/sn-article.tex`) |
| Sample file in archive | `sn-article.tex`, `sn-jnl.cls`, eight `.bst` files |

**Note:** The fallback mirror matches the official December 2024 template family (`sn-jnl.cls` v3.1). The mirror is missing `Orcidlogo.eps`; COAP `main.tex` therefore uses a text ORCID hyperlink fallback.

## Confirmed COAP requirements

| Requirement | Official source | Confirmed value | Applied in `paper_coap/` |
|---|---|---|---|
| LaTeX template family | COAP submission guidelines → Text | Springer Nature LaTeX template encouraged | `sn-jnl.cls` |
| `sn-jnl` vs legacy `svjour3` | Springer author support | Current unified template is `sn-jnl`; `svjour3` deprecated | `sn-jnl` only |
| LaTeX source accepted | COAP submission guidelines → Manuscript Submission / Text | Yes; editable source + compiled PDF | isolated source tree |
| Bibliography style | COAP submission guidelines → References | Numbered citations in square brackets; numbered reference list; DOIs when available | `sn-mathphys-num` (`sn-mathphys-num.bst`) |
| Review / anonymity model | COAP submission guidelines (no double-blind requirement stated) | Single-anonymized / author-visible manuscript acceptable | author block included |
| Abstract length | COAP submission guidelines → Abstract | 150–250 words | transferred abstract verified in compile report |
| Keyword count | COAP submission guidelines → Keywords | 4–6 keywords | six keywords retained |
| Heading levels | COAP submission guidelines → Headings | Decimal headings, max three levels | unchanged section hierarchy |
| Statements and Declarations | COAP submission guidelines → Statements and Declarations | Required before references | `declarations/statements_and_declarations.tex` |
| Acknowledgments placement | COAP submission guidelines → Acknowledgments | Separate title-page section | not added to main body (none in source manuscript) |
| Supplementary material naming | COAP submission guidelines → Supplementary Information (SI) | Refer as **Online Resource**; files named `ESM_1`, `ESM_2`, ... | placeholder Online Resource 1 only |
| Related manuscripts | COAP submission guidelines → Additional Information | Authors must discuss related papers; include unpublished related papers when applicable | deferred to `notes/RELATED_MANUSCRIPTS_AUDIT_NEEDED.md` |

## Uncertainties requiring later manual verification

1. Whether COAP Editorial Manager prefers a specific `sn-jnl` reference option other than `sn-mathphys-num` (official COAP examples match numbered Springer style, but the template offers multiple numbered options).
2. Whether ORCID should appear only in the submission portal rather than the manuscript PDF (COAP recommends ORCID at submission; manuscript inclusion not explicitly required).
3. Whether the final supplementary upload must use exact `ESM_1.zip` naming and metadata fields beyond the general SI guidance.
4. Whether a separate title page PDF is required at submission in addition to the main LaTeX/PDF manuscript.
5. Whether the official December 2024 ZIP has changed since the local mirror was captured (re-download should be attempted before final upload).

## Bibliography style decision

- **Document class option:** `sn-mathphys-num`
- **BST file:** `sn-mathphys-num.bst`
- **Rationale:** COAP requires numbered bracket citations; this is the Springer Nature numbered math/physical sciences style provided by the official `sn-jnl` template family.

## Compilation environment

- **Engine used:** Tectonic (LaTeX wrapper available as `~/.local/bin/latexmk` → tectonic)
- **Output:** `paper_coap/main.pdf`
- **Isolation:** compilation uses only files under `paper_coap/`
