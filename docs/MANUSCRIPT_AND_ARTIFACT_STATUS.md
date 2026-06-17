# Manuscript and Artifact Status

**Repository:** [SoroushVahidi/minimum-weighted-fas-heuristics](https://github.com/SoroushVahidi/minimum-weighted-fas-heuristics) — **public**.
**Repository branch:** `main` holds the historical COAP snapshot below; the active SN Computer Science retargeting draft lives on branch `sncs-retargeting` (see `docs/sncs_preparation_202606/`) and has not been merged.

**Active target: SN Computer Science. Historical target: Computational Optimization and Applications. COAP status: declined / closed.** The COAP version is retained as a historical submission snapshot: the manuscript was submitted to *Computational Optimization and Applications* and was declined on journal-audience/fit grounds. The current SN Computer Science version retargets the same scientific contribution for a broader computer-science algorithms audience.

| Target | Status | Source | Notes |
|---|---|---|---|
| **Computational Optimization and Applications (COAP)** | **Declined / closed** — submitted and rejected on audience/fit grounds | `paper_coap/` | Historical snapshot only; not under consideration anywhere |
| **SN Computer Science (SNCS)** | **Active target.** First retargeting draft, **not submission-ready** | `paper_sncs/` (branch `sncs-retargeting`) | See `docs/sncs_preparation_202606/SUBMISSION_PACKAGE_STATUS.md` |

**Author decision recorded:** COAP is closed after rejection. SN Computer Science is the active target for the revised IPSNS sparse-digraph manuscript. The SNCS manuscript must not be submitted until the pending Journal of Supercomputing overlap check is completed; see `docs/sncs_preparation_202606/OVERLAP_AND_DISCLOSURE_AUDIT.md` for the full disclosure analysis.

## COAP version (`paper_coap/`, branch `main`)

### Download

| Artifact | Canonical path |
|---|---|
| **Manuscript PDF (GitHub download)** | [`paper_coap/submission/final_upload/Vahidi_COAP_Manuscript.pdf`](../paper_coap/submission/final_upload/Vahidi_COAP_Manuscript.pdf) |
| Manuscript source | `paper_coap/` |
| Online Resource 1 PDF | `online_resource_1/Online_Resource_1.pdf` |
| Portal upload bundle | `paper_coap/submission/final_upload/` |

Historical audit directories under `docs/` are archival only.

### Submission status

This manuscript was **formally submitted** to COAP and was **declined** on journal-audience/fit grounds. The COAP submission is now closed and is retained here only as a historical snapshot; it is not under consideration anywhere. `paper_coap/submission/AUTHOR_PRE_SUBMISSION_CONFIRMATION.md` predates the submission/decline event and its blank sign-off block should not be read as evidence about current status — it is superseded by this section.

### Canonical artifacts

| Artifact | Path | Pages / size |
|---|---|---|
| Manuscript PDF | `paper_coap/main.pdf` / `paper_coap/submission/final_upload/Vahidi_COAP_Manuscript.pdf` | 24 pages, 199,822 bytes |
| Manuscript SHA-256 | `aebdf183f3a1c794b42b5b8a362524e396eaf7f7c8dd379c6c5b48f4a23bca77` | (verified 2026-06-17; supersedes a stale hash recorded in an earlier pass) |
| Manuscript source | `paper_coap/` + source ZIP in `final_upload/` | |
| Online Resource 1 PDF | `online_resource_1/Online_Resource_1.pdf` / `final_upload/Vahidi_Online_Resource_1_MWFAS.pdf` | 14 pages |
| Online Resource 1 ZIP | `final_upload/Vahidi_Online_Resource_1_MWFAS.zip` | see manifest |
| Cover letter | `final_upload/Vahidi_COAP_Cover_Letter.pdf` | |
| Related manuscripts | `final_upload/Vahidi_Related_Manuscripts_Statement.pdf` | |

Checksums: `paper_coap/submission/final_upload/MANIFEST.sha256`

Note: loose root-level files `Vahidi_Online_Resource_1_MWFAS.pdf` / `.zip` are an older, stale duplicate (137,937 / 1,136,708 bytes) left over from before the `final_upload/` bundle was last refreshed; they do not match the canonical hashes above. The canonical copies are `online_resource_1/Online_Resource_1.pdf` and `paper_coap/submission/final_upload/Vahidi_Online_Resource_1_MWFAS.zip`. This is flagged for cleanup but not altered in this pass (out of scope; not a paper_coap content change).

### Abstract

230 words in `paper_coap/main.tex` (COAP 150–250 guideline).

### OR1 provenance

- Rendered OR1 front matter points to `online_resource_1/provenance/source_commit.txt` rather than embedding a packaging commit SHA.
- `source_commit.txt` records the **scientific source snapshot** commit used to build the frozen OR1 bundle, not the packaging commit that contains the frozen bytes.
- See `docs/EXP3_EXACT_GAP_VALIDATION.md` for the exact-validation `0.0006%` reconciliation.

### Editorial Manager handoff

One-file upload copy: `/home/soroush/COAP_initial_submission/Vahidi_COAP_Manuscript.pdf` (byte-identical to the GitHub manuscript PDF after the final sync). This path is local to the author's machine, not part of the repository.

## SNCS version (`paper_sncs/`, branch `sncs-retargeting`)

### Download

| Artifact | Canonical path |
|---|---|
| Manuscript PDF | `paper_sncs/main.pdf` / `paper_sncs/submission/sncs_initial/Vahidi_SNCS_Manuscript.pdf` |
| Manuscript source | `paper_sncs/` + source ZIP in `submission/sncs_initial/` |
| Online Resource 1 | reused unchanged from the COAP bundle (`Vahidi_SNCS_Online_Resource_1.pdf` / `.zip` in `submission/sncs_initial/`) |

### Submission status

**Active target. Not yet submission-ready.** First retargeting pass only: title, structured abstract, keywords, introduction framing, related-work framing, and declarations were adapted for SN Computer Science; problem definition through conclusion are still byte-identical to `paper_coap/`. See `docs/sncs_preparation_202606/CHANGELOG_SNCS_PASS1.md` for the itemized diff and `docs/sncs_preparation_202606/OVERLAP_AND_DISCLOSURE_AUDIT.md` for the one remaining blocking item (the Journal of Supercomputing overlap audit, currently blocked because that manuscript could not be located in the repository or local workspace) that must be resolved by the author before any portal upload.

### Canonical artifacts

| Artifact | Path | Pages / size |
|---|---|---|
| Manuscript PDF | `paper_sncs/main.pdf` | 25 pages, 203,596 bytes |
| Manuscript SHA-256 | `bcb8f30106f08f7e5eba791a5d5c585353e0062c3b16829a18b4bfed510bbe49` | (rebuilt 2026-06-17 after the COAP-status declaration correction; supersedes the pre-correction hash) |
| Abstract | 246 words, structured (Purpose/Methods/Results/Conclusion), SNCS 150–250 guideline | |

Checksums: `paper_sncs/submission/sncs_initial/MANIFEST.sha256`
