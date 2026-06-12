# Executive Summary: Related Manuscript Status Resolution

**Date:** 2026-06-12  
**Author:** Soroush Vahidi  
**Task:** Task 4 — COAP Related Manuscript Status Resolution

---

## What this audit did

Established controlled-vocabulary statuses for all five related manuscripts and preprints; analyzed concurrent-submission compliance; verified all disclosure surfaces; made one factual correction (Eduardo Uchoa reviewer email); created 14 required output documents.

---

## Audit verdict: STATUS_EVIDENCE_INSUFFICIENT

No rank 1–6 documentary evidence (decision emails, portal status, withdrawal letters) is available for the four journal submissions (JOCO-D-26-00099, DA19469, CAIE, EJCO). All statuses must be marked STATUS_UNVERIFIED from a formal-audit standpoint.

**This does not block submission.** The concurrent-submission declaration in the cover letter is the author's personal attestation, and this audit found no evidence contradicting it.

---

## Related item statuses

| Item | Status | Confidence | Risk |
|---|---|---|---|
| arXiv:2412.16181 | PREPRINT_ONLY | HIGH | NONE — preprints are not journal submissions |
| JOCO-D-26-00099 | STATUS_UNVERIFIED | LOW for outcome | LOW if confirmed inactive (inferred REJECTED) |
| DA19469 | STATUS_UNVERIFIED | LOW for outcome | LOW if confirmed inactive (inferred REJECTED) |
| CAIE package | STATUS_UNVERIFIED | Moderate for submission, low for outcome | LOW if confirmed inactive (probable rejection or withdrawal) |
| EJCO package | STATUS_UNVERIFIED | LOW for formal submission | LOW if never formally submitted |

---

## Disclosure surfaces: no changes required

The current cover letter, related-manuscript statement, and §2 are factually accurate and defensible. No new confirmed facts emerged that would require disclosure text to be corrected. All five related items are disclosed. Hedging language for JOCO, DAM, CAIE, and EJCO is appropriate given the absence of rank 1–6 evidence in this repository.

---

## One factual correction made

**Eduardo Uchoa (suggested reviewer) email corrected:**
- From: `eduardo_uchoa@id.uff.br`
- To: `uchoa@producao.uff.br`

This applies to `EDITORIAL_MANAGER_FINAL_COPY_READY_TEXT.md`, `FINAL_REVIEWER_RECOMMENDATIONS.csv`, and `AUTHOR_PRE_SUBMISSION_CONFIRMATION.md`. Upload artifacts are not affected.

---

## Upload artifacts: unchanged

All six upload artifacts have SHA-256 checksums identical to the Task 3 freeze manifest. No artifacts were regenerated. The tag `coap-submission-ready-2026-06-12` on commit `e1c27c74b1e0ec9001eee189b8ae4dc05ee374f9` remains valid.

---

## Validation: passed

- Main test suite: 90 passed, 1 skipped
- OR1 pytest (Task 3): 79 passed, 7 skipped (unchanged)
- All upload checksums match frozen manifest

---

## Required author actions

1. **JOCO-D-26-00099** — check submission system; confirm inactive.
2. **DA19469** — check submission system; confirm inactive. *(highest-priority check: IPSNS is the primary COAP contribution)*
3. **CAIE** — confirm from email/memory whether submitted and outcome.
4. **EJCO** — confirm whether formally submitted.
5. **Eduardo Uchoa email** — verify `uchoa@producao.uff.br` is active before entering in portal.
6. **Complete AUTHOR_PRE_SUBMISSION_CONFIRMATION.md** — check every box.
7. **Follow STEP_BY_STEP_SUBMISSION_WALKTHROUGH.md** — upload six files; record manuscript number.

---

## Files produced by this audit

| File | Purpose |
|---|---|
| EVIDENCE_METHOD.md | Evidence hierarchy; what was and was not found |
| RELATED_ITEM_STATUS_MATRIX.csv | Controlled-vocabulary status matrix for all 5 items |
| CONCURRENT_SUBMISSION_COMPLIANCE.md | Per-component overlap analysis; per-item risk tables |
| SUBMISSION_DECISION.md | Formal verdict (STATUS_EVIDENCE_INSUFFICIENT) + path to SUBMIT_NOW |
| DISCLOSURE_SURFACE_REGISTER.csv | All disclosure surfaces; change-required column |
| DISCLOSURE_CHANGE_LOG.md | Changes made (one email correction; no disclosure changes) |
| FINAL_SUGGESTED_REVIEWERS.csv | Corrected reviewer list with Uchoa email fix |
| UPLOAD_ARTIFACT_STATUS.md | Checksum verification; unchanged verdict |
| CONFIDENTIAL_EVIDENCE_EXCLUSION_CHECK.md | Verified no confidential material committed |
| VALIDATION_RESULTS.md | Test results and artifact verification |
| FINAL_AUTHOR_ACTIONS.md | Step-by-step personal actions required from author |
| REPOSITORY_STATE.md | Git state; what was and was not changed |
| EXECUTIVE_SUMMARY.md | This file |
| audit_metadata.json | Machine-readable audit record |
