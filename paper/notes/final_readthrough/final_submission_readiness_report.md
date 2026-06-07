# Final Submission Readiness Report

Date: 2026-06-06

## Generated upload files

- `submission_package/files_for_upload/main_anonymized.pdf`
- `submission_package/files_for_upload/title_page.pdf`
- `submission_package/files_for_upload/cover_letter_draft.pdf`
- `submission_package/files_for_upload/highlights.txt`

## Page counts

- `main_anonymized.pdf`: 38 pages
- `title_page.pdf`: 2 pages
- `cover_letter_draft.pdf`: 1 page

## Anonymous artifact

- Zip path: `submission_package/anonymous_artifact/mwfas_reproducibility_artifact_anonymous.zip`
- Size: 147077 bytes
- SHA256: `3bbb70a1027eae59205c1437064bd1b9aaff1a3e114e8a795bb9f3a2b456e924`
- Status: built locally and intentionally left uncommitted

## Compile status

- `main_anonymized.tex`: compiled successfully
- `title_page.tex`: compiled successfully
- `cover_letter_draft.tex`: compiled successfully

## Warning summary

Before the final layout pass, the main anonymized compile log contained:

- 47 overfull `\hbox` warnings
- 101 underfull `\hbox` warnings
- 153 warning lines total

After the final layout pass, the main anonymized compile log contained:

- 51 overfull `\hbox` warnings
- 101 underfull `\hbox` warnings
- 157 warning lines total

Interpretation:

- the remaining warnings are still layout-quality issues rather than compilation failures;
- the persistent warnings are concentrated in compact tables, some bibliography line breaks, the framework figure caption region, and a few dense prose paragraphs;
- the `algorithm.sty` UTF-8 warning remains non-fatal and appears to come from the package rather than manuscript content.

## Identity and placeholder scans

- anonymized manuscript PDF text: no identity hits, no placeholder hits
- anonymized manuscript source: no identity hits
- title page PDF text: expected author/affiliation identity present; corresponding-author placeholder remains
- cover letter PDF text: expected author identity present; editor and contact placeholders remain

## Submission-constraint checks

- Double-anonymized manuscript: yes
- Highlights within CAIE limits: yes (5 bullets; all <= 85 characters)
- AI declaration present before references in `main_anonymized.tex`: yes
- Data/code availability statement points to the anonymous artifact and public release after acceptance: yes
- Acknowledgments absent from the anonymized manuscript: yes
- Acknowledgments in title page deferred until after review: yes

## Layout fixes made in this pass

- shortened the manuscript title slightly to reduce header pressure;
- tightened long prose lines in Introduction, Related Work, Problem Definition, Results, and Conclusions;
- shortened the dense LOLIB figure caption;
- compressed wording in the experiment-overview table;
- shortened the funding statement wording;
- confirmed that the cover letter compiles cleanly after the closing-block fix.

## Remaining manual placeholders

- `[Corresponding Author Contact]` in `paper/main.tex`, `paper/title_page.tex`, and `paper/cover_letter_draft.tex`
- `[Editor Name]` in `paper/cover_letter_draft.tex`
- the auto-rendered letter date remains local-build generated and should be replaced or confirmed for the final upload context

## Final assessment

Status: ready for submission packaging, pending manual placeholder completion and one last human visual check of the PDFs.

The anonymized manuscript is clean, the upload PDFs exist locally, the anonymous artifact is built and validated, the highlights pass the stated limits, and the core declaration files are in place. The remaining issues are manual metadata placeholders and residual non-fatal line-break warnings.
