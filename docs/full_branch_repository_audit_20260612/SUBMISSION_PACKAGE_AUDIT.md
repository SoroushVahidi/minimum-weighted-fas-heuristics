# Submission Package Audit

**Canonical upload directory:** `paper_coap/submission/final_upload/`  
**HEAD:** `6c04ff1`

## Portal files (6)

| # | Filename | Size (B) | SHA-256 | Current? |
|---|---|---|---|---|
| 1 | `Vahidi_COAP_Manuscript.pdf` | 333,157 | `97eb61238a81e12e2597a6963926f0f092ad994f3f369b89715f36e9e06d0898` | **Yes** (6c04ff1 abstract trim) |
| 2 | `Vahidi_COAP_Manuscript_Source.zip` | 145,760 | `0fd2b2c138c31798ff334a47f7d5c917fd32ec83aa5b05b932c82c20a32f7b38` | **Yes** |
| 3 | `Vahidi_COAP_Cover_Letter.pdf` | 24,732 | `df6622bd7b19f2ed73e5d54c38e953a2092f9436f574db4da86b374efe6496f8` | Yes (f306c15) |
| 4 | `Vahidi_Online_Resource_1_MWFAS.pdf` | 130,236 | `8cc1479fb7aebe9e8b4c219aada0bf87f6c0383f53345a2d851b776b581aa0ea` | Yes (f306c15) |
| 5 | `Vahidi_Online_Resource_1_MWFAS.zip` | 1,116,197 | `5dc3875acad386f992266a43d1406b96787c95fa1d3acde7124be327ee29495e` | Yes (f306c15) |
| 6 | `Vahidi_Related_Manuscripts_Statement.pdf` | 22,804 | `7e5ee12c4200ff0a006f350b379d63a1dc38dccbc588ab7dbb62e241a08b519e` | Yes (f306c15) |

## Source files (LaTeX)

| File | Role |
|---|---|
| `paper_coap/submission/cover_letter.tex` | Cover letter source |
| `paper_coap/submission/related_manuscripts_statement.tex` | Related manuscripts source |

## Portal metadata (not in final_upload/)

Located in `docs/coap_cover_letter_and_upload_20260612/`:

- `EDITORIAL_MANAGER_UPLOAD_MAP.csv`
- `EDITORIAL_MANAGER_COPY_READY_TEXT.md` — **stale abstract (271 words)**; portal must use `main.tex` abstract (238 words)
- `SUGGESTED_REVIEWERS.csv`
- `AUTHOR_METADATA_REGISTER.csv`
- `PORTAL_ORIGINALITY_AND_OVERLAP_RESPONSES.md`

## Root-level duplicates

| Root file | Matches final_upload? |
|---|---|
| `Vahidi_Online_Resource_1_MWFAS.pdf` | Yes (OR1) |
| `Vahidi_Online_Resource_1_MWFAS.zip` | Yes (OR1) |
| `paper_coap/main.pdf` | Matches manuscript PDF |

## Stale copies to exclude from COAP upload

| Path | Reason |
|---|---|
| `submission_package/ejco_*.zip` | EJCO venue |
| `submission_package/files_for_upload/` | EJCO (partially gitignored) |
| `paper/main.pdf` | Legacy journal tree |

## Quality checks

| Check | Result |
|---|---|
| Opens successfully | PDFs verified via prior builds |
| Correct title/authors/journal | Yes |
| Placeholders | None in PDFs |
| Internal absolute paths | None in upload PDFs |
| Confidential material | None in upload set |

## Verdict

**Submission package is ready** for Editorial Manager. Only manuscript PDF/ZIP changed at 6c04ff1; OR1 and cover materials remain valid from f306c15.
