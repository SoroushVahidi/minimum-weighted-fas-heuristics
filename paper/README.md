# Elsevier Manuscript Workspace

This directory contains the draft manuscript workspace for the merged MWFAS paper. It is intentionally a scaffold: section headings, placeholders, audit notes, source maps, and consolidated references only.

## Template

The manuscript uses the Elsevier `elsarticle` class:

```latex
\documentclass[preprint,12pt]{elsarticle}
```

The archived DAM/IPSNS predecessor package contains an Elsevier template and local copies of `elsarticle.cls` and `elsarticle-num.bst`. Small local copies are kept in this directory so compile checks do not depend on a system-wide Elsevier install.

The archived JOCO/local-ratio predecessor package uses Springer `svjour3` files and is not the template source for this workspace.

## Files

- `main.tex`: top-level manuscript skeleton.
- `sections/`: section stubs with TODOs tied to EXP1b--EXP5.
- `references.bib`: merged predecessor bibliography requiring verification.
- `notes/latex_template_audit.md`: template and LaTeX source audit.
- `notes/bibliography_extraction_report.md`: extracted BibTeX source map and reference checklist.
- `notes/reusable_material_audit.md`: candidate predecessor sections with reuse warnings.
- `notes/reference_gap_report.md`: missing or weak citation areas to resolve before writing.
- `notes/reuse_risk_report.md`: obsolete-claim and text-reuse risks.

## Compile Check

From this directory:

```bash
latexmk -pdf main.tex
```

If `latexmk` is unavailable, try:

```bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

Generated PDFs, aux files, logs, and caches should remain uncommitted unless specifically needed for diagnosis.
