# Project overview

This file states what `gnomon` is for, the failure modes of conventional note-taking it addresses, and the architectural stance that responds to them. It is the entry point that precedes the design folder: it names the problem before the design folder works out the response.

For the design itself, see [design index](vendor/gnomon/docs/design/_index).

---

## Goal

`gnomon` is a substrate for organizing **complex theoretical frameworks**: bodies of research that combine definitions, derivations, arguments, proofs, and the relations among them. The system supports the dual function of representing what is known and guiding what to do next: which questions are open, which objects answer them, which sub-arguments compose into the main argument, and where the inquiry must go to advance.

The substrate is **object-centric**: stable typed entities with explicit identifiers, queryable relations, and derived views, rather than free-form prose accumulated in documents.

---

## Failure modes of conventional note-taking

Conventional note-taking — accumulating prose in documents — suffices for short pieces of work. As a theoretical framework grows, five failure modes appear and compound each other:

- **Loss of dependency visibility.** As objects accumulate, tracking which results depend on which definitions and which sub-arguments depend on which lemmas becomes impractical from prose alone. When a new question arises, the writer cannot identify which existing objects bear on the answer.
- **Dilution of the main argumentative structure.** Ideas accumulate redundantly across notes, summaries, and drafts. Each restatement is locally reasonable; collectively, they bury the backbone of the main argument under paraphrase.
- **Uncontrolled expansion toward side questions.** Without an explicit notion of which questions are necessary to answer the current target, inquiries drift into topically related but epistemically unnecessary side-questions. The work expands; the target does not advance.
- **Mixing of distinct epistemic roles.** Ordinary notes blend introducing a concept, stating a result, motivating a question, recording an assumption, sketching a proof, comparing alternatives, and giving examples. These roles play structurally different parts in reasoning, and conflating them prevents the reader (and the writer) from reasoning about the work as a graph rather than a stream.
- **Over-reliance on expository presentation.** As the corpus grows, the explanatory layer — paragraphs written for a reader — gradually becomes the only layer. The stable argumentative content (the canonical objects and their dependencies) ceases to exist apart from its expository presentation, and revising one means revising the other.

These failures are not stylistic. They are structural: they follow from a document-centric organization in which prose is both the storage medium and the access medium, and in which dependencies, roles, and revisions are implicit in the writing rather than first-class structures.

---

## Approach

`gnomon` replaces document-centric organization with **object-centric knowledge architecture**: typed canonical objects with explicit identifiers, a typed relation vocabulary, queryable registries, and derived expository views.

The architecture instantiates three software-engineering principles in the knowledge domain:

- [separation of concerns](vendor/gnomon/docs/design/2-architecture/constraints#^t2-separation-of-concerns) between content and presentation,
- [single source of truth](vendor/gnomon/docs/design/2-architecture/constraints#^t2-single-source-of-truth) for each piece of canonical content,
- [explicit dependency management](vendor/gnomon/docs/design/2-architecture/constraints#^t2-dependency-management) through a typed relation graph.

Each failure mode above maps to one or more architectural responses recorded in the design folder. The design folder organizes these responses into three tiers: framework-level desiderata, architectural commitments, and per-aspect decisions; see [design index](vendor/gnomon/docs/design/_index).
