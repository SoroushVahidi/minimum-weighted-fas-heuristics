# Related Manuscripts Audit

**Audit date:** 2026-06-10 (updated 2026-06-11 — predecessor identity corrections applied)  
**Note:** Factual inventory only — no legal conclusions.

## 2026-06-11 Critical additions

**arXiv:2412.16181 (Vahidi & Koutis) identified as undisclosed author predecessor.**

The JOCO predecessor manuscript (archive ZIP) cites arXiv:2412.16181 as [V25-2]:
"Vahidi and Koutis formulate ranking from pairwise comparisons as a minimum weighted feedback
arc set problem and propose combinatorial heuristics with strong empirical performance and fast
runtimes on standard benchmarks."

This preprint:
- Is by the COAP corresponding author (Vahidi) and co-author Koutis.
- Is NOT cited in the COAP manuscript or bibliography.
- Must be treated as an author predecessor requiring COAP portal disclosure.
- Cannot be treated as independent competing work.

The full content of arXiv:2412.16181 was not retrieved in this audit. Full-text access is
needed to determine whether IPSNS, WMSF, or the specific experimental results appear there.

See `RELATED_MANUSCRIPT_CONTRIBUTION_MATRIX.md` for complete overlap analysis and
`NOVELTY_AND_PRIOR_WORK_AUDIT.md` for the overall prior-work assessment.

**The JOCO predecessor manuscript is the source of LR-TA as implemented.**

The JOCO predecessor (archive ZIP main.tex) contains:
- LR-TA Phase I and Phase II in exact correspondence with `lrta.py`
- Heavy-first add-back by **original weights** (confirmed in text: "nonincreasing order of
  their original weights")
- Topological fast path and reachability fallback as in current code
- 33-instance benchmark results
- Partial complexity analysis
- Single author (Vahidi) — NOT co-authored with Koutis

The JOCO predecessor also cites arXiv:2412.16181 as a related work by "Vahidi and Koutis."



## Known related work (repository evidence)

| Item | Evidence | Likely overlap |
|---|---|---|
| Predecessor LR-TA (JOCO target) | `docs/provenance/predecessor_project_manifest.md`, `archive/predecessor_projects/Fast_Local_Ratio_*JOCO.zip` | LR-TA algorithm, text, figures |
| Predecessor IPSNS/WMSF (Elsevier) | Same manifest, `Incumbent_Protected_SCC_*zip` | IPSNS, WMSF, experiments |
| CAIE submission | Git history `d496b8a Finalize CAIE submission package` | Full manuscript variant |
| EJCO submission | `submission_package/`, commits `581ee35`–`623f044` | Near-identical to pre-COAP manuscript |
| COAP current | `paper_coap/` since `7e8e0b7` | EJCO + formal analysis + template |
| OPSEARCH ranking/FAS | Listed in `RELATED_MANUSCRIPTS_AUDIT_NEEDED.md` | **Not audited** — extent unknown |
| DAM submission | Same deferred note | **Not audited** |
| arXiv / Research Square | Deferred note | **Unknown** — search not performed in this pass |
| Identical predecessor notebooks | `notebooks/` (both repos) | All three algorithms in one notebook |

## Shared components (exact)

| Component | Shared across |
|---|---|
| `src/mwfas/lrta.py`, `wmsf.py`, `ipsns.py` | Current + EJCO artifact |
| EXP1b–EXP9 summaries | Manuscript tables |
| Framework figure / TikZ | `paper_coap/figures/` |
| Bibliography core | `references.bib` keys largely shared |

## COAP portal requirement

From `paper_coap/COAP_TEMPLATE_AND_GUIDELINES_AUDIT.md` and deferred note:
- Discuss **all related papers**, including unpublished
- Upload copies of related unpublished manuscripts **when applicable**

## Risk assessment (inference)

| Risk | Level | Mitigation |
|---|---|---|
| Duplicate publication | **Moderate–High** without disclosure | Side-by-side overlap document + cover letter |
| Salami slicing (LR-TA vs IPSNS papers) | **Moderate** | Unified narrative in current title helps |
| Reviewer discovers EJCO/CAIE package in repo | **Moderate** | Transparent citation of prior submissions |
| Text overlap with predecessor ZIPs | **Unknown** | Text diff needed |

## Must disclose (minimum)

1. Prior CAIE and EJCO submission attempts (same repository history)
2. Predecessor GitHub repos (`weighted-minfas-local-ratio`, `weighted-minfas-codes`)
3. Any OPSEARCH / DAM versions if submitted or publicly posted
4. Relationship between current unified title and split predecessor papers

## Copies to prepare for upload (TBD after manual review)

- [ ] EJCO manuscript PDF from `submission_package/`
- [ ] CAIE package if substantially different
- [ ] Predecessor ZIP manuscripts if not superseded
- [ ] OPSEARCH/DAM versions if they exist

## Missing comparison documents

- No side-by-side text diff
- No table of reused experiments vs new experiments
- No explicit "what is new in COAP vs EJCO" paragraph (partial in migration notes only)

See `paper_coap/notes/COAP_PASS1_MIGRATION_NOTES.md` for COAP-specific deltas (template, formal analysis, ESM deferral).
