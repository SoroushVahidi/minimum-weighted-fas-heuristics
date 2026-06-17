# Minimum Weighted Feedback Arc Set Heuristics

## Manuscript targets (active target: SN Computer Science — see status doc before acting on either)

**Active target: SN Computer Science (SNCS). Historical target: Computational Optimization and Applications (COAP). COAP status: declined / closed.** The COAP version was formally submitted to *Computational Optimization and Applications* and was declined on journal-audience/fit grounds; `paper_coap/` is retained as a historical submission snapshot, not an active target. The SN Computer Science version retargets the same scientific contribution for a broader computer-science algorithms audience. Full status and artifact paths: `docs/MANUSCRIPT_AND_ARTIFACT_STATUS.md`.

**Author decision recorded:** COAP is closed after rejection. SN Computer Science is the active target for the revised IPSNS sparse-digraph manuscript.

**Author confirmation recorded:** the Journal of Supercomputing manuscript concerning learning-free ranking from pairwise comparisons via feedback-arc-set pruning and add-back is related but distinct and is not a substantial overlap concern for the present SN Computer Science manuscript. The local workspace did not contain the Supercomputing PDF/source, so no text-level comparison was performed; however, the author confirms that the SNCS manuscript is a distinct sparse-digraph SCC-local refinement study and that no substantially overlapping manuscript is currently under consideration elsewhere.

| Target | Status | Source |
|---|---|---|
| Computational Optimization and Applications (COAP) | **Declined / closed** (historical submission snapshot) | `paper_coap/` (branch `main`) |
| SN Computer Science (SNCS) | **READY FOR HUMAN REVIEW BEFORE SNCS SUBMISSION** — active target, not yet ready for final journal upload | `paper_sncs/` (branch `sncs-retargeting`) |

[Download the COAP manuscript PDF](paper_coap/submission/final_upload/Vahidi_COAP_Manuscript.pdf?raw=1) — Title: *IPSNS for Minimum Weighted Feedback Arc Set on Sparse Digraphs* (historical, declined submission)

Active Online Resource 1: `online_resource_1/Online_Resource_1.pdf`
Historical submission and audit directories under `docs/` are archival only and are not active upload materials.

---

Reproducible implementation and experiments for the **minimum weighted feedback arc set (MWFAS)** problem on **sparse nonnegative weighted digraphs**.

**Primary contribution:** IPSNS (incumbent-protected SCC neighborhood search) — an SCC-local destroy-and-repair heuristic integrated with LR-TA and WMSF-style seeds. LR-TA and WMSF-style seeding inherit prior work (Demetrescu–Finocchi lineage; Cavallaro–Cutello pipeline); IPSNS is the new integrated framework.

> Repository is **public**. Online Resource 1 is the supplementary reproducibility artifact, shared by both manuscript targets.

---

## Scope and limitations

- **Nonnegative edge weights** in standard comparisons (negative-weight instances excluded).
- **Sparse general digraphs** as primary benchmark; dense LOLIB reported as a scope boundary.
- See `docs/KNOWN_LIMITATIONS.md`.

---

## Canonical layout

| Path | Purpose |
|---|---|
| `src/mwfas/` | **Canonical** algorithm source (edit here) |
| `tests/` | Pytest suite (91 collected) |
| `scripts/` | CLI runners |
| `experiments/` | EXP1b–EXP11 + COAP sensitivity/holdout |
| `paper_coap/` | **COAP manuscript** (24 pages) |
| `paper_coap/submission/final_upload/` | **Portal upload bundle** (6 files) |
| `paper_sncs/` | **SNCS manuscript draft** (25 pages, branch `sncs-retargeting`, not submission-ready) |
| `online_resource_1/` | Online Resource 1 source + validation (shared by both manuscript targets) |
| `docs/INDEX.md` | Documentation navigation |
| `docs/archive/` | Historical EJCO packages and legacy `paper/` tree |

**Do not use** `docs/archive/legacy_submission_packages/` for COAP uploads.

---

## Installation

```bash
pip install -r requirements.txt
pip install -e .
```

Benchmark instances: [alidasdan/graph-benchmarks](https://github.com/alidasdan/graph-benchmarks). List paths in `configs/benchmark_instances.txt`.

---

## Quick usage

```bash
# LR-TA
python scripts/run_lrta.py --input /path/to/instance.d --output /tmp/lrta.csv

# WMSF (use ordering L2 by default)
python scripts/run_wmsf.py --input /path/to/instance.d --output /tmp/wmsf.csv

# IPSNS (always --wmsf-seed-mode full)
python scripts/run_ipsns.py --input /path/to/instance.d --output /tmp/ipsns.csv --wmsf-seed-mode full

# Exact DP (n ≤ 20)
python scripts/run_exact.py --input /path/to/instance.d --output /tmp/exact.csv
```

**Objective:** reported backward weight `bw(π)` from the returned ranking (ordering objective), not removed-set weight alone.

---

## Tests

```bash
PYTHONPATH=src python3 -m pytest --ignore=experiments/exp4_external_baselines/external_tools -q
```

Expected: **90 passed, 1 skipped** (EXP10 namespace test when DRMacIver runner inactive).

---

## Experiments

See [`experiments/README.md`](experiments/README.md) and [`docs/EXPERIMENT_REGISTRY.csv`](docs/EXPERIMENT_REGISTRY.csv).

| Study | Role |
|---|---|
| EXP1b | Main 105-instance internal benchmark |
| EXP4 | Sparse external comparison (96/97 wins) |
| EXP10 | 20× repeated-run robustness (38/55/0 medians) |
| EXP11 | Topological extraction calibration |
| coap_ipsns_holdout | Parameter holdout (1290 runs) |

**EXP1 is superseded** — do not cite.

---

## Reproduction levels

| Level | What |
|---|---|
| A | Pytest + OR1 smoke scripts |
| B | Regenerate principal tables from committed summaries (`online_resource_1/scripts/`) |
| C | Re-run experiments from configs (requires external benchmarks) |
| D | Full EXP10 raw rerun (DRMacIver binary + compute; summaries committed) |

---

## Manuscript and submission

See `docs/MANUSCRIPT_AND_ARTIFACT_STATUS.md` for the full status.

- **COAP manuscript (historical, declined):** `paper_coap/main.pdf`; upload files in `paper_coap/submission/final_upload/` (see `MANIFEST.sha256`)
- **SNCS manuscript (active target, draft, branch `sncs-retargeting`):** `paper_sncs/main.pdf`; upload files in `paper_sncs/submission/sncs_initial/` (see `MANIFEST.sha256`)
- **Online Resource 1:** `online_resource_1/Online_Resource_1.pdf` / canonical ZIP in `paper_coap/submission/final_upload/Vahidi_Online_Resource_1_MWFAS.zip` (shared by both manuscripts; the loose root-level `Vahidi_Online_Resource_1_MWFAS.pdf`/`.zip` copies are a stale duplicate flagged in the status doc)

---

## Provenance

Merges predecessor repositories [weighted-minfas-local-ratio](https://github.com/SoroushVahidi/weighted-minfas-local-ratio) and [weighted-minfas-codes](https://github.com/SoroushVahidi/weighted-minfas-codes). See `docs/provenance/`.

---

## License

MIT — see [LICENSE](LICENSE).
