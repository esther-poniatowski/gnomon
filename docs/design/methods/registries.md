# Registries and validation

> [!INFO] See also
> Part of the [agent instruction system](plan-agents-humain-generation.md). Related: [decision rules](../quality-criteria/decision-rules.md) — [workspace architecture](workspace-architecture.md) — [procedural workflows](procedural-workflows.md).

## Overview

To construct an argument, the agent must reason over the vault as a graph rather than as a flat collection of documents. The registries make the **global structure** explicit, so that the vault behaves as a **proof graph**, a **reasoning DAG**, or an **argumentation map**.

**Formats**: Maintain machine-readable indexes (YAML or JSON) which can be used both by the human supervisor and by the agent.

> [!WARNING]
> Avoid duplicating the same registry logic identically at every scale:
> - **Workspace level** contains only the project catalog and global terminology if shared across projects.
> - **Project level** contains the authoritative reasoning architecture for the project.
> - **Module level** should usually contain just a local index note, not full duplicates of the project graph.

## Registry files

### Reasoning graph

**File**: `registry/reasoning_graph.yaml`

**Role**: This file encodes the inferential architecture.

**Suggested structure**:

- note ID and locations
- type
- status
- local objective
- **typed imports** (not bare note references — each import specifies the source note, the kind of object imported, the object name, and optionally its exact use inside the note)
- **typed outputs** (each output specifies an ID, an object type, and a statement role)
- downstream consumers (notes that use its results)
- overlap warnings

A note rarely depends on another note as a whole. It depends on a definition, a theorem, a notation convention, an assumption schema, a proof pattern, a counterexample, or a construction. Without typed imports, the dependency list is a citation list, not an inferential map. Coarse dependencies are one of the main causes of accidental overlap and hidden rederivations.

**Admissible import kinds** ^admissible-import-kinds: `definition`, `theorem`, `lemma`, `notation`, `assumption`, `construction`, `counterexample`, `proof_pattern`, `criterion`.

**Admissible output types** ^admissible-output-types: `theorem`, `lemma`, `definition`, `criterion`, `construction`, `counterexample`, `interpretation`.

**Admissible statement roles** ^admissible-statement-roles: `structural` (establishes an internal mechanism), `operational` (provides a diagnostic, test, or applicable rule), `boundary` (delimits scope or identifies failure).

**Per-note entry fields.** The file opens with a `project` block containing `main_question` and `main_outputs`. The `notes` array contains one entry per note with the following fields:

- `id`, `path`, `contract`, `audit`: identification and file locations
- `type`: one of the admissible note types (see [note types](note-types.md))
- `status`: `pending`, `in-progress`, `done`, or `revised`
- `question`: the note's local objective as a question
- `expected_contribution`, `validated_contribution`, `divergence`: contribution tracking (pre-draft vs. post-draft)
- `imports`: array of typed imports, each with `from` (source note ID), `kind` (from the admissible import kinds above), `object` (name), and optionally `used_for` (role in the current note)
- `outputs`: array of typed outputs, each with `id` (namespaced, e.g., `result.block_decomposition`), `type` (from admissible output types), and `statement_role` (from admissible statement roles)
- `consumers`: array of downstream note IDs
- `revision_history`: change log

**Upstream instability propagation.** When a completed note is revised, downstream consumers may silently inherit stale premises. The reasoning graph must track this explicitly. When a note's status changes to `revised`, three fields are added: `revision_note` (what changed), `downstream_affected` (list of consumer note IDs), and `propagation_status`.

`propagation_status` values:
- **unresolved**: the revision has not been checked against downstream consumers
- **checked**: downstream consumers have been inspected; some require revision
- **cleared**: all downstream consumers have been confirmed or updated

