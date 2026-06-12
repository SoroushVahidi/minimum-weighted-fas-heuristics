# Final Submission Package Checklist

## Required files

- Title page with author details
  - Source: `paper/title_page.tex`
  - PDF to upload: `submission_package/files_for_upload/title_page.pdf`
  - Status: source ready; PDF built locally
  - Remaining placeholders: corresponding author contact

- Manuscript without author details
  - Source: `paper/main_anonymized.tex`
  - PDF to upload: `submission_package/files_for_upload/main_anonymized.pdf`
  - Status: source ready; PDF built locally

- Cover letter
  - Source: `paper/cover_letter_draft.tex`
  - PDF/text to upload: `submission_package/files_for_upload/cover_letter_draft.pdf`
  - Status: draft ready; PDF built locally
  - Remaining placeholders: editor name, date, corresponding author contact

- Highlights
  - Source: `paper/highlights.txt`
  - Upload file: `submission_package/files_for_upload/highlights.txt`
  - Status: ready; copied locally

- Anonymous artifact
  - Source zip: `submission_package/anonymous_artifact/mwfas_reproducibility_artifact_anonymous.zip`
  - SHA256: `3bbb70a1027eae59205c1437064bd1b9aaff1a3e114e8a795bb9f3a2b456e924`
  - Status: built and validated locally; zip intentionally left uncommitted

- Optional graphical abstract
  - Status: not included

## Declarations

- Generative AI declaration
  - Source: `paper/declarations/generative_ai_declaration.tex`
  - Status: included in anonymized manuscript before references

- Funding / competing interest / CRediT
  - Sources:
    - `paper/declarations/funding_statement.tex`
    - `paper/declarations/competing_interest.tex`
    - `paper/declarations/credit_statement_nonanonymized.tex`
  - Status: ready in source files

- Data and code availability
  - Sources:
    - `paper/declarations/data_code_availability_anonymized.tex`
    - `paper/declarations/data_code_availability.tex`
  - Status: ready; review version points to anonymous artifact and public release after acceptance

## Remaining non-anonymous placeholders

- corresponding author full email/contact in `paper/main.tex` and `paper/title_page.tex`
- cover letter placeholders for editor name, date, and corresponding author contact
- acknowledgments remain intentionally deferred until after double-anonymized review
