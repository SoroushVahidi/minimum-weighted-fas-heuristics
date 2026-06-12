# Warning-to-Section Map

Mapping from deduplicated baseline warnings to manuscript structure.

## Introduction (`sections/01_introduction.tex`)

| Lines | Warning | Severity | Notes |
|---|---|---|---|
| 10--11 | Overfull 10.61pt | high | Long IPSNS paragraph; split refinement sentence |

## Related work (`sections/02_related_work.tex`)

| Lines | Warning | Severity | Notes |
|---|---|---|---|
| 16--17 | Overfull 4.28pt | high | python-igraph baseline sentence |
| 26--1 | Overfull 21.18pt | high | Exact-methods subsection closing paragraph |
| 34--35 | Overfull 21.47pt | high | Sparse benchmark provenance paragraph |
| 42--1 | Overfull (via sec. 02 end) | high | Final positioning paragraph |

## Problem definition (`sections/03_problem_definition.tex`)

| Lines | Warning | Severity | Notes |
|---|---|---|---|
| 42--1 | Overfull 22.41pt | high | LOLIB transfer-test closing sentence |

## Proposed methodology

| Source | Warning | Severity | Notes |
|---|---|---|---|
| `figures/framework_overview.tex` 29--30 | Overfull 24.17pt | high | TikZ feedback-arrow label width |

## Experimental design / tables

| Source | Warning | Severity | Notes |
|---|---|---|---|
| `tables/table_algorithm_components.tex` | Underfull (multiple) | medium | Fixed-width `p{}` columns without ragged text |
| `tables/table_algorithm_invariants.tex` | Underfull | medium | Same table formatting issue |
| `tables/table_experiment_overview.tex` 6--17 | Overfull 8.99pt | high | Wide four-column overview table |
| `tables/table_experiment_overview.tex` 8--8 | Overfull 5.29pt | high | Header cell overflow |

## Computational results (`sections/06_results.tex`)

| Lines | Warning | Severity | Notes |
|---|---|---|---|
| 48--49 | Overfull 6.63pt | high | `r20_60` exact-validation interpretation paragraph |

## Conclusions (`sections/08_conclusion.tex`)

| Lines | Warning | Severity | Notes |
|---|---|---|---|
| 8--9 | Overfull 9.25pt / 0.34pt | high / low | Dense LOLIB boundary paragraph |

## Frontmatter (`main_anonymized.tex`)

| Lines | Warning | Severity | Notes |
|---|---|---|---|
| 12--42 | Overfull 15.25pt | high | Abstract/keyword block width |

## Declarations

| Source | Warning | Severity | Notes |
|---|---|---|---|
| `declarations/funding_statement.tex` 2--1 | Overfull 19.42pt | high | Funding sentence line breaking |

## Bibliography (`main_anonymized.bbl`)

| Lines | Warning | Severity | Notes |
|---|---|---|---|
| 16--24, 57--64, 102--110 | Underfull | medium | Long DOI/URL lines; remove duplicate URLs from BibTeX |

## Package-level

| Source | Warning | Severity | Notes |
|---|---|---|---|
| `algorithm.sty:11` | UTF-8 replacement | low | Documented package-level warning; visually harmless |
