# License and Provenance Audit

## Repository license

| File | Finding |
|---|---|
| Root `LICENSE` | Present (project license for code) |
| `online_resource_1/LICENSE` | Present in OR1 bundle |
| `CITATION.cff` | Present at OR1 root |

## Dataset provenance

| Dataset | Source | Citation in manuscript | Bundled? | License |
|---|---|---|---|---|
| graph-benchmarks (sparse) | GitHub alidasdan/graph-benchmarks | `graph_benchmarks_repo` | **No** — download required | Per upstream repo |
| LOLIB | uv.es Martí library page | `lolib_library`, `MRD12` | **No** | Academic use; cite library |
| SNAP wiki-Vote | Stanford SNAP | `LHK10WikiVote` | **No** — download for EXP9 | SNAP terms |
| Synthetic / diagnostic | In-repo `.d` fixtures | tests/smoke | Yes (small fixtures) | Same as repo |

**Manuscript/OR1 correctly state** public benchmarks are cited, not redistributed.

## External tools

| Tool | Included in git? | License / access | Used in |
|---|---|---|---|
| DRMacIver/FAS | `external_tools/` **gitignored** | R package; author binary | EXP4,5,9,10 |
| python-igraph | PyPI dependency | GPL-2+ (igraph) | EXP4,5 baselines |
| HiGHS (via scipy) | PyPI | MIT (HiGHS) | EXP8 |
| graph-benchmarks clone | External download | Per repo | All sparse exps |

See `EXTERNAL_TOOL_REGISTER.csv` for detail.

## Code provenance

| Component | Attribution in manuscript |
|---|---|
| LR-TA | Demetrescu–Finocchi \cite{DF03}; author LR-TA predecessor |
| WMSF-style | Cavallaro–Cutello \cite{CC25} |
| IPSNS | Author contribution (this work) |
| arXiv preprint | \cite{VahidiKoutis2024arxiv} |

## Predecessor repositories

README links:

- `weighted-minfas-local-ratio`
- `weighted-minfas-codes`

Documented in `docs/provenance/predecessor_project_manifest.md`.

## Confidentiality

- No reviewer letters in tracked upload files.
- `docs/coap_rejection_history_and_revision_plan_20260611/` may contain **editorial strategy** — verify no confidential PDFs before any public release (not opened in this audit).

## Risks

| Risk | Level | Mitigation |
|---|---|---|
| DRMacIver not in repo | Medium for full rerun | Documented; summaries committed |
| Private GitHub | Low for submission | OR1 is complete supplementary artifact |
| EJCO package confusion | Medium for maintainers | Label stale; exclude from COAP uploads |

## Verdict

**Provenance and licensing are adequately documented** for COAP submission. External datasets and DRMacIver are honestly external.
