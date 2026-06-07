# Final Contact Pass Report

## Repository

- **Starting HEAD:** `54f4432228830bfa688ea206d2c8008ecf4f0f0e`
- **Prior baseline:** `2ba67a7` (last audit before contact fill)

## Placeholders before (from `2ba67a7`)

- `paper/main.tex:32` — `\ead{[Corresponding Author Contact]}`
- `paper/title_page.tex:13` — `\ead{[Corresponding Author Contact]}`
- `paper/cover_letter_draft.tex:6` — `[Editor Name]` (recipient)
- `paper/cover_letter_draft.tex:8` — `[Editor Name]` (salutation)
- `paper/cover_letter_draft.tex:18` — `[Corresponding Author Contact]`

## Placeholders after

- No `[Corresponding Author Contact]`, `[Editor Name]`, `[Date]`, `TODO`, or `FIXME` in:
  - `paper/main.tex`
  - `paper/title_page.tex`
  - `paper/cover_letter_draft.tex`
  - `paper/declarations/`

## Files updated

- `paper/main.tex` — `\ead{sv96@njit.edu}`
- `paper/title_page.tex` — `\ead{sv96@njit.edu}`; acknowledgments placeholder unchanged
- `paper/cover_letter_draft.tex` — `Editor` / `Dear Editor,` / `sv96@njit.edu` in closing

## PDF rebuild

| File | Rebuilt | Status |
|---|---|---|
| `submission_package/files_for_upload/title_page.pdf` | yes | identity + email present; no placeholders |
| `submission_package/files_for_upload/cover_letter_draft.pdf` | yes | identity + email present; no placeholders |
| `submission_package/files_for_upload/main_anonymized.pdf` | no | clean (no identity, no email, no placeholders) |
| `submission_package/files_for_upload/highlights.txt` | copied (unchanged) | pass |

## Anonymized source scan

- `main_anonymized.tex`, all `sections/`, `tables/`, `figures/`, `algorithms/`: **PASS** (no identity or email hits)

## Anonymized PDF scan

- `main_anonymized.pdf`: **PASS** — no identity hits, no placeholder hits

## Artifact email rescan

- `submission_package/anonymous_artifact/mwfas_reproducibility_artifact_anonymous.zip`: **PASS** — 0 identity/email hits

## Remaining manual placeholders

- None in non-anonymized submission sources
- Title-page acknowledgments remain deferred (intentional)
- ORCID: not in manuscript files; enter in submission portal if requested

## Final upload file paths

1. `submission_package/files_for_upload/title_page.pdf`
2. `submission_package/files_for_upload/main_anonymized.pdf`
3. `submission_package/files_for_upload/cover_letter_draft.pdf`
4. `submission_package/files_for_upload/highlights.txt`
5. `submission_package/anonymous_artifact/mwfas_reproducibility_artifact_anonymous.zip`

## Remaining manual action before submission

1. Visually review all three upload PDFs (title page, anonymized manuscript, cover letter)
2. Confirm framework figure readability and bibliography appearance
3. Upload the five files above to CAIE
