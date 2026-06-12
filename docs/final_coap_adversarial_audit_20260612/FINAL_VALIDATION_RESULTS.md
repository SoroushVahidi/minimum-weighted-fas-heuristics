# Final Validation Gate Results

**Audit date:** 2026-06-12  
**Post-correction validation**

## Pytest (full repository)

```
Command: PYTHONPATH=src python3 -m pytest --ignore=experiments/exp4_external_baselines/external_tools -q
Result: 90 passed, 1 skipped, 2 warnings
Log: docs/final_coap_adversarial_audit_20260612/logs/pytest.log
Skipped: tests/regression/test_exp10_namespace.py (DRMacIver runner not active)
```

## Main manuscript build

```
Engine: tectonic
Output: paper_coap/main.pdf
Pages: 45
SHA-256: 97eb61238a81e12e2597a6963926f0f092ad994f3f369b89715f36e9e06d0898
Log: logs/main_build.log
```

## Online Resource 1 build

```
Engine: tectonic
Output: online_resource_1/supplement/online_resource_1.pdf (unchanged content vs upload at f306c15)
Pages: 12
Log: logs/or1_build.log
```

## OR1 artifact validation

```
Command: online_resource_1/scripts/validate_artifact.sh
Result: VALIDATION PASSED
Tests in OR1 package: 79 passed, 7 skipped
Principal tables: PASSED (EXP4 21.6076%, EXP3 56/57, EXP10 38/55/0, EXP11 0 improvement)
Log: logs/artifact_validation.log
Note: Initial fail due to __pycache__ from audit pytest; caches removed; re-run passed
```

## Source package validation

```
File: paper_coap/submission/final_upload/Vahidi_COAP_Manuscript_Source.zip
Clean extraction compile: PASS (tectonic main.tex → 45 pages)
SHA-256: 0fd2b2c138c31798ff334a47f7d5c917fd32ec83aa5b05b932c82c20a32f7b38
Log: logs/source_package_validation.log
```

## Upload bundle checksums (post-correction)

| File | SHA-256 |
|---|---|
| Vahidi_COAP_Manuscript.pdf | `97eb61238a81e12e2597a6963926f0f092ad994f3f369b89715f36e9e06d0898` |
| Vahidi_COAP_Manuscript_Source.zip | `0fd2b2c138c31798ff334a47f7d5c917fd32ec83aa5b05b932c82c20a32f7b38` |
| Vahidi_COAP_Cover_Letter.pdf | `df6622bd7b19f2ed73e5d54c38e953a2092f9436f574db4da86b374efe6496f8` |
| Vahidi_Online_Resource_1_MWFAS.pdf | `8cc1479fb7aebe9e8b4c219aada0bf87f6c0383f53345a2d851b776b581aa0ea` |
| Vahidi_Online_Resource_1_MWFAS.zip | `5dc3875acad386f992266a43d1406b96787c95fa1d3acde7124be327ee29495e` |
| Vahidi_Related_Manuscripts_Statement.pdf | `7e5ee12c4200ff0a006f350b379d63a1dc38dccbc588ab7dbb62e241a08b519e` |

## Placeholder / confidentiality scan

| Check | Result |
|---|---|
| Placeholders in upload PDFs | None detected |
| Absolute /home paths in OR1 | None (post-validation) |
| Confidential correspondence in upload | None |
| Stale venue names in manuscript PDF | None (COAP throughout) |

## Corrections applied before this validation

1. Abstract trimmed to 238 words.
2. Related-work EXP10 wording corrected.
3. Manuscript PDF and source ZIP refreshed in `final_upload/`.
