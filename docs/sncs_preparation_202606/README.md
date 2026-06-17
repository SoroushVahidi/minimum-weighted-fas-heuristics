# SN Computer Science Retargeting — Pass 1 Documentation

This directory documents the first preparation pass for retargeting the manuscript from *Computational Optimization and Applications* (COAP) to *SN Computer Science* (SNCS), performed on branch `sncs-retargeting` on 2026-06-17. **This is a preparation pass, not a submission.** Nothing in this directory or `paper_sncs/` has been submitted to any journal.

| Document | Contents |
|---|---|
| [`SNCS_GUIDELINE_CHECK.md`](SNCS_GUIDELINE_CHECK.md) | Researched SN Computer Science submission requirements (article type, structured abstract, keywords, declarations, AI disclosure, LaTeX template) and the decisions made for this manuscript based on them |
| [`OVERLAP_AND_DISCLOSURE_AUDIT.md`](OVERLAP_AND_DISCLOSURE_AUDIT.md) | **Read this before any submission action.** Audits related manuscripts in the repository, the (unverified) Journal of Supercomputing manuscript named in the task, the COAP↔SNCS overlap, and proposes replacement disclosure wording |
| [`CHANGELOG_SNCS_PASS1.md`](CHANGELOG_SNCS_PASS1.md) | File-by-file diff summary of every edit made in this pass |
| [`BUILD_AND_VALIDATION.md`](BUILD_AND_VALIDATION.md) | Manuscript build results, test suite results, artifact validation results |
| [`SUBMISSION_PACKAGE_STATUS.md`](SUBMISSION_PACKAGE_STATUS.md) | What's in `paper_sncs/submission/sncs_initial/`, what's deferred, and the blocking items before real submission |

## tl;dr

- `paper_sncs/` was created from `paper_coap/` and modified: title, structured abstract, keywords, introduction framing, related-work framing, declarations (added Ethics/Consent sections, updated related-manuscripts and data-availability wording).
- `paper_coap/` is untouched.
- The manuscript builds (25 pages) and all test suites pass at documented baselines.
- **Two items block actual SNCS submission:** (1) the author must confirm/record whether COAP has been formally submitted, so only one target is active at a time; (2) the author must supply or rule out the Journal of Supercomputing manuscript referenced in the originating task — it was not found anywhere in this repository.
