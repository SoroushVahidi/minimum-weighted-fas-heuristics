# SNCS Submission Package Status — Pass 1

**Date:** 2026-06-17
**Branch:** `sncs-retargeting`

## What exists after this pass

`paper_sncs/submission/sncs_initial/`:

| File | Status |
|---|---|
| `Vahidi_SNCS_Manuscript.pdf` | Built in this pass from `paper_sncs/main.tex` (25 pages) |
| `Vahidi_SNCS_Source.zip` | Built in this pass — zip of `paper_sncs/` excluding `main.pdf`, the `sncs_initial/` output directory itself, and LaTeX build artifacts (65 files) |
| `Vahidi_SNCS_Online_Resource_1.pdf` | Copied unchanged from the frozen, hash-verified COAP bundle (`paper_coap/submission/final_upload/Vahidi_Online_Resource_1_MWFAS.pdf`) — content is venue-agnostic |
| `Vahidi_SNCS_Online_Resource_1.zip` | Copied unchanged from the same frozen COAP bundle |
| `MANIFEST.sha256` | Generated in this pass |
| `README_SNCS_UPLOAD.md` | Written in this pass; documents bundle contents and blocking items |

## What was deferred in this pass (and why)

| Item | Why deferred |
|---|---|
| SNCS-specific cover letter | The COAP cover letter (`paper_coap/submission/cover_letter.tex`) is COAP-specific and cannot be reused verbatim. A recommended disclosure paragraph is drafted in `OVERLAP_AND_DISCLOSURE_AUDIT.md` §6b, but the letter itself was not written because it depends on the author resolving the two blocking items below first. |
| SNCS-specific related-manuscripts statement | Same reasoning; recommended wording is in `OVERLAP_AND_DISCLOSURE_AUDIT.md` §6a/§6b. |
| Full-manuscript SNCS rewrite (problem definition through conclusion) | Out of scope for this pass per the task instructions, which scoped this pass to title/abstract/keywords/introduction/declarations/packaging. These sections remain byte-identical to `paper_coap/`. |
| Removal of the stale root-level `Vahidi_Online_Resource_1_MWFAS.pdf`/`.zip` duplicate | Out of scope for this pass; flagged in `docs/MANUSCRIPT_AND_ARTIFACT_STATUS.md` for a future cleanup pass, not acted on here to avoid unrequested repository changes. |

## Blocking items before any actual SNCS portal upload

These are carried over verbatim from `OVERLAP_AND_DISCLOSURE_AUDIT.md` §6c — repeated here because they gate this specific package, not just the audit document:

1. **Author must confirm COAP's real submission status** (submitted / not submitted / withdrawn) and ensure only one of COAP or SNCS is under active consideration at any time. Repository evidence (a blank sign-off block in `paper_coap/submission/AUTHOR_PRE_SUBMISSION_CONFIRMATION.md`, and a "Pending"/"Not yet submitted" status in `docs/archive/internal/coap_rejection_history_and_revision_plan_20260611/PRIOR_DECISION_AND_REVIEW_REGISTER.csv`) indicates COAP has very likely not yet been formally submitted, but the repository contains no explicit record of a decision between the two targets.
2. **Author must supply or rule out the Journal of Supercomputing manuscript** named in the task that requested this pass (manuscript ID `OPSE-D-26-00226`, a specific UUID). An exhaustive repository search found no trace of it anywhere — no source file, no PDF, no mention in any audit or status document. This cannot be resolved from repository evidence alone.
3. SNCS cover letter and related-manuscripts statement must be drafted (using the wording already prepared in the overlap audit) once items 1–2 are resolved.
4. A human author review of the full manuscript for SNCS fit, beyond the sections touched in this pass.

## Verdict for this package

**Builds and validates correctly; not cleared for portal upload.** This bundle exists to prove the manuscript, source, and Online Resource 1 package correctly together — it is a packaging-readiness check, not a submission-readiness certification.
