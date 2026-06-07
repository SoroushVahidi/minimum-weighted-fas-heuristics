# CAIE Final Upload Checklist

**Repository:** minimum-weighted-fas-heuristics  
**Final HEAD:** 53e740a560e61888ec3614884df80b85441763e9  
**Date prepared:** 2026-06-07  
**Journal:** Computers & Industrial Engineering

---

## Files to Upload

| # | File | Role | Pages | Size | SHA256 |
|---|---|---|---:|---:|---|
| 1 | `submission_files_for_download/main_anonymized.pdf` | Blinded manuscript | 44 | 236737 | `3237eac24f6a34bbda13cc1df62f0acab6db913fe7d1cd10e4ef2da812d3c099` |
| 2 | `submission_files_for_download/title_page.pdf` | Title page (non-anonymized) | 2 | 27665 | `e136e8c753d4f8dcbea561d8ce7511085c13ea99a420a9a369d08d294f6be7f1` |
| 3 | `submission_files_for_download/cover_letter_draft.pdf` | Cover letter (non-anonymized) | 1 | 13292 | `e2be34bb67e25da5093d52debf754b942e330a984e39c377e060f5479f609223` |
| 4 | `submission_files_for_download/highlights.txt` | Highlights | — | 312 | `65b2485340f79b9259ae4741948a3b68ac95a25d39f57b194a9c51d0affe28af` |
| 5 | `submission_files_for_download/mwfas_reproducibility_artifact_anonymous.zip` | Supplementary / reproducibility artifact | — | 147077 | `3bbb70a1027eae59205c1437064bd1b9aaff1a3e114e8a795bb9f3a2b456e924` |

---

## Upload Instructions

- Upload **main_anonymized.pdf** as the blinded manuscript (double-anonymous review).
- Upload **title_page.pdf** separately in the designated title-page field.
- Upload **cover_letter_draft.pdf** as the cover letter.
- Upload **highlights.txt** in the highlights field (paste text if the system requires plain text).
- Upload the **zip** as supplementary material / reproducibility artifact for review.
- **Do not** provide the GitHub private repository URL to reviewers.
- **Do not** include acknowledgments until after double-blind review is complete.
- Perform a **human visual review** of main_anonymized.pdf before pressing the final submit button.

---

## Final Checks Passed

| Check | Result |
|---|---|
| Abstract word count | 232 / 250 — **PASS** |
| Abstract has citations | None — **OK** |
| LOLIB defined at first use in abstract | Yes — **OK** |
| Keyword count | 7 / 7 max — **PASS** |
| Keywords contain "and" or "of" | None — **OK** |
| Keywords match main.tex ↔ main_anonymized.tex | Yes — **OK** |
| Highlights count | 5 (3–5 required) — **PASS** |
| Highlights all ≤ 85 characters | Yes (max 68 chars) — **PASS** |
| paper/highlights.txt matches upload copy | Yes — **OK** |
| Anonymized PDF: no identity leaks | Clean — **PASS** |
| Anonymized PDF: no placeholders | Clean — **PASS** |
| Title page and cover letter: non-anonymized, placeholder-free | Confirmed — **OK** |
| Artifact zip: anonymous | Confirmed — **OK** |
| LaTeX compile: no new warnings | Only pre-existing underfull hbox — **OK** |
| No blocking issues | Confirmed — **READY** |

---

## Pre-Submit Visual Review Checklist (manual)

Before clicking submit, open main_anonymized.pdf and verify:

- [ ] Title does not contain author names or institution
- [ ] All author fields are blank or anonymized
- [ ] No acknowledgments section is present
- [ ] No funding attribution to named individuals
- [ ] Abstract text matches what was submitted in the form fields
- [ ] Keywords match what was entered in the form fields
- [ ] Figure captions and table captions do not reference internal lab names
- [ ] References do not contain a self-citation that reveals identity
- [ ] Page count is 44 and manuscript renders correctly

---

*Checklist generated automatically by `paper/scripts/audit_abstract_keywords_length.py`.*
