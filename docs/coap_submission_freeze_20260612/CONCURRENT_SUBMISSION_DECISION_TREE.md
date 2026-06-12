# Concurrent Submission Decision Tree

**Date:** 2026-06-12  
**Applies to:** COAP submission of "SCC-Local Destroy-and-Repair Heuristics for Minimum Weighted Feedback Arc Set on Sparse Digraphs"

---

## Background

The cover letter (`Vahidi_COAP_Cover_Letter.pdf`) contains the following declaration:

> "I confirm that no substantially overlapping manuscript by me is under consideration elsewhere at the time of submission."

This declaration is **accurate only if both JOCO-D-26-00099 and DA19469 are currently not under active peer review** at their respective journals. The status of these submissions is documented in author records outside the repository. **No inference about current status should be drawn from the presence of submission packages in the repository.**

---

## What can be stated from repository evidence

| Manuscript | Known facts | What is NOT determinable from repo |
|---|---|---|
| arXiv:2412.16181 | Public preprint; status: permanently available | N/A — preprints are not "under consideration" |
| JOCO-D-26-00099 | LR-TA manuscript; submitted to JOCO; "editorial outcome documented in author records" | Whether it was accepted, rejected, or is still under review |
| DA19469 | IPSNS manuscript; submitted to DAM; "editorial outcome documented in author records" | Same |
| CAIE package | Repository submission package prepared; "whether and when it was submitted to Computers & Industrial Engineering is recorded in author submission logs outside this statement" | Whether it was submitted at all; outcome if submitted |
| EJCO package | Repository submission package prepared; "submission outcome, if any, is recorded in author submission logs outside this statement" | Whether it was submitted at all; outcome if submitted |

---

## Decision tree

### Step 1 — Check JOCO-D-26-00099

Log in to the JOCO Editorial Manager system and verify the current status of manuscript JOCO-D-26-00099.

**Proceed to the corresponding case below:**

---

### Case A — JOCO and DAM are both inactive (withdrawn, rejected, or accepted/published)

**Defined as:** JOCO-D-26-00099 is not currently under peer review AND DA19469 is not currently under peer review.

**Assessment:** The cover letter declaration is accurate as written.

**Action:**
1. No amendment to the cover letter is required.
2. Proceed to the portal with the existing `Vahidi_COAP_Cover_Letter.pdf`.
3. Complete the remaining items in `AUTHOR_PRE_SUBMISSION_CONFIRMATION.md` and submit.

**Safe cover letter and portal declaration:** The current cover letter text is appropriate:
> "I confirm that no substantially overlapping manuscript by me is under consideration elsewhere at the time of submission."

---

### Case B — One manuscript remains under active consideration but the overlap with COAP is not substantial

**Defined as:** Either JOCO or DAM is still under peer review, but the specific version remaining under review does not substantially overlap with the COAP submission in scientific contribution (e.g., it is a narrowly scoped earlier version covering only one of the two algorithms, with a clearly different scope statement).

**Assessment:** This case requires careful author judgment. The cover letter declaration as written is not safe for this case — it would constitute a false assertion.

**Action:**
1. **Do not submit with the current cover letter.**
2. Assess the extent of overlap between the active submission and the COAP manuscript.
3. Consult the relevant journal's concurrent-submission policy before making any declaration.
4. If the journals permit concurrent submission of non-substantially-overlapping work, amend the cover letter to accurately disclose the concurrent active submission and explain the distinction in scope and contribution.
5. A revised cover letter must be rebuilt from `cover_letter.tex`, rebuilt to PDF, and its SHA-256 recorded before upload.
6. If journals prohibit concurrent submission regardless of overlap, withdraw the active submission first, then submit to COAP.

**Do not submit to COAP under this case without explicit journal-policy verification.**

---

### Case C — One manuscript remains under active consideration and overlaps substantially with the COAP submission

**Defined as:** Either JOCO-D-26-00099 or DA19469 is still under active peer review, and its scientific content (algorithms, experimental results, claims) substantially overlaps with the COAP submission — i.e., a reasonable editor would conclude they cover the same contribution.

**Assessment:** The COAP submission must not proceed until the conflict is resolved.

**Action:**
1. **Do not submit to COAP at this time.**
2. Either:
   a. Withdraw the active submission from JOCO or DAM (as appropriate), then proceed to COAP; or
   b. Wait for the JOCO/DAM decision, then proceed to COAP.
3. After the conflicting submission is no longer active, return to Case A.
4. The cover letter does not require amendment if Case A is then satisfied.

**Submitting under this case without resolution would constitute a false author declaration and a potential ethics violation under Springer Nature journal policies.**

---

### Case D — Status is uncertain or cannot be confirmed

**Defined as:** The author cannot determine the current status of JOCO-D-26-00099 or DA19469 (e.g., the submission system is inaccessible, decision emails are ambiguous, or records are unclear).

**Assessment:** The cover letter declaration cannot safely be made.

**Action:**
1. **Do not submit to COAP until status is confirmed.**
2. Contact the JOCO editorial office to request a status update for manuscript JOCO-D-26-00099.
3. Contact the DAM editorial office to request a status update for manuscript DA19469.
4. Once status is confirmed, proceed to the applicable case above.

---

## CAIE and EJCO

The repository contains submission packages for CAIE and EJCO but explicitly does not record whether these were formally submitted. The cover letter correctly qualifies this: "preparation of a package does not by itself establish submission history." The decision tree above focuses on JOCO and DAM because they have confirmed manuscript IDs. For CAIE and EJCO:

- If CAIE package was formally submitted and is still under review: treat as Case B or C above for that journal
- If EJCO package was formally submitted and is still under review: treat as Case B or C above for that journal
- If neither was formally submitted, or both outcomes are known to be inactive: no additional action required beyond the existing disclosure

---

## After COAP submission

Once COAP submission is made, do not submit substantially overlapping work elsewhere while it is under review. The COAP concurrent-submission declaration applies for the duration of the review.
