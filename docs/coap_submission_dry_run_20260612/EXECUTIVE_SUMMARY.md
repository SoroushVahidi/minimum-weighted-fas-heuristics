# Submission Dry Run — Executive Summary

**Date:** 2026-06-12  
**Journal:** Computational Optimization and Applications (COAP), Springer  
**Manuscript:** SCC-Local Destroy-and-Repair Heuristics for Minimum Weighted Feedback Arc Set on Sparse Digraphs  
**Author:** Soroush Vahidi — sv96@njit.edu — NJIT  
**Repository commit at dry-run completion:** 04ba2c3

---

## Verdict

**SUBMISSION READY — one author action required before submitting**

The upload files, manuscript, cover letter, supplementary artifact, and repository are technically clean. The sole blocker is a policy verification that only the author can confirm: that neither JOCO-D-26-00099 nor DA19469 is currently under active peer review at another journal.

---

## Six upload files (all verified)

| File | SHA-256 (first 16 hex) | Size | Status |
|---|---|---|---|
| Vahidi_COAP_Manuscript.pdf | 97eb61238a81e12e | 2.95 MB | VERIFIED |
| Vahidi_COAP_Cover_Letter.pdf | df6622bd7b19f2ed | 153 KB | VERIFIED |
| Vahidi_COAP_Manuscript_Source.zip | 0fd2b2c138c31798 | 1.10 MB | VERIFIED |
| Vahidi_Online_Resource_1_MWFAS.pdf | 8cc1479fb7aebe9e | 1.75 MB | VERIFIED |
| Vahidi_Online_Resource_1_MWFAS.zip | 5dc3875acad386f9 | 12.0 MB | VERIFIED |
| Vahidi_Related_Manuscripts_Statement.pdf | 7e5ee12c4200ff0a | 87 KB | VERIFIED |

All files located in `paper_coap/submission/final_upload/`.

---

## Test results

- Main test suite: **90 passed, 1 skipped**
- OR1 artifact validation: **PASSED** (after cache cleanup)
- OR1 packaged tests: **79 passed, 7 skipped**

---

## Key facts verified

| Item | Value | Verified |
|---|---|---|
| Abstract word count | 238 words | YES — within 150–250 requirement |
| Keywords | 6 | YES — within 4–6 requirement |
| LaTeX template | sn-jnl.cls (Springer) | YES |
| IPSNS wins / ties / losses (EXP10) | 38 / 55 / 0 | YES — consistent with committed summaries |
| IPSNS best on (EXP4) | 96 of 97 standard instances | YES |
| EXP11 scope | 6 nonneg instances; 0 improved | YES (fixed in commit 04ba2c3) |
| EXP3 exact matches | 56 of 57 | YES |
| AI disclosure | ChatGPT, Codex, Claude, Perplexity AI | YES — in Declarations |
| arXiv preprint | arXiv:2412.16181 — disclosed in manuscript, cover letter, statement | YES |
| JOCO-D-26-00099 disclosed | YES | YES |
| DA19469 disclosed | YES | YES |

---

## The one blocker

The cover letter contains the statement: "I confirm that no substantially overlapping manuscript by me is under consideration elsewhere at the time of submission."

This is accurate only if JOCO-D-26-00099 (LR-TA, Journal of Combinatorial Optimization) and DA19469 (IPSNS, Discrete Applied Mathematics) are not currently under active peer review. The status of these submissions is not derivable from repository files.

**Author action required:** Check both submission records. If either is still under review, amend the cover letter before submitting. If both are withdrawn or rejected, proceed.

---

## Dry-run output files

| File | Purpose |
|---|---|
| REPOSITORY_STATE.md | Phase 1 — repo state at dry-run date |
| UPLOAD_FILE_REGISTER.csv | Phase 2 — 6 files with checksums and designations |
| MANUSCRIPT_UPLOAD_VERIFICATION.md | Phase 3 — manuscript content checks |
| SOURCE_ZIP_VERIFICATION.md | Phase 4 — source ZIP structure |
| ONLINE_RESOURCE_UPLOAD_VERIFICATION.md | Phase 5 — OR1 validation |
| COVER_LETTER_VERIFICATION.md | Phase 6 — cover letter checks |
| RELATED_MANUSCRIPT_VERIFICATION.md | Phase 7 — related items table |
| AUTHOR_CONFIRMATIONS_REQUIRED.md | Phase 8 — 15 items (2 blockers) |
| OFFICIAL_COAP_REQUIREMENTS.csv | Phase 9 — 27 requirements |
| LIVE_PORTAL_FIELD_REGISTER.csv | Phase 10 — 31 portal fields with values |
| SUGGESTED_REVIEWER_REGISTER.csv | Phase 12 — 5 reviewer candidates |
| FILE_DESIGNATION_MAP.csv | Phase 13 — file-to-designation mapping |
| GENERATED_PDF_ORDER_PLAN.md | Phase 14 — review PDF verification plan |
| SUBMISSION_CONSISTENCY_MATRIX.csv | Phase 15 — 24 cross-surface checks |
| FINAL_PORTAL_ISSUE_REGISTER.csv | Phase 16 — 13 issues (1 blocker) |
| STEP_BY_STEP_SUBMISSION_WALKTHROUGH.md | Phase 20 — 32-step portal walkthrough |
| FINAL_SUBMISSION_DRY_RUN_VERDICT.md | Final verdict with all findings |
| audit_metadata.json | Machine-readable dry-run metadata |
| logs/tests.log | pytest -v output |
| logs/or1_validation.log | OR1 validate_artifact.sh output |
| logs/path_and_secret_scan.log | Security scan output (CLEAN) |
| logs/source_zip_build.log | Source ZIP structure verification |

Canonical copy-ready text: `paper_coap/submission/EDITORIAL_MANAGER_FINAL_COPY_READY_TEXT.md`
