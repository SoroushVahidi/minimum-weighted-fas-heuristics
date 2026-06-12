# CAIE revision pass 1

Manuscript-polish pass after external peer-review feedback. No experiments, result values, or algorithm code changes.

| Concern | Planned action | Status |
|---|---|---|
| Meta-commentary removed | Remove audit/writing-pass/venue-fit phrasing from sections | done |
| Defensive repetition reduced | Keep one caveat each for local-ratio prior art, no approximation ratio, dense LOLIB limit | done |
| Float placement fixed | `placeins` + `\FloatBarrier` before declarations/references | done |
| Captions shortened | Move interpretive notes from tables 4–7 into Section 6 body text | done |
| Best observed vs optimal clarified | Abstract + Results distinguish certified optima from benchmark minima | done |
| Exact subset clarified | 57 standard nonnegative instances with n ≤ 20 in DP study; exclusions stated | done |
| Notation/hyphenation checked | `W_C` in Section 3; `WMSF\-style` in Table 2; dense-ordering-native terminology | done |
| Repository-style wording removed | Rewrite Section 5.4 reproducibility prose | done |
| Anonymization preserved | No author identity in anonymized sources/PDF | done |

## Files edited

- `paper/main_anonymized.tex`, `paper/main.tex` (abstract, placeins, FloatBarrier)
- `paper/sections/01_introduction.tex` through `08_conclusion.tex`
- `paper/tables/table_*.tex` (captions and footnotes)
