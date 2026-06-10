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

## Not changed in this pass

- EJCO package under `submission_package/ejco_*`
- Elsevier `paper/` tree
- CAIE historical packages
- Reproducibility artifact zips
- Cover letter, reviewer list, upload directory, ESM zip

## Supplementary material status

- Manuscript cites **Online Resource 1** as future supplementary material.
- Final Springer-compliant **`ESM_1.zip` not built**.
- See `supplementary/README.md`.
