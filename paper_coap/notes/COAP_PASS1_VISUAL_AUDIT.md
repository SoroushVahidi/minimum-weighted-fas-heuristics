# COAP Pass 1 Visual Audit

**PDF:** `paper_coap/main.pdf`  
**Date:** 2026-06-10  
**Pages:** 36  
**SHA-256:** `a181b82b05b2f8e280362d1600400bab16c4343ec9e3f16cf5b85bb92b0b56bf`

## Automated text checks (pdftotext)

| Check | Result |
|---|---|
| Title block | PASS |
| Author name | PASS |
| Corresponding author email | PASS |
| Abstract present | PASS (182 words) |
| Six keywords | PASS |
| Numbered in-text citations `[n]` | PASS |
| Numbered reference list | PASS (26 entries) |
| No `??` unresolved references | PASS |
| No stale EJCO/CAIE/Elsevier wording | PASS |
| Figure 1 caption text | PASS |
| Statements content (Funding, competing interests, data availability, generative AI) | PASS |
| Online Resource 1 placeholder | PASS |

## Manual review targets (spot-checked via text extraction)

| Region | Result | Notes |
|---|---|---|
| Title and author block | PASS | ORCID renders as adjacent text `VahidiORCID` because logo EPS unavailable |
| Abstract | PASS | Within 150–250 words |
| Keywords | PASS | Six keywords |
| Figure 1 (TikZ framework) | PASS | Caption extracted; vector figure compiled |
| Dense tables | PASS with caveat | LOLIB table has known overfull hbox in source log (~34 pt); values intact |
| Algorithms | PASS | Algorithm 1–3 text present in PDF extract |
| Figure 4 / 5 (exp4 panels) | PASS | Captions and figure references present |
| Budget curve figure | PASS | EXP6 figure caption present |
| LOLIB figure | PASS | Family scope caption present |
| Statements and Declarations | PASS | Combined section before references |
| References | PASS | Springer numbered style |
| Last page | PASS | Reference list completes on page 36 |

## Warnings (non-fatal)

- Multiple underfull `\vbox` warnings from Springer page breaks (not visually severe in spot check)
- LOLIB table slightly wide in LaTeX log; monitor in human PDF review
- `algorithm.sty` UTF-8 warning from engine (pre-existing package quirk)
- ALS09 and some proceedings entries show `???` publisher placeholder in bibliography (BST formatting of missing address field; not missing citation keys)

## Verdict

**Template migration compiles successfully and is internally consistent for pass 1.**  
Not submission-ready: supplementary `ESM_1.zip`, cover letter, related-manuscript disclosure, and final upload package remain deferred.
