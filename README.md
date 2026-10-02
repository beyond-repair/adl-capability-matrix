<div align="center">

[![Lifecycle](https://img.shields.io/badge/●_RESEARCH-a855f7?style=for-the-badge&labelColor=0f0f23)](https://github.com/beyond-repair/ADL-Governance)
[![Claim](https://img.shields.io/badge/Claim_≤1-22c55e?style=for-the-badge&labelColor=0f0f23)](https://github.com/beyond-repair/ADL-Governance/blob/main/docs/CLAIM_VALIDATION.md)
[![Governance](https://img.shields.io/badge/ADL--Governance-7c3aed?style=for-the-badge&labelColor=0f0f23)](https://github.com/beyond-repair/ADL-Governance)

```
LIFECYCLE   RESEARCH
CLAIM       ≤1
NOT CLAIMED thrust · energy extraction · AGI · production autonomy · live SLA · live crawl
```

</div>

---

# adl-capability-matrix

**Status: RESEARCH** (governance census tool). Claim level **≤1**. Claim-capped cluster matrix for the `beyond-repair` GitHub portfolio.

Deterministic **cluster + claim-cap** checker for a **dated** snapshot. A green run does not refresh the portfolio and does not assign clusters or caps to names that were absent on 2026-09-04.

Nothing to configure. The checker reads only the JSON committed in this repository. It does not use the network, the environment, or a token.

## Quick start

Python 3.10 or newer. From the repository root:

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -e ".[dev]"
python -m matrix.engine
python -m matrix
python -m pytest -q
```

Both commands print:

```
rows=67 queue=5 gap_unassigned=15
OK
```

and exit 0 when the locked matrix and the committed 2026-10-01 name gap pass. They exit 1 and list `ERRORS` when a record breaks the contract. `python -m matrix` is the same report as `python -m matrix.engine`. After the editable install, those commands work from any working directory.

`requirements.txt` pins the same pytest for a root-directory run without installing the package. That path only works when the current directory is the repository root, because Python then imports the local `matrix` package:

```bash
python -m pip install -r requirements.txt
python -m matrix.engine
python -m pytest -q
```

## Contract

The checker validates records already in this repo. It does not invent rows.

- `matrix/capability_matrix.json` stays a **67-row** inventory (`inventory_count` 67) snapshotted from GitHub search `user:beyond-repair` on **2026-09-04**.
- Each locked row has a unique `name`, a `cluster` that matches the `clusters` index exactly, a legal `claim_cap`, the maturity paired with that cap, and a `url` of `https://github.com/<owner>/<name>`.
- `compatible_build_queue` ids are unique. Status is `IN_THIS_COMMIT`, `QUEUED`, or `REJECTED`. Every `compatible_with` name is a locked row. `Q-001` is this repo and `IN_THIS_COMMIT`. Each item has a non-empty `must_not_claim`.
- `rejected_hypotheses` has at least three statements.
- `matrix/census_gap_2026-10-01.json` is name-only presence accounting against a 2026-10-01 search list committed in that file. `missing_from_locked_matrix` and `in_matrix_not_in_live_search` must be the sorted set differences. Unassigned names keep `cluster` and `claim_cap` null and `status` `UNASSIGNED`. Policy is `NO_CLUSTER_OR_CAP_INVENTED`.

Locked cap / maturity pairing (already true of every row; not a new assignment):

| Cap | Maturity | Meaning |
|---|---|---|
| NAME_ONLY | empty_stub | Empty or near-empty tree |
| METADATA_ONLY | scaffold | Scaffold / tiny tree |
| SURFACE_API_UNVERIFIED | partial | Partial tree; APIs not audited |
| TREE_PRESENT_FUNCTIONS_UNAUDITED | substantial_tree | Larger tree; functions not inventoried |

## What this repository claims

- 67 repositories were enumerated from GitHub search `user:beyond-repair` on **2026-09-04**.
- Each of those 67 is assigned a **cluster** and a **claim_cap** from metadata only.
- A **compatible-build queue** lists systems compatible with existing work and **not** claimed as already built (except `Q-001`, this repo).
- Sweep-175 records the set difference between that locked inventory and a 2026-10-01 search of 82 names. Missing names are `UNASSIGNED`. That is presence accounting, not a capability audit.
- The checker enforces the contract above on the committed files only.

## What this repository does not claim

- Currency of cluster/cap rows with any later portfolio census. Cap refresh remains **OPEN**.
- That the 15 names absent from the lock have a cluster or a claim cap.
- Per-function inventories of every repository.
- Runtime interoperability of Sunder, SEEM, VSA, or CFT stacks.
- Physical correctness of Coherence Drive / Ware Constant artifacts.
- That duplicate Digital Double / SEEM repos are equivalent.
- A live GitHub crawl. The committed gap file is not re-fetched.

## Sweep-175 re-audit

Historical record. This repair does not expand the 67 rows and does not assign caps.

| Field | Value |
|-------|--------|
| Classification | RESEARCH (unchanged; not promoted) |
| Locked JSON rows | 67 (2026-09-04 snapshot; not expanded) |
| Live search census | 82 (`user:beyond-repair`, `incomplete_results=false`, 2026-10-01) |
| Names in live search absent from locked rows | 15 (name-only gap file; cluster and cap left null) |
| Names in locked rows absent from live search | 0 |
| Row expansion with caps | NOT DONE (would invent caps) |
| Local tests this sweep | 8 passed (6 prior + 2 gap); Finish repair 16 passed |
| Post-push CI | **success** [36889001703](https://github.com/beyond-repair/adl-capability-matrix/actions/runs/36889001703) on `e57ec52` |

See `CLAIM_STATUS.md` and `GOVERNANCE.md`.

---

<div align="center">

**REWRITE · BUILD · TRANSCEND**

Governing source: [ADL-Governance](https://github.com/beyond-repair/ADL-Governance) · [Claim levels 0–5](https://github.com/beyond-repair/ADL-Governance/blob/main/docs/CLAIM_VALIDATION.md)

</div>
