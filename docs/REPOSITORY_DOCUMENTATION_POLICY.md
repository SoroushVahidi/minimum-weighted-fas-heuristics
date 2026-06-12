# Repository Documentation Policy

## Living documents (update in place)

- `docs/INDEX.md`
- `docs/CANONICAL_SOURCE_MAP.md`
- `docs/EXPERIMENT_REGISTRY.csv`
- `docs/MANUSCRIPT_AND_ARTIFACT_STATUS.md`
- `README.md`, `experiments/README.md`

## When to create a new dated audit directory

Create `docs/<topic>_audit_YYYYMMDD/` only when:

1. A submission gate or major release requires a frozen evidence bundle; and
2. The result cannot be captured by updating a living document.

## Naming

`docs/<short_topic>_audit_YYYYMMDD/` or `docs/<short_topic>_finalization_YYYYMMDD/`

## Do not

- Copy entire repository backups into `docs/`
- Store raw experiment outputs in `docs/` when `experiments/` is the proper home
- Duplicate portal PDFs in audit directories

## Archive superseded audits

Move to `docs/archive/superseded_audits/` only when paths are updated and value is purely historical.
