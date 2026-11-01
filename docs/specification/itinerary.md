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
| Steps: inputs | with every step | per input, its product type and a reference: a record identifier, the identifier of the step that produces the input, or a pointer for a `source` | a `hypothesis` produced by the step `propose`; the `data` of a phenomenon record | — |
| Steps: output | with every step | the product type of the product, and the record that holds the product, given while that record holds the output type | a `verdict` held by an assessment record | — |
| Steps: norm | with every step | the test named by the registry for the activity, written `norm.<activity>`, and its verdict: pass · fail · pending | `norm.testing`, pending until the assessment is stabilized | — |
| Steps: mode | when the step states its inference | deductive · inductive · abductive · analogical · non-inferential, equal to the mode of the activity | `abductive` for the step that proposes a candidate answer | — |

- **The command `gnomon itinerary` checks the steps and the fields of an itinerary.** An itinerary must meet the [conditions of a well-formed itinerary](../epistemology/processes/activities/epistemic-activities.md#^itinerary-check), read on the fields of its steps. These conditions and the conditions on the fields below compare types and identifiers only, so the check is decidable. The type of a referenced record follows from its present state: a question with a placeholder slot holds a `question-schema`. A target system at commitment `specified` holds a `target-specification`, and also an `identified-subject`. The command also checks six fields of the record: ^record-checks

    - the itinerary addresses a problem record or a question record;
    - the activity of each step is an identifier of the activity registry;
    - no two steps share an identifier;
    - an output reference, once given, names a record that holds the output type in its present state;
    - the norm of a step is the test of its activity, and a stated mode is the mode of the activity;
    - the verdict of each step is `pass`, `fail` or `pending`.

- **A verdict records a judgment outside the reach of the check.** Whether a norm is met depends on the content of the products: whether a test was severe, whether a definition is eliminable. The itinerary records that judgment as `pass`, `fail` or `pending`, whereas the check reads only whether the verdict is admitted.

- The [requested relation](../epistemology/objects/task/requested-relation.md) of the epistemic task selects one of the candidate relations between an explanans and the phenomenon, so the test `norm.explanation` reads that field.

- **The product-type registry states the coverage of each type by the records.** Each type carries a status: `exists`, when the type is held in full by a kind of record; `partial`, when a record holds part of the type; `to-create`, when no kind of record holds the type yet. The [table of product types](../epistemology/processes/activities/epistemic-activities.md#^product-types) lists the types, and the registry alone states their coverage. ^type-coverage

- **A product of a type without a record kind is reached through a step.** The product types are derived from the taxonomy of activities, so some types have no record kind yet, such as a design of experiments or a concept. An itinerary can take such a product as an input only as the output of one of its own steps. A `source`, by contrast, stays outside the records, so its reference is a pointer, left unresolved by the check.

- **A step references a record in its present state only.** The records keep no successive versions, so a step cannot reference a record at the state that the record had when the step ran. The [project goals](../../TODO.md) list this missing reference as `as_of`. The [order of specification](../epistemology/processes/inquiry/specification-order.md#^iteration-circularity) states why controlled iteration needs such versions. ^record-versions

- **A step references a product by the identifier of its step.** A product often has no record when the itinerary is written. Therefore, a later step names the step that produces it, and the check compares the declared output type of that step with the type expected by the later step. A record may also leave the state in which a step produced it, as a schema becomes a question once its slots are identified. Then, the step states its output type without a reference.

*Example*: the [itinerary of the inquiry into delayed generalization](../../examples/grokking-delayed-generalization/itinerary.yml) holds eight steps, from posing the problem to testing the candidate answer. Its step of background appraisal records the verdict `fail`, since no admitted law of that case yet states its origin.
