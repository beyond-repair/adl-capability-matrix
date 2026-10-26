import json
from pathlib import Path

from matrix.load import load_matrix

AUDIT_PATH = (
    Path(__file__).resolve().parents[1]
    / "matrix"
    / "function_audit_Digital_Double_virtual_workforce.json"
)


def test_digital_double_audit_does_not_elevate_cap():
    matrix = load_matrix()
    audit = json.loads(AUDIT_PATH.read_text(encoding="utf-8"))
    assert matrix["inventory_count"] == 67
    assert len(matrix["rows"]) == 67
    assert audit["repo"] == "Digital_Double_virtual_workforce"
    assert audit["claim_cap"] == "TREE_PRESENT_FUNCTIONS_UNAUDITED"
    assert audit["locked_inventory_expanded"] is False
    assert "Agent.assign_task" in audit["executed_by_tests"]
    assert "LLM inference" in audit["not_executed_by_tests"]
    # Confirm existing row still has the same cap
    row = next(r for r in matrix["rows"] if r["name"] == "Digital_Double_virtual_workforce")
    assert row["claim_cap"] == "TREE_PRESENT_FUNCTIONS_UNAUDITED"
