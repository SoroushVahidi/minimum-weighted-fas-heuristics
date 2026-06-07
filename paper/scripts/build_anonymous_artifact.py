#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import sys
import zipfile
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SUBMISSION_ROOT = ROOT / "submission_package"
STAGING_DIR = SUBMISSION_ROOT / "anonymous_artifact" / "staging" / "mwfas_reproducibility_artifact_anonymous"
ZIP_PATH = SUBMISSION_ROOT / "anonymous_artifact" / "mwfas_reproducibility_artifact_anonymous.zip"

VALIDATION_DIR = ROOT / "paper" / "notes" / "artifact_validation"
MANIFEST_MD = VALIDATION_DIR / "artifact_manifest.md"
MANIFEST_JSON = VALIDATION_DIR / "artifact_manifest.json"
ANONYMITY_REPORT = VALIDATION_DIR / "artifact_anonymity_report.md"
CHECKSUMS_TXT = VALIDATION_DIR / "artifact_checksums.txt"

MAX_FILE_SIZE = 20 * 1024 * 1024
ARTIFACT_ROOT_NAME = "mwfas_reproducibility_artifact_anonymous"

TEXT_EXTENSIONS = {
    ".md", ".txt", ".py", ".json", ".yaml", ".yml", ".csv", ".cfg", ".ini", ".toml",
    ".sh", ".d", ".lop", ".tex", ".rst",
}
TEXT_FILENAMES = {"README", "LICENSE", "Makefile"}
FORBIDDEN_PATH_PARTS = {
    ".git", ".github", "archive", "paper/source_material", "results", "external_tools",
    "downloads", "logs", "raw", "__pycache__", ".pytest_cache", ".ipynb_checkpoints",
    ".venv", "venv",
}
IDENTITY_TERMS = [
    "Soroush",
    "Vahidi",
    "SoroushVahidi",
    "NJIT",
    "New Jersey Institute of Technology",
    "sv96",
    "/home/soroush",
]
EMAIL_RE = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")


@dataclass
class CopiedFile:
    relative_path: str
    size: int
    sha256: str


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def ensure_clean() -> None:
    shutil.rmtree(STAGING_DIR, ignore_errors=True)
    ZIP_PATH.unlink(missing_ok=True)
    VALIDATION_DIR.mkdir(parents=True, exist_ok=True)
    STAGING_DIR.mkdir(parents=True, exist_ok=True)


def is_text_file(path: Path) -> bool:
    return path.suffix.lower() in TEXT_EXTENSIONS or path.name in TEXT_FILENAMES


def sanitize_text(text: str) -> str:
    replacements = [
        (r"/home/soroush/minimum-weighted-fas-heuristics", "[workspace root]"),
        (r"/home/soroush/benchmark_sources/graph-benchmarks/?", "[graph-benchmarks root]/"),
        (r"github\.com/SoroushVahidi/minimum-weighted-fas-heuristics", "[repository anonymized for review]"),
        (r"github\.com/SoroushVahidi/weighted-minfas-local-ratio", "[repository anonymized for review]"),
        (r"github\.com/SoroushVahidi/weighted-minfas-codes", "[repository anonymized for review]"),
        (r"SoroushVahidi", "[author removed for double-anonymized review]"),
        (r"New Jersey Institute of Technology", "[affiliation removed for double-anonymized review]"),
        (r"\bNJIT\b", "[affiliation removed for double-anonymized review]"),
        (r"\bsv96\b", "[author removed for double-anonymized review]"),
        (r"\bSoroush\b", "[author removed for double-anonymized review]"),
        (r"\bVahidi\b", "[author removed for double-anonymized review]"),
    ]
    for pattern, repl in replacements:
        text = re.sub(pattern, repl, text)
    text = EMAIL_RE.sub("[email removed for double-anonymized review]", text)
    return text


def path_forbidden(rel_path: str) -> bool:
    normalized = rel_path.replace("\\", "/")
    return any(part in normalized for part in FORBIDDEN_PATH_PARTS)


