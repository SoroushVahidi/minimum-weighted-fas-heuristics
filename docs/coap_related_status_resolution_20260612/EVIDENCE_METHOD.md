# Evidence Method

**Date:** 2026-06-12  
**Purpose:** Documents the evidence sources consulted and their authority ranking for this status resolution audit.

---

## Evidence hierarchy applied

Per task specification, evidence is ranked in descending order of authority:

| Rank | Type | Found in this audit? |
|---|---|---|
| 1 | Official journal decision email | NO — external evidence directory not created |
| 2 | Official Editorial Manager / Springer submission-status page | NO — portal login not performed |
| 3 | Dated withdrawal confirmation | NO |
| 4 | Dated transfer confirmation | NO |
| 5 | Manuscript receipt or submission acknowledgment | PARTIAL — inferred from git commit messages labeled "submission preparation" |
| 6 | Author correspondence with editorial office | PARTIAL — references to "email history" in venue_decision_notes_20260606.md; emails not in repository |
| 7 | Repository cover letters and submission packages | YES — cover_letter.tex, related_manuscripts_statement.tex |
| 8 | Internal audit records | YES — PRIOR_DECISION_AND_REVIEW_REGISTER.csv, SUBMISSION_LINEAGE.md, reuse_risk_report.md, REJECTION_REASON_MASTER_REGISTER.csv, venue_decision_notes_20260606.md |
| 9 | Git history | YES — commit messages, dates, branch structure |

---

## External evidence directory

Expected location: `/home/soroush/coap_status_evidence/`

**Status: NOT FOUND.** The external evidence directory was not created before this task was run. No documentary evidence files (decision letters, withdrawal confirmations, portal status screenshots, submission acknowledgment emails) are available outside the repository.

---

## What was found inside the repository

The following internal documents contain status-relevant content:

| Document | Evidence type | Authority |
|---|---|---|
| `docs/archive/internal/coap_rejection_history_and_revision_plan_20260611/PRIOR_DECISION_AND_REVIEW_REGISTER.csv` | Internal audit register | Rank 8 |
| `docs/archive/internal/coap_rejection_history_and_revision_plan_20260611/SUBMISSION_LINEAGE.md` | Internal timeline with explicit INFER tags | Rank 8–9 |
| `docs/archive/predecessor_manuscripts/.../notes/reuse_risk_report.md` | Internal planning note | Rank 8 |
| `docs/archive/internal/coap_rejection_history_and_revision_plan_20260611/REJECTION_REASON_MASTER_REGISTER.csv` | Internal review-feedback register | Rank 8 |
| `docs/venue_decision_notes_20260606.md` | Venue selection analysis; references email history | Rank 7–8 |
| `paper_coap/submission/cover_letter.tex` | Author's own declaration | Rank 7 |
| `paper_coap/submission/related_manuscripts_statement.tex` | Author's own disclosure | Rank 7 |
| Git commit history | Commit messages, timestamps, labeled revision experiments | Rank 9 |

---

## Critical finding about CAIE git evidence

Commits explicitly labeled "for CAIE revision" (c847747, 7f16b6c, e48b663) dated 2026-06-06 contain the phrase "External reviewers requested" in experiment READMEs. This constitutes rank-9 evidence that:
1. CAIE received external (peer) review
2. A revision was prepared
3. The author then pivoted to EJCO (2026-06-10) and COAP (2026-06-11)

The outcome of the CAIE review cycle (rejection, withdrawal, or resubmission status) is not documented in the repository.

---

## What is explicitly INFERRED vs. confirmed

| Item | Claim | Evidence Type | Can be stated as fact? |
|---|---|---|---|
| JOCO rejected | "rejected JOCO manuscripts" | Rank 8: internal planning note only; "[INFER]" tag in SUBMISSION_LINEAGE.md | NO — requires decision letter |
| DAM rejected | "rejected DAM manuscripts" | Same | NO |
| CAIE submitted | Git commits "CAIE submission files", "Clean repository after CAIE submission preparation" | Rank 9: strong inference | PROBABLE but not confirmed by submission acknowledgment |
| CAIE review received | Commits labeled "for CAIE revision" + experiment READMEs citing "External reviewers" | Rank 9 | PROBABLE but not confirmed by review letter |
| CAIE outcome | Pivot to EJCO suggests CAIE became inactive | Rank 9: very indirect | NO — requires decision or withdrawal confirmation |
| EJCO submitted | Package finalized in git; then archived | Rank 9 | PROBABLE that package was prepared; formal submission unconfirmed (no ID in repository) |

---

## Conclusion on evidence quality

No formal documentary evidence (rank 1–6) is available for any of the four journal submissions (JOCO, DAM, CAIE, EJCO). The repository provides rank 7–9 evidence that is informative but insufficient to formally confirm statuses using the controlled vocabulary defined in the task.

The author must provide rank 1–6 evidence (decision emails, portal status, withdrawal confirmations) before statuses can be formally confirmed.
