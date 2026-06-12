# Submission Package Audit

**Audit date:** 2026-06-10

## Packages found

| Package | Path | Venue | Status |
|---|---|---|---|
| EJCO full package | `submission_package/` | EJCO | Committed; **stale for COAP** |
| EJCO source ZIP | `submission_package/ejco_source.zip` | EJCO | Stale (no formal analysis) |
| EJCO repro ZIP | `submission_package/ejco_reproducibility_artifact.zip` | EJCO | Code synced; branding wrong |
| EJCO upload files | `submission_package/ejco_files_for_upload/` | EJCO | Historical |
| Anonymous artifact | `submission_package/anonymous_artifact/` | Review | Partial |
| Download bundle | `submission_files_for_download/` | CAIE/anonymized | Historical PDFs |
| **COAP package** | — | COAP | **Does not exist** |

## EJCO package contents (audit)

| Component | Present | COAP-safe? |
|---|---|---|
| Manuscript PDF | `ejco_files_for_upload/main_manuscript.pdf` | **No** — wrong venue |
| Source ZIP | `ejco_source.zip` | **No** — missing COAP sections |
| Reproducibility ZIP | `ejco_reproducibility_artifact.zip` | **No** — EJCO metadata |
| Title page | EJCO-specific | **No** |
| Cover letter | EJCO draft (PDF gitignored in files_for_upload) | **No** |
| Highlights | EJCO format | **No** |
| Supplementary | Anonymous artifact staging | Rebuild as ESM_1 |
| Reviewer suggestions | Not verified for COAP | **Missing** |
| Declarations | In ejco_source | Partially reusable |
| Upload manifest | EJCO checklist in git history | **Missing for COAP** |

## Valid COAP package today?

**No.** Uploading EJCO materials to COAP would be incorrect and risks wrong template, missing related-manuscript uploads, and wrong supplementary naming.

## Files safe vs unsafe to upload

| Safe (after refresh) | Unsafe as-is |
|---|---|
| `paper_coap/main.pdf` (rebuild before upload) | `submission_package/ejco_*` |
| `paper_coap/` LaTeX source tree | `paper/main.pdf` (CAIE/EJCO) |
| Future `ESM_1.zip` | `submission_files_for_download/main_anonymized.pdf` |
| COAP cover letter (to write) | EJCO highlights file |

## Missing for COAP submission

1. COAP cover letter with related-manuscript disclosure
2. `ESM_1.zip` (Online Resource 1)
3. Suggested reviewers list
4. Related unpublished manuscript PDFs (TBD)
5. COAP upload checklist / manifest
6. Optional separate title page (portal-dependent)

## Recommendation

Create new `submission_coap/` directory in a **future pass** (not this audit). Do not rename or upload EJCO package to COAP portal.
