# Layout QA

Visual inspection performed on rendered `paper_coap/main.pdf` (24 pages).

## Passed

- Title page: ORCID link visible; no collision with affiliation marker; correspondence line readable.
- Tables 1 and 2: fit within text block; no clipped right columns; no word-by-word fragmentation.
- Primary sparse table (two-panel): readable at normal zoom.
- Exact-validation and repeated-run tables: headers and notes fit.
- Table 6 (dense LOLIB): uses available width; method column readable.
- No unresolved references or undefined citations in build log.
- Data/code URLs render as hyperlinks.

## Notes

- Manuscript grew from 23 to **24 pages** after added parameter, benchmark-characteristics, and seed-contribution material.
- Minor underfull vbox warning on title page (cosmetic only).
- Page preceding dense LOLIB table: blank space reduced versus prior build; no forced half-page gap observed.

## Build command

```bash
cd paper_coap && latexmk -pdf -interaction=nonstopmode main.tex
```
