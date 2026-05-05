# Architecture C

## Three-Level Architecture

The representation is structured at three granularity levels, each necessary and non-redundant:

### Level 1 — Inference Node (micro)

The atomic unit. Each node encodes a single inferential step with full annotation across all five epistemic functions above.

| Field                             | Type                                                                                                                                                               | Description                                                                                                                                                                 |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                              | string                                                                                                                                                             | Unique identifier                                                                                                                                                           |
| `claim`                           | string                                                                                                                                                             | Propositional content (formal or natural language)                                                                                                                          |
| `epistemic_status`                | established \| assumed \| conjectured \| provisional \| discharged                                                                                                 | "discharged" for assumptions eliminated by reductio or case closure                                                                                                         |
| `inference.type`                  | deduction \| induction \| abduction \| analogy \| instantiation \| case-split \| contraposition \| reductio \| generalisation \| schema-application \| …           |                                                                                                                                                                             |
| `inference.warrant`               | string                                                                                                                                                             | The principle, rule, or theorem that licenses the step. This is the WHAT: "by commutativity of ∧", "by modus ponens on [n3, n4]", "by IH on smaller input"                  |
| `inference.motivation`            | string                                                                                                                                                             | The WHY: "direct construction unavailable; contrapositive exposes the negation hypothesis which is tractable", "case-split on parity exploits the ±1 periodicity structure" |
| `explanatory_function.role`       | hypothesis_elim \| thesis_reduction \| case_closure \| obstacle_removal \| hypothesis_elim \| normalization \| instantiation \| key_lemma \| auxiliary \| bridging |                                                                                                                                                                             |
| `explanatory_function.discharges` | [`node_id`, …]                                                                                                                                                     | Ids of assumptions or open sub-goals this step closes                                                                                                                       |
| `explanatory_function.sub_goal`   | `segment_id`                                                                                                                                                       | The meso-level segment this step contributes to                                                                                                                             |
| `depends_on`                      | [`node_id`, …]                                                                                                                                                     | Direct inferential dependencies (DAG edges)                                                                                                                                 |
| `supports`                        | [`node_id`, …]                                                                                                                                                     | Nodes for which this is a premise                                                                                                                                           |

The `motivation` field is the critical addition absent from all standard proof formats. It is not a restatement of the warrant (which is a syntactic/semantic fact about the inference schema) but an explicit record of the _strategic choice_ among available rules — grounding the step in the structure of the problem rather than in formal permissibility alone.

The `explanatory_function.role` taxonomy encodes the teleological classification: a `key_lemma` node carries a different explanatory weight than an `auxiliary` or `bridging` node, and this distinction should be machine-readable.

### Level 2 — Argument Segment (meso)

A contiguous group of nodes sharing a common sub-goal. This level makes the _proof strategy_ explicit at an intermediate granularity — neither the global thesis nor a single inference step.

| Field | Type | Description |
|-------|------|-------------|
| `id` | string |  |
| `sub_goal` | string | The proposition or obstacle this segment addresses |
| `strategy` | string | The proof-strategic pattern employed: "reduction to finite-dimensional case via compactness", "inductive construction with strengthening", "diagonalisation against purported counterexamples" |
| `resolves` | [obstacle_id, …] | Explicit obstacles dispatched by this segment |
| `contributes_to` | segment_id | Parent segment, if nested |

The `inference_pattern` field operationalises Kitcher's _unification_ account: when the same schematic pattern (e.g. a diagonal argument, a compactness argument) is instantiated in multiple segments, the system can represent the explanatory connection across arguments — a form of cross-argument warrant reuse that is invisible at the node level.

### Level 3 — Argument Graph (macro)

The root structure encoding the global strategy.

| Field | Type | Description |
|-------|------|-------------|
| `id` | string |  |
| `thesis` | string | The principal claim under defence |
| `decomposition.strategy` | string | How the thesis was reduced to sub-goals: "necessary and sufficient conditions", "exhaustive case partition", "contrapositive + induction base/step" |
| `decomposition.sub_segments` | [segment_id, …] | The top-level segments |
| `global_obstacles` | [obstacle_id, …] | Known difficulties / counterexample candidates upfront |
| `status` | open \| complete \| failed \| retracted |  |

---

## Schema Integration and Validation Constraints

For automation and manipulation, the following structural invariants must be enforced at schema-validation time:

1. **Warrant completeness**: every node of type `deduction` must reference a formal warrant; abductive and inductive nodes require a source-credibility annotation.
2. **Motivation non-emptiness**: the `motivation` field is not optional for any node whose `inference.type` could have been replaced by an alternative valid inference (detectable by a coverage analysis over the warrant set).
3. **Teleological closure**: every `argument_segment` must reference at least one `obstacle_id` in the root `obstacles` registry; segments not resolving any registered obstacle are structurally suspect.
4. **DAG acyclicity**: the `depends_on` edges at both node and segment level must constitute a directed acyclic graph; cycles indicate circular reasoning.
5. **Discharge accounting**: every node with `epistemic_status: assumed` must appear in the `discharges` list of some downstream node, or be explicitly flagged as an unresolved assumption in `open_questions`.

---

## Explanatory Adequacy Conditions

Beyond validity and well-formedness, a reasoning representation is _explanatorily adequate_ if and only if it satisfies three conditions:

**C1 — Warrant transparency**: the principle licensing each inference is stated at the appropriate level of generality — neither so specific as to be uninformative (restating the instance) nor so general as to be trivially permissive.

**C2 — Motivational non-triviality**: the motivation annotation must identify a _contrastive choice_ — it must be capable of answering "why this inference rather than the alternative $\alpha$?" for at least one salient alternative $\alpha$. A motivation that reduces to "this is a valid inference" fails the condition; "this contrapositive formulation is chosen because the positive direction requires constructing $x$ with $P(x)$, for which no constructive method is available" satisfies it.

**C3 — Teleological coherence**: the sub-goal tree induced by `explanatory_function.sub_goal` and `segment.resolves` pointers must form a well-founded tree rooted at the principal thesis. Every leaf node must either close an assumption, discharge an obstacle, or contribute to an argument segment that does so. Steps satisfying none of these conditions are explanatorily idle and should trigger a validation warning.

---

## Partial Automation

This architecture supports several automated operations without sacrificing explanatory content:

- **Warrant verification**: type-theoretic or SMT-based checking of `deduction`-type nodes against declared warrants.
- **Obstacle coverage analysis**: checking whether all registered obstacles appear in some `segment.resolves` field.
- **Motivational gap detection**: flagging nodes whose `motivation` is structurally identical to the `warrant` (a heuristic proxy for condition C2 failure).
- **Explanation summarisation**: traversal of the macro-level `decomposition.rationale` and meso-level `segment.strategy` fields yields a human-readable proof sketch independent of the node-level detail — recovering the "key idea" that standard formats suppress.
- **Cross-argument schema extraction**: clustering segments by `inference_pattern` across multiple argument graphs surfaces reused argumentative schemas, supporting the kind of explanatory unification Kitcher identifies as constitutive of deep understanding.
