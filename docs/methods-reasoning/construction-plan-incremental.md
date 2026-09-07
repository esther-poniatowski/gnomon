---
tags:
  - reference
index: "[References and methods](_index.md)"
aliases:
  - Incremental construction plan
---
# Concrete Incremental Construction Plan

## Orienting Decision

Before any technical step, the most consequential choice is the _unit of incremental progress_. Two natural-but-wrong choices must be rejected.

The first wrong choice is _building bottom-up by formal layer_: first fix the syntax, then the semantics, then the rule catalog, then the ontology, then start using the language. This produces years of foundational work before the framework is testable, locks in early choices that later corpus calibration would refute, and reproduces the top-down failure mode warned against in Principle 6.

The second wrong choice is _building top-down by operation category_: first implement all deductive operations, then all erotetic operations, then all comparative operations, etc. This produces a language satisfactory at one kind of move and incapable of the others, and it forces choosing an arbitrary starting category. Real research episodes mix categories from the start; a framework that handles deduction beautifully but cannot pose a question is unusable on the first day.

The right unit of incremental progress is the _minimal viable trace_: the smallest sequence of atomic moves that reconstructs a non-trivial research episode end-to-end. Each iteration of the construction adds one more research episode that can be reconstructed, where each new episode forces the addition of exactly the minimum apparatus needed to handle it. The corpus drives the construction; the formalism grows as required; usability is tested at every iteration because every iteration produces a working trace.

This approach is the operational interpretation of Principle 6 (bottom-up calibration on hard cases) combined with the operational-atomicity discipline of Section 6. It is also pragmatically wise: the framework is _useful_ from iteration two onward, even if the apparatus is incomplete; each iteration produces a deliverable; the design choices that are not yet forced remain _deferred_, available for later reconsideration as more episodes are reconstructed.

The plan below articulates this approach in concrete phases.

---

## Phase 0 — Pre-Work: Establish the Working Discipline

Before iterations begin, three preparations are needed. None are formalism; they are infrastructure for the construction process itself.

### 0.1 Establish the Corpus Repository

Assemble the local research projects into a _corpus repository_: a structured directory containing, for each project, its source materials (papers, notes, derivations, code) and a designated _episode index_ — a curated list of research episodes within that project that are candidates for formal reconstruction.

An episode is a _self-contained reasoning trajectory_: it has identifiable inputs (a question, an observation, a prior result), identifiable outputs (an answer, an explanation, a new concept, a refutation), and a finite sequence of intermediate reasoning steps. Appropriate episodes are _small enough to fit in working memory_ (a single proof, a single conceptual clarification, a single comparison between approaches) and _rich enough to exhibit the activity type_ being tested.

Across the available projects, draft an initial _episode catalog_ targeting representative diversity:

