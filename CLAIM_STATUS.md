# Claim Status — adl-capability-matrix

**Classification:** RESEARCH (governance census tool)
**Sweep:** 175 (2026-10-01) re-audit of Sweep-115 lock
**Head at prior lock:** `ea940fe405201855747e4d4cd9eed3816f5c9e91`

## Allowed claims

| Feature | State |
|---------|-------|
| Deterministic load + validate of locked JSON matrix | VERIFIED (local pytest 8 passed this sweep; prior CI 33932359958 success) |
| 67-row inventory snapshot from GitHub search `user:beyond-repair` on 2026-09-04 | VERIFIED as of that date only |
| Claim caps restricted to NAME_ONLY / METADATA_ONLY / SURFACE_API_UNVERIFIED / TREE_PRESENT_FUNCTIONS_UNAUDITED | VERIFIED by `validate_matrix` |
| Compatible-build queue exists with Q-001 = this repo IN_THIS_COMMIT | VERIFIED by tests |
| Sweep-175 name gap: 15 live names absent from locked rows; 0 locked names absent from live search | VERIFIED against the committed 2026-10-01 name list and the locked JSON |
| GOVERNANCE.md present | VERIFIED |

## Forbidden / not claimed

| Claim | Status |
|-------|--------|
| Matrix caps are complete for the current live portfolio | **UNSUPPORTED** — live search total_count **82**; JSON inventory_count locked at **67** |
| The 15 missing names have a cluster or claim cap | **NOT ASSIGNED** (`cluster` and `claim_cap` are null) |
| Per-function AST census of any repo | NOT PERFORMED |
| Runtime interop of Sunder / SEEM / VSA / CFT | NOT CLAIMED |
| Physical correctness of Coherence Drive / Ware artifacts | NOT CLAIMED |
| Equivalence of Digital Double or SEEM name forks | NOT CLAIMED |
| Production-ready portfolio SLA | FORBIDDEN |

## Drift note

Sweep-175 reconfirmed live GitHub search `user:beyond-repair` **total_count=82** (`incomplete_results=false`). Missing names: ADL-Nexus, Open-Energy-Fusion, Sovereign-Epistemic-Reality-Engine, adl-capability-matrix, adl-function-census, atomicdreamlabs, bloch-coherence-factor2, finite-gasket-spectral-derivatives, informational-flux-identity, mend, mendthegame, os-family-constitution-map, seem-identity-unifier, seem-sunder-bridge, sunder-cleanroom-vsa-adapter. Expanding rows with caps remains **OPEN**. Do not invent cluster/cap assignments.

## CI

Prior listed product workflow on `main`: run **33932359958** conclusion **success** (2026-09-05). Actions conclusion after the Sweep-175 push: run **36889001703** conclusion **success** on `e57ec52`.
