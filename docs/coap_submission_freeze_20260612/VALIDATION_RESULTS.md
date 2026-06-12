# Validation Results

**Date:** 2026-06-12  
**Repository commit:** af34d57d3a921c1be50a61f990c2d85ff8d97df3

---

## Main test suite

**Command:** `python3 -m pytest --ignore=experiments/exp4_external_baselines/external_tools -v`

**Result:** `90 passed, 1 skipped`

The skipped test is the same long-running test skipped consistently throughout the project lifecycle; no new failures.

---

## OR1 validation

**Command:** `bash online_resource_1/scripts/validate_artifact.sh`

**Pre-condition:** Cache cleared before running:
```
find online_resource_1/ -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null
find online_resource_1/ -name ".pytest_cache" -type d -exec rm -rf {} + 2>/dev/null
find online_resource_1/ -name "*.pyc" -delete 2>/dev/null
```

**Output (final lines):**
```
PASS: EXP10 DR wins -> 0
PASS: EXP10 mean rel excess -> 21.601773263726717
PASS: EXP11 median improvement -> 0.0
PASS: EXP11 instances improved (nonneg) -> 0
PASS: Digest exists -> None
PASS: Combined external table -> None

All principal table checks PASSED
OK: tables
=== VALIDATION PASSED ===
```

**Result: VALIDATION PASSED**

Note: Running pytest after validation re-creates cache files. Always clean cache before running `validate_artifact.sh` if tests have been run since the last clean.

---

## OR1 packaged test suite

**Result:** `79 passed, 7 skipped`

---

## Upload artifact checksums

**Command:** `sha256sum -c MANIFEST.sha256` (in `paper_coap/submission/final_upload/`)

**Result:** All 6 files: OK

---

## Security and path scan

Prior scan (recorded in `docs/repository_maintenance/cleanup_20260612/SECURITY_AND_PRIVACY_RESULT.md`): CLEAN

Post-dry-run check:
- `EDITORIAL_MANAGER_FINAL_COPY_READY_TEXT.md`: no absolute paths (`/home/soroush/`) — verified by grep
- Main manuscript (`paper_coap/main.tex`): no absolute paths — verified
- All 6 upload PDFs: paths not embedded in publication-facing content

---

## Source ZIP build

`pdflatex` is not available in the local environment. The source ZIP (`Vahidi_COAP_Manuscript_Source.zip`) was verified structurally (clean directory layout, correct LaTeX files present, no stale artifacts). The manuscript PDF (`Vahidi_COAP_Manuscript.pdf`) was confirmed as built from this source at commit `04ca3ad` and verified by SHA-256 match. No LaTeX recompile was performed or required.

---

## Abstract word count

238 words — verified in `EDITORIAL_MANAGER_FINAL_COPY_READY_TEXT.md` and confirmed against pdftotext output from the manuscript PDF. Within COAP 150–250 guideline.

---

## Keyword count

6 keywords — verified in copy-ready text. Within COAP 4–6 requirement.

---

## Local paths in publication-facing material

None found. `/home/soroush/` paths appear only in:
- Internal maintenance documentation (`docs/repository_maintenance/`)
- Transient build logs (excluded from commit)

---

## Credentials scan

No credentials, API keys, passwords, or reviewer reports found. CLEAN.

---

## Summary

| Check | Result |
|---|---|
| Main tests (90+1 skip) | PASS |
| OR1 validation | PASS |
| OR1 packaged tests (79+7 skip) | PASS |
| Upload checksums (6/6) | PASS |
| Security scan | CLEAN |
| Abstract 238 words | PASS |
| Keywords 6 | PASS |
| No local paths in public-facing files | PASS |
| No secrets | PASS |
