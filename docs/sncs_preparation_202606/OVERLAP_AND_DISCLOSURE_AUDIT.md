# Overlap and Disclosure Audit — SN Computer Science Retargeting (Pass 1)

**Audit date:** 2026-06-17
**Scope:** repository-only evidence. No external portals, email, or out-of-repo files were consulted (none were available to this audit).
**Method:** exhaustive `grep`/`find` across the full working tree (including `docs/archive/`) for the manuscript titles, journal name, manuscript ID, and UUID supplied in the task, plus a review of the existing COAP-era related-manuscript audit trail (`docs/coap_related_status_resolution_20260612/`, `docs/archive/internal/coap_rejection_history_and_revision_plan_20260611/`, `paper_coap/submission/related_manuscripts_statement.tex`).

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
| 6 | "IPSNS for Minimum Weighted Feedback Arc Set on Sparse Digraphs" | Computational Optimization and Applications (COAP) | none assigned | **Prepared, not yet submitted** — see §2 | `paper_coap/` |
| 7 | "An Incumbent-Protected Component-Local Heuristic for Minimum Weighted Feedback Arc Set on Sparse Digraphs" (this pass) | SN Computer Science (SNCS) | none assigned | New working draft, derived from #6 | `paper_sncs/` |

No DOCX files of any kind were found. No other `.tex`/`.pdf` manuscript sources exist outside the paths above and their immediate build artifacts (figures, tables, declarations).

## 2. Which one is currently pending at The Journal of Supercomputing?

**None.** An exhaustive case-insensitive search of the entire repository — including `docs/archive/`, all bibliography files, all CSV/markdown audit registers, and every `.tex`/`.pdf` file — for each of the following found **zero matches**:

- `Journal of Supercomputing` (exact phrase)
- `OPSE-D-26-00226` (manuscript ID)
- `feb25704-187e-4f95-8640-5e8c1ca26a94` (UUID)
- `Learning-Free Ranking from Pairwise Comparisons via Feedback-Arc-Set Pruning and Add-Back` (title)

The only title in the repository that is textually close to "Learning-Free Ranking from Pairwise Comparisons via Feedback-Arc-Set Pruning and Add-Back" is the arXiv preprint title ("Ranking from Pairwise Comparisons as Minimum Weighted Feedback Arc Set" / "Minimum Weighted Feedback Arc Sets for Ranking from Pairwise Comparisons", arXiv:2412.16181) and the JOCO predecessor ("Fast Local-Ratio Cycle Reduction with Topological Add-Back for Weighted Feedback Arc Sets") — both share thematic vocabulary (pairwise comparisons, feedback arc set, add-back) but neither is the queried title verbatim, and neither carries the ID `OPSE-D-26-00226` or the supplied UUID.

**Conclusion: the Journal of Supercomputing manuscript referenced in the task is not present in this repository in any form** — no source file, no PDF, no mention in any audit/status/lineage document, no bibliography entry. This task's premise that it is a "pending/related" manuscript could not be verified from repository evidence.

**Required author action:** before final SNCS submission, the author must supply (a) the actual manuscript file or its repository location if it exists outside this checkout, or (b) confirmation that no such manuscript exists / it was misidentified, so the SNCS related-manuscripts disclosure and cover letter can be completed accurately. This audit cannot resolve this item from repository evidence and treats it as **blocking** for final submission, not for this preparation pass.

## 3. Overlap in title, methods, experiments, tables, figures, claims, code, and references

Two overlap relationships are relevant. The Journal of Supercomputing manuscript cannot be assessed (see §2). The COAP↔SNCS relationship can be assessed directly and is the dominant finding of this audit:

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

**This statement cannot be carried over unchanged**, for two independent reasons:

