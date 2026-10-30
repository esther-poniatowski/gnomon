---
tags:
  - reference
index: "[References](docs/references/_index.md)"
aliases:
  - Open Knowledge Format
---
# Open Knowledge Format

The Open Knowledge Format (OKF) is an open specification for packaging knowledge as linked Markdown files with YAML frontmatter, readable by language-model agents without a vendor platform [mcveety2026]. This note states the specification and compares its commitments with those of `gnomon`. The role of the format in `gnomon` is fixed by the [decision on the knowledge interchange format](../adr/knowledge-interchange-format.md).

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
| Relation between entries | Untyped link, with its type stated in prose. | [Typed relation vocabulary](../adr/closed-typed-relations.md#^typed-ends), closed, with declared source and target kinds. |
| Unresolved reference | Must be tolerated. | Reported as a defect. |
| Identity | File path, optionally a `resource` URI. | Stable [dotted identifier](../adr/dotted-identifiers.md) such as `quest.TOPIC.NAME`, declared in the authored record. |
| Unit per file | One concept per Markdown file. | In the current records, one YAML record per concern, declaring many symbols. |
| Formal content | None beyond the code of an `Attested Computation`. | Declared symbols, and [formulas](../specification/expressions.md) over them. |
| Status | Lifecycle of a document: `draft`, `stable`, `deprecated`. | Epistemic state of an inquiry, for instance a question `posed`, `refined`, `answered` or `abandoned`. |
| Authorship and verification | `generated`, `verified`, and the actor convention. | No field. |

## Sources

- [google2026_spec] ◐ [Google Cloud, *Open Knowledge Format specification*, version 0.2, GoogleCloudPlatform/knowledge-catalog, 2026](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
- [google2026_trust] ◐ [Google Cloud, *OKF v0.2 adds trust signals*, Google Cloud Blog, 2026](https://cloud.google.com/blog/products/data-analytics/okf-v0-2-adds-trust-signals)
- [mcveety2026] ◐ [McVeety and Hormati, *How the Open Knowledge Format can improve data sharing*, Google Cloud Blog, 2026](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing)
