# Overlap and Disclosure Audit — SN Computer Science Retargeting (Pass 1)

**Audit date:** 2026-06-17 (updated 2026-06-17 following an author correction of COAP's submission status — see "Author decision recorded" below; updated again 2026-06-17 following the author's explicit confirmation that the Journal of Supercomputing manuscript is not a substantial overlap concern — see §2 and the Overall verdict)
**Scope:** repository evidence plus an exhaustive local-workspace search (the full `/home/soroush` home directory, not just this repository checkout). No external portals or email accounts were consulted directly by this audit; the existence of the Journal of Supercomputing manuscript is taken as an established fact per the author's email records, supplied directly by the author.
**Method:** exhaustive `grep`/`find` across the full working tree (including `docs/archive/`) and across the entire local workspace for the manuscript titles, journal name, manuscript ID, and UUID supplied in the task, plus a review of the existing COAP-era related-manuscript audit trail (`docs/coap_related_status_resolution_20260612/`, `docs/archive/internal/coap_rejection_history_and_revision_plan_20260611/`, `paper_coap/submission/related_manuscripts_statement.tex`).

**Active target: SN Computer Science. Historical target: Computational Optimization and Applications. COAP status: declined / closed.** The COAP version is retained as a historical submission snapshot: the manuscript was submitted to *Computational Optimization and Applications* and was declined on journal-audience/fit grounds. The current SN Computer Science version retargets the same scientific contribution for a broader computer-science algorithms audience.

**Author decision recorded:** COAP is closed after rejection. SN Computer Science is the active target for the revised IPSNS sparse-digraph manuscript.

## 1. What related manuscripts exist in the repository?

Search command used (and variants of it):

```
find . -iname '*.tex' -o -iname '*.pdf' -o -iname '*.docx' | sort
grep -rliE "Learning-Free Ranking|Fast Local-Ratio Cycle Reduction|Ranking from Pairwise Comparisons as Minimum|Journal of Supercomputing|supercomputing|OPSE-D-26-00226|feb25704-187e-4f95-8640-5e8c1ca26a94" .
```

Confirmed related manuscripts/packages in the repository, oldest to newest:

| # | Title | Target venue | Manuscript ID (repo evidence) | Status per repo evidence | Location |
|---|---|---|---|---|---|
| 1 | "Minimum Weighted Feedback Arc Sets for Ranking from Pairwise Comparisons" (bib title: "Ranking from Pairwise Comparisons as Minimum Weighted Feedback Arc Set") — Vahidi & Koutis | arXiv (public preprint) | arXiv:2412.16181 | Public preprint, not a journal submission | cited throughout `paper_coap/` and `paper_sncs/`; `bibliography/references.bib` |
| 2 | "Fast Local-Ratio Cycle Reduction with Topological Add-Back for Weighted Feedback Arc Sets" | Journal of Combinatorial Optimization (JOCO) | JOCO-D-26-00099 | **[INFER] rejected/inactive** — internal note only (`reuse_risk_report.md`), no decision letter in repo | `docs/archive/predecessor_manuscripts/paper_legacy_pre_coap/source_material/extracted_archives/Fast_Local_Ratio_..._JOCO/` |
| 3 | "Incumbent-Protected SCC-Neighborhood Search for the Weighted Feedback Arc Set Problem" | Discrete Applied Mathematics (DAM) | DA19469 | **[INFER] rejected/inactive** — internal note only, no decision letter in repo | `docs/archive/predecessor_manuscripts/paper_legacy_pre_coap/source_material/extracted_archives/Incumbent_Protected_SCC.../` |
| 4 | "A Reproducible Local-Ratio and SCC-Refinement Framework for Weighted Ordering in Directed Graphs" | Computers & Industrial Engineering (CAIE) | none recorded | Package prepared (~2026-06-06); author pivoted to EJCO; outcome not in repo | `docs/archive/legacy_submission_packages/` (lineage only; CAIE source itself not retained separately) |
| 5 | "Local-Ratio Seeding and SCC-Based Refinement for the Minimum Weighted Feedback Arc Set Problem" | EURO Journal on Computational Optimization (EJCO) | none recorded | Package finalized and archived; no submission confirmation in repo; superseded by COAP | `docs/archive/legacy_submission_packages/ejco_submission_package/` |
| 6 | "IPSNS for Minimum Weighted Feedback Arc Set on Sparse Digraphs" | Computational Optimization and Applications (COAP) | none recorded in repo | **Submitted and declined — closed, historical snapshot** (author-confirmed; not under consideration anywhere) | `paper_coap/` |
| 7 | "An Incumbent-Protected Component-Local Heuristic for Minimum Weighted Feedback Arc Set on Sparse Digraphs" (this pass) | SN Computer Science (SNCS) | none assigned | New working draft, derived from #6 | `paper_sncs/` |

No DOCX files of any kind were found. No other `.tex`/`.pdf` manuscript sources exist outside the paths above and their immediate build artifacts (figures, tables, declarations).

## 2. Which one is currently pending at The Journal of Supercomputing?

