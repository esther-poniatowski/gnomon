---
tags:
  - reference
index: "[Methods for reasoning](docs/methods-reasoning/_index.md)"
aliases:
  - Open Knowledge Format
---
# Open Knowledge Format

The Open Knowledge Format (OKF) is an open specification for packaging knowledge as linked Markdown files with YAML frontmatter, readable by language-model agents without a vendor platform [mcveety2026]. This note assesses whether `gnomon` can use the format in one of three roles:

- as the source format of its records;
- as a derived export;
- as a source of field designs.

> [!QUESTION] Should `gnomon` store its records in the Open Knowledge Format, emit bundles in it, or borrow some of its fields?

## Specification

### Origin and purpose

Version 0.1 was announced on 12 June 2026 by two Google Cloud technical leads [mcveety2026]. Version 0.2 is the current version of the specification in the reference repository [google2026_spec]. The format formalizes a pattern named the "LLM wiki": language-model agents maintain a linked Markdown knowledge base [mcveety2026]. The target content is knowledge about data and systems, such as tables, datasets, metrics, runbooks and APIs [mcveety2026].

### Bundle and concept documents

A **bundle** is a directory tree of UTF-8 Markdown files, distributed as a git repository, an archive, or a subdirectory of a larger repository. Two file names are reserved: `index.md` lists the concepts of its directory, and `log.md` records dated changes, newest first. Every other Markdown file is a **concept document**. Its frontmatter requires one key, `type`, a free string naming the concept type. Four further keys are recommended:

- `title`, the display name;
- `description`, a one-sentence summary;
- `resource`, a URI identifying the underlying asset;
- `tags`, a list of categories.

### Links

Concept documents link to one another by ordinary Markdown links, either relative or rooted at the bundle root by a leading `/`. A link carries no relation type. The relation type, for instance parent, reference, join or dependency, is conveyed by the surrounding prose [google2026_spec].

### Trust, provenance and lifecycle

Version 0.2 answers a concern raised after the first release: once agents write to a bundle, a consumer must judge whether each concept can be trusted [google2026_trust]. Version 0.2 adds five optional fields for that purpose:

- `generated: {by, at}` records the actor that produced the content, and the time of its last meaningful change.
- `verified: [{by, at}, ...]` records independent confirmations. Three trust tiers are derived from it: unverified when the key is absent, machine-confirmed when no verifier is a person, human-reviewed when at least one verifier is a person.
- `sources` lists the materials from which a concept derives. Each entry requires `resource`, and an optional `id` attributes a single claim through a Markdown footnote.
- `status` takes `draft`, `stable` or `deprecated`, and defaults to `stable`.
- `stale_after` fixes an absolute instant from which the concept counts as stale and requires verification again.

Actors follow one naming convention: `<producer>/<version>` for an agent or a tool, `human:<id>` for a person, and `process:<id>` for an automated process. The trust tier is computed from the `human:` prefix of the verifiers, so producers must use that prefix for content written or confirmed by a person. Version 0.2 also defines one concept type, `Attested Computation`. This type carries a sanctioned way to compute a value (`runtime`, `parameters`, `computation`), the instructions for running it (`executor`), and deterministic code that checks the receipt of each run (`attester`).

### Conformance

A bundle conforms when every concept document carries parseable frontmatter with a non-empty `type`, and when each reserved file, where present, follows its structure. Beyond conformance, the specification requires consumers to tolerate deviations [google2026_spec]:

- a consumer must accept a bundle with missing optional fields, unknown types, unknown keys, broken links or missing index files;
- a consumer should preserve unknown keys when it rewrites a document.

The specification also excludes three matters from its scope [google2026_spec]:

- a taxonomy of concept types;
- storage, serving and query infrastructure;
- a replacement for domain schemas such as OpenAPI or Protobuf.

## Comparison with gnomon

Both formats store plain text files suited to version control with git, and both open a directory with an index file. The two formats diverge on each commitment that makes a `gnomon` record machine-checkable:

