# SNCS Retargeting — Pass 1 Changelog

**Branch:** `sncs-retargeting` (not merged to `main`)
**Date:** 2026-06-17
**Scope:** title, abstract, keywords, introduction framing, related-work framing, declarations, submission packaging, and dual-version status documentation. No changes to `paper_coap/`, `src/`, `tests/`, `online_resource_1/`, or any verified scientific result.

## New directory: `paper_sncs/`

Created via `rsync -a` from `paper_coap/`, then pruned of COAP-portal-specific files (see `docs/sncs_preparation_202606/SUBMISSION_PACKAGE_STATUS.md` for the full removal list). Identical to `paper_coap/` except for the edits below.

## File-by-file diff summary

### `paper_sncs/main.tex`

- **Title:** `IPSNS for Minimum Weighted Feedback Arc Set on Sparse Digraphs` → `An Incumbent-Protected Component-Local Heuristic for Minimum Weighted Feedback Arc Set on Sparse Digraphs` (running title: `Component-Local Heuristic for MWFAS`). Avoids leading with the IPSNS acronym, per SNCS broad-CS framing.
- **Abstract:** rewritten as a structured abstract (Purpose / Methods / Results / Conclusion), 246 words, within the SNCS 150–250 word guideline. All verified numbers preserved: 96/97, 14 strict / 83 ties / 0 regressions, 57-instance subset, 0.0031% mean gap (standardized from "0.003%" for consistency with Table 7), 38/55/0 vs. DRMacIver/FAS, 21.60% mean reduction, 45/50 dense LOLIB.
- **Keywords:** `Minimum weighted feedback arc set, Combinatorial optimization, Local-ratio algorithm, Strongly connected components, Heuristic search, Algorithm engineering` → `Feedback arc set, Graph algorithms, Combinatorial optimization, Heuristic search, Strongly connected components, Algorithm engineering` (matches the task's specified keyword list exactly).
- Author/affiliation/ORCID/email block: unchanged.

### `paper_sncs/sections/01_introduction.tex`

- Central-contribution paragraph reordered to explain the idea ("incumbent-protected, component-local heuristic") before introducing the IPSNS acronym, instead of acronym-first.
- Several "SCC" → "component"/"strongly connected component" substitutions to define the concept before relying on the shorthand.
- "0.003\%" → "0.0031\%" in the empirical-message paragraph, for numeric consistency with Table 7 (`table_exact_validation.tex`); the underlying verified result is unchanged.
- "Algorithmic contribution" and "Integrated framework" bullets reworded to avoid stacked-acronym sentences (e.g., splitting the seed-attribution sentence into two), without changing claims.

### `paper_sncs/sections/02_related_work.tex`

- Added one lead-in sentence after `\section{Related work}` framing the section around three literatures: graph algorithms for cycle breaking, experimental algorithmics/heuristic design, and the minimal/stable and SCC-aware feedback-set lineage.
- Extended the closing sentence of the first paragraph in "Feedback arc set algorithms" to explicitly name "experimental algorithmics and algorithm engineering" as the paper's territory.
- No citations added, removed, or altered. No other subsections touched.

### `paper_sncs/declarations/statements_and_declarations.tex`

- Added three new subsections between "Competing interests" and "Author contributions": **Ethics approval** ("Not applicable" + one-sentence justification), **Consent to participate** ("Not applicable"), **Consent for publication** ("Not applicable").
- **Related manuscripts and prior author work:** replaced the blanket "No substantially overlapping manuscript is currently under consideration elsewhere" with wording that discloses the COAP sibling manuscript by title, commits to non-concurrent active consideration, and hedges the residual claim ("knowingly," "at the time of this submission"). See `OVERLAP_AND_DISCLOSURE_AUDIT.md` §5–6 for the rationale.
- **Data and code availability:** updated paths from `paper_coap/submission/final_upload/` to `paper_sncs/submission/sncs_initial/`; added an explicit statement that the repository is public.
- AI-disclosure subsection: unchanged in substance (per task instruction).

### `paper_sncs/README.md`, `paper_sncs/submission/README.md`

Rewritten from COAP-specific wording to describe the SNCS draft status, build command, and pointers to the pass-1 docs and the overlap audit.

## Removed from the `paper_coap/` → `paper_sncs/` copy

These were COAP-portal-specific or asserted COAP-specific facts, and were deleted from `paper_sncs/` (originals untouched in `paper_coap/`):

- `submission/final_upload/` (entire frozen COAP upload bundle)
- `submission/related_manuscripts_statement.tex` / `.pdf`
- `submission/cover_letter.tex` / `.pdf`
- `submission/AUTHOR_PRE_SUBMISSION_CONFIRMATION.md`
- `submission/EDITORIAL_MANAGER_FINAL_COPY_READY_TEXT.md`
- `COAP_TEMPLATE_AND_GUIDELINES_AUDIT.md`
- `notes/COAP_*.md` (all COAP-labeled internal notes)
- `notes/RELATED_MANUSCRIPTS_AUDIT_NEEDED.md`

## New files added (not present in `paper_coap/`)

- `paper_sncs/submission/sncs_initial/` — draft upload bundle: `Vahidi_SNCS_Manuscript.pdf`, `Vahidi_SNCS_Source.zip`, `Vahidi_SNCS_Online_Resource_1.pdf`, `Vahidi_SNCS_Online_Resource_1.zip`, `MANIFEST.sha256`, `README_SNCS_UPLOAD.md`.
- `docs/sncs_preparation_202606/SNCS_GUIDELINE_CHECK.md`
- `docs/sncs_preparation_202606/OVERLAP_AND_DISCLOSURE_AUDIT.md`
- `docs/sncs_preparation_202606/CHANGELOG_SNCS_PASS1.md` (this file)
- `docs/sncs_preparation_202606/BUILD_AND_VALIDATION.md`
- `docs/sncs_preparation_202606/SUBMISSION_PACKAGE_STATUS.md`

## Documentation updated outside `paper_sncs/` and `docs/sncs_preparation_202606/`

- `README.md` (repository root): added a dual-target manuscript section, fixed the stale "Repository is private" claim to "public" (confirmed via `gh repo view`), added `paper_sncs/` to the canonical layout table, updated page counts (COAP 23→24 pages, corrected to match the actual current build), updated the "Manuscript and submission" section to list both targets and flag the stale root-level Online Resource 1 duplicate.
- `docs/MANUSCRIPT_AND_ARTIFACT_STATUS.md`: restructured into a dual-target status document; corrected a stale COAP manuscript SHA-256/byte-count (`36a01f92...`, 201,092 bytes → `aebdf183...`, 199,822 bytes, matching the actual current `paper_coap/main.pdf`); added the SNCS artifact table; flagged the stale root-level Online Resource 1 duplicate for future cleanup (not removed in this pass — out of scope).

## Explicitly unchanged

- `paper_coap/` — byte-for-byte identical (verified via `git status --short paper_coap/` showing no modifications).
- `src/`, `tests/`, `scripts/`, `experiments/`, `online_resource_1/` — untouched.
- All verified scientific results (96/97, 14 strict bests, 14/83/0, 56/57 exact matches, 0.0031% mean gap, 38/55/0 vs. DRMacIver/FAS, 21.60% mean reduction, 45/50 dense LOLIB) — unchanged; only surrounding prose and one rounding-precision presentation choice (0.003% → 0.0031%) were touched, and only in `paper_sncs/`.

## Pass 1 correction (same day, 2026-06-17): COAP status corrected to "submitted and declined"

This pass's original COAP-status language (inferring "very likely not yet been formally submitted" from a blank sign-off block and a "Pending" CSV row) was factually wrong and has been corrected per an explicit author statement: **COAP was formally submitted to *Computational Optimization and Applications* and was declined** on journal-audience/fit grounds. `paper_coap/` is now documented as a historical, declined-submission snapshot; SN Computer Science is recorded as the active target.

Files corrected: `README.md`, `docs/MANUSCRIPT_AND_ARTIFACT_STATUS.md`, `docs/sncs_preparation_202606/OVERLAP_AND_DISCLOSURE_AUDIT.md`, `docs/sncs_preparation_202606/SUBMISSION_PACKAGE_STATUS.md`, `docs/sncs_preparation_202606/README.md`, and `paper_sncs/declarations/statements_and_declarations.tex` ("Related manuscripts and prior author work": dropped the now-obsolete "ensure only one is under active consideration" framing in favor of disclosing the prior submission and decline, and added disclosure of the still-unresolved Journal of Supercomputing manuscript). The dated, archival documents under `docs/coap_related_status_resolution_20260612/`, `docs/coap_submission_freeze_20260612/`, and `docs/coap_submission_dry_run_20260612/` were intentionally left untouched as historical snapshots from before the actual submission/decline event.

The Journal of Supercomputing manuscript search was also re-run across the entire local workspace (not just this repository) in this correction pass; it remains unlocated. Its existence is confirmed per the author's email records, but the overlap audit remains blocked pending the author supplying the actual manuscript file.
