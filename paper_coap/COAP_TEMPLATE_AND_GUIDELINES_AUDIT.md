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
| Official download URL (pass 2) | `https://cms-resources.apps.public.k8s.springernature.io/springer-cms/rest/v1/content/18782940/data/v12` |
| Access date | 2026-06-10 |
| Archive filename | `template_reference/sn-jnl-official-dec2024.zip` |
| Archive size | 901,814 bytes |
| Archive SHA-256 | `812e76dcaa9c28dc1bff1fb6065d51729b67d4ea140552a05088317414a3ecae` |
| Package date in ZIP | 2024-12-12 |
| Template version string | **Version 3.1 December 2024** (`template_reference/sn-article.tex`) |
| Class file | `sn-jnl.cls` (55,857 bytes; SHA-256 `36d0c3273a59d48dc6a9c7b080dfa1ec50dc10229d8751568d1f2e490ffa5ecc`) |
| Bibliography styles included | `sn-apacite.bst`, `sn-aps.bst`, `sn-basic.bst`, `sn-chicago.bst`, `sn-mathphys-ay.bst`, `sn-mathphys-num.bst`, `sn-nature.bst`, `sn-vancouver-ay.bst`, `sn-vancouver-num.bst` (under `bst/` in archive; copied to `paper_coap/` root for compilation) |
| Other bundled assets | `sn-article.tex`, `sn-article.pdf`, `sn-bibliography.bib`, `user-manual.pdf`, `empty.eps`, `fig.eps` |
| `Orcidlogo.eps` | **Not included** in the official December 2024 ZIP despite `\orcid{}` macro referencing it |

### Pass 1 fallback (superseded for active class files)

| Item | Value |
|---|---|
| Pass 1 CMS URL attempted | `https://resource-cms.springernature.com/springer-cms/rest/v1/content/19238648/data/v3` → **404** |
| Pass 1 fallback mirror | `SoroushVahidi/frontier-allocation-for-budgeted-llm-inference/paper_ml_journal_snjnl_stage/` |
| Pass 1 archived mirror | `template_reference/sn-jnl-template-v3.1-dec2024-local-mirror.zip` (SHA-256 `c65e718f...`) |

**Pass 2 action:** synchronized `paper_coap/sn-jnl.cls` and all `.bst` files from the official December 2024 ZIP. Byte comparison showed the pass-1 active class differed from the official file; the official copy is now authoritative in `paper_coap/`.

**ORCID note:** because the official package omits `Orcidlogo.eps`, `main.tex` uses a superscript linked textual ORCID via a local `\orcid{}` redefinition.

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
5. Whether the official December 2024 ZIP has changed since pass 1 — **resolved in pass 2** via successful official download; re-check before final upload if Springer updates the package again.

## Bibliography style decision

- **Document class option:** `sn-mathphys-num`
- **BST file:** `sn-mathphys-num.bst`
- **Rationale:** COAP requires numbered bracket citations; this is the Springer Nature numbered math/physical sciences style provided by the official `sn-jnl` template family.

## Compilation environment

- **Engine used:** Tectonic (LaTeX wrapper available as `~/.local/bin/latexmk` → tectonic)
- **Output:** `paper_coap/main.pdf`
- **Isolation:** compilation uses only files under `paper_coap/`
