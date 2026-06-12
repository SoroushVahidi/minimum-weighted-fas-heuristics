# Supplement Update Log

## Structural changes

- Added **S12 (EXP11)**; renumbered tests → S13, reproduction → S14, limitations → S15.
- **S2:** Numbered equations; proofs of \(B_\pi \subseteq F\) and \(w(B_\pi) \le w(F)\); equality conditions.
- **S6:** Topological extraction + EXP11 protocol and results.
- **S11:** EXP10 final evidence (1860/1860, 38/55/0, 21.60%).
- **S13:** Test counts aligned to full repo (90/1) vs OR1 package (79/7).

## Artifact sync (`finalize_or1.py`)

- Syncs `src/mwfas/`, `tests/` (minus infrastructure test), EXP10 summaries, EXP11 results.
- Excludes live EXP10 production tree and internal preflight notes.
- Regenerates `MANIFEST.sha256` and `provenance/source_commit.txt`.
