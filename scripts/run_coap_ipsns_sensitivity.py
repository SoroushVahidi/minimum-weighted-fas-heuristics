#!/usr/bin/env python3
"""
COAP IPSNS parameter sensitivity driver with per-run checkpointing and --resume.

Each completed run is written immediately to:
  - checkpoints/runs/<run_key>.json
  - results/runs.jsonl (append, flushed)

Failed runs go to:
  - results/failures.jsonl (append, flushed)

On successful completion of all required runs:
  - results/summary.json
  - logs/coap_ipsns_sensitivity/COMPLETED.ok  (via --completion-marker-dir)
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import multiprocessing as mp
import os
import sys
import time
import traceback
from copy import deepcopy
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "src"))

from mwfas.evaluation import compute_forward_backward  # noqa: E402
from mwfas.ipsns import lns_merge_wmsf_lr_best_incumbent  # noqa: E402

DEFAULT_PLAN = REPO_ROOT / "experiments/coap_ipsns_sensitivity/config/sensitivity_plan.yaml"
DEFAULT_COMPLETION_DIR = REPO_ROOT / "logs/coap_ipsns_sensitivity"

REQUIRED_RESULT_FIELDS = (
    "run_key",
    "instance",
    "status",
    "backward_weight",
    "runtime",
    "iters",
    "topk_scc",
    "destroy_addback_frac",
    "destroy_remove_frac",
    "tol",
    "rng_seed",
)


@dataclass(frozen=True)
class RunConfig:
    instance: str
    file_path: str
    iters: int
    topk_scc: int
    destroy_addback_frac: float
    destroy_remove_frac: float
    tol: float
    rng_seed: int
    wmsf_seed_mode: str
    seed_ordering: str
    scc_select_mode: str
    varied_param: str

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)

    def run_key(self) -> str:
        payload = (
            f"{self.instance}|{self.iters}|{self.topk_scc}|"
            f"{self.destroy_addback_frac:.6g}|{self.destroy_remove_frac:.6g}|"
            f"{self.tol:.6g}|{self.rng_seed}|{self.wmsf_seed_mode}|"
            f"{self.seed_ordering}|{self.scc_select_mode}"
        )
        digest = hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16]
        return f"{self.instance}__{digest}"


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_plan(plan_path: Path) -> dict[str, Any]:
    with open(plan_path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_instances(plan: dict[str, Any]) -> list[dict[str, str]]:
    inst_path = REPO_ROOT / plan["instance_list"]
    with open(inst_path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    missing = [r["instance"] for r in rows if not Path(r["file_path"]).exists()]
    if missing:
        raise FileNotFoundError(
            "Missing instance files: " + ", ".join(missing)
        )
    return rows


def build_oat_configs(plan: dict[str, Any], instances: list[dict[str, str]]) -> list[RunConfig]:
    baseline = plan["baseline"]
    variations = plan.get("oat_variations", {})
    configs: list[RunConfig] = []

    def make(instance_row: dict[str, str], overrides: dict[str, Any], varied_param: str) -> RunConfig:
        cfg = {**baseline, **overrides}
        return RunConfig(
            instance=instance_row["instance"],
            file_path=instance_row["file_path"],
            iters=int(cfg["iters"]),
            topk_scc=int(cfg["topk_scc"]),
            destroy_addback_frac=float(cfg["destroy_addback_frac"]),
            destroy_remove_frac=float(cfg["destroy_remove_frac"]),
            tol=float(cfg["tol"]),
            rng_seed=int(cfg["rng_seed"]),
            wmsf_seed_mode=str(cfg["wmsf_seed_mode"]),
            seed_ordering=str(cfg["seed_ordering"]),
            scc_select_mode=str(cfg["scc_select_mode"]),
            varied_param=varied_param,
        )

    for inst in instances:
        configs.append(make(inst, {}, "baseline"))
        for param, values in variations.items():
            for value in values:
                configs.append(make(inst, {param: value}, param))

    # Stable ordering for reproducible scheduling
    configs.sort(key=lambda c: (c.instance, c.varied_param, c.run_key()))
    return configs


def checkpoint_path(checkpoints_dir: Path, run_key: str) -> Path:
    return checkpoints_dir / f"{run_key}.json"


def is_valid_checkpoint(path: Path) -> bool:
    if not path.is_file():
        return False
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return False
    if data.get("status") != "ok":
        return False
    return all(field in data for field in REQUIRED_RESULT_FIELDS)


def append_jsonl(path: Path, record: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, sort_keys=True) + "\n")
        f.flush()
        os.fsync(f.fileno())


def execute_run(cfg: RunConfig, checkpoints_dir: Path, tmp_dir: Path) -> dict[str, Any]:
    run_key = cfg.run_key()
    ckpt = checkpoint_path(checkpoints_dir, run_key)
    started = utc_now()
    t0 = time.perf_counter()
    tmp_out = tmp_dir / f"{run_key}.csv"
    tmp_out.parent.mkdir(parents=True, exist_ok=True)

    try:
        result = lns_merge_wmsf_lr_best_incumbent(
            dimacs_path=cfg.file_path,
            output_ranking_csv_path=str(tmp_out),
            seed_ordering=cfg.seed_ordering,
            iters=cfg.iters,
            topK_scc=cfg.topk_scc,
            destroy_addback_frac=cfg.destroy_addback_frac,
            destroy_remove_frac=cfg.destroy_remove_frac,
            tol=cfg.tol,
            rng_seed=cfg.rng_seed,
            log_every=0,
            wmsf_seed_mode=cfg.wmsf_seed_mode,
            scc_select_mode=cfg.scc_select_mode,
            return_info=False,
        )
        edges_indexed, node_to_index, _index_to_node, scores, _F = result[:5]
        total_w, fw, bw = compute_forward_backward(edges_indexed, scores)
        runtime = time.perf_counter() - t0
        record = {
            **cfg.as_dict(),
            "run_key": run_key,
            "status": "ok",
            "started_at": started,
            "finished_at": utc_now(),
            "n": len(node_to_index),
            "m": len(edges_indexed),
            "total_weight": round(float(total_w), 6),
            "forward_weight": round(float(fw), 6),
            "backward_weight": round(float(bw), 6),
            "forward_ratio": round(float(fw / total_w), 8) if total_w > 0 else 1.0,
            "runtime": round(runtime, 6),
            "error": "",
        }
        ckpt.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        return record
    except Exception as exc:
        runtime = time.perf_counter() - t0
        record = {
            **cfg.as_dict(),
            "run_key": run_key,
            "status": "error",
            "started_at": started,
            "finished_at": utc_now(),
            "runtime": round(runtime, 6),
            "error": f"{type(exc).__name__}: {exc}",
            "traceback": traceback.format_exc(),
        }
        fail_ckpt = checkpoints_dir / f"{run_key}.FAILED.json"
        fail_ckpt.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        return record


def _worker(args: tuple[RunConfig, str, str]) -> dict[str, Any]:
    cfg, checkpoints_dir_str, tmp_dir_str = args
    return execute_run(cfg, Path(checkpoints_dir_str), Path(tmp_dir_str))


def write_manifest(path: Path, configs: list[RunConfig], plan_path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    manifest = {
        "generated_at": utc_now(),
        "plan_path": str(plan_path),
        "n_configurations": len({c.run_key() for c in configs}),
        "n_instances": len({c.instance for c in configs}),
        "n_runs": len(configs),
        "configs": [c.as_dict() | {"run_key": c.run_key()} for c in configs],
    }
    path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def validate_completion(
    configs: list[RunConfig], checkpoints_dir: Path
) -> tuple[list[str], list[str], list[str]]:
    expected = [c.run_key() for c in configs]
    completed: list[str] = []
    missing: list[str] = []
    failed: list[str] = []
    for cfg in configs:
        key = cfg.run_key()
        ckpt = checkpoint_path(checkpoints_dir, key)
        fail = checkpoints_dir / f"{key}.FAILED.json"
        if is_valid_checkpoint(ckpt):
            completed.append(key)
        elif fail.is_file():
            failed.append(key)
        else:
            missing.append(key)
    return completed, missing, failed


def maybe_write_completion_marker(
    completion_dir: Path,
    configs: list[RunConfig],
    checkpoints_dir: Path,
    results_jsonl: Path,
    failures_jsonl: Path,
    started_at: str,
    skipped_at_start: int = 0,
) -> None:
    completion_dir.mkdir(parents=True, exist_ok=True)
    completed, missing, failed = validate_completion(configs, checkpoints_dir)
    summary = {
        "experiment_id": "coap_ipsns_sensitivity",
        "expected_runs": len(configs),
        "completed_runs": len(completed),
        "skipped_resumed_runs": skipped_at_start,
        "failed_runs": len(failed),
        "missing_runs": len(missing),
        "started_at": started_at,
        "finished_at": utc_now(),
        "elapsed_seconds": round(time.perf_counter() - _GLOBAL_T0, 3),
        "results_jsonl": str(results_jsonl),
        "failures_jsonl": str(failures_jsonl),
        "checkpoints_dir": str(checkpoints_dir),
    }
    summary_path = completion_dir / "summary.json"
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    marker = completion_dir / "COMPLETED.ok"
    if missing or failed:
        if marker.exists():
            marker.unlink()
        print(
            f"[INCOMPLETE] completed={len(completed)} failed={len(failed)} "
            f"missing={len(missing)}",
            flush=True,
        )
        return

    marker.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"[COMPLETE] Wrote {marker}", flush=True)


_GLOBAL_T0 = time.perf_counter()


def main() -> int:
    global _GLOBAL_T0
    _GLOBAL_T0 = time.perf_counter()
    started_at = utc_now()

    ap = argparse.ArgumentParser(description="COAP IPSNS sensitivity (resumable)")
    ap.add_argument("--plan", type=Path, default=DEFAULT_PLAN)
    ap.add_argument("--resume", action="store_true", help="Skip valid completed checkpoints")
    ap.add_argument("--workers", type=int, default=1, help="Parallel worker processes")
    ap.add_argument("--pilot", action="store_true", help="Run a small pilot subset only")
    ap.add_argument("--pilot-instances", type=int, default=2)
    ap.add_argument("--pilot-configs", type=int, default=3,
                    help="First N unique configs per pilot instance")
    ap.add_argument("--dry-run", action="store_true", help="Print planned runs and exit")
    ap.add_argument("--completion-marker-dir", type=Path, default=DEFAULT_COMPLETION_DIR)
    args = ap.parse_args()

    plan = load_plan(args.plan)
    instances = load_instances(plan)
    configs = build_oat_configs(plan, instances)

    if args.pilot:
        pilot_instances = {r["instance"] for r in instances[: args.pilot_instances]}
        pilot_keys: set[str] = set()
        filtered: list[RunConfig] = []
        for cfg in configs:
            if cfg.instance not in pilot_instances:
                continue
            per_inst = [c for c in configs if c.instance == cfg.instance]
            unique_order: list[RunConfig] = []
            seen: set[str] = set()
            for c in per_inst:
                if c.run_key() in seen:
                    continue
                seen.add(c.run_key())
                unique_order.append(c)
            allowed = {c.run_key() for c in unique_order[: args.pilot_configs]}
            if cfg.run_key() in allowed:
                filtered.append(cfg)
        configs = filtered

    out_root = REPO_ROOT / plan["output_root"]
    checkpoints_dir = REPO_ROOT / plan["checkpoints_dir"]
    results_jsonl = REPO_ROOT / plan["results_jsonl"]
    failures_jsonl = REPO_ROOT / plan["failures_jsonl"]
    manifest_json = REPO_ROOT / plan["manifest_json"]
    tmp_dir = out_root / "tmp_rankings"

    for path in (checkpoints_dir, results_jsonl.parent, failures_jsonl.parent, tmp_dir):
        path.mkdir(parents=True, exist_ok=True)

    write_manifest(manifest_json, configs, args.plan)

    pending: list[RunConfig] = []
    skipped = 0
    for cfg in configs:
        ckpt = checkpoint_path(checkpoints_dir, cfg.run_key())
        if args.resume and is_valid_checkpoint(ckpt):
            skipped += 1
            continue
        pending.append(cfg)

    print(f"Plan: {args.plan}", flush=True)
    print(f"Instances: {len({c.instance for c in configs})}", flush=True)
    print(f"Configurations (unique keys): {len({c.run_key() for c in configs})}", flush=True)
    print(f"Total planned runs: {len(configs)}", flush=True)
    print(f"Pending runs: {len(pending)}  skipped(resume): {skipped}", flush=True)
    print(f"Workers: {max(1, args.workers)}", flush=True)

    if args.dry_run:
        for cfg in pending[:20]:
            print(f"  pending {cfg.instance} {cfg.varied_param} key={cfg.run_key()}", flush=True)
        if len(pending) > 20:
            print(f"  ... and {len(pending) - 20} more", flush=True)
        return 0

    if not pending:
        maybe_write_completion_marker(
            args.completion_marker_dir,
            configs,
            checkpoints_dir,
            results_jsonl,
            failures_jsonl,
            started_at,
            skipped_at_start=skipped,
        )
        print("Nothing to do.", flush=True)
        return 0

    workers = max(1, args.workers)
    done = 0
    total_pending = len(pending)

    if workers == 1:
        iterator = pending
        for cfg in iterator:
            done += 1
            print(
                f"[{done}/{total_pending}] {cfg.instance} varied={cfg.varied_param} "
                f"iters={cfg.iters} topK={cfg.topk_scc} seed={cfg.rng_seed}",
                flush=True,
            )
            record = execute_run(cfg, checkpoints_dir, tmp_dir)
            if record["status"] == "ok":
                append_jsonl(results_jsonl, record)
                print(
                    f"  -> ok bw={record.get('backward_weight')} rt={record.get('runtime')}s",
                    flush=True,
                )
            else:
                append_jsonl(failures_jsonl, record)
                print(f"  -> FAIL {record.get('error')}", flush=True)
    else:
        ctx = mp.get_context("spawn")
        with ctx.Pool(processes=workers) as pool:
            for done, record in enumerate(
                pool.imap_unordered(
                    _worker,
                    [(cfg, str(checkpoints_dir), str(tmp_dir)) for cfg in pending],
                    chunksize=1,
                ),
                start=1,
            ):
                if record["status"] == "ok":
                    append_jsonl(results_jsonl, record)
                else:
                    append_jsonl(failures_jsonl, record)
                print(
                    f"[{done}/{total_pending}] {record.get('instance')} "
                    f"status={record.get('status')} rt={record.get('runtime')}s",
                    flush=True,
                )

    maybe_write_completion_marker(
        args.completion_marker_dir,
        configs,
        checkpoints_dir,
        results_jsonl,
        failures_jsonl,
        started_at,
        skipped_at_start=skipped,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
