---
tags:
  - specification
index: "[Specification](docs/specification/_index.md)"
aliases:
  - Concept record
---
# Concept record

> [!QUESTION] Goal: what does a researcher write in each field of a concept record, and when is each field required?

A concept record holds the meaning of one concept of the research: its gloss, its kind, its broader concept, its source, and its confusions with neighboring concepts. The [theory of a concept](../epistemology/objects/concept/concept.md) states why the meaning is held apart from the names and the symbols of the concept. A concept of another project is referenced by its identifier, never copied. ^concept-record

The gloss fixes a meaning without asserting anything about the instances of the concept. Content that asserts, denies or evaluates belongs to a claim, which an answer or a background record holds. A full definition belongs to a definition object, to which the field `definition` points. ^concept-boundary

| Specification | When it is required | Content | Examples |
| ------------- | ------------------- | ------- | -------- |
| Gloss | always | one sentence that fixes the meaning of the concept, without a claim about its instances | an invariant set of a dynamical system that attracts every trajectory starting near it (attractor) |
| Kind | always | the kind of entity that the concept represents, `system` · `subtype-or-class` · `property` · `process`, a kind and a subclass counting as a class, in the senses of [system](../epistemology/vocabulary/systems/system-constituent-environment.md), [class](../epistemology/vocabulary/systems/kind-class-population.md), [property](../epistemology/vocabulary/systems/property-attribute-predicate.md) and [process](../epistemology/vocabulary/change/process-event-history.md) | a recurrent network (system); an attractor (subtype or class); the stability of a fixed point (property); the descent of the loss during training (process) |
| Antagonist | optional, for a property only | the concept of the opposed property | instability, opposed to stability |
| Broader concept | optional, at most one | the concept that this one specializes; the broader concept does not list its narrower concepts | invariant set, broader than attractor |
| Source | always | the note or the publication that states the concept | the chapter of a textbook on dynamical systems that defines attractors |
| Confusions | when a neighboring concept risks being conflated with this one | one entry per such concept, with the parts of the next five rows | attractor and fixed point |
| Confusions: other concept | in each entry | the identifier of the other concept, or the term in use when no record states it | fixed point |
| Confusions: axis of difference | in each entry | the axis along which the two concepts differ | the stability of the set |
| Confusions: blocking feature | in each entry | the feature of one concept that the other lacks, which blocks their interchange | an attractor attracts the trajectories that start near it, whereas a saddle point is a fixed point that repels some of them |
| Confusions: risk | in each entry | the shared feature that makes the two concepts easy to conflate | both are found as zeros of the vector field by the same root search |
| Confusions: consequence | in each entry | the error that the inquiry commits when it conflates the two concepts | a saddle point is read as a state that the network stores |
| Definition | optional | a pointer to the full definition object of the concept | the note that defines attractors by their basin of attraction |
