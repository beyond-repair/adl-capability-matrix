import json
from pathlib import Path

from matrix.load import load_matrix

AUDIT_PATH = (
    Path(__file__).resolve().parents[1]
    / "matrix"
    / "function_audit_scale_functional_I.json"
)
GAP_PATH = Path(__file__).resolve().parents[1] / "matrix" / "census_gap_2026-10-02.json"


def test_scale_functional_i_audit_does_not_assign_cap():
    matrix = load_matrix()
    audit = json.loads(AUDIT_PATH.read_text(encoding="utf-8"))
    gap = json.loads(GAP_PATH.read_text(encoding="utf-8"))
    assert matrix["inventory_count"] == 67
    assert len(matrix["rows"]) == 67
    assert audit["repo"] == "scale-functional-I"
    assert audit["cluster"] is None
    assert audit["claim_cap"] is None
    assert audit["status"] == "UNASSIGNED"
    assert audit["locked_inventory_expanded"] is False
    assert audit["executed_by_tests"] == ["dumbbell_mask", "perimeter"]
    assert audit["not_executed_by_tests"] == ["main"]
    assert "main" not in audit["executed_by_tests"]
    missing = [item["name"] for item in gap["missing_from_locked_matrix"]]
    row = next(item for item in gap["missing_from_locked_matrix"] if item["name"] == "scale-functional-I")
    assert "scale-functional-I" in missing
    assert row["cluster"] is None
    assert row["claim_cap"] is None
    assert row["status"] == "UNASSIGNED"
