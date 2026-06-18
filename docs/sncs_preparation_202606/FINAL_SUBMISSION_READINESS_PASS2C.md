# SNCS Final Submission Readiness — Pass 2C

**Date:** 2026-06-17  
**Branch:** `sncs-retargeting`  
**Starting commit for this pass:** `0f047ba`

## 1. Current manuscript status

Pass 2A diagnosis and Pass 2B corrective edits are complete. This Pass 2C review re-checked the edited manuscript, rebuilt the PDF, verified citation usage, validated the submission manifest, and applied only two minor consistency fixes:

- `paper_sncs/sections/05_experimental_design.tex`: changed “four roles” to “five roles”
- `paper_sncs/sections/07_discussion.tex`: changed “Four limitations” to “Five limitations”

No experiments were rerun. No numerical results were changed. No new baselines were implemented.

The manuscript now reads as a sparse-digraph algorithm-engineering paper with explicit scope limits, a clearer contribution statement, broader and more current related work, and a documented PDF-first submission plan.

## 2. Final title, abstract word count, and keywords

- **Title:** `An Incumbent-Protected Component-Local Heuristic for Minimum Weighted Feedback Arc Set on Sparse Digraphs`  
  Evidence: `paper_sncs/main.tex:50`
- **Structured abstract word count:** **245 words**  
  Count source: extracted from `paper_sncs/main.tex` abstract block after removing LaTeX markup
- **Keywords:** `Feedback arc set, Graph algorithms, Combinatorial optimization, Heuristic search, Strongly connected components, Algorithm engineering`  
  Evidence: `paper_sncs/main.tex:67`

## 3. Pass 2A risk-resolution table

| Risk | Pass 2A severity | Pass 2C status | Evidence/location | Remaining action |
|---|---|---|---|---|
| Acronym/readability | P0 | Resolved | `paper_sncs/main.tex:57-64`; `paper_sncs/sections/01_introduction.tex:6-14`; first-page PDF text from `paper_sncs/main.pdf` | Human read for prose polish only |
| Novelty/significance | P0 | Mostly resolved | `paper_sncs/sections/01_introduction.tex:10-24`; `paper_sncs/sections/07_discussion.tex:6-19`; `paper_sncs/sections/08_conclusion.tex:4-8` | Final human read should check whether the “incremental over strong seeds” objection is preempted strongly enough |
| Related work/references | P0 | Resolved | `paper_sncs/sections/02_related_work.tex:8-35`; `paper_sncs/sections/05_experimental_design.tex:27`; `paper_sncs/bibliography/references.bib` | None beyond ordinary human reading |
| External baseline rationale | P1 | Mostly resolved | `paper_sncs/sections/02_related_work.tex:18-20`; `paper_sncs/sections/05_experimental_design.tex:23-27` | Optional future comparator work only; not required for current scoped submission |
| Method/parameter self-containedness | P1 | Resolved | `paper_sncs/sections/04_algorithmic_framework.tex:4,47,59-65,100`; `paper_sncs/sections/05_experimental_design.tex:52-58` | None beyond human readability pass |
| Scope/overclaiming | P1 | Resolved | `paper_sncs/main.tex:62-64`; `paper_sncs/sections/01_introduction.tex:14,24`; `paper_sncs/sections/07_discussion.tex:6,12-19`; `paper_sncs/sections/08_conclusion.tex:6-8` | None |
| Declarations/submission risk | P1 in practice | Resolved | `paper_sncs/declarations/statements_and_declarations.tex:21-30` | None in manuscript; separate cover-letter drafting remains outside manuscript |
| Editorial Manager upload compliance | P1 in practice | Resolved for documentation | `paper_sncs/submission/sncs_initial/README_SNCS_UPLOAD.md:17-27,34-40` | Backup source ZIP is flattened to exactly one `.tex` file; upload it only if the portal requires LaTeX source |

## 4. Remaining risks

The remaining risks are limited and do not block a final human read:

- The scientific claim is still intentionally narrow, so some reviewers may still call the refinement “incremental over strong seeds.” The manuscript now addresses that objection directly, but it remains the most likely substantive review pressure point.
- TIGHT-CUT* remains the most plausible “why not this baseline?” question. The manuscript now explains why it is not included and labels it future work, but a determined reviewer could still ask for it.
- The current source ZIP is a flattened backup package containing exactly one `.tex` file. The procedural risk is now limited to uploading it when PDF-only is sufficient.
- The upload-bundle README still notes that the cover letter and separate related-manuscripts statement are not yet drafted. That is outside the manuscript itself but still part of overall submission preparation.

