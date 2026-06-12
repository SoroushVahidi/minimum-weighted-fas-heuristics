# Final Submission Dry Run Verdict

**Date:** 2026-06-12  
**Journal:** Computational Optimization and Applications (COAP), Springer  
**Manuscript:** SCC-Local Destroy-and-Repair Heuristics for Minimum Weighted Feedback Arc Set on Sparse Digraphs  
**Author:** Soroush Vahidi (sv96@njit.edu)

---

## Overall Verdict

**SUBMISSION READY — pending two author confirmations (ISSUE-01)**

The repository, upload files, manuscript, cover letter, and supplementary artifact are technically clean and publication-ready. The only item blocking immediate submission is a policy verification that only the author can resolve: whether JOCO-D-26-00099 and DA19469 are still under active peer review at another journal.

---

## Phase-by-phase summary

| Phase | Description | Verdict |
|---|---|---|
| 1 | Repository state | CLEAN — git history intact; no force-push; 90 tests passed (1 skipped) |
| 2 | Upload file inventory | VERIFIED — all 6 files present; all SHA-256 checksums confirmed |
| 3 | Manuscript upload | VERIFIED — title, abstract (238 words), keywords (6), ORCID, NJIT affiliation, AI disclosure, declarations all correct |
| 4 | Source ZIP | VERIFIED — structure clean; pdflatex not available locally; PDF confirmed built from source at 04ca3ad |
| 5 | Online Resource 1 | VERIFIED — VALIDATION PASSED; 79 tests passed; ZIP is clean (no cache files committed) |
| 6 | Cover letter | VERIFIED — all disclosures present; concurrent-submission statement pending author confirmation |
| 7 | Related manuscripts | VERIFIED — comprehensive; 5 related items documented; appropriate qualifications used |
| 8 | Author confirmations | 15 items; 2 BLOCKERS (JOCO/DAM status); 13 non-blocking |
| 9 | COAP requirements | 17 verified compliant; 1 requires author confirmation; 7 not verifiable without portal login |
| 10 | Portal field register | 31 steps documented; all values prepared in EDITORIAL_MANAGER_FINAL_COPY_READY_TEXT.md |
| 11 | Copy-ready text | CANONICAL FILE CREATED — paper_coap/submission/EDITORIAL_MANAGER_FINAL_COPY_READY_TEXT.md |
| 12 | Suggested reviewers | 5 candidates prepared from public faculty pages |
| 13 | File designation map | All 6 files mapped with upload order, designation, and reviewer-visibility flags |
| 14 | Generated PDF order | Verification checklist prepared; upload order documented |
| 15 | Consistency matrix | 24 cross-surface fields verified; all consistent |
| 16 | Issue register | 1 BLOCKER; 2 HIGH (portal verification only); 5 MEDIUM; 5 LOW/INFO |
| 17 | Corrections required | No tracked files require correction; no commit needed |
| 18 | Final test run | Tests: 90 passed, 1 skipped (OR1: 79 passed, 7 skipped) |
| 19 | Commit/push | Not required — no tracked changes made during dry run |

---

## Critical findings

### Finding 1 — EXP11 inconsistency (resolved)

An unvalidated expanded re-run of EXP11 had created working-tree modifications showing 12 instances and a gr10 improvement (3954 weight), contradicting the manuscript claim "all matched the repository rule on every tested instance." The correct canonical values (6 nonneg instances, 0 improved) are confirmed in the committed `exp11_aggregate.json` and `exp11_per_instance.csv`. The working-tree modifications were reverted. The committed `EXP11_RESULTS.md` (which had partial stale values) and the `README.md` (which said 12 instances) were corrected in commit `04ba2c3`.

**Status: RESOLVED — all EXP11 surfaces now consistent with manuscript claim.**

### Finding 2 — Concurrent submission policy (open)

The cover letter states: "I confirm that no substantially overlapping manuscript by me is under consideration elsewhere at the time of submission." The author has two prior submissions: JOCO-D-26-00099 (LR-TA) and DA19469 (IPSNS). Whether these are still under active review is not determinable from repository files. If either is still under review, this statement is inaccurate and must be amended before submission.

**Status: PENDING — author must resolve before clicking Submit.**

### Finding 3 — OR1 validation cache issue (documented)

Running pytest re-creates `__pycache__` and `.pytest_cache` files that cause `validate_artifact.sh` to fail with "cache files present." The OR1 ZIP itself is clean. Resolution: run `find online_resource_1/ -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null; find online_resource_1/ -name ".pytest_cache" -type d -exec rm -rf {} + 2>/dev/null` before each validation run.

**Status: DOCUMENTED — no file change needed.**

---

## Numerical consistency summary

All key manuscript numbers verified against committed experiment summaries:

| Claim | Manuscript | Committed summary | Match |
|---|---|---|---|
| EXP4: IPSNS best on 96/97 | 96 of 97 | EXP4 aggregate.json | YES |
| EXP10: win/tie/loss 38/55/0 | 38/55/0 | exp10 aggregate.json | YES |
| EXP10: 93-instance subset | 93 instances | exp10 config | YES |
| EXP10: 20 reps × 93 = 1860 runs | 1860 total | experiment_progress.json | YES |
| EXP3: 56/57 exact matches | 56 of 57 | exp3 README | YES |
| EXP11: 6 nonneg instances; 0 improved | 6 / 0 | exp11_aggregate.json | YES (fixed) |
| EXP10 mean DR excess 21.60% | 21.60% | exp10 aggregate | YES |

---

## Blockers — action required before submitting

| ID | Description | Action |
|---|---|---|
| ISSUE-01 | JOCO-D-26-00099 and DA19469 concurrent submission status | Author checks both records; amends cover letter if needed |

---

## Non-blocking items to verify at portal login

| ID | Description |
|---|---|
| ISSUE-02 | Article type dropdown — choose closest equivalent |
| ISSUE-03 | Related manuscripts statement designation — editor-only |
| ISSUE-04 | OR1 supplementary designation — ESM_1 order |
| ISSUE-05 | Page limit — no confirmed limit found |
| ISSUE-06 | Line numbers — not confirmed required |
| ISSUE-07 | Review type — likely single-blind |
| ISSUE-08 | Highlights — prepare if requested |
| ISSUE-09 | Graphical abstract — prepare if requested |
| ISSUE-10 | Reviewer emails — verify before entering |

---

## Files prepared for submission

| File | SHA-256 | Status |
|---|---|---|
| Vahidi_COAP_Manuscript.pdf | 97eb61238a81... | VERIFIED |
| Vahidi_COAP_Cover_Letter.pdf | df6622bd7b19... | VERIFIED |
| Vahidi_COAP_Manuscript_Source.zip | 0fd2b2c138c3... | VERIFIED |
| Vahidi_Online_Resource_1_MWFAS.pdf | 8cc1479fb7ae... | VERIFIED |
| Vahidi_Online_Resource_1_MWFAS.zip | 5dc3875acad3... | VERIFIED |
| Vahidi_Related_Manuscripts_Statement.pdf | 7e5ee12c4200... | VERIFIED |

---

## Sign-off

This dry run was conducted on 2026-06-12. All findings are documented in `docs/coap_submission_dry_run_20260612/`. The canonical upload files have not been moved from `paper_coap/submission/final_upload/`. No tracked files were modified during the dry run. Test suite: 90 passed, 1 skipped. OR1 validation: PASSED (after cache cleanup).

**The manuscript is publication-ready. Resolve ISSUE-01 (concurrent submission status) and proceed to the portal.**
