# Inquiry specification templates

Templates that a research project copies and fills to specify an inquiry, following the method of `docs/epistemology/inquiry-specification.md`. One target system serves several phenomena, and one phenomenon serves several questions, so each is a separate object that the next one references by its identifier.

Filling order:

1. `target-system.yml` — the system studied: its reference class, constituents, state variables, parameters, laws with their closure, interface and external systems, once per system.
2. `phenomenon.yml` — the behavior of that system that questions concern, once per phenomenon.
3. `question.yml` — one research question: its subject, contrast, domain, epistemic task, required accuracy and selected virtues, filled before any candidate answer is evaluated.
4. `answer.yml` — one candidate answer: its constituents, terms, laws, organization, idealizations and explanans, once per candidate.
5. `assessment.yml` — the verdict and the evidence of each test of `docs/epistemology/satisfaction-conditions.md`, and the assessment of the answer on each selected virtue, once per candidate assessed. It is kept apart from the answer, so that a candidate can be restated without touching its assessment.

Format:

- each file is pure YAML, so that a slot owning dependent fields carries them as nested keys instead of splitting one slot between a structured field and a prose block;
- closed option lists sit in a comment beside their field, so that a schema can check them, and every closed field accepts `open`;
- free text sits in the value of its own field, written in UPPERCASE as a placeholder, with formulas allowed;
- the slots follow the order of the method note that defines them, and each row of that note names its key, so that the two can be compared mechanically.

This format departs from `docs/design/2-architecture/data-formats.md`, which rejects YAML-only sources for framework notes carrying prose, proofs and rendered math. These files carry records rather than notes, so that objection does not reach them; the architecture note has yet to record the distinction.
