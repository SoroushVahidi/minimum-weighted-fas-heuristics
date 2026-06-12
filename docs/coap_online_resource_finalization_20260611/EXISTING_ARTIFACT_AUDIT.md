# Existing Artifact Audit

## Repository state

1. **Branch:** main  
2. **HEAD:** `80b3144d5fdbbe250faed8a4fe671dde2da76c89`  
3. **Working tree:** modified manuscript and OR1 paths; no commit performed (per instruction).

## Prior artifact (stale)

| Property | Value |
|---|---|
| Filename | `Vahidi_Online_Resource_1_MWFAS_stale_20260612.zip` (backup) |
| SHA-256 | `c95e09dd86b5bebc7e33c6fe9b78d50aa408b2c24d2c5af8214dc80ae63e40c5` |
| Size | 1,042,550 bytes |

The prior root-level ZIP predated EXP11, corrected F/H/π/B_π notation, and the 90-test gate.

## Current artifact

| Property | Value |
|---|---|
| PDF | `Vahidi_Online_Resource_1_MWFAS.pdf` — 12 pages, `8cc1479fb7aebe9e8b4c219aada0bf87f6c0383f53345a2d851b776b581aa0ea` |
| ZIP | `Vahidi_Online_Resource_1_MWFAS.zip` — 1,115,845 bytes, `5c922e64b34576b4f6fef4d22b45c9fab9fdc4e8821578439f3c46146dc8aa22` |
| Top-level directory in ZIP | `online_resource_1/` |

## Stale references remediated

- 78/77-test counts → updated to 91 collected / 90 passed / 1 skipped (full repo) and 86 collected / 79 passed / 7 skipped (OR1 package)
- Missing EXP11 → S12 + results/exp11 + registry entry
- Objective-equivalence wording → S2 proofs and manuscript §3
- Absolute `/home/soroush/` paths → sanitized; internal preflight MD excluded
- Obsolete EXP10 preflight report → excluded from publication bundle

## ZIP replacement safety

Stale ZIP backed up under `docs/coap_online_resource_finalization_20260611/` before replacement. **Safe to replace** — completed.
