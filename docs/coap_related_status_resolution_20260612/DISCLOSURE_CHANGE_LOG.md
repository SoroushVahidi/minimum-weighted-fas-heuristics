# Disclosure Change Log

**Date:** 2026-06-12  
**Audit:** Task 4 — Related Manuscript Status Resolution

---

## Summary of changes to disclosure surfaces

**No substantive changes were made to any disclosure surface.**

The current cover letter, related-manuscript statement, and §2 are factually accurate and defensible based on all available evidence. No new confirmed facts emerged from this audit that would require a factual correction to any disclosure.

---

## Changes made

### 1. Eduardo Uchoa email domain correction

**File:** `paper_coap/submission/EDITORIAL_MANAGER_FINAL_COPY_READY_TEXT.md`  
**Also:** `docs/coap_submission_freeze_20260612/FINAL_REVIEWER_RECOMMENDATIONS.csv`

**Change:** `eduardo_uchoa@id.uff.br` → `uchoa@producao.uff.br`

**Justification:** Web search during Task 2 dry run identified the correct domain for Eduardo Uchoa (Fluminense Federal University, Department of Production Engineering). The `id.uff.br` domain is the university-wide ID system; the research email uses the departmental `producao.uff.br` domain. This is a factual correction to suggested-reviewer contact information — not a disclosure surface for related manuscripts.

**Impact on disclosure:** None. This correction does not affect any related-manuscript disclosure surface.

---

## No changes to

| Surface | Reason no change required |
|---|---|
| `cover_letter.tex` | Text is factually accurate; concurrent-submission declaration is author attestation; no contradicting evidence found |
| `related_manuscripts_statement.tex` | All five items are disclosed; hedging language is accurate for repository-unverified statuses; no new confirmed facts |
| `paper_coap/main.tex` (§2) | Technical lineage disclosure is accurate; no new algorithm or result claims; no confirmed facts changed |
| Upload artifacts (PDFs, ZIPs) | No source text changed; rebuilding would change checksums; checksums must remain consistent with frozen manifests |

---

## Optional future updates (not required for submission)

If the author confirms JOCO-D-26-00099 and DA19469 are both rejected, and CAIE/EJCO are inactive, the related-manuscript statement *may* be updated to reflect confirmed statuses (e.g., changing "editorial outcome documented in author records, not reproduced here" to "received rejection decision; details documented in author records"). This is optional — the current wording is defensible as-is.

**Such an update would require:**
1. Author to confirm status with rank 1–6 evidence
2. Retypeset related-manuscript statement PDF
3. SHA-256 update to SUBMISSION_FREEZE.sha256
4. Update to SUBMISSION_FREEZE.json
5. New commit and push
6. Tag `coap-submission-ready-2026-06-12` would no longer point to the live HEAD — author to decide whether to move or add a new tag

**Recommendation:** Do not make optional disclosure updates unless the author has a compelling reason. The current wording is accurate and compliant. Reopening frozen artifacts introduces re-validation work.
