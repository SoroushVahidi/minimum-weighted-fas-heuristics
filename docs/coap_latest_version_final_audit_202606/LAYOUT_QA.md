# Layout QA — 24-page manuscript (post-audit build)

Build: `paper_coap/main.pdf` after differential corrections.

## Page-level checks

| Area | Result |
|---|---|
| Title page (p.1) | ORCID link, Newark NJ 07102, singular correspondence line |
| Tables 1–2 (pp.8–9) | Fit text block; readable |
| Benchmark characteristics | Fits; no clipping |
| Primary sparse table (Panel A/B) | Readable; updated column header |
| Seed contribution table | Clear 14/83/0 |
| Exact-validation table | Opt-norm column label |
| Repeated-run table | Comparison-level tests |
| LOLIB table | Full width; no clipping |
| Parameter table | Readable |
| Declarations / references | No layout blockers |

## Build metadata

- Pages: **24** (unchanged)
- Minor underfull vbox on title page only (cosmetic)

## Visual method

`pdftoppm` render of pages 1 and 8–12; full PDF text/table grep cross-check.
