# Object candidate — Interpretation

## Role

An interpretation assigns a semantic reading to an object whose domain meaning is not fixed by its form alone.

Its role is to connect structure with domain content.

*Example*: 

- a circuit interpretation maps the symbol `R` to electrical resistance,
- a probabilistic interpretation reads a model output as belief, frequency, or calibrated uncertainty.

## Properties

**Truth-apt**: Derivative. An interpretation can be apt, faithful, distorting, or admissible; claims about the mapping are truth-apt.

**Functional stratum**: Semantic

**Internal structure**:

- **Interpreted object.** Formal, abstract, ambiguous, or underspecified object being read.
- **Domain.** Target domain in which meaning is assigned.
- **Mapping.** Assignment from structure to domain objects, quantities, or roles.
- **Constraints.** Conditions that make the reading admissible.
- **Licensed use** (context-dependent). Claim or use licensed by the interpretation.

## Encoding options

### Semantic map

**Category:** Composite object

**Specification:** Reify the semantic map that links interpreted `CONCEPT`, `MODEL`, or symbol objects to the target domain objects that give them meaning (e.g., `R` denotes resistance).

**Pros.**
- Preserves reusable semantic maps that support restriction, extension, composition, and transport.
- Separates semantic grounding from claims that evaluate or assert the assignment.

**Cons.**
- Requires a narrow map-based definition of interpretation.

### Interpretive claim

**Category:** Subtype object

**Specification:** Use `CLAIM` for the assertion that one object denotes, realizes, or represents another (e.g., `R` denotes resistance).

**Pros.**
- Fits truth-apt assertions about what a symbol, model, or concept denotes.
- Works when interpretation is only an assertion.

**Cons.**
- Obscures mediating behavior between model, concept, and evidence.
- Treats assignment as assertion even when the map functions as a reusable semantic object.

### Denotes edge

**Category:** Relation (graph edge)

**Specification:** Use asymmetric semantic edges from symbol, `CONCEPT`, or `MODEL`s to target domain objects (e.g., `R` to resistance).

**Pros.**
- Keeps simple denotation links explicit.
- Works when the assignment needs no separate object.

**Cons.**
- Cannot store admissibility, scope, or competing assignments.

## Subtypes

Subtypes are meaningful along one dimension: the kind of object whose meaning or significance is assigned.

| Label                      | Description                                                                               | Encoding                                                                                                                | Assessment                                                                                                |
| -------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| Symbol interpretation      | Assigns a referent or value to a symbol.                                                  | `INTERPRETATION` composite or denotes edge.                                                                             | Core case for formal notation.                                                                            |
| Model interpretation       | Assigns domain meaning to a model structure.                                              | `INTERPRETATION` linked to `MODEL` and target domain objects.                                                           | Stable when model use depends on the map.                                                                 |
| Concept interpretation     | Fixes how a concept is read in a context.                                                 | `INTERPRETATION` linked to `CONCEPT` and `FRAMEWORK`.                                                                   | Useful when concepts shift across frameworks.                                                             |
| Result interpretation      | States what a result claim, theorem, or formula means (implies) for a domain or question. | `INTERPRETATION` linked to result `CLAIM`, `DERIVATION / PROOF`, or formula object, with optional implication `CLAIM`s. | Stable when significance differs from the formal result; use `CLAIM` for the asserted consequence itself. |
| Measurement interpretation | Reads a measurement or output as a domain quantity.                                       | `INTERPRETATION` linked to `EVIDENCE`, `METHOD`, or `MODEL`.                                                            | Stable when validity depends on calibration or construct meaning.                                         |
