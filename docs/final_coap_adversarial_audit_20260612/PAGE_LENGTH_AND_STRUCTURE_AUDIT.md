# Page Length and Information Density Audit

**Main manuscript:** `paper_coap/main.pdf`  
**Pages:** 45 (unchanged after abstract trim)  
**Online Resource 1:** 12 pages

## Official COAP limits

| Limit type | Verified? | Finding |
|---|---|---|
| Hard page maximum | **Not verified** on live COAP guidelines page during this audit (fetch timeout); prior repo audit recorded no mandatory page cap | No confirmed desk-rejection trigger |
| Soft norm (concise articles) | Springer Nature general guidance | Articles should be as concise as practicable |
| Abstract 150–250 words | Verified in repo COAP guidelines audit (2026-06-10) | **Was exceeded; corrected to 238 words** |

## Editorial risk of 45 pages

**Assessment: minor editorial risk, not a blocker.**

Rationale:

- COAP publishes algorithm-engineering papers with extensive computational evidence.
- The manuscript’s length is driven by scoped multi-stream validation (exact, MIP, external baselines, ablation, holdout, EXP10, EXP11, LOLIB boundary) rather than redundant theory.
- Formal analysis and proofs are largely deferred to Online Resource 1.

## Material already in OR1 (appropriate)

- Full proofs (S4)
- Extended tables and EXP10/EXP11 detail (S10–S12)
- Parameter tables and reproduction protocol (S7, S9, S14)
- Test documentation (S13)

## Candidates for future trimming (optional, not required now)

| Material | Location | Recommendation |
|---|---|---|
| Secondary runtime-quality table | `table_runtime_quality_tradeoff.tex` | Already omitted from main PDF |
| Long baseline prose | Section 5 | Retain — supports scoped external-baseline honesty |
| Duplicated limitation sentences | Discussion + conclusion | Minor overlap acceptable |
| EXP11 detail | Main results | Appropriately brief; full detail in OR1 |

## Recommendation

**Retain 45 pages** for initial submission. Do not compress aggressively. If an editor requests shortening, move additional EXP10 diagnostic tables to OR1 first.

## Answer

14. **Within verified journal length requirements?** Yes — no verified hard page limit; abstract now within 150–250.  
15. **Is 45 pages an editorial risk?** Minor soft risk only.
