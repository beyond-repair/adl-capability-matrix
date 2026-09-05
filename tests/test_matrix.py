from matrix.load import load_matrix, validate_matrix, ALLOWED_CAPS


def test_matrix_validates():
    data = load_matrix()
    assert validate_matrix(data) == []


def test_inventory_count_is_sixty_seven():
    data = load_matrix()
    assert data["inventory_count"] == 67
    assert len(data["rows"]) == 67


def test_no_function_level_claim_cap():
    data = load_matrix()
    forbidden = {"FEATURE_COMPLETE", "FUNCTION_AUDITED", "PRODUCTION_READY"}
    for row in data["rows"]:
        assert row["claim_cap"] in ALLOWED_CAPS
        assert row["claim_cap"] not in forbidden


def test_queue_has_this_repo_and_gaps():
    data = load_matrix()
    qids = {q["id"] for q in data["compatible_build_queue"]}
    assert "Q-001" in qids
    statuses = {q["id"]: q["status"] for q in data["compatible_build_queue"]}
    assert statuses["Q-001"] == "IN_THIS_COMMIT"


def test_rejected_hypotheses_present():
    data = load_matrix()
    assert len(data["rejected_hypotheses"]) >= 3


def test_digital_double_cluster_has_duplicates():
    data = load_matrix()
    dd = [r["name"] for r in data["rows"] if r["cluster"] == "digital_double"]
    assert len(dd) >= 4
