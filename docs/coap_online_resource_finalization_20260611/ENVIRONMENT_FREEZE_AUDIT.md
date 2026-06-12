# Environment Freeze Audit

## Tested platform

| Component | Value |
|---|---|
| OS | Linux 6.17.0-35-generic |
| Python (tested) | 3.12.3 |
| CPU | 12th Gen Intel Core i7-12700K |
| LaTeX | latexmk (TeX Live; local `~/.local/bin`) |

## Python dependencies

- **Runtime:** `online_resource_1/requirements.txt`
- **Dev/test:** `online_resource_1/requirements-dev.txt`
- **Exact freeze:** `online_resource_1/environment/requirements-freeze.txt` (if present) or regenerate from `pip freeze` at submission

## External binaries

| Binary | Role | Documented |
|---|---|---|
| HiGHS | EXP8 MIP | yes (OR1 §S9) |
| DRMacIver/FAS | EXP4/EXP10 baseline | commit + SHA in provenance |
| python-igraph | graph IO | requirements |

## Policy

Maintainable minimum versions in `requirements.txt`; exact tested freeze kept separately. Machine-specific hashes not forced into install files.

## Status

**Dependencies documented**; exact freeze file should be refreshed if `environment/` snapshot is updated before upload.
