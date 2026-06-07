# DRMacIver/FAS baseline revision

Targeted manuscript pass integrating verified Perplexity characterization. No experiments, result values, or algorithm code changes.

## Verified safe characterization

- DRMacIver/Feedback-Arc-Set is a C library/CLI for computing an ordering from a nonnegative \(n \times n\) weight matrix of pairwise evidence.
- Given matrix \(W\), it seeks a permutation maximizing forward weight \(\sum_{p_i < p_j} W_{ij}\).
- Documented as a **deterministic heuristic**, not an exact optimizer.
- Repository states output is locally optimal with respect to **single-element moves**.
- Documented **\(O(n^2)\)** complexity in the number of items.
- CLI accepts sparse listings of matrix entries; conceptual model is matrix-based pairwise evidence.
- Naturally aligned with dense pairwise-comparison / complete ordering instances; repository does not explicitly require tournaments.

## Unsupported claims avoided

- simulated annealing, branch-and-bound, dynamic programming, Monte Carlo, exact solver, randomized search, tournament-only algorithm, tournament-native (for DRMacIver)

## Manuscript locations edited

| File | Change |
|---|---|
| `paper/sections/02_related_work.tex` | Matrix-based DRMacIver/FAS paragraph in software baselines |
| `paper/sections/05_experimental_design.tex` | Baseline list + short LOLIB relevance note |
| `paper/sections/06_results.tex` | Incompletion wording; matrix-based sparse/dense interpretation |
| `paper/sections/07_discussion.tex` | Dense LOLIB boundary via matrix-based alignment |
| `paper/sections/08_conclusion.tex` | Matrix-based baseline wording |
| `paper/sections/01_introduction.tex` | Dense LOLIB paragraph terminology |

## Final status

| Check | Status |
|---|---|
| Compile | pass (39 pages; underfull hboxes only) |
| Citation sanity | pass (no missing keys; no forbidden terms) |
| Anonymization scan | pass |
| Download folder refresh | pass — SHA256 `e15c0876353dee3a29080effd487fea78290332017951257e07bf5833f2f0985` |
