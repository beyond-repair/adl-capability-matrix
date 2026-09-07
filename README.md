# adl-capability-matrix

**Status: RESEARCH** (governance census tool). Claim-capped cluster matrix for the `beyond-repair` GitHub portfolio.

Deterministic **cluster + claim-cap** matrix. Snapshot is **dated**, not a live SLA.

## Sweep-115 lock

| Field | Value |
|-------|--------|
| Classification | RESEARCH |
| Live search census | 75 (`user:beyond-repair`, incomplete_results=false) |
| Locked JSON rows | 67 (2026-09-04) |
| Row expansion this sweep | NOT DONE (would invent caps) |
| Last listed product CI | 33932359958 success |
| Post-lock CI | PENDING |

## What this repository claims

- 67 public repositories were enumerated from GitHub search `user:beyond-repair` on **2026-09-04**.
- Each of those 67 is assigned a **cluster** and a **claim_cap** from metadata only.
- A **compatible-build queue** lists systems compatible with existing work and **not** claimed as already built (except `Q-001`, this repo).
- Validator + tests + listed CI enforce legal claim caps only.

## What this repository does not claim

- Currency with the live portfolio census (**75** items, Sweep-115). Inventory refresh is **OPEN**.
- Per-function inventories of every repository.
- Runtime interoperability of Sunder, SEEM, VSA, or CFT stacks.
- Physical correctness of Coherence Drive / Ware Constant artifacts.
- That duplicate Digital Double / SEEM repos are equivalent.

Claim caps (locked):

| Cap | Meaning |
|---|---|
| NAME_ONLY | Empty or near-empty tree |
| METADATA_ONLY | Scaffold / tiny tree |
| SURFACE_API_UNVERIFIED | Partial tree; APIs not audited |
| TREE_PRESENT_FUNCTIONS_UNAUDITED | Larger tree; functions not inventoried |

## Run tests

```bash
pip install -r requirements.txt
python -m pytest -q
```

See `CLAIM_STATUS.md` and `GOVERNANCE.md`.
