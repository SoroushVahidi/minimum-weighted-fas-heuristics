# Build and Visual Audit

## Main manuscript

| Property | Value |
|---|---|
| Command | `latexmk -pdf -interaction=nonstopmode main.tex` (in `paper_coap/`) |
| Success | yes |
| Pages | 45 |
| SHA-256 | `33bffde0a8a054bfe3a50c0f90baf13d71d292f0ec6b57b26c00bde21d1669c2` |
| Undefined references | none blocking (log review) |
| Missing graphics | none |

## Online Resource 1 supplement

| Property | Value |
|---|---|
| Command | `latexmk -pdf -interaction=nonstopmode online_resource_1.tex` |
| Success | yes |
| Pages | 12 |
| SHA-256 | `8cc1479fb7aebe9e8b4c219aada0bf87f6c0383f53345a2d851b776b581aa0ea` |
| Warnings | minor overfull hbox in S15 limitations |
| Numbered equations | yes in S2 and formal sections |

## Visual spot-check

- Supplement front page, TOC, S2 proofs, S7 parameters, S11 EXP10, S12 EXP11, S13 tests, S14 reproduction: present and readable.

## Status

**Both PDFs build cleanly.**
