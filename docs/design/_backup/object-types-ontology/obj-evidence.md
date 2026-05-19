# Object candidate — Evidence

## Role

Evidence is an epistemic input that bears on other epistemic objects.

Its role is to preserve the material or recorded basis for support without reducing that basis to a proposition.

*Example*: a measured reaction time dataset is evidence for a claim about cognitive load.

*Evidence forms*:

- observation
- dataset
- measurement
- experiment trace
- computational output
- source extract
- textual passage

## Properties

**Truth-apt**: No. Evidence is cited or used; claims about what it shows are truth-apt.

**Functional stratum**: Evidential

**Internal structure**:

- **Item.** Observation, dataset, measurement, source extract, or trace.
- **Source.** Origin of the item.
- **How obtained** (context-dependent). Method or process that produced the item.
- **Target.** Claim, model, argument, or interpretation supported or challenged.
- **Bearing.** How the item supports, constrains, or defeats the target.
- **Trust** (context-dependent). Trust condition or known weakness.

## Encoding options

### Evidential object

**Category:** Primitive object

**Specification:** Keep cited material as `EVIDENCE` that `ARGUMENT`, `CLAIM`, or `EVALUATION`s can reference directly (e.g., dataset, quotation, measurement).

**Pros.**
- Preserves the difference between data used as support and claims about data.
- Keeps cited material distinct from a proposition that reports it.
- Works when other objects must refer to the material rather than to a proposition about it.

**Cons.**
- Needs provenance and source relations to avoid becoming a generic storage type.

### Empirical claim

**Category:** Subtype object

**Specification:** Use an empirical `CLAIM` that supports or refutes another `CLAIM` (e.g., the sample mean is higher).

**Pros.**
- Keeps simple observations in the claim layer.
- Works when the evidence is fully captured by a statement.

**Cons.**
- Forces premature propositional form on datasets, records, and excerpts.
- Loses raw or structured evidential form when the material must be cited, inspected, or traced.

### Source family

**Category:** Variant decomposition

**Specification:** Replace generic evidence with `EVIDENCE`, `SOURCE-FRAGMENT`, and `REFERENCE` variants (e.g., measurement, quoted passage, citation).

**Pros.**
- Separates observed material, anchored excerpts, and bibliographic sources.
- Works when source objects must be cited separately from observed or recorded evidence.

**Cons.**
- Adds types that may be unnecessary when provenance is secondary.
- Loses one generic evidence carrier for simple support relations.

## Subtypes

Subtypes are meaningful along one dimension: evidential provenance.

| Label                | Description                                                 | Encoding                                                 | Assessment                                   |
| -------------------- | ----------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------- |
| Observation          | Recorded occurrence or noticed pattern.                     | `EVIDENCE` subtype linked to observer or source context. | Stable when provenance matters.              |
| Measurement          | Quantified observation produced by an instrument or method. | `EVIDENCE` subtype linked to `METHOD`.                   | Stable when calibration and error matter.    |
| Dataset              | Structured collection of observations or measurements.      | `EVIDENCE` subtype with internal records or reference.   | Stable when reuse and aggregation matter.    |
| Source fragment      | Textual or documentary excerpt used as support.             | `SOURCE-FRAGMENT` variant linked to `REFERENCE`.         | Stable for interpretive and historical work. |
| Computational output | Result produced by code, simulation, or model run.          | `EVIDENCE` subtype linked to `MODEL` or `METHOD`.        | Stable when reproducibility matters.         |

Experimental provenance is encoded by linking an observation, measurement, or dataset to the `METHOD` that produced it.
