# Validation Results

**Date:** 2026-06-12  
**Pass:** Phase 11 validation

---

## Test suite

**Command:** `PYTHONPATH=src python3 -m pytest --ignore=experiments/exp4_external_baselines/external_tools -q`

**Result:** 90 passed, 1 skipped in 1.25s

**Verdict:** PASS — no regressions.

---

## PDF validation

| File | Valid PDF? | Size | Notes |
|---|---|---|---|
| Vahidi_COAP_Manuscript.pdf | YES — %PDF- header | 331,577 bytes | Rebuilt; byte-identical with paper_coap/main.pdf |
| Vahidi_COAP_Cover_Letter.pdf | YES — %PDF- header | 21,601 bytes | Rebuilt; no rejection history |
| Vahidi_Related_Manuscripts_Statement.pdf | YES — %PDF- header | 22,957 bytes | Rebuilt; neutral language; on-request only |
| Vahidi_Online_Resource_1_MWFAS.pdf | YES (unchanged) | 130,236 bytes | Hash unchanged |

---

## Rejection-history scan (reviewer-facing sources)

**Files scanned:** `paper_coap/sections/` and `paper_coap/declarations/`

**Terms searched:** JOCO, DA19469, Discrete Applied Mathematics, Computers & Industrial Engineering, CAIE, EURO Journal on Computational Optimization, EJCO, rejected, rejection, previous submission, prior submission, under consideration, related manuscript

**Findings:**
- `sections/04_algorithmic_framework.tex` line 84: "the move is rejected" — ALGORITHMIC USAGE; retain
- `sections/04_algorithmic_framework.tex` line 128: "accepted-or-rejected IPSNS iterations" — ALGORITHMIC USAGE; retain
- `sections/06_results.tex` line 26: "two DAG inputs rejected by the wrapper" — TECHNICAL USAGE; retain
- No editorial history found in any reviewer-facing source file

---

## Cover letter scan

**Terms searched:** JOCO, DA19469, Discrete Applied, Computers & Industrial, CAIE, EURO Journal, EJCO, rejected

**Result:** None of the specified terms found in cover_letter.pdf. PASS.

---

## Manuscript identity checks

| Check | Result |
|---|---|
| `paper_coap/main.pdf` SHA-256 | `2da6f051a353b55350ad46bb3f945a17aa6953c726e5b6fd3b3c5d4d90f84b87` |
| `final_upload/Vahidi_COAP_Manuscript.pdf` SHA-256 | `2da6f051a353b55350ad46bb3f945a17aa6953c726e5b6fd3b3c5d4d90f84b87` |
| Byte-identical? | YES |
| Abstract word count | 238 (unchanged) |
| Keywords count | 6 (unchanged) |

---

## Final artifact checksums

| Artifact | SHA-256 |
|---|---|
| Vahidi_COAP_Manuscript.pdf | `2da6f051a353b55350ad46bb3f945a17aa6953c726e5b6fd3b3c5d4d90f84b87` |
| Vahidi_COAP_Cover_Letter.pdf | `ef3ea9cd08b1d922435d07c9b6b3d2bacec00d95ef0307af4434c51196a7880a` |
| Vahidi_COAP_Manuscript_Source.zip | `f748c7a32fd83cff2291abf105b6b1d8b09dc5d1a77a9294b71fc09fe9c816ec` |
| Vahidi_Online_Resource_1_MWFAS.pdf | `8cc1479fb7aebe9e8b4c219aada0bf87f6c0383f53345a2d851b776b581aa0ea` |
| Vahidi_Online_Resource_1_MWFAS.zip | `5dc3875acad386f992266a43d1406b96787c95fa1d3acde7124be327ee29495e` |
| Vahidi_Related_Manuscripts_Statement.pdf | `86fc208163d36d89a3683df90731d41cfa5b840d83c72a04681cda968b90ddd6` |
