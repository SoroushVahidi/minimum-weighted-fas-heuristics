# Executive Summary — Full Branch Repository Audit

**Date:** 2026-06-12  
**Repository:** `minimum-weighted-fas-heuristics`  
**Branch:** `main` @ `6c04ff1cc19d1887bd5b1b2bd1d1f31dc2b6924a`  
**Target:** COAP submission — *SCC-Local Destroy-and-Repair Heuristics for MWFAS on Sparse Digraphs*

## Bottom line

The repository is **internally consistent, submission-ready, and well-evidenced** at HEAD. Git is clean; local matches `origin/main`; CI passes. Manuscript (45 pp), Online Resource 1 (12 pp), and six-file upload bundle align with committed experiment summaries EXP1b–EXP11.

**No scientific blocker** and **no submission-package blocker** were found. Remaining gaps are **maintainability, metadata, and author-confirmation** items—not integrity defects.

## Scale

| Metric | Value |
|---|---|
| Files inventoried (incl. ignored local) | 17,898 |
| Tracked in inventory | 6,336 |
| Ignored (mostly EXP10 raw/checkpoints, caches) | 11,562 |
| Total size on disk (inventory) | ~0.16 GB |
| pytest | 90 passed, 1 skipped |
| CI run 27393186733 | success (Python 3.11, 3.12) |

## What is complete

- Canonical algorithms in `src/mwfas/` with OR1 mirror
- Full sparse benchmark evidence (EXP1b, EXP4, EXP10)
- Exact/MIP/LOLIB/ablation/supporting studies
- COAP manuscript + declarations + cover letter + related-manuscript statement
- Frozen OR1 PDF/ZIP with validation gate
- Prior adversarial audit (`docs/final_coap_adversarial_audit_20260612/`)

## What remains incomplete

1. **Holdout** — checkpoints without committed `summary/`
2. **`experiments/combined/` digest** — predates EXP6–11
3. **Portal submission** — author action
4. **CAIE/EJCO status** — author confirmation
5. **Public repo / DOI** — deferred (private GitHub OK with OR1)

## Key risks (non-blocking)

| Risk | Mitigation |
|---|---|
| `submission_package/` EJCO confusion | Label stale; never COAP upload |
| Stale portal abstract in copy-ready text | Paste from `main.tex` (238 words) |
| EXP10 progress JSON says NONFINAL | Cosmetic; summaries authoritative |
| Incremental-publication scrutiny | Transparent disclosures in place |

## Recommended next actions (author)

1. Submit via Editorial Manager using `paper_coap/submission/final_upload/`
2. Confirm CAIE/EJCO/JOCO/DAM statuses for portal
3. Post-submission: optional cleanup per `CLEANUP_AND_REORGANIZATION_RECOMMENDATIONS.md`

## Audit deliverables

This directory contains 30+ files: Git/CI state, full file inventory (CSV), architecture map, source/test/experiment/manuscript/OR1/submission audits, dataset/tool registers, issue register, and cleanup recommendations.

**This audit made no code, manuscript, or Git changes** (audit outputs only).
