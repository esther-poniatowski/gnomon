---
tags:
  - method
  - wip
index: "[Epistemology](docs/epistemology/_index.md)"
aliases:
  - Specifying the background
  - Background record
---
# Specifying the background

> [!QUESTION] Goal: which laws does an inquiry admit about its target before it seeks an answer, and on what grounds?

The background record states a body of laws admitted *a priori* about one [target system](target-system.md), with their closure and the organization: the relations among the parts or among the laws. The target-system record delimits the target: it fixes the referent and declares the quantities. The background record states claims about those quantities, and each such claim can be false of the system.

> [!IMPORTANT] One target, several backgrounds
> Several background records may describe one target, for instance two bodies of laws drawn from rival theories, or the laws of one subsystem beside those of another. Each question names its admitted background records in its [subject](subject-of-inquiry.md).

| Specification | When it is required | Options or frame | Examples | Source |
| ------------- | ------------------- | ---------------- | -------- | ------ |
| Describes — the target whose quantities the laws use | always | the identifier of one target-system record | the record of the trained networks; the record of the four tipping elements | — |
| Laws — known behaviors of the components or of the system | always | an expression over the symbols that the target declares, with its signature and the places that the claim ranges over (one entry each, empty when the law concerns the system as a whole). Its warrant (derived from other admitted laws, derived in a limit, posited, fitted or measured), with its grounds. Its role, one of six:<br>- evolution: how the state changes along the course<br>- input-output: how one quantity is determined by others at the same point<br>- measurement: how an instrument registers the state<br>- state-constraint: which states may hold together, including at the start and at the boundary<br>- distribution: the law of a random quantity<br>- admissibility: a restriction on the parameters or on the forms that a member may take | - the leaky integration of each neuron (one place, local, evolution)<br>- the gradient-descent learning rule (collective, evolution)<br>- the energy function on the state space (no place, state-constraint)<br>- the forward map of a network from its inputs to its prediction (input-output)<br>- the spike threshold of the recording (measurement) | laws of succession and coexistence, renamed by their function [winther2020] |
| Laws: origin | with each law | a pointer to the publication, the data set or the derivation from which the law is taken | the article that defines the model; the recordings to which a transfer function was fitted | [law appraised before admission](#^law-range) |
| Laws: range | when the law is established over part of the reference class only | an expression over declared symbols that bounds the conditions under which the law is established | a rate equation established for inputs below saturation; a scaling law established above a minimal width | [law appraised before admission](#^law-range) |
| Closure (of the laws) — separates a formal target from an empirical one | always | complete, for a formal target whose laws define the system · partial, for an empirical target that may admit a rule independent of them | the Wilson–Cowan equations define the model (complete); a recorded circuit, where a plasticity rule may still be discovered (partial) | [laws admitted as given](#^laws) |
| Organization | when the parts or the laws stand in a relation on which the behavior depends | per relation, its tuples and its laws. The tuples take the form `prod(source, reach)` or `subset(prod(source, reach), adjacency)`. A directed relation puts the reach last, and a joint one has three or more components. When the ends are laws, the relation names the laws that it orders, with the reach last | a transmitted signal between two climate subsystems; a nonreciprocal cross-coupling between two species fields; two populations jointly changing the growth of a third | organization of a mechanism [craver2007] |

- **A law is kept apart from the declarations because only a law can be false.** A declaration introduces a symbol and its value set, and asserts nothing about the system. A law asserts a dependence among declared quantities, so new evidence can refute it. Therefore, the two kinds of content change at different rates: the delimitation of a target stays fixed while the admitted laws are revised. Separate records let a question replace a body of laws without restating the quantities that enter those laws. ^law-is-a-claim

- **An empirical bridge law is an admitted law.** The [rule on bridge laws](target-system.md#^bridge-law) places such a law among the laws of a background record, under the role `measurement`.

- **The laws are admitted as given.** The record keeps the laws that are admitted *a priori* as relevant to characterizing the system. The inquiry may nevertheless seek new laws. The closure of a body of admitted laws separates a formal target from an empirical one, and it decides what a new law may be. For a formal target, the laws define the system, so a new law must be derivable from them, for instance an effective equation obtained in a mean-field limit. For an empirical target, a new law may be independent of the admitted ones, for instance a newly discovered plasticity mechanism. *Example*: the Edwards–Anderson spin glass consists of $N$ Ising spins $s_i\in\{-1,+1\}$ on the sites of a lattice, interacting through random couplings $J_{ij}$ between neighboring sites. The target record declares the spins, the site positions and the couplings. The background record admits the energy $H=-\sum_{\langle ij\rangle}J_{ij}s_is_j$ as a law [edwards1975]. ^laws

- **The closure qualifies one body of laws.** When several background records describe one target, each record states whether its own laws define the system. When a question admits two bodies of laws that are each complete, the question presupposes that the two bodies agree wherever both apply. ^closure

- **A law is appraised before it is admitted.** Each admitted law carries a warrant and an origin, and a range when it is established over part of the reference class only. The origin points to the source of the law, so a reader can check the law against that source. The range states the conditions under which the law is established. The range belongs to the law, because every question admitting the background inherits the same law. A bound written into the [domain](domain.md) of one question would leave the other questions unbounded. ^law-range

- **Every law is admitted *a priori*, and its warrant names the grounds.** The grounds differ between laws. A law derived from other laws holds only as long as those laws hold. A law that is posited, fitted or measured rests on a choice, a fit or an instrument, so new evidence revises such a law first. The warrant is therefore a property of the *law*. The warrant also propagates along dependence: a result resting on a measured law inherits the exposure of that law to revision. An answer built on the result inherits that exposure in turn. A [model](model-and-binding.md#^model-elements) states the warrant of its own laws in the same vocabulary. A [candidate answer](answer-form.md#^answer-elements) cites each law on which it rests, of the background or of a model, among its grounds with the role `warrant`, so a chain of dependence can be read from end to end. ^law-warrant

- **A relation among parts is internal to the target.** The external systems of the target fix its boundary, so they hold no relation whose ends both lie inside the target. Therefore, such a relation is stated in the organization. The organization names the laws stating the relation and the ordered tuples along which it runs. Those laws supply the quantities that carry the relation, namely the quantities indexed by every place of the relation. The target declares these quantities, so the organization declares none of its own. The reach comes last in each tuple, so the order of the components gives the direction. A tuple of three or more components states a joint relation. No pair of ends can state such a relation: two populations may together change the growth of a third without either population affecting it alone. ^organization

- **A relation whose ends are laws names and orders those laws, without a carrying quantity.** In a mechanism, the activities are organized as well as the parts [craver2007]. Two laws may therefore stand in a relation: for example, one law may run only after another has completed, or hold only while another holds. Such a relation puts the reach last. No expression carries such a relation, because no quantity is indexed by a law. A relation between laws adds content only where the law expressions leave the order open. Where the laws share an index, that index already fixes the order. *Example*: a distribution stated at step zero beside an evolution written over the later steps. For this reason, no record of the corpus states a relation between laws. ^law-ends

- **A law or a relation carried by only some members names its variant.** The target declares the [variants](target-system.md#^variants) of its class. An unmarked entry of the background holds of every member, so it may name only the symbols carried by every member. The check for unborne variants counts the marks of the background records as well: a variant marked by a background law is carried, even when no declaration of the target carries it.

---
## Sources

Marks follow the [legend of reading marks](../../CONTRIBUTING.md#^reading-marks).

- [craver2007] ◐ [Craver, _Explaining the Brain_, OUP, 2007](https://philpapers.org/rec/CRAETB-2)
- [edwards1975] ◐ Edwards & Anderson, "Theory of spin glasses", _Journal of Physics F_ 5, 965, 1975, via [a 2025 review of the field](https://arxiv.org/html/2505.24432)
- [winther2020] ◐ [Winther, "The structure of scientific theories", _SEP_, revised 2020](https://plato.stanford.edu/entries/structure-scientific-theories/), §3.1.1 on the state-space approach
