from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ALLOWED_CAPS = {
    "NAME_ONLY",
    "METADATA_ONLY",
    "SURFACE_API_UNVERIFIED",
    "TREE_PRESENT_FUNCTIONS_UNAUDITED",
}

# Pairing already true of every locked row. Not a new maturity assignment.
CAP_MATURITY = {
    "NAME_ONLY": "empty_stub",
    "METADATA_ONLY": "scaffold",
    "SURFACE_API_UNVERIFIED": "partial",
    "TREE_PRESENT_FUNCTIONS_UNAUDITED": "substantial_tree",
}

ALLOWED_QUEUE_STATUS = {"IN_THIS_COMMIT", "QUEUED", "REJECTED"}

MATRIX_PATH = Path(__file__).with_name("capability_matrix.json")
GAP_PATH = Path(__file__).with_name("census_gap_2026-10-01.json")


def load_matrix(path: Path | None = None) -> dict[str, Any]:
    p = path or MATRIX_PATH
    return json.loads(p.read_text(encoding="utf-8"))


def load_gap(path: Path | None = None) -> dict[str, Any]:
    p = path or GAP_PATH
    return json.loads(p.read_text(encoding="utf-8"))


def validate_matrix(data: dict[str, Any]) -> list[str]:
    """Return a list of violation strings. Empty list means pass."""
    errors: list[str] = []
    rows = data.get("rows") or []
    names = [r.get("name") for r in rows]
    if len(names) != data.get("inventory_count"):
        errors.append("inventory_count mismatch")
    if len(names) != len(set(names)):
        errors.append("duplicate repository names")
    if len(names) < 1:
        errors.append("empty inventory")
    owner = data.get("owner")
    if not isinstance(owner, str) or not owner.strip():
        errors.append("missing owner")
    locked_names = {n for n in names if isinstance(n, str) and n}
    for r in rows:
        name = r.get("name")
        cap = r.get("claim_cap")
        cluster = r.get("cluster")
        if cap not in ALLOWED_CAPS:
            errors.append(f"illegal claim_cap for {name}: {cap}")
        if not cluster:
            errors.append(f"missing cluster for {name}")
        if not name:
            errors.append("row missing name")
        expected_maturity = CAP_MATURITY.get(cap) if isinstance(cap, str) else None
        if expected_maturity is None or r.get("maturity") != expected_maturity:
            errors.append(f"maturity/cap mismatch for {name}: {r.get('maturity')} vs {cap}")
        if isinstance(name, str) and isinstance(owner, str) and owner.strip():
            expected_url = f"https://github.com/{owner}/{name}"
            if r.get("url") != expected_url:
                errors.append(f"url mismatch for {name}")
    clusters = data.get("clusters")
    if not isinstance(clusters, dict):
        errors.append("clusters index missing")
    else:
        grouped: dict[str, list[Any]] = {}
        for r in rows:
            grouped.setdefault(r.get("cluster"), []).append(r.get("name"))
        if set(grouped) != set(clusters):
            errors.append("cluster index keys do not match row clusters")
        for key, indexed in clusters.items():
            if not isinstance(indexed, list):
                errors.append(f"cluster index {key} is not a list")
                continue
            if len(indexed) != len(set(indexed)) or sorted(indexed) != sorted(grouped.get(key, [])):
                errors.append(f"cluster index mismatch for {key}")
    hypotheses = data.get("rejected_hypotheses")
    if not isinstance(hypotheses, list) or len(hypotheses) < 3 or any(
        not isinstance(item, str) or not item.strip() for item in hypotheses
    ):
        errors.append("rejected_hypotheses must list at least 3 statements")
    queue = data.get("compatible_build_queue") or []
    ids = [q.get("id") for q in queue]
    if len(ids) != len(set(ids)):
        errors.append("duplicate queue ids")
    saw_q001 = False
    for q in queue:
        qid = q.get("id")
        if q.get("status") not in ALLOWED_QUEUE_STATUS:
            errors.append(f"illegal queue status {qid}")
        if not q.get("must_not_claim"):
            errors.append(f"queue {qid} missing must_not_claim")
        compatible = q.get("compatible_with")
        if not isinstance(compatible, list) or not compatible:
            errors.append(f"queue {qid} missing compatible_with")
        else:
            for ref in compatible:
                if ref not in locked_names:
                    errors.append(f"queue {qid} compatible_with unknown repo {ref}")
        if qid == "Q-001":
            saw_q001 = True
            if q.get("status") != "IN_THIS_COMMIT":
                errors.append("Q-001 must be IN_THIS_COMMIT")
            if q.get("proposed_repo") != "adl-capability-matrix":
                errors.append("Q-001 proposed_repo must be adl-capability-matrix")
    if not saw_q001:
        errors.append("queue missing Q-001")
    return errors


def validate_gap(matrix: dict[str, Any], gap: dict[str, Any]) -> list[str]:
    """Check the committed name-only gap against the locked matrix. No caps are assigned."""
    errors: list[str] = []
    locked = {row.get("name") for row in (matrix.get("rows") or []) if row.get("name")}
    observed = gap.get("observed_names")
    if not isinstance(observed, list) or any(not isinstance(name, str) or not name for name in observed):
        errors.append("observed_names must be a list of names")
        observed_list: list[str] = []
    else:
        observed_list = observed
    if len(observed_list) != len(set(observed_list)):
        errors.append("duplicate observed_names")
    if gap.get("live_total_count") != len(observed_list):
        errors.append("live_total_count mismatch")
    if gap.get("incomplete_results") is not False:
        errors.append("incomplete_results must be false")
    if gap.get("matrix_inventory_count") != matrix.get("inventory_count"):
        errors.append("gap matrix_inventory_count mismatch")
    if gap.get("assignment_policy") != "NO_CLUSTER_OR_CAP_INVENTED":
        errors.append("assignment_policy must be NO_CLUSTER_OR_CAP_INVENTED")
    missing_items = gap.get("missing_from_locked_matrix")
    if not isinstance(missing_items, list):
        errors.append("missing_from_locked_matrix must be a list")
        missing_items = []
    missing_names = [item.get("name") if isinstance(item, dict) else None for item in missing_items]
    expected_missing = sorted(set(observed_list) - locked)
    if missing_names != expected_missing:
        errors.append("missing_from_locked_matrix is not the sorted set difference")
    extras = gap.get("in_matrix_not_in_live_search")
    if extras != sorted(locked - set(observed_list)):
        errors.append("in_matrix_not_in_live_search is not the sorted set difference")
    for item in missing_items:
        if not isinstance(item, dict):
            errors.append("gap item must be an object")
            continue
        if item.get("cluster") is not None or item.get("claim_cap") is not None:
            errors.append(f"invented cluster or cap for {item.get('name')}")
        if item.get("status") != "UNASSIGNED":
            errors.append(f"gap status must be UNASSIGNED for {item.get('name')}")
    return errors
