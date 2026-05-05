# Framework-level criteria

> [!INFO] Status
> Output of [Step A.3](_refactor-handoff#^step-a3) of the refactoring plan. This file is the canonical reference for every framework-level (T1) criterion of the gnomon framework. The legacy thematic files in the `1-framework/` folder remain in place during Step A.3; their bodies are migrated here, and each legacy file carries a `> [!INFO] Migrated to ...` callout pointing to the new home. Inbound-reference redirects from the legacy anchors are deferred to [Step C](_refactor-handoff#^step-c).

> [!TIP] Reading order
> Criteria are grouped by conceptual theme. Within each group, foundational F's appear before derived ones. Cross-group dependencies flow downward: *Adequacy and Expressivity* sets the content range; *Reasoning quality* refines what the recorded reasoning must satisfy; *Understanding and Manipulability* fixes what readers can do with it; *Operationality* constrains what gets recorded; *Modularity and Separation of concerns* governs how content is composed; *Cost and Ergonomics* bounds the price; *Workflow integrity* governs how the framework is used at run time.

---

## Adequacy and Expressivity

The content axis: which aspects of research reasoning the framework must capture, and at what depth.

### Research faithfulness ^t1-research-faithfulness

The framework captures **genuine research reasoning**, not a stylized substitute. A representation is adequate only if it tracks what researchers actually do: identify a deficiency, perform an inferential move, license it under a warrant, and articulate the resulting epistemic gain.

**Failure mode prevented.** A formalism that constrains every move to a single regime (e.g., classical deduction) silently excludes the bulk of research practice — abductive jumps, semi-formal sketches, conceptual reformulations — and so misrepresents the inquiries it claims to record.

**Upstream dependencies.** None at the framework level. This is the root content-adequacy criterion.

**Downstream consequences.**

- The reasoning-structure theme partitions inferential progression along the four-way `(lack / move / warrant / gain)` axis (a decision rather than a desideratum, recorded as the chosen partition under this F).
- [Object-kind taxonomy fidelity](object-kinds#^t2-ontology-content-fidelity) traces upstream to this F: the kind set must cover the system's substantive content without omission or distortion.
- [Subtype safety](object-kinds#^t2-ontology-subtype-safety) traces upstream: subtype labels must not silently imply substitutability between kinds with different reasoning roles.
- [Move coverage](object-kinds#^t2-move-coverage) traces upstream to this F at the operations grain: the operation library must span every epistemic move the framework supports. The classification table records the edge as "Consequence of `^t1-epistemic-adequacy`" (the prior anchor name for this F).
- All three reasoning-quality F's ([no circular reasoning](#^t1-no-circular-reasoning), [no silent incompleteness](#^t1-no-silent-incompleteness), [mixed monotonicity](#^t1-mixed-monotonicity)) are sub-conditions of this F: each names a way the recorded reasoning could fail to track real reasoning.

### Reasoning-types coverage ^t1-reasoning-types-coverage

The framework admits the **range of reasoning regimes** that research actually employs:

- mathematical proofs (monotonic, rule-governed, deductive),
- informal theoretical reasoning (conceptual analysis, distinction-making, reformulation),
- empirical arguments (evidence-based, defeasible, probabilistic),
- abductive and exploratory reasoning (hypothesis generation, serendipitous discovery),
- analogical reasoning (cross-domain transfer of structure).

**Failure mode prevented.** A framework that admits only deductive moves forces empirical and abductive content into a deductive shape that distorts both. Real research mixes regimes within a single inquiry.

**Upstream dependencies.** [Research faithfulness](#^t1-research-faithfulness) — without coverage across regimes the framework cannot capture genuine research.

**Downstream consequences.**

- [Mixed monotonicity](#^t1-mixed-monotonicity) follows: when monotonic and defeasible regimes co-exist, the framework specifies how they compose at boundaries.
- The warrant-kind enum and the defeasibility combination rule in the validity-revision theme realise this F at the per-edge grain.

### Rich prose expressivity ^t1-rich-prose-expressivity

The framework supports **rich prose alongside structured fields**. Notes carry mathematical formulas, multi-paragraph derivations, diagrams, and free-form commentary, not only schema-checkable atoms.

**Failure mode prevented.** A representation that admits only typed fields and short scalar values cannot host the substantive content of research: derivations, conceptual discussions, worked examples. Forcing such content into structured fields either truncates it or scatters it across many opaque atoms.

**Upstream dependencies.** [Research faithfulness](#^t1-research-faithfulness) — research artefacts include prose; an adequate framework must accept prose as a first-class content kind.

**Downstream consequences.**

- Constrains [field typing](object-kinds#^t2-field-typing) — the admissible field shapes must include rich-text bodies.
- Constrains the [object-kind admission test](object-kinds#^t2-object-kind-admission) — kinds whose canonical content is prose remain admissible.
- Constrains canonical-vs-exposition encoding — both layers must support prose, with exposition layer taking the larger share.

### Partial formalization tolerance ^t1-partial-formalization

Annotation depth is **per-object, not per-framework**. For any object, some aspects may be left unannotated; the framework specifies which annotations are mandatory, which are optional, and which formal guarantees degrade under relaxation.

**Failure mode prevented.** A binary all-or-nothing demand (either every object is fully formalized or the framework offers no guarantees) is incompatible with real research, which advances by gradually formalizing partially specified objects.

**Upstream dependencies.** [Research faithfulness](#^t1-research-faithfulness) — research operates on partially specified objects.

**Downstream consequences.**

- The partial-formalization profile open D in the validity-revision theme answers *which profiles are admissible* under this F.
- In tension with [reasoning understandability](#^t1-reasoning-understandability) per `^t2-x2`: deeper formalization improves the recoverability of reasoning at the cost of authoring overhead.
- In tension with [goal-driven reasoning](#^t1-goal-driven-reasoning) per `^t2-x2` (same tradeoff at the motivation grain).

---

## Reasoning quality

Sub-conditions of [research faithfulness](#^t1-research-faithfulness) that name specific defects the framework must prevent.

### No circular reasoning ^t1-no-circular-reasoning

A step's justification cannot **ultimately rest on itself**. The justification chain through `supports` and warrant-bearing edges, traced from any node, must not return to that node.

**Failure mode prevented.** Circular justification — A licenses B, B licenses A — appears valid locally but provides no epistemic content. Without an explicit prohibition, the framework cannot detect the failure.

**Upstream dependencies.** [Research faithfulness](#^t1-research-faithfulness) — circular justification falsifies the representation.

**Downstream consequences.**

- The snapshot DAG acyclicity property `^t2-snapshot-dag-property` (a refinement on the [relational graph representation](relations-graph#^t2-relational-graph-representation)) is the chosen mechanism that realises this F at the graph grain.
- In tension with [revision semantics](#^t2-revision-semantics) per `^t2-x4` (revision history is cyclic; resolution is the snapshot-vs-history slicing).

### No silent incompleteness ^t1-no-silent-incompleteness

The framework lets validators **detect silently incomplete reasonings**: chains whose conclusion secretly relies on an unstated hypothesis or an undischarged assumption.

**Failure mode prevented.** A proof that appears closed but depends on a tacit assumption is the canonical failure of research writing. Without an explicit accounting mechanism, downstream readers cannot tell which assumptions remain open.

**Upstream dependencies.** [Research faithfulness](#^t1-research-faithfulness).

**Downstream consequences.**

- The open D `^t3-assumption-discharge-mechanism` (in the arguments-reasoning theme) selects how the framework handles assumed nodes — three candidate paths (eliminate by downstream proof, absorb into the conclusion as a hypothesis, flag as unresolved residue).
- Pairs with [no circular reasoning](#^t1-no-circular-reasoning): both name structural defects of the justification graph that the validator must surface.

### Revision semantics ^t2-revision-semantics

The framework **represents how reasoning states are revised** when sub-arguments fail, assumptions are weakened, or goals are reformulated. Without this, the framework records completed reasoning only, not research reasoning in progress.

**Failure mode prevented.** A representation that captures only stable end-states of reasoning silently discards the trajectory by which inquiry reached them — the failed sub-arguments, the weakened assumptions, the reformulated goals. Subsequent readers cannot reconstruct why the final form was chosen, and downstream activity cannot detect when an upstream revision invalidates dependent work.

**Upstream dependencies.** [Research faithfulness](#^t1-research-faithfulness) — research reasoning is revisable by construction; an adequate framework must capture revision events.

**Downstream consequences.**

- The forward-edge / revision-edge / propagation specification becomes T2 decisions in the validity-revision theme, absorbed by `^t2-revision-feedback` and its sub-decisions.
- In tension with [no circular reasoning](#^t1-no-circular-reasoning) per `^t2-x4` (revision history is cyclic; resolution is the snapshot-vs-history slicing — snapshots stay acyclic, history records the revision trace).
- The dependent-flagging D `^t2-dependent-flagging` realises propagation at the registry grain. Both `^t2-dependent-flagging` and [staleness gating](#^t1-staleness-gating) are downstream of this F via separate paths recorded in the classification table; the framework table does not record a direct edge between them.

> [!INFO] Anchor convention
> This F retains its original anchor `^t2-revision-semantics` per the classification-table directive (line 104, `F (T1, kept)`). The `^t2-` prefix is a historical artefact of the pre-extraction location; the F itself is framework-level and binds the architecture as a whole.

### Mixed monotonicity ^t1-mixed-monotonicity

Mixed reasoning — combining monotonic and defeasible regions — is **admissible**, and the **boundary behaviour is specified**. A defeasible step that feeds a deductive step does not silently inherit deductive certainty; a deductive step downstream of a defeasible step inherits the latter's defeat conditions.

**Failure mode prevented.** A framework that classifies every regime as monotonic or defeasible at the inquiry grain forces the author to choose one regime per inquiry, suppressing the boundary behaviour where most research errors occur. (The binary classification is already covered by the warrant-kind enum and the defeasibility combination rule; the genuine F is the interface requirement at boundaries.)

**Upstream dependencies.** [Reasoning-types coverage](#^t1-reasoning-types-coverage) — without multiple regimes there is no boundary to govern.

**Downstream consequences.**

- The defeasibility combination rule in the validity-revision theme implements this F at the per-edge grain.
- The warrant-kind enum (in `warrant-vocabulary.md`) is the closed list of admissible warrant labels, each tagged monotonic or defeasible so that the boundary computation is total.

---

## Understanding and Manipulability

The framework records reasoning so that downstream readers and tools can recover, compare, compress, and diagnose it. These F's name what readers and tools must be able to *do*.

### Goal-driven reasoning ^t1-goal-driven-reasoning

Every reasoning step is **explicitly goal-oriented**. No step is admitted on free or topical grounds; each step names the local target it addresses, the move it performs, and why this move is preferable now to a salient alternative.

**Failure mode prevented.** A reasoning chain whose individual steps are valid but whose composition is unmotivated reads as arbitrary. The reader cannot distinguish strategically necessary moves from incidental detours.

**Upstream dependencies.** [Research faithfulness](#^t1-research-faithfulness) — research reasoning is goal-driven by construction.

**Downstream consequences.**

- The five-field motivation specification in the reasoning-fields theme — `(target / move / principle / gap / preferred alternative)` — is the chosen encoding under this F.
- In tension with [partial formalization](#^t1-partial-formalization) per `^t2-x2`: full motivation annotation is heavy; partial annotation profiles trade depth for ergonomics.
- The [inquiry-scope](workflows#^t3-inquiry-scope) and [inquiry-format](workflows#^t3-inquiry-format) decisions in the workflows theme realise this F at the inquiry grain.

### Reasoning understandability ^t1-reasoning-understandability

Reasoning yields **genuine understanding**, not merely formal validity. A representation satisfies this F when downstream readers can recover *why* the inquiry advanced, not only *that* it did. This requires three independent forms of justification to be representable simultaneously:

- **licensing** — why the result is valid under which warrant,
- **strategic** — why this move is relevant now over admissible alternatives,
- **explanatory** — why this move improves understanding, what cognitive change it produces.

**Failure mode prevented.** A formalism that records only licensing (formal validity) reduces research reasoning to proof-checking and silently drops the strategic and explanatory dimensions that distinguish a research artefact from a verified script.

**Upstream dependencies.** [Research faithfulness](#^t1-research-faithfulness).

**Downstream consequences.**

- Three implementation D's in the reasoning-structure theme realise this F, one per justificatory level: licensing implementation, strategic implementation, explanatory implementation. The current design partially answers the first two and leaves the third open.
- The justificatory-level placement decision (`^t2-justificatory-level-loci`) governs where each level lives: licensing intrinsic to the move, strategic and explanatory belonging to the recruiting assembly.
- In tension with [partial formalization](#^t1-partial-formalization) per `^t2-x2`.

### Cognitive manipulability ^t1-cognitive-manipulability

A representation is **manipulable** when a reader can perform five operations on it:

- **reconstruction** — recover the global strategy from local steps,
- **contrast** — see why one route was chosen over another,
- **compression** — summarise the argument by strategic blocks rather than by isolated formulas,
- **transfer** — reuse the strategic pattern in another problem,
- **diagnosis** — locate weak points (unsupported claim, missing condition, unjustified transition, irrelevant detour, hidden assumption, poor subquestion decomposition).

**Failure mode prevented.** A reasoning can be understandable in principle (the reader can follow each step) yet not manipulable (the reader cannot extract the strategy, transfer it, or compare alternatives). Understandability is the means; manipulability is the end.

**Upstream dependencies.** [Reasoning understandability](#^t1-reasoning-understandability) — manipulability presupposes understandability but goes further (means versus ends).

**Downstream consequences.**

- Five derived T3 decisions, one per capability: `^t3-global-reconstruction`, `^t3-contrastive-reasoning`, `^t3-compressed-essence`, `^t3-pattern-transfer`, `^t3-diagnosis-weaknesses`. Each names the chosen mechanism by which the system supports the corresponding operation.

---

## Operationality

Constraints on what the recorded reasoning must contain and how its primitives are bounded.

### Concrete analytical execution ^t1-concrete-execution

Reasoning chains encode **actual epistemic work**: step-by-step proofs, computations, comparisons, constructions, conceptual analyses. Labels such as "derive", "explain", "decompose", "eliminate" do not satisfy the requirement on their own; the underlying operation and its operands must be present.

**Failure mode prevented.** A skeleton of high-level dependencies and verb labels — without the underlying computation — looks like a reasoning chain but contains no epistemic content. Such skeletons cannot be validated, transferred, or diagnosed.

**Upstream dependencies.** [Research faithfulness](#^t1-research-faithfulness).

**Downstream consequences.**

- The operation-schemas theme commits to a five-row admissibility table (signature / conditions / semantics / success / license) for every primitive operation; concrete execution is the F that justifies the table.
- The "no opaque transformation" reasoning-quality clause is absorbed by this F at the per-step grain.

### No infinite regress ^t1-no-infinite-regress

Describing a reasoning **terminates**: the description does not lead to an open-ended demand for further primitives. Some terminating mechanism is required, but the framework does not prescribe which one.

**Failure mode prevented.** A reasoning description that decomposes every step into sub-steps without a halting principle never terminates; the author cannot finish recording, and downstream tools cannot validate.

**Upstream dependencies.** [Concrete analytical execution](#^t1-concrete-execution) — execution is concrete only if the description bottoms out.

**Downstream consequences.**

- The closed-library mechanism (a finite library of primitive operation schemas) is one chosen answer, recorded as the operation-schemas D after the post-audit reclassification of the former `^t2-closed-operational-core`. A different framework could satisfy this F by other means (e.g., a meta-rule reducing every operation to a fixed computational basis).
- The [operation-primitiveness open question](operations-and-modes#^t2-operation-primitiveness) selects among four termination strategies — definitional fiat, well-foundedness derivation, schema calculus, open library.

### Function-driven typology ^t1-function-driven-typology

Object types are distinguished by their **function**, not by their superficial structure. To remain stable across the system, kind boundaries track the epistemic role each object plays in inquiry, not the syntactic form it happens to take in any given file.

**Failure mode prevented.** A taxonomy keyed on surface form (file extension, presence of certain fields, length) collapses or proliferates when the surface form drifts. A function-keyed taxonomy survives reformatting.

**Upstream dependencies.** [Research faithfulness](#^t1-research-faithfulness) — function is what the representation must capture.

**Downstream consequences.**

- The motivation-encoding D (`^t2-motivation-encoding`) and the epistemic-work-encoding D (`^t2-epistemic-work-encoding`) in the reasoning-structure theme implement the function-vs-content split at the object-implementation grain.
- [Object-kind admission](object-kinds#^t2-object-kind-admission) tests candidates by function, not by structural resemblance.

---

## Modularity and Separation of concerns

Composition rules: how content is partitioned, how parts are referenced, how duplicates are detected.

### Activity separation ^t1-activity-separation

Distinct **research activities** — content production, content critique, content exposition, navigation, inquiry direction — have distinct loci. The framework does not collapse two activities into a single artefact, and a change to one activity does not require editing the artefacts of another.

**Failure mode prevented.** When content production and exposition share a locus, every audience-tailored rephrasing edits the canonical content; canonical edits silently rewrite expositions. The two activities then drift, and the system loses the ability to tell which artefact is authoritative.

**Upstream dependencies.** [Research faithfulness](#^t1-research-faithfulness).

**Downstream consequences.**

- The layered architecture (the layer inventory + per-layer functional roles in the layering theme) realises this F at the architecture grain.
- The single-source-of-truth D in the layering theme is the canonical-edit-locus mechanism.
- The audience-independent-stability sub-claim of the legacy `^t1-modularity` reduces to this F (multi-audience projection from a single canonical source).
- The multi-projection capability traces upstream here.

### Representation versus generation ^t1-representation-vs-generation

The framework operates in two modes: **post-hoc representation** of completed reasoning and **in-flight generation** during research. The two modes have different completeness, validation, and operability requirements; the framework distinguishes them rather than silently conflating.

**Failure mode prevented.** A framework tuned only for post-hoc representation imposes completeness requirements that block in-flight authoring; a framework tuned only for generation drops the validation that representation needs.

**Upstream dependencies.** [Research faithfulness](#^t1-research-faithfulness) — both modes occur in real research.

**Downstream consequences.**

- Per-criterion mode-sensitivity is recorded locally where it matters (e.g., on [partial formalization](#^t1-partial-formalization)) rather than as a blanket annotation.
- Workflow decisions (drafting gate, validation gating) read mode as one input.

### Reuse ^t1-reuse

The same **epistemic content** participates in multiple inquiries without duplication. A proof, definition, or mechanism contributes to several inquiry assemblies by reference, not by copy.

**Failure mode prevented.** Duplication of epistemic content forces the author to maintain divergent copies. Edits to one copy silently leave the others stale; readers cannot tell which copy is authoritative.

**Upstream dependencies.** [Research faithfulness](#^t1-research-faithfulness).

**Downstream consequences.**

- Pairs with [addressability](#^t1-addressability): reuse without addressability is impossible (there is no way to point at the reused content); addressability without reuse is empty (nothing points back).
- The single-source-of-truth D and the canonical-source-of-truth layer commit to one canonical home per content.
- [Non-redundancy](#^t1-non-redundancy) is the consistency condition that makes reuse enforceable across the system.

### Addressability ^t1-addressability

Every piece of **epistemic content** can be referenced by a stable identifier.

**Failure mode prevented.** Content that cannot be referenced cannot be reused, validated, or re-rendered.

**Upstream dependencies.** [Research faithfulness](#^t1-research-faithfulness); pairs with [reuse](#^t1-reuse).

**Downstream consequences.**

- Justifies `^t3-identifier-stability` (the persistence-vs-content-addressable choice) and `^t3-namespace-hierarchy` (the namespace organisation) in `ids-versioning.md`.
- Justifies the typed-import D in the registries-indexes theme.

### Relational queryability ^t1-relational-queryability

Relations between objects are **queryable as an addressable structure**. Dependency analysis, reverse-impact lookups, and orphan detection are first-class operations, not ad-hoc scripts over canonical files.

**Failure mode prevented.** When relations are buried in object bodies and never aggregated, a reader cannot ask "what depends on X?" or "what does Y impact?" without re-parsing the corpus. Refactoring becomes guesswork; orphans accumulate silently.

**Upstream dependencies.** [Addressability](#^t1-addressability) — queryability presupposes that targets have stable references.

**Downstream consequences.**

- The chosen mechanism is the relational-graph representation D in the relations-graph theme (alternatives: relational tables, triple stores).
- The build aggregates object-authored edges into the centralized graph (the dependency-management content folds here).
- The orphan-detection D in the registries-indexes theme realises one queryability operation; pairs with the dependency-graph component of the registry-component taxonomy.

### Non-redundancy ^t1-non-redundancy

Each **interpretive point** appears exactly once across the system. A second occurrence — verbatim restatement or paraphrase that adds no new content — is replaced by a cross-reference to the first.

**Failure mode prevented.** Duplication splits the source of truth and creates drift between copies. Readers cannot tell which version is current; validators cannot enforce a single canonical statement.

**Upstream dependencies.** [Activity separation](#^t1-activity-separation) — once activities have distinct loci, non-redundancy is enforceable across the system.

**Downstream consequences.**

- [Layer replaceability](layering#^t2-layering-replaceability) follows: a layer that duplicates content of another cannot be replaced cleanly.
- [Layering with no silent coupling](layering#^t2-layering-no-silent-coupling) follows for the same reason at the layer-pair grain.
- [Object-kind role purity](object-kinds#^t2-ontology-role-pure) follows at the kind grain.

### Terminology canonicity ^t1-terminology-canonicity

**Terminology is canonical across notes.** Variant names for the same concept silently degrade cross-note coherence and dependency tracking. The framework enforces canonicity through automated linting against a declared vocabulary registry.

**Failure mode prevented.** Three notes that refer to the same object as "warrant", "justification", and "support" appear unrelated to a string-matching tool. Terminology drift defeats both human reading and machine tracking; uncaught, it accumulates without limit.

**Upstream dependencies.** None recorded as F-level dependencies in the classification table. Pass-9 promotion (Rule 11) lifted this F out of the local terminology-enforcement D in `_backup/tooling-validation.md` because the canonicity *capability* is a user-facing prose-style commitment in its own right.

**Downstream consequences.**

- The terminology-enforcement D `^bk-terminology-enforcement` in the validation-views theme is the chosen linter mechanism that realises this F (per-entry `preferred_terms` and `forbidden_variants` against the terminology-index registry component).
- Pairs with [validation externality](#^t1-validation-externality): the linter runs outside the agent's authoring loop.

---

## Cost and Ergonomics

The four per-action costs (read versus write, human versus machine) plus the system-scale axis. The cluster forms a 2×2 grid:

|              | **Read cost**                                 | **Write cost**                                    |
| ------------ | --------------------------------------------- | ------------------------------------------------- |
| **Human**    | [Human read cost](#^t1-human-read-cost)       | [Human action cost](#^t1-human-action-cost)       |
| **Machine**  | [Read-side automation](#^t1-read-side-automation) | [Write-side automation](#^t1-write-side-automation) |

Plus [system scale](#^t1-system-scale) bounding the four costs as project size grows.

### Human read cost ^t1-human-read-cost

Per-read cost is **bounded**: a human reader reaches the content they need without parsing more material than the question requires. Legibility, navigation, and the local density of cross-references all contribute.

**Failure mode prevented.** A representation that requires reading three layers of indirection to answer a simple question burns the reader's attention before they reach the content. The framework loses its readers.

**Upstream dependencies.** None at the framework level (cost-axis root).

**Downstream consequences.**

- One of the four cost-axis F's that [system scale](#^t1-system-scale) bounds as project size grows. The cost-axis grid in the classification table positions human read cost as the human-row-read-cell, paired with [human action cost](#^t1-human-action-cost) on the write side and with [read-side automation](#^t1-read-side-automation) on the machine row.

### Human action cost ^t1-human-action-cost

Per-action cost is **bounded**: each authoring action — adding an object, recording a relation, updating a field, validating a draft — costs the author a small bounded amount. Excessive field overhead, redundant manipulations, and multi-step validations are explicit failures of the framework.

**Failure mode prevented.** A representation that demands ten fields per object and three validation passes per draft is technically expressive but operationally unusable. Researchers abandon it.

**Upstream dependencies.** None at the framework level (cost-axis root).

**Downstream consequences.**

- [Object-kind smallness](object-kinds#^t2-ontology-small) traces upstream (more kinds raise per-action cost).
- The *readable* and *low cognitive load* sub-claims of the legacy `^t2-narrow-ontology` and `^t2-data-format-criteria` reduce to this F.
- In tension with [reasoning understandability](#^t1-reasoning-understandability) per `^t2-x2`: deeper annotation lowers ambiguity at the cost of more per-action work.

### Read-side automation ^t1-read-side-automation

The system supports **automated reading**: query, search, navigation, comparison, and dependency analysis are mechanizable without human inference. Tools answer "what depends on X?" or "find all objects of kind K with property P" by deterministic computation over canonical state.

**Failure mode prevented.** A representation whose only reader is a human cannot scale: cross-corpus queries, refactoring impact, and integrity audits all become manual sweeps.

**Upstream dependencies.** None at the framework level (cost-axis root). Mirrors [human read cost](#^t1-human-read-cost) on the machine side.

**Downstream consequences.**

- The relational-graph representation (the chosen mechanism under [relational queryability](#^t1-relational-queryability)) is one consumer.
- The *parseable* sub-claim of the legacy `^t2-data-format-criteria` reduces to this F.

### Write-side automation ^t1-write-side-automation

The system supports **automated writing**: validation, build, registry update, orphan detection, and derived-artefact regeneration are mechanizable without human judgment. The author writes canonical content; the build derives indexes, registries, and rendered views.

**Failure mode prevented.** When derived artefacts must be edited by hand, every canonical edit creates a hidden TODO list of artefact updates. Drift accumulates and the system loses consistency.

**Upstream dependencies.** None at the framework level (cost-axis root). Mirrors [human action cost](#^t1-human-action-cost) on the machine side.

**Downstream consequences.**

- The *no-manual-edit policy* on derived artefacts (the absorbed sub-claim of `^t3-no-manual-edits-rendered`) follows directly from this F.
- The *schema-checkable* and *stable Git diffs* sub-claims of the legacy `^t2-data-format-criteria` reduce to this F.
- The validation-architecture D in the validation-views theme is one realisation; pairs with [validation externality](#^t1-validation-externality).

### System scale ^t1-system-scale

The four cost axes above remain **bounded as project size grows**. The framework handles wide projects — many objects, many contributors, many versions — without storage, query, or build degradation.

**Failure mode prevented.** A representation whose per-read cost grows linearly with corpus size, or whose build time grows quadratically with relation count, fails at research scale even when individual costs are reasonable on a small example.

**Upstream dependencies.** Cost-axis cluster — system scale bounds the four per-action costs as the project grows.

**Downstream consequences.**

- Constrains storage decisions, registry design, and the build pipeline.
- [Object-kind smallness](object-kinds#^t2-ontology-small) traces upstream here (kind proliferation hurts scale).

---

## Workflow integrity

How the framework is used at run time. These F's depend on every other group: they constrain *when* activity is gated and *who* validates, given the content, costs, and structure already in place.

### Staleness gating ^t1-staleness-gating

The framework **gates dependent activity** — drafting, citation, downstream derivation — on the resolution of upstream revision staleness. Users cannot proceed past unresolved upstream changes without explicit override.

**Failure mode prevented.** Drafting on top of a stale dependency silently produces work that rests on a withdrawn premise. Without a gate, the author discovers the conflict only at validation time, by which point the downstream work needs rewriting.

**Upstream dependencies.** None recorded as F-level dependencies in the classification table. Pass-9 promotion (Rule 11) lifted this F out of the local drafting-gate D in `_backup/registries-indexes.md` because the gating *capability* is a user-facing workflow commitment in its own right.

**Downstream consequences.**

- The drafting-gate D `^bk-drafting-gate` in the validity-revision theme is the chosen mechanism under this F. The mechanism is conditional on `^t2-dependent-flagging` (the flag-field source), `^bk-dependencies-registry` (the registry that stores per-import propagation status), and this F itself.

### Validation externality ^t1-validation-externality

**Validation is external to the agent.** Agent self-correction does not substitute for validator output; tooling outside the agent's authoring loop runs the structural integrity checks, and the agent treats validator output as authoritative.

**Failure mode prevented.** An agent that grades its own work conflates the writer and the checker. Errors that the agent's own model fails to recognise pass undetected; the validation signal collapses into the authoring signal.

**Upstream dependencies.** [Write-side automation](#^t1-write-side-automation) — externality presupposes that validators are mechanizable.

**Downstream consequences.**

- The validation-architecture D `^bk-validation-architecture` in the validation-views theme is the chosen layered set of validators (schema enforcement, referential integrity, graph integrity, uniqueness, status transitions, terminology enforcement, human review). Conditional on this F.
- The validation-gating D `^bk-validation-gating` selects the gating policy (hard gate / advisory / per-rule / per-target), Conditional on this F and on the validation-architecture D.
- Pairs with [terminology canonicity](#^t1-terminology-canonicity): the terminology linter is one externalised validator.
