
# Argument bundles

To represent **paths of justification**, the architecture supports **argument assemblies** or **reasoning units**: explicit subgraphs constructed to answer a target question.

An argument bundle specifies:

- target question
- question decomposition
- selected assumptions
- imported objects (definitions, intermediate lemmas)
- dependency subgraph
- proof path or explanation path
- resulting answer or final conclusion
- limits of validity
- unresolved points

These are complementary to object registries ("databases"), and are closer to a structured argument graph. They are essential to avoid reconstructing the actual reasoning manually each time.

## Components

|Component|Role|
|---|---|
|**Argument bundle**|Structured subgraph assembled to answer one target question|
|**Question decomposition tree**|Parent-child decomposition of inquiry goals|
|**Minimal answer subgraph**|Smallest selected dependency-supporting subgraph for one answer|
|**Answer object / resolution package**|Consolidated response to one question|
|**Issue bundle**|Open dependencies, unresolved branches, missing proofs|
|**Alternative route bundle**|Competing decompositions or argumentative strategies|
|**Session task bundle**|Operational subset selected for one research session|

## Internal structure - Proposal 1

A minimal schema of an argument bundle is:

| Field              | Meaning                                           |
| ------------------ | ------------------------------------------------- |
| `target_question`  | question being answered                           |
| `purpose`          | proof, explanation, comparison, exploratory route |
| `selected_objects` | imported object IDs                               |
| `selected_edges`   | imported typed relations                          |
| `assumption_set`   | active assumptions                                |
| `entry_points`     | semantic prerequisites                            |
| `reasoning_path`   | ordered or partially ordered argumentative route  |
| `conclusion_set`   | resulting answer claims                           |
| `gaps`             | unresolved dependencies                           |
| `validity_limits`  | scope and exclusions                              |
| `status`           | maturity of the bundle itself                     |

## Internal structure - Proposal 2

For genuine understanding, a minimal sufficient format for each inferential step is the following:

|Field|Necessity|
|---|---|
|`inputs`|identifies dependencies|
|`output`|identifies result|
|`operation`|identifies inferential kind|
|`warrant`|identifies validity source|
|`local_goal`|identifies the subproblem being solved|
|`strategic_role`|identifies why the step matters globally|
|`gap_closed`|identifies the missing piece supplied by the step|
|`conceptual_effect`|identifies what changes in the problem representation|
|`alternatives_considered`|prevents arbitrariness|
|`status/confidence`|distinguishes proof, conjecture, heuristic, or empirical support|

## Reasoning as a typed graph - Proposal G

A linear sequence hides structure. A reasoning chain tis instead a **motivated argument graph** rather than a simple proof trace.

**Edge types**:

|Edge|Meaning|
|---|---|
|`supports`|one node justifies another|
|`uses`|one step depends on a definition, theorem, or datum|
|`answers`|a claim or subargument resolves a question|
|`refines`|a question is decomposed into more precise subquestions|
|`motivates`|a difficulty or objective prompts a move|
|`contrasts_with`|an alternative route is considered or rejected|
|`exemplifies`|an example clarifies a concept|
|`blocks`|an obstacle prevents a route|
|`reduces_to`|one problem is transformed into another|

## Insufficient fields - Proposal I

- `inputs` and `outputs` flatten several distinct roles that are not interchangeable. For example, in a proof or theoretical argument, the following are different:
	- a premise
	- a definition invoked to re-express the target
	- an obstacle showing why direct progress fails
	- an auxiliary lemma introduced to overcome that obstacle
	- a case split motivated by a structural distinction
	- an analogy used heuristically to identify a promising route
	
- `operation` is too compressed: "derive", "explain", "decompose", "eliminate" remain labels, not representations of actual reasoning.
	
- `warrant` answers: _why is this result licensed?_  But intelligibility also requires: *why was this route chosen?*