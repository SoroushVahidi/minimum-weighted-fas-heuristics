# COAP Editorial Risk Map

**Audit date:** 2026-06-11  
**Authority:** `docs/final_branch_audit_20260611/COAP_COMPLIANCE_AUDIT.md`, COAP aims & scope (via `paper_coap/COAP_TEMPLATE_AND_GUIDELINES_AUDIT.md`)

Risk levels: **Desk-rejection | High reviewer | Moderate reviewer | Low | Resolved**

---

## Scope fit: COAP vs prior venues

| Prior concern venue | Issue | COAP view |
|--------------------|-------|-----------|
| CAIE | Engineering/heuristic focus | COAP accepts computational optimization heuristics with rigorous evaluation — **better fit for formal analysis** |
| EJCO | OR computational methods | Near-identical fit; COAP adds Springer Nature COAP-specific disclosure rules |
| JOCO | Combinatorial optimization theory | COAP less demanding on approximation theorems — **fit if framed as engineering** |
| DAM | Discrete algorithms / graphs | Overlap high; unified COAP paper reduces split-paper concern if disclosed |
| C&OR (considered, not submitted) | Higher theory bar | COAP preferred over C&OR given current evidence portfolio |

---

## Risk map by objection

| Objection | COAP scope issue? | Desk risk? | Reviewer risk | Revision level | Manuscript section |
|-----------|-------------------|------------|---------------|----------------|-------------------|
| Undisclosed arXiv/predecessors | Ethics, not scope | **Yes** | High | Mandatory pre-submission | Cover letter; §2; portal uploads |
| Salami slicing | Ethics | **Yes** | High | Mandatory | Cover letter; overlap matrix |
| LR-TA novelty leakage | No | No | Moderate | Revision | §1–§2; contribution list |
| IPSNS incremental vs Elsevier-V | No | No | High | Revision + disclosure | §2; §4; cover letter |
| DRMacIver single-run | No | No | **High** | Mandatory (EXP10) | §5–§6 |
| Missing OR1 / tests | Reproducibility policy | **Yes** | High | Mandatory | Declarations; supplement |
| LOLIB weakness | No (honest scope) | No | Low | None if framed as boundary | §6–§7 |
| No approximation theorem | No (COAP accepts heuristics) | No | Moderate | Clarify in abstract | §4; §7 |
| GNNRank absent | No (scoped out) | No | Low | Optional sentence | §2; §5 |
| Manuscript length | Format | Possible | Moderate | Consolidate | All; move to OR1 |
| False cover letter | Ethics | **Yes** | High | Rewrite | Cover letter only |
| Parameter defaults | No | No | Moderate | Holdout paragraph | §5 |
| sfas baseline gap | No | No | Moderate | Document exclusion | §5 |
| HiGHS citation | Minor editorial | No | Low | Bib fix | §5; references.bib |

---

## Desk-rejection checklist (COAP)

| Trigger | Current status | Mitigation |
|---------|----------------|------------|
| Related manuscript nondisclosure | **FAIL** | Upload predecessors + cover letter paragraph |
| Simultaneous duplicate submission | Unknown — author must confirm | State withdrawals in cover letter |
| Missing supplementary files when claimed | **FAIL** | Build OR1 before upload |
| Template noncompliance | **PASS** | sn-jnl present |
| Missing declarations | **PASS** | statements_and_declarations.tex complete |
| Inaccurate originality statement | **FAIL** | Rewrite cover letter |

---

## Reviewer-level battle lines

1. **“This is three old papers stapled together.”**  
   Counter: Unified formal analysis (Props 1–4); expanded experiments; EXP10; holdout; LOLIB scope boundary — with transparent predecessor uploads.

2. **“IPSNS is just LNS with SCC scoring.”**  
   Counter: Incumbent-protection invariant (Prop 3); EXP7 shows generic LS insufficient; ablation + budget curve.

3. **“37/55/1 vs DRMacIver is one lucky run.”**  
   Counter: EXP10 (mandatory before submission).

4. **“No approximation guarantee.”**  
   Counter: Explicitly scoped; near-optimal on EXP3/EXP8; not claiming APX.

---

## Mapping to COAP expectations (from compliance audit)

| COAP requirement | Prior objection addressed | Status |
|------------------|---------------------------|--------|
| Computational optimization contribution | Novelty/theory gap | Met via IPSNS + empirical program |
| Reproducible research | RR-006, RR-019, RR-020 | **Not met until OR1 + tests** |
| Honest limitations | RR-004 | Met via LOLIB |
| Related work completeness | RR-017 | **Not met** |
| Supplementary Online Resource | RR-020 | **Not met** |
