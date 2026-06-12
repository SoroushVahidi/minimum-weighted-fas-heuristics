# COAP Compliance Audit

**Audit date:** 2026-06-10  
**Reference:** `paper_coap/COAP_TEMPLATE_AND_GUIDELINES_AUDIT.md`

## Met requirements (with evidence)

| Requirement | Status | Evidence |
|---|---|---|
| Springer `sn-jnl` class | Met | `paper_coap/sn-jnl.cls`, template v3.1 Dec 2024 |
| Numbered references | Met | `sn-mathphys-num.bst` |
| Abstract 150–250 words | Met | Compile audit / PDF text extraction |
| Keywords 4–6 | Met | Six keywords in PDF |
| Max three heading levels | Met | Section structure |
| Statements and Declarations | Met | `declarations/statements_and_declarations.tex` |
| AI disclosure | Met | Declarations section |
| Data/code availability statement | Partial | References Online Resource 1 placeholder |
| Author ORCID | Met | Textual ORCID link (official `Orcidlogo.eps` absent from template ZIP) |
| Algorithm environments | Met | PDF contains Algorithm blocks |
| Theorem/proposition envs | Met | Added in `92e9c5a` pass |

## Unmet or uncertain

| Requirement | Status | Action |
|---|---|---|
| **Related manuscripts disclosure** | **Unmet** | `notes/RELATED_MANUSCRIPTS_AUDIT_NEEDED.md` deferred |
| **ESM_1.zip supplementary** | **Missing** | Placeholder citation only |
| COAP submission package | **Missing** | Only EJCO package in `submission_package/` |
| Cover letter (COAP) | **Missing** | EJCO cover letter exists |
| Suggested reviewers | **Unknown** | Not found for COAP |
| Title page PDF separate? | **Uncertain** | Manual portal check |
| Final ORCID in portal vs PDF | **Uncertain** | Both may be needed |
| Acknowledgments | N/A | None in source |
| Funding statement | Check declarations | Verify completeness |
| Related unpublished uploads | **Not prepared** | DAM/OPSEARCH/predecessor versions |
| Source ZIP for Editorial Manager | **Not packaged for COAP** | `paper_coap/` exists but no upload manifest |
| Anonymized vs author-visible | Author-visible | OK for COAP (not double-blind) |

## File completeness (`paper_coap/`)

| Asset | Present |
|---|---|
| `main.tex` | Yes |
| `main.pdf` | Yes (40 pp) |
| `references.bib` | Yes |
| `sn-jnl.cls`, `.bst` files | Yes |
| Figures (EXP4–6 PDFs) | Yes in `figures/` |
| Framework figure (TikZ) | Yes |
| Supplementary TeX | Placeholder only |

## Stale COAP/EJCO confusion risk

| Path | Venue |
|---|---|
| `paper_coap/` | **COAP (current)** |
| `paper/`, `submission_package/ejco_*` | **EJCO/CAIE (historical)** |

Uploading EJCO PDF or artifact to COAP would be **unsafe**.

## Online Resource 1

Manuscript cites future `ESM_1.zip`. Must contain: code, configs, committed summaries, environment pins, reproduction commands, licenses — **not yet built for COAP branding**.
