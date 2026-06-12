# Executive Summary: Rejection History Cleanup

**Date:** 2026-06-12  
**Task:** Remove unnecessary prior-submission history from COAP submission materials while preserving scientific attribution.

---

## What was done

Removed editorial rejection history from all reviewer-facing and manuscript-body files. Preserved all scientific provenance, algorithm attribution, and concurrent-submission compliance. Four upload artifacts were rebuilt; OR1 was unchanged.

---

## Files changed

| File | Change |
|---|---|
| `paper_coap/sections/02_related_work.tex` | Removed journal names, manuscript IDs (JOCO-D-26-00099, DA19469), and "rejected" from predecessor paragraphs; removed CAIE/EJCO paragraph entirely |
| `paper_coap/declarations/statements_and_declarations.tex` | Replaced detailed rejection list (four venues + "rejected") with concise statement referencing §2 and declaring no active concurrent submission |
| `paper_coap/submission/cover_letter.tex` | Rewritten related-manuscripts paragraph: now uses Phase 3 preferred wording — arXiv disclosure, concurrent-submission declaration, offer to supply overlap on request |
| `paper_coap/submission/related_manuscripts_statement.tex` | Status language changed from "rejected; no longer under consideration" to "earlier unpublished author manuscript; no longer under consideration"; venue labels changed to scientific descriptions; upload policy set to on-request-only |
| `paper_coap/submission/EDITORIAL_MANAGER_FINAL_COPY_READY_TEXT.md` | Cleared header simplified (rejection list removed); portal text updated to Phase 5 preferred wording; upload table updated to mark related-manuscript statement as on-request-only |

---

## Scientific attribution preserved

- arXiv:2412.16181 preprint cited and described in §2 — YES
- LR-TA predecessor manuscript described (code-level match, benchmark scope) — YES
- IPSNS predecessor manuscript described (algorithmic core, benchmark scope) — YES
- LR-TA attribution (Demetrescu–Finocchi lineage) — YES
- WMSF attribution (Cavallaro–Cutello) — YES
- IPSNS novelty positioned cautiously — YES
- Contribution increments listed (i–vi) — YES

---

## Concurrent-submission compliance preserved

- Cover letter declares: "No substantially overlapping manuscript is currently under consideration elsewhere." — YES
- Declarations state: "No substantially overlapping manuscript is currently under consideration elsewhere." — YES
- Portal text includes: "No substantially overlapping manuscript is currently under consideration elsewhere." — YES

---

## Upload policy

| File | Policy |
|---|---|
| Vahidi_COAP_Manuscript.pdf | Upload — required |
| Vahidi_COAP_Cover_Letter.pdf | Upload — required |
| Vahidi_COAP_Manuscript_Source.zip | Upload — required |
| Vahidi_Online_Resource_1_MWFAS.pdf | Upload — required |
| Vahidi_Online_Resource_1_MWFAS.zip | Upload — required |
| Vahidi_Related_Manuscripts_Statement.pdf | **Do not upload at initial submission** — supply only if portal or editor explicitly requests it |

---

## Final artifact checksums

| Artifact | SHA-256 | Changed? |
|---|---|---|
| Vahidi_COAP_Manuscript.pdf | `2da6f051a353b55350ad46bb3f945a17aa6953c726e5b6fd3b3c5d4d90f84b87` | YES (v2→v3) |
| Vahidi_COAP_Cover_Letter.pdf | `ef3ea9cd08b1d922435d07c9b6b3d2bacec00d95ef0307af4434c51196a7880a` | YES |
| Vahidi_COAP_Manuscript_Source.zip | `f748c7a32fd83cff2291abf105b6b1d8b09dc5d1a77a9294b71fc09fe9c816ec` | YES |
| Vahidi_Online_Resource_1_MWFAS.pdf | `8cc1479fb7aebe9e8b4c219aada0bf87f6c0383f53345a2d851b776b581aa0ea` | NO |
| Vahidi_Online_Resource_1_MWFAS.zip | `5dc3875acad386f992266a43d1406b96787c95fa1d3acde7124be327ee29495e` | NO |
| Vahidi_Related_Manuscripts_Statement.pdf | `86fc208163d36d89a3683df90731d41cfa5b840d83c72a04681cda968b90ddd6` | YES |

---

## Validation

- Test suite: **90 passed, 1 skipped** — no regressions
- `paper_coap/main.pdf` byte-identical with `final_upload/Vahidi_COAP_Manuscript.pdf`
- No rejection history in any reviewer-facing source file
- No journal manuscript IDs in manuscript body

---

## GitHub download path

```
https://github.com/SoroushVahidi/minimum-weighted-fas-heuristics/raw/main/paper_coap/main.pdf
```
