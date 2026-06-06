# Repository merge notes

This repository merges code and experiment material from:

1. https://github.com/SoroushVahidi/weighted-minfas-local-ratio
2. https://github.com/SoroushVahidi/weighted-minfas-codes

Both source repositories contained identical notebooks (`feeback-arc-set-codes.ipynb`)
with three algorithm cells: LR-TA, WMSF, and IPSNS.

## What was done

- Original notebooks are preserved under `notebooks/local_ratio_original/` and
  `notebooks/ipsns_original/` for provenance.
- Reusable Python code was extracted and reorganized under `src/mwfas/`:
  - `io.py` — DIMACS reader
  - `evaluation.py` — forward/backward weight evaluation
  - `lrta.py` — LR-TA algorithm (graph building, cycle finding, topo sort,
    reachability checker, and end-to-end entry point)
  - `wmsf.py` — WMSF algorithm (SCC decomposition, removeArcs, MinimizeFas,
    StabilizeFas, and end-to-end entry point)
  - `ipsns.py` — IPSNS/LNS algorithm (SCC-restricted utilities, seed solutions,
    LNS destroy+repair, and end-to-end entry point)
- Hard-coded paths (e.g., `/mmfs1/home/sv96/Feedback-arc-set-paper/datasets/`)
  were replaced by `--input` / `--output` command-line arguments in all scripts.
- Both source READMEs (identical) are preserved in `docs/`.

## License

Both source repositories used MIT License (Copyright 2026 Soroush Vahidi).
The unified repository inherits that license unchanged.
