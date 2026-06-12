# License and Provenance Audit

**Audit date:** 2026-06-10

## Main repository

| Item | Value |
|---|---|
| License file | `LICENSE` — **MIT** (Copyright 2026 Soroush Vahidi) |
| Attribution | Permissive; suitable for code redistribution in ESM |

## Vendored / copied components

| Component | License / provenance | Issue |
|---|---|---|
| `paper_coap/sn-jnl.cls`, `.bst` | Springer Nature template — author use | OK for submission; check redistribution in ESM |
| `paper/elsarticle.cls` | Elsevier template | Historical CAIE/EJCO |
| DRMacIver Feedback-Arc-Set | External clone (gitignored) | Must preserve license in ESM docs |
| python-igraph | BSD-like | Dependency notice |
| LOLIB converted data | Academic benchmark | Verify redistribution terms |
| SNAP wiki-vote | SNAP license | Academic use; cite in manuscript |
| Predecessor ZIPs | `archive/predecessor_projects/` | Provenance only |

## Missing or unclear

| ID | Severity | Item |
|---|---|---|
| L-01 | Moderate | No `LICENSE` in `experiments/exp5_lolib_dense/converted/` |
| L-02 | Low | External tool licenses not bundled (DRMacIver, igraph) — documented in prose only |
| L-03 | Low | Springer template redistribution in public GitHub — standard practice but not explicit |
| L-04 | Moderate | MIT license on code vs academic dataset restrictions — ESM README must clarify |

## Incompatible license risks

- **Low** for code stack (MIT + BSD deps)
- **Moderate** if redistributing full LOLIB converted files without license file

## Attribution gaps

- Predecessor repos cited in `docs/provenance/` — good
- Demetrescu–Finocchi, Simpson, Baharev cited in bib — good
- Copied baseline code: DRMacIver wrapper should retain upstream notice in ESM

## Recommendations

1. Add `DATASETS.md` with license summary for in-repo converted files
2. Include third-party NOTICES file in future `ESM_1.zip`
3. Link external datasets rather than vendoring full graph-benchmarks
