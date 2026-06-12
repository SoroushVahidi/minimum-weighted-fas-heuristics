# Build and Visual Check

**Audit date:** 2026-06-11  
**Build directory:** `paper_coap/`

---

## Build

| Item | Result |
|------|--------|
| Command | `~/.local/bin/latexmk -pdf -interaction=nonstopmode main.tex` |
| Status | **Success** |
| Output | `paper_coap/main.pdf` |
| SHA-256 | `95d1c7fca809adefe7189ac2579160ee869fe07a0dc5c9b4ff8c47593fc8c9f2` |
| Pages (post-edit) | **42** |
| Pages (pre-edit backup) | **40** |

---

## LaTeX diagnostics

| Check | Count | Blocking? |
|-------|-------|-----------|
| Undefined references | 0 | No |
| Undefined citations | 0 | No |
| Duplicate labels | 0 | No |
| Overfull boxes | 0 | No |
| Underfull boxes | 56 | No (typical sn-jnl layout warnings) |

New citations `VahidiKoutis2024arxiv`, `HuangfuHall2018`, `CCP24` compile cleanly after rebuild.

---

## PDF content checks

| Check | Result |
|-------|--------|
| `% EXP10-INTEGRATION` text in PDF | **Absent** |
| `% AUTHOR-STATUS` text in PDF | **Absent** |
| “fully reproducible” in PDF | **Absent** |
| “among all tested methods” in PDF | **Absent** |
| “best known results” in PDF | **Absent** |
| “state of the art” in PDF | **Present only negated** (“not intended to represent state of the art” in §2) |

---

## Front matter verification

| Element | Present / correct |
|---------|-------------------|
| Title (IPSNS-first, sparse scope) | Yes |
| Abstract order (problem → IPSNS → seeds → validation → sparse result → LOLIB → qualified reproducibility) | Yes |
| Contribution list (IPSNS first, four items) | Yes |
| §2.1 Relationship to our prior work | Yes |
| Declarations: related manuscripts subsection | Yes |

---

## Visual / layout spot check

- Title page and abstract: readable; no internal comment leakage.
- Wide tables (`table_sparse_external_baselines`, `table_lolib_scope`, `table_experiment_overview`): no new overfull boxes introduced by reframing edits.
- Algorithm floats and formal-analysis propositions: proofs removed from main text; proposition blocks remain compact.
- Bibliography: new entries appear in numbered list; no orphaned keys.

**No blocking LaTeX or layout issues identified.**
