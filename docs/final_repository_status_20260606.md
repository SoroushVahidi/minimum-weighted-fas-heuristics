# Final Repository Status — 2026-06-06

Snapshot after CAIE submission-package preparation and repository cleanup.

## Repository

| Item | Value |
|---|---|
| **HEAD** | `27aeb08` (update after cleanup commit if newer) |
| **Branch** | `main` |
| **Remote** | `origin/main` (synced) |

## Submission package status

**Ready for visual PDF review and CAIE upload.**

All automated audits pass. Contact placeholders filled in non-anonymized sources (`sv96@njit.edu`). Anonymized manuscript and anonymous artifact remain identity-free.

### Upload files (local only, gitignored)

| File | Path |
|---|---|
| Anonymized manuscript | `submission_package/files_for_upload/main_anonymized.pdf` (38 pages) |
| Title page | `submission_package/files_for_upload/title_page.pdf` (2 pages) |
| Cover letter | `submission_package/files_for_upload/cover_letter_draft.pdf` (1 page) |
| Highlights | `submission_package/files_for_upload/highlights.txt` |
| Anonymous artifact | `submission_package/anonymous_artifact/mwfas_reproducibility_artifact_anonymous.zip` |

## Committed vs intentionally uncommitted

| Category | Status |
|---|---|
| Manuscript TeX sources | committed |
| Experiment summaries/tables | committed |
| Audit reports under `paper/notes/` | committed |
| Upload PDFs and artifact zip | **not committed** (gitignored) |
| `results/` local outputs | **not committed** (gitignored) |
| TeX aux/log files | **not committed** (gitignored) |
| External tools/downloads under `experiments/` | **not committed** (gitignored) |

## Reproduce main paper assets

From `paper/`:

```bash
# Anonymized review manuscript
latexmk -pdf -interaction=nonstopmode main_anonymized.tex
cp main_anonymized.pdf ../submission_package/files_for_upload/main_anonymized.pdf

# Non-anonymized title page and cover letter
latexmk -pdf -interaction=nonstopmode title_page.tex
latexmk -pdf -interaction=nonstopmode cover_letter_draft.tex
cp title_page.pdf cover_letter_draft.pdf ../submission_package/files_for_upload/
cp highlights.txt ../submission_package/files_for_upload/
```

Anonymous artifact:

```bash
python paper/scripts/build_anonymous_artifact.py
```

## Final audit reports

| Report | Path |
|---|---|
| Full branch/repository audit | `paper/notes/repository_final_audit/full_branch_repository_audit.md` |
| No-edit sanity check | `paper/notes/final_upload_audit/final_no_edit_sanity_check.md` |
| Manual submission actions | `paper/notes/final_upload_audit/manual_submission_actions.md` |
| Notes index | `paper/notes/README.md` |
| Cleanup report | `paper/notes/repository_cleanup_after_submission_prep.md` |

## Remaining human action

1. Visually review all three upload PDFs (framework figure, tables, bibliography, cover letter).
2. Upload the five files listed above to CAIE.
3. Enter ORCID in the submission portal if requested (not in manuscript files).
