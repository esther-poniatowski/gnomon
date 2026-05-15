# Arguments and reasoning

> [!INFO] Tier and source
> **Tier 3 (per aspect).** Stub file. Holds criteria that constrain the structure and quality of argumentative reasoning (assemblies relative to a target and their internal moves). Traces to [t1-intelligibility](vendor/gnomon/docs/design/1-framework/epistemic-adequacy#^t1-intelligibility), [t1-non-arbitrary](vendor/gnomon/docs/design/1-framework/content-adequacy#^t1-non-arbitrary), [t2-revision-semantics](vendor/gnomon/docs/design/2-architecture/constraints#^t2-revision-semantics), and what an assembly may contain under [promotion of assembly-local records](vendor/gnomon/docs/design/2-architecture/reasoning-structure#^t2-assembly-record-promotion).

---

## Criteria

### Warrant transparency at appropriate generality ^t3-warrant-transparency

The licensing principle for each step is stated at appropriate generality — neither so specific that reuse is blocked, nor so generic that the warrant is uninformative.

### Motivational non-triviality ^t3-motivational-non-triviality

Motivation identifies a contrastive choice against at least one salient alternative. A motivation that names no rejected alternative is uninformative.

### Teleological coherence of the sub-goal tree ^t3-teleological-coherence

The sub-goal tree is well-founded and rooted at the principal thesis; there are no explanatorily idle steps.

### No unsupported derived claim ^t3-no-unsupported-derived-claim

Every derived claim has at least one incoming `supports` edge with an explicit warrant.

### No opaque transformation ^t3-no-opaque-transformation

Every non-trivial step has a stated conceptual effect — what it transforms, into what, and why.

### No hidden branch choice ^t3-no-hidden-branch-choice

When multiple admissible routes exist, the chosen route includes at least one rejected alternative recorded in the strategic annotation (per [Reasoning-annotation field set](vendor/gnomon/docs/design/3-aspect-specific/reasoning-fields)).

### Discharge accounting for assumptions ^t3-discharge-accounting

> [!INFO] The criterion clause is migrated to [no silent incompleteness](_framework-criteria#^t1-no-silent-incompleteness). The discharge-mechanism choice survives as the open D `^t3-assumption-discharge-mechanism` in this theme.

Every assumed node is either discharged downstream or flagged as unresolved.

### Snapshot DAG acyclicity ^t3-snapshot-dag-acyclicity

Within a reasoning snapshot, the dependency graph is a DAG. Cycles indicate circular reasoning and are a hard error (per [snapshot DAG acyclicity](vendor/gnomon/docs/design/2-architecture/constraints#^t2-snapshot-dag)).

---

## Decisions

*To be drafted at the arguments-and-reasoning work.*

---

## Open questions

### Reusable reasoning schemes ^t3-reasoning-schemes

> [!QUESTION] Does the framework admit named, reusable reasoning schemes as a content kind, separate from individual filled arguments?

A reasoning scheme is a reusable template for a recurring form of defeasible reasoning, drawn from Walton-style argumentation-scheme theory. A scheme separates a general reasoning pattern from the specific content inserted into it, and so directly addresses the generalizable-versus-context-specific tension: the scheme is reusable, the filled slots preserve local content.

A scheme carries four parts:

- **Slots** — the context-specific propositions a use of the scheme must fill.
- **Warrant template** — the general bridge principle the scheme licenses, stated with slot variables.
- **Critical questions** — a systematic stress test attached to the scheme; each question probes a way the scheme can fail.
- **Applicability conditions** — when the scheme is a legitimate move.

Candidate schemes for a research framework: argument from analogy (transfer a structure across domains), argument from sign (infer latent structure from an observable marker), argument from expert opinion (use literature authority under source constraints), causal argument, argument from consequences, argument from classification, methodological argument (justify a method or analysis-strategy choice — "use this analysis because it is the least arbitrary level" — rather than a propositional inference; the worked-example suite, example 8, surfaces this as a distinct argument target the three-level justification model does not cover).

A use of a scheme is a separate object — a scheme instance — pairing the scheme with its slot values, local qualifiers, and local defeaters.

Bears on [t2-operation-primitiveness](vendor/gnomon/docs/design/2-architecture/operations-and-modes#^t2-operation-primitiveness): a scheme is one candidate form an operation schema can take. Bears on [t1-goal-driven-reasoning](vendor/gnomon/docs/design/_framework-criteria#^t1-goal-driven-reasoning): the critical questions of a scheme are a source of admissible sub-questions. Staged inputs and the broader paradigm survey are in [_fleeting-ideas](vendor/gnomon/docs/design/_fleeting-ideas#^fleeting-move-vocabulary).

> [!WARNING] Editable templates, not fixed labels
> A scheme is a template authors edit, extend, and instantiate, not a closed taxonomic label. Treating schemes as a fixed category set would make them classificatory rather than productive.

### What an attack edge targets ^t3-attack-target

> [!QUESTION] When one object attacks another, does the framework record what the attack targets — the conclusion, or the inference that reaches it?

Structured-argumentation practice (ASPIC+) distinguishes two attack kinds that a single `attacks` edge conflates:

- **Rebuttal** — an attack on a *conclusion*: a competing object asserts the negation or a defeater of the target's claim.
- **Undercutter** — an attack on an *inference*: the attacker grants the grounds but denies that the warrant licenses the step from grounds to conclusion.

The distinction is sharper than a generic disagreement edge. Many research conflicts are not contradictions between conclusions; the attack targets a method, an operationalisation, an analogy, or an interpretive bridge. A worked instance: linear decodability of a variable from a representation is offered as grounds that the variable is represented; the undercutter grants the decodability but denies the warrant connecting decodability to representational use — it targets the inference, not the conclusion.

A third attack target is the **framing of a question**: a critique that the question itself presupposes something illegitimate. The worked-example suite (example 4) gives the instance — asking whether a network "contains" a concept presupposes a container model of representation; the critique attacks neither a conclusion nor an inference but the presupposition built into the question. This target kind connects to [discharge accounting for assumptions](#^t3-undischarged-commitments): the presupposition a question carries is an undischarged commitment, and a framing-attack surfaces it. The attack-target vocabulary should therefore admit a third value — an attack on a `Question`'s framing — alongside rebuttal and undercutter.

**Method-result circularity** is a specific undercutter worth recording as a recurring pattern. The worked-example suite (example 26) gives the instance — a clustering analysis may *reveal* task-relevant groups, or may *impose* the very discreteness that later appears as evidence for those groups. The critique grants the result but attacks the inference from result to conclusion, by noting that the method partly constructed the object it then measured. This is not a justification cycle (nothing in the recorded chain returns to itself) and not a mutual constraint; it is an undercutter whose ground is the method-object relation. The framework should record when a result is method-dependent in a way that undercuts its evidential force.

**Critique-driven re-typing** is a further undercutter pattern (worked-example suite, example 36). A critique can do more than defeat a claim: it can re-type the inquiry's *target object* — the failure of a decoding criterion reveals that "an acceptable criterion" is the wrong object kind, and the target should instead be "a family of tests characterized by their failure modes". The undercutter's payload is not a defeated conclusion but a re-typing of what the question is about. This is distinct from a modelling-choice re-typing (which is a branch point under [snapshot DAG acyclicity / no-hidden-branch-choice](#^t3-no-hidden-branch-choice)) and from a process-trajectory re-typing (a temporal fact about the phenomenon): only the critique-driven case is an attack edge, and it belongs here.

Bears on [t2-typed-relation-vocabulary](vendor/gnomon/docs/design/2-architecture/relations-graph#^t2-typed-relation-vocabulary): the relation vocabulary either carries distinct `rebuts`, `undercuts`, and framing-attack labels, or a single `attacks` label with a target-discriminator field. The acceptance-set computation that structured argumentation builds on these edges is out of scope per [t1-no-runtime-inference](vendor/gnomon/docs/design/1-framework/external-interfaces#^t1-no-runtime-inference); only the authored, typed edges are in scope.

### Undischarged commitments of a statement ^t3-undischarged-commitments

> [!QUESTION] How does the framework record the propositional commitments a statement leans on but does not assert — and how strong is each?

A statement carries commitments beyond the content it asserts. A definition that references undefined terms presupposes background propositions: that the genus is a meaningful concept, that the genus can bear the differentia attribute, that the attribute admits the stated value. These presuppositions are not errors. They are **deferred obligations** — epistemic debt the statement incurs and the framework should track rather than silently absorb. This bears on [t1-no-silent-incompleteness](vendor/gnomon/docs/design/_framework-criteria#^t1-no-silent-incompleteness): an undischarged presupposition is exactly the kind of hidden dependency that silent-incompleteness detection must surface. The discharge of such obligations is governed by the same mechanism as assumption discharge — see [t3-assumption-discharge-mechanism](#^t3-assumption-discharge-mechanism) once that decision is drafted.

Three refinements distinguish what a statement commits to:

- **Presuppositions as first-class objects, with priority.** Each presupposition records its content, the statement that incurred it, its role, its resolution status, and a priority. Priority lets the framework defer low-urgency obligations (a value term awaiting a directionality concept) without losing them, while flagging high-urgency ones (an undefined genus).
- **Three strengths of commitment.** A statement's use of a term is weaker than the background structure it presupposes, which is weaker than a global axiom. "Term Z functions here as an attribute of Y" (a *local role*) is weaker than "the definition presupposes Y can bear attribute Z" (a *provisional commitment*), which is weaker than "every Y bears attribute Z" (a *global ontology axiom*). Promotion from a weaker to a stronger commitment is explicit, never automatic. Bears on [t2-epistemic-status](vendor/gnomon/docs/design/2-architecture/object-kinds#^t2-epistemic-status).
- **Definitional force.** A statement of the form "an X is a Y where Z is W" may carry a necessary condition, a sufficient condition, a biconditional definition, or an informal characterisation. Scientific prose rarely marks which. The normalized object records definitional force as an explicit, possibly uncertain value rather than silently committing to the strongest reading. Bears on [t1-partial-formalization](vendor/gnomon/docs/design/_framework-criteria#^t1-partial-formalization).

Bearing criteria: [t1-no-silent-incompleteness](vendor/gnomon/docs/design/_framework-criteria#^t1-no-silent-incompleteness), [t1-partial-formalization](vendor/gnomon/docs/design/_framework-criteria#^t1-partial-formalization), [t2-epistemic-status](vendor/gnomon/docs/design/2-architecture/object-kinds#^t2-epistemic-status).

The motivating worked example and the companion definition-structure refinements are recorded at [normalized definition form](vendor/gnomon/docs/design/3-aspect-specific/ontology#^t3-definition-normal-form) and [_worked-examples](vendor/gnomon/docs/design/_worked-examples#^example-genus-differentia).
