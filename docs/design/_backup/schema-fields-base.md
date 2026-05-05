# Schema & Fields

## Criteria 

Each type should define:

- required fields (hard constraints),
- optional fields (soft extensions),
- field types (controlled vocabularies for machine-parsable fields, free-form markdown for descriptive fields),
- inter-object invariants (e.g., a `proof` object must reference exactly one `theorem` or `lemma` in its `proves` field, and all `uses` references must resolve to existing IDs).

These invariants are formally analogous to interface contracts in design-by-contract methodology.

Avoid fields whose values are ontologically heterogeneous or vague. Each field should point either to:

- a scalar or enumeration
- an embedded record
- a reference to another core object
- a typed list of such references

## Proposal-1

Distinguish:

- **identity**
- **content**
- **relations**
- **status**
- **operational metadata**

A generic schema could contain the following common fields.

|Field|Function|
|---|---|
|`id`|stable identifier|
|`type`|object type|
|`title`|short human-readable label|
|`statement` or `content`|main payload|
|`status`|epistemic status|
|`scope`|domain of validity or intended use|
|`tags`|auxiliary retrieval labels|
|`relations`|typed links to other objects|
|`relevance`|relation to target questions|
|`sources`|origin or provenance|
|`version`|revision control|

Then each type receives specialized fields.

_Examples_:

|Object|Fields|
|---|---|
|**Question**|- target form of answer  <br>- motivation  <br>- parent question  <br>- subquestions  <br>- stopping criterion|
|**Definition**|- formal statement  <br>- informal intuition  <br>- notation  <br>- dependencies  <br>- contrasts with nearby concepts|
|**Proof**|- proposition proved  <br>- assumptions used  <br>- strategy  <br>- intermediate lemmas  <br>- proof body  <br>- gaps|
|**Mechanism**|- explanandum  <br>- operative components  <br>- causal or logical structure  <br>- assumptions  <br>- predicted consequences  <br>- examples  <br>- competing mechanisms|

### Status (Epistemic Maturity)

Every object carries an explicit `status` field encoding its **epistemic maturity**: ==TODO: define a precise, non-overlapping set of status values==

- `draft`
- `provisional`
- `informal`
- `validated` / `established` / `verified` / `machine_checked`
- `refuted`
- `deprecated` / `superseded`
- `open`

Thereby, the dependency graph can distinguish whether a chain of reasoning rests on:

- established results
- speculative ideas
- provisional heuristics
- failed attempts
- tentative claims
- partial proofs
- competing formulations
- unresolved ambiguities
- obsolete paths
- alternative assumptions
- conjectures

### Relevance

To avoid side questions that are not epistemically necessary, operational relevance criteria are a first-class design principle.

For each object, a compact relevance schema could include: ==TODO: approve or simplify the following schema if overly complex==

1. **Relevant to what target question** (`target_question_id`)
    
2. **Relevant in what role** (`relevance_kind`): ==TODO: define a precise, non-overlapping set of relevance roles==
    
    - **logical / justificatory necessity**: object required for derivation
    - **semantic dependency**: object needed to interpret another object
    - **methodological dependency**: object needed because a chosen method presupposes it
    - **contextual usefulness**: object helps understanding but is not necessary
    - **expository usefulness**: object useful only for presentation
    - **historical relevance**: object explains origin of an idea but is not required for the target reasoning
    
3. **Epistemic necessity** (`epistemic_necessity`) encoding how critically the object participates in the main argument
    
    - load_bearing, supporting, illustrative, dispensable
    - necessary, useful, optional, irrelevant
    
4. **Under which assumptions** (`conditions`)

These encode why an object matters for a target. ==TODO: how the properties below connect to the relevance fields? are they redundant or reformulations?==

_Examples_:

- `necessary_for_target`
- `optional_for_target`
- `excluded_from_scope`
- `background_only`
- `open_dependency`
- `priority_level`

The combination of two fields (epistemic maturity and epistemic necessity) with the dependency graph enables automated identification of the weakest links in the argument chain — the most critical objects with the lowest proof status.

### Scope and boundary

For each major question or project branch, a scope could state: ==TODO: define a precise, non-overlapping set of scope fields==

- target question
- included subquestions
- excluded subquestions or issues
- admissible evidence types or methods
- required form of answer
- stopping criteria

This is architecturally analogous to an interface or contract delimiting a module.


# Proposal-2

All canonical object types should probably share a common abstract contract of the following form:

|Field|Role|
|---|---|
|`id`|stable identifier|
|`type`|canonical ontological kind|
|`kind`|optional subtype or rhetorical subclass|
|`status`|epistemic state|
|`content`|normalized substantive body|
|`scope`|domain, assumptions, context of applicability|
|`provenance`|source or authorship trace|
|`relations_declared`|outgoing canonical relations|
|`revision_metadata`|versioning, timestamps, editor, confidence|

Then each subtype adds its own invariant fields.

Examples:

- `Definition`: `defines_concept`, `statement`, optional `notation`  
- `Claim`: `statement`, `modal_scope`, `status`  
- `Proof`: `target_claim`, `strategy`, `body`  
- `Example`: `target`, `instance_description`

## Proposal C

Abstract Base: `EpistemicObject`

All canonical object types  share a common abstract contract (interface):

| Field                | Role                                          | Type                                                                   |
| -------------------- | --------------------------------------------- | ---------------------------------------------------------------------- |
| `id`                 | stable identifier                             | URI                                                                    |
| `label`              | alias                                         |                                                                        |
| `type`               | canonical ontological kind                    |                                                                        |
| `kind`               | optional subtype or rhetorical subclass       |                                                                        |
| `epistemic_status`   | epistemic state                               | Enum[established, provisional, conjectural, stipulative, foundational] |
| `content`            | normalized substantive body                   | `str`                                                                  |
| `scope`              | domain, assumptions, context of applicability |                                                                        |
| `provenance`         | source or authorship trace                    |                                                                        |
| `relations_declared` | outgoing canonical relations                  |                                                                        |
| `revision_metadata`  | versioning, timestamps, editor, confidence    |                                                                        |
| `tags`               |                                               | `Set[str]`                                                             |

