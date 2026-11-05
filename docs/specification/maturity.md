---
tags:
  - specification
index: "[Specification](docs/specification/_index.md)"
aliases:
  - Maturity of a field
---
# Maturity of a field

> [!QUESTION] Goal: how does a record mark the maturity of each of its fields?

The field `maturity` is carried by every record kind except the itinerary: target system, background, phenomenon, question, operators, model, binding, key, answer, assessment, problem, concept, design and derivation.

Each specification may also carry its own maturity marker (open, provisional, or stabilized). A marker `open` carries a comment naming one of the [three reasons for an open specification](../epistemology/objects/status/statuses-and-acceptance.md#^open-reasons). A specification left unmarked takes the maturity that the status of its record states, for the records whose status is a maturity. In an answer, a problem or a question, whose status is an attitude or a stage, it takes the maturity `provisional`, as the [record attributes](../epistemology/objects/question/question.md#^record-attributes) state.

A key of `maturity` is the path of a field. Its segments are joined by dots from the root of the record, and a segment names a field of a mapping. Inside a list, a segment names either one entry, by its `symbol` or its `id`, or a field of the entries. A path through a field of the entries marks that field in every entry. For instance, `manifestations.form` marks the form of every manifestation, and `observables.Z.values` marks the value set of the observable `Z` alone. A field is named when the schema of the record declares it, so a field of a list without entries can be marked. An entry, by contrast, is named only when the record holds it. The check reports a key naming no field under the rule `completeness/misplaced-maturity`. ^maturity-keys

The reasons for admitting empty and immature fields are stated under the [safeguards against rigidity](../epistemology/objects/subject/subject-of-inquiry.md).
