# Compile Check

Checked with `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` from `paper/` inside tmux.

- Status: success
- Exit code: 0
- Generated PDF: `main.pdf`, 50.0 KiB, removed after the check
- Warnings:
  - `algorithm.sty` emitted an invalid UTF-8 byte warning from the downloaded TeX package.
  - `sections/05_experimental_design.tex` has one overfull line in placeholder text.
  - BibTeX emitted warnings because the scaffold currently has no citations.

No generated PDF, auxiliary TeX files, or raw build logs are intended for commit.
