# Build and Visual Audit

**Build date:** 2026-06-12  
**Command:** `latexmk -pdf main.tex` (Tectonic backend)

## Build result

| Check | Status |
|-------|--------|
| Build success | **Yes** |
| PDF pages | **44** (was 42 pre-EXP10) |
| PDF SHA-256 | `4318e8c80c0f0e10b1f75e9122c955be251681ddb9b473811fb926e7cb254fb6` |
| Undefined references | **None** |
| Undefined citations | **None** |
| EXP10-INTEGRATION placeholders in PDF | **None** |
| Local absolute paths in PDF text | **None** |
| Provisional "being finalized" language | **Removed** |

## Warnings

- Underfull vbox warnings (pre-existing, cosmetic)
- Overfull hbox in `table_exp10_stochastic_robustness` footnote (~37pt) — table legible; minor

## Visual inspection checklist

| Element | Status |
|---------|--------|
| Abstract robustness sentence | Present |
| §5 EXP10 protocol subsection | Present |
| §6 stochastic robustness subsection | Present |
| Table `tab:exp10-stochastic-robustness` | Present |
| Figure `fig:exp10-median-scatter` | Present |
| Discussion limitation item 8 | Updated |
| Conclusion EXP10 sentence | Present |
