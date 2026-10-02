import copy
import json
import subprocess
import sys
from pathlib import Path

from matrix import __version__
from matrix.load import load_gap, load_matrix, validate_gap, validate_matrix

ROOT = Path(__file__).resolve().parents[1]


def test_package_version():
    assert __version__ == "0.1.1"


def test_engine_cli_reports_locked_snapshot():
    proc = subprocess.run(
        [sys.executable, "-m", "matrix.engine"],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert proc.returncode == 0, proc.stderr
    assert proc.stdout.splitlines() == [
        "rows=67 queue=5 gap_unassigned=15",
        "OK",
    ]
    assert proc.stderr == ""


def test_module_cli_matches_engine():
    proc = subprocess.run(
        [sys.executable, "-m", "matrix"],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert proc.returncode == 0, proc.stderr
    assert proc.stdout.splitlines()[0] == "rows=67 queue=5 gap_unassigned=15"
    assert proc.stdout.splitlines()[-1] == "OK"


def test_illegal_cap_fails():
    data = copy.deepcopy(load_matrix())
    data["rows"][0]["claim_cap"] = "FEATURE_COMPLETE"
    errors = validate_matrix(data)
    assert any("illegal claim_cap" in err for err in errors)


def test_cluster_index_mismatch_fails():
    data = copy.deepcopy(load_matrix())
    key = data["rows"][0]["cluster"]
    data["clusters"][key] = list(data["clusters"][key][:-1])
    errors = validate_matrix(data)
    assert any(f"cluster index mismatch for {key}" in err for err in errors)


def test_dangling_queue_reference_fails():
    data = copy.deepcopy(load_matrix())
    data["compatible_build_queue"][0]["compatible_with"] = ["not-a-locked-repo"]
    errors = validate_matrix(data)
    assert any("unknown repo not-a-locked-repo" in err for err in errors)


def test_invented_gap_cap_fails():
    matrix = load_matrix()
    gap = copy.deepcopy(load_gap())
    gap["missing_from_locked_matrix"][0]["claim_cap"] = "NAME_ONLY"
    errors = validate_gap(matrix, gap)
    assert any("invented cluster or cap" in err for err in errors)


def test_gap_file_round_trip_is_json():
    raw = json.loads((ROOT / "matrix" / "census_gap_2026-10-01.json").read_text(encoding="utf-8"))
    assert validate_gap(load_matrix(), raw) == []
