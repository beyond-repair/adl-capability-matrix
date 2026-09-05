# adl-capability-matrix

Deterministic **cluster + claim-cap** matrix for the `beyond-repair` GitHub portfolio.

## What this repository claims

- 67 public repositories were enumerated from GitHub search `user:beyond-repair` on 2026-09-04.
- Each repository is assigned a **cluster** and a **claim_cap** from metadata only (name, description, approximate size).
- A **compatible-build queue** lists systems that are compatible with existing work and are **not** claimed as already built (except `Q-001`, this repo).

## What this repository does not claim

- Per-function inventories of every repository (not performed; would require AST/read of every default-branch tree).
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

## Related

- `ADL-Portfolio-Census` — locked inventory protocol
- `aegis-repo-graph` — FLS artifact graph
- `ADL-Governance` — portfolio constitution
- `forge-aegis` — FLS / AEGIS ontology
