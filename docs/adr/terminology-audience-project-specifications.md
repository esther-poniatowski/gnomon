---
role: decision
status: accepted
index: "[Architecture decisions](docs/adr/_index.md)"
aliases:
  - Terminology, audience and project specifications
tags: []
source:
---
# Terminology, audience and project specifications

> [!QUESTION] Goal: which tool provides the mechanisms of glossaries, notations, audience specifications and project specifications, and which repository holds their instances?

A research project names its quantities in a notation, its concepts in a glossary, and itself in a project specification. Each exposition of the project calibrates its claims, its terminology and its level of technicity against the audiences cited by its design brief. `geonexus`, a consumer of `gnomon`, declares these four kinds of record with schemas of its own and checks them with a checker of its own. Their mechanisms overlap with `gnomon`:

- each symbol declared by an inquiry record carries its LaTeX form, and `gnomon vocabulary` generates the symbols and operators of a problem;
- `gnomon` ratifies a canonical terminology, and the [decision on concepts, glossaries and notations](concepts-glossaries-notations.md) settles its scope: a concept keeps one meaning across projects, whereas its names vary with the audience and the context;
- the view specifications of `gnomon` declare audience profiles, as the [decision on expositions](expositions-as-projections.md) states;
- the questions of a project specification restate the question records of `gnomon`.

## Decision

`gnomon` provides the mechanisms of four record types: notation, glossary, audience and project. Each mechanism holds a schema, written as the [decision on record schemas](record-schemas.md) states, a template generated from that schema, and the checks of its records. A consumer instantiates the records of its projects and of its audiences.

The four types form one chain:

- a **project** specification names the project, binds its glossary, its notation and its audiences, and lists its decisions. Its scope references the problem and question records of `gnomon` instead of restating their questions;
- a **notation** holds the conventions of a project, such as the typography of vectors and matrices and its reserved labels, together with the symbols reused across records. Each other symbol stays declared in its inquiry record, and the LaTeX macros of an exposition are generated from the symbols;
- a **glossary** names the concepts of a project, with their aliases, the names that suit some contexts only, and the entries imported from other glossaries under a namespace;
- an **audience** specification records the knowledge, the skills and the register of a readership. The specification references the concepts that its readers hold, and a subtype inherits the knowledge and the register of its parent.

The design brief of an exposition cites its audiences, and the exposition family checks the terms of an exposition against them.

## Constraints that decide the owner

- **The four types serve research and its expositions.** A notation names the quantities of inquiry records, a glossary names the concepts that research defines, an audience calibrates an exposition, and a project specification binds the three to one inquiry.
- **One symbol has one declaration.** If a notation restated the symbols of the records, it would hold a second copy. The [single field per fact](single-field-per-fact.md) excludes that copy.
- **One question has one record.** If a project specification listed the questions of its scope, it would restate the question records.
- **A reference does not transfer ownership.** A record of another concern may name an instance, such as a contact profile naming the audiences that include a researcher. That reference leaves the mechanism of audiences with `gnomon`, and the contact profile with its own owner.

## Options weighed

| Option | Benefit | Reason it is not taken alone |
| ------ | ------- | ---------------------------- |
| Each consumer keeps its own mechanisms | Each research vault adapts its schemas freely | Every research vault restates the same schemas and checks, and the notation of a consumer duplicates the symbols of the records |
| A separate tool for terminology and audiences | `gnomon` keeps a narrower scope | The four types depend on the inquiry records and on the exposition family, so a separate tool would depend on `gnomon` for every check |
| `gnomon` provides the four mechanisms, and consumers hold the instances | One owner for the schemas and the checks, beside the records that they describe | The scope of `gnomon` widens, and each consumer migrates its records to the identifiers `gnomon:<type>@<version>` |

## Consequences

- The schemas `gnomon:project`, `gnomon:notation`, `gnomon:glossary` and `gnomon:audience` replace the schemas of the consumers, and the checks of imports, references, conflicts, aliases and cycles move with them.
- The decisions of `geonexus` on [notations separate from glossaries](/Users/eresther/Documents/research/geonexus/docs/_decisions/notations-separate-from-glossaries.md), [namespaced imports](/Users/eresther/Documents/research/geonexus/docs/_decisions/namespaced-imports.md), [consumer-side glossary binding](/Users/eresther/Documents/research/geonexus/docs/_decisions/consumer-side-glossary-binding.md), [context-dependent usage](/Users/eresther/Documents/research/geonexus/docs/_decisions/context-dependent-usage.md), [audience-agnostic glossaries](/Users/eresther/Documents/research/geonexus/docs/_decisions/audience-agnostic-glossaries.md), [audience knowledge by reference](/Users/eresther/Documents/research/geonexus/docs/_decisions/audience-knowledge-by-reference.md), [audience subtypes](/Users/eresther/Documents/research/geonexus/docs/_decisions/audience-subtypes.md) and [project specifications](/Users/eresther/Documents/research/geonexus/docs/_decisions/project-specifications.md) supply the first statement of these mechanisms. Their resolution of module-local terminology settles the tension recorded on canonical terminology.
- Whether a glossary entry is the lexical face of a concept record, the product of an explicit definition, remains to be decided.
