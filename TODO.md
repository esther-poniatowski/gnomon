---
tags:
  - tasks
aliases:
  - Project goals
---
# Project goals

This list holds the goals of `gnomon` that span several parts of the project. The open decisions of the design stay in the [design task list](docs/TODO.md), and a goal that extends one of them links to that decision.

## Conventions

- [ ] Align the conventions of `gnomon` with those of `geonexus`, recorded in `/Users/eresther/Documents/research/geonexus/CONVENTIONS.md`. 🆔 geonexus-conventions
	- [ ] Compare the two workspaces on frontmatter keys, conventional file types (task lists, dashboards, handoffs), and task syntax.
	- [ ] Adopt the conventions retained, in this list and in the [design task list](docs/TODO.md) first.
- [ ] Give each entry of `docs/_index.md`, and of the indexes under `docs/design/` and `docs/methods-*`, one sentence stating why a reader opens the file. The indexes of `docs/epistemology/`, `docs/adr/`, and `test/` already follow this rule. 🆔 index-goals

## Frameworks

- [x] Update the README to register the new orientation of the framework and the pending features.
- [ ] Improve the answer and assessment templates from the test cases.
- [ ] Build a framework that formalizes definitions, grounded in the authoritative literature of epistemology and checked against concrete problems of `geonexus`. 🆔 definitions-framework
- [ ] Build a framework that formalizes the decomposition of a question into subquestions. It extends the partly settled [decisions on questions](docs/TODO.md). 🆔 question-decomposition
- [ ] Define a vocabulary of atomic research actions. It bears on the open decision on [primitive operations](docs/design/2-architecture/operations-and-modes.md#^t2-operation-primitiveness). 🆔 research-actions
- [ ] Build a framework that formalizes derivation (the analysis), its results, and synthesis (the answer). It extends the open decision on [arguments and derivations](docs/design/3-aspect-specific/arguments-reasoning.md) and the [answer form](docs/epistemology/answer-form.md). 🆔 derivation-framework
- [ ] Refactor the documentation for the epistemic framework. Create one file that enumerates all the fields by alphabetic order (including nested paths) and links to a markdown anchor that documents this field.