**Confirmed to exist (per the author's email records), but the manuscript file itself was not found anywhere in the repository or local workspace.** This pass extended the search beyond the repository to the entire local workspace (`/home/soroush`), including every other project directory, the local audit-archive directory (`minimum-weighted-fas-heuristics-local-audit-archive/`, including the contents of its two compressed `.tar.gz` working-directory snapshots), and the `outputs/` directory. An exhaustive case-insensitive search for each of the following found **zero genuine matches** (the only hits were false positives: a git object hash and a ruff cache filename that happen to contain the numeric substring "11227", and this audit's own previously written text inside Claude's internal session history, not an external manuscript):

- `Journal of Supercomputing` (exact phrase)
- `OPSE-D-26-00226` (manuscript ID)
- `feb25704-187e-4f95-8640-5e8c1ca26a94` (UUID)
- `Learning-Free Ranking from Pairwise Comparisons via Feedback-Arc-Set Pruning and Add-Back` (title)
- filename patterns for `*Supercomputing*`, `*Learning-Free*Ranking*`, `*Feedback-Arc-Set*Pruning*Add-Back*`

The only title in the repository that is textually close to "Learning-Free Ranking from Pairwise Comparisons via Feedback-Arc-Set Pruning and Add-Back" is the arXiv preprint title ("Ranking from Pairwise Comparisons as Minimum Weighted Feedback Arc Set" / "Minimum Weighted Feedback Arc Sets for Ranking from Pairwise Comparisons", arXiv:2412.16181) and the JOCO predecessor ("Fast Local-Ratio Cycle Reduction with Topological Add-Back for Weighted Feedback Arc Sets") — both share thematic vocabulary (pairwise comparisons, feedback arc set, add-back) but neither is the queried title verbatim, and neither carries the ID `OPSE-D-26-00226` or the supplied UUID.

**Conclusion: the Journal of Supercomputing manuscript was not found in the repository or local workspace.** It is known from email records to exist and to concern "Learning-Free Ranking from Pairwise Comparisons via Feedback-Arc-Set Pruning and Add-Back."

**Author confirmation recorded:** the Journal of Supercomputing manuscript concerning learning-free ranking from pairwise comparisons via feedback-arc-set pruning and add-back is related but distinct and is not a substantial overlap concern for the present SN Computer Science manuscript. The local workspace did not contain the Supercomputing PDF/source, so no text-level comparison was performed; however, the author has confirmed that the SNCS manuscript is a distinct sparse-digraph SCC-local refinement study and that no substantially overlapping manuscript is currently under consideration elsewhere.

This audit could not independently verify that confirmation via text-level comparison (the manuscript file remains unavailable), so it is recorded here as an author-supplied fact rather than an audit finding. It is sufficient to lift this item as a submission blocker, but a text-level comparison should still be performed if the manuscript becomes available before actual journal upload.

## 3. Overlap in title, methods, experiments, tables, figures, claims, code, and references

Two overlap relationships are relevant. The Journal of Supercomputing manuscript could not be assessed by text-level comparison (see §2), but the author has confirmed it is related but distinct and not a substantial overlap concern. The COAP↔SNCS relationship can be assessed directly and is the dominant finding of this audit:

| Dimension | paper_coap vs. paper_sncs (this pass) |
|---|---|
| Title | Different (COAP: "IPSNS for Minimum Weighted Feedback Arc Set on Sparse Digraphs"; SNCS: "An Incumbent-Protected Component-Local Heuristic for Minimum Weighted Feedback Arc Set on Sparse Digraphs") — same algorithm, reworded for acronym-avoidance |
| Abstract | Rewritten as a structured abstract for SNCS; same verified numbers, same conclusions |
| Introduction | Reframed (acronym ordering, "component-local" framing) but same claims, same contributions list, same numbers |
| Related work | Near-identical; one framing sentence added for SNCS |
| Problem definition, algorithmic framework, formal analysis, experimental design, results, discussion, conclusion sections | **Byte-for-byte identical** — not yet touched in this pass |
| Tables (21 files) | **Identical** — direct copies |
| Figures (5 PDFs + 1 TikZ source) | **Identical** — direct copies |
| Code (`src/mwfas/`) | **Identical** — both manuscripts describe the same frozen implementation; no separate codebase |
| References (`bibliography/references.bib`) | **Identical** — direct copy |
| Declarations | Diverging: SNCS pass adds Ethics/Consent sections; data-and-code-availability wording pending update (separate task in this pass) |

This is expected and intentional for a first retargeting pass — `paper_sncs/` was created in this session by copying `paper_coap/` per the task's own instructions (step 3) — but it means that **as of this commit, the two manuscripts are substantially the same paper** by any reasonable overlap standard. Only the title, abstract, keywords, and parts of the introduction and related work differ.

## 4. Is the SNCS manuscript substantially distinct?

**Not yet.** At the end of this first pass, `paper_sncs/` differs from `paper_coap/` only in title, structured abstract, keywords, parts of the introduction, one framing sentence in related work, and the declarations block. The problem definition, algorithmic framework, formal analysis, experimental design, results, discussion, and conclusion sections are unmodified copies. This is consistent with the task's explicit instruction to focus this pass on "title, abstract, keywords, introduction, declarations, and submission packaging" and not rewrite the full paper — but it means the distinctness question must be answered **no** for this snapshot, and re-asked after any later pass that revises the remaining sections.

## 5. Does "No substantially overlapping manuscript is currently under consideration elsewhere" remain true?

**This statement cannot be carried over unchanged, but for a narrower reason than originally assessed.** The original version of this section (written before the author's correction below) reasoned about a hypothetical concurrent-submission risk between COAP and SNCS. That reasoning is now superseded:

1. **The COAP sibling is no longer a concurrency risk.** Per the author's correction, COAP was formally submitted to *Computational Optimization and Applications* and was declined on journal-audience/fit grounds. The COAP submission is closed; it is not under consideration anywhere, and there is no possibility of it being concurrently active with the SNCS submission. Per §3/§4, `paper_sncs/` is, at present, still substantially the same manuscript as the closed `paper_coap/` snapshot — that overlap is expected and disclosable as "this is a revised, retargeted version of a prior, now-declined submission," not as a live concurrency risk.

2. **The Journal of Supercomputing manuscript is now resolved by author confirmation (§2).** Its content remains unavailable to this audit for an independent text-level comparison, but the author has explicitly confirmed it is related but distinct and not a substantial overlap concern. Given that confirmation, the blanket "no substantially overlapping manuscript" statement can be retained, since it accurately reflects the author's assessment.

**Conclusion: the blanket statement is not safe to keep verbatim for the SNCS declaration as originally worded (it predates both the COAP decline and the Supercomputing confirmation), but a corrected version of it is now safe.** It must be replaced with wording that (a) transparently discloses the prior COAP submission and its decline, and (b) confirms, on the basis of the author's stated assessment, that no substantially overlapping manuscript is under consideration elsewhere — while briefly acknowledging the related-but-distinct Supercomputing manuscript so the disclosure is not silent about it.

## 6. Recommended replacement wording

### 6a. In-manuscript declaration (`paper_sncs/declarations/statements_and_declarations.tex`, "Related manuscripts and prior author work")

Updated in this corrected pass:

> An earlier version of this manuscript was submitted to Computational Optimization and Applications and was declined on journal-audience/fit grounds. The present version retargets the same scientific contribution for a broader computer-science algorithms audience. No substantially overlapping manuscript is currently under consideration elsewhere. A related but distinct manuscript concerning learning-free ranking from pairwise comparisons via feedback-arc-set pruning and add-back is being handled separately; it does not substantially overlap with the present sparse-digraph SCC-local refinement study.

This wording is truthful given current evidence: it discloses the prior COAP submission and its decline, and reflects the author's confirmed assessment that the related Journal of Supercomputing manuscript is distinct and not a substantial overlap concern, without over-disclosing beyond what is needed.

### 6b. Cover-letter disclosure (for the SNCS cover letter, not yet drafted in this pass — see `SUBMISSION_PACKAGE_STATUS.md`)

Recommended paragraph for the eventual `paper_sncs/submission/cover_letter.tex`:

> An earlier version of this manuscript was submitted to Computational Optimization and Applications and was declined on journal-audience/fit grounds; that submission is closed and is not under consideration anywhere. I am not aware of any substantially overlapping manuscript currently under review elsewhere. A related but distinct manuscript of mine, concerning learning-free ranking from pairwise comparisons via feedback-arc-set pruning and add-back, is being handled separately and does not substantially overlap with the present sparse-digraph SCC-local refinement study.

### 6c. Action items before this can be finalized for actual submission

1. ~~Author must confirm COAP's real-world status~~ — **Resolved.** Author decision recorded: COAP is closed after rejection (submitted, declined on audience/fit grounds). SN Computer Science is the active target.
2. ~~Author must supply the Journal of Supercomputing manuscript~~ — **Resolved by author confirmation.** The author has confirmed the Supercomputing manuscript is related but distinct and not a substantial overlap concern. The manuscript file remains unavailable in this repository/workspace, so no independent text-level comparison was performed; if the file becomes available before actual journal upload, a text-level comparison should still be run to corroborate this.
3. Before final submission, re-run this audit once the remaining manuscript sections (problem definition through conclusion) have actually been differentiated from `paper_coap/`, since §3/§4's "not yet distinct" finding is a snapshot of this pass, not a permanent verdict.
4. **Pass 2 (not yet done):** add modern FAS/MWFAS references and related-work/baseline-selection paragraphs before actual SNCS submission.

## Overall verdict for this audit

**READY FOR HUMAN REVIEW BEFORE SNCS SUBMISSION.** The COAP-status concern is resolved (COAP is closed; SN Computer Science is the recorded active target), and the Journal of Supercomputing overlap concern is resolved by the author's explicit confirmation that the manuscript is related but distinct and not a substantial overlap concern. This is **not** a certification that the manuscript is ready for final journal upload: Pass 2 (modern FAS/MWFAS references and related-work/baseline-selection language) is still outstanding, and the problem-definition-through-conclusion sections remain byte-identical to the closed `paper_coap/` snapshot. See the final report for the overall pass verdict.
