# Manual Submission Actions

Items that require user action before uploading to CAIE.

## Visual review (required)

- [ ] Visually review `submission_package/files_for_upload/main_anonymized.pdf` (38 pages)
- [ ] Visually review `submission_package/files_for_upload/title_page.pdf` (2 pages)
- [ ] Visually review `submission_package/files_for_upload/cover_letter_draft.pdf` (1 page)
- [ ] Confirm framework figure readability after recent scaling
- [ ] Confirm bibliography pages look acceptable (remaining underfull warnings only)

## Placeholders to fill manually

- [ ] Replace `[Corresponding Author Contact]` in:
  - `paper/title_page.tex` (line 13)
  - `paper/main.tex` (line 32, post-acceptance/non-anonymized use)
  - `paper/cover_letter_draft.tex` (line 18)
- [ ] Replace `[Editor Name]` in `paper/cover_letter_draft.tex` (lines 6 and 8)
- [ ] Decide whether to replace any date placeholder or rely on the submission system's auto date (no explicit date placeholder is currently in source)

After filling placeholders, recompile title page and cover letter locally and refresh:
- `submission_package/files_for_upload/title_page.pdf`
- `submission_package/files_for_upload/cover_letter_draft.pdf`

## CAIE upload package

Upload these files to the submission system:

1. **Title page** — `submission_package/files_for_upload/title_page.pdf`
2. **Manuscript without author details** — `submission_package/files_for_upload/main_anonymized.pdf`
3. **Cover letter** — `submission_package/files_for_upload/cover_letter_draft.pdf`
4. **Highlights** — `submission_package/files_for_upload/highlights.txt`
5. **Anonymous artifact** — `submission_package/anonymous_artifact/mwfas_reproducibility_artifact_anonymous.zip`

## Deferred until after review / acceptance

- [ ] Keep acknowledgments deferred in the anonymized manuscript (intentional for double-anonymized review)
- [ ] After acceptance: replace anonymized data/code availability statement with public repository URL and DOI
- [ ] After acceptance: add acknowledgments to the non-anonymized manuscript and title-page materials as needed

## Do not upload from repo

- Generated TeX auxiliary files, compile logs, rendered page images
- Local `results/` experiment outputs (untracked)
- Non-anonymized `paper/main.tex` as the review manuscript
