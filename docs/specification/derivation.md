---
tags:
  - specification
index: "[Specification](docs/specification/_index.md)"
aliases:
  - Derivation record
---
# Derivation record

> [!QUESTION] Goal: what does a researcher write in each field of a derivation record, and when is each field required?

A derivation record holds the reasoning that establishes a consequence from premises, below the grain of a product. It states the sought, the posits, the moves with their warrants, the orientations selecting the moves, the interpretations of the items, the segments and the outcomes of the derivation. The [theory of derivations](../epistemology/objects/derivation/_index.md) states the concepts behind these fields, and the [decision on the derivation record](../adr/derivation-record.md) states why the derivation is a record of its own. ^derivation-record

Each unit of the record carries a descriptive identifier, unique within the record, so that a move, an orientation or an interpretation can name the unit taken, selected or interpreted. A reference to a premise held by another record takes the dotted form of a unit of that record, such as `mod.grokking.effective-representation.representation_flow`. ^derivation-identifiers

Three properties are read from other fields, so that no field restates them:

- the **degree of determinacy** of a sought: open when its type is empty, typed when only its type is filled, determinate when its type and its condition are filled;
- a **lemma**: a consequence whose field `answers` names a subordinate sought;
- the **item** of an interpretation, read from the unit interpreted: an object of form `object`, an object of form `expression`, a move, a feature of the calculation, or a composite for a segment or a consequence.

