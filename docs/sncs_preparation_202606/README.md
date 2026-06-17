# SN Computer Science Retargeting — Pass 1 Documentation

This directory documents the first preparation pass for retargeting the manuscript from *Computational Optimization and Applications* (COAP) to *SN Computer Science* (SNCS), performed on branch `sncs-retargeting` on 2026-06-17. **This is a preparation pass, not a submission.** Nothing in `paper_sncs/` has been submitted to SN Computer Science. (COAP, by contrast, *was* formally submitted and was declined — see below.)

**Active target: SN Computer Science. Historical target: Computational Optimization and Applications. COAP status: declined / closed.**

| Document | Contents |
|---|---|
| [`SNCS_GUIDELINE_CHECK.md`](SNCS_GUIDELINE_CHECK.md) | Researched SN Computer Science submission requirements (article type, structured abstract, keywords, declarations, AI disclosure, LaTeX template) and the decisions made for this manuscript based on them |
| [`OVERLAP_AND_DISCLOSURE_AUDIT.md`](OVERLAP_AND_DISCLOSURE_AUDIT.md) | **Read this before any submission action.** Audits related manuscripts in the repository, the Journal of Supercomputing manuscript named in the task (confirmed by the author to be related but distinct, not a substantial overlap concern), the COAP↔SNCS relationship, and proposes replacement disclosure wording |
| [`CHANGELOG_SNCS_PASS1.md`](CHANGELOG_SNCS_PASS1.md) | File-by-file diff summary of every edit made in this pass |
| [`BUILD_AND_VALIDATION.md`](BUILD_AND_VALIDATION.md) | Manuscript build results, test suite results, artifact validation results |
| [`SUBMISSION_PACKAGE_STATUS.md`](SUBMISSION_PACKAGE_STATUS.md) | What's in `paper_sncs/submission/sncs_initial/`, what's deferred, and the remaining task (Pass 2) before real submission |

## Editorial Manager initial-upload plan

For the initial SN Computer Science submission, upload `Vahidi_SNCS_Manuscript.pdf` as the main Manuscript file. The portal indicates that a single manuscript file is required as the minimum for first submissions and that authors may submit only a PDF at this stage.

Do not upload `Vahidi_SNCS_Source.zip` as the main manuscript unless the portal requires LaTeX source files. Keep the source ZIP as backup for human review and later production.

If full LaTeX source upload becomes necessary, prepare a separate flattened source package with all `.tex`, `.bib`, `.bst`, `.cls`, `.sty`, and figure files at the same folder level, with no subfolders. The main manuscript TeX file must be the first item and declared as Manuscript. TeX support/style files should be declared as LaTeX Supporting File(s), and figures should be uploaded as figure files. Do not use custom fonts, `.ps`, or `.dvi` files. Since this project uses pdfLaTeX/Springer Nature `sn-jnl`, do not add a XeLaTeX directive unless the manuscript is actually converted to XeLaTeX.

Recommended initial upload: PDF only.

Backup source package: available but not recommended for initial upload unless required.

## tl;dr

- `paper_sncs/` was created from `paper_coap/` and modified: title, structured abstract, keywords, introduction framing, related-work framing, declarations (added Ethics/Consent sections, updated related-manuscripts and data-availability wording).
- `paper_coap/` is untouched and is retained as a historical, declined-submission snapshot.
- The manuscript builds (25 pages) and all test suites pass at documented baselines.
- **Author decision recorded:** COAP is closed after rejection. SN Computer Science is the active target.
- **Author confirmation recorded:** the Journal of Supercomputing manuscript concerning learning-free ranking from pairwise comparisons via feedback-arc-set pruning and add-back is related but distinct and is not a substantial overlap concern. No text-level comparison was possible (the file remains unavailable locally), but this is no longer a submission blocker.
- **Verdict: READY FOR HUMAN REVIEW BEFORE SNCS SUBMISSION** — not a certification of readiness for final journal upload. Pass 2 (modern FAS/MWFAS references and related-work/baseline-selection language) is still outstanding.
