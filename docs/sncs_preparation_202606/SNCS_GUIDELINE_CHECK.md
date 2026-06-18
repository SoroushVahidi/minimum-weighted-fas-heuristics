# SN Computer Science Submission Guideline Check

**Access date:** 2026-06-17
**Journal:** SN Computer Science
**Springer journal ID:** 42979
**Method:** Live web search/fetch of the official Springer Nature Link pages (not relied on training-data memory).

## Official guideline URLs consulted

| Resource | URL | Access date |
|---|---|---|
| SN Computer Science submission guidelines | https://link.springer.com/journal/42979/submission-guidelines | 2026-06-17 |
| SN Computer Science aims and scope | https://link.springer.com/journal/42979/aims-and-scope | 2026-06-17 |
| SN Computer Science home | https://link.springer.com/journal/42979 | 2026-06-17 |

Note: the submission-guidelines page required following a cookie/auth redirect chain before the content rendered; the extraction below is from the final rendered page content, not a cached/secondary source.

## Requirements extracted

| Item | SNCS requirement | Source |
|---|---|---|
| Article type | "Original Research" (also Survey/Review, Brief Communication, Continuing Education are separate categories). This manuscript is Original Research. | submission-guidelines + search confirmation |
| Peer review | **Single-blind**, minimum 2 reviewers per article | submission-guidelines |
| Title page | Concise/informative title; author names; affiliations; corresponding author + active email; ORCID (16-digit) if available | submission-guidelines |
| Abstract | **Structured abstract, 150–250 words**, with sections **Purpose, Methods, Results, Conclusion** (Trial registration section is life-science-only, not applicable here) | submission-guidelines |
| Keywords | **4 to 6 keywords** for indexing | submission-guidelines |
| Source files | Primary format is Word (.docx/.doc); **"Manuscripts with mathematical content can also be submitted in LaTeX. We recommend using Springer Nature's LaTeX template."** Full editable source files required. | submission-guidelines |
| LaTeX template | Same Springer Nature `sn-jnl` class family used for COAP — no class change needed, only metadata/content | submission-guidelines + repo template_reference |
| Declarations | "Statements and Declarations" section before references, covering: Competing Interests, Funding, Ethics Approval, Consent to Participate/Publish, Data and Code Availability, Author Contributions (recommended) | submission-guidelines |
| AI-assisted writing disclosure | LLM usage in writing must be documented (Methods or another suitable section); LLMs cannot be listed as authors; "AI-assisted copy editing" limited to grammar/spelling/punctuation/tone does **not** require declaration | submission-guidelines |
| Data/code availability | "All authors are requested to make sure that all data and materials as well as software application or custom code support their published claims" — no fixed wording mandated | submission-guidelines |
| Supplementary material naming | Refer to supplementary files as **"Online Resource"** (e.g., "Online Resource 1"); name files consecutively (e.g., `ESM_1.pdf`); each supplementary file must self-identify article title, journal name, author name(s), affiliation, and corresponding-author email | submission-guidelines |
| Reference style | Numbered, square-bracket in-text citations (e.g., `[3]`); consecutively numbered reference list; DOIs as full links when available | submission-guidelines |

## Decisions for this manuscript based on the above

- **Abstract:** structured, 150–250 words, four labels exactly as specified in the task (`Purpose:`, `Methods:`, `Results:`, `Conclusion:`) — matches official guidance exactly, no deviation needed.
- **Keywords:** task specifies six keywords; SNCS allows 4–6, so six is within range — kept as specified.
- **Source files:** LaTeX is acceptable for mathematical content (this manuscript qualifies) using the Springer Nature template, which is already in use (`sn-jnl.cls`, `sn-mathphys-num` option) — no class/template change required, only `paper_sncs/` content edits.
- **Peer review:** single-blind — author identity stays on the title page (no anonymization needed), consistent with current `paper_sncs/main.tex` author block.
- **Declarations:** current `statements_and_declarations.tex` already has Funding, Competing interests, Author contributions, Related manuscripts/prior work, Data and code availability, and Generative AI sections. Missing: explicit **Ethics approval**, **Consent to participate**, **Consent for publication** sections — added in this pass (see `CHANGELOG_SNCS_PASS1.md`).
- **Online Resource naming:** existing `online_resource_1/` naming convention ("Online Resource 1") already matches SNCS's expected terminology; no rename of the resource concept is required, only SNCS-specific packaging copies under `paper_sncs/submission/sncs_initial/`.
- **AI disclosure:** existing declaration substance (tools used, verification performed, author accountability) is consistent with SNCS policy and is preserved, not weakened.
