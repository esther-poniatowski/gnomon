---
tags:
  - specification
index: "[Specification](docs/specification/_index.md)"
aliases:
  - Background record
  - Specifying the background
---
# Background record

> [!QUESTION] Goal: what does a researcher write in each field of a background record?

The grounds of these fields are stated in the note on the [background](../epistemology/subject/background.md).

> [!IMPORTANT] One target, several backgrounds
> Several background records may describe one target, for instance two bodies of laws drawn from rival theories, or the laws of one subsystem beside those of another. Each question names its admitted background records in its [subject](../epistemology/subject/subject-of-inquiry.md).

| Specification | When it is required | Options or frame | Examples | Source |
| ------------- | ------------------- | ---------------- | -------- | ------ |
| Describes — the target whose quantities the laws use | always | the identifier of one target-system record | the record of the trained networks; the record of the four tipping elements | — |
| Laws — known behaviors of the components or of the system | always | an expression over the symbols that the target declares, with its signature and the places that the claim ranges over (one entry each, empty when the law concerns the system as a whole). Its warrant (derived from other admitted laws, derived in a limit, posited, fitted or measured), with its grounds. Its role, one of six:<br>- evolution: how the state changes along the course<br>- input-output: how one quantity is determined by others at the same point<br>- measurement: how an instrument registers the state<br>- state-constraint: which states may hold together, including at the start and at the boundary<br>- distribution: the law of a random quantity<br>- admissibility: a restriction on the parameters or on the forms that a member may take | - the leaky integration of each neuron (one place, local, evolution)<br>- the gradient-descent learning rule (collective, evolution)<br>- the energy function on the state space (no place, state-constraint)<br>- the forward map of a network from its inputs to its prediction (input-output)<br>- the spike threshold of the recording (measurement) | laws of succession and coexistence, renamed by their function [winther2020] |
| Laws: origin | with each law | a pointer to the publication, the data set or the derivation from which the law is taken | the article that defines the model; the recordings to which a transfer function was fitted | [law appraised before admission](#^law-range) |
| Laws: range | when the law is established over part of the reference class only | an expression over declared symbols that bounds the conditions under which the law is established | a rate equation established for inputs below saturation; a scaling law established above a minimal width | [law appraised before admission](#^law-range) |
| Closure (of the laws) — separates a formal target from an empirical one | always | complete, for a formal target whose laws define the system · partial, for an empirical target that may admit a rule independent of them | the Wilson–Cowan equations define the model (complete); a recorded circuit, where a plasticity rule may still be discovered (partial) | [laws admitted as given](../epistemology/subject/background.md#^laws) |
| Organization | when the parts or the laws stand in a relation on which the behavior depends | per relation, its tuples and its laws. The tuples take the form `prod(source, reach)` or `subset(prod(source, reach), adjacency)`. A directed relation puts the reach last, and a joint one has three or more components. When the ends are laws, the relation names the laws that it orders, with the reach last | a transmitted signal between two climate subsystems; a nonreciprocal cross-coupling between two species fields; two populations jointly changing the growth of a third | organization of a mechanism [craver2007] |

- **An empirical bridge law is an admitted law.** The [rule on bridge laws](../epistemology/subject/target-system.md#^bridge-law) places such a law among the laws of a background record, under the role `measurement`.

- **The closure qualifies one body of laws.** When several background records describe one target, each record states whether its own laws define the system. When a question admits two bodies of laws that are each complete, the question presupposes that the two bodies agree wherever both apply. ^closure

- **A law is appraised before it is admitted.** Each admitted law carries a warrant and an origin, and a range when it is established over part of the reference class only. The origin points to the source of the law, so a reader can check the law against that source. The range states the conditions under which the law is established. The range belongs to the law, because every question admitting the background inherits the same law. A bound written into the [domain](../epistemology/subject/domain.md) of one question would leave the other questions unbounded. ^law-range

- **The range of invariance of a law is stated in the record.** When a law is stated without a range, it claims invariance over the whole reference class.

- **A law or a relation carried by only some members names its variant.** The target declares the [variants](target-system.md#^variants) of its class. An unmarked entry of the background holds of every member, so it may name only the symbols carried by every member. The check for unborne variants counts the marks of the background records as well: a variant marked by a background law is carried, even when no declaration of the target carries it.

---
## Sources

Marks follow the [legend of reading marks](../../CONTRIBUTING.md#^reading-marks).

- [craver2007] ◐ [Craver, _Explaining the Brain_, OUP, 2007](https://philpapers.org/rec/CRAETB-2)
- [winther2020] ◐ [Winther, "The structure of scientific theories", _SEP_, revised 2020](https://plato.stanford.edu/entries/structure-scientific-theories/), §3.1.1 on the state-space approach
