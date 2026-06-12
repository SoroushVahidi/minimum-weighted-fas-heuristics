# Repository Cleanup After Submission Prep

Hygiene pass after CAIE submission-package preparation. No manuscript content, upload PDFs, or anonymous artifact were modified.

## Repository

- **Starting HEAD:** `27aeb08e330f8ebd730e2d49d849cbc0556866ad`

## Generated artifacts removed

| Category | Action |
|---|---|
| TeX aux/log/out files under `paper/` | removed if present (none found at cleanup time) |
| `__pycache__/`, `*.pyc`, `.pytest_cache/` | removed if present |
| `paper/notes/final_warning_pass/rendered_pages/` | removed if present (not present) |
| `paper/notes/final_warning_pass/contact_sheets/` | removed if present (not present) |

**Preserved (not removed):**
- All five upload files under `submission_package/`
- Committed audit markdown/json reports under `paper/notes/`
- Committed manuscript sources and experiment summaries

## `.gitignore` changes

Added/consolidated exclusions for:
- `results/` (whole directory)
- LaTeX build artifacts: `*.aux`, `*.bbl`, `*.blg`, `*.fdb_latexmk`, `*.fls`, `*.out`, `*.spl`, `*.synctex.gz`
- Local compiled PDFs: `paper/title_page.pdf`, `paper/cover_letter_draft.pdf`, `paper/main_anonymized.pdf`
- Compile logs: `paper/contact_*.log`
- Diagnostic renders: `paper/notes/final_warning_pass/rendered_pages/`, `contact_sheets/`

Existing exclusions retained for submission package PDFs/txt/zip, experiment raw/external_tools/downloads/logs, Python caches, and virtual environments.

## Documentation created/updated

| File | Purpose |
|---|---|
| `paper/notes/README.md` | Index of important audit and submission notes |
| `docs/final_repository_status_20260606.md` | Repository and submission-package status snapshot |
| `paper/notes/repository_cleanup_after_submission_prep.md` | This cleanup report |

## Upload files confirmed present

| File | Size (bytes) |
|---|---:|
| `submission_package/files_for_upload/main_anonymized.pdf` | 194819 |
| `submission_package/files_for_upload/title_page.pdf` | 27665 |
| `submission_package/files_for_upload/cover_letter_draft.pdf` | 13287 |
| `submission_package/files_for_upload/highlights.txt` | 312 |
| `submission_package/anonymous_artifact/mwfas_reproducibility_artifact_anonymous.zip` | 147077 |

## Anonymized source scan

**PASS** — no identity, email, ORCID, or GitHub hits in `main_anonymized.tex` or shared section/table/figure sources.

## Intentionally untracked/ignored

| Item | Reason |
|---|---|
| `results/` | Local regenerable experiment outputs |
| Upload PDFs under `submission_package/files_for_upload/` | Submission binaries kept local-only |
| Anonymous artifact zip | Submission binary kept local-only |
| `submission_package/anonymous_artifact/staging/` | Artifact build staging |
| Experiment `raw/`, `external_tools/`, `downloads/`, `logs/` | Large/temporary experiment infrastructure |

## `submission_package` tracking

**PASS** — no files under `submission_package/` are tracked in git.

## Blocking issues

**None.**

## Recommendation

Repository is clean and organized. Proceed to visual PDF review and CAIE upload.
