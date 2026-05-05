# Registries and indexes

## Proposal 1

Constructing an argument requires to reason over the vault as a **graph** rather than as a flat collection of documents. The registries make the **global structure** explicit, so that the vault behaves as a **proof graph**, a **reasoning DAG**, or an **argumentation map**.

**Formats**: Maintain machine-readable indexes (YAML or JSON) which can be used simultaneously by a human supervisor, a program or an AI agent.

> [!WARNING]
> Avoid duplicating the same registry logic identically at every scale:
> - **Workspace level** contains only the project catalog and global terminology if shared across projects.
> - **Project level** contains the authoritative reasoning architecture for the project.
> - **Module level** should usually contain just a local index note, not full duplicates of the project graph.

### Types of registries

#### Reasoning graph

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
- `type`: one of the admissible note types (see [note types](vendor/gnomon/docs/rendering/note-types))
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

> [!INFO] The gating *capability* is migrated to [staleness gating](_framework-criteria#^t1-staleness-gating). The local mechanism (read `propagation_status` and refuse drafting) survives as the D `^bk-drafting-gate` in `2-architecture/validity-revision.md` Conditional on the F.

#### Open questions

**Role**: This file enumerates unresolved tasks. It serves to determine the next note, not vague intuition alone.

**Suggested structure**: Each entry contains: `id`, `priority` (high/medium/low), `question` (the open question as a sentence), `prerequisite_notes` (list of note IDs that must be completed first), `status` (pending/in-progress/done), and `blocking_reason` (why the question cannot yet be addressed).

#### Dependencies

**Role**: This file tracks reusable objects and their provenance. It helps to reduce accidental redefinition and hidden duplication. Each entry is typed, enabling the reasoning graph to distinguish what exactly is imported from a note.

**Suggested structure**: The file contains an `objects` array. Each entry has: `id`, `kind` (using the admissible import kinds from the reasoning graph), and a provenance field that depends on the kind — `defined_in` for definitions or `proved_in` for theorems and lemmas. Theorem and lemma entries additionally list their `assumptions` (array of assumption identifiers). All entries include `imported_by` (array of note IDs that use the object). This structure enables the validation toolchain to detect rederivations, orphaned objects, and missing imports.

#### Terminology

**Role**: This file keeps naming stable across notes. Terminology drift — using variant names for the same concept — silently degrades cross-note coherence and makes dependency tracking unreliable. The terminology registry is enforced by an automated linter (`tools/lint_terminology.py`) at the draft and audit stages.

**Suggested structure**: The file contains a `preferred_terms` array. Each entry has `canonical_name` (the authorized term) and `forbidden_variants` (array of strings that the linter must flag and replace).



## Proposal 2

### Types of registries

Multiple registries are needed:

| Component                       | Role                                                                              |
| ------------------------------- | --------------------------------------------------------------------------------- |
| **Identity registry**           | Maps IDs to canonical objects                                                     |
| **Type index**                  | Groups objects by type and subtype                                                |
| **Namespace registry**          | Organizes objects by module / branch / research thread                            |
| **Relation registry**           | Collects typed edges between object IDs                                           |
| **Dependency graph**            | Directed graph for justificatory and semantic dependence                          |
| **Reverse dependency index**    | Tracks downstream impact                                                          |
| **Status index**                | Groups objects by epistemic maturity (established, provisional, open, refuted...) |
| **Relevance index**             | For each target question, identifies ranked relevant objects and their roles      |
| **Terminology index**           | Tracks notations, aliases, equivalent formulations                                |
| **Version graph**               | Tracks revisions, supersession, derivation                                        |
| **Integrity report structures** | Missing links, broken references, cycles, orphan nodes                            |

The dependency graph is a **first-class, separately maintained structure** for the following reasons:

- Edges carry **semantic type**, which is irreducible to a list of identifiers.
- Edges enable **graph queries** that object-internal fields cannot: reachability (is object O on any path from any root question?), cycle detection, transitive dependency closure, identification of disconnected components (i.e., orphaned objects with no epistemic path to the root).
- The **orphan detection query** is the primary automated enforcement mechanism for epistemic necessity: any object with no directed path to a root question node is flagged as epistemically unjustified within the framework.

### Internal subdistinction

Within this layer, one distinction is essential:

| **Subtype**          | **Role**                                     | **Examples**                                                         |
| -------------------- | -------------------------------------------- | -------------------------------------------------------------------- |
| **Registries**       | Answer **lookup** questions                  | Given `DEF-014`, retrieve the object                                 |
| **Graph structures** | Answer **relational** questions              | Find all objects on a justificatory path from `ASM-003` to `ANS-002` |
| **Analytic indexes** | Answer **computed organizational** questions | Rank objects by load-bearing centrality for target `Q-001`           |

### Edge types

To avoid semantic ambiguity, at least three edge families must be distinguished:

|Edge family|Meaning|
|---|---|
|**Semantic dependence**|required to interpret a statement|
|**Justificatory dependence**|required to validate or derive a statement|
|**Inquiry relevance**|required because of the current target question or methodological route|