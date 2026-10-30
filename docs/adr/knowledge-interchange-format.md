---
tags:
  - decision
status: accepted
created: 2026-10-29
revised: 2026-10-29
index: "[Architecture decisions](docs/adr/_index.md)"
aliases:
  - Knowledge interchange format
---
# Knowledge interchange format

> [!QUESTION] Goal: which role does the Open Knowledge Format take in `gnomon`: the source format of its records, a derived export, or a source of field designs?

The [Open Knowledge Format](../references/open-knowledge-format.md) (OKF) packages knowledge as linked Markdown files with YAML frontmatter, which language-model agents read without a vendor platform [mcveety2026]. Its version 0.2 adds optional fields that record the actor that produced a document and the actors that confirmed it [google2026_trust]. The note on the format states its specification and compares each of its commitments with those of `gnomon`. Language-model agents draft records of `gnomon` that a researcher reviews, so the format raises three questions: whether it can hold the records, whether `gnomon` should emit bundles in it, and whether its trust fields fill a gap of the records.

## Decision

The records of `gnomon` are not stored in the OKF. ^no-okf-source

An OKF bundle is admitted as an export generated from the records and never edited. The export is deferred until a named consumer requires it, such as a catalog or an agent framework that loads OKF bundles. ^okf-export-deferred

The trust fields of the OKF are not adopted yet. These fields are `generated` and `verified`, together with the prefix `human:` that marks a person among the actors. These fields record the actor that produced a record and the actors that confirmed it, which no field of `gnomon` records, and their adoption into the record templates awaits a decision of its own. ^trust-fields-open

Two other elements of version 0.2 are not adopted: the field `stale_after`, and the concept type `Attested Computation`. ^not-transferred

## Constraints that decide the role of the format

- **A tool reads a field only through a grammar.** The [decision on grammatical fields](grammatical-fields-and-readings.md#^grammar-for-read-fields) lets a tool interpret a value only when a grammar declares that value. An OKF link leaves its relation type to prose, so a relation stored in OKF form conforms to no grammar, and no tool can build the [graph of relations](closed-typed-relations.md#^relation-graph) from it.
- **`gnomon` reports the deviations that an OKF consumer must tolerate.** An OKF consumer must accept unknown types and broken links [google2026_spec], whereas the checks of `gnomon` report a value outside its vocabulary and an unresolved reference as defects.
- **Conformance to the OKF adds no check.** A Markdown file of `gnomon` conforms once its frontmatter carries a key `type`, since the OKF admits every other key. An OKF consumer then reads `type`, `title` and the links, and leaves uninterpreted every field that `gnomon` checks. The current records are YAML files, so none of them counts as a concept document.
- **A copy of the records is admitted only when a tool generates it.** The [rule of one source](one-source-per-unit.md#^generated-copies-only) therefore admits an export, and excludes a bundle edited beside the records.
- **An export serves only a consumer that cannot read the sources.** A language-model agent reads the Markdown and YAML sources of `gnomon` directly. One product was announced as ingesting OKF bundles: Google Cloud Knowledge Catalog [mcveety2026].
- **The actor of a revision belongs to its origin.** The [decision on revision accountability](revision-accountability.md#^traceable-revision) requires each revision to be traceable to its origin, and leaves open the [mechanism that records that origin](revision-accountability.md#^mechanism-open).
- **Staleness follows from a revision upstream.** A record of `gnomon` becomes stale when a record upstream of it is revised, and the [propagation of a revision](revision-accountability.md#^propagated-revision) reports that state.
- **`gnomon` executes no computation.** `Attested Computation` presupposes a runtime that executes a sanctioned computation and checks the receipt of each run.

## Options weighed

| Option | Benefit | Reason it is not taken |
| ------ | ------- | ---------------------- |
| Store the records as OKF concept documents | Any OKF consumer reads the records | A relation typed in prose conforms to no grammar, an OKF consumer must accept the unknown types and broken links that `gnomon` reports, and conformance adds no check |
| Emit an OKF bundle at every build | A catalog that loads OKF bundles reads the records | No named consumer reads OKF bundles while being unable to read the sources, and the export loses the relation types |
| Adopt `generated` and `verified` in the record templates now | A checker computes the trust tier of each record from the prefix `human:` of its verifiers | The fields enter every template before the mechanism that records the origin of a revision is decided, so the actor could be recorded twice |
| Expire a record at a fixed instant, by `stale_after` | Staleness requires no relation | A record becomes stale when a record upstream of it is revised, not at a date |
| Keep the records in their own form, defer the export to a named consumer, and leave the trust fields to a later decision | Every check keeps its grammar, and each deferred option keeps the constraint that would reopen it | — |

## Consequences

- An export, once a consumer requires it, maps each record to one concept document: the kind of the record fills `type`, and its title fills `title`. Each typed relation becomes a link whose type is stated in prose, and a typed copy of the relation may be kept under an extra key, which OKF consumers should preserve without interpreting its value.
- The trust fields wait for the decision on the [mechanism that records a revision](revision-accountability.md#^mechanism-open). The [decision on the inputs of checks](checks-read-records.md) already separates a field that names the actor of a record from a field that certifies conformance.
- A version of the OKF whose links carry a type, and whose consumers may reject a broken link, reopens the decision on the source format.
- The specification of the format and its comparison with `gnomon` stay in the [note on the format](../references/open-knowledge-format.md), as external reference.

---
## Sources

Marks follow the [legend of reading marks](../../CONTRIBUTING.md#^reading-marks). A mark ◐ records a check of the published page.

- [google2026_spec] ◐ [Google Cloud, *Open Knowledge Format specification*, version 0.2, GoogleCloudPlatform/knowledge-catalog, 2026](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
- [google2026_trust] ◐ [Google Cloud, *OKF v0.2 adds trust signals*, Google Cloud Blog, 2026](https://cloud.google.com/blog/products/data-analytics/okf-v0-2-adds-trust-signals)
- [mcveety2026] ◐ [McVeety and Hormati, *How the Open Knowledge Format can improve data sharing*, Google Cloud Blog, 2026](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing)
