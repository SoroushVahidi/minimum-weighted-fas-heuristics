# Bibliography Verification

**Audit date:** 2026-06-11  
**Source file:** `paper_coap/bibliography/references.bib`

Verification method: primary publisher/DOI/arXiv records and repository audit documents. Perplexity numbering not imported.

| Key | Authors | Title / venue | Year | DOI / ID | Manuscript cite | Status |
|-----|---------|---------------|------|----------|-----------------|--------|
| `DF03` | Demetrescu, Finocchi | Combinatorial Algorithms for Feedback Problems in Directed Graphs, IPL 86(3):129–136 | 2003 | 10.1016/S0020-0190(02)00491-X | LR-TA lineage | **Verified** |
| `CCP24` | Cavallaro, Cutello, Pavone | Efficient Heuristics to Compute Minimal and Stable Feedback Arc Sets, J Comb Optim 48:30 | 2024 | 10.1007/s10878-024-01209-8 | WMSF lineage predecessor | **Added & verified** |
| `CC25` | Cavallaro, Cutello | An Efficient Heuristic Algorithm to Compute Minimal and Stable Weighted Feedback Arc Sets, SEKE 2025, pp. 84–87 | 2025 | 10.18293/SEKE2025-049 | WMSF primary weighted source | **Verified** |
| `BSNA21` | Baharev, Schichl, Neumaier, Achterberg | An Exact Method for the Minimum Feedback Arc Set Problem, JEA 26, Art. 1.4 | 2021 | 10.1145/3446429 | Exact methods context | **Verified** |
| `SST16` | Simpson, Srinivasan, Thomo | Efficient Computation of Feedback Arc Set at Web-Scale, PVLDB 10(3):133–144 | 2016 | 10.14778/3021924.3021930 | Scalable FAS context | **Verified** |
| `VahidiKoutis2024arxiv` | Vahidi, Koutis | Ranking from Pairwise Comparisons as Minimum Weighted Feedback Arc Set | 2024 | arXiv:2412.16181 / 10.48550/arXiv.2412.16181 | Author predecessor | **Added & verified** |
| `drmaciver_feedback_arc_set` | DRMacIver | Feedback-Arc-Set GitHub repository | 2026 | commit 16ff24a… (experiment pin) | External baseline | **Verified as software cite** |
| `python_igraph_feedback_arc_set` | python-igraph developers | Graph.feedback_arc_set documentation | 2026 | python-igraph.org API page | Library baseline | **Verified as documentation cite** |
| `MRD12` | Marti, Reinelt, Duarte | LOLIB benchmark library paper, COAP 51(3):1297–1317 | 2012 | 10.1007/s10589-010-9384-9 | Dense LOLIB context | **Verified** |
| `lolib_library` | Marti | LOLIB official library page | 2010 | uv.es/~rmarti/paper/lop.html | Dataset provenance | **Verified as web resource** |
| `HuangfuHall2018` | Huangfu, Hall | Parallelizing the Dual Revised Simplex Method, MPC 10(1):119–142 | 2018 | 10.1007/s12532-017-0130-5 | HiGHS backend for EXP8 MIP | **Added & verified** |

---

## Notes

- **CCP24 vs CC25:** JoCO 2024 treats unweighted minimal-and-stable FAS; SEKE 2025 is the weighted WMSF source used for the internal seed. Both retained.
- **DRMacIver:** Cited as open-source software with pinned commit in `note` field; not a journal article.
- **igraph:** Documentation citation used because the experiment calls the library API rather than a single paper version.

---

## No action required

Remaining bibliography entries (`ELS93`, `K72`, `F90`, `graph_benchmarks_repo`, etc.) were carried from the pre-edit curated bib and were not flagged in the reframing audits.
