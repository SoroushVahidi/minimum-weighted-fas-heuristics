# Structure Cleanup Report

Date: 2026-06-06

## Section and subsection counts

### Before

- Main sections: 8
- Subsections: 19
- Subsubsections: 0

Breakdown before cleanup:

- `01_introduction.tex`: 0 subsections
- `02_related_work.tex`: 5 subsections
- `03_problem_definition.tex`: 0 subsections
- `04_algorithmic_framework.tex`: 4 subsections
- `05_experimental_design.tex`: 5 subsections
- `06_results.tex`: 5 subsections
- `07_discussion.tex`: 0 subsections
- `08_conclusion.tex`: 0 subsections

### After

- Main sections: 8
- Subsections: 15
- Subsubsections: 0

Breakdown after cleanup:

- `01_introduction.tex`: 0 subsections
- `02_related_work.tex`: 4 subsections
- `03_problem_definition.tex`: 0 subsections
- `04_algorithmic_framework.tex`: 4 subsections
- `05_experimental_design.tex`: 4 subsections
- `06_results.tex`: 3 subsections
- `07_discussion.tex`: 0 subsections
- `08_conclusion.tex`: 0 subsections

## Headings merged or renamed

- Renamed `Algorithmic framework` to `Proposed methodology`.
- Renamed `Discussion and limitations` to `Discussion`.
- Renamed `Conclusion` to `Conclusions`.
- Merged the former `Position of this work` subsection into `Linear ordering benchmarks and manuscript position`.
- Removed the standalone `Research questions` subsection and folded the framing into the opening paragraphs of Experimental Design.
- Removed the standalone `Overall interpretation` subsection and folded the close-out interpretation into the ending paragraphs of Computational Results.

## Overclaiming and repository-language fixes

- Replaced unfinished TODO placeholders in Discussion and Conclusions with manuscript prose.
- Reduced repeated repository-style phrasing in Experimental Design:
  - changed `repository`-framed descriptions to `saved summaries`, `recorded outputs`, or direct benchmark descriptions where appropriate;
  - reduced repeated in-running-prose references to `EXP1b`--`EXP5`;
  - replaced explicit script/path emphasis with lighter manuscript-style wording.
- Preserved the core claim boundaries:
  - local-ratio is prior art;
  - LR-TA is an engineered reproducible instantiation;
  - IPSNS is the main refinement framework;
  - no new approximation guarantee;
  - sparse nonnegative graph benchmarks are the main success case;
  - dense LOLIB is a scope boundary where DRMaciver is stronger.

## Remaining layout warnings

Current anonymized compile succeeds, but LaTeX still reports some non-fatal warnings:

- pre-existing `algorithm.sty` UTF-8 warning;
- older overfull boxes in Introduction, Related Work, Problem Definition, and the framework overview figure;
- modest overfull/underfull warnings in `table_experiment_overview.tex`;
- a few paragraph-level overfull boxes in Experimental Design and Computational Results;
- pre-existing funding statement and bibliography box warnings.

These are layout-quality issues, not compilation blockers.

## Remaining manuscript TODOs

- Discussion and Conclusions are now drafted.
- No manuscript TODO comments remain from this cleanup pass.
- If desired, a later pass can further trim paragraph width and table captions to reduce minor LaTeX box warnings.

## Assessment

The manuscript now reads closer to a standard CAIE computational optimization article:

- fewer framing subsections;
- more coherent paragraphs;
- conventional section titles;
- stronger Discussion and Conclusions;
- less repository-report phrasing in the manuscript body;
- clearer scope boundaries without universal-performance language.
