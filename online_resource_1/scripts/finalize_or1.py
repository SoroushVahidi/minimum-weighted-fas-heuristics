#!/usr/bin/env python3
"""Rebuild and freeze Online Resource 1 from repository root."""
from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
OR1 = Path(__file__).resolve().parents[1]
AUD = REPO / "docs" / "coap_online_resource_finalization_20260611"
SKIP_DIRS = {".pytest_cache", "__pycache__", ".git", ".coverage"}
SKIP_SUFFIX = {".pyc", ".pyo"}


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def git_head() -> str:
    return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO, text=True).strip()


def sync_tree(src: Path, dst: Path, patterns: tuple[str, ...]):
    if dst.exists():
        shutil.rmtree(dst)
    dst.parent.mkdir(parents=True, exist_ok=True)

    def ignore(d, names):
        return [n for n in names if n in SKIP_DIRS or n.endswith(".pyc")]

    shutil.copytree(src, dst, ignore=ignore)


def clean_or1():
    for p in OR1.rglob("*"):
        if any(part in SKIP_DIRS for part in p.parts):
            if p.is_dir():
                shutil.rmtree(p, ignore_errors=True)
            elif p.exists():
                p.unlink(missing_ok=True)
        elif p.suffix in SKIP_SUFFIX:
            p.unlink(missing_ok=True)


def sync_code_tests():
    sync_tree(REPO / "src" / "mwfas", OR1 / "src" / "mwfas", ())
    sync_tree(REPO / "tests", OR1 / "tests", ())
    # EXP10 namespace tests require live production checkpoints; summaries suffice in OR1.
    exp10_tree = OR1 / "experiments" / "exp10_stochastic_robustness"
    if exp10_tree.exists():
        shutil.rmtree(exp10_tree)
    infra = OR1 / "tests" / "regression" / "test_experiment_infrastructure.py"
    if infra.exists():
        infra.unlink()
    for name in ("pytest.ini", "requirements.txt", "requirements-dev.txt"):
        shutil.copy2(REPO / name, OR1 / name)


def sync_exp11():
    dst = OR1 / "results" / "exp11"
    src = REPO / "experiments" / "exp11_topological_extraction_sensitivity"
    if not src.exists():
        return
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(
        src,
        dst,
        ignore=lambda d, n: [x for x in n if x in SKIP_DIRS or x == "logs"],
    )


def sync_exp10_summaries():
    """Ensure results/exp10 has latest summaries from production experiment."""
    prod = REPO / "experiments" / "exp10_stochastic_robustness" / "summary"
    dst = OR1 / "results" / "exp10" / "summary"
    if not prod.exists():
        return
    dst.mkdir(parents=True, exist_ok=True)
    for pat in ("*.json", "*.csv", "COMPLETED.ok"):
        for f in prod.glob(pat):
            shutil.copy2(f, dst / f.name)
    # Internal preflight notes may contain machine-local paths; omit from publication bundle.
    (dst / "drmaciver_preflight_report.md").unlink(missing_ok=True)
    # tables and figures if present
    for sub, dsub in (("tables", "tables"), ("figures", "figures")):
        ps, pd = prod.parent / sub, OR1 / "results" / "exp10" / dsub
        if ps.exists():
            pd.mkdir(parents=True, exist_ok=True)
            for f in ps.glob("*"):
                if f.is_file():
                    shutil.copy2(f, pd / f.name)


def prune_non_public_results():
  """Remove internal sensitivity/holdout trees not needed for publication."""
  for rel in (
      "results/coap_ipsns_sensitivity",
      "results/coap_ipsns_holdout",
  ):
      p = OR1 / rel
      if p.exists():
          shutil.rmtree(p)


def sanitize_absolute_paths():
    repo_prefix = re.compile(r"/home/soroush/minimum-weighted-fas-heuristics/")
    bench_prefix = re.compile(r"/home/soroush/benchmark_sources/")
    for p in OR1.rglob("*"):
        if not p.is_file():
            continue
        if p.suffix not in {".csv", ".json", ".md", ".txt", ".tex", ".sh", ".py"}:
            continue
        if p.name == "MANIFEST.sha256" or p.name == "finalize_or1.py":
            continue
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        if "/home/soroush" not in text:
            continue
        new = bench_prefix.sub("benchmark_sources/", text)
        new = repo_prefix.sub("", new)
        if new != text:
            p.write_text(new, encoding="utf-8")


def write_manifest():
    lines = []
    for p in sorted(OR1.rglob("*")):
        if not p.is_file():
            continue
        if any(part in SKIP_DIRS for part in p.parts):
            continue
        if p.name == "MANIFEST.sha256":
            continue
        rel = p.relative_to(OR1).as_posix()
        lines.append(f"{sha256_file(p)}  {rel}\n")
    (OR1 / "MANIFEST.sha256").write_text("".join(lines))


def update_source_commit():
    (OR1 / "provenance" / "source_commit.txt").write_text(
        f"branch=main\ncommit={git_head()}\nfrozen_at={datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}\n"
    )


def main():
    AUD.mkdir(parents=True, exist_ok=True)
    stale_zip = REPO / "Vahidi_Online_Resource_1_MWFAS.zip"
    if stale_zip.exists():
        backup = AUD / f"Vahidi_Online_Resource_1_MWFAS_stale_{datetime.now(timezone.utc).strftime('%Y%m%d')}.zip"
        shutil.copy2(stale_zip, backup)
        print(f"Backed up stale ZIP to {backup}")

    clean_or1()
    sync_code_tests()
    sync_exp11()
    sync_exp10_summaries()
    prune_non_public_results()
    sanitize_absolute_paths()
    update_source_commit()
    write_manifest()
    print("OR1 sync complete.")


if __name__ == "__main__":
    main()
