# SN Computer Science Upload Bundle — Pass 1 (READY FOR HUMAN REVIEW BEFORE SNCS SUBMISSION)

**Status:** working draft prepared during the first SNCS retargeting pass (2026-06-17). See `docs/sncs_preparation_202606/SUBMISSION_PACKAGE_STATUS.md` for the full pass status and `docs/sncs_preparation_202606/OVERLAP_AND_DISCLOSURE_AUDIT.md` for the disclosure analysis. This bundle is ready for human review before SN Computer Science submission, but it is not yet ready for final journal upload.

## Contents

| File | Purpose | Source |
|---|---|---|
| `Vahidi_SNCS_Manuscript.pdf` | Manuscript / main document | Built in this pass from `paper_sncs/main.tex` |
| `Vahidi_SNCS_Source.zip` | LaTeX source bundle (if requested by the portal) | Flattened backup package containing exactly one `.tex` file plus the required support files |
| `Vahidi_SNCS_Online_Resource_1.pdf` | Online Resource 1 (readable PDF) | Copied unchanged from the frozen, verified COAP bundle (`paper_coap/submission/final_upload/Vahidi_Online_Resource_1_MWFAS.pdf`); content is venue-agnostic (reproducibility appendix), so it is reused rather than rebuilt |
| `Vahidi_SNCS_Online_Resource_1.zip` | Online Resource 1 (full reproducibility archive) | Copied unchanged from the frozen, verified COAP bundle (`paper_coap/submission/final_upload/Vahidi_Online_Resource_1_MWFAS.zip`) |
| `MANIFEST.sha256` | SHA-256 checksums for the four files above | Generated in this pass |

Verify SHA-256 against `MANIFEST.sha256` before any upload.

## Editorial Manager initial-upload plan

Recommended initial upload: upload `Vahidi_SNCS_Manuscript.pdf` as the main Manuscript file.
`Vahidi_SNCS_Source.zip` is a backup LaTeX source package. It contains exactly one `.tex` file, `Vahidi_SNCS_Main.tex`, plus required bibliography/style/class/figure support files. Upload it only if Editorial Manager requests LaTeX source files.

## Deliberately not included in this pass

- **SNCS cover letter** — not yet drafted. A COAP cover letter exists at `paper_coap/submission/cover_letter.tex` but is COAP-specific and must not be reused verbatim. See `docs/sncs_preparation_202606/OVERLAP_AND_DISCLOSURE_AUDIT.md` §6b for the recommended disclosure paragraph to include once drafted.
- **SNCS related-manuscripts statement** — not yet drafted; see `docs/sncs_preparation_202606/OVERLAP_AND_DISCLOSURE_AUDIT.md` §6a/§6b for the required wording.

## Remaining items before actual SNCS submission

1. SNCS cover letter and related-manuscripts statement must be drafted using the wording in the overlap audit.
2. A human author must review the full manuscript (not just the sections touched in this pass) for SNCS fit before upload.
3. Pass 2B manuscript edits have addressed the rejection-risk audit findings; the next step is Pass 2C human review and final submission-readiness checking before actual SNCS submission.

This bundle exists to validate that the manuscript, source, and Online Resource 1 build and package correctly. Recommended initial upload: PDF only. Keep `Vahidi_SNCS_Source.zip` as backup unless the portal explicitly requires LaTeX source files.
