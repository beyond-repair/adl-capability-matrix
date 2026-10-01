import json
from pathlib import Path

from matrix.load import load_matrix

GAP_PATH = Path(__file__).resolve().parents[1] / "matrix" / "census_gap_2026-10-01.json"


def test_census_gap_is_exact_set_difference():
    matrix = load_matrix()
    gap = json.loads(GAP_PATH.read_text(encoding="utf-8"))
    locked = {row["name"] for row in matrix["rows"]}
    observed = gap["observed_names"]
    assert gap["live_total_count"] == 82
    assert gap["incomplete_results"] is False
    assert len(observed) == 82
    assert len(observed) == len(set(observed))
    missing = [item["name"] for item in gap["missing_from_locked_matrix"]]
    assert missing == sorted(set(observed) - locked)
    assert gap["in_matrix_not_in_live_search"] == sorted(locked - set(observed))
    assert len(missing) == 15
    for item in gap["missing_from_locked_matrix"]:
        assert item["cluster"] is None
        assert item["claim_cap"] is None
        assert item["status"] == "UNASSIGNED"
    assert gap["assignment_policy"] == "NO_CLUSTER_OR_CAP_INVENTED"


def test_locked_matrix_row_count_unchanged():
    matrix = load_matrix()
    assert matrix["inventory_count"] == 67
    assert len(matrix["rows"]) == 67