1. **The COAP sibling is the elephant in the room.** Per §3/§4, `paper_sncs/` is, at present, substantially the same manuscript as `paper_coap/`. Whether this is a problem depends entirely on COAP's submission status, which the repository evidence leaves ambiguous:
   - `docs/MANUSCRIPT_AND_ARTIFACT_STATUS.md` (last updated before this pass): "A manuscript has been **prepared for submission** to COAP. Portal submission is an author action."
   - `paper_coap/submission/AUTHOR_PRE_SUBMISSION_CONFIRMATION.md`: every checklist box is unchecked; the sign-off block (submission date, COAP manuscript number, confirmation email) is blank.
   - `docs/archive/internal/coap_rejection_history_and_revision_plan_20260611/PRIOR_DECISION_AND_REVIEW_REGISTER.csv`, record SL-06: COAP status = **"Pending"**, submission date = "In preparation," manuscript ID = "Not yet submitted."

   Taken together, repository evidence indicates **COAP has very likely not yet been formally submitted** to Editorial Manager as of this audit. That is good news (no live concurrent submission exists *yet*), but it is precisely why the declaration cannot simply assert "no substantially overlapping manuscript is under consideration elsewhere": if the author submits the COAP version on any later date while the SNCS version is also active (or vice versa), that *would* become a substantially overlapping concurrent submission, and the repository currently contains no explicit record of a decision to retire/withdraw the COAP target in favor of SNCS, or to hold one until the other resolves.

2. **The Journal of Supercomputing manuscript is unverifiable (§2).** A declaration cannot affirmatively assert non-overlap against a manuscript whose existence and content this audit could not confirm.

**Conclusion: the blanket statement is not safe to keep verbatim for the SNCS declaration.** It must be replaced with wording that (a) transparently discloses the COAP sibling relationship and the author's operational commitment to not running both concurrently, and (b) does not make an unconditional claim about manuscripts this audit could not locate.

## 6. Recommended replacement wording

### 6a. In-manuscript declaration (`paper_sncs/declarations/statements_and_declarations.tex`, "Related manuscripts and prior author work")

Applied in this pass:

> This manuscript extends related author work on minimum weighted feedback arc set and ranking-as-ordering heuristics. Section~2.4 describes the relationship to the public preprint (Vahidi and Koutis, arXiv:2412.16181) and explains how the LR-TA and WMSF-style components are attributed. The author has also prepared a manuscript covering the same algorithm and a substantially overlapping experimental program for *Computational Optimization and Applications*, under the title "An Incumbent-Protected Component-Local Heuristic for Minimum Weighted Feedback Arc Set on Sparse Digraphs"; the author will ensure that only one of the two versions is under active consideration at any given time and will disclose the outcome to the editor. No other substantially overlapping manuscript is knowingly under consideration elsewhere at the time of this submission.

This wording is truthful given current repository evidence: it discloses the sibling relationship instead of hiding it, commits to an operational non-concurrency rule the author can actually keep, and hedges the residual claim ("knowingly," "at the time of this submission") rather than asserting something this audit could not verify.

### 6b. Cover-letter disclosure (for the SNCS cover letter, not yet drafted in this pass — see `SUBMISSION_PACKAGE_STATUS.md`)

Recommended paragraph for the eventual `paper_sncs/submission/cover_letter.tex`:

> I confirm that a manuscript describing the same algorithm and a substantially overlapping experimental program, under the title "IPSNS for Minimum Weighted Feedback Arc Set on Sparse Digraphs," has been prepared for submission to *Computational Optimization and Applications* (COAP) but, to my knowledge, has not yet been formally submitted through that journal's portal. I will not allow both versions to be under active review concurrently, and will withdraw or hold whichever version is not progressing before proceeding with the other. I am not aware of any other substantially overlapping manuscript currently under review elsewhere; if information comes to light about a related submission (e.g., to the Journal of Supercomputing) I will disclose it to the editor immediately.

### 6c. Action items before this can be finalized for actual submission

1. **Author must confirm COAP's real-world status** (submitted / not submitted / withdrawn) and record that decision in `docs/MANUSCRIPT_AND_ARTIFACT_STATUS.md` so the declaration in §6a is operationally true at the moment of SNCS submission, not just at the moment of drafting.
2. **Author must supply or rule out the Journal of Supercomputing manuscript.** This audit found no trace of it in the repository; the task's reference to manuscript ID `OPSE-D-26-00226` and a specific UUID strongly suggests it exists somewhere (e.g., a separate local checkout, a cloud drafting tool, or a different repository) that was not made available to this audit.
3. Before final submission, re-run this audit once the remaining manuscript sections (problem definition through conclusion) have actually been differentiated from `paper_coap/`, since §3/§4's "not yet distinct" finding is a snapshot of this pass, not a permanent verdict.

## Overall verdict for this audit

**BLOCKED FOR FINAL SUBMISSION, NOT BLOCKED FOR THIS PREPARATION PASS.** Continuing to draft, build, and locally commit the SNCS retargeting branch is safe. Submitting it to SN Computer Science is not safe yet, for the two reasons in §5. See the final report for the overall pass verdict.
