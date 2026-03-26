# Procedural workflows

> [!INFO] See also
> Part of the [agent instruction system](plan-agents-humain-generation.md). Related: [decision rules](../quality-criteria/decision-rules.md) — [formal contracts](formal-contracts.md) — [note types](note-types.md) — [workspace architecture](workspace-architecture.md).

## Pipeline ^pipeline-table

| Stage                                           | Action                                                                                                                                                                                                                                                                                                               | Human intervention                                                                                                            |
| ----------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| **0. Gap identification**                       | Select the next note from `open_questions.yaml` and `reasoning_graph.yaml` (not from free association).                                                                                                                                                                                                              | Check: relevance of proposed next gap, atomicity of the question, ordering of reasoning steps                                 |
| **1. Contract specification: scope commitment** | Create the contract in `contracts/active/`. Fill "Scope commitment" from registry context alone: local objective, utility, typed imports, expected contribution, excluded topics. No mathematical reasoning is required. No drafting is allowed.                                                                     | **Gate "scope"**: atomicity, inferential necessity, import correctness, contribution distinctness, absence of overlap         |
| **2. Contract specification: execution plan**   | Fill "Execution plan" after Gate "scope" approval. Requires active mathematical reasoning: minimal target result, proof strategy, admissibility table, section skeleton, termination criterion, success criterion, deliverables, audit targets.                                                                      | **Gate "execution"**: result-objective match, proof strategy non-triviality, section admissibility, termination verifiability |
| **3. Draft**                                    | Generate the full note using the validated contract and the note specification. The [mandatory drafting gate](workspace-architecture.md#^mandatory-drafting-gate) must pass before this stage begins.                                                                                                                      | Optional (e.g. delicate mathematics)                                                                                          |
| **4. Integration record**                       | Fill the post-draft integration record: validated contribution, divergence assessment, actual outputs, failure modes, downstream use confirmation, registry additions.                                                                                                                                               | Review divergence assessment if present                                                                                       |
| **5. Audit**                                    | Produce a separate audit report verifying both the note and the integration record against the contract and `governance/audits/checklists.md`. Run `tools/lint_terminology.py` against the draft note; all forbidden-variant matches must be resolved before the audit can pass.                                            | Accept or reject audit conclusions                                                                                            |
| **6. Revision**                                 | Route the note back only to the pass named by the audit report. Revision is controlled re-entry, not a free-form drafting stage: use the audit report to decide whether the next action belongs to the Architect, Derivation, or Writing pass, and preserve the contract unless the audit explicitly requires contract repair. | Optional                                                                                                                      |
| **7. Registry update**                          | Agent writes proposed updates to `registry/staging/` (never to live `registry/` directly). Automated validation runs all checks in the [validation architecture](workspace-architecture.md#^validation-architecture) via `tools/validate_registry.py`. On pass: human reviews structured diff. On approval: promote staging to live registry. | **Gate "registry"**: automated validation must pass with zero errors; human reviews diff of all mutations before promotion    |
| **8. Archive**                                  | Move the contract (Phase 1 + Phase 2 + integration record) from `contracts/active/` to `contracts/completed/`.                                                                                                                                                                                                       | None                                                                                                                          |

> [!FAIL]
> **Non-strategic elaboration**: never let the agent choose *both* the question and the scope.
> **Unconstrained revision**: the revision should use *only* the audit report to avoid endless expansion.

> [!IMPORTANT] Human intervention
> Human intervention should occur at **control points**.
> The more a note determines future architecture, terminology, or conceptual framing, the more direct human control it requires.

## Distinct agents / prompts

A productive decomposition is:

1. **Architect pass**: define the note contract and outline (concerned with scope, dependency hygiene, uniqueness, and logical role).
2. **Derivation pass**: write the mathematical proofs and arguments to actually _establish the claim_ (concerned with equations, case distinctions, counterexamples, intermediate steps — with no concern for prose).
3. **Writing pass**: convert the established derivation into pedagogical prose (concerned with exposition and writing style).
4. **Audit pass**: verify coherence against the contract.

**Pass-to-stage mapping.** The four passes cover a subset of the [pipeline](#^pipeline-table) stages. Stages outside any pass are transitional steps (gap selection, integration record, revision, registry update, archive) executed by the orchestrating agent or the human supervisor — they are not drafting passes subject to the non-interference constraints below.

| Pass | Pipeline stages covered |
| --- | --- |
| **Architect** | 0 (gap identification), 1 (scope commitment), 2 (execution plan) |
| **Derivation** | 3 (draft — mathematical content only) |
| **Writing** | 3 (draft — prose conversion only) |
| **Audit** | 5 (audit) |
| _No pass_ | 4 (integration record), 6 (revision routing), 7 (registry update), 8 (archive) |

Stage 3 is split across two passes: the Derivation pass produces the mathematical content (annotated derivation), and the Writing pass converts it into prose. Stage 4 (integration record) is a transitional step executed after the Writing pass and before the Audit pass; its responsibilities (validated contribution, divergence assessment, registry additions) are evaluative and administrative, not drafting actions. The [decision rule dispatch table](#^decision-rule-dispatch) specifies which rules each pass enforces and which rules are enforced outside the pass model.

> [!FAIL]
> **Interference**: do not require a single pass to simultaneously optimize architecture, novelty, pedagogy, and technical mathematics.
> **Importance of separation**: a model drafting and self-auditing in one pass often misses its own drift.

### Non-interference constraints

Each pass has a bounded mandate. A pass that exceeds its mandate invalidates the downstream chain.

| Pass           | May                                                                                                     | May not                                                                 |
| -------------- | ------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| **Architect**  | Define scope, imports, target result, stopping rule, section skeleton with admissibility justifications | Write final prose, invent technical derivations beyond the route sketch |
| **Derivation** | Derive claims, test assumptions, generate proof details, identify failure modes                         | Broaden scope, add new conceptual goals, rewrite the contract           |
| **Writing**    | Improve exposition, restructure paragraph flow, insert pedagogical bridges, apply style rules           | Add new claims, alter assumptions, introduce undeclared side results    |
| **Audit**      | Identify drift, omission, redundancy, invalid steps, contract violations                                | Silently repair mathematics inside the audited note                     |

If the audit pass discovers a scope violation or a mathematical gap, it must record the finding and trigger a return to the appropriate earlier pass — it must not patch the note directly.

### Handoff artifacts

Each pass produces a specific artifact that the next pass receives as input. Without specified handoff artifacts, each pass regenerates context rather than building on a stable prior output.

| Transition | Artifact produced | Format | What it must contain |
| --- | --- | --- | --- |
| Architect → Derivation | **Section skeleton** | Markdown outline with empty section bodies | For each section: heading, one primary admissibility label and any optional secondary label, one-sentence statement of what must be established, named local output, immediate downstream consumer, typed imports available for that section |
| Derivation → Writing | **Annotated derivation** | Structured proof document (not polished prose) | For each section: formal claims with labels, proof steps with justifications, assumptions used, intermediate results named, failure modes noted, major constructs with the exact later step they enable, and unit-role tags (`claim`, `derivation`, `interpretation`). No prose styling. |
| Writing → Integration | **Draft note** | Full Markdown note following the note specification | Complete note with all callouts, body sections, anchors, and cross-references. No post-draft fields are filled yet. |
| Integration → Audit | **Audit package** | Draft note plus post-draft integration record | Draft note, completed integration record, and the pre-draft specification used as the audit baseline. |
| Audit → Revision | **Audit report** | Structured report following audit template | For each finding: location, violation type, severity, which contract field is violated, recommended action (revise / excise / defer / return to earlier pass) |

**Return triggers.** When the audit pass identifies a problem, the return target depends on the violation type:

| Violation type | Return to |
| --- | --- |
| Scope violation (undeclared result, lateral drift) | Architect pass (contract must be amended or note split) |
| Mathematical gap or invalid step | Derivation pass (proof must be repaired) |
| Style or structure violation | Writing pass (exposition must be revised) |
| Contract field inconsistency | Architect pass (specification must be corrected) |

Stage 6 produces no independent artifact beyond the audit report. It routes that report, together with the current draft package, back to the pass named in the table above; the resumed pass then receives its normal governance files in addition to the audit findings.

### Context injection protocol ^context-injection-protocol

Passing all governance files to every pass saturates the context window with low-relevance material, degrades attention on the operative constraint (the contract), and produces inconsistent weighting between global and local rules. Decision rules are therefore delivered through pass-specific file injection rather than restated globally at every stage.

| Pass | Binding inputs delivered to the pass | Reference inputs the pass may read | Output artifact the pass may write |
| --- | --- | --- | --- |
| **Architect** | project-local `governance/project_scope.md`, relevant note spec from `governance/specs/`, relevant contract template from `governance/contracts/` | `registry/reasoning_graph.yaml`, `registry/open_questions.yaml`, `registry/dependencies.yaml` | pre-draft specification: Phase 1, then Phase 2 after Gate 1 |
| **Derivation** | `governance/rules/mathematical_standards.md`, the validated pre-draft specification | imported dependencies: source notes for declared typed imports only | annotated derivation |
| **Writing** | `governance/rules/writing_principles.md`, `registry/terminology.yaml`, the validated pre-draft specification, relevant note spec from `governance/specs/` | annotated derivation | draft note |
| **Audit** | `governance/audits/checklists.md`, `governance/audits/report_template.md`, the validated pre-draft specification, `registry/terminology.yaml` | draft note, integration record, `registry/reasoning_graph.yaml` for downstream consumer verification | audit report |

**Transitional stages.** Stage 4 (integration record) is not a pass but receives the relevant contract template from `governance/contracts/` (post-draft section), the pre-draft specification, and the completed draft note; it outputs the audit package consumed by the Audit pass. Stage 6 (revision) does not have a fixed governance bundle of its own: it receives the audit report and the current draft package, then dispatches back to the Architect, Derivation, or Writing pass named by the return-trigger table above. Stages 7–8 (registry update, archive) receive registry files and the completed contract.

**Orchestration files.** `AGENTS.md` and the `governance/workflow/` directory are loaded by the orchestrating agent at session start to determine the pipeline sequence and pass dispatch. They are not injected into individual passes — each pass receives only the governance files listed above.

**Invariant**: the pre-draft specification is available to every pass and transitional stage after the architect pass, since it is the binding constraint. All other files are pass-specific.

### Decision rule dispatch ^decision-rule-dispatch

The dispatch tables mirror the three-layer structure of the [decision rules](../quality-criteria/decision-rules.md): a full table for **epistemic rules** (the generation-time criteria), then a compact table for **operators and workflow routing** across all layers.

**Authority.** All tables are cross-cutting summaries derived from the "Enforcement" subsections within the [rule definitions](../quality-criteria/decision-rules.md). Those subsections remain authoritative. When updating enforcement logic, update the rule definition first, then keep the dispatch tables consistent.

**Epistemic rules**

| Rule | Governing question | Carrying file | Architect | Derivation | Writing | Audit |
| --- | --- | --- | --- | --- | --- | --- |
| [Objective unity](../quality-criteria/decision-rules.md#^atomicity-criterion) | Does this note pursue exactly one inferential objective? | type-specific contract / `audits/checklists.md` | Phase 1: require one local objective. Phase 2: record each section's output and downstream consumer and reject skeletons whose output-consumer pair differs materially from the note-level pair. | return to architect if a proof branch produces an output for a materially different downstream consumer | — | verify note-level unity; use the [section-level dependency-cone test](../quality-criteria/decision-rules.md#^drift-detection) |
| [Local necessity](../quality-criteria/decision-rules.md#^admissibility-rule) | Does this content unit need to be here once the objective is fixed? | type-specific contract / `writing_principles.md` / `audits/checklists.md` | Phase 2: admissibility table for planned sections with one primary label per section | keep only proof steps and cases that advance the contracted result | map each paragraph to a skeleton step and one primary admissibility label; do not write unmapped paragraphs; apply the [interpretive sub-criterion](../quality-criteria/decision-rules.md#^bounded-interpretive-radius) to interpretive paragraphs | verify section admissibility; apply the [removal test](../quality-criteria/decision-rules.md#^drift-detection) to local content; flag interpretation that fails the [interpretive sub-criterion](../quality-criteria/decision-rules.md#^bounded-interpretive-radius) |
| [Functional motivation](../quality-criteria/decision-rules.md#^functional-motivation) | May this major construct be introduced? | `mathematical_standards.md` / `writing_principles.md` / `audits/checklists.md` | — | apply the template when introducing any major construct and record the exact later step it enables | preserve the enabled-step link in prose | verify every major construct has functional justification |
| [Proof strategies](../quality-criteria/decision-rules.md#^proof-strategies) | Is a non-trivial proof allowed to proceed without an explicit route, proof family, and [explanatory target](../quality-criteria/decision-rules.md#^explanatory-target)? | `mathematical_standards.md` / type-specific contract / `audits/checklists.md` | Phase 2: fill and validate the proof-strategy schema, including the proof family and explanatory target | follow the committed proof family and route; hold the explanatory target in working memory; verify at derivation end that the completed derivation supports the committed target through family-appropriate forward construction; return if the route broadens | — | check that the delivered proof matches the committed family and route; verify that the derivation reveals the committed structural mechanism; flag verificational patterns |
| [Premise legitimacy](../quality-criteria/decision-rules.md#^premise-legitimacy) | Is every non-trivial premise either proved locally or declared as an import? | type-specific contract / `writing_principles.md` / `audits/checklists.md` | Phase 1: declare typed imports and rederivation prohibitions. Phase 2: verify every premise in the proof strategy is accounted for | use only locally proved claims or declared imports; do not introduce hidden premises | enforce the background-restatement criterion on every imported result | flag hidden premises, rederivations, and unnecessary background recall |

**Operators and workflow routing**

| Operator | Layer / specializes | Stage focus | Function |
| --- | --- | --- | --- |
| [Side-result criterion](../quality-criteria/decision-rules.md#^forbid-free-expansion) | Epistemic / [Local necessity](../quality-criteria/decision-rules.md#^admissibility-rule) | Draft, Revision | Contract-authorization criterion: defers side results that pass local necessity but are not authorized by the contracted skeleton, target result family, or declared deliverables |
| [Retention audit operator](../quality-criteria/decision-rules.md#^drift-detection) | Epistemic / [Local necessity](../quality-criteria/decision-rules.md#^admissibility-rule) + [Objective unity](../quality-criteria/decision-rules.md#^atomicity-criterion) | Audit, Revision | Test A applies the removal test to local content; Test B compares each section's dependency signature to the main result path; Test C runs a triggered overlap check using the unit-rank tie-break order |
| [Deductive continuity](../quality-criteria/decision-rules.md#^deductive-articulation) | Argumentative | Architect, Draft, Audit | Section-level logical dependency: each section names the specific output from a preceding section that it uses as input. Problem-structure correspondence: the skeleton declares one admissible decomposition pattern and uses it consistently |
| [Claim / derivation / interpretation separation](../quality-criteria/decision-rules.md#^claim-derivation-interpretation-separation) | Argumentative | Derivation, Writing, Audit, Revision | Three roles (claim, derivation, interpretation) must remain distinct; the annotated derivation marks unit roles before prose drafting; audit flags mixed-role prose |
| [Divergence resolution](../quality-criteria/decision-rules.md#^divergence-resolution) | Workflow routing | Integration, Audit | Classifies post-draft divergence between expected and validated contribution and routes the required correction |

**Reading the tables.** The epistemic table identifies the generation-time criteria that should remain salient during planning and drafting. The second table lists operators, argumentative checks, and workflow routing that implement or verify those criteria in narrower contexts or at later stages; they should not be injected as if they were coequal generation-time criteria.
