# Governance — adl-capability-matrix

**Sweep:** 175 (re-audit)
**Classification:** RESEARCH
**Claim level:** 1 (dated census tool; not live SLA)
**Pre-sweep head:** `ea940fe405201855747e4d4cd9eed3816f5c9e91`

## Invariants

- This repository is a **dated JSON snapshot** plus a validator. It is not the live portfolio registry.
- Authoritative live inventory lives in `beyond-repair/ADL-Governance` (`docs/PORTFOLIO_STATUS_REPORT.md`).
- `capability_matrix.json` inventory_count stays **67** until a fresh per-row cluster/cap assignment exists. Sweep-175 did not assign those.
- `matrix/census_gap_2026-10-01.json` may list names only. Null cluster and null claim_cap are mandatory for unassigned names.
- Forbidden: claiming the matrix is complete, claiming per-function AST census, claiming runtime interop across clusters.

- The runnable surface is `python -m matrix.engine` / `python -m matrix`. It checks the committed JSON. It is not a live portfolio crawl.

## Observed tree

- `matrix/capability_matrix.json` — locked inventory_count **67** (2026-09-04 snapshot).
- `matrix/census_gap_2026-10-01.json` — 82 observed names; 15 unassigned; 0 extras.
- `matrix/load.py` + tests — deterministic load/validate plus gap set-difference.
- CI workflow present (pytest on push to `main`). Post-push conclusion: run **36889001703** success on `e57ec52`.

## Allowed agent actions

Docs, claim tokens, name-only gap files, tests. No invented rows. No ACTIVE promotion. No archive API. No release tag.
