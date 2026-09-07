# Governance — adl-capability-matrix

**Sweep:** 115  
**Classification:** RESEARCH  
**Claim level:** 1 (dated census tool; not live SLA)  
**Head at lock:** `50ce48524c372f628137c0bd3b7901c5c7c10ba5`

## Invariants

- This repository is a **dated JSON snapshot** plus a validator. It is not the live portfolio registry.
- Authoritative live inventory lives in `beyond-repair/ADL-Governance` (`docs/PORTFOLIO_STATUS_REPORT.md`, `docs/repository_registry.md`).
- Expanding `capability_matrix.json` to match live `total_count=75` requires a **fresh enumeration plus per-row cluster/cap assignment**. That expansion is **not** performed in Sweep-115 (would invent unsupported metadata).
- Forbidden: claiming the matrix is complete, claiming per-function AST census, claiming runtime interop across clusters.

## Observed tree

- `matrix/capability_matrix.json` — locked inventory_count **67** (2026-09-04 snapshot).
- `matrix/load.py` + tests — deterministic load/validate.
- CI workflow present. Last listed product success: run **33932359958** (2026-09-05). Sweep-115 does not re-assert a new Actions conclusion until listed.
- `GOVERNANCE.md` added this sweep.

## Allowed agent actions

Docs, claim tokens, docs-presence. No invented rows. No ACTIVE promotion. No archive API.
