# Validation Results

**Date:** 2026-06-12  
**Validation pass:** Task 5 Phase 14

---

## Test suite (main repository)

**Command:** `PYTHONPATH=src python3 -m pytest --ignore=experiments/exp4_external_baselines/external_tools -q`

**Result:** 90 passed, 1 skipped in 1.22s

**Verdict:** PASS — no regressions from any Task 5 change.

---

## PDF validation

| File | Valid PDF? | Size | Notes |
|---|---|---|---|
| Vahidi_COAP_Cover_Letter.pdf | YES — %PDF- header | 24,716 bytes | Rebuilt from updated cover_letter.tex |
| Vahidi_COAP_Manuscript.pdf | YES — %PDF- header | 333,231 bytes | Rebuilt from updated §2 and declarations |
| Vahidi_Related_Manuscripts_Statement.pdf | YES — %PDF- header | 23,672 bytes | Rebuilt from updated related_manuscripts_statement.tex |
| Vahidi_Online_Resource_1_MWFAS.pdf | YES (unchanged) | 130,236 bytes | Hash unchanged from v1 freeze |

---

## Upload artifact checksums (final)

| Artifact | SHA-256 | Changed from v1? |
|---|---|---|
| Vahidi_COAP_Manuscript.pdf | `13aec51a53baf5e34d7ed5391c32e4af5c12f67daee551627499be85817e6563` | YES |
| Vahidi_COAP_Cover_Letter.pdf | `b0fd9d0ab4d760a16b75a3336bfa450685b825a9ec32f5cb74c4a685c54e1c29` | YES |
| Vahidi_COAP_Manuscript_Source.zip | `ed198a719a29abb2bf6ba7e4bde1423d6770ee184cfd546a24d562da8c52c1c5` | YES |
| Vahidi_Online_Resource_1_MWFAS.pdf | `8cc1479fb7aebe9e8b4c219aada0bf87f6c0383f53345a2d851b776b581aa0ea` | NO |
| Vahidi_Online_Resource_1_MWFAS.zip | `5dc3875acad386f992266a43d1406b96787c95fa1d3acde7124be327ee29495e` | NO |
| Vahidi_Related_Manuscripts_Statement.pdf | `9af3b73e9c6ad06c8843c42864acd15e7321cd236a78fd85847ea8779cbb4636` | YES |

---

## Unresolved-status language scan

**Command:** `grep -r "AUTHOR-STATUS|status unknown|package prepared|outcome recorded elsewhere|STATUS VERIFICATION REQUIRED|JOCO/DAM STATUS|CONFIRM BEFORE PASTING" paper_coap/`

**Result:** No matches found. All unresolved-status placeholders removed.

---

## Abstract word count

Abstract word count: 238 (unchanged from v1 freeze). No abstract text was modified.

---

## Keywords

6 keywords (unchanged): Minimum weighted feedback arc set; Combinatorial optimization; Local-ratio algorithm; Strongly connected components; Heuristic search; Algorithm engineering

---

## OR1 validation

OR1 ZIP SHA-256 unchanged from Task 3 validation. OR1 pytest: 79 passed, 7 skipped (from Task 3; OR1 not modified).

---

## Confidential material check

No decision letters, rejection emails, reviewer reports, screenshots, or portal exports were committed. All rejection reasons and confidential correspondence excluded from repository.
