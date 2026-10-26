import json
from pathlib import Path

from matrix.load import load_matrix

AUDIT_PATH = (
    Path(__file__).resolve().parents[1]
    / "matrix"
    / "function_audit_finite_gasket_spectral_derivatives.json"
)


def test_finite_gasket_audit_does_not_invent_cap():
    matrix = load_matrix()
    audit = json.loads(AUDIT_PATH.read_text(encoding="utf-8"))
    assert matrix["inventory_count"] == 67
    assert len(matrix["rows"]) == 67
    assert audit["repo"] == "finite-gasket-spectral-derivatives"
    assert audit["claim_cap"] is None
    assert audit["cluster"] is None
    assert audit["status"] == "UNASSIGNED"
    assert audit["locked_inventory_expanded"] is False
    assert "gamma_loop" in audit["executed_by_tests"]
    assert "CLI entrypoints" in audit["not_executed_by_tests"]
    # Confirm name remains in unassigned gap (not in locked rows)
    locked_names = {r["name"] for r in matrix["rows"]}
    assert "finite-gasket-spectral-derivatives" not in locked_names
