# COAP Compliance Audit
**Date:** 2026-06-11  
**Journal:** Computational Optimization and Applications (COAP), Springer Nature

---

## 1. Template Compliance

| Item | Required | Status |
|------|---------|--------|
| Document class | `sn-jnl` with `sn-mathphys-num` option | ✓ CORRECT (`\documentclass[pdflatex,sn-mathphys-num]{sn-jnl}`) |
| Springer template version | December 2024 or current | ✓ Template files present: `sn-jnl.cls`, `sn-mathphys-num.bst` |
| ORCID present | Required | ✓ `https://orcid.org/0000-0003-1934-6282` in `\author` macro |
| Author email | Required | ✓ `sv96@njit.edu` |
| Affiliation | Required | ✓ NJIT, Department of Computer Science, Newark NJ 07102 USA |
| Abstract | Required, 150–250 words | ✓ Present; ~220 words |
| Keywords | Required (3–8) | ✓ 6 keywords present |
| Section structure | Standard | ✓ 8 sections: intro, related, problem, framework, experiments, results, discussion, conclusion |
| Declarations section | Required by SN | ✓ Present in `declarations/statements_and_declarations.tex` |

## 2. Declarations Compliance

| Declaration | Springer Nature Requirement | Status |
|-------------|----------------------------|--------|
| Funding | State source or "no funding" | ✓ "did not receive any specific grant" |
| Competing interests | Required | ✓ "no known competing financial or non-financial interests" |
| Author contributions | Required for multi-author; single-author | ✓ Full CRediT taxonomy: Conceptualization, Methodology, Software, Formal analysis, Investigation, Validation, Data curation, Visualization, Writing |
| Data and code availability | Required | ✓ Present: "will be provided as supplementary material in Online Resource 1" |
| AI disclosure | Required (SN policy since 2023) | ✓ Lists ChatGPT, Codex, Claude, Perplexity AI; states author reviewed all outputs |
| Ethics approval | Required for human/animal studies | N/A — no human/animal subjects |
| Consent to participate | Required for human studies | N/A |
| Consent to publish | Required for identifiable individuals | N/A |

## 3. ORCID Workaround

The December 2024 Springer template references `Orcidlogo.eps` in the `\orcid` macro but does not ship this asset. The manuscript uses a custom workaround:

```latex
\gdef\orcid#1{\,\textsuperscript{\href{#1}{\textcolor{blue}{ORCID}}}}
```

This produces a linked blue "ORCID" superscript. **Functionally equivalent; ORCID link is correct and present.** The editorial production team typically replaces this with the proper ORCID icon. No issue for submission.

## 4. Title

**Title:** "Local-Ratio Seeding and SCC-Based Refinement for the Minimum Weighted Feedback Arc Set Problem"

- Length: acceptable for COAP (~14 words)
- Running head: "Local-Ratio Seeding and SCC-Based Refinement for MWFAS" (set in `\title[...]`)
- No hype words, no superlatives — ✓ APPROPRIATE

## 5. Bibliography

| Item | Status |
|------|--------|
| Bibliography style | `sn-mathphys-num.bst` (numeric, mathphys flavor) | ✓ |
| Bibliography file | `bibliography/references.bib` | ✓ |
| All cited works have `.bib` entries | Not exhaustively verified; no compilation errors noted | ✓ (pdf compiled successfully, `main.pdf` present) |
| DOI/URL for primary citations | Should be present for key works | Not independently verified for all entries |
| DRMacIver repository cited | Must have URL | Check: should be present as `drmaciver_fas_tool` or similar |

## 6. Supplementary Material

| Item | Required | Status |
|------|---------|--------|
| Online Resource 1 | Must accompany submission | **NOT YET CREATED for COAP** |
| EJCO artifact (`ejco_reproducibility_artifact/`) | EJCO-targeted package | Present but stale; uses EJCO paths |
| COAP-targeted artifact | Must be created | **MISSING — BLOCKER for submission** |
| Anonymous version | For double-blind review | `submission_package/anonymous_artifact/` exists but EJCO-era |
| Manifest | For editorial office | `submission_files_for_download/manifest.json` exists |

**Action required:** Create COAP-targeted supplementary artifact (Online Resource 1) after EXP10 completes. The existing EJCO artifact must be revised to:
1. Include EXP10 scripts and results
2. Remove EJCO-specific references
3. Update paths (remove absolute `/home/soroush/` references from documentation)
4. Verify README describes COAP submission context

## 7. PDF Build

`paper_coap/main.pdf` is present and was presumably built successfully (`.aux`, `.bbl`, `.blg`, `.log`, `.out` all present). The PDF should be reviewed for:
- Page count (COAP target: ~25–40 pages for full article)
- Figure rendering (TikZ diagrams, eps/pdf figures)
- Hyperlinks (ORCID, URLs)

Not independently verified in this audit (read-only).

## 8. Submission Checklist (Per COAP Submission Guidelines)

| Item | Status |
|------|--------|
| Cover letter | `submission_files_for_download/cover_letter_draft.pdf` — needs update for COAP resubmission |
| Highlights | `submission_files_for_download/highlights.txt` — verify still accurate |
| Title page (separate) | `submission_files_for_download/title_page.pdf` — needed for double-blind |
| Anonymized PDF | `submission_files_for_download/main_anonymized.pdf` — verify current |
| Supplementary (Online Resource 1) | **NOT YET CREATED** — **BLOCKER** |
| Response to reviewers | N/A for new submission |
| Source files (LaTeX) | Need `.tex` + `.bst` + `.cls` + all assets | Verify before submission |

## 9. Word and Length Limits

COAP research articles have no strict word limit but typically run 25–40 typeset pages. The manuscript structure (8 sections + declarations + bibliography) is consistent with this. No length concern identified.

## 10. Summary

| Category | Status |
|----------|--------|
| Template compliance | ✓ PASS |
| Declarations | ✓ COMPLETE |
| ORCID | ✓ Present (linked workaround) |
| Supplementary artifact | ✗ MISSING — must be created post-EXP10 |
| Cover letter | ✗ Needs update for COAP |
| Anonymous submission package | ✗ Stale (EJCO era) — needs refresh |
