---
tags:
  - specification
index: "[Specification](docs/specification/_index.md)"
aliases:
  - Question record
---
# Question record

> [!QUESTION] Goal: what does a researcher write in the top-level fields of a question record, and how does the commitment of its slots fix the type of the record?

The question record names its problem when one exists and the external material that states or motivates it. The record also names linked questions. The relations of each link are defined with the [linked questions](../epistemology/objects/question/question.md#^linked-questions).

| Field | When it is required | Content | Example |
| ----- | ------------------- | ------- | ------- |
| Title | always | a short name of the question, as a label | delay before generalization |
| Statement | always | the question in words, restating its fields in the [statement frame](../epistemology/objects/subject/subject-of-inquiry.md#^question-statement); `gnomon views` composes the same frame from the fields, for comparison with this statement | "in overparameterized networks trained to fit their data, what produces the delay before generalization?" |
| Status | always | posed · refined · answered · dissolved · abandoned, as the [stages of a question](../epistemology/objects/question/question.md#^question-stages) define them | `posed`, for a question not yet refined |
| Version | always | a positive whole number, `"1"` when the question is first posed and raised by one at each [revision of the specification](#^question-version) | `"2"`, after the tolerance was revised |
| Addresses | when a problem record states the problem that the question serves | the identifier of one problem record | the problem of the delay before generalization |
| Sources | when existing material states or motivates the question | per source, a pointer to an existing note, publication, model or data set; the pointer imports no content and assigns no epistemic kind | a section of a research note that states the question |
| Request | to make the record a question rather than a schema | how many possible answers a direct answer selects, and whether it claims completeness: one · all · over-a-parameter · decision, as the [request of a question](../epistemology/objects/question/question-specification.md#^question-request) defines them; the request of the problem that the question serves, when one exists | `one`, for a question that one explanatory account answers |
| Links | when the answer to another question bears on this one | per link, the other question, the relation, and the record shared by the two questions | — |
| Links: question | with every link | the identifier of the other question record | the question that describes the representation geometry of a network |
| Links: relation | with every link | subquestion-of · explanans-from · presupposes · enables | `explanans-from`, for a question that explains a readout capacity by that geometry |
| Links: via | when the two questions share a record | the identifier of the shared record, such as a phenomenon | the phenomenon record of the geometry |
| Excludes | when the question leaves out a part of its answer | per part, its identifier, its kind: deferred · out-of-scope, the question of the part when one is posed, its reading and its reason, as the [parts left out by a level](../epistemology/processes/inquiry/question-decomposition.md#^excluded-parts) define them | the dependence on the noise level, deferred until the noiseless case is settled |
| Presuppositions | for a presupposition that neither a link `presupposes` nor the evidential status of the phenomenon states | per presupposition, its part of [soundness](../epistemology/objects/question/conditions-of-answerability.md#^eight-conditions): existence · topic, its reading and, once formalized, its expression | a stable fixed point exists for every admitted gain (existence) |
| Construction | when a procedure is named that would yield a direct answer | the procedure, a design of kind `method` or a pointer, and how it would yield a direct answer; the [route of construction](../epistemology/objects/question/conditions-of-answerability.md#^routes) is then diagnosed | an algorithm that enumerates the fixed points of the network at each gain |
| Answerability | for each condition whose state the inquiry asserts | per condition, its route: selection · construction · both, for definiteness its term, its [state](../epistemology/objects/question/conditions-of-answerability.md#^condition-states): established · refuted, for a refutation its kind: outright · lack-of-means, with every means considered and tried, and the pointers that show the state; a condition left out is not established | access refuted for lack of means, after a mean-field derivation and a simulation both failed |

- **A problem is recorded in its own record.** Its fields, and the field by which a question names its problem, are specified in the [problem record](problem.md).
- **A source remains external until the inquiry needs its content.** A source pointer identifies the existing material that states or motivates the question. The pointer does not copy the material or classify any passage as a Gnomon object. ^question-sources
- **The version of a question names the specification against which it is assessed.** Each assessment names, in `against_version`, the version that it read, and a check reports the assessment void once the version of the question differs, as the [rule on tests fixed before evaluation](../epistemology/objects/answer/satisfaction-conditions.md#^tests-fixed-before) requires. The version is raised by one at each revision, a change that can alter which statements are direct answers or which tests apply: ^question-version
    - the subject: its target system, phenomenon and background, its contrast, its domain, and a revision of a record that it names when the revision changes a quantity, an observable, a reference class or an admitted law that a test reads;
    - the task: its epistemic aim, explicandum, requested relation, function sense, modal strength, admissible explanans, required accuracy and proof obligations;
    - the virtues and their standing;
    - beside the layers, the request, the links `explanans-from`, the presuppositions, the parts out of scope in `excludes`, and a maturity marker that leaves `open` on any of these fields.

  A change of the title, of the status, of a source pointer, of the answerability, of the construction, of another link, of a deferred part, or of the wording of a justification revises nothing, and neither does a migration of the format or a renaming of an identifier that leaves its referent unchanged. A revision is made in one commit that raises the version, and recorded by a step `question-revision` of the itinerary, whose question input names by `as_of` the revision at the earlier version, and whose review flags each assessment of the question. Each assessment reported void is then renewed against the new version, or retracted.
- **The steps that answer a question are recorded in an itinerary.** An [itinerary](itinerary.md) lists the activities that lead from a problem to its questions, and from a question to its answers and their assessments. The itinerary check verifies that each step takes the types of product required by its activity.

The commitment of a slot takes one of the [levels of commitment](../epistemology/objects/question/question.md#^commitment-levels) defined for a question. Each level is decided by one check over the records: ^commitment-checks

| Level | Check |
| --- | --- |
| `placeholder` | the type of the placeholder belongs to the [admitted types](question-subject.md#^placeholder-slots) |
| `identified` | the record exists and states its identification |
| `specified` | the required fields are filled, and every symbol resolves |

- **The slots of a question admit a placeholder.** The rule is stated under [placeholders before records](question-subject.md#^placeholder-slots).
- **The type of a question record follows the commitment of its slots.** When any slot holds a placeholder, or the request is not fixed, the record is a `question-schema`. When every slot is `identified` or `specified` and the request is fixed, the record is a `question`. The two take the same fields.
