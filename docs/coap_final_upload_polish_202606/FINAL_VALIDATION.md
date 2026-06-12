# Final validation — pre-submission polish (2026-06-12)

Starting commit: `fb90636`

## Repository state (pre-commit)

- Branch: `main`
- Local == `origin/main` (0 ahead / 0 behind)
- Expected starting manuscript SHA: `36a01f9235d1d5971f06dd0cfb28a55b05f4ddc2ffa26300dcc495d0520ad44`

## Compilation

| Check | Result |
|---|---|
| `latexmk -pdf paper_coap/main.tex` | Success, 24 pages |
| Undefined citations/references | None in PDF |
| `cmp paper_coap/main.pdf paper_coap/submission/final_upload/Vahidi_COAP_Manuscript.pdf` | Byte-identical |
| Handoff PDF vs repository | Byte-identical |

## Tests

| Suite | Result |
|---|---|
| `python3 -m compileall src online_resource_1/src tests online_resource_1/tests` | OK |
| `PYTHONPATH=src python3 -m pytest --ignore=experiments/exp4_external_baselines/external_tools -ra` | **90 passed, 1 skipped** |
| `PYTHONPATH=online_resource_1/src python3 -m pytest online_resource_1/tests -ra` | **79 passed, 7 skipped** |
| `online_resource_1/scripts/validate_artifact.sh` | **VALIDATION PASSED** |
| `git diff --check` | OK |
| `git diff --cached --check` | OK |

## Manifest

```
aebdf183f3a1c794b42b5b8a362524e396eaf7f7c8dd379c6c5b48f4a23bca77  Vahidi_COAP_Manuscript.pdf
1dc1e4c9e1798b93be6515d8b520a2c850f3247e01e2fd199d237e095689f9e0  Vahidi_COAP_Cover_Letter.pdf
9196e304fe38c62a6c650f4e8ed7db03aa824e53685dbaff1194aab376b25ad8  Vahidi_COAP_Manuscript_Source.zip
3b90f21cd1d2e922fd3d3ee40b613e0a3b17d9590e5ca4eb2134a23a3aded922  Vahidi_Online_Resource_1_MWFAS.pdf
0c4ef12d03266c65b2ef63d4c9f8c69f2348054e696c37065062b85bc2a248db  Vahidi_Online_Resource_1_MWFAS.zip
d5a53ddde6bc0fdaa2112a3497db42ad7cb472904925ea23da7dad94f56abc17  Vahidi_Related_Manuscripts_Statement.pdf
```

## Verified scientific values (unchanged)

- 96/97 minimum observed (ties credited); 14 strict unique bests
- 14/83/0 vs better seed
- 56/57 exact optimum; 0.0031% mean optimum-normalized gap; r20_60 3-unit / 0.178% gaps
- 38/55/0 vs DRMacIver/FAS; 21.60% mean comparator-normalized reduction
- 45/50 dense LOLIB best for DRMacIver/FAS; −3.88% mean instance-level IPSNS-normalized dense gap

## Online Resource 1

No substantive OR1 rebuild required (no main-paper table-number cross-references changed in OR1).

## Editorial Manager handoff

Path: `/home/soroush/COAP_initial_submission/Vahidi_COAP_Manuscript.pdf` (single file, byte-identical to repository PDF).
