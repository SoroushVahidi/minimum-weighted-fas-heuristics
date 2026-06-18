# Manuscript and Artifact Status

**Repository:** [SoroushVahidi/minimum-weighted-fas-heuristics](https://github.com/SoroushVahidi/minimum-weighted-fas-heuristics) — **public**.
**Repository branch:** `main` holds the historical COAP snapshot below; the active SN Computer Science retargeting draft lives on branch `sncs-retargeting` (see `docs/sncs_preparation_202606/`) and has not been merged.

**Active target: SN Computer Science. Historical target: Computational Optimization and Applications. COAP status: declined / closed.** The COAP version is retained as a historical submission snapshot: the manuscript was submitted to *Computational Optimization and Applications* and was declined on journal-audience/fit grounds. The current SN Computer Science version retargets the same scientific contribution for a broader computer-science algorithms audience.

| Target | Status | Source | Notes |
|---|---|---|---|
| **Computational Optimization and Applications (COAP)** | **Declined / closed** — submitted and rejected on audience/fit grounds | `paper_coap/` | Historical snapshot only; not under consideration anywhere |
| **SN Computer Science (SNCS)** | **READY FOR HUMAN REVIEW BEFORE SNCS SUBMISSION** — active target, not yet ready for final journal upload | `paper_sncs/` (branch `sncs-retargeting`) | See `docs/sncs_preparation_202606/SUBMISSION_PACKAGE_STATUS.md` |

**Author decision recorded:** COAP is closed after rejection. SN Computer Science is the active target for the revised IPSNS sparse-digraph manuscript.

**Author confirmation recorded:** the Journal of Supercomputing manuscript concerning learning-free ranking from pairwise comparisons via feedback-arc-set pruning and add-back is related but distinct and is not a substantial overlap concern for the present SN Computer Science manuscript. The local workspace did not contain the Supercomputing PDF/source, so no text-level comparison was performed; however, the author has confirmed that the SNCS manuscript is a distinct sparse-digraph SCC-local refinement study and that no substantially overlapping manuscript is currently under consideration elsewhere. See `docs/sncs_preparation_202606/OVERLAP_AND_DISCLOSURE_AUDIT.md` for the full disclosure analysis.

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

**READY FOR HUMAN REVIEW BEFORE SNCS SUBMISSION.** First retargeting pass only: title, structured abstract, keywords, introduction framing, related-work framing, and declarations were adapted for SN Computer Science; problem definition through conclusion are still byte-identical to `paper_coap/`. See `docs/sncs_preparation_202606/CHANGELOG_SNCS_PASS1.md` for the itemized diff and `docs/sncs_preparation_202606/OVERLAP_AND_DISCLOSURE_AUDIT.md` for the full overlap analysis. The COAP-status and Journal of Supercomputing overlap items are both resolved (the latter by author confirmation, not by text-level comparison — the manuscript file remains unavailable locally). This is not yet ready for final journal upload. The remaining task before actual submission is Pass 2: modern FAS/MWFAS references and related-work/baseline-selection paragraphs.

### Canonical artifacts

| Artifact | Path | Pages / size |
|---|---|---|
| Manuscript PDF | `paper_sncs/main.pdf` | 25 pages, 202,453 bytes |
| Manuscript SHA-256 | `92301e20a4f8018f378aa1139fa376d998a3924157a8146e8080976c0ed364ab` | (rebuilt 2026-06-17 after the finalized declaration cleanup and bundle refresh in this continuation pass) |
| Abstract | 246 words, structured (Purpose/Methods/Results/Conclusion), SNCS 150–250 guideline | |

Checksums: `paper_sncs/submission/sncs_initial/MANIFEST.sha256`
