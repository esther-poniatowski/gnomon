---
tags:
  - specification
index: "[Specification](docs/specification/_index.md)"
aliases:
  - Itinerary record
  - Specifying the itinerary
---
# Itinerary record

> [!QUESTION] Goal: how are the steps of an inquiry recorded so that a check can tell whether each step takes what it needs and produces what the next step uses?

The itinerary record lists the steps of an inquiry. Each step instantiates one [epistemic activity](../epistemology/processes/activities/epistemic-activities.md): it names the activity, its input products, its output product, and the verdict of the norm that judges it. Two registries fix the content of a step. The [activity registry](../../src/gnomon/data/registries/activities.yml) gives each activity its input and output types, its norm, its mode and its context. The [product-type registry](../../src/gnomon/data/registries/product-types.yml) gives each type the record kinds that hold it. An itinerary addresses a [problem](problem.md) or a question.

| Specification | When it is required | Options or frame | Examples | Source |
| ------------- | ------------------- | ---------------- | -------- | ------ |
| Addresses | always | the identifier of one problem record or of one question record | the problem of the delay before generalization | — |
| Steps | always | one entry per activity instance, listed in any order | posing the problem, formulating the question, testing the candidate answer | [activity taxonomy](../epistemology/processes/activities/epistemic-activities.md) |
| Steps: id | with every step | a name unique within the itinerary, by which a later step refers to the output of this one | `pose`; `test` | — |
| Steps: activity | with every step | the identifier of one activity of the registry | `abduction`; `testing` | — |
| Steps: inputs | with every step | per input, its product type and a reference: a record identifier, the full identifier of the step that produces the input, or a pointer for a `source`; for a record, optionally the revision of the repository at which the step read it | a `target-claim` produced by the step `itin.grokking.explain-delay.propose`; the `data` of a phenomenon record | — |
| Steps: output | with every step | the product type of the product, and the record that holds the product, given while that record holds the output type; for a `knowledge-state-change`, also the revision of the repository before the change, whose status of the record differs from its present status | a `verdict` held by an assessment record | — |
| Steps: derivation | for a step whose reasoning a [derivation record](derivation.md) holds, and always once a step of the activity `derivation` passes its norm | the identifier of the derivation record; one of its consequences is recorded in the output record of the step, since the norm of the step judges that derivation as a whole | `derivation.grokking.delay-scale` | — |
| Steps: norm | with every step | the test named by the registry for the activity, written `norm.<activity>`, its verdict: pass · fail · pending, and, once judged, the evidence and the date of the judgment | `norm.testing`, pending until the assessment is stabilized | — |
| Steps: rationale | with every step | the question that the step serves, or its problem for a step that precedes any question, and the object on which the step acts: one of the eight [conditions for obtaining an answer](../epistemology/objects/question/conditions-of-answerability.md#^eight-conditions) (definiteness · answer-type · soundness · candidates · discrimination · access · bridging · representation), the obtaining of the answer (obtaining), or its evaluation (evaluation) | `quest.grokking.explain-delay`, acting on the candidates | [choice of the next act](../procedures/inquiry/next-act.md) |
| Steps: branch | for a step taken under a condition | the condition under which the step is taken, and the step taken when the condition fails, which produces the same output type | a simulation taken when no closed form is found, otherwise the derivation | [constructors of an itinerary](../epistemology/processes/activities/epistemic-activities.md#^itinerary-constructors) |
| Steps: iterate | for a step repeated on its own output | the criterion that ends the repetition | a fitting repeated until the residuals fall below the tolerance of the question | [constructors of an itinerary](../epistemology/processes/activities/epistemic-activities.md#^itinerary-constructors) |
| Steps: revises | for a step that revises a record | the record revised, the [kind of the revision](../epistemology/objects/knowledge/grounds-and-dependence.md#^revision-kinds): retraction · scope-narrowing · scope-generalization · reorientation · taxonomic-restructure · correction, and per flagged dependent reviewed, its state: pending · revised · unaffected · retracted | the retraction of a background law, with the answers resting on it reviewed one by one | [revision accountability](../adr/revision-accountability.md#^flag-not-edit) |
| Steps: mode | when the step states its inference | deductive · inductive · abductive · analogical · error-statistical · model-based · non-inferential, equal to the mode of the activity | `abductive` for the step that proposes a candidate answer | — |

- **The stage of an itinerary is computed, not recorded.** The view `itinerary-progress` of `gnomon views` reports, per itinerary, the addressed record and the stage: planned · in-progress · concluded · abandoned. The stage follows from the steps and from the status of the addressed record, as the [stages of an itinerary](../epistemology/processes/activities/epistemic-activities.md#^itinerary-stages) define it, so the record holds no field for it.

- **The command `gnomon itinerary` checks the steps and the fields of an itinerary.** An itinerary must meet the [conditions of a well-formed itinerary](../epistemology/processes/activities/epistemic-activities.md#^itinerary-check), read on the fields of its steps. These conditions and the conditions on the fields below compare types and identifiers only, so the check is decidable. The type of a referenced record follows from its kind, from its present state, and from the fields that hold the type, which the [registry of product types](../../src/gnomon/data/registries/product-types.yml) names: a question with a placeholder slot holds a `question-schema`, and a model holds a `consequence` only through a law marked `derived`. A target system at commitment `specified` holds a `target-specification`, and also an `identified-subject`. The command also checks six fields of the record: ^record-checks

    - the itinerary addresses a problem record or a question record;
    - the activity of each step is an identifier of the activity registry;
    - no two steps share an identifier;
    - an output reference, once given, names a record that holds the output type in its present state;
    - the norm of a step is the test of its activity, and a stated mode is the mode of the activity;
    - the verdict of each step is `pass`, `fail` or `pending`, and a verdict `pass` or `fail` states its evidence and the date of its judgment;
    - an input that states a revision names a record readable at that revision, which holds the input type in that state;
    - the rationale of a step serves a question or a problem record;
    - a branch states its condition and names a step of the same output type, and an iterated step takes its own output type as an input.

- **A verdict records a judgment outside the reach of the check.** Whether a norm is met depends on the content of the products: whether a test was severe, whether a definition is eliminable. The itinerary records that judgment as `pass`, `fail` or `pending`, with the evidence on which it rests and the date on which it was made, whereas the check reads only whether the verdict is admitted and justified. Judging a norm is therefore an act recorded in the step that it judges, not an activity of its own: its output is an attribute of the step, not an epistemic object. A later judgment replaces the verdict, and the history of the repository keeps the earlier one. ^verdict-judgment

- The [requested relation](../epistemology/objects/task/requested-relation.md) of the epistemic task selects one of the candidate relations between an explanans and the phenomenon, so the test `norm.explanation` reads that field.

- **The product-type registry states the coverage of each type by the records.** Each type carries a status: `exists`, when the type is held in full by a kind of record; `partial`, when a record holds part of the type; `to-create`, when no kind of record holds the type yet. The [table of product types](../epistemology/processes/activities/epistemic-activities.md#^product-types) lists the types, and the registry alone states their coverage. ^type-coverage

- **A product of a type without a record kind is reached through a step.** The product types are derived from the taxonomy of activities, so some types have no record kind yet, such as an inter-theory relation. An itinerary can take such a product as an input only as the output of one of its own steps. A `source`, by contrast, stays outside the records, so its reference is a pointer, left unresolved by the check.

- **A step references a record at the revision at which it read it.** The records keep no successive versions, and the history of the repository keeps every earlier state, as the [decision on versions](../adr/versions-and-history.md#^git-keeps-history) states. An input therefore names, by `as_of`, the revision of the repository at which the step read its record, and the check reads the record at that revision, so a step stays valid once the record is revised. An input without `as_of` names the record in its present state. The [order of specification](../epistemology/processes/inquiry/specification-order.md#^iteration-circularity) states why controlled iteration needs such states. ^record-versions

- **A step references a product by the full identifier of its step.** A product often has no record when the itinerary is written. Therefore, a later step names the step that produces it, by the identifier of the itinerary followed by that of the step, as the [decision on dotted identifiers](../adr/dotted-identifiers.md) fixes, and the check compares the declared output type of that step with the type expected by the later step. A record may also leave the state in which a step produced it, as a schema becomes a question once its slots are identified. Then, the step states its output type without a reference.

*Example*: the [itinerary of the inquiry into delayed generalization](../../examples/grokking-delayed-generalization/itinerary.yml) holds nine steps, from posing the problem to testing the candidate answer. Its step of background appraisal records the verdict `fail`, since no admitted law of that case yet states its origin.
