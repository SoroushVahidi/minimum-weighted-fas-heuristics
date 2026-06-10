# COAP Pass 1 Migration Notes

**Date:** 2026-06-10  
**Source manuscript:** `paper/main.tex` (EJCO/Elsevier `elsarticle` version)  
**Target manuscript:** `paper_coap/main.tex` (`sn-jnl`)

## Content preserved without substantive change

- All eight section files (`sections/01`–`08`)
- All algorithms and pseudocode in `sections/04_algorithmic_framework.tex`
- TikZ Figure 1 (`figures/framework_overview.tex`)
- PDF result figures (`exp4_*`, `exp6_*`, `exp5_*`)
- Mathematical definitions, propositions, experimental counts, statistical statements, captions (except template-driven caption formatting)
- Bibliography entries (minus journal-specific anonymous artifact placeholder)

## Mechanical / template changes only

| Change | Reason |
|---|---|
| New `sn-jnl` preamble and author block | Springer COAP template migration |
| `\keywords{...}` comma-separated list | Springer template syntax |
| Numbered bibliography via `sn-mathphys-num` | COAP reference style requirement |
| Combined `Statements and Declarations` section | COAP policy placement |
| Removed uncited `anonymous_artifact_2026` bib entry | Author-visible COAP version; entry was anonymized-review-only |
| Online Resource 1 placeholder in data availability | COAP SI naming; final `ESM_1.zip` deferred |
| ORCID rendered as text hyperlink | Official template asset `Orcidlogo.eps` unavailable in mirror |
| Table formatting adjustments (see below) | `sn-jnl`/Tectonic compatibility |

## Table formatting adjustments (values unchanged)

1. **`tables/table_experiment_overview.tex`** — replaced `\resizebox` + `p{...}` columns with `tabularx` to avoid TeX grouping error.
2. **`tables/table_sparse_external_baselines.tex`** — removed `\resizebox`; used `\scriptsize` tabular; moved note out of `\parbox`.
3. **`tables/table_lolib_scope.tex`** — same as above; one overfull hbox warning remains (~34 pt) on family-breakdown row.
4. **`tables/table_ipsns_budget_curve.tex`** — removed `\resizebox`; replaced `\par\vspace` with `\vspace`.
5. **`tables/table_plain_local_search.tex`** — same as budget-curve table.

## Pass 2 polish (2026-06-10)

Mechanical fixes only:

| File | Change |
|---|---|
| Official template files | Replaced `sn-jnl.cls` and all `.bst` files with official December 2024 ZIP |
| `bibliography/references.bib` | Added verified `address` fields for `BH13`, `ALS09`, `LHK10WikiVote` |
| `tables/table_lolib_scope.tex` | Fixed margin overflow via `tabularx` + `\shortstack` headers |
| `main.tex` | Improved ORCID superscript link presentation |

**Scientific content unchanged:** `sections/` remains byte-identical to `paper/sections/`; Figure 1 TikZ unchanged; abstract/keywords/algorithms/results text unchanged.

## Supplementary material status

- Manuscript cites **Online Resource 1** as future supplementary material.
- Final Springer-compliant **`ESM_1.zip` not built**.
- See `supplementary/README.md`.
