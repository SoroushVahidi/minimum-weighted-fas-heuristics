# Submission Freeze — Executive Summary

**Date:** 2026-06-12  
**Journal:** Computational Optimization and Applications (COAP), Springer  
**Manuscript:** SCC-Local Destroy-and-Repair Heuristics for Minimum Weighted Feedback Arc Set on Sparse Digraphs  
**Author:** Soroush Vahidi — sv96@njit.edu — NJIT  
**Repository commit at freeze start:** `af34d57d3a921c1be50a61f990c2d85ff8d97df3`

---

## Verdict

**SUBMISSION READY — one author confirmation required**

The repository, upload files, manuscript, test suite, and supplementary artifact are validated and frozen. The only remaining action before portal submission is the author confirming that neither JOCO-D-26-00099 nor DA19469 is currently under active peer review, which would make the concurrent-submission cover-letter declaration accurate.

---

## Git state reconciliation

| Question | Answer |
|---|---|
| Starting HEAD | `af34d57d3a921c1be50a61f990c2d85ff8d97df3` |
| origin/main | `af34d57d3a921c1be50a61f990c2d85ff8d97df3` |
| Local = Remote | YES |
| Relationship 04ba2c3 vs af34d57 | `04ba2c3` is an ancestor of `af34d57`; no conflict |
| Any commit missing or lost | NO |
| History intact | YES |

The dry-run report cited `04ba2c3` because that was HEAD at the start of that session. `af34d57` was committed afterward (maintenance summary update) in the same cleanup pass. Both are in the correct linear history.

---

## Six upload files — all verified

| File | SHA-256 (first 16) | Bytes | Status |
|---|---|---|---|
| Vahidi_COAP_Manuscript.pdf | 97eb61238a81e12e | 333,157 | OK |
| Vahidi_COAP_Cover_Letter.pdf | df6622bd7b19f2ed | 24,732 | OK |
| Vahidi_COAP_Manuscript_Source.zip | 0fd2b2c138c31798 | 145,760 | OK |
| Vahidi_Online_Resource_1_MWFAS.pdf | 8cc1479fb7aebe9e | 130,236 | OK |
| Vahidi_Online_Resource_1_MWFAS.zip | 5dc3875acad386f9 | 1,116,197 | OK |
| Vahidi_Related_Manuscripts_Statement.pdf | 7e5ee12c4200ff0a | 22,804 | OK |

No artifact was regenerated. All checksums match MANIFEST.sha256.

---

## Validation

| Check | Result |
|---|---|
| Main tests | 90 passed, 1 skipped |
| OR1 validation | PASSED |
| OR1 packaged tests | 79 passed, 7 skipped |
| Upload checksums (6/6) | ALL OK |
| Security scan | CLEAN |
| Abstract word count | 238 (within 150–250) |
| Keywords | 6 (within 4–6) |
| No local paths in publication-facing files | CONFIRMED |

---

## Reviewer screening

All 5 proposed reviewers confirmed at current institutions via public sources:

| Name | Institution | Relevant expertise |
|---|---|---|
| Kathrin Hanauer | University of Vienna | Graph algorithms, FAS — most directly relevant |
| Petra Mutzel | University of Bonn | Combinatorial optimization, algorithm engineering |
| Giuseppe Lancia | University of Udine | Combinatorial optimization, ILP |
| Eduardo Uchoa | Univ. Federal Fluminense | Exact/heuristic methods — **email needs live verification** |
| Ivana Ljubic | ESSEC Business School | Network design, combinatorial optimization |

Name note: task instructions listed "Martin Hanauer" — the correct name is **Kathrin Hanauer** (confirmed by University of Vienna public profile and DBLP). No reviewers removed.

No apparent conflicts found from public record inspection. Author verification is still required before entering names in the portal.

---

## Concurrent submission

The cover-letter declaration requires confirmation that JOCO-D-26-00099 and DA19469 are not currently under active peer review. See `CONCURRENT_SUBMISSION_DECISION_TREE.md` for all four cases (A: both inactive → proceed; B: one active, no substantial overlap → disclose and verify policy; C: one active, substantial overlap → do not proceed; D: status unknown → verify first).

---

## What was committed

32 new files + 1 .gitignore modification:
- Dry-run documentation (19 files in `docs/coap_submission_dry_run_20260612/`)
- Freeze documentation (11 files in `docs/coap_submission_freeze_20260612/`)
- Canonical portal text (updated with confirmation gates)
- Author pre-submission checklist
- Freeze manifest (JSON + SHA-256)

No scientific results, algorithms, manuscript body, or upload binaries were changed.

---

## Tag

Annotated tag `coap-submission-ready-2026-06-12` applied to the freeze commit.

---

## Next action for author

1. Check JOCO-D-26-00099 status in submission system
2. Check DA19469 status in submission system
3. If both inactive: open https://www.editorialmanager.com/coap and follow `STEP_BY_STEP_SUBMISSION_WALKTHROUGH.md`
4. Sign off `AUTHOR_PRE_SUBMISSION_CONFIRMATION.md` before clicking Submit
