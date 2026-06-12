# Final No-Edit Sanity Check

Read-only verification of the CAIE upload package. No source files, PDFs, or artifacts were modified.

## Repository

- **HEAD:** `3f086cbac9a5d5396891e4eea38c3ac69eb82ba6`
- **Branch:** `main` (up to date with `origin/main`)
- **Git status:** clean except untracked `results/` (local experiment outputs; not part of upload package)

## Upload file inventory

| File | Size (bytes) | SHA256 |
|---|---:|---|
| `submission_package/files_for_upload/main_anonymized.pdf` | 194819 | `011e0c93d5cb489526d7ee460243cc012391a3355a264be10d3a5b1aa955b4b2` |
| `submission_package/files_for_upload/title_page.pdf` | 27665 | `e136e8c753d4f8dcbea561d8ce7511085c13ea99a420a9a369d08d294f6be7f1` |
| `submission_package/files_for_upload/cover_letter_draft.pdf` | 13287 | `1fe0b25c9344408f14cd79164ffcec12507c768c4cee12e8880cff2ed0593bdb` |
| `submission_package/files_for_upload/highlights.txt` | 312 | `65b2485340f79b9259ae4741948a3b68ac95a25d39f57b194a9c51d0affe28af` |
| `submission_package/anonymous_artifact/mwfas_reproducibility_artifact_anonymous.zip` | 147077 | `3bbb70a1027eae59205c1437064bd1b9aaff1a3e114e8a795bb9f3a2b456e924` |

All five required upload files are present.

## Page counts

| PDF | Pages |
|---|---:|
| `main_anonymized.pdf` | 38 |
| `title_page.pdf` | 2 |
| `cover_letter_draft.pdf` | 1 |

## Anonymized manuscript scan (`main_anonymized.pdf`)

**Result: PASS**

Forbidden terms scanned (case-insensitive): `Soroush`, `Vahidi`, `NJIT`, `New Jersey Institute of Technology`, `sv96`, `sv96@njit.edu`, ORCID, GitHub identity, acknowledgments, `TODO`, `FIXME`, `??`, placeholders.

- **Hits:** none

## Title page scan (`title_page.pdf`)

**Result: PASS**

Required content present:
- `Soroush Vahidi`
- `sv96@njit.edu`
- `New Jersey Institute of Technology`

## Cover letter scan (`cover_letter_draft.pdf`)

**Result: PASS**

Required content present:
- `Soroush Vahidi`
- `sv96@njit.edu`
- `Dear Editor,`

## Anonymous artifact scan

**Result: PASS**

Scanned text-like files inside `mwfas_reproducibility_artifact_anonymous.zip` for:
`Soroush`, `Vahidi`, `NJIT`, `New Jersey Institute of Technology`, `sv96`, `sv96@njit.edu`, `/home/soroush`, `github.com/SoroushVahidi`, ORCID.

- **Hits:** 0

## Highlights (`highlights.txt`)

**Result: PASS**

- **Bullet count:** 5 (within 3–5 limit)
- **Max length:** 70 characters (limit 85)

| # | Length | Text |
|---:|---:|---|
| 1 | 70 | Reproducible heuristics for weighted directed ordering are developed |
| 2 | 67 | Strongly connected refinement improves local-ratio seed solutions |
| 3 | 63 | Exact small-instance tests show near-optimal ordering quality |
| 4 | 56 | Sparse benchmarks outperform tested external baselines |
| 5 | 51 | Dense LOLIB results define a clear scope boundary |

## Git tracking check

**Result: PASS**

None of the five upload files (PDFs, highlights, artifact zip) are tracked in git. Generated binaries remain local-only as intended.

## Blocking issues

**None found.**

## Proceed to visual review and CAIE upload?

**Yes.** All automated checks pass. The upload package is present, correctly partitioned (anonymized vs non-anonymized), and ready for your visual PDF review before submission.

Recommended final manual steps:
1. Visually review all three PDFs (framework figure, tables, bibliography, cover letter formatting).
2. Upload the five files listed above to CAIE.
3. Enter ORCID in the submission portal if requested (not required in manuscript files).
