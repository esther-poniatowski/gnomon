---
tags:
  - specification
index: "[Specification](docs/specification/_index.md)"
aliases:
  - Validation scopes
---
# Validation scopes

> [!QUESTION] Goal: which completion target should govern the check of a partial inquiry?

Validation scopes let a caller state how far Gnomon checks a partial inquiry. Their order follows the [inquiry stages](../epistemology/processes/inquiry/specification-order.md#^specification-stages). At the final endpoint, Gnomon checks each authored assessment record.

The caller must select one scope explicitly. The [scope-selection rationale](../adr/registries-as-source.md) explains why the scope must be explicit.

## Ordered scopes

A scope identifies one checkpoint and defines its completed inquiry state.

| Scope identifier | Basis | Completion point |
| --- | --- | --- |
| `problem-posed` | Problem | the problem record states the demand that the inquiry serves |
| `question-typed` | Question schema | serving questions use typed placeholders and fix the epistemic task as far as required |
| `subject-identified` | Identified subject | descriptions and pointers fix the referents of the system and phenomenon |
| `subject-specified` | Background and specified subject | the background states every subject detail demanded by a current open condition |
| `candidate-proposed` | Candidate product | the inquiry proposes a candidate answer or a construct demanded directly by the problem |
| `candidate-assessed` | Assessment endpoint | assessment records state verdicts against the specification version fixed before evaluation |

^ordered-validation-scopes

## Requirement increments

Requirements become current according to their declaration. A `checkpoint_records` entry applies only at its named scope. Therefore, a question-led project can pass `question-typed` without an artificial problem record. A `required_records` or `required_unless_aim` entry remains current at that scope and every scope that follows. An `activate_when_present` entry applies the ordinary clauses of a present record from its named scope onward, but it does not require that record to exist. Unconditional paths, minimum commitments and settled states remain current from the first scope that declares them. The experimental checker cannot yet activate `on_demand` paths or commitments from open conditions.

Independently of completion requirements, every scope retains the checks of record contracts, identifier syntax and references. Therefore, the selected target cannot make an invalid present record admissible.

- **`problem-posed`:** requires a problem record
- **`question-typed`:** requires a question record with its schema-defining fields, adds task fields selected by its aim and activates an itinerary
- **`subject-identified`:** requires an identified target system and an identified phenomenon, except that exploration may retain a phenomenon placeholder
- **`subject-specified`:** declares paths and stronger subject commitments on demand, adds the fields selected by exploration or prediction and activates background and operator records
- **`candidate-proposed`:** requires the candidate selected by the demand, requires the question request for an answer and activates supporting candidate records
- **`candidate-assessed`:** requires the applicable answer tests or construct constraints and requires every applicable verdict to be settled

^scope-requirement-sets

## Scoped results

At the selected scope, missing content due at that scope or any preceding scope produces a `method-conformance finding`. Missing content due at a subsequent scope produces future work with the result class `computed inquiry diagnosis`. All defects outside missing-content rules remain current, including contract, identifier and reference defects.

The text report lists future work and counts it separately. The YAML report records the selected `scope`, the count `future` and the entries `future_work`. Each entry states:

- the due scope;
- the source location: file, record identifier, record kind and field path;
- the message.

The Static Analysis Results Interchange Format (SARIF) log contains only current findings because future work has no defect identity, rule, severity or repair condition. When a scope is selected, the run property `gnomon/validationScope` names that completion target and states that later requirements remain future work. A consumer can therefore display the active target even when the result list is empty. This context is not a finding and does not change the exit status.

Without `--scope`, the command preserves the unscoped behavior. Every finding on a present record remains current. Absent records and future work remain outside the unscoped result.
