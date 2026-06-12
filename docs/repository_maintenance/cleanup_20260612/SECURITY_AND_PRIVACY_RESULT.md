# Security and Privacy Scan Results

**Date:** 2026-06-12  
**Scope:** All tracked files in the repository at 3b51476fb2a6815fd566f09c7a79d931f1d99dda

## Scan methodology

Scanned all tracked files using:
```bash
git ls-files | xargs grep -l "password\|api_key\|token\|private_key\|secret\|/home/soroush"
```

Also manually inspected:
- All PDFs in `paper_coap/submission/final_upload/` (for embedded metadata)
- All cover letters and declaration documents
- `CITATION.cff` and `README.md`
- `docs/coap_cover_letter_and_upload_20260612/EDITORIAL_MANAGER_COPY_READY_TEXT.md`

## Results

### Credentials / secrets

**None found.** No API keys, passwords, tokens, or private keys in any tracked file.

### Absolute paths to local filesystem

`/home/soroush/` references found **only in archived/legacy documentation**:
- `docs/archive/` (historical development notes — not in active navigation)
- `docs/full_branch_repository_audit_20260612/REPOSITORY_FILE_INVENTORY.csv` (file inventory path column)

These are in archival documentation and do not constitute privacy risks. The inventory path column records canonical repository structure, not sensitive information.

No absolute local paths appear in:
- manuscript source or PDF
- Online Resource 1
- upload artifacts
- root README

### Private correspondence

No reviewer reports, rejection letters, or private correspondence in tracked files.
Internal editorial strategy files are in `docs/archive/internal/` with an explicit
`PUBLIC_RELEASE_POLICY.md` noting they must be removed before public release.

### Author PII

Author name, email (sv96@njit.edu), and ORCID (0000-0003-1934-6282) appear in:
- `CITATION.cff` — appropriate; standard citation metadata
- Cover letter PDF — appropriate; standard submission document
- Declaration documents — appropriate

No unnecessary PII beyond standard academic identification.

### PDF metadata

Submission PDFs were built from LaTeX and contain standard TeX-generated metadata.
No local filesystem paths or system-identifying metadata observed.

### Live PIDs

No live PID files in tracked content. Local PID files are gitignored.

### Confidential journal status

`docs/coap_cover_letter_and_upload_20260612/EDITORIAL_MANAGER_COPY_READY_TEXT.md`
contains CAIE/EJCO submission status with author-confirmation placeholders:
```
[AUTHOR: please confirm current CAIE/EJCO status before submitting]
```
This is an internal working document, not a public artifact. It is not embedded in
any upload PDF.

## Verdict

**CLEAN — no secrets, credentials, or sensitive material requiring action before push.**

The repository is safe to push to the private remote. Before making the repository
public (post-acceptance), remove `docs/archive/internal/` per `PUBLIC_RELEASE_POLICY.md`.
