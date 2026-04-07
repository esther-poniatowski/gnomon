# Formal contracts

> [!INFO] See also
> Part of the [agent instruction system](plan-agents-humain-generation.md). Related: [decision rules](../quality-criteria/decision-rules.md) — [note types](note-types.md) — [procedural workflows](procedural-workflows.md) — [workspace architecture](workspace-architecture.md).

## Overview

**Valid unit of work**: Each note should be generated from a compact specification, which defines:

**Contents** (see [contract template](#^contract-template)):

- **Scope** → the note must be organized around one **local inferential objective** (see [atomicity criterion](../quality-criteria/decision-rules.md#^atomicity-criterion))
- **Utility** → the note must state why it is necessary in the global argument (e.g. for downstream consumers or as the natural continuation / specialization of upstream analyses)
- **Contribution control** → the note must declare its expected contribution _before_ drafting (binding scope constraint), then record the validated contribution _after_ drafting; any divergence triggers a classified audit event with determinate resolution rules
- **Main result family** → the note must declare one main result and optional tightly coupled variants (not independent results)
- **Dependencies allowed** → the note must use only declared dependencies
- **Dependencies forbidden to rederive** → the note must specify which concepts are excluded pre-requisites to avoid drifts and overlaps
- **Admissibility** → every section must satisfy at least one admissibility condition
- **Success criterion** → defined by downstream importability (see contract template)
- **Termination criterion** → stated as a conjunction of verifiable conditions

## Contract template ^contract-template

**Directory**: `governance/contracts/` (one template per note type, e.g., `result_contract.md`, `tool_contract.md`)

**Type-specific fields.** Different note types require different deliverables, proof strategy depth, and admissibility criteria. A result note contract requires a proof strategy and explanatory target; a problem note contract requires an expected output format; a synthesis note contract requires imported ingredients. The Architect pass receives the relevant contract template as a binding input alongside the note specification.

**Role**: Each new note must begin with filling the pre-draft specification from the appropriate contract template and placing it in `contracts/active/`. After drafting and audit, the post-draft integration record is appended. The pre-draft specification should be precise enough that two different agents would produce roughly the same inferential object. The post-draft record captures what was actually established and feeds registry updates.

**Structure**: The contract is split into two objects: a **pre-draft specification** (filled before drafting, binding) and a **post-draft integration record** (filled after drafting, evidential). This prevents the agent from ceremonially filling post-hoc fields before the result is actually established, which yields fictitious precision in the planning phase.

**Structural redundancy elimination.** The contract fields are organized into dimensions that govern distinct aspects of the note. Every field satisfies three properties simultaneously:

1. **Unique governing question**: no two fields answer the same question
2. **Unique authoring stage**: each field is filled at exactly one stage (pre-draft, post-draft, or audit)
3. **Primary consumer with authorized readers**: each field has one pass or downstream use that governs why the field exists, while other passes may read it without redefining or overwriting it

Conflicts between fields become impossible by construction rather than resolved by priority rule.

| Overlapping pair (old template) | Resolution |
| --- | --- |
| "Minimal target result" vs. "Unique contribution" | Target result states *what is proven* (the formal proposition); contribution states *why the note must exist* (its novelty relative to the vault). Orthogonal. |
| "Success criterion" vs. "Termination criterion" | Termination governs the *drafting pass* (when to stop writing); success governs the *audit pass* and downstream consumers (when the result is fit for use). Different agents, different stages. |
| "Deliverables" vs. "Minimal target result" | Target result is a *mathematical object*; deliverables is a *structural checklist* of required note sections. Different levels. |
| "Proof strategy" in contract vs. standalone decision rule | The standalone rule in `governance/rules/mathematical_standards.md` defines the *schema*; the contract field is the *instantiation* for this note. Single point of authority. |

The pre-draft specification uses **staged filling**: one artifact, two phases, with a human validation gate between them. Phase 1 requires only registry context. Phase 2 requires active mathematical reasoning and cannot begin until Phase 1 is validated. This prevents shallow commitment on the harder fields while eliminating the duplicate "outline" artifact.

### Pre-draft specification

The pre-draft specification opens with a **Metadata** block: `ID`, `Type` (note type), `Path`, and `Status` (`phase-1` | `phase-2` | `drafting` | `audit` | `stable`).

#### Phase 1 — Scope commitment

Filled from registry context alone (reasoning graph, project scope, open questions). Requires no mathematical reasoning. Human validation is required before Phase 2 may begin.

Phase 1 contains the following fields:

- **Parent question.** The broader question this note serves within the global argument.
- **Local objective.** The single, precisely bounded question this note answers. The formulation must be such that a yes/no or a formal proposition constitutes a complete answer.
- **Utility.** Why this note must exist in the global argument — for which downstream consumers, or as the natural continuation of which upstream analyses.
- **Typed imports.** A table with columns: source note, kind (using the [admissible import kinds](workspace-architecture.md#^admissible-import-kinds) enum), object name, and what the import is used for in this note.
- **Imports forbidden to rederive.** A table listing source note, kind, and object for each import that must not be re-derived locally.
- **Expected contribution.** One sentence stating the inferential advance this note provides relative to the existing vault — what it adds that no existing note provides. Does not restate the proposition; states its novelty relative to declared dependencies. This field is **binding**: drafting must remain within the same local inferential objective and must not introduce an independent advance not authorized by the contract.
- **Excluded nearby topics.** List of topics explicitly outside scope.

**Gate 1 — Human validation of scope commitment.** The human verifies: (1) the local objective is genuinely atomic, (2) the utility statement is inferentially necessary rather than merely topically adjacent, (3) the declared imports are correct and sufficient, (4) the expected contribution is distinct from existing vault content.

#### Phase 2 — Execution plan

Filled after Phase 1 is validated. Requires active mathematical reasoning. Human validation is required before drafting may begin.

Phase 2 contains the following fields:

- **Minimal target result.** The formal proposition to be established: its type (lemma / theorem / construction), its assumptions, and its conclusion. Does not state why the vault needs it — that belongs in Expected contribution (Phase 1). Includes a **main result family**: the main result and optional tightly coupled variants. Any result outside the declared family is peripheral unless required for the proof of a central result or for an immediate downstream use declared in the contract.
- **Proof strategy.** ^contract-proof-strategy Instantiates the [proof strategy schema](../quality-criteria/decision-rules.md#^proof-strategy-schema). The eight fields are: Proof family, Objective, Obstacle, Route, Key idea, Essential assumptions, Why this route over nearby alternatives, and Explanatory target (one sentence: "The derivation reveals that [result] holds because [structural reason]," where the structural reason names a mathematical property whose absence would make the result fail).
- **Admissibility.** Instantiates the [local necessity rule](../quality-criteria/decision-rules.md#^admissibility-rule). A table mapping each planned section to one primary admissibility condition and any optional secondary condition. Any section satisfying none must be removed or deferred.
- **Section skeleton.** Instantiates the [deductive continuity rule](../quality-criteria/decision-rules.md#^deductive-articulation) and the sharpened [objective unity test](../quality-criteria/decision-rules.md#^atomicity-criterion). Lists the required sections in order; for each, states its local inferential role, its named local output, its immediate downstream consumer, and (after the first) the specific output from a preceding section it uses as input. No prose drafting or argument development is permitted here. Must identify one admissible decomposition pattern and justify why the skeleton mirrors the problem's natural structure rather than being imposed by topic, discovery order, or a generic pattern.
- **Termination criterion.** Governs the **drafting pass**: the precise condition under which the agent must stop. Stated as a conjunction of verifiable conditions, including at minimum: (1) the target result is stated as a formal proposition, (2) the proof is complete, (3) at least one failure mode is addressed, (4) the operational interpretation is written, (5) no section exists that is not demanded by the contract, (6) no concept outside declared imports has been introduced. Additional contract-specific conditions may be added.
- **Success criterion.** Governs the **audit pass** and downstream consumers: the condition under which a later note can import the result without re-examination. Stated as: "A downstream note may import [result name] provided assumptions X and Y hold in its context."
- **Deliverables.** A structural checklist of required output sections (not mathematical content): main proposition with assumptions, proof, failure mode or limitation, operational interpretation, net contribution sentence. May include admissible companion outputs (variant comparison, additional interpretation for a specific downstream consumer).
- **Audit targets.** What the audit pass must specifically verify beyond the standard checklists.

**Gate 2 — Human validation of execution plan.** The human verifies: (1) the minimal target result matches the local objective exactly, (2) the proof strategy is non-trivial and names an appropriate proof family, (3) the section skeleton contains only sections demanded by the contract and each section's output-consumer pair remains on the main result path, (4) the termination criterion is stated as verifiable conditions rather than prose intent.

### Post-draft integration record

Filled after drafting. This object records what was actually established and feeds the registry update. No field may duplicate or contradict a pre-draft field — it records outcomes, not intentions.

The integration record contains the following sections:

- **Validated contribution.** One sentence stating the inferential advance actually established by the note.
- **Divergence assessment** (filled only if validated ≠ expected). Contains: discrepancy class (`sharpening` / `weakening` / `lateral drift` / `scope expansion`), what changed and why, whether the termination criterion was respected, downstream impact, and resolution. The [divergence resolution rules](../quality-criteria/decision-rules.md#^divergence-resolution) determine the appropriate action.
- **Actual outputs.** A table with columns: Output ID, Type (using [admissible output types](workspace-architecture.md#^admissible-output-types)), Statement role (using [admissible statement roles](workspace-architecture.md#^admissible-statement-roles)), and Anchor (block reference in the note).
- **Failure modes identified.** List of failure modes or limitations discovered during drafting.
- **Downstream uses confirmed.** For each consumer note: whether it can import the output directly, or whether adaptation is needed.
- **Registry additions.** Objects to add to `registry/dependencies.yaml`, notes to update in `registry/reasoning_graph.yaml`, and new questions for `registry/open_questions.yaml`.
- **Audit status.** Audit report path, outcome (`pass` / `revision required`), and outstanding issues.
