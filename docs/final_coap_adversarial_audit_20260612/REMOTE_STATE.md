# Remote Repository State Verification

**Audit date:** 2026-06-12  
**Repository:** `https://github.com/SoroushVahidi/minimum-weighted-fas-heuristics`  
**Expected pre-audit commit:** `f306c15259132c564f981316872cfc63e94e2f80`

## Phase 1 — Git state (pre-correction baseline)

| Check | Result |
|---|---|
| Current branch | `main` |
| Local SHA (at audit start) | `f306c15259132c564f981316872cfc63e94e2f80` |
| Remote `origin/main` SHA (at audit start) | `f306c15259132c564f981316872cfc63e94e2f80` |
| Local/remote match | **Yes** |
| Working tree (at audit start) | **Clean** |
| Post-audit rebuild drift | `main.pdf` rebuilt during validation; restored then corrected abstract edits applied |
| Ignored submission-critical files | None identified locally only; all six portal files present under `paper_coap/submission/final_upload/` |
| Root OR1 copies | `Vahidi_Online_Resource_1_MWFAS.pdf` and `.zip` at repo root match upload bundle (committed at f306c15) |

## Commit contents verified at f306c15

The pushed commit includes:

- COAP manuscript (`paper_coap/`) with 45-page `main.pdf`
- Online Resource 1 (`online_resource_1/`, root OR1 PDF/ZIP)
- Submission package (`paper_coap/submission/final_upload/`, cover letter, related-manuscript statement)
- Implementation (`src/mwfas/`), tests, experiment summaries (EXP1b–EXP11)
- Prior audit directories (`docs/coap_*`)

Excluded by policy: raw EXP10 checkpoints, confidential correspondence, caches.

## GitHub repository metadata

| Property | Value |
|---|---|
| Visibility | **Private** (`gh api` confirmed) |
| Default branch | `main` |
| Description | null (unset) |
| Last push | 2026-06-12T03:32:49Z |

## Homepage / README

README states the repository is **private while the manuscript is under preparation**. This is accurate and consistent with current GitHub visibility. The manuscript Data Availability statement points to Online Resource 1 rather than claiming a public GitHub URL.

## Post-audit correction state

Two manuscript defects required correction before submission:

1. Abstract exceeded COAP 150–250 word guideline (271 words → 238 words).
2. Related-work section described EXP10 as “ongoing” despite completion.

Updated files: `paper_coap/main.tex`, `paper_coap/sections/02_related_work.tex`, rebuilt `main.pdf`, refreshed `final_upload/` manuscript PDF and source ZIP. A new commit is required before portal upload.

## Answers (Phase 1)

1. **Current branch:** `main`
2. **Local SHA at audit start:** `f306c15259132c564f981316872cfc63e94e2f80`
3. **Remote SHA at audit start:** `f306c15259132c564f981316872cfc63e94e2f80`
4. **Match:** Yes (pre-correction)
5. **Working tree clean at start:** Yes
6. **Automatic post-push modification:** None to tracked files until audit rebuild/validation
7. **Local-only submission files:** None
8. **Commit contains intended artifacts:** Yes at f306c15
9. **Homepage reflects project state:** Yes (private, MWFAS heuristics, predecessor links)
