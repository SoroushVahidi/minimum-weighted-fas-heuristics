# Second Reference Pass Report

Controlled comparison of Perplexity suggestions against the post-strengthening bibliography (23 cited keys).

## Summary

| Metric | Before pass | After pass |
|---|---:|---:|
| Unique cited keys | 23 | 25 |
| Bib entries | 23 | 25 |
| References added | — | 2 |
| Citation phrasing fixes | — | redundant author+cite patterns removed |

## Perplexity suggestion evaluation

| Suggested reference | In bib before? | Cited before? | Verified? | Decision | Reason |
|---|---|---|---|---|---|
| Lempel & Cederbaum 1966 | no | no | yes (IEEE TCT DOI) | **add** | Foundational FAS formulation; supports classical-problem sentence |
| Flood 1990 | yes | yes | yes | keep | Already cited |
| Demetrescu & Finocchi 2003 | yes | yes | yes | keep | Already cited |
| Bar-Yehuda et al. 1998 | yes | yes | yes | keep | Already cited |
| Bar-Yehuda & Even 1985 | no | no | yes (literature) | **do not add** | BYGR98 already covers local-ratio positioning sufficiently |
| Eades, Lin, Smyth 1993 | yes | yes | yes | keep | Already cited |
| Eades & Lin 1995 | no | no | yes (AJC vol. 12) | **add** | Verified heuristic-family antecedent beyond ELS93 |
| Baharev et al. 2021 | yes | yes | yes | keep | Already cited |
| Simpson et al. 2016 | yes | yes | yes | keep | Already cited |
| Cavallaro, Cutello, Pavone 2024/2025 | partial | yes (`CC25`) | yes for CC25 | keep | CC25 already present; Pavone not verified on local entry |
| Martí/Reinelt/Duarte LOLIB | yes | yes | yes | keep | Already cited via `MRD12`, `lolib_library` |
| GNNRank | yes | yes | yes | keep | Already cited |
| Karp 1972 | yes | yes | yes | keep | Already cited |
| Vahidi–Koutis preprint | no | no | n/a | **reject** | Author-identifying; must not appear in anonymized manuscript |
| Wikipedia | no | no | n/a | **reject** | Not acceptable source |
| Younger 1963 | no | no | yes | **do not add** | Would inflate count without a specific uncovered sentence |

## References added

1. **`LC66`** — Lempel & Cederbaum (1966), IEEE Transactions on Circuit Theory, DOI `10.1109/TCT.1966.1082620`
2. **`EL95`** — Eades & Lin (1995), Australasian Journal of Combinatorics, vol. 12, pp. 15–25

## Citation phrasing fixes

Removed redundant textual author names before `\cite{...}` where author-year rendering would duplicate names (e.g., Demetrescu and Finocchi \cite{DF03} → \cite{DF03}).

## Author-identifying exclusions confirmed

No Vahidi, Koutis, NJIT, sv96, or author arXiv entries were added.

## Integration locations

- `LC66`: Related work, classical FAS foundations paragraph
- `EL95`: Related work, heuristic baselines paragraph
- Phrasing cleanup: Introduction, Related work, Algorithmic framework
