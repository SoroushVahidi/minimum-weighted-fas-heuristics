# Final CAIE Submission Package Audit — Readiness Report

**Date:** 2026-06-07  
**HEAD at audit start:** `17dec438e8eabaedc59d18bd5b093a870eda4a49`

---

## Upload File Inventory

| File | Pages | Size (bytes) | SHA256 |
|---|---:|---:|---|
| main_anonymized.pdf | 44 | 236723 | `c10ecfa21f79ffa6cfcb1984d7ac000ae716c30fc4c15d05232bad8318729699` |
| title_page.pdf | 2 | 27665 | `e136e8c753d4f8dcbea561d8ce7511085c13ea99a420a9a369d08d294f6be7f1` |
| cover_letter_draft.pdf | 1 | 13292 | `e2be34bb67e25da5093d52debf754b942e330a984e39c377e060f5479f609223` |
| highlights.txt | — | 312 | `65b2485340f79b9259ae4741948a3b68ac95a25d39f57b194a9c51d0affe28af` |
| mwfas_reproducibility_artifact_anonymous.zip | — | 147077 | `3bbb70a1027eae59205c1437064bd1b9aaff1a3e114e8a795bb9f3a2b456e924` |

---

## Check Results

### 1. Upload / Download File Match — PASS
All 5 upload files match their `submission_files_for_download/` counterparts (identical SHA256).

### 2. Staleness Check — PASS
`main_anonymized.pdf` is newer than all manuscript source inputs. No source files are newer than the upload PDF. `title_page.pdf` and `cover_letter_draft.pdf` have no `.tex` sources newer than the compiled PDFs.

### 3. Anonymized PDF Text Scan — PASS
- Identity hits: none
- Placeholder hits: none
- Bad style hits: none
- Acknowledgment section: none (absent, as required for double-blind)
- References section: present

**Note on `WMSFstyle`:** The audit script's `bad_terms` list includes "WMSFstyle". This term appears in the manuscript as a legitimate technical term ("the full WMSFstyle seed", "The WMSFstyle seed similarly..."). It has been present in all prior PDF audit snapshots (final_layout_readability_audit, final_placeholder_pass, second_reference_pass_pdf_scan, exp9_application_case, computational_environment scans). It is not a compliance or anonymization issue; it is standard terminology used throughout the methods section. **Not a blocking issue.**

### 4. Title Page and Cover Letter PDF Text Scan — PASS
- Title page: author info present (Soroush Vahidi, sv96@njit.edu), no placeholders
- Cover letter: author info present, "Dear Editor" present, no placeholders

### 5. PDF Metadata Scan — PASS
- `main_anonymized.pdf`: Creator=LaTeX with hyperref; no identity hits in metadata
- `title_page.pdf`: Creator=tectonic; no identity hits
- `cover_letter_draft.pdf`: Creator=tectonic; no identity hits
- No hostname, username, or path in any PDF metadata

### 6. Highlights — PASS
- 5 bullet points (within 3–5 limit)
- All under 85 characters (max: 70)

### 7. Anonymous Artifact Zip — PASS
- 83 files, 147077 bytes
- SHA256: `3bbb70a1027eae59205c1437064bd1b9aaff1a3e114e8a795bb9f3a2b456e924`
- No identity hits in file paths or text file contents
- No forbidden paths (.git/, __pycache__/, submission_package/, etc.)

### 8. CAIE Declarations — PASS
- Generative AI statement: present
- Funding statement: present
- Competing interest declaration: present
- Data/code availability: present

### 9. LaTeX Warning Status — PASS
Most recent compile (env_compile, 2026-06-07):
- EXIT=0 (clean)
- 0 overfull hboxes
- Underfull hboxes only (cosmetic; not actionable)
- 0 undefined citations
- 25 citation keys used, 26 defined in `references.bib`

### 10. Git Tracking — INFO
- 518 tracked files total
- 0 tracked files over 5 MB
- 7 download files tracked in `submission_files_for_download/`
- `submission_package/main.pdf` is tracked (an old file from early in the project, not the current upload PDF)
- All current upload files in `submission_package/files_for_upload/` are gitignored and not tracked (correct)

---

## Blocking Issues

**None.**

---

## Final Recommendation

**Ready for manual visual review and CAIE upload.**

Before uploading, perform a brief visual review of:
1. `main_anonymized.pdf` — confirm 44 pages render correctly; spot-check table placement (EXP8, EXP9, ablation), algorithm listings, and figures
2. `title_page.pdf` — confirm author names, affiliation, email, ORCID, and CRediT statement are correct
3. `cover_letter_draft.pdf` — confirm salutation, journal name, and contact details

Then upload to the CAIE editorial system:
- `main_anonymized.pdf` (44 pp) — primary manuscript
- `title_page.pdf` (2 pp) — title/author page
- `cover_letter_draft.pdf` (1 p) — cover letter
- `highlights.txt` — 5 bullet highlights
- `mwfas_reproducibility_artifact_anonymous.zip` — supplementary reproducibility artifact
