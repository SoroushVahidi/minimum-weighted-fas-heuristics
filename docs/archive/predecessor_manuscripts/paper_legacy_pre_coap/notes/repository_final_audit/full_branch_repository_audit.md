# Full Branch and Repository Audit

Pre-CAIE submission read-only audit. No manuscript content, code, results, or upload files were modified.

## Repository state

| Item | Value |
|---|---|
| **Start HEAD** | `d8c3725ea6c5a6b24d3f0f9900ecb551d8d6a3b7` |
| **Branch** | `main` |
| **Remote sync** | Up to date with `origin/main` (no ahead/behind after fetch) |
| **Working tree** | Clean except untracked `results/` |
| **Tracked files** | 372 |

### Expected commits present

- `3086b26` — warning reduction pass
- `2ba67a7` — upload package audit
- `54f4432` — source contact fill
- `3f086cb` — final contact-pass audit
- `d8c3725` — final no-edit sanity check (current HEAD at audit start)

## Tracked / untracked / ignored summary

| Category | Status |
|---|---|
| **Untracked** | `results/tables/.gitkeep` only (local experiment outputs; regenerable) |
| **Ignored** | Entire `submission_package/` directory (upload PDFs, artifact zip remain local-only) |
| **Tracked large files (>5 MB)** | None |
| **Local large files (>10 MB, not tracked)** | External tool git pack and SNAP datasets under `experiments/exp4_external_baselines/external_tools/`; `experiments/exp5_lolib_dense/downloads/lolib_2010.zip` — experiment infrastructure only, not part of upload package |

Upload PDFs and artifact zip are **not tracked** in git (confirmed via `git ls-files --error-unmatch`).

## Upload file inventory

| File | Size (B) | SHA256 | Pages | Tracked |
|---|---:|---|---:|---|
| `submission_package/files_for_upload/main_anonymized.pdf` | 194819 | `011e0c93d5cb489526d7ee460243cc012391a3355a264be10d3a5b1aa955b4b2` | 38 | no |
| `submission_package/files_for_upload/title_page.pdf` | 27665 | `e136e8c753d4f8dcbea561d8ce7511085c13ea99a420a9a369d08d294f6be7f1` | 2 | no |
| `submission_package/files_for_upload/cover_letter_draft.pdf` | 13287 | `1fe0b25c9344408f14cd79164ffcec12507c768c4cee12e8880cff2ed0593bdb` | 1 | no |
| `submission_package/files_for_upload/highlights.txt` | 312 | `65b2485340f79b9259ae4741948a3b68ac95a25d39f57b194a9c51d0affe28af` | — | no |
| `submission_package/anonymous_artifact/mwfas_reproducibility_artifact_anonymous.zip` | 147077 | `3bbb70a1027eae59205c1437064bd1b9aaff1a3e114e8a795bb9f3a2b456e924` | 83 files | no |

All five required upload files are present.

## Upload staleness

| Check | Result |
|---|---|
| **Broad source mtime check** | Flags `main_anonymized.pdf` as older than latest source (because `title_page.tex` / `cover_letter_draft.tex` were edited for contact fill) |
| **Input-specific check** | **Current** — zero anonymized-manuscript inputs (`main_anonymized.tex`, sections, tables, figures, algorithms, `references.bib`) are newer than `main_anonymized.pdf` |
| **Title page / cover letter / highlights** | Current relative to their sources |

The broad staleness flag is a **false positive** for the anonymized manuscript; no rebuild needed.

## Anonymized manuscript scan

### PDF (`main_anonymized.pdf`)

**PASS** — no identity hits, no placeholder hits.

### Source (`main_anonymized.tex`, sections, tables, figures, algorithms)

**PASS** — no identity, email, ORCID, GitHub, or placeholder hits.

## Non-anonymized file scan

### PDFs

| File | Expected identity | Placeholders |
|---|---|---|
| `title_page.pdf` | Soroush, Vahidi, NJIT, `sv96@njit.edu` present | none |
| `cover_letter_draft.pdf` | Soroush, Vahidi, NJIT, `sv96@njit.edu` present | none |

### Source (`main.tex`, `title_page.tex`, `cover_letter_draft.tex`)

**PASS** — no remaining placeholders.

## Anonymous artifact scan

**PASS**

- Zip exists: yes
- File count: 83
- Identity hits: 0
- Forbidden path hits: 0 (no `.git`, `results/`, `external_tools/`, personal paths, etc.)

## Manuscript metrics

| Metric | Value | Status |
|---|---|---|
| Highlights count | 5 | PASS (3–5) |
| Highlight max length | 68 chars | PASS (≤ 85) |
| Abstract word count | 209 | PASS (≤ 250) |
| Citation keys used | 11 | PASS |
| Missing citation keys | 0 | PASS |

## Experiment / result provenance

**PASS** — all expected files present:

- `experiments/combined/summary/manuscript_results_digest.md`
- `experiments/exp3_exact_small/summary/`
- `experiments/exp4_external_baselines/summary/exp4_raw_summary.csv`
- `experiments/exp4_external_baselines/tables/`
- `experiments/exp5_lolib_dense/summary/exp5_lolib_raw_summary.csv`
- `experiments/exp5_lolib_dense/tables/exp5_lolib_paper_summary.csv`
- `paper/notes/results_asset_provenance.md`
- All four results tables in `paper/tables/`

## LaTeX warning status

Prior warning-reduction pass (`3086b26`) resolved all critical/high/overfull warnings.

**Remaining (non-blocking):**

| Severity | Count | Location |
|---|---:|---|
| critical | 0 | — |
| high | 0 | — |
| medium | 3 | bibliography underfull boxes (`main_anonymized.bbl`) |
| low | 2 | bibliography underfull + one results paragraph glue |

Reports on file: `paper/notes/final_warning_pass/warning_resolution_report.md`, `warning_analysis_after.json`, `paper/notes/final_readthrough/final_submission_readiness_report.md`.

## Blocking issues

**None.**

## Non-blocking issues

1. Broad upload-staleness script flags `main_anonymized.pdf`; input-specific check confirms it is current.
2. Five remaining underfull `\hbox` warnings (bibliography and one results line); no overfull boxes.
3. `results/` remains untracked local output (intentional).
4. `submission_package/` is gitignored (intentional; upload files stay local).
5. Large external-tool/download files exist under `experiments/` but are not in the upload package or anonymous artifact.

## Final recommendation

**Ready for visual PDF review and CAIE upload.**

All automated checks pass. The repository branch is synced with remote, upload files are present and correctly partitioned (anonymized vs non-anonymized), the anonymous artifact is clean, manuscript metrics and citations are valid, and experiment provenance files are in place.

### Recommended manual steps

1. Visually review all three upload PDFs (framework figure, tables, bibliography, cover letter).
2. Upload the five files from `submission_package/`.
3. Enter ORCID in the CAIE submission portal if requested (not in manuscript files).

### Supporting audit artifacts

- `paper/notes/repository_final_audit/upload_file_inventory.{md,json}`
- `paper/notes/repository_final_audit/upload_staleness_audit.{md,json}`
- `paper/notes/repository_final_audit/pdf_text_scan.{md,json}`
- `paper/notes/repository_final_audit/source_scan.{md,json}`
- `paper/notes/repository_final_audit/artifact_scan.{md,json}`
- `paper/notes/repository_final_audit/manuscript_metrics.{md,json}`
- `paper/notes/repository_final_audit/result_provenance_check.{md,json}`
- `paper/notes/repository_final_audit/latex_warning_status.md`
