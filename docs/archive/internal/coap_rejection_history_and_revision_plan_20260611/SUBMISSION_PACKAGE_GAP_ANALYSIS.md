# Submission Package Gap Analysis

**Audit date:** 2026-06-11  
**Authority:** `docs/final_branch_audit_20260611/COAP_COMPLIANCE_AUDIT.md`

Status codes: **Ready | Needs revision | Missing | Not required | Waiting on EXP10 | Waiting on holdout**

---

| Item | Status | Notes / path |
|------|--------|--------------|
| Final manuscript LaTeX source | **Needs revision** | `paper_coap/` — disclosure + EXP10 + holdout pending |
| Final manuscript PDF | **Needs revision** | `paper_coap/main.pdf` exists; rebuild after edits |
| Online Resource 1 / supplementary ZIP | **Missing** | EJCO artifact stale: `submission_package/ejco_reproducibility_artifact/` |
| Reproducibility README | **Missing** | COAP-targeted REPRODUCE.md not created |
| Environment specification | **Needs revision** | `requirements.txt` unpinned (M-03) |
| Pinned dependencies | **Missing** | Add version pins + Python version comment |
| Raw result availability | **Ready** | Committed summaries in `experiments/exp*/summary/` |
| Automated tests | **Missing** | B-02 blocker: zero tests |
| Cover letter | **Needs revision** | `paper/cover_letter_draft.tex` is EJCO; CAIE PDF outdated |
| Related-manuscript disclosure | **Missing** | No arXiv/JOCO/DAM in manuscript or uploads |
| Predecessor PDFs for portal | **Missing** | Archives exist; upload bundle not prepared |
| Overlap matrix | **Needs revision** | Draft in `RELATED_MANUSCRIPT_CONTRIBUTION_MATRIX.md`; not submission-ready PDF |
| Reviewer suggestions | **Missing** | Not found for COAP |
| Declarations (funding, COI, CRediT, AI) | **Ready** | `paper_coap/declarations/statements_and_declarations.tex` |
| Author contributions | **Ready** | Single-author CRediT complete |
| Funding | **Ready** | No specific funding stated |
| Conflict of interest | **Ready** | None declared |
| Code/data availability statement | **Needs revision** | Promises OR1 not yet delivered |
| AI disclosure | **Ready** | Lists tools used |
| ORCID | **Ready** | In author macro |
| Figure files | **Ready** | `paper_coap/figures/` TikZ |
| Table files | **Ready** | `paper_coap/tables/` — may consolidate |
| Graphical abstract | **Not required** | COAP compliance audit: not mandatory |
| Highlights | **Needs revision** | `submission_files_for_download/highlights.txt` — verify vs COAP abstract |
| Title page (separate) | **Needs revision** | EJCO/CAIE era; regenerate for COAP |
| Anonymized PDF | **Needs revision** | Not verified current for COAP |
| DRMacIver binary checksum | **Missing** | M-04: add SHA256 to OR1 |
| EXP10 results in package | **Waiting on EXP10** | ~21% DRMacIver at audit |
| Holdout summary in package | **Waiting on holdout** | 1290 runs exist; postprocess pending |
| HiGHS citation in bib | **Needs revision** | MIN-04: verify `bibliography/references.bib` |
| sfas baseline documentation | **Needs revision** | P-01 unresolved |
| Git commit hygiene | **Needs revision** | ipsns.py diagnostics uncommitted; EXP10 untracked |
| Public repository / DOI | **Missing** | Private repo per audits |
| Response to reviewers | **Not required** | New submission to COAP |
| LaTeX class files for editorial | **Ready** | `sn-jnl.cls`, bst in `paper_coap/template_reference/` |

---

## Blockers for upload (P1)

1. Online Resource 1
2. Cover letter with accurate disclosure
3. Related manuscript portal uploads
4. EXP10 integration
5. Smoke tests (strongly tied to reproducibility claim)

---

## Items ready today (no EXP10 dependency)

- Declarations block
- Core algorithm source in `src/mwfas/`
- EXP1–EXP9 summary CSVs/JSONs
- COAP template compliance
- Scientific manuscript body (pending disclosure edits)

---

## Stale packages — do not submit

| Package | Path | Issue |
|---------|------|-------|
| EJCO source | `submission_package/ejco_source/` | Wrong journal; pre-holdout/EXP10 |
| EJCO artifact | `submission_package/ejco_reproducibility_artifact/` | EJCO paths; missing EXP10 |
| CAIE upload PDFs | gitignored `submission_package/files_for_upload/` | Wrong venue; 44 pp draft |
| Anonymous artifact | `submission_package/anonymous_artifact/` | EJCO-era |

---

## Recommended Online Resource 1 structure

```
Online_Resource_1/
  README.md                 # COAP context, cite paper, env setup
  REPRODUCE.md               # Minimal reproduction commands
  requirements-pinned.txt
  src/                       # mwfas package
  experiments/               # Scripts + configs + summary/ only (not full raw)
  exp10/                     # Stochastic robustness summaries
  holdout/                   # Holdout summary
  external/
    drmaciver_fas            # + SHA256SUMS
  proofs/                    # Full Prop proofs
  overlap_matrix.pdf         # Predecessor disclosure
  MANIFEST.json
  LICENSE
```
