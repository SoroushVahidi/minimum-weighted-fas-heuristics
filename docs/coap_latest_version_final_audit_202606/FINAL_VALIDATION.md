# Final Validation

Date: 2026-06-12

## Version confirmation (starting)

| Check | Expected | Observed |
|---|---|---|
| Commit | 4879f30 | 4879f30 |
| Pages | 24 | 24 |
| Starting SHA | 5ae415c6… | 5ae415c6… |
| Abstract (LaTeX) | ~229 | 229 |
| Keywords | 6 | 6 |
| Main tables in PDF | 10 | 10 (`\input{tables/…}`) |
| Algorithms | 1 | 1 (`alg:ipsns`) |
| Propositions | 3 | 3 |
| References | 25 | 25 |

## Post-correction artifacts

| Check | Result |
|---|---|
| `compileall` | OK |
| Main pytest | **90 passed, 1 skipped** |
| OR1 pytest | **79 passed, 7 skipped** |
| `validate_artifact.sh` | **PASSED** |
| Manuscript/upload PDF parity | identical |
| OR1/upload PDF parity | identical |
| Submission `MANIFEST.sha256` | valid |
| OR1 `MANIFEST.sha256` | valid |
| Handoff PDF parity | identical |

## Final hashes

- Manuscript: `36a01f9235d1d5971f06dd0cfb28a55b05f4ddc2ffa26300dcc495d0520ad144` (201,092 bytes, 24 pages)
- OR1: `3b90f21cd1d2e922fd3d3ee40b613e0a3b17d9590e5ca4eb2134a23a3aded922` (139,204 bytes, 14 pages)

## Numerical values changed in this pass

| Quantity | Before | After |
|---|---|---|
| Manuscript PDF hash | 5ae415c6… | 36a01f92… |
| LOLIB prose | “3.88% lower mean BW” | explicit IPSNS-normalized mean −3.88% |
| CFR10 author | Rurda | Rudra |
| Scientific counts (14/83/0, 38/55/0, etc.) | unchanged | unchanged |
