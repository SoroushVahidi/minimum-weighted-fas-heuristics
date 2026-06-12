# Author Confirmations Required

**Date:** 2026-06-12  
**Purpose:** Facts that cannot be determined from repository files and require author verification before or during portal submission.

---

## BLOCKER confirmations (must know before submitting)

### 1. JOCO-D-26-00099 current status

**Question:** What is the current status of the LR-TA manuscript submitted to the Journal of Combinatorial Optimization (JOCO-D-26-00099)?

Options: Under review / Rejected / Withdrawn / Accepted

**Why this matters:** The cover letter states "no substantially overlapping manuscript by me is under consideration elsewhere at the time of submission." If JOCO-D-26-00099 is still under review, the cover letter requires amendment (remove or qualify the statement) or the submission requires disclosure as a concurrent submission. COAP editors may ask.

**Action:** Confirm status. If rejected or withdrawn, no change needed. If under review, amend cover letter.

### 2. DA19469 current status

**Question:** What is the current status of the IPSNS manuscript submitted to Discrete Applied Mathematics (DA19469)?

Same logic as above. The same cover letter statement applies.

**Action:** Confirm status. If rejected or withdrawn, no change needed. If under review, amend cover letter.

---

## IMPORTANT confirmations (should resolve before submitting)

### 3. CAIE submission fact

**Question:** Was the CAIE package formally submitted to Computers & Industrial Engineering? If so: submission date, manuscript number, and outcome (desk-rejected / reviewed / withdrawn)?

**Why this matters:** The related-manuscript statement says "whether and when it was submitted to Computers & Industrial Engineering is recorded in author submission logs outside this statement." If it was submitted and desk-rejected, that fact should be confirmable and disclosed. No change to files is needed unless the editor asks for specifics.

### 4. EJCO submission fact

**Question:** Was the EJCO package formally submitted to the EURO Journal on Computational Optimization? If so: submission date, manuscript number, and outcome?

Same reasoning as CAIE.

### 5. Is the COAP manuscript currently under consideration at any other journal?

**Question:** At the moment of COAP submission, is this manuscript (or a substantially overlapping version) under consideration at any other journal?

**Expected answer:** No (the cover letter states this; author must confirm it is still accurate at submission time).

---

## STANDARD confirmations (portal will ask)

### 6. GitHub repository visibility during review

**Question:** Should the repository remain private throughout peer review?

**Context:** The manuscript does not state a public URL. OR1 is the submission reproducibility artifact. The repository is currently private.  
**Recommended answer:** Yes, remain private during review. Make public after acceptance if desired.

### 7. Author awareness and approval

**Question:** As sole author, you approve this submission?

**Expected answer:** Yes.

### 8. ORCIDs verified

**Question:** Is ORCID `0000-0003-1934-6282` correct and active?

**Expected answer:** Verify at orcid.org.

### 9. Funding statement completeness

**Question:** Is "This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors." accurate and complete?

**Note:** If any indirect support (graduate stipend, university computing resources) exists that requires disclosure under COAP policy, update the funding statement. Many single-author submissions from PhD students note graduate stipend or computing infrastructure. If no grant, the current statement is appropriate.

### 10. Conflict of interest completeness

**Question:** Are there any financial or non-financial interests that could have appeared to influence the reported work?

**Expected answer:** None (matches current declaration).

### 11. AI disclosure accuracy

**Question:** Does the current AI disclosure statement accurately reflect all AI tools used?

Current statement: "ChatGPT, Codex, Claude, and Perplexity AI, to support literature exploration, organization of material, language editing, and coding assistance."

**Note:** Springer Nature requires disclosure in the "Methods" section (or equivalent) if AI was used to create content. The current disclosure is in the "Statements and Declarations" section. The manuscript may need to verify placement against current COAP policy if the editor raises this.

### 12. Generative AI in figures

**Question:** Does any figure contain AI-generated imagery?

**Expected answer:** No — framework_overview.tex is a TikZ vector diagram; exp6 figure is a data plot. No AI-generated images.

---

## INFORMATIONAL (portal convenience, not blocking)

### 13. Suggested reviewers

The cover letter offers to suggest reviewers "through the submission portal if requested." The existing reviewer list in `docs/coap_cover_letter_and_upload_20260612/EDITORIAL_MANAGER_COPY_READY_TEXT.md` lists two candidates. Author should prepare 3–5 verified suggestions before the portal step (see `SUGGESTED_REVIEWER_REGISTER.csv`).

### 14. Opposed reviewers

Author should confirm if there are specific reviewers who should be excluded due to conflict of interest.

### 15. Subject classifications

Portal may ask for MSC codes or similar. Author should prepare: **90C27** (Combinatorial optimization), **68W25** (Approximation algorithms), **05C85** (Graph algorithms).

---

## Summary

| # | Question | Blocking | Status |
|---|---|---|---|
| 1 | JOCO-D-26-00099 status | YES if still under review | Author must check |
| 2 | DA19469 status | YES if still under review | Author must check |
| 3 | CAIE submission fact | No | Author to confirm for completeness |
| 4 | EJCO submission fact | No | Author to confirm for completeness |
| 5 | No other concurrent submission | YES | Author confirms at time of submission |
| 6 | Repository visibility | No | Author preference |
| 7 | Sole author approval | No | Standard |
| 8 | ORCID correct | No | Verify at orcid.org |
| 9 | Funding complete | No | Verify |
| 10 | No conflicts | No | Standard |
| 11 | AI disclosure accurate | No | Verify tool list |
| 12 | No AI figures | No | Confirmed from source |
| 13 | Suggested reviewers | No | Prepare list |
| 14 | Opposed reviewers | No | Prepare list if applicable |
| 15 | Subject classifications | No | Prepare MSC codes |
