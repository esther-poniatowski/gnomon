# Project overview

This file states the objectives of the `gnomon` project: the failure modes of conventional note-taking, and the architectural stance that responds to them.

---

## Goal

`gnomon` is a system for organizing **complex research frameworks**, typically theoretical, mathematical or modeling frameworks. 

Such research projects combine a large body of interrelated definitions, derivations, arguments, proofs, and the relations among them. The system aims to:

- represent the **state of knowledge** — the epistemic contents with their maturity;
- record the **logic of inquiry** — the dependencies that determine how arguments articulate various epistemic contents to answer a question, and how they compose into larger arguments;
- **guide the inquiry** — the next questions to ask, the next objects to define, and the next arguments to construct, given the current state of knowledge and the target question.

---

## Failure modes of conventional note-taking

Conventional note-taking — accumulating prose in documents — suffices for short pieces of work. As a theoretical framework grows, five failure modes appear and compound each other:

- **Loss of dependency visibility.** As objects accumulate, tracking which results depend on which definitions and which sub-arguments depend on which lemmas becomes impractical from prose alone. When a new question arises, the writer cannot identify which existing objects bear on the answer.
- **Dilution of the main argumentative structure.** Ideas accumulate redundantly across notes, summaries, and drafts. Each restatement is locally reasonable; collectively, they bury the backbone of the main argument under paraphrase.
- **Uncontrolled expansion toward side questions.** Without an explicit notion of which questions are necessary to answer the current target, inquiries drift into topically related but epistemically unnecessary side-questions. The work expands; the target does not advance.
- **Mixing of distinct epistemic roles.** Ordinary notes blend introducing a concept, stating a result, motivating a question, recording an assumption, sketching a proof, comparing alternatives, and giving examples. These roles play structurally different parts in reasoning, and conflating them prevents the reader (and the writer) from reasoning about the work as a graph rather than a stream.
- **Over-reliance on expository presentation.** As the corpus grows, the explanatory layer — paragraphs written for a reader — gradually becomes the only layer. The stable argumentative content (the canonical objects and their dependencies) ceases to exist apart from its expository presentation, and revising one means revising the other.

These failures are structural: they follow from a document-centric organization in which:

- prose is both the storage medium and the access medium, 
- dependencies, roles, and revisions are implicit in the writing rather than first-class structures.

---

## Approach

`gnomon` replaces document-centric organization with **object-centric knowledge architecture**, which provides:

- typed canonical objects with explicit identifiers, that represent the stable content of the framework,
- a typed relation vocabulary, that represents the epistemic dependencies among objects, 
- queryable registries, that support navigation, retrieval, and revision of content based on its epistemic role and its dependencies,
- derived expository views, that support presentation and communication of the content without being the primary storage or access medium.

The architecture instantiates three software-engineering principles in the knowledge domain:

- [separation of concerns](vendor/gnomon/docs/design/1-framework/research-activities-workflows#^t1-activity-access-rights) between content and presentation,
- [single source of truth](vendor/gnomon/docs/design/1-framework/research-activities-workflows#^t1-single-source-of-truth) for each piece of canonical content,
- [explicit dependency management](vendor/gnomon/docs/design/2-architecture/relations-graph#^t2-relational-graph-representation) through a typed relation graph.

Each failure mode above maps to one or more architectural responses recorded in the [design](vendor/gnomon/docs/design/_index).
