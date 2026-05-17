
# Validation toolchain

Registry corruption is a silent, compounding failure: it does not surface immediately but progressively degrades the agent's ability to reason about the vault's established knowledge. Validation must be **external, automated, and a hard gate** — it cannot rely on the agent's self-correction.

> [!INFO] The externality commitment ("validation cannot rely on the agent's self-correction") is migrated to [validation externality](../1-framework/research-activities-workflows#^t1-validation-externality). The layered-architecture, gating-policy, and human-review mechanisms survive as the D's `^bk-validation-architecture`, `^bk-validation-gating`, and `^bk-human-review-gate` in `2-architecture/validation-views.md` Conditional on the F.

## Architecture ^validation-architecture

> [!INFO] The *Terminology enforcement* row's canonicity *capability* is migrated to [canonical terminology](../1-framework/modular-content-organization#^t1-canonical-terminology) (pass-5 rename of "Terminology canonicity" / `^t1-terminology-canonicity`). The linter mechanism survives as the D `^bk-terminology-enforcement` in `2-architecture/validation-views.md`.

| Layer | Mechanism | Failure mode addressed |
| --- | --- | --- |
| **Schema enforcement** | JSON Schema validation on write | Field name drift, missing required fields, type errors |
| **Referential integrity** | Cross-registry ID resolution script | Dangling dependency IDs, references to non-existent notes |
| **Graph integrity** | Cycle detection on proof-dependency edges | Circular dependencies introduced silently |
| **Uniqueness checks** | ID and path uniqueness validation | Duplicate entries |
| **Status transitions** | Permitted-transition validation | Arbitrary status changes |
| **Terminology enforcement** | Linter scanning note prose against `registry/terminology.yaml` | Naming drift across notes (variant names for the same concept) |
| **Human gate** | Diff-based review of all registry mutations | Semantic errors that pass structural checks |

## Schema requirements

**Directory**: `governance/schemas/`. One JSON Schema per registry file: `reasoning_graph.schema.json`, `dependencies.schema.json`, `open_questions.schema.json`, `terminology.schema.json`. Critical properties:

- **`additionalProperties: false`** on all note entries: prevents silently accepted novel field names from a drifting agent
- **Typed imports** enforced in schema: `imports` entries must have `from`, `kind`, and `object` fields (not bare note IDs)
- **Enumerated types**: `type`, `status`, `propagation_status`, import `kind`, and output `statement_role` must be enum-constrained
- **ID format**: `^[a-z0-9-]+$` pattern on all identifiers

## Status-transition rules

Only permitted transitions are valid:

| From | Allowed transitions |
| --- | --- |
| `pending` | `in-progress` |
| `in-progress` | `done`, `pending` (with justification) |
| `done` | `revised` |
| `revised` | `done` |

Any other transition is a validation error.

## Staging area

The agent must never modify live registry files directly. All proposed updates are written to `registry/staging/`:

- `staging/note_index.yaml`
- `staging/reasoning_graph.yaml`
- `staging/dependencies.yaml`
- `staging/open_questions.yaml`

Promotion to the live `registry/` directory requires:

1. All automated validation checks pass (zero errors)
2. Human reviews the structured diff (`tools/registry_diff.py registry/ registry/staging/`) for semantic correctness:
   - Are new note IDs consistent with vault naming conventions?
   - Are status transitions legitimate?
   - Are new dependencies inferentially justified?
   - Are downstream consumer lists complete?
3. On approval: promote staging to live registry. On rejection: return specific field-level errors to the agent; repeat from step 1.
4. Confirmation validation runs against the promoted state to guard against copy errors.

## Tooling

Three scripts in `tools/`:

- **`tools/validate_registry.py`**: schema validation, ID uniqueness, path existence, referential integrity, cycle detection (on proof-dependency edges only, excluding comparisons and thematic links), status-transition validity, propagation consistency, cross-registry consistency. Exits non-zero on any failure.
- **`tools/registry_diff.py`**: produces a structured diff between `registry/` and `registry/staging/`, showing all mutations by change type (added, removed, modified) with old and new values.
- **`tools/lint_terminology.py`**: scans note Markdown files against `registry/terminology.yaml`. For each `preferred_terms` entry, searches for any `forbidden_variants` in the note prose and reports violations with the canonical replacement. Also flags terms that appear to introduce new concepts not present in the registry (heuristic: bold-defined terms or `:=` definitions whose name has no registry entry). Exits non-zero on any forbidden-variant match.