# Reference Gap Report

Updated on 2026-06-06 after the CAIE anonymization pass.

## Resolved in `paper/references.bib`

- Local-ratio background via `BYGR98`
- Directed feedback local-ratio paper via `DF03`
- Eades-Lin-Smyth heuristic via `ELS93`
- Exact MFAS method via `BSNA21`
- Web-scale FAS via `SST16`
- graph-benchmarks repository via `graph_benchmarks_repo`
- LOLIB provenance via `lolib_library` and `MRD12`
- python-igraph feedback arc set documentation via `python_igraph_feedback_arc_set`
- DRMacIver repository via `drmaciver_feedback_arc_set`
- Anonymous reproducibility artifact placeholder via `anonymous_artifact_2026`

## Still TODO Before Full Drafting

- Verify whether `Cavallaro, Cutello, Pavone` needs a stable final citation in the paper or should remain outside the manuscript until explicitly discussed.
- Decide whether `LOP_MA-EDM` is mentioned in the final text; if not, it can be removed from the bibliography.
- Decide whether `GNNRank22` belongs in related work; if not, remove it before submission.
- Add Baharev, Simpson-Srinivasan, and similar references to manuscript prose only if those topics actually enter the Related Work or Discussion section.
- Verify the live CAIE Guide for Authors for any journal-specific constraints beyond the generic Elsevier policies summarized in `paper/notes/caie_author_guidelines.md`.

## Manuscript-Specific Citation Risks

- The current manuscript text cites `BYGR98`, `DF03`, and `ELS93`; later sections will need dataset and baseline citations when the experimental-design prose is written.
- The anonymized manuscript must not cite a public repository or DOI that would identify the authors before review. Use `anonymous_artifact_2026` if a supplementary artifact citation becomes necessary.
