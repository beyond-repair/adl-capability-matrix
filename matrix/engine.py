"""Run the locked capability-matrix checker. Does not crawl GitHub."""

from __future__ import annotations

from .load import GAP_PATH, load_gap, load_matrix, validate_gap, validate_matrix


def main() -> int:
    data = load_matrix()
    errors = list(validate_matrix(data))
    unassigned = 0
    if not GAP_PATH.is_file():
        errors.append("missing census gap file")
    else:
        gap = load_gap()
        errors.extend(validate_gap(data, gap))
        missing = gap.get("missing_from_locked_matrix") or []
        unassigned = len(missing) if isinstance(missing, list) else 0
    rows = len(data.get("rows") or [])
    queue = len(data.get("compatible_build_queue") or [])
    print(f"rows={rows} queue={queue} gap_unassigned={unassigned}")
    if errors:
        print("ERRORS:")
        for err in errors:
            print(" -", err)
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
