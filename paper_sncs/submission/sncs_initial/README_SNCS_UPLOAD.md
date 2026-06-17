# SN Computer Science Upload Bundle — Pass 1 (Draft, Not Submission-Ready)

**Status:** working draft prepared during the first SNCS retargeting pass (2026-06-17). See `docs/sncs_preparation_202606/SUBMISSION_PACKAGE_STATUS.md` for the full pass status and `docs/sncs_preparation_202606/OVERLAP_AND_DISCLOSURE_AUDIT.md` for the disclosure analysis that must be resolved before this bundle is actually uploaded to the SN Computer Science portal.

## Contents

| File | Purpose | Source |
|---|---|---|
| `Vahidi_SNCS_Manuscript.pdf` | Manuscript / main document | Built in this pass from `paper_sncs/main.tex` |
| `Vahidi_SNCS_Source.zip` | LaTeX source bundle (if requested by the portal) | Zipped from `paper_sncs/` (excludes `main.pdf`, this `sncs_initial/` directory, and LaTeX build artifacts) |
| `Vahidi_SNCS_Online_Resource_1.pdf` | Online Resource 1 (readable PDF) | Copied unchanged from the frozen, verified COAP bundle (`paper_coap/submission/final_upload/Vahidi_Online_Resource_1_MWFAS.pdf`); content is venue-agnostic (reproducibility appendix), so it is reused rather than rebuilt |
| `Vahidi_SNCS_Online_Resource_1.zip` | Online Resource 1 (full reproducibility archive) | Copied unchanged from the frozen, verified COAP bundle (`paper_coap/submission/final_upload/Vahidi_Online_Resource_1_MWFAS.zip`) |
| `MANIFEST.sha256` | SHA-256 checksums for the four files above | Generated in this pass |

Verify SHA-256 against `MANIFEST.sha256` before any upload.

## Deliberately not included in this pass

- **SNCS cover letter** — not yet drafted. A COAP cover letter exists at `paper_coap/submission/cover_letter.tex` but is COAP-specific and must not be reused verbatim. See `docs/sncs_preparation_202606/OVERLAP_AND_DISCLOSURE_AUDIT.md` §6b for the recommended disclosure paragraph to include once drafted.
- **SNCS related-manuscripts statement** — not yet drafted, for the same reason; see the same audit document §6a/§6b for the required wording once the author has resolved the two open items in §6c (COAP real-world submission status; the unverified Journal of Supercomputing manuscript).

## Blocking items before this bundle can be uploaded for real

1. Author must confirm whether the COAP version has actually been submitted via Editorial Manager, and ensure only one of COAP/SNCS is under active consideration at a time (see overlap audit §5–6).
2. Author must supply or rule out the Journal of Supercomputing manuscript referenced in the task that requested this pass; it could not be located anywhere in this repository (see overlap audit §2).
3. SNCS cover letter and related-manuscripts statement must be drafted using the wording in the overlap audit.
4. A human author must review the full manuscript (not just the sections touched in this pass) for SNCS fit before upload.

This bundle exists to validate that the manuscript, source, and Online Resource 1 build and package correctly — not to certify submission readiness.
