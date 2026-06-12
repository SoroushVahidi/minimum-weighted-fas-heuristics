# Executive Summary — COAP Manuscript Reframing

**Audit date:** 2026-06-11  
**Branch:** `main`  
**HEAD:** `80b3144d5fdbbe250faed8a4fe671dde2da76c89`  
**EXP10 modified:** No (experiments/checkpoints/logs untouched by this task)  
**Source code modified by this task:** No (`src/mwfas/ipsns.py` pre-existing modification not part of this pass)

---

## Required final conclusions (25 questions)

| # | Question | Answer |
|---|----------|--------|
| 1 | **Selected title?** | **SCC-Local Destroy-and-Repair Heuristics for Minimum Weighted Feedback Arc Set on Sparse Digraphs** (running head: SCC-Local Heuristics for MWFAS on Sparse Digraphs) |
| 2 | **IPSNS first and primary?** | **Yes** — title, abstract, §1 contributions item 1, §4 IPSNS subsection, conclusion |
| 3 | **LR-TA inherited/refined?** | **Yes** — DF03 + arXiv VK; “refined sparse-graph engineering variant,” not new approximation theorem |
| 4 | **arXiv:2412.16181 disclosed?** | **Yes** — §2.1, declarations, bib `VahidiKoutis2024arxiv` |
| 5 | **WMSF properly attributed?** | **Yes** — CC25 engineered variant; CCP24 lineage added; not a new algorithm |
| 6 | **IPSNS novelty narrow/defensible?** | **Yes** — “FAS-specific integration” of SCC neighborhoods, scoring, destroy/repair, incumbent protection |
| 7 | **Propositions supporting not central?** | **Yes** — “Supporting correctness properties”; proofs deferred to OR1 |
| 8 | **Global best-known/SOTA claims removed?** | **Yes** — replaced with “best observed among the evaluated methods”; SOTA only negated for calibration baselines |
| 9 | **Sparse scope explicit?** | **Yes** — title, abstract, §1, limitations item 1 |
| 10 | **LOLIB limitation explicit?** | **Yes** — abstract, §1, §6, §7, limitations item 2, conclusion |
| 11 | **Abstract safe pending EXP10?** | **Yes** — no repeated-run medians; `% EXP10-INTEGRATION` comment only in source |
| 12 | **Placeholders noncompiled?** | **Yes** — 6 EXP10 anchors are LaTeX comments; verified absent from PDF |
| 13 | **“Fully reproducible” qualified?** | **Yes** — declarations and abstract use code/configs/summaries + future OR1 |
| 14 | **Key references verified?** | **Yes** — see `BIBLIOGRAPHY_VERIFICATION.md`; CCP24 added |
| 15 | **Distinct from preprint?** | **Yes** — IPSNS-first title, unified framework, expanded validation, explicit prior-work subsection |
| 16 | **Contribution list suitable for COAP?** | **Yes** — algorithm-engineering + computational evidence hierarchy |
| 17 | **Shorter or more focused?** | **More focused** — proofs removed from main text; framing tightened; page count 40 → 42 (+CCP24/disclosure text) |
| 18 | **Depends on EXP10?** | Stochastic robustness wording (abstract, §1, §5 anchor, §7 item 8, §8); possible §5 subsection/table |
| 19 | **Depends on holdout?** | Holdout described in §5; full holdout integration in §6 may remain if detailed table not yet in main results |
| 20 | **Depends on OR1?** | Detailed proofs, final supplementary archive, fully consolidated reproducibility package |
| 21 | **Missing author predecessor info?** | JOCO LR-TA manuscript ID/outcome; DAM IPSNS ID/outcome; CAIE/EJCO submission status/dates |
| 22 | **Build successful?** | **Yes** |
| 23 | **New page count?** | **42** (pre-edit: 40) |
| 24 | **Blocking LaTeX issues?** | **None** |
| 25 | **Next task after EXP10?** | Run finalize pipeline → integrate EXP10 at all anchors → rebuild PDF → begin OR1 + cover letter |

---

## Claim register summary

| Metric | Pre-edit | Post-edit |
|--------|----------|-----------|
| Term matches scanned | 114 | 115 |
| High-risk items addressed | 2 (`fully reproducible`; `all tested methods`) | 0 remaining at same risk |
| Qualified | — | 33 |
| Retained with evidence | — | 81 |
| Pending OR1 | — | 1 |
| Pending EXP10 (comment anchors) | — | 6 |

---

## Deliverables created

`docs/coap_manuscript_reframing_20260611/`:

1. `EXECUTIVE_SUMMARY.md` (this file)
2. `PRE_EDIT_CLAIM_REGISTER.csv`
3. `TITLE_OPTIONS_AND_DECISION.md`
4. `SECTION_CHANGE_LOG.md`
5. `PRIOR_WORK_DISCLOSURE_MATRIX.md`
6. `COVER_LETTER_DISCLOSURE_DRAFT.md`
7. `EXP10_INTEGRATION_LOCATIONS.csv`
8. `BIBLIOGRAPHY_VERIFICATION.md`
9. `POST_EDIT_CLAIM_REGISTER.csv`
10. `BUILD_AND_VISUAL_CHECK.md`
11. `REMAINING_MANUSCRIPT_GAPS.md`
12. `audit_metadata.json`

Pre-edit backup: `docs/coap_manuscript_reframing_20260611/paper_coap_pre_edit_backup/`

---

## Unresolved blockers

1. EXP10 numerical integration (in progress externally).
2. Online Resource 1 not yet built.
3. Author-supplied predecessor submission metadata for cover letter.
4. Pre-existing `src/mwfas/ipsns.py` modification unrelated to this manuscript task (not touched).

---

## Manuscript files modified

`main.tex`, `bibliography/references.bib`, `declarations/statements_and_declarations.tex`, `sections/01_introduction.tex`, `sections/02_related_work.tex`, `sections/04_algorithmic_framework.tex`, `sections/04_formal_analysis.tex`, `sections/05_experimental_design.tex`, `sections/06_results.tex`, `sections/07_discussion.tex`, `sections/08_conclusion.tex`, `tables/table_algorithm_components.tex`, `main.pdf`

**Numerical tables unchanged.**
