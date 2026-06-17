# SN Computer Science Retargeting — Pass 1 Documentation

This directory documents the first preparation pass for retargeting the manuscript from *Computational Optimization and Applications* (COAP) to *SN Computer Science* (SNCS), performed on branch `sncs-retargeting` on 2026-06-17. **This is a preparation pass, not a submission.** Nothing in `paper_sncs/` has been submitted to SN Computer Science. (COAP, by contrast, *was* formally submitted and was declined — see below.)

**Active target: SN Computer Science. Historical target: Computational Optimization and Applications. COAP status: declined / closed.**

| Document | Contents |
|---|---|
| [`SNCS_GUIDELINE_CHECK.md`](SNCS_GUIDELINE_CHECK.md) | Researched SN Computer Science submission requirements (article type, structured abstract, keywords, declarations, AI disclosure, LaTeX template) and the decisions made for this manuscript based on them |
| [`OVERLAP_AND_DISCLOSURE_AUDIT.md`](OVERLAP_AND_DISCLOSURE_AUDIT.md) | **Read this before any submission action.** Audits related manuscripts in the repository, the Journal of Supercomputing manuscript named in the task (confirmed to exist per author email records, but not locally available), the COAP↔SNCS relationship, and proposes replacement disclosure wording |
| [`CHANGELOG_SNCS_PASS1.md`](CHANGELOG_SNCS_PASS1.md) | File-by-file diff summary of every edit made in this pass |
| [`BUILD_AND_VALIDATION.md`](BUILD_AND_VALIDATION.md) | Manuscript build results, test suite results, artifact validation results |
| [`SUBMISSION_PACKAGE_STATUS.md`](SUBMISSION_PACKAGE_STATUS.md) | What's in `paper_sncs/submission/sncs_initial/`, what's deferred, and the blocking item before real submission |

## tl;dr

- `paper_sncs/` was created from `paper_coap/` and modified: title, structured abstract, keywords, introduction framing, related-work framing, declarations (added Ethics/Consent sections, updated related-manuscripts and data-availability wording).
- `paper_coap/` is untouched and is retained as a historical, declined-submission snapshot.
- The manuscript builds (25 pages) and all test suites pass at documented baselines.
- **Author decision recorded:** COAP is closed after rejection. SN Computer Science is the active target.
- **One item blocks actual SNCS submission:** the author must supply the Journal of Supercomputing manuscript referenced in the originating task. Its existence is confirmed via the author's email records, but an exhaustive search of this repository and the entire local workspace found no trace of the file itself.
