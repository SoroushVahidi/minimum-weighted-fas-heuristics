# Online Resource 1 Audit

**HEAD:** `6c04ff1`  
**PDF pages:** 12  
**ZIP entries:** 216

## Canonical artifacts

| Artifact | Path | SHA-256 |
|---|---|---|
| OR1 PDF (submit) | `paper_coap/submission/final_upload/Vahidi_Online_Resource_1_MWFAS.pdf` | `8cc1479fb7aebe9e8b4c219aada0bf87f6c0383f53345a2d851b776b581aa0ea` |
| OR1 ZIP (submit) | `paper_coap/submission/final_upload/Vahidi_Online_Resource_1_MWFAS.zip` | `5dc3875acad386f992266a43d1406b96787c95fa1d3acde7124be327ee29495e` |
| Root mirror PDF/ZIP | `Vahidi_Online_Resource_1_MWFAS.{pdf,zip}` | **Identical** to final_upload |
| Source tree | `online_resource_1/` | Built from repo via `finalize_or1.py` |

## Structure

```
online_resource_1/
├── supplement/online_resource_1.tex  → PDF (S1–S15)
├── src/mwfas/                        → code mirror
├── tests/                            → packaged pytest
├── results/exp{3,4,10,11}/           → committed summaries
├── scripts/validate_artifact.sh      → integrity gate
├── manifests/, provenance/           → claim maps, commit SHA
├── environment/                      → requirements freeze
└── MANIFEST.sha256
```

## Validation (this audit)

`online_resource_1/scripts/validate_artifact.sh`:

- **PASSED** (after removing local `__pycache__` from audit pytest)
- Tests: 79 passed, 7 skipped (EXP10 live tree not bundled)
- Principal table checks: EXP3, EXP4, EXP10, EXP11 numbers match manuscript

## Consistency checks

| Check | Result |
|---|---|
| No `/home/soroush` paths in OR1 text | Pass |
| No confidential files | Pass |
| EXP10 integrated (S11) | Pass |
| EXP11 integrated (S12) | Pass |
| Test counts documented (S13) | Pass — distinguishes full vs OR1 |
| Proofs for propositions (S4) | Pass |
| Stale ZIP inside ZIP | None detected |
| Match main manuscript abstract/post-EXP10 wording | Pass at f306c15/6c04ff1 OR1 content (manuscript-only edits in 6c04ff1 did not require OR1 rebuild) |

## Clean extraction

Prior audit (`docs/coap_online_resource_finalization_20260611/`) validated clean extraction. Source commit recorded in `provenance/source_commit.txt`.

## Reproducibility scripts

| Script | Purpose |
|---|---|
| `validate_artifact.sh` | Full gate |
| `reproduce_smoke.sh` | Tiny instances |
| `reproduce_tests.sh` | Packaged pytest |
| `reproduce_principal_tables.sh` | Summary → table numbers |
| `optional_full_reproduction.sh` | Documents full rerun requirements |

## Gaps

- Raw EXP10 per-run JSON **not** bundled (by policy; documented).
- DRMacIver binary **not** bundled.
- Full benchmark `.d` files **not** bundled.

## Verdict

OR1 is **complete, validated, and consistent** with the COAP manuscript. Safe for portal upload.
