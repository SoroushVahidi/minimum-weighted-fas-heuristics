# COAP Pass 2 Build Warning Audit

**Date:** 2026-06-10  
**Build command:** `tectonic --keep-logs main.tex` from `paper_coap/`  
**Result:** success; `main.pdf` generated

## Summary

| Category | Count | Action |
|---|---:|---|
| Fatal errors | 0 | none |
| Undefined citations / references | 0 | none |
| Missing files | 0 | none |
| Duplicate labels | 0 | none |
| **Overfull hboxes** | **0** | LOLIB table overflow resolved |
| Underfull hboxes / vboxes | 52 | documented; no visible defects requiring fix |
| Package UTF-8 note (`algorithm.sty`) | 1 | harmless engine substitution |
| Bibliography warnings | 0 | none |

## Overfull boxes (fixed in this pass)

| Source | Page context | Width | Visible? | Fix |
|---|---|---:|---|---|
| `tables/table_lolib_scope.tex` | Table 10 (LOLIB scope) | ~34 pt (pass 1) | yes, margin intrusion risk | Replaced wide `tabular` with `tabularx`, reduced `\tabcolsep`, split family-breakdown headers using `\shortstack` |

**Post-fix status:** zero overfull warnings in `main.log`.

## Underfull boxes (harmless, retained)

Representative sources:

- Float/page break spacing in long sections (`sections/05_experimental_design`, `sections/06_results`, `sections/07_discussion`)
- Table footnote paragraphs (`table_experiment_overview`, `table_exact_validation`, `table_application_case`)
- Bibliography line breaking in long URLs/DOIs (`main.bbl`)

These produce no visible clipping, margin intrusion, or unreadable layout in PDF text/visual review.

## Other engine notes

- `algorithm.sty`: invalid UTF-8 byte replaced by U+FFFD (package encoding quirk; no visible algorithm corruption)
- No PDF-string hyperref warnings observed
- No figure bounding-box warnings observed

## Blocking issues remaining

None.
