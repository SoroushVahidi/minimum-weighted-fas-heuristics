# Manuscript Structure Audit (`paper_coap/`)

**PDF:** `paper_coap/main.pdf` — **45 pages**  
**SHA-256 (submit copy):** `97eb61238a81e12e2597a6963926f0f092ad994f3f369b89715f36e9e06d0898`  
**HEAD:** `6c04ff1`

## Directory structure

| Area | Files | Role |
|---|---|---|
| `main.tex` | 1 | Document root, abstract, keywords |
| `sections/01–08` | 8 | Introduction through conclusion |
| `sections/04_algorithmic_framework.tex` | | LR-TA, WMSF, IPSNS, pseudocode |
| `sections/04_formal_analysis.tex` | | Propositions (proofs in OR1) |
| `tables/` | 16 | `\input` tables |
| `figures/` | 6 PDF + 1 TikZ | Figures |
| `bibliography/references.bib` | 29 entries | Numbered sn-mathphys-num |
| `declarations/` | statements | COAP required declarations |
| `submission/` | cover letter, related stmt, final_upload | Portal package |
| `template_reference/` | sn-jnl archive | Official template reference |
| `notes/` | COAP migration audits | Internal; not in source ZIP |

## Metadata consistency

| Field | Status |
|---|---|
| Title | Matches submission files |
| Running title | `SCC-Local Heuristics for MWFAS on Sparse Digraphs` |
| Abstract | **238 words** (post 6c04ff1 trim) |
| Keywords | 6 keywords |
| Author | Soroush Vahidi; ORCID linked |
| Affiliation | NJIT |
| Article class | `sn-jnl` `sn-mathphys-num` |

## Contribution hierarchy

1. **IPSNS** — primary novel integration (introduction bullet 1, title).
2. **LR-TA** — inherited/engineered seed (not new literature claim).
3. **WMSF-style** — adapted seed from CC25.
4. Experimental program — supporting evidence.

**Verified** in abstract, §1, §2.1, §4, conclusion.

## Notation and acronyms

MWFAS, SCC, IPSNS, LR-TA defined at first use. Objective: backward weight `bw(π)` vs removed set `w(F)` — central §3 distinction.

## Formulas

**12** `\begin{equation}` blocks with **12** `\label{eq:…}` — all displayed equations numbered.

## Internal comments (not blocking)

Three `% AUTHOR-STATUS:` comments in `02_related_work.tex` — editor-facing confirmation reminders; not visible as placeholders in PDF.

## Unused / orphan files

| File | Status |
|---|---|
| `tables/table_runtime_quality_tradeoff.tex` | **Not included** in main PDF |
| `supplementary/README.md` | Placeholder note; OR1 is external |
| `notes/*` | Excluded from source ZIP by design |

## Build

Engine: Tectonic. Build warnings: underfull vbox (cosmetic). No missing references in last successful build at 6c04ff1.

## Declarations

Funding (none), COI (none), data/code (OR1), AI disclosure (ChatGPT/Codex/Claude/Perplexity listed), author contributions — present in `declarations/statements_and_declarations.tex`.

## Related-manuscript disclosure

arXiv:2412.16181; JOCO-D-26-00099; DA19469; CAIE/EJCO prepared packages — consistent with cover letter and related-manuscript PDF.

## Verdict

Manuscript tree is **complete, internally consistent, and submission-aligned** at HEAD. See `MANUSCRIPT_FILE_REGISTER.csv` and `FIGURE_TABLE_REGISTER.csv` for file-level detail.
