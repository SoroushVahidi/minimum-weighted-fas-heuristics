# Source Copy Policy

## Canonical development tree

`src/mwfas/` — all algorithm changes happen here.

## Intentional frozen mirror

`online_resource_1/src/mwfas/` — snapshot packaged in Online Resource 1. Refresh only via `online_resource_1/scripts/finalize_or1.py` after validation.

## Historical copies (do not edit)

- `docs/archive/legacy_submission_packages/ejco_submission_package/ejco_reproducibility_artifact/src/mwfas/`

## Rule

Never fix bugs in the OR1 mirror without updating `src/mwfas/` and re-running OR1 validation.