| Specification | When it is required | Content | Examples |
| ------------- | ------------------- | ------- | -------- |
| Serves | when the derivation serves a question, a proof obligation, or a law or an operation stated in advance | the identifier of the record served, from which the root sought is read; empty for a derivation that constructs its result | `quest.grokking.explain-delay` |
| Runs on | always | the records that hold the premises: models, backgrounds, the target system or an answer | `mod.grokking.effective-representation` |
| Uses | when the derivation uses the consequences of another derivation | one identifier per derivation used | `derivation.grokking.mode-spectrum` |
| Sought | when the derivation serves no record | the root sought, with its identifier, its statement, its type and its condition; a derivation that serves a record reads its root sought from that record and leaves this field empty | — |
| Sought: id | with the sought | a descriptive identifier of the root sought | `delay-scale` |
| Sought: statement | with the sought | the unknown or the statement sought, in one phrase | the law that sets the scale of the delay after fitting |
| Sought: type | once the type of the unknown is known | `law` · `value-or-bound` · `object` · `classification` · `claim-truth` | `law` |
| Sought: condition | once the condition is known | the condition that the unknown satisfies | in the linear relaxation of the effective theory |
| Subordinate soughts | when the derivation sets a sought for itself | one entry per subordinate sought | the time at which the quality reaches its threshold |
| Subordinate: id | in each entry | a descriptive identifier | `crossing-time` |
| Subordinate: statement | in each entry | the unknown or the statement sought | the time at which the quality of the representation reaches its threshold |
| Subordinate: type | once the type of the unknown is known | as for the root sought | `value-or-bound` |
| Subordinate: condition | once the condition is known | the condition that the unknown satisfies | the slowest structured mode has decayed by the factor that the closure fixes |
| Subordinate: replaces | when the sought replaces an ill-posed one | the identifier of the sought replaced | `exact-crossing` |
| Subordinate: reason | with a replacement | why the earlier sought was ill-posed | the threshold is not crossed at one sharp time |
| Slots | when a move or a posit introduces an unknown | one entry per slot, which a later move binds | the amplitude of an eigenmode |
| Slots: symbol | in each entry | a symbol unique within the record | `a_mode` |
| Slots: reading | in each entry | what the slot stands for | the amplitude of one eigenmode of the effective Hessian |
| Slots: introduced by | in each entry | the identifier of the move or the posit that introduces the slot | `diagonalize` |
| Objects | always | one entry per intermediate object that a move takes or yields | — |
| Objects: id | in each entry | a descriptive identifier | `mode-decay` |
| Objects: form | in each entry | `object` · `expression` | `expression` |
| Objects: expression | when the object is formalized | the object in the expression syntax, over the symbols that the derivation sees | `exp(-eta_rep * lambda3 * step)` |
| Objects: reading | in each entry | the object stated in one phrase | each eigenmode decays exponentially at its own rate |
| Posits | when the derivation introduces a premise on trial | one entry per posit, with its origin and its tests | — |
| Posits: id | in each entry | a descriptive identifier | `quality-tracks-slow-mode` |
| Posits: kind | in each entry | `ansatz` · `closure` · `relevant-quantities` · `complete-similarity` · `incomplete-similarity` | `closure` |
| Posits: statement | in each entry | the form or the relation assumed | the quality reaches its threshold once the slowest mode has decayed by a fixed factor |
| Posits: origin | in each entry | the source of the guess | — |
| Posits: origin: kind | in each entry | `act` · `source` · `scheme` · `none` | `source` |
| Posits: origin: ref | unless the origin is `none` | the step, the source or the scheme | Liu et al., NeurIPS 2022 |
| Posits: tests | once a test is made | one entry per test, with its verdict | — |
| Posits: tests: kind | in each entry | `consistency` · `limit` · `exact` · `approximation` · `empirical` · `computation` | `empirical` |
| Posits: tests: verdict | in each entry | `supports` · `refutes`; a test that refutes is the refutation of its posit | `supports` |
| Posits: tests: standard | for a computation | `certified` · `numerical` | `numerical` |
| Posits: tests: by | in each entry | the move, the record or the source that carries the test | `mod.grokking.effective-representation.generalization_link` |
| Moves | always | one entry per move stated: every [non-routine move](../epistemology/objects/derivation/move.md#^non-routine), and each routine move that no segment bridges | — |
| Moves: id | in each entry | a descriptive identifier | `slowest-dominates` |
| Moves: kind | always, in each entry | one of the [atomic kinds of move](../epistemology/objects/derivation/move.md) | `take-limit` |
| Moves: inputs | always, in each entry | the objects, the posits or the premises taken | `mode-decay` |
| Moves: outputs | always, in each entry | the objects yielded | `slowest-mode` |
| Moves: binds | when the move binds a slot | the symbols of the slots bound | `a_mode` |
| Moves: warrant | in each entry | the license of the move | — |
| Moves: warrant: source | always, in each entry | `definition` · `theorem` · `approximation` · `computation` · `act-verdict` | `approximation` |
| Moves: warrant: cites | when a definition, a theorem, a record or a step licenses the move | the item cited | dominance of the slowest positive mode of a linear relaxation |
| Moves: warrant: error | always, in each entry | `exact` · `controlled` · `uncontrolled` · `singular` | `controlled` |
| Moves: warrant: regime | when the error is not exact | the regime in which the warrant holds | times long compared with the inverse of the spectral gap |
| Moves: warrant: applies because | when a property of the objects makes the warrant apply | the identifier of a structural or magnitude interpretation established before the move | `spectral-gap` |
| Kernel | when the derivation has a kernel | the identifier of the move declared as kernel, which the kernel test checks | `slowest-dominates` |
| Orientations | for each non-routine move and each segment | one entry per orientation | — |
| Orientations: id | in each entry | a descriptive identifier | `isolate-slow-mode` |
| Orientations: of | in each entry | the identifier of the move or the segment selected | `slowest-dominates` |
| Orientations: purpose | in each entry | the end, written as a goal: "to …" | to isolate the mode that sets the long-time behavior |
| Orientations: determines | when the purpose determines a sought | the identifier of that sought; either this field or `change` | `crossing-time` |
| Orientations: change | when the purpose is an intended change | `eliminate` · `decouple` · `isolate` · `reduce` · `expose` · `close` · `match`; either this field or `determines` | `isolate` |
| Orientations: occasion | when the purpose does not follow from the sought alone | the identifier of the interpretation that makes the purpose relevant now, established before the move | `spectral-gap` |
| Orientations: means | optional | the kind of move, the scheme or the act called for | take the limit of long times |
| Orientations: alternatives | when moves were set aside | one entry per move set aside | — |
| Orientations: alternatives: move | in each entry | the move set aside | integrate the nonlinear effective dynamics numerically |
| Orientations: alternatives: reason | in each entry | `inapplicable` · `inconsistent` · `costlier` · `losing-information` · `tried-without-success` | `costlier` |
| Orientations: provenance | in each entry | `contemporaneous` · `reconstructed` | `reconstructed` |
| Orientations: expected gain | optional | the gain expected from the move | one rate in place of the whole spectrum |
| Interpretations | when the record assigns a meaning | one entry per meaning, with a pair of item and kind among the [admitted pairs](../epistemology/objects/derivation/interpretation.md#^admitted-pairs) | — |
| Interpretations: id | in each entry | a descriptive identifier | `spectral-gap` |
| Interpretations: of | in each entry | the identifier of the item interpreted | `mode-decay` |
| Interpretations: kind | in each entry | `referential` · `form` · `process` · `structural` · `magnitude` · `variation` · `analogical` · `diagnostic` | `magnitude` |
| Interpretations: reading | in each entry | the meaning assigned, in one sentence | at long times the slowest positive mode dominates |
| Interpretations: grounds | when the kind requires a ground that the record can cite | the references of the type that the kind requires: a declared symbol for a referential meaning, a law for a process, an expression of the ordering for a magnitude, the known law or source for an analogy, and the move or the posit whose failure it reveals for a diagnostic interpretation | `mod.grokking.effective-representation.Hrep` |
| Features of the calculation | when the calculation exhibits an event that a diagnostic interpretation reads | one entry per event | — |
| Features: id | in each entry | a descriptive identifier | `zero-mode` |
| Features: kind | in each entry | `divergence` · `secular-term` · `zero-mode` · `sign-change` · `crossing` | `zero-mode` |
| Features: at | in each entry | the identifier of the object at which the event occurs | `mode-decay` |
| Segments | when moves group under one idea, or when a segment bridges omitted moves | one entry per segment | — |
| Segments: id | in each entry | a descriptive identifier | `relaxation` |
| Segments: moves | in each entry | the moves stated inside the segment | `diagonalize`, `slowest-dominates` |
| Segments: inputs | always, in each entry | the objects or the premises consumed | `mod.grokking.effective-representation.representation_flow` |
| Segments: outputs | always, in each entry | the objects produced | `delay-law` |
| Segments: applies | when the segment applies a scheme | the identifier of a design of kind `scheme` | `design.grokking.slowest-mode-relaxation` |
| Segments: within | when the segment is nested | the identifier of the enclosing segment | `relaxation` |
| Consequences | when the derivation establishes a statement | one entry per consequence; a consequence answering a subordinate sought is a lemma | — |
| Consequences: id | in each entry | a descriptive identifier | `delay-law` |
| Consequences: answers | in each entry | the identifier of the sought answered, or the record served for the root sought of a derivation that serves one | `delay-scale` |
| Consequences: from | in each entry | the identifier of the object that states the consequence | `delay-law` |
| Consequences: record | for a consequence of the root sought, unless the derivation serves the law or the operation that states it; for a lemma, once it holds beyond the derivation | the law, the answer or the obligation that states it, as the [records of a consequence](../epistemology/processes/activities/model-analysis.md#^consequence-records) list them; a law named here is marked derived | `mod.grokking.effective-representation.representation_time` |
| Consequences: gain | optional | the gain obtained | the delay is read from one spectral quantity of the effective Hessian |
| Consequences: principle | optional | the identifier of the variation interpretation that names the property making the consequence hold | `rate-variation` |
| Consequences: pattern | optional | the scheme applied, with the other problems within its reach | the slowest mode of a stable linear relaxation sets its relaxation time |
| Impasses | when a sought stays without answer | one entry per impasse | — |
| Impasses: sought | in each entry | the identifier of the sought left without answer | `crossing-time` |
| Impasses: obstacle | in each entry | the identifier of the diagnostic interpretation that names the obstacle | `nonlinear-quality` |
| Refutations | when a counterexample of the derivation shows a statement to fail | one entry per counterexample; a refuting test of a posit is recorded among the tests of the posit | — |
| Refutations: target | in each entry | the posit, the consequence or the claim refuted | `quality-tracks-slow-mode` |
| Refutations: by | in each entry | the object that is the counterexample | `slow-mode-counterexample` |

The checks of a derivation read these fields as follows. This list is the one statement of the checks, and each rule carries the identifier that a finding reports: ^derivation-checks

- every identifier named inside the record resolves to a unit of a list that its field admits, as the schema declares by the key `x-units`, and every dotted reference resolves to a record of the workspace (`derivation/unknown-unit`); no two units share an identifier (`derivation/repeated-unit`);
- a derivation that serves a record neither declares a root sought nor names the record served as the record of a consequence (`derivation/restated-fact`);
- each interpretation pairs its item with an admitted kind, a unit of another record being an object or an expression (`derivation/unadmitted-pair`);
- a warrant cites a structural or magnitude interpretation, an impasse a diagnostic one, and a consequence a variation one as its principle, and the grounds of each interpretation cite a reference of the type that its kind requires (`derivation/mistyped-ground`);
- the moves and the segments form no cycle (`derivation/cycle`), and no segment encloses itself, nor any subordinate sought replaces itself, through a cycle (`derivation/cyclic-nesting`);
- the occasion of an orientation (`derivation/retrospective-orientation`) and the property that a warrant cites (`derivation/retrospective-license`) interpret only objects established before their move or segment;
- each orientation states exactly one of `determines` and `change` (`derivation/ambiguous-purpose`), and each non-routine move and each segment has an orientation (`derivation/unoriented-move`);
- each move of a segment takes only what the segment takes or what its moves yield (`derivation/broken-bridge`), and a segment applies a design of the kind `scheme` (`derivation/misapplied-scheme`);
- the declared kernel lies on every route from the premises to each consequence of the root sought (`derivation/failed-kernel`);
- each consequence is stated by an object that a move or a segment yields (`derivation/unreached-consequence`);
- each move yields something that it does not take, and its outputs reach an outcome, a test of a posit or an interpretation cited by the record (`derivation/idle-move`);
- each consequence of the root sought names its record, unless the derivation serves the law or the operation stating it (`derivation/unrecorded-consequence`), and a law named as the record of a consequence is marked derived (`derivation/underived-record`);
- each slot is bound by a move, unless an impasse stops the route that the slot opens (`derivation/unbound-slot`);
- each law marked derived names a derivation stating it as a consequence, or a published origin (`derivation/unrecorded-descent`), and a law whose descent a derivation records lists no units that it requires, since the derivation states its premises (`derivation/restated-premises`).
