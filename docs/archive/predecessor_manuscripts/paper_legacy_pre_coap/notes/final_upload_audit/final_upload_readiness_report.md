# Final Upload Readiness Report

## Repository

- **Starting HEAD:** `b4e0765`
- **Upload staleness:** all upload files current relative to source; recompile skipped
- **Blocking issues:** none

## Upload inventory

| File | Size | Pages | SHA256 |
|---|---:|---:|---|
| `submission_package/files_for_upload/main_anonymized.pdf` | 194,819 bytes | 38 | `011e0c93d5cb489526d7ee460243cc012391a3355a264be10d3a5b1aa955b4b2` |
| `submission_package/files_for_upload/title_page.pdf` | 28,112 bytes | 2 | `95b80c5e9a24c3be6f1baa1792e997ea90eed00292240e785a0e921d38b158a6` |
| `submission_package/files_for_upload/cover_letter_draft.pdf` | 13,054 bytes | 1 | `954c8acd904598ee744058d1aadffa40531f360a9a3f7154947a2c5bf8666c6a` |
| `submission_package/files_for_upload/highlights.txt` | 312 bytes | — | `65b2485340f79b9259ae4741948a3b68ac95a25d39f57b194a9c51d0affe28af` |

## Anonymous artifact

| Property | Value |
|---|---|
| Path | `submission_package/anonymous_artifact/mwfas_reproducibility_artifact_anonymous.zip` |
| Size | 147,077 bytes |
| SHA256 | `3bbb70a1027eae59205c1437064bd1b9aaff1a3e114e8a795bb9f3a2b456e924` |
| File count | 83 |
| Top-level dir | `mwfas_reproducibility_artifact_anonymous` |

Checksum matches `paper/notes/artifact_validation/artifact_checksums.txt`.

## PDF text scan

### `main_anonymized.pdf` (anonymized manuscript)
- identity hits: none
- placeholder hits: none
- unresolved `??`: 0
- **Status:** pass

### `title_page.pdf` (non-anonymized; expected)
- identity hits: Soroush, Vahidi, New Jersey Institute of Technology (expected)
- placeholder hits: `[Corresponding Author Contact]` (manual fill required)

### `cover_letter_draft.pdf` (non-anonymized; expected)
- identity hits: Soroush, Vahidi (expected)
- placeholder hits: `[Editor Name]`, `[Corresponding Author Contact]` (manual fill required)

## Source placeholder scan

Remaining placeholders (manual only):

- `paper/title_page.tex:13` — `[Corresponding Author Contact]`
- `paper/main.tex:32` — `[Corresponding Author Contact]` (non-anonymized version)
- `paper/cover_letter_draft.tex:6,8,18` — `[Editor Name]`, `[Corresponding Author Contact]`

No `TODO`, `FIXME`, or `??` in anonymized manuscript source.

## Anonymous artifact rescan

- zip exists: yes
- forbidden path hits: 0
- identity hits: 0
- **Status:** pass

## Abstract and highlights

- abstract words: 209 (limit 250) — pass
- highlight count: 5 (required 3–5) — pass
- all highlight lines ≤ 85 characters — pass

## LaTeX warning status

From prior warning pass (`paper/notes/final_warning_pass/warning_analysis_after.json`); upload PDFs not recompiled this run because sources are current:

| Severity | Count |
|---|---:|
| critical | 0 |
| high | 0 |
| medium | 3 |
| low | 2 |
| overfull hbox | 0 |
| underfull hbox | 5 |
| total deduplicated warning lines | 5 |

Remaining warnings are bibliography underfull boxes and one low-severity results paragraph underfull warning. No submission-blocking layout issues.

## Readiness status

**Technically ready after manual placeholders are filled and visual PDF review is completed.**

Scientific content, experiment values, and anonymized manuscript identity controls are synchronized. Only corresponding-author contact and editor/contact placeholders remain before upload.

## Next recommended task

Fill `[Corresponding Author Contact]` and `[Editor Name]`, recompile title page and cover letter, visually review all three upload PDFs, then upload the five files listed in `manual_submission_actions.md`.
