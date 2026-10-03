import json
from pathlib import Path

from matrix.load import load_matrix, validate_gap

GAP_PATH = Path(__file__).resolve().parents[1] / "matrix" / "census_gap_2026-10-02.json"
PRIOR_PATH = Path(__file__).resolve().parents[1] / "matrix" / "census_gap_2026-10-01.json"


def test_census_gap_2026_10_02_is_exact_set_difference():
    matrix = load_matrix()
    gap = json.loads(GAP_PATH.read_text(encoding="utf-8"))
    errors = validate_gap(matrix, gap)
    assert errors == []
    assert gap["live_total_count"] == 83
    assert gap["incomplete_results"] is False
    assert len(gap["observed_names"]) == 83
    missing = [item["name"] for item in gap["missing_from_locked_matrix"]]
    assert len(missing) == 16
    assert "scale-functional-I" in missing
    for item in gap["missing_from_locked_matrix"]:
        assert item["cluster"] is None
        assert item["claim_cap"] is None
        assert item["status"] == "UNASSIGNED"


def test_only_new_name_versus_2026_10_01():
    prior = json.loads(PRIOR_PATH.read_text(encoding="utf-8"))
    gap = json.loads(GAP_PATH.read_text(encoding="utf-8"))
    added = sorted(set(gap["observed_names"]) - set(prior["observed_names"]))
    removed = sorted(set(prior["observed_names"]) - set(gap["observed_names"]))
    assert added == ["scale-functional-I"]
    assert removed == []
    assert matrix_row_count_unchanged()


def matrix_row_count_unchanged():
    matrix = load_matrix()
    assert matrix["inventory_count"] == 67
    assert len(matrix["rows"]) == 67
    return True
