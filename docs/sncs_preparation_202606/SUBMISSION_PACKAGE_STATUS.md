# SNCS Submission Package Status — Pass 1

**Date:** 2026-06-17 (updated 2026-06-17 following an author correction of COAP's submission status; updated again 2026-06-17 following the author's confirmation that the Journal of Supercomputing manuscript is not a substantial overlap concern)
**Branch:** `sncs-retargeting`

**Active target: SN Computer Science. Historical target: Computational Optimization and Applications. COAP status: declined / closed.** **Author decision recorded:** COAP is closed after rejection. SN Computer Science is the active target for the revised IPSNS sparse-digraph manuscript.

**Author confirmation recorded:** the Journal of Supercomputing manuscript concerning learning-free ranking from pairwise comparisons via feedback-arc-set pruning and add-back is related but distinct and is not a substantial overlap concern for the present SN Computer Science manuscript. The local workspace did not contain the Supercomputing PDF/source, so no text-level comparison was performed; however, the author has confirmed that the SNCS manuscript is a distinct sparse-digraph SCC-local refinement study and that no substantially overlapping manuscript is currently under consideration elsewhere.

## What exists after this pass

`paper_sncs/submission/sncs_initial/`:

| File | Status |
|---|---|
| `Vahidi_SNCS_Manuscript.pdf` | Built in this pass from `paper_sncs/main.tex` (25 pages) |
| `Vahidi_SNCS_Source.zip` | Built in this pass — zip of `paper_sncs/` excluding `main.pdf`, the `sncs_initial/` output directory itself, and LaTeX build artifacts (59 files) |
| `Vahidi_SNCS_Online_Resource_1.pdf` | Copied unchanged from the frozen, hash-verified COAP bundle (`paper_coap/submission/final_upload/Vahidi_Online_Resource_1_MWFAS.pdf`) — content is venue-agnostic |
| `Vahidi_SNCS_Online_Resource_1.zip` | Copied unchanged from the same frozen COAP bundle |
| `MANIFEST.sha256` | Generated in this pass |
| `README_SNCS_UPLOAD.md` | Written in this pass; documents bundle contents and the recommended initial-upload plan |

## What was deferred in this pass (and why)

| Item | Why deferred |
|---|---|
| SNCS-specific cover letter | The COAP cover letter (`paper_coap/submission/cover_letter.tex`) is COAP-specific and cannot be reused verbatim. A recommended disclosure paragraph is drafted in `OVERLAP_AND_DISCLOSURE_AUDIT.md` §6b, but the letter itself was not written in this pass. |
| SNCS-specific related-manuscripts statement | Same reasoning; recommended wording is in `OVERLAP_AND_DISCLOSURE_AUDIT.md` §6a/§6b. |
| Full-manuscript SNCS rewrite (problem definition through conclusion) | Out of scope for this pass per the task instructions, which scoped this pass to title/abstract/keywords/introduction/declarations/packaging. These sections remain byte-identical to `paper_coap/`. |
| Removal of the stale root-level `Vahidi_Online_Resource_1_MWFAS.pdf`/`.zip` duplicate | Out of scope for this pass; flagged in `docs/MANUSCRIPT_AND_ARTIFACT_STATUS.md` for a future cleanup pass, not acted on here to avoid unrequested repository changes. |

## Blocking items before any actual SNCS portal upload

These are carried over verbatim from `OVERLAP_AND_DISCLOSURE_AUDIT.md` §6c — repeated here because they gate this specific package, not just the audit document:

1. ~~Author must confirm COAP's real submission status~~ — **Resolved.** Author decision recorded: COAP was formally submitted and declined on journal-audience/fit grounds; the COAP submission is closed and not under consideration anywhere. SN Computer Science is the active target.
2. ~~Author must supply the Journal of Supercomputing manuscript~~ — **Resolved by author confirmation.** The author has confirmed the Supercomputing manuscript is related but distinct and not a substantial overlap concern; no text-level comparison was possible since the file remains unavailable, but this is no longer treated as a submission blocker.
3. SNCS cover letter and related-manuscripts statement must be drafted (using the wording already prepared in the overlap audit).
4. A human author review of the full manuscript for SNCS fit, beyond the sections touched in this pass.
5. **Pass 2 (not yet done):** add modern FAS/MWFAS references and related-work/baseline-selection paragraphs before actual SNCS submission.

## Editorial Manager initial-upload plan

For the initial SN Computer Science submission, upload `Vahidi_SNCS_Manuscript.pdf` as the main Manuscript file. The portal indicates that a single manuscript file is required as the minimum for first submissions and that authors may submit only a PDF at this stage.

Do not upload `Vahidi_SNCS_Source.zip` as the main manuscript unless the portal requires LaTeX source files. Keep the source ZIP as backup for human review and later production.

If full LaTeX source upload becomes necessary, prepare a separate flattened source package with all `.tex`, `.bib`, `.bst`, `.cls`, `.sty`, and figure files at the same folder level, with no subfolders. The main manuscript TeX file must be the first item and declared as Manuscript. TeX support/style files should be declared as LaTeX Supporting File(s), and figures should be uploaded as figure files. Do not use custom fonts, `.ps`, or `.dvi` files. Since this project uses pdfLaTeX/Springer Nature `sn-jnl`, do not add a XeLaTeX directive unless the manuscript is actually converted to XeLaTeX.

Recommended initial upload: PDF only.

Backup source package: available but not recommended for initial upload unless required.

## Verdict for this package

**READY FOR HUMAN REVIEW BEFORE SNCS SUBMISSION.** This bundle exists to prove the manuscript, source, and Online Resource 1 package correctly together — it is a packaging-readiness check, not a submission-readiness certification. This is **not** a certification that the package is ready for final journal upload: item 5 above (Pass 2 modern references/related-work language) is still outstanding.
