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

MATRIX_PATH = Path(__file__).with_name("capability_matrix.json")


def load_matrix(path: Path | None = None) -> dict[str, Any]:
    p = path or MATRIX_PATH
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
    for r in rows:
        cap = r.get("claim_cap")
        if cap not in ALLOWED_CAPS:
            errors.append(f"illegal claim_cap for {r.get('name')}: {cap}")
        if not r.get("cluster"):
            errors.append(f"missing cluster for {r.get('name')}")
        if not r.get("name"):
            errors.append("row missing name")
    queue = data.get("compatible_build_queue") or []
    ids = [q.get("id") for q in queue]
    if len(ids) != len(set(ids)):
        errors.append("duplicate queue ids")
    for q in queue:
        if q.get("status") not in {"IN_THIS_COMMIT", "QUEUED", "REJECTED"}:
            errors.append(f"illegal queue status {q.get('id')}")
        if not q.get("must_not_claim"):
            errors.append(f"queue {q.get('id')} missing must_not_claim")
    return errors