## 5. References and baseline adequacy

The reference layer is materially stronger than in Pass 2A:

- Bibliography entries present: **34**
- Entries dated 2020–2026: **24** total (including software/data/documentation entries)
- Newly added Pass 2B entries: `GJR22`, `BH11TR`, `CCP23CEUR`, `GLT23`, `Hanauer2017thesis`
- Newly added Pass 2B entries used in text: **all five are used**

Evidence of text usage:

- `GJR22`: `paper_sncs/sections/02_related_work.tex:8`
- `BH11TR`: `paper_sncs/sections/02_related_work.tex:12`
- `CCP23CEUR`: `paper_sncs/sections/01_introduction.tex:12`; `paper_sncs/sections/02_related_work.tex:24`; `paper_sncs/sections/05_experimental_design.tex:27`
- `GLT23`: `paper_sncs/sections/02_related_work.tex:12`; `paper_sncs/sections/05_experimental_design.tex:27`
- `Hanauer2017thesis`: `paper_sncs/sections/02_related_work.tex:12,16`

Baseline adequacy is acceptable for the current scoped claim:

- DRMacIver/FAS is clearly treated as an **external executable comparator**.
- python-igraph Eades is clearly treated as an **external library baseline**.
- DP and HiGHS MIP are clearly treated as **validation / certification tools** on subsets rather than scalable full-benchmark competitors.
- TIGHT-CUT*, minimal-FAS methods, web-scale GreedyFAS/SortFAS-line work, and PageRankFAS are now discussed as related but not directly integrated baselines.

Conclusion for this section: references and baseline discussion are sufficient for a final human reading pass before SNCS upload. An additional external baseline is not required to justify the current manuscript scope.

## 6. Scope and overclaiming check

The scope language is now consistently bounded:

- Abstract uses “Among the evaluated methods” and states the dense-boundary limitation.  
  Evidence: `paper_sncs/main.tex:62-64`
- Introduction explicitly states that the claim is narrow and not universal.  
  Evidence: `paper_sncs/sections/01_introduction.tex:14,24`
- Discussion states the sparse-regime scope, the dense LOLIB boundary, and the non-universal claim.  
  Evidence: `paper_sncs/sections/07_discussion.tex:6,12-19`
- Conclusion presents the results as a “deliberately scoped” empirical result and marks the dense transfer boundary.  
  Evidence: `paper_sncs/sections/08_conclusion.tex:6-8`

Assessment: no problematic universal-superiority language remains.

## 7. Declaration and overlap check

The declaration language is currently low risk:

- COAP disclosure is factual and non-alarming.  
  Evidence: `paper_sncs/declarations/statements_and_declarations.tex:21-22`
- The prior author work / public preprint relationship is explained and localized to attributed components.  
  Evidence: `paper_sncs/declarations/statements_and_declarations.tex:22`
- The manuscript states that **no substantially overlapping manuscript is currently under consideration elsewhere**.  
  Evidence: `paper_sncs/declarations/statements_and_declarations.tex:22`
- The related Supercomputing manuscript is described as related but distinct and non-overlapping.  
  Evidence: `paper_sncs/declarations/statements_and_declarations.tex:22`
- The generative-AI disclosure is explicit, responsible, and leaves responsibility with the author.  
  Evidence: `paper_sncs/declarations/statements_and_declarations.tex:29-30`

Assessment: no unresolved overlap or declaration blocker remains in the manuscript text.

## 8. Editorial Manager upload plan

The documented initial-upload recommendation remains:

- Upload `Vahidi_SNCS_Manuscript.pdf` as the main Manuscript file.
- Recommended initial upload: **PDF only**.
- `Vahidi_SNCS_Source.zip` is a **backup package**, not the recommended initial upload.
- `Vahidi_SNCS_Source.zip` has been flattened so that it contains exactly one `.tex` file plus the required support files. Upload it only if source files are required.

Evidence: `paper_sncs/submission/sncs_initial/README_SNCS_UPLOAD.md:17-27,40`

Assessment: upload guidance is clear and consistent with the earlier documented portal interpretation.

## 9. Build/package validation

