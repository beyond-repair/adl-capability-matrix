# Claim Status — adl-capability-matrix

**Classification:** RESEARCH (governance census tool)
**Sweep:** 115 (2026-09-07)
**Head at lock:** `50ce48524c372f628137c0bd3b7901c5c7c10ba5` (pre-docs); Sweep-115 docs commit follows.

## Allowed claims

| Feature | State |
|---------|-------|
| Deterministic load + validate of locked JSON matrix | VERIFIED (tests + CI run 33932359958 success; not re-run this sweep) |
| 67-row inventory snapshot from GitHub search `user:beyond-repair` on 2026-09-04 | VERIFIED as of that date only |
| Claim caps restricted to NAME_ONLY / METADATA_ONLY / SURFACE_API_UNVERIFIED / TREE_PRESENT_FUNCTIONS_UNAUDITED | VERIFIED by `validate_matrix` |
| Compatible-build queue exists with Q-001 = this repo IN_THIS_COMMIT | VERIFIED by tests |
| GOVERNANCE.md present | VERIFIED Sweep-115 |

## Forbidden / not claimed

| Claim | Status |
|-------|--------|
| Matrix is complete for current live portfolio | **UNSUPPORTED** — live search total_count **75** (`incomplete_results=false`) Sweep-115; JSON inventory_count locked at **67** |
| Per-function AST census of any repo | NOT PERFORMED |
| Runtime interop of Sunder / SEEM / VSA / CFT | NOT CLAIMED |
| Physical correctness of Coherence Drive / Ware artifacts | NOT CLAIMED |
| Equivalence of Digital Double or SEEM name forks | NOT CLAIMED |
| Production-ready portfolio SLA | FORBIDDEN |

## Drift note

Sweep-115 reconfirmed live GitHub search `user:beyond-repair` **total_count=75**. Expanding rows is **OPEN** and operator-gated. Do not invent cluster/cap assignments.

## CI

Latest listed product workflow on `main`: run **33932359958** conclusion **success** (2026-09-05). First Actions conclusion after Sweep-115 docs push is **PENDING**.
