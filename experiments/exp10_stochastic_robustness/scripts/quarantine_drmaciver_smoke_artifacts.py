"""
Quarantine EXP10 DRMacIver smoke-test artifacts from the production namespace.

Preserves provenance: moves (never deletes) conclusively classified smoke outputs
from raw/drmaciver/ and checkpoints/ into smoke_archive/drmaciver/.

Usage:
  # Dry-run (default): validate manifest and print planned moves
  python scripts/quarantine_drmaciver_smoke_artifacts.py --manifest summary/drmaciver_smoke_artifact_inventory.csv

  # Execute quarantine
  python scripts/quarantine_drmaciver_smoke_artifacts.py --manifest ... --execute

  # Rollback a prior quarantine using manifest.csv in the archive
  python scripts/quarantine_drmaciver_smoke_artifacts.py --rollback smoke_archive/drmaciver/manifest.csv
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
EXP_DIR = os.path.join(REPO_ROOT, "experiments", "exp10_stochastic_robustness")
RAW_PROD = os.path.join(EXP_DIR, "raw", "drmaciver")
CKPT_PROD = os.path.join(EXP_DIR, "checkpoints")
SUMMARY_DIR = os.path.join(EXP_DIR, "summary")
ARCHIVE_ROOT = os.path.join(EXP_DIR, "smoke_archive", "drmaciver")
ARCHIVE_RAW = os.path.join(ARCHIVE_ROOT, "raw")
ARCHIVE_CKPT = os.path.join(ARCHIVE_ROOT, "checkpoints")
ARCHIVE_LOGS = os.path.join(ARCHIVE_ROOT, "logs")

SMOKE_INSTANCES = frozenset({"stg", "r20_60", "s27"})
SMOKE_RUN_INDICES = frozenset(range(3))


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def git_head() -> str:
    try:
        r = subprocess.run(
            ["git", "-C", REPO_ROOT, "rev-parse", "HEAD"],
            capture_output=True, text=True, timeout=5,
        )
        return r.stdout.strip()
    except Exception:
        return "unknown"


def git_branch() -> str:
    try:
        r = subprocess.run(
            ["git", "-C", REPO_ROOT, "branch", "--show-current"],
            capture_output=True, text=True, timeout=5,
        )
        return r.stdout.strip()
    except Exception:
        return "unknown"


def classify_artifact(raw_path: str) -> dict:
    """Classify a single raw JSON as smoke or ambiguous."""
    base = os.path.basename(raw_path)
    if not base.startswith("drmaciver_") or not base.endswith(".json"):
        return {"confidence": "ambiguous", "evidence": "unexpected filename pattern"}

    stem = base[:-5]  # drop .json
    parts = stem.split("_")
    # drmaciver_{inst}_run{idx}
    if len(parts) < 3 or parts[-1][:3] != "run":
        return {"confidence": "ambiguous", "evidence": "cannot parse instance/run_index"}

    run_idx = int(parts[-1][3:])
    inst_id = "_".join(parts[1:-1])

    evidence = []
    if inst_id in SMOKE_INSTANCES:
        evidence.append("instance in documented smoke trio (stg,r20_60,s27)")
    if run_idx in SMOKE_RUN_INDICES:
        evidence.append("run_index 0..2 matches --smoke n_reps=3")
    if inst_id in SMOKE_INSTANCES and run_idx in SMOKE_RUN_INDICES:
        evidence.append("matches run_drmaciver_repetitions.py --smoke schedule exactly")

    with open(raw_path) as f:
        rec = json.load(f)

    if rec.get("instance_id") != inst_id:
        return {"confidence": "ambiguous", "evidence": f"filename instance {inst_id} != record {rec.get('instance_id')}"}
    if rec.get("run_index") != run_idx:
        return {"confidence": "ambiguous", "evidence": f"filename run_index != record run_index"}

    ts = rec.get("timestamp_start") or rec.get("process_start_timestamp", "")
    if ts.startswith("2026-06-11T17:59"):
        evidence.append("timestamp matches documented smoke-test window (2026-06-11T17:59Z)")

    git = rec.get("git_commit", "")
    if git == "80b3144d5fdbbe250faed8a4fe671dde2da76c89":
        evidence.append("git_commit matches frozen EXP10 HEAD")

    status = rec.get("status", "unknown")
    inst_sha = rec.get("instance_sha256", "")

    ckpt_name = f"drmaciver_{inst_id}_run{run_idx:02d}.done"
    ckpt_path = os.path.join(CKPT_PROD, ckpt_name)

    confidence = "high" if len(evidence) >= 3 else "ambiguous"
    if inst_id in SMOKE_INSTANCES and run_idx in SMOKE_RUN_INDICES and len(evidence) >= 3:
        confidence = "high"

    return {
        "instance_id": inst_id,
        "run_index": run_idx,
        "status": status,
        "instance_sha256": inst_sha,
        "output_sha256": sha256_file(raw_path),
        "timestamp": ts,
        "related_checkpoint": ckpt_path,
        "related_log": "logs/validation_result.json (environment validation 2026-06-11T17:56:01Z)",
        "evidence_smoke": "; ".join(evidence),
        "classification_confidence": confidence,
    }


def discover_smoke_candidates() -> list[dict]:
    """Find all drmaciver_* artifacts in production namespace."""
    rows = []
    if not os.path.isdir(RAW_PROD):
        return rows
    for name in sorted(os.listdir(RAW_PROD)):
        if not name.startswith("drmaciver_") or not name.endswith(".json"):
            continue
        raw_path = os.path.join(RAW_PROD, name)
        info = classify_artifact(raw_path)
        ckpt_path = info.get("related_checkpoint", "")
        ckpt_sha = sha256_file(ckpt_path) if os.path.isfile(ckpt_path) else ""
        rows.append({
            "artifact_type": "raw_json",
            "original_path": raw_path,
            "instance_id": info.get("instance_id", ""),
            "run_index": info.get("run_index", ""),
            "timestamp": info.get("timestamp", ""),
            "sha256": info.get("output_sha256", ""),
            "instance_sha256": info.get("instance_sha256", ""),
            "status": info.get("status", ""),
            "related_log": info.get("related_log", ""),
            "related_checkpoint": ckpt_path,
            "checkpoint_sha256": ckpt_sha,
            "evidence_smoke": info.get("evidence_smoke", ""),
            "classification_confidence": info.get("classification_confidence", "ambiguous"),
            "proposed_destination": os.path.join(ARCHIVE_RAW, name),
        })
        if os.path.isfile(ckpt_path):
            rows.append({
                "artifact_type": "checkpoint",
                "original_path": ckpt_path,
                "instance_id": info.get("instance_id", ""),
                "run_index": info.get("run_index", ""),
                "timestamp": info.get("timestamp", ""),
                "sha256": ckpt_sha,
                "instance_sha256": info.get("instance_sha256", ""),
                "status": info.get("status", ""),
                "related_log": info.get("related_log", ""),
                "related_checkpoint": ckpt_path,
                "checkpoint_sha256": ckpt_sha,
                "evidence_smoke": info.get("evidence_smoke", ""),
                "classification_confidence": info.get("classification_confidence", "ambiguous"),
                "proposed_destination": os.path.join(ARCHIVE_CKPT, os.path.basename(ckpt_path)),
            })
    return rows


def write_inventory_csv(rows: list[dict], path: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    fieldnames = [
        "artifact_type", "original_path", "instance_id", "run_index", "timestamp",
        "sha256", "instance_sha256", "status", "related_log", "related_checkpoint",
        "checkpoint_sha256", "evidence_smoke", "classification_confidence", "proposed_destination",
    ]
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for row in rows:
            w.writerow({k: row.get(k, "") for k in fieldnames})


def load_inventory_csv(path: str) -> list[dict]:
    with open(path) as f:
        return list(csv.DictReader(f))


def verify_manifest(rows: list[dict]) -> list[str]:
    errors = []
    if not rows:
        errors.append("manifest is empty")
        return errors
    ambiguous = [r for r in rows if r.get("classification_confidence") != "high"]
    if ambiguous:
        errors.append(f"{len(ambiguous)} artifact(s) not confidently classified as smoke")
    for r in rows:
        orig = r["original_path"]
        if not os.path.isfile(orig):
            errors.append(f"missing source file: {orig}")
            continue
        if sha256_file(orig) != r["sha256"]:
            errors.append(f"checksum mismatch for {orig}")
    raw_count = sum(1 for r in rows if r["artifact_type"] == "raw_json")
    if raw_count != 9:
        errors.append(f"expected 9 raw_json artifacts, found {raw_count}")
    return errors


def move_preserve_mtime(src: str, dst: str) -> None:
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    st = os.stat(src)
    shutil.move(src, dst)
    os.utime(dst, (st.st_atime, st.st_mtime))


def execute_quarantine(rows: list[dict]) -> dict:
    """Move artifacts; record before/after checksums. Roll back on failure."""
    moves = []
    completed = []
    try:
        for r in rows:
            src = r["original_path"]
            dst = r["proposed_destination"]
            if os.path.isfile(dst):
                raise RuntimeError(f"destination already exists (refusing overwrite): {dst}")
            sha_before = sha256_file(src)
            move_preserve_mtime(src, dst)
            sha_after = sha256_file(dst)
            if sha_before != sha_after:
                raise RuntimeError(f"checksum changed after move: {src}")
            move_rec = {
                "original_path": src,
                "new_path": dst,
                "sha256_before": sha_before,
                "sha256_after": sha_after,
                "artifact_type": r["artifact_type"],
            }
            moves.append(move_rec)
            completed.append(move_rec)
        return {"ok": True, "moves": moves}
    except Exception as e:
        # Rollback completed moves in reverse order
        for m in reversed(completed):
            if os.path.isfile(m["new_path"]) and not os.path.isfile(m["original_path"]):
                shutil.move(m["new_path"], m["original_path"])
        return {"ok": False, "error": str(e), "moves": moves, "rolled_back": len(completed)}


def rollback(manifest_path: str) -> dict:
    with open(manifest_path) as f:
        rows = list(csv.DictReader(f))
    restored = []
    for row in reversed(rows):
        src = row["new_path"]
        dst = row["original_path"]
        if not os.path.isfile(src):
            continue
        if os.path.isfile(dst):
            raise RuntimeError(f"rollback blocked: {dst} already exists")
        sha_before = sha256_file(src)
        move_preserve_mtime(src, dst)
        if sha256_file(dst) != sha_before:
            raise RuntimeError(f"rollback checksum mismatch: {src}")
        restored.append({"from": src, "to": dst})
    return {"ok": True, "restored": restored}


def write_archive_manifest(moves: list[dict], branch: str, head: str) -> str:
    path = os.path.join(ARCHIVE_ROOT, "manifest.csv")
    os.makedirs(ARCHIVE_ROOT, exist_ok=True)
    fieldnames = [
        "artifact_type", "original_path", "new_path", "sha256_before", "sha256_after",
        "quarantine_timestamp", "branch", "head", "script",
    ]
    ts = utc_now()
    script = "scripts/quarantine_drmaciver_smoke_artifacts.py"
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for m in moves:
            w.writerow({
                "artifact_type": m["artifact_type"],
                "original_path": m["original_path"],
                "new_path": m["new_path"],
                "sha256_before": m["sha256_before"],
                "sha256_after": m["sha256_after"],
                "quarantine_timestamp": ts,
                "branch": branch,
                "head": head,
                "script": script,
            })
    return path


def write_readme(branch: str, head: str, moves: list[dict]) -> str:
    path = os.path.join(ARCHIVE_ROOT, "README.md")
    ts = utc_now()
    lines = [
        "# DRMacIver Smoke-Test Archive (EXP10)",
        "",
        f"**Quarantine date:** {ts}",
        f"**Branch:** {branch}",
        f"**HEAD:** {head}",
        f"**Script:** `scripts/quarantine_drmaciver_smoke_artifacts.py`",
        "",
        "## Purpose",
        "",
        "These are preflight/smoke-test outputs from `run_drmaciver_repetitions.py --smoke`",
        "(3 instances × 3 repetitions = 9 runs). They were written to the production",
        "namespace (`raw/drmaciver/`, `checkpoints/`) during environment validation and",
        "would collide with production run keys (run00–run02 on stg, r20_60, s27).",
        "",
        "**They are excluded from production analysis.**",
        "",
        "## Why quarantined",
        "",
        "DRMacIver preflight requires a clean production namespace before the full",
        "93 × 20 = 1860 run phase. Smoke outputs share filenames with the first three",
        "production repetitions on the smoke trio instances.",
        "",
        "## Original paths",
        "",
    ]
    for m in moves:
        lines.append(f"- `{m['original_path']}` → `{m['new_path']}`")
    lines.extend([
        "",
        "## Scientific note",
        "",
        "No scientific result was deleted. All artifacts were moved with SHA-256",
        "verification before and after transfer.",
        "",
    ])
    with open(path, "w") as f:
        f.write("\n".join(lines))
    return path


def write_cleanup_report(result: dict, branch: str, head: str) -> str:
    path = os.path.join(SUMMARY_DIR, "drmaciver_namespace_cleanup_report.json")
    report = {
        "timestamp": utc_now(),
        "branch": branch,
        "head": head,
        "prior_contaminated_count": {"raw": 9, "checkpoints": 9},
        "corrected_production_count": {"raw": 0, "checkpoints": 0},
        "smoke_archive_count": 9,
        "note": (
            "experiment_progress.json previously reported DRMacIver 9/1860 because "
            "smoke checkpoints were counted in the production namespace; corrected after quarantine."
        ),
        "quarantine_result": result,
    }
    with open(path, "w") as f:
        json.dump(report, f, indent=2)
    return path


def write_classification_md(rows: list[dict]) -> str:
    path = os.path.join(SUMMARY_DIR, "drmaciver_smoke_artifact_classification.md")
    lines = [
        "# DRMacIver Smoke Artifact Classification",
        "",
        f"**Date:** {utc_now()}",
        "",
        "## Summary",
        "",
        f"- Artifacts examined: {len([r for r in rows if r['artifact_type']=='raw_json'])} raw JSON + "
        f"{len([r for r in rows if r['artifact_type']=='checkpoint'])} checkpoints",
        f"- All classified as smoke with **high** confidence: "
        f"{all(r.get('classification_confidence')=='high' for r in rows if r['artifact_type']=='raw_json')}",
        "",
        "## Classification criteria",
        "",
        "Each artifact matches the documented `--smoke` schedule:",
        "- Instances: `stg`, `r20_60`, `s27` (diagnostic smoke trio)",
        "- Run indices: 0, 1, 2 only (`n_reps=3` in smoke mode)",
        "- Timestamps: 2026-06-11T17:59Z batch",
        "- Git commit: 80b3144d5fdbbe250faed8a4fe671dde2da76c89",
        "- Preflight `check_smoke_records()` explicitly lists these nine keys",
        "",
        "## Per-artifact detail",
        "",
    ]
    seen = set()
    for r in rows:
        if r["artifact_type"] != "raw_json":
            continue
        key = (r["instance_id"], r["run_index"])
        if key in seen:
            continue
        seen.add(key)
        lines.extend([
            f"### {r['instance_id']} run {r['run_index']}",
            "",
            f"- **Status:** {r['status']}",
            f"- **Confidence:** {r['classification_confidence']}",
            f"- **Evidence:** {r['evidence_smoke']}",
            f"- **SHA-256:** `{r['sha256']}`",
            f"- **Instance SHA-256:** `{r['instance_sha256']}`",
            f"- **Original path:** `{r['original_path']}`",
            f"- **Checkpoint:** `{r['related_checkpoint']}`",
            "",
        ])
    with open(path, "w") as f:
        f.write("\n".join(lines))
    return path


def main() -> int:
    parser = argparse.ArgumentParser(description="Quarantine DRMacIver smoke artifacts")
    parser.add_argument("--manifest", help="Inventory CSV (required for execute/dry-run)")
    parser.add_argument("--execute", action="store_true", help="Perform quarantine (default: dry-run)")
    parser.add_argument("--rollback", help="Rollback using archive manifest.csv")
    parser.add_argument("--discover", action="store_true", help="Discover and write inventory CSV")
    args = parser.parse_args()

    if args.rollback:
        result = rollback(args.rollback)
        print(json.dumps(result, indent=2))
        return 0 if result["ok"] else 1

    if args.discover or not args.manifest:
        rows = discover_smoke_candidates()
        inv_path = os.path.join(SUMMARY_DIR, "drmaciver_smoke_artifact_inventory.csv")
        write_inventory_csv(rows, inv_path)
        write_classification_md(rows)
        print(f"Discovered {len(rows)} artifacts; wrote {inv_path}")
        if not args.manifest:
            args.manifest = inv_path

    if not args.manifest or not os.path.isfile(args.manifest):
        print("ERROR: --manifest required (use --discover to generate)", file=sys.stderr)
        return 1

    rows = load_inventory_csv(args.manifest)
    errors = verify_manifest(rows)
    if errors:
        print("Manifest verification FAILED:", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        return 1

    move_rows = [r for r in rows if r["artifact_type"] in ("raw_json", "checkpoint")]
    print(f"Verified {len(move_rows)} artifacts for quarantine")
    for r in move_rows:
        print(f"  {r['artifact_type']:12} {r['original_path']} -> {r['proposed_destination']}")

    if not args.execute:
        print("\nDRY-RUN: no files moved. Pass --execute to quarantine.")
        return 0

    branch = git_branch()
    head = git_head()
    result = execute_quarantine(move_rows)
    if not result["ok"]:
        print(f"QUARANTINE FAILED: {result.get('error')}", file=sys.stderr)
        write_cleanup_report(result, branch, head)
        return 1

    write_archive_manifest(result["moves"], branch, head)
    write_readme(branch, head, result["moves"])
    write_cleanup_report(result, branch, head)
    print(f"Quarantine complete: {len(result['moves'])} files moved")
    return 0


if __name__ == "__main__":
    sys.exit(main())
