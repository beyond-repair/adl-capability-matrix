<div align="center">

[![Lifecycle](https://img.shields.io/badge/●_RESEARCH-a855f7?style=for-the-badge&labelColor=0f0f23)](https://github.com/beyond-repair/ADL-Governance)
[![Claim](https://img.shields.io/badge/Claim_≤1-22c55e?style=for-the-badge&labelColor=0f0f23)](https://github.com/beyond-repair/ADL-Governance/blob/main/docs/CLAIM_VALIDATION.md)
[![Governance](https://img.shields.io/badge/ADL--Governance-7c3aed?style=for-the-badge&labelColor=0f0f23)](https://github.com/beyond-repair/ADL-Governance)

```
LIFECYCLE   RESEARCH
CLAIM       ≤1
NOT CLAIMED thrust · energy extraction · AGI · production autonomy · live SLA
```

</div>

---

# adl-capability-matrix

**Status: RESEARCH** (governance census tool). Claim-capped cluster matrix for the `beyond-repair` GitHub portfolio.

Deterministic **cluster + claim-cap** matrix. Snapshot is **dated**, not a live SLA.

## Sweep-175 re-audit

| Field | Value |
|-------|--------|
| Classification | RESEARCH (unchanged; not promoted) |
| Locked JSON rows | 67 (2026-09-04 snapshot; not expanded) |
| Live search census | 82 (`user:beyond-repair`, `incomplete_results=false`, 2026-10-01) |
| Names in live search absent from locked rows | 15 (name-only gap file; cluster and cap left null) |
| Names in locked rows absent from live search | 0 |
| Row expansion with caps | NOT DONE (would invent caps) |
| Local tests this sweep | 8 passed (6 prior + 2 gap) |
| Post-push CI | **success** [36889001703](https://github.com/beyond-repair/adl-capability-matrix/actions/runs/36889001703) on `e57ec52` |

## What this repository claims

- 67 repositories were enumerated from GitHub search `user:beyond-repair` on **2026-09-04**.
- Each of those 67 is assigned a **cluster** and a **claim_cap** from metadata only.
- A **compatible-build queue** lists systems compatible with existing work and **not** claimed as already built (except `Q-001`, this repo).
- Sweep-175 records the set difference between that locked inventory and a 2026-10-01 search of 82 names. Missing names are `UNASSIGNED`. That is presence accounting, not a capability audit.
- Validator + tests + CI enforce legal claim caps on the locked rows only.

## What this repository does not claim

- Currency of cluster/cap rows with the live portfolio census (**82** items, Sweep-175). Cap refresh remains **OPEN**.
- Per-function inventories of every repository.
- Runtime interoperability of Sunder, SEEM, VSA, or CFT stacks.
- Physical correctness of Coherence Drive / Ware Constant artifacts.
- That duplicate Digital Double / SEEM repos are equivalent.

Claim caps (locked rows only):

| Cap | Meaning |
|---|---|
| NAME_ONLY | Empty or near-empty tree |
| METADATA_ONLY | Scaffold / tiny tree |
| SURFACE_API_UNVERIFIED | Partial tree; APIs not audited |
| TREE_PRESENT_FUNCTIONS_UNAUDITED | Larger tree; functions not inventoried |

Gap file: `matrix/census_gap_2026-10-01.json`.

## Run tests

```bash
pip install -r requirements.txt
python -m pytest -q
```

See `CLAIM_STATUS.md` and `GOVERNANCE.md`.

---

<div align="center">

**REWRITE · BUILD · TRANSCEND**

Governing source: [ADL-Governance](https://github.com/beyond-repair/ADL-Governance) · [Claim levels 0–5](https://github.com/beyond-repair/ADL-Governance/blob/main/docs/CLAIM_VALIDATION.md)

</div>
