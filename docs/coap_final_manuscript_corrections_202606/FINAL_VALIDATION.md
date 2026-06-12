# Final Validation

Date: 2026-06-12

## Commands and results

| Check | Result |
|---|---|
| `python3 -m compileall src online_resource_1/src tests online_resource_1/tests` | OK |
| `PYTHONPATH=src python3 -m pytest --ignore=experiments/exp4_external_baselines/external_tools -ra` | **90 passed, 1 skipped** |
| `PYTHONPATH=online_resource_1/src python3 -m pytest online_resource_1/tests -ra` | **79 passed, 7 skipped** |
| `online_resource_1/scripts/validate_artifact.sh` | **VALIDATION PASSED** |
| `cmp paper_coap/main.pdf paper_coap/submission/final_upload/Vahidi_COAP_Manuscript.pdf` | identical |
| `cmp online_resource_1/Online_Resource_1.pdf paper_coap/submission/final_upload/Vahidi_Online_Resource_1_MWFAS.pdf` | identical |
| `sha256sum -c online_resource_1/MANIFEST.sha256` | all entries OK |
| `sha256sum -c paper_coap/submission/final_upload/MANIFEST.sha256` | all entries OK |

## Manuscript metadata

- SHA-256: `5ae415c68fa307fa3fa6726b39eb4af67ac78dbc1b37bff856f30732aa67827e`
- Size: 199,379 bytes
- Pages: 24
- Abstract: 229 words
- Keywords: 6

## Handoff parity (local)

`/home/soroush/COAP_initial_submission/Vahidi_COAP_Manuscript.pdf` matches `paper_coap/main.pdf`.

Remote GitHub parity to be verified immediately after push.
