# Dry Run Retention Decision

**Date:** 2026-06-12  
**Source directory:** `docs/coap_submission_dry_run_20260612/`  
**Evaluated for:** suitability for Git commit into main branch

---

## Retention criteria

Files are classified and given a commit/exclude/archive decision based on:
- **Durable value:** provides lasting submission provenance, verification record, or author reference
- **Sensitive material:** contains internal editorial strategy, speculative portal behavior, or material that would mislead a future reader
- **Local paths / secrets:** contains absolute paths (`/home/soroush/`) that are inappropriate in a public commit
- **Verification status:** speculative portal guesses are clearly labeled `NOT VERIFIED` — acceptable if labeled; unacceptable if presented as fact

---

## Classification table

| file | classification | commit | exclude | archive_internal | reason | future_public_release_action |
|---|---|---|---|---|---|---|
| AUTHOR_CONFIRMATIONS_REQUIRED.md | internal author checklist | YES | — | — | Permanent governance record of what was unknown at submission time; JOCO/DAM status clearly flagged as author-only | Strip personal email/ORCID if public release desired; otherwise acceptable as-is |
| COVER_LETTER_VERIFICATION.md | durable submission documentation | YES | — | — | Line-by-line audit evidence of cover letter completeness | Safe for public release |
| EXECUTIVE_SUMMARY.md | durable submission documentation | YES | — | — | Top-level dry-run summary; no sensitive material | Safe for public release |
| FINAL_SUBMISSION_DRY_RUN_VERDICT.md | durable submission documentation | YES | — | — | Primary verdict document; includes EXP11 resolution and concurrent-submission warning | Safe for public release |
| GENERATED_PDF_ORDER_PLAN.md | durable submission documentation | YES | — | — | Portal PDF verification plan; no sensitive content | Safe for public release |
| MANUSCRIPT_UPLOAD_VERIFICATION.md | durable submission documentation | YES | — | — | Manuscript audit evidence | Safe for public release |
| ONLINE_RESOURCE_UPLOAD_VERIFICATION.md | durable submission documentation | YES | — | — | OR1 validation result record | Safe for public release |
| RELATED_MANUSCRIPT_VERIFICATION.md | durable submission documentation | YES | — | — | Related-work disclosure table; status appropriately qualified as author-records-only | Safe for public release; no confidential outcomes disclosed |
| REPOSITORY_STATE.md | durable submission documentation | YES | — | — | Concise state snapshot | Safe for public release |
| SOURCE_ZIP_VERIFICATION.md | durable submission documentation | YES | — | — | Documents pdflatex unavailability; appropriate limitation record | Safe for public release |
| STEP_BY_STEP_SUBMISSION_WALKTHROUGH.md | internal author checklist | YES | — | — | Contains reviewer emails and portal navigation; useful for submission governance; emails are publicly available faculty contacts | Strip reviewer emails if public release desired |
| audit_metadata.json | official-requirement evidence | YES | — | — | Machine-readable record; pending_confirmations field is appropriately honest | Safe for public release |
| FILE_DESIGNATION_MAP.csv | durable submission documentation | YES (needs .gitignore exception) | — | — | Upload designation record; no sensitive content | Safe for public release |
| FINAL_PORTAL_ISSUE_REGISTER.csv | official-requirement evidence | YES (needs .gitignore exception) | — | — | 13-issue tracker; editor-only designation notes are reasonable submission governance, not internal editorial correspondence | ISSUE-01 (JOCO/DAM) remains pending; note this is factually accurate |
| LIVE_PORTAL_FIELD_REGISTER.csv | internal author checklist | YES (needs .gitignore exception) | — | — | 31-step portal reference; portal behaviors labeled NOT VERIFIED; reviewer emails present | Strip reviewer emails if public release desired |
| OFFICIAL_COAP_REQUIREMENTS.csv | official-requirement evidence | YES (needs .gitignore exception) | — | — | 27 requirements with verified/unverified distinction; appropriate qualification | Items marked NOT VERIFIED should not be treated as facts; labeling is adequate |
| SUBMISSION_CONSISTENCY_MATRIX.csv | durable submission documentation | YES (needs .gitignore exception) | — | — | 24 cross-surface consistency fields; all pass | Safe for public release |
| SUGGESTED_REVIEWER_REGISTER.csv | internal author checklist | YES (needs .gitignore exception) | — | — | Contains reviewer emails; public faculty contacts | Strip emails if making fully public; appropriate for author's own repo |
| UPLOAD_FILE_REGISTER.csv | durable submission documentation | YES (needs .gitignore exception) | — | — | 6-file checksum register; no sensitive content | Safe for public release |
| logs/tests.log | temporary build log | — | YES | — | Transient; contains /home/soroush/ paths; test results recorded in VALIDATION_RESULTS.md | N/A — excluded |
| logs/or1_validation.log | temporary build log | — | YES | — | Transient; contains /home/soroush/ paths; PASSED result recorded elsewhere | N/A — excluded |
| logs/path_and_secret_scan.log | temporary build log | — | YES | — | Contains local paths; CLEAN result recorded in maintenance docs | N/A — excluded |
| logs/source_zip_build.log | temporary build log | — | YES | — | Transient; findings in SOURCE_ZIP_VERIFICATION.md | N/A — excluded |

---

## .gitignore exceptions required

The following patterns must be added to `.gitignore` to allow the CSV files to be committed (pattern `*.csv` currently blocks them):

```gitignore
!docs/coap_submission_dry_run_20260612/*.csv
!docs/coap_submission_freeze_20260612/*.csv
```

Log exceptions are NOT added — logs remain excluded by design.

---

## Material NOT present in dry-run directory

Confirmed absent (as required):
- No reviewer reports or rejection letters
- No confidential editorial correspondence
- No content inferred from unknown submission outcomes (JOCO/DAM statuses appropriately marked as unknown)
- No portal screenshots (portal not logged into)
- No sensitive internal editorial strategy beyond publicly documented portal behavior

---

## Items requiring editorial caution

**LIVE_PORTAL_FIELD_REGISTER.csv and OFFICIAL_COAP_REQUIREMENTS.csv** contain items marked `NOT VERIFIED` for portal-specific behavior (page limits, line numbers, highlights, graphical abstract, review type). These are appropriately labeled and must not be read as confirmed COAP requirements. A future reader should treat `NOT VERIFIED` entries as questions to resolve at portal login, not as established facts.

**SUGGESTED_REVIEWER_REGISTER.csv** contains institutional email addresses obtained from public faculty pages. These are appropriate for author use but should be stripped of emails before any fully public scholarly release.