- two or three episodes of _mathematical derivation_ (e.g., from the mixture-representation-geometry work — ?; or from the learning-representations-isotypic-framework — ?);
- two or three of _conceptual clarification_ (e.g., from the geometry-specialization review taxonomy — disentangling operational probes from the observable phenomena);
- two of _taxonomic carving_ (e.g., from the geometry-specialization review — the classification of computational challenges);
- two of _literature integration_ (e.g., from the geometry-specialization review — );
- two of _question decomposition_ (e.g., from each of the geometry-specialization review, the mixture-representation-geometry work, the learning-representations-isotypic-framework);
- one of _abductive reasoning_ (e.g., from the mixture-representation-geometry — when the neuroscience work grounded the identification of three modes of response to mixture inputs);
- one of _revision_ (e.g., from the geometry-specialization review — a moment during development where an earlier classification architecture was reconsidered; or from the mixture-representation-geometry — a moment when the main question was narrowed or reformulated);
- one of _transfer / analogy_ (e.g., from the geometry-specialization review — Marr's levels to the questions of the review, or how to unify feedfoward and recurrent networks with respects to static vs. dynamical encoding);
- one of *formal interpretation episode* (e.g. from the learning-representations-isotypic-framework — when an abstract mathematical notion or tool was explained in terms of its meaning);
- one of *evidence integration episode* (e.g. from the geometry-specialization review — when a simulation result from a study entails a claim of necessity about a mechanism).

This is the _seed corpus_. It need not be definitive — corpus items will be added and refined as the construction proceeds — but it should exist before iteration begins, because each iteration is selected from it.

The corpus should be diverse enough that no two consecutive iterations exercise exactly the same apparatus, and ordered to _force_ the apparatus to grow in productive directions (rather than re-exercising what is already in place).

### 0.2 Establish the Working Notation

Before the formal grammar exists, a _working notation_ is needed for sketching atomic-move sequences. This is not the final syntax; it is a stable intermediate notation for development purposes, expected to be replaced once the formal grammar stabilizes.

The working notation should be:

- _line-oriented_: one atomic move per line, for trace inspection;
- _structured-data-backed_: each line corresponds to a typed record (JSON, YAML, or s-expression), so traces are machine-readable from the start;
- _minimally formal_: enforce structural shape but not semantic content yet;
- _versioned_: every trace is a file under version control, with a recorded schema version.

A reasonable initial format: one trace per file, in a structured serialization (the exact choice — TOML, JSON-Lines, an s-expression dialect, a custom YAML schema — matters less than committing to one and tooling around it). Each move record contains at minimum: a `move-type` field, a `parameters` block, a `produces` block (the object the move creates), and a `provenance` block (rationale, motivating question reference, source reference).

This is the _authoring substrate_ for the entire construction process. Tooling on top of it (validators, viewers, query interfaces) will be built incrementally.

### 0.3 Establish the Validation Discipline

For each iteration, a single criterion determines success: _the target episode can be reconstructed as an atomic-move trace in the working notation, with no step relying on unstated reasoning, and the trace passes the validation tools available at that iteration_. Validation tools at iteration $k$ are necessarily incomplete; the question is whether they are sufficient to catch the errors they were designed to catch on the trace produced.

Three artifacts are produced per iteration: (i) the trace itself, (ii) an _iteration journal_ recording what was added to the apparatus and why, and (iii) a _deferred-decisions log_ recording design choices that were left open because the current iteration did not force them. The deferred-decisions log is critical — it prevents premature commitment to choices that later iterations might constrain differently.

---

## Phase 1 — Iteration One: The Minimal Calculus

The goal of the first iteration is to establish the framework's _spine_: the smallest apparatus that can reconstruct _any_ research episode at all. The target episode should be the simplest available — a short mathematical derivation, ideally from familiar territory.

### 1.1 Selection of the First Episode

Choose an episode that is:

- _purely deductive_ (no observation, no abduction, no revision yet);
- _short_ (under twenty inference steps);
- _familiar_ (so disagreement about the content does not contaminate disagreement about the formalism);
- _well-grounded_ (the inferences are uncontroversially valid).

A first candidate from the available material: a single mathematical derivation from the mixture representational geometry work — the kind of result that a textbook would present in half a page, with each step clearly licensed by a standard rule.

The choice is deliberate. Starting deductively does _not_ contradict the rejection of deductive bias from earlier discussion. It is starting with the _best-understood_ operation type, where existing literature provides validated rules to import (Step 3 of the catalog-construction methodology). The non-deductive operations will be introduced in subsequent iterations, where the deductive spine supports their integration.

### 1.2 Apparatus to Build

The minimum apparatus for iteration one:

**State components instantiated:**

- $\Sigma$ — a signature, populated with the symbols needed for the episode (types, functions, predicates, constants).
- $T$ — a theory, populated initially with the episode's premises (definitions, prior results, axioms).
- $H$ — a trace, recording the sequence of moves.
- $\Pi$ — commitment statuses, with `asserted` as the only status used at this iteration.

Other state components ($Q, U, \mathcal{X}, M$) are _declared but unused_ at this iteration. They will be exercised by later iterations.

**Atomic moves implemented:**

- `introduce-symbol`, `assert-axiom` (for setting up the initial state),
- `apply-rule` (for inference steps),
- `record-source` (for provenance on every introduced item).

**Rule catalog seeded:**

- The standard rules of natural deduction for the propositional and first-order content of the episode.
- Equality rules (reflexivity, symmetry, transitivity, congruence).
- Whatever domain-specific rules the episode requires (e.g., basic algebraic manipulation rules, matrix algebra rules, calculus rules, presented as named inference rules).

Each rule is a _named, formally specified object_ with stated premises (as patterns), a stated conclusion (as a pattern), and a stated invariant (truth-preservation, given the rule's intended semantics).

**Object catalog seeded:** Per Section 7, the object catalog is dual to the move catalog. The seeded objects are: `Symbol`, `Axiom`, `RuleApplication`, `Provenance`, `Trace`.

**Validation tools at this iteration:**

- _Type checking_: every introduced symbol is typed; every axiom is well-formed over the current signature; every rule application's premises actually appear in the trace.
- _Rule-application checking_: every `apply-rule` invocation cites a rule from the catalog whose pattern matches the cited premises and whose conclusion matches the produced formula.
- _Provenance completeness_: every object has a non-empty provenance field.

These checks are _purely syntactic_ at this iteration. Semantic soundness of the imported rules is taken on faith (they are standard; their soundness is in the literature). Soundness audits of framework-specific rules will be required in later iterations.

### 1.3 Deliverables of Iteration One

- One reconstructed trace.
- The seeded rule catalog, with each rule named and specified.
- The seeded object catalog, with each object type defined.
- Validation tools that pass on the produced trace.
- An iteration journal noting which design choices were forced and which were deferred.

### 1.4 What Iteration One Does _Not_ Yet Have

Explicitly absent, and the absence should be recorded in the deferred-decisions log:

- The full grammar of $\mathcal{L}_C$ (only a fragment exercised by the episode is defined).
- A model-theoretic semantics specification (rule soundness rests on borrowed standard accounts).
- Modal-epistemic rules for commitment propagation (everything is asserted at full credence).
- The inquiry language $\mathcal{L}_I$ (no questions, no plans, no revisions yet).
- Verification debt machinery (no automated procedures are invoked yet).

This is deliberate. Iteration one establishes the spine; the omitted components will be forced by subsequent iterations.

### 1.5 What Iteration One Validates

If iteration one succeeds, the framework has demonstrated that a deductive episode can be reconstructed at atomic granularity in the working notation with full provenance and rule citation. This is the _baseline competency_ — necessary but not sufficient.

If iteration one _fails_ — if the chosen episode cannot be reconstructed without prose annotations, hand-waving, or rule invocations whose patterns cannot be specified — then either the episode was wrongly chosen (try a simpler one) or the granularity discipline was misjudged (the apparatus needs deeper foundations). Failure mode here is a diagnostic, not a setback.

---

## Phase 2 — Iterations Two Through Five: Forcing Each Operation Family

Each iteration selects one episode from a different operation family and forces the apparatus to grow to accommodate it. The order matters: each iteration should add maximal new structure with minimal disruption to what was built.

### 2.1 Iteration Two: A Conceptual Clarification Episode

Selecting an episode that introduces a new concept — for instance, clarifying a term.

This forces:

- `introduce-symbol` with a defining axiom (already in the catalog, now exercised with non-trivial content);
- The _conservativity-check_ rule (new): given a definitional axiom $\forall \bar{x}. P(\bar{x}) \leftrightarrow \varphi(\bar{x})$, the rule produces a proof obligation, which the user discharges by constructing a derivation showing that $P$'s removal does not change provability of $\varphi$-free statements;
- A new object type: `ConceptConstruction`, recording the defining axiom, the conservativity proof, the motivating rationale.

If the concept is implicit (defined by axioms rather than reduced to prior vocabulary), the iteration forces:

- A _characterization rule_ (new): an implicit definition is admissible only if its axioms are jointly satisfiable, which the user shows by constructing a witnessing model (or by appeal to an existence theorem in the imported theory).

The iteration journal records the rule additions and the rationale.

### 2.2 Iteration Three: A Question Posing and Decomposition Episode

Selecting an episode where a research question is posed, its presuppositions are identified, and it is decomposed into investigable sub-questions.

This forces:

- $Q$ — the question agenda — to become an active state component.
- New atomic moves: `pose-question`, `extract-presupposition`, `decompose-question`, with corresponding object types `Question`, `Presupposition`, `Decomposition`.
- New rules: the _erotetic-implication_ rule (decomposition is admissible only if joint resolution of sub-questions resolves the parent), the _presupposition-coherence_ check (a question's presuppositions must be consistent with $T$ or explicitly marked conjectural).

The iteration also forces the introduction of $\mathcal{L}_I$ proper — a distinct sub-language for questions, with its own grammar fragment, sitting alongside $\mathcal{L}_C$. The coupling between the two (a question's answer set is a set of propositions in $\mathcal{L}_C$) is the first concrete instance of inter-language coupling and must be specified.

### 2.3 Iteration Four: A Comparison or Analogy Episode

Selecting an episode where two frameworks, methods, or theories are compared.

This forces:

- $M$ — the structural-mappings component — to become active.
- New atomic moves: `declare-mapping`, `record-preservation`, `record-divergence`, with corresponding object types `Mapping`, `PreservationClaim`, `DivergenceClaim`.
- New rules: _preservation verification_ (a preservation claim about a particular axiom requires a derivation in the target showing the axiom's image is provable there), _divergence verification_ (a divergence claim requires a counter-derivation or counter-model).

This iteration is the first that requires _substantive type-checking_ of object construction in the sense of Section 7: a `PreservationClaim` cannot be constructed unless an accompanying derivation is provided as part of its construction. Object construction is no longer mere registration; it has become _gated by proof obligations_. The tooling around this is the first piece of genuinely dependent type-like infrastructure in the framework.

### 2.4 Iteration Five: A Revision Episode

Selecting an episode where a prior commitment is revised in light of new information.

This forces:

- The event-sourcing discipline of Section 7 to be implemented: retraction is not removal but addition of a `Retraction` event-object.
- $\Pi$ — commitment statuses beyond `asserted` — to become active: `conjectured`, `suspended`, `retracted` statuses are exercised.
- An _entrenchment ordering_ over $T$ — a partial order on axioms recording relative commitment strength.
- New atomic moves: `retract-axiom`, `set-commitment`, `set-entrenchment`, with corresponding event-object types.
- New rules: _AGM contraction-kernel selection_ (given a target axiom to be removed and an entrenchment ordering, identifies the minimal set of axioms that must go), _commitment-propagation_ (when an axiom's commitment status is lowered, derived items that depend on it have their statuses adjusted accordingly).

This iteration also forces the dependency-tracking infrastructure: the framework now needs to know which objects depend on which others, so that retractions can propagate their consequences. The trace becomes not just a sequence but a _dependency graph_, with the temporal sequence as one of several relations over the graph.

By the end of iteration five, the framework has been exercised on:

- Pure deduction;
- Concept construction;
- Question posing and decomposition;
- Comparison;
- Revision.

Most of the central operation families have been touched. The apparatus has grown to include the deductive core, the framework-specific rules for concept construction and questioning, the dependent-typed object construction discipline, the event-sourcing discipline, dependency tracking, and the first inter-language coupling.

---

## Phase 3 — Iterations Six Through Roughly Ten: Filling the Inventory

The remaining operation families are introduced in iterations chosen by the same principle: each new iteration targets an episode that exercises an operation type not yet exercised, forcing the apparatus to grow.

Suggested ordering, though it should adapt to which corpus episodes prove most informative:

**Iteration six: an observation interpretation episode.** Forces the chain `datum → instrument-reliability → defeater-check → evidence-uptake → asserted-claim`, as in Section 6.3. New rules: _instrument-reliability_, _defeater-absence_, _evidence-uptake_. This iteration is where the bridge between empirical content and the formal trace gets built.

**Iteration seven: an abductive episode.** Forces the explicit hypothesis-generation, vetting, and ordering machinery of Section 6.3. New rules: _abductive-schema-instantiation_, _entailment-check_, _novelty-check_, _plausibility-ordering_. Connects to the `conjectured` commitment status from iteration five.

**Iteration eight: a transfer episode.** Forces the use of a mapping from $M$ to carry content across, with the result tagged as conjectural and provenance-linked. New rule: _transfer-along-mapping_. Connects iterations four (comparison/mapping) and seven (conjectural commitment).

**Iteration nine: a taxonomic carving episode.** Forces the _carving_ move with subsumption, disjointness, and covering axioms, plus the _carving-criterion_ record. New rules: _taxonomic-coherence-check_, _carving-justification_.

**Iteration ten: a worked-example-and-counterexample episode.** Forces the _witness construction_, _model exhibition_, and _counter-example construction_ moves. New rules and the integration of model-class reasoning into the trace.

By the end of phase three, the inventory of Section 4 has been substantially exercised. The catalog of rules has grown by perhaps thirty to fifty primitive rules and a similar number of derived rules; the catalog of object types has grown to perhaps twenty to thirty types; the validation tools have grown correspondingly.

This is the point at which the framework becomes _broadly useful_: most research moves the user encounters can be reconstructed within it, even if some specialized moves still require new apparatus.

---

## Phase 4 — Stabilization and Audit

After roughly ten iterations, the apparatus is rich enough to be useful but not yet _coherent_. The choices made in early iterations may not align cleanly with choices made later; redundancies may have accumulated; soundness audits have been deferred.

This phase pauses corpus-driven growth and conducts a _retrospective consolidation_.

### 4.1 Soundness Audit

For each rule in the catalog — primitive and derived — produce a soundness proof against the framework's semantics. This is the deferred Step 4 of catalog construction (§7).

The semantics may itself need to be made explicit at this point: the early iterations leaned on borrowed standard semantics; the framework-specific rules (for commitment propagation, transfer, abduction, etc.) require explicit semantic accounts.

Three outcomes are possible:

- _Rule confirmed sound_: no change needed.
- _Rule confirmed unsound_: the rule is removed or restricted; the traces that used it are flagged for re-verification.
- _Rule's soundness undecided_: the rule is marked _provisional_ with explicit dependence on assumptions to be discharged.

Verification debt becomes a real, populated structure for the first time, retroactively annotating earlier traces.

### 4.2 Redundancy Audit

Identify rules that license the same derivations. For each redundancy:

- If both are useful for authoring, keep both, marking one as derivable from the other.
- If one is strictly more convenient, deprecate the other but keep it for trace-compatibility.

Identify object types that overlap in their fields and meanings. Consolidate.

### 4.3 Conservativity Check

Verify that the rules added in later iterations are conservative over the deductive core: they should not license new derivations within the deductive fragment that were not licensable before.

If conservativity fails, the offending rule is restricted via signature scoping.

### 4.4 Surface-Layer Refinement

The working notation of Phase 0 may have accumulated awkwardness. Now is the moment to refine the _surface syntax_ — but only after the underlying object and rule catalogs are stable. The surface syntax is now designed as a _projectional_ notation faithfully compiling to the established object catalog.

Earlier traces are reformatted in the new notation; their object-level content does not change.

### 4.5 Tooling Maturation

Validation tools that grew incrementally are refactored into a coherent system: a typed object database, a trace viewer with granularity controls, a query interface, a dependency-graph visualizer. The tools become genuinely productive — the user is no longer fighting them.

### 4.6 Documentation Pass

Each rule, each object type, each macro is now documented: its precondition, its effect, its invariant, its motivation, the corpus episode that forced its introduction. This documentation is itself a typed object catalog — meta-documentation cross-referencing the formal apparatus.

The deliverable of phase four is a _coherent, audited, documented_ framework, ready for broader application.

---

## Phase 5 — Expansion: Beyond the Initial Corpus

After stabilization, the framework can be applied to new material: research episodes outside the seed corpus, including episodes in ongoing or future work. Each new application is itself a small iteration, but the apparatus is now mature enough that most episodes will reconstruct without forcing new rules.

When new rules are needed, they are added under the established discipline:

1. The rule's pattern, premises, and conclusion are specified.
2. Its invariant is identified and its preservation proved.
3. Its conservativity over the existing catalog is verified.
4. Its scoping is specified.
5. It is documented and integrated.

This is the _steady-state_ operation of the framework: occasional rule additions in response to genuinely novel research moves, but mostly the application of established apparatus.

This phase also opens the framework to _external corpus_ material: published papers, historical research episodes, examples from other investigators' work. Each successful reconstruction is a validation; each failure is a diagnostic.

---

## Concrete Implementation Choices for Phase 0

Returning to the immediate practical question: what should be done _first_?

### A Two-Week Phase-Zero Plan

**Week one:**

- _Day 1–2._ Survey the local research projects and assemble the seed corpus (§0.1). For each project, identify two or three candidate episodes. Tag each with its expected operation family.
- _Day 3._ Select the iteration-one episode (§1.1). Write it out informally first — the actual reasoning, prose-permitted — to know what is being reconstructed.
- _Day 4._ Decide the working notation (§0.2). A reasonable starting choice: JSON-Lines for traces (one move per line, each line a JSON object), with a YAML schema specification for move types. The choice can be revised later, but commit to it for the first iteration.
- _Day 5._ Set up the repository: a Git repo with `corpus/`, `traces/`, `catalog/` (subdirectories for `objects/` and `rules/`), `tools/` (validation scripts), `journal/` (iteration journals).

**Week two:**

- _Day 1–2._ Execute iteration one. Reconstruct the chosen episode atomically in the working notation. Expect this to take longer than anticipated and to surface design questions that the deferred-decisions log will absorb.
- _Day 3._ Write the first validation tool: a script that reads a trace file, type-checks each move against the move catalog, and reports errors. Run it on the trace; fix errors until it passes.
- _Day 4._ Write the first iteration journal. What was added? What was deferred? What surprised?
- _Day 5._ Choose the iteration-two episode (a conceptual clarification per §2.1). Review whether the iteration-one apparatus needs adjustment before proceeding (often it does — a deferred choice has been forced into the open by the act of trying to use it).

After two weeks, iteration one is complete and iteration two is queued. The framework's spine exists; it has been exercised on one episode; the discipline of incremental construction has been instantiated.

### The Available Projects as Benchmark Sources

The question of whether to leverage the local projects as benchmarks is answered emphatically yes — and more strongly than the question implies. The projects should not be merely _consulted_ as benchmark sources; they should be _the primary driver_ of the construction.

The diversity of activity types covered by the available work is itself an asset: neuroscience research provides empirical-input and abductive episodes; mathematical derivation work provides deductive episodes; the review classifications provide taxonomic carving, conceptual clarification and question decomposition; the isotypic decomposition framework provides framework development and meta-reasoning episodes; the bibliography summaries provides literature integration episodes; the prior framework-architecture work provides comparison and revision episodes.

This diversity is precisely what the corpus method (Principle 6) requires. Many designers attempt this kind of construction with a _manufactured_ corpus — episodes invented to exercise specific apparatus. Manufactured corpora encode the designer's preconceptions and miss the surprises real research produces. Working from genuine episodes, in domains the designer knows deeply, is incomparably better.

A specific recommendation: maintain a _corpus annotation_ alongside each project, recording which episodes have been reconstructed, which are queued, and what each episode taught about the framework. Over time, this annotation becomes a research artifact in its own right — a record of the framework's evolution against real practice, useful for documentation, validation, and dissemination.

### What to Avoid in Phase Zero

Three failure modes in the early phase deserve explicit warning.

_The first_ is _premature formalization of the grammar_. The instinct to begin by writing down the formal grammar of $\mathcal{L}_C$ is strong and wrong. Grammar is the last thing to fix, because every iteration reveals constraints the grammar must satisfy. The working notation of §0.2 is _not_ the grammar; it is a temporary substrate. Treat the grammar as a deferred decision until the apparatus is stable enough that the grammar's design is largely forced.

_The second_ is _premature semantic specification_. Writing down a model-theoretic semantics before the rule catalog is stable is wasted effort; the semantics will be reshaped by every rule addition. The early iterations rely on imported semantics for imported rules and on intuitive correctness for framework-specific rules, with the soundness audit of Phase 4 making everything explicit.

_The third_ is _premature tooling sophistication_. The temptation to build an editor, a visualizer, an inference engine, a UI — before there is anything to display or check — is strong. Build only the validation tool needed for the current iteration; let tooling evolve incrementally alongside the apparatus. Sophisticated tooling locked in early constrains the formalism's evolution; minimal tooling adapts.

---

## Closing Considerations

### The Right Mindset for the Construction Process

The framework's construction is a _research project in itself_. It has its own questions (what apparatus is needed?), its own evidence (corpus episode reconstructions), its own revisions (rule audits), its own deferred decisions, its own provenance. The discipline being built into the framework should be applied to the framework's construction.

A concrete implication: maintain the iteration journals as carefully as one would maintain research notes. Treat the deferred-decisions log as a research instrument. When a design choice is deferred, record _why_ it was deferred and _what would force it_. When an iteration produces a surprise, record the surprise. The construction process should itself be reconstructable within the framework once the framework is mature enough.

### When the Framework Is "Done"

A framework of this kind is never finished — it is a living apparatus that grows as practice grows. But three milestones are worth identifying.

The first is _self-sufficiency_: the framework can reconstruct the kinds of episodes the designer routinely engages with. At this point the framework is usable for the designer's own work.

The second is _transferability_: another researcher, given the documentation, can reconstruct their own episodes. At this point the framework is a tool that exists beyond its designer.

The third is _productivity_: the framework reveals patterns, supports queries, and enables analyses that were unavailable before. At this point the framework becomes a research instrument that does work the designer could not do without it.

The phases above are oriented toward the first milestone. The second and third are downstream goals — but they are achievable only by reaching the first, which is achievable only by the disciplined, corpus-driven, incremental approach described.

### Synthesis

The construction proceeds by iterations, each targeting a specific research episode from the local corpus. Each iteration adds the minimum apparatus needed to reconstruct that episode atomically. Earlier iterations establish the deductive spine; subsequent iterations force the introduction of concept construction, questioning, comparison, revision, observation, abduction, transfer, taxonomic carving, and exemplification. After roughly ten iterations, a stabilization phase audits soundness, removes redundancy, verifies conservativity, refines the surface syntax, matures the tooling, and produces coherent documentation. Beyond this, the framework operates in steady state, with occasional additions for genuinely novel research moves and broad application to internal and external corpora.

The local projects — neuroscience, mathematical work, conceptual taxonomy, framework development, literature integration — provide an ideal corpus for this construction, with the diversity of activity types needed to exercise the framework against real practice. They should be the construction's primary driver, not merely its benchmark, and the framework should grow with the corpus rather than against an abstract specification.

The construction is patient: useful at iteration two, broadly capable by iteration ten, mature after stabilization. It is also disciplined: every iteration produces a working trace, every addition is justified by an episode, every deferred decision is recorded, and the framework's own construction is documented with the same care that the framework demands of its users.