def stage_text(content: str, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(sanitize_text(content))


def stage_file(src: Path, rel_dest: str | None = None, sanitize: bool | None = None) -> None:
    if not src.exists() or not src.is_file():
        return
    rel_dest = rel_dest or src.relative_to(ROOT).as_posix()
    if path_forbidden(rel_dest):
        return
    if src.stat().st_size > MAX_FILE_SIZE:
        return
    dest = STAGING_DIR / rel_dest
    dest.parent.mkdir(parents=True, exist_ok=True)
    text_mode = is_text_file(src) if sanitize is None else sanitize
    if text_mode:
        stage_text(src.read_text(errors="ignore"), dest)
    else:
        shutil.copy2(src, dest)


def stage_tree(src_dir: Path, allow_ext: set[str] | None = None, exclude_names: set[str] | None = None) -> None:
    if not src_dir.exists():
        return
    exclude_names = exclude_names or set()
    for path in sorted(src_dir.rglob("*")):
        if path.is_dir():
            continue
        rel = path.relative_to(ROOT).as_posix()
        if any(name in path.parts for name in exclude_names):
            continue
        if path_forbidden(rel):
            continue
        if allow_ext is not None and path.suffix.lower() not in allow_ext and path.name not in TEXT_FILENAMES:
            continue
        stage_file(path)


def build_artifact_docs() -> None:
    readme = f"""# Anonymous Reproducibility Artifact

This package is an anonymous reproducibility artifact prepared for double-anonymized review.
It contains the implementation, experiment support scripts, selected committed summaries,
paper-asset builders, and documentation needed to inspect and reproduce the manuscript-facing
tables and figures without exposing author identity.

## Included

- `src/mwfas/` core implementation modules
- `scripts/` command-line wrappers for the reported methods
- selected experiment configs, postprocessors, committed summaries, and paper tables
- manuscript asset builders and provenance notes
- dataset and baseline reference notes

## Excluded

- Git history and repository metadata
- raw experiment outputs, logs, downloads, and external cloned tools
- manuscript PDFs and TeX build artifacts
- private paths, personal identifiers, and non-anonymized submission files

## Dependency setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

## Inspect committed summaries

- `experiments/combined/summary/` contains the manuscript results digest.
- `experiments/combined/tables/` contains the paper-facing CSV tables.
- experiment-specific `summary/` and `tables/` directories contain the committed supporting files.

## Regenerate manuscript result tables and figures from committed summaries

```bash
python paper/scripts/build_paper_results_assets.py
```

This command rebuilds the manuscript-facing tables and vector figures from the committed
summary files without rerunning the reported experiments.

## Optional reruns

Time-consuming reruns are documented in `REPRODUCE.md`. Full reruns are optional and may
depend on external tools, dataset access, and the local software environment.

## Public dataset and tool sources

- graph-benchmarks: https://github.com/alidasdan/graph-benchmarks
- LOLIB: https://grafo.etsii.urjc.es/optsicom/lolib.html
- python-igraph: https://python.igraph.org/
- DRMacIver/FAS: https://github.com/DRMaciver/Feedback-Arc-Set

No author-identifying information is intentionally included in this artifact.
A public repository and archival release will be provided after acceptance.
"""
    datasets = """# Datasets

## graph-benchmarks sparse directed instances

- Public source: https://github.com/alidasdan/graph-benchmarks
- Redistribution in this artifact: no
- Access mode: download separately from the public source
- Selected subset: manuscript benchmark instance lists in `experiments/*/configs/`
- Conversion note: instances are used in DIMACS directed-arc format
- Scope note: standard paper claims use the nonnegative-weight subset only
- Negative-weight exclusions: `gerez`, `howard-max`, `k3_3`, `ku`, `peterson`, `peterson1`, `peterson2`, `stg0`

## LOLIB dense ordering instances

- Public source: https://grafo.etsii.urjc.es/optsicom/lolib.html
- Redistribution in this artifact: no original archive; only the small committed smoke-test `.lop` file is included
- Access mode: download from the cited public source, then convert with `scripts/convert_lolib_to_dimacs.py`
- Selected subset: SGB, IO, and RandA1 families listed in `experiments/exp5_lolib_dense/configs/exp5_lolib_instances.txt`
- Conversion note: the manuscript uses converted DIMACS digraphs derived from dense ordering matrices
- Scope note: LOLIB is used as a dense transfer test, not the primary sparse benchmark
"""
    reproduce = """# Reproduce

## Quick checks

```bash
python -m compileall src/mwfas scripts
python experiments/combined/build_manuscript_results_digest.py
python paper/scripts/build_paper_results_assets.py
```

## Inspect the committed summary tables

- `experiments/combined/tables/`
- `experiments/exp2_ablation/summary/`
- `experiments/exp3_exact_small/summary/`
- `experiments/exp4_external_baselines/summary/`
- `experiments/exp5_lolib_dense/summary/`

## Optional reruns

The following commands are time-consuming and may require datasets or external tools that are not bundled in this artifact:

```bash
python scripts/run_lrta.py --help
python scripts/run_wmsf.py --help
python scripts/run_ipsns.py --help
python scripts/run_exact.py --help
python scripts/run_drmaciver_fas.py --help
```

Exact reproduction of runtimes or external-baseline behavior may vary by machine,
dependency versions, and availability of third-party tools.
"""
    stage_text(readme, STAGING_DIR / "README.md")
    stage_text(datasets, STAGING_DIR / "DATASETS.md")
    stage_text(reproduce, STAGING_DIR / "REPRODUCE.md")


def collect_files() -> list[CopiedFile]:
    copied = []
    for path in sorted(STAGING_DIR.rglob("*")):
        if path.is_dir():
            continue
        rel = path.relative_to(STAGING_DIR).as_posix()
        data = path.read_bytes()
        copied.append(CopiedFile(rel, len(data), sha256_bytes(data)))
    return copied


def write_manifest(copied: list[CopiedFile]) -> None:
    top_level = sorted({item.relative_path.split("/", 1)[0] for item in copied})
    manifest_obj = {
        "artifact_root": ARTIFACT_ROOT_NAME,
        "file_count": len(copied),
        "top_level_contents": top_level,
        "files": [item.__dict__ for item in copied],
    }
    MANIFEST_JSON.write_text(json.dumps(manifest_obj, indent=2) + "\n")

    lines = [
        "# Artifact Manifest",
        "",
        f"- Artifact root: `{ARTIFACT_ROOT_NAME}`",
        f"- File count: {len(copied)}",
        "",
        "## Top-level contents",
        "",
    ]
    for name in top_level:
        lines.append(f"- `{name}`")
    lines += ["", "## Files", ""]
    for item in copied:
        lines.append(f"- `{item.relative_path}` — {item.size} bytes — `{item.sha256}`")
    MANIFEST_MD.write_text("\n".join(lines) + "\n")

    stage_text(
        "\n".join([
            "# Manifest",
            "",
            f"- File count: {len(copied)}",
            "",
            "## Top-level contents",
            *[f"- `{name}`" for name in top_level],
            "",
            "## File list",
            *[f"- `{item.relative_path}`" for item in copied],
        ]),
        STAGING_DIR / "MANIFEST.md",
    )


def build_zip() -> None:
    ZIP_PATH.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(ZIP_PATH, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(STAGING_DIR.rglob("*")):
            if path.is_dir():
                continue
            arcname = f"{ARTIFACT_ROOT_NAME}/{path.relative_to(STAGING_DIR).as_posix()}"
            zf.write(path, arcname=arcname)


def validate_zip() -> tuple[bool, list[str], list[str], int]:
    forbidden_hits: list[str] = []
    identity_hits: list[str] = []
    file_count = 0
    with zipfile.ZipFile(ZIP_PATH) as zf:
        for name in zf.namelist():
            if name.endswith("/"):
                continue
            file_count += 1
            logical = name.split("/", 1)[1] if "/" in name else name
            if path_forbidden(logical):
                forbidden_hits.append(logical)
            ext = Path(logical).suffix.lower()
            if ext in TEXT_EXTENSIONS or Path(logical).name in TEXT_FILENAMES:
                try:
                    text = zf.read(name).decode("utf-8", errors="ignore")
                except Exception:
                    continue
                for term in IDENTITY_TERMS:
                    if term.lower() in text.lower():
                        identity_hits.append(f"{logical}: {term}")
                for email in sorted(set(EMAIL_RE.findall(text))):
                    identity_hits.append(f"{logical}: {email}")
    zip_sha = sha256_file(ZIP_PATH)
    size_bytes = ZIP_PATH.stat().st_size
    CHECKSUMS_TXT.write_text(
        f"sha256  {zip_sha}  {ZIP_PATH.relative_to(ROOT).as_posix()}\n"
        f"size_bytes  {size_bytes}\n"
        f"file_count  {file_count}\n"
    )
    report = [
        "# Artifact Anonymity Report",
        "",
        f"- Zip path: `{ZIP_PATH.relative_to(ROOT).as_posix()}`",
        f"- Zip size: {size_bytes} bytes",
        f"- Zip SHA256: `{zip_sha}`",
        f"- File count: {file_count}",
        "",
        "## Forbidden path scan",
        "",
    ]
    if forbidden_hits:
        report.extend(f"- `{hit}`" for hit in forbidden_hits)
    else:
        report.append("- No forbidden paths detected.")
    report += ["", "## Identity leak scan", ""]
    if identity_hits:
        report.extend(f"- `{hit}`" for hit in identity_hits)
    else:
        report.append("- No identity leaks detected.")
    ANONYMITY_REPORT.write_text("\n".join(report) + "\n")
    ok = not forbidden_hits and not identity_hits
    return ok, forbidden_hits, identity_hits, file_count


def populate_staging() -> None:
    # Core code and wrappers.
    stage_tree(ROOT / "src" / "mwfas")
    stage_tree(ROOT / "scripts", allow_ext={".py", ".sh", ".md", ".txt"})

    # Project metadata.
    for filename in ["requirements.txt", "setup.py", "LICENSE"]:
        stage_file(ROOT / filename)
    if (ROOT / "README.md").exists():
        stage_file(ROOT / "README.md", rel_dest="PROJECT_README.md", sanitize=True)

    # Experiment overview.
    stage_file(ROOT / "experiments" / "README.md")

    def include_experiment(exp_name: str, include_top_level: tuple[str, ...] = ()) -> None:
        exp = ROOT / "experiments" / exp_name
        if not exp.exists():
            return
        for name in include_top_level:
            stage_file(exp / name)
        for sub in ["configs", "summary", "tables"]:
            subdir = exp / sub
            if not subdir.exists():
                continue
            for path in sorted(subdir.rglob("*")):
                if path.is_dir():
                    continue
                if path.name == "pip_freeze.txt":
                    continue
                if sub == "configs" and path.suffix.lower() not in {".txt", ".yaml", ".yml", ".lop", ".md"}:
                    continue
                if sub in {"summary", "tables"} and path.suffix.lower() not in {".csv", ".json", ".md"}:
                    continue
                stage_file(path)

    include_experiment("combined", include_top_level=("build_manuscript_results_digest.py",))
    include_experiment("exp2_ablation", include_top_level=("README.md", "run_exp2_ablation_tmux.sh"))
    include_experiment("exp3_exact_small", include_top_level=("run_exp3_exact_tmux.sh",))
    include_experiment("exp4_external_baselines", include_top_level=("baseline_registry.md", "run_exp4_benchmark.py", "run_exp4_external_baselines_tmux.sh", "run_exp4_smoke.sh", "postprocess_exp4_external.py"))
    include_experiment("exp5_lolib_dense", include_top_level=("README.md", "run_exp5_lolib_benchmark.py", "run_exp5_lolib_tmux.sh", "postprocess_exp5_lolib.py"))
    include_experiment("exp1b_core_benchmark_full_wmsf_seed", include_top_level=("postprocess_exp1b.py",))

    # Include one tiny committed LOLIB smoke-test input only.
    stage_file(ROOT / "experiments" / "exp5_lolib_dense" / "configs" / "tiny_lolib_test.lop")

    # Supporting docs and provenance.
    stage_file(ROOT / "docs" / "baselines_and_datasets_references.md")
    stage_file(ROOT / "docs" / "manuscript_results_and_claims_20260606.md")
    stage_file(ROOT / "paper" / "notes" / "results_asset_provenance.md")
    stage_file(ROOT / "paper" / "notes" / "results_asset_provenance.json")
    stage_file(ROOT / "paper" / "scripts" / "build_paper_results_assets.py")

    build_artifact_docs()


def main() -> int:
    ensure_clean()
    populate_staging()
    copied = collect_files()
    write_manifest(copied)
    copied = collect_files()
    write_manifest(copied)
    build_zip()
    ok, forbidden_hits, identity_hits, _ = validate_zip()
    if not ok:
        print("Artifact validation failed.", file=sys.stderr)
        print("Forbidden hits:", forbidden_hits, file=sys.stderr)
        print("Identity hits:", identity_hits, file=sys.stderr)
        return 1
    print(f"Built {ZIP_PATH.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