- `latexmk -pdf main.tex`: succeeded in Pass 2C
- Undefined citations / references check: none found by grep scan of `paper_sncs/*.log` and `paper_sncs/*.blg`
- `paper_sncs/main.pdf` page count: **27**
- `paper_sncs/main.pdf` SHA-256 after Pass 2C rebuild: `48a10704b6dbb66b3dcf22b3839212c5af28e2c96dae985abf84f356bf2cb4fe`
- `paper_sncs/main.pdf` size: **207K**
- First-page PDF sanity check passed for:
  - title
  - author name
  - ORCID
  - structured abstract readability
  - keywords
  - later inclusion of declarations and references in the full PDF

Submission-bundle status after refresh:

- `Vahidi_SNCS_Manuscript.pdf` copied from rebuilt `paper_sncs/main.pdf`
- `Vahidi_SNCS_Source.zip` rebuilt as a flattened backup source package with exactly one `.tex` file
- `MANIFEST.sha256` regenerated
- `sha256sum -c paper_sncs/submission/sncs_initial/MANIFEST.sha256`: all four files **OK**

Non-fatal build warnings that remain:

- the longstanding `algorithm.sty` UTF-8 warning
- standard underfull/overfull box warnings

These are layout/package warnings, not citation or scientific-content blockers.

## 10. Final verdict

The manuscript is now in a state suitable for a final author reading before actual SN Computer Science upload. The Pass 2A P0/P1 manuscript risks have been addressed to a level appropriate for a scoped submission. Remaining work is primarily human-review and submission-packaging administration, not additional scientific editing or experimentation.

**READY FOR FINAL HUMAN READ BEFORE SNCS UPLOAD**

## Simulated SNCS reviewer objections

| Likely objection | Status | Where the manuscript addresses it |
|---|---|---|
| The contribution is incremental over the seeds. | Mostly resolved | `paper_sncs/sections/01_introduction.tex:10-24`; `paper_sncs/sections/07_discussion.tex:6-8`; `paper_sncs/sections/08_conclusion.tex:6-8` |
| Recent FAS heuristic references are missing. | Resolved | `paper_sncs/sections/02_related_work.tex:8-24`; `paper_sncs/sections/05_experimental_design.tex:27`; new entries in `paper_sncs/bibliography/references.bib` |
| The baseline set is incomplete. | Mostly resolved | `paper_sncs/sections/05_experimental_design.tex:23-27`; `paper_sncs/sections/02_related_work.tex:18-20` |
| The method is too heuristic or parameter-based. | Mostly resolved | `paper_sncs/sections/04_algorithmic_framework.tex:59-65,100`; `paper_sncs/sections/05_experimental_design.tex:52-58` |
| Dense LOLIB weakens the paper. | Resolved | `paper_sncs/sections/01_introduction.tex:6,14`; `paper_sncs/sections/05_experimental_design.tex:19`; `paper_sncs/sections/07_discussion.tex:13-14`; `paper_sncs/sections/08_conclusion.tex:8` |
| The paper overclaims. | Resolved | `paper_sncs/main.tex:62-64`; `paper_sncs/sections/01_introduction.tex:14`; `paper_sncs/sections/07_discussion.tex:6,19`; `paper_sncs/sections/08_conclusion.tex:6` |
| The paper is not self-contained without supplementary material. | Mostly resolved | `paper_sncs/sections/04_algorithmic_framework.tex:47,61-65,100`; `paper_sncs/sections/05_experimental_design.tex:52-58` |
| The declarations imply overlap risk. | Resolved | `paper_sncs/declarations/statements_and_declarations.tex:21-30` |
| TIGHT-CUT* should have been a baseline. | Still a concern | `paper_sncs/sections/05_experimental_design.tex:27`; related-method context at `paper_sncs/sections/02_related_work.tex:10` |
| The paper is too narrow for SNCS. | Mostly resolved | `paper_sncs/sections/01_introduction.tex:6-8,14-24`; `paper_sncs/sections/08_conclusion.tex:4-8` |
| DRMacIver/FAS is not a fair sparse-graph comparator. | Mostly resolved | `paper_sncs/sections/02_related_work.tex:18-20`; `paper_sncs/sections/05_experimental_design.tex:25,39,52` |
| DP/MIP are not real competitors. | Resolved | `paper_sncs/sections/05_experimental_design.tex:17,25,33,39`; `paper_sncs/sections/06_results.tex:20-30` |