| Commitment | OKF v0.2 | `gnomon` |
| --- | --- | --- |
| Entry type | Free `type` string. An unknown type must be tolerated. | Closed vocabularies declared in [registries](../adr/registries-as-source.md). A value outside its vocabulary is reported. |
| Relation between entries | Untyped link, with its type stated in prose. | [Typed relation vocabulary](../design/2-architecture/relations-graph.md#^t2-typed-relation-vocabulary), closed, with declared source and target kinds. |
| Unresolved reference | Must be tolerated. | Reported as a defect. |
| Identity | File path, optionally a `resource` URI. | Stable identifier such as `quest.TOPIC.NAME`, held in the [canonical layer](../design/2-architecture/layering.md#^t2-canonical-source-of-truth). |
| Unit per file | One concept per Markdown file. | In the current records, one YAML record per concern, declaring many symbols. |
| Formal content | None beyond the code of an `Attested Computation`. | Declared symbols, and [formulas](../epistemology/symbols-and-expressions.md) over them. |
| Status | Lifecycle of a document: `draft`, `stable`, `deprecated`. | Epistemic state of an inquiry, for instance a question `posed`, `refined`, `answered` or `abandoned`. |
| Authorship and verification | `generated`, `verified`, and the actor convention. | No field. |

## Assessment

Each of the three roles is decided by one constraint of the `gnomon` design.

### Source format

The OKF cannot serve as the storage format of `gnomon` records. The decisive constraint is [formal expression of all content](../design/1-framework/framework-foundations.md#^t1-formal-expression): every field read by a validator or a query must conform to a known grammar. An OKF link leaves its relation type to prose. Consequently, a relation stored in OKF form conforms to no grammar. Without that grammar, the build step cannot derive the dependency graph from OKF links. The conformance rules raise a second conflict: an OKF consumer must accept unknown types and broken links, whereas `gnomon` reports both as defects.

Moreover, OKF conformance adds no check to those of `gnomon`. A `gnomon` Markdown file meets the conformance rules once its frontmatter carries a `type` key, since the OKF admits every other key. An OKF consumer then reads `type`, `title` and the links, and leaves uninterpreted every field checked by `gnomon`. The current records are YAML files, so none of them counts as a concept document.

### Export view

An OKF bundle is admissible as an export, because [derived artifacts](../design/2-architecture/layering.md#^t2-derived-artifacts) are compiled from the canonical objects and never edited. The mapping from canonical objects to concept documents preserves kinds and titles: each object becomes one concept document, its kind fills `type`, and its title fills `title`. The same mapping loses the relation types. Each typed edge becomes a link whose type is stated in prose. A typed copy of the edge can be kept under an extra key. OKF consumers should preserve that key, without interpreting its value.

The export gains value only for a consumer reading OKF bundles and unable to read the `gnomon` sources. One product was announced as ingesting OKF bundles: Google Cloud Knowledge Catalog [mcveety2026]. By contrast, a language-model agent can read the `gnomon` Markdown and YAML sources directly. Therefore, the export should be deferred until a named consumer requires it, such as a catalog or an agent framework loading OKF bundles.

### Trust fields

The v0.2 trust fields address a gap present in `gnomon`. When language-model agents draft records and a researcher reviews them, no `gnomon` field records the actor that produced a record or the actor that confirmed the record. Together with the `human:` prefix, the pair `generated.by` and `verified[].by` separates agent-produced content from human-reviewed content by syntax alone. Consequently, a checker can compute the trust tier of each record. The fields bear on [revision accountability](../design/1-framework/research-activities-workflows.md#^t1-revision-accountability): each revision must be traceable to its origin. The actor producing a revision is one component of that origin. Therefore, the trust fields can be adopted into the record templates, once a design decision ratifies them.

Two other elements of version 0.2 do not transfer to `gnomon`:

- `stale_after` expires content at a fixed instant. A `gnomon` object becomes stale when any object upstream of it is revised, and [dependent flagging](../design/2-architecture/validity-revision.md#^t2-dependent-flagging) surfaces that state.
- `Attested Computation` presupposes a runtime executing a sanctioned computation, and `gnomon` executes none.

## Sources

- [google2026_spec] ◐ [Google Cloud, *Open Knowledge Format specification*, version 0.2, GoogleCloudPlatform/knowledge-catalog, 2026](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
- [google2026_trust] ◐ [Google Cloud, *OKF v0.2 adds trust signals*, Google Cloud Blog, 2026](https://cloud.google.com/blog/products/data-analytics/okf-v0-2-adds-trust-signals)
- [mcveety2026] ◐ [McVeety and Hormati, *How the Open Knowledge Format can improve data sharing*, Google Cloud Blog, 2026](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing)