**Mandatory drafting gate.** Before any drafting pass begins, the agent must check whether any declared import has `propagation_status: unresolved` in the reasoning graph. If so, drafting is blocked until the upstream instability is resolved (by confirming that the downstream note's argument remains valid under the revised premise, or by revising the downstream note). ^mandatory-drafting-gate

### Open questions

**File**: `registry/open_questions.yaml`

**Role**: This file enumerates unresolved tasks. It serves to determine the next note, not vague intuition alone.

**Suggested structure**: Each entry contains: `id`, `priority` (high/medium/low), `question` (the open question as a sentence), `prerequisite_notes` (list of note IDs that must be completed first), `status` (pending/in-progress/done), and `blocking_reason` (why the question cannot yet be addressed).

### Dependencies

**File**: `registry/dependencies.yaml`

**Role**: This file tracks reusable objects and their provenance. It helps to reduce accidental redefinition and hidden duplication. Each entry is typed, enabling the reasoning graph to distinguish what exactly is imported from a note.

**Suggested structure**: The file contains an `objects` array. Each entry has: `id`, `kind` (using the admissible import kinds from the reasoning graph), and a provenance field that depends on the kind — `defined_in` for definitions or `proved_in` for theorems and lemmas. Theorem and lemma entries additionally list their `assumptions` (array of assumption identifiers). All entries include `imported_by` (array of note IDs that use the object). This structure enables the validation toolchain to detect rederivations, orphaned objects, and missing imports.

### Terminology

**File**: `registry/terminology.yaml`

**Role**: This file keeps naming stable across notes. Terminology drift — using variant names for the same concept — silently degrades cross-note coherence and makes dependency tracking unreliable. The terminology registry is enforced by an automated linter (`tools/lint_terminology.py`) at the draft and audit stages.

**Suggested structure**: The file contains a `preferred_terms` array. Each entry has `canonical_name` (the authorized term) and `forbidden_variants` (array of strings that the linter must flag and replace).

## Validation toolchain

Registry corruption is a silent, compounding failure: it does not surface immediately but progressively degrades the agent's ability to reason about the vault's established knowledge. Validation must be **external, automated, and a hard gate** — it cannot rely on the agent's self-correction.

### Architecture ^validation-architecture

| Layer | Mechanism | Failure mode addressed |
| --- | --- | --- |
| **Schema enforcement** | JSON Schema validation on write | Field name drift, missing required fields, type errors |
| **Referential integrity** | Cross-registry ID resolution script | Dangling dependency IDs, references to non-existent notes |
| **Graph integrity** | Cycle detection on proof-dependency edges | Circular dependencies introduced silently |
| **Uniqueness checks** | ID and path uniqueness validation | Duplicate entries |
| **Status transitions** | Permitted-transition validation | Arbitrary status changes |
| **Terminology enforcement** | Linter scanning note prose against `registry/terminology.yaml` | Naming drift across notes (variant names for the same concept) |
| **Human gate** | Diff-based review of all registry mutations | Semantic errors that pass structural checks |

### Schema requirements

**Directory**: `governance/schemas/`. One JSON Schema per registry file: `reasoning_graph.schema.json`, `dependencies.schema.json`, `open_questions.schema.json`, `terminology.schema.json`. Critical properties:

- **`additionalProperties: false`** on all note entries: prevents silently accepted novel field names from a drifting agent
- **Typed imports** enforced in schema: `imports` entries must have `from`, `kind`, and `object` fields (not bare note IDs)
- **Enumerated types**: `type`, `status`, `propagation_status`, import `kind`, and output `statement_role` must be enum-constrained
- **ID format**: `^[a-z0-9-]+$` pattern on all identifiers

### Status-transition rules

Only permitted transitions are valid:

| From | Allowed transitions |
| --- | --- |
| `pending` | `in-progress` |
| `in-progress` | `done`, `pending` (with justification) |
| `done` | `revised` |
| `revised` | `done` |

Any other transition is a validation error.

### Staging area

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

### Tooling

Three scripts in `tools/`:

- **`tools/validate_registry.py`**: schema validation, ID uniqueness, path existence, referential integrity, cycle detection (on proof-dependency edges only, excluding comparisons and thematic links), status-transition validity, propagation consistency, cross-registry consistency. Exits non-zero on any failure.
- **`tools/registry_diff.py`**: produces a structured diff between `registry/` and `registry/staging/`, showing all mutations by change type (added, removed, modified) with old and new values.
- **`tools/lint_terminology.py`**: scans note Markdown files against `registry/terminology.yaml`. For each `preferred_terms` entry, searches for any `forbidden_variants` in the note prose and reports violations with the canonical replacement. Also flags terms that appear to introduce new concepts not present in the registry (heuristic: bold-defined terms or `:=` definitions whose name has no registry entry). Exits non-zero on any forbidden-variant match.
