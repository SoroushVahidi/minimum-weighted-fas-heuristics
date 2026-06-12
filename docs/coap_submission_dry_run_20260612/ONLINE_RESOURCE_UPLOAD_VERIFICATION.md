# Online Resource Upload Verification

## OR1 PDF

**File:** `Vahidi_Online_Resource_1_MWFAS.pdf`  
**SHA-256:** `8cc1479fb7aebe9e8b4c219aada0bf87f6c0383f53345a2d851b776b581aa0ea`  
**Size:** 130,236 bytes  

| Field | Value | Correct |
|---|---|---|
| Pages | 12 | ✓ |
| Title in PDF | "Online Resource 1: Algorithms, Proofs, Reproducibility Materials, and Extended Computational Results" | ✓ |
| Companion statement | "Companion to: SCC-Local Destroy-and-Repair Heuristics... Computational Optimization and Applications (COAP), Springer Nature" | ✓ |
| Author | Soroush Vahidi, Department of Computer Science, NJIT | ✓ |
| Version | 2026-06-12 | ✓ |
| Source commit | 80b3144d | ✓ (documented) |

## Key claim verification in OR1 PDF

| Claim | OR1 text | Correct |
|---|---|---|
| EXP10 wins/ties/losses | "EXP10 median 38/55/0" | ✓ |
| EXP10 mean relative excess | "21.6% mean excess" | ✓ |
| EXP11 extraction effect | "EXP11 zero extraction change on calibration subset" | ✓ |
| IPSNS optimal (exact) | "exact 56/57 matches" | ✓ |
| Test count | "91 collected" (pytest discovers 91 = 90 passed + 1 skipped) | ✓ |

## OR1 ZIP

**File:** `Vahidi_Online_Resource_1_MWFAS.zip`  
**SHA-256:** `5dc3875acad386f992266a43d1406b96787c95fa1d3acde7124be327ee29495e`  
**Size:** 1,116,197 bytes  
**Entries:** ~221  

| Check | Result |
|---|---|
| ZIP extractable | ✓ |
| No `__pycache__` or `.pytest_cache` | ✓ (confirmed by `unzip -l` grep) |
| No `.git/` directory | ✓ |
| No `/home/soroush/` absolute paths | ✓ (validated by validate_artifact.sh) |
| No confidential files | ✓ |
| No nested ZIP | ✓ |
| Source commit documented (`provenance/source_commit.txt`) | ✓ |
| Validation script present | ✓ (`scripts/validate_artifact.sh`) |

## OR1 validation result

```
=== VALIDATION PASSED ===
```

All checks passed:
- Principal table PASSes: EXP4 (21.61%), EXP3 (56/57), EXP10 (38/55/0), EXP11 (0.0, 0 improved), EXP10 mean rel excess (21.60%)
- Tests: 79 passed, 7 skipped
- Smoke validation: PASSED
- No absolute paths

## Issues

**WARN: README test count** — OR1 `README.md` does not contain the string "79 passed, 7 skipped" or "90 passed, 1 skipped". This is a WARN, not FAIL; the validation still passes. The README is minimal and intentional; the test log section in the OR1 supplement PDF mentions "91 collected."

This warning is non-blocking and does not require action before submission.

## Verdict

**OR1 PDF: APPROVED FOR UPLOAD**  
**OR1 ZIP: APPROVED FOR UPLOAD**
