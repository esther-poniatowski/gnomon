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

*To be drafted at the arguments-and-reasoning work.*
