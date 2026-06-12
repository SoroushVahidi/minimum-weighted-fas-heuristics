# Executive Summary: Final Author Status Gate

**Date:** 2026-06-12  
**Task:** Apply author-confirmed rejection statuses for all prior journal submissions and finalize the COAP submission package.

---

## Verdict

**SUBMIT NOW.**

All four prior journal submissions have been author-confirmed rejected and are no longer under consideration. The concurrent-submission declaration in the cover letter is factually accurate. All disclosure surfaces are consistent with confirmed statuses. All upload artifacts have been rebuilt and validated. The submission package is ready for portal entry.

---

## Confirmed statuses

| Item | Confirmed status | Currently active? |
|---|---|---|
| arXiv:2412.16181 | PREPRINT_ONLY | N/A (public preprint, not a journal submission) |
| JOCO-D-26-00099 | REJECTED | No |
| DA19469 | REJECTED | No |
| CAIE submission | REJECTED | No |
| EJCO submission | REJECTED | No |

---

## Changes made

**Manuscript §2 (`sections/02_related_work.tex`):**
- LR-TA paragraph: added "submitted to the Journal of Combinatorial Optimization as JOCO-D-26-00099; rejected" inline; removed AUTHOR-STATUS comment.
- DAM paragraph: added "submitted to Discrete Applied Mathematics as DA19469; rejected" inline; removed AUTHOR-STATUS comment.
- CAIE/EJCO paragraph: replaced "package prepared; submission history must be disclosed separately" with "submitted to CAIE and EJCO; both rejected and no longer under consideration"; removed AUTHOR-STATUS comment.

**Declarations (`declarations/statements_and_declarations.tex`):**
- Related-manuscripts subsection: updated to state all four prior submissions with venues and confirmed rejected status; removed "will be disclosed where author records are complete."

**Cover letter (`submission/cover_letter.tex`):**
- Related manuscripts paragraph: added "and was rejected" to JOCO and DAM; replaced "Repository packages were also prepared for CAIE/EJCO" with explicit submission and rejection statements for both; added "None of these four prior journal submissions is currently under consideration."

**Related-manuscript statement (`submission/related_manuscripts_statement.tex`):**
- JOCO: "editorial outcome documented in author records, not reproduced here" → "rejected; no longer under consideration"
- DAM: same → "rejected; no longer under consideration"
- CAIE: "package prepared; whether submitted is recorded in author logs" → "submitted to Computers & Industrial Engineering; rejected; no longer under consideration"
- EJCO: "package prepared; outcome if any is recorded in author logs" → "submitted to EURO Journal on Computational Optimization; rejected; no longer under consideration"
- Summary table added.

**Portal copy-ready text (`EDITORIAL_MANAGER_FINAL_COPY_READY_TEXT.md`):**
- Gate block replaced with "CLEARED FOR COAP SUBMISSION" header listing all four confirmed rejected.
- Related work field replaced with confirmed portal text.
- Warning notes about JOCO/DAM status removed.

**Author checklist (`AUTHOR_PRE_SUBMISSION_CONFIRMATION.md`):**
- "SUBMISSION STATUS: CLEARED FOR COAP SUBMISSION" header added.
- Blocker checkboxes replaced with confirmed repository records.

---

## Rebuilt artifacts

Four upload artifacts were rebuilt due to source changes:

| Artifact | Old SHA-256 | New SHA-256 |
|---|---|---|
| Vahidi_COAP_Cover_Letter.pdf | `df6622bd...` | `b0fd9d0a...` |
| Vahidi_COAP_Manuscript.pdf | `97eb6123...` | `13aec51a...` |
| Vahidi_COAP_Manuscript_Source.zip | `0fd2b2c1...` | `ed198a71...` |
| Vahidi_Related_Manuscripts_Statement.pdf | `7e5ee12c...` | `9af3b73e...` |

OR1 PDF and OR1 ZIP unchanged.

---

## Validation

- Test suite: **90 passed, 1 skipped** — no regressions.
- All PDFs open correctly (%PDF- header verified).
- No unresolved-status language found in any source file.
- No numerical results changed.
- No algorithm code changed.
- No confidential material committed.
- MANIFEST.sha256, SUBMISSION_FREEZE.json, SUBMISSION_FREEZE.sha256 all updated.
- v2 tag `coap-submission-ready-2026-06-12-v2` applied after CI passes.
