# Claim Status — adl-capability-matrix

**Classification:** RESEARCH (governance census tool)
**Sweep:** 175 (2026-10-01) re-audit of Sweep-115 lock
**Head at prior lock:** `ea940fe405201855747e4d4cd9eed3816f5c9e91`

## Allowed claims

| Feature | State |
|---------|-------|
| Deterministic load + validate of locked JSON matrix | VERIFIED (local pytest 16 passed (Finish repair); prior CI 33932359958 success) |
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
| Portfolio-wide per-function census | NOT PERFORMED — Sweep-210 audits only scale-functional-I test-executed names |
| Runtime interop of Sunder / SEEM / VSA / CFT | NOT CLAIMED |
| Physical correctness of Coherence Drive / Ware artifacts | NOT CLAIMED |
| Equivalence of Digital Double or SEEM name forks | NOT CLAIMED |
| Production-ready portfolio SLA | FORBIDDEN |

## Drift note

Sweep-175 reconfirmed live GitHub search `user:beyond-repair` **total_count=82** (`incomplete_results=false`). Missing names: ADL-Nexus, Open-Energy-Fusion, Sovereign-Epistemic-Reality-Engine, adl-capability-matrix, adl-function-census, atomicdreamlabs, bloch-coherence-factor2, finite-gasket-spectral-derivatives, informational-flux-identity, mend, mendthegame, os-family-constitution-map, seem-identity-unifier, seem-sunder-bridge, sunder-cleanroom-vsa-adapter. Expanding rows with caps remains **OPEN**. Do not invent cluster/cap assignments.

## Checker

The supported run path is `python -m matrix.engine` (same report as `python -m matrix`) after `pip install -e ".[dev]"`. It validates the locked JSON and the committed gap file only. It prints `rows=67 queue=5 gap_unassigned=15` and `OK` when they pass. It does not crawl GitHub, does not expand the 67 rows, and does not assign a cluster or claim cap to the 15 unassigned names. Package version `0.1.1` is the checker; the JSON `version` field remains the snapshot label `0.1.0`.

## CI

Prior listed product workflow on `main`: run **33932359958** conclusion **success** (2026-09-05). Actions conclusion after the Sweep-175 push: run **36889001703** conclusion **success** on `e57ec52`.

## Sweep-207 name observation (2026-10-02)

Not a cap refresh. `matrix/census_gap_2026-10-02.json` records GitHub search `user:beyond-repair` `total_count=83`, `incomplete_results=false`. Set difference versus `census_gap_2026-10-01.json` is exactly `scale-functional-I` added and nothing removed. Missing-from-lock count is 16. `cluster` and `claim_cap` stay null. Locked inventory remains 67. `python -m matrix.engine` still reports the 2026-10-01 gap (`gap_unassigned=15`) and does not load the new file. Local pytest after this file: 18 passed. `scale-functional-I` was not function-audited in this pass.

## Sweep-210 function audit (2026-10-03)

Not a cap refresh. `matrix/function_audit_scale_functional_I.json` records the `scale-functional-I` head `9768280b4d6eb039defa7072cabf243f3e3740b2`. Tests import and execute `dumbbell_mask` and `perimeter` only. `main` is not executed by tests. `cluster` and `claim_cap` stay null. Locked inventory remains 67. Local witness: `python3 -m unittest tests.test_scale_functional` → 1 test OK. No continuum, selected W, thrust, or 0.08 comparison is claimed.
