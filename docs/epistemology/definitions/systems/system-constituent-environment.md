---
role: definition
status: wip
index: "[Bearers and systems](docs/epistemology/definitions/systems/_index.md)"
aliases:
  - System, constituent and environment
  - System
  - Constituent
  - Environment
  - Structure and organization
tags: []
source:
---
# System, constituent and environment

> [!QUESTION] Goal: how are a system, its constituents, its environment and its structure told apart?

A **system** is a complex object whose constituents are bound by relations. Its simplest description lists three items [bunge1979]:
$$\langle \mathsf{Comp}(\sigma),\mathsf{Env}(\sigma),\mathsf{Str}(\sigma)\rangle$$

- the composition $\mathsf{Comp}(\sigma)$: the constituents of the system $\sigma$;
- the environment $\mathsf{Env}(\sigma)$: the things outside $\mathsf{Comp}(\sigma)$ that act on constituents or are acted on by them;
- the structure $\mathsf{Str}(\sigma)$: the relations among the constituents.

A later version of this description adds a fourth item, the mechanism $\mathsf{Mech}(\sigma)$, glossed as "the mechanisms, or characteristic processes of σ" [bunge2004]. That sense of mechanism differs from the sense used in mechanistic philosophy, as the [vocabulary of mechanism](../regularities/mechanism-and-mechanistic-model.md) states.

## Senses

| Term | Definition | Near-synonyms | Source |
| --- | --- | --- | --- |
| System | a complex object whose constituents are bound by relations | — | [bunge1979] |
| Constituent | a member of $\mathsf{Comp}(\sigma)$: an object that stands in the part–whole relation to the system | component, part | [simons1987]; [bunge1979] |
| Environment | the set $\mathsf{Env}(\sigma)$ of things outside the composition that act on constituents or are acted on by them | surroundings | [bunge1979] |
| Structure | the set $\mathsf{Str}(\sigma)$ of relations among the constituents, regardless of their relevance to a behavior | — | [bunge1979] |
| Organization | the relations among parts and activities on which a behavior of the whole depends, so that the behavior is not the sum of the behaviors of the parts | arrangement | [craver2007] |

Constituent, component and part are synonyms only relative to one system. Mereology treats "part" as an absolute relation between two objects [simons1987], whereas "constituent" always refers to a containing system.

## Distinctions

- **System, constituent and environment are *roles*.** No object is a system, a constituent or an environment by its kind: a neuron is a constituent of a circuit and a system of ion channels. The role of an object is fixed by the choice of a boundary. Given that boundary, each object $x$ of a description falls in exactly one of three classes: $x\in\mathsf{Comp}(\sigma)$, $x\in\mathsf{Env}(\sigma)$, or neither. The third class holds when $x$ neither belongs to the system nor acts on it. ^system-role-test
- **Organization is the part of the structure on which a behavior depends.** The structure lists every relation among the constituents, including relations that change no behavior of interest. *Example*: a matrix of correlations among neurons describes part of the structure before any causal reading of it is supplied. The organization keeps the relations that make a behavior of the whole non-aggregative [craver2007]. The test is an intervention: rearranging the constituents changes the behavior only when the rearranged relations belong to the organization. Organization takes the form of a typed relational structure in the [specification of a mechanism](../../mechanism.md).
- **A configuration is not a structure.** The structure holds the relations that persist while the system evolves. A configuration is the arrangement of the constituents at one instant, as defined in the [vocabulary of state](../quantities/state-and-configuration.md).

## Consequences for a record

The items of the system description correspond to blocks of two records, the [target specification](../../target-system.md) and its [background](../../background.md):

| Item | Block of a record |
| --- | --- |
| Composition $\mathsf{Comp}(\sigma)$ | constituents of the target specification, with their kinds and index sets |
| Environment $\mathsf{Env}(\sigma)$ | external systems of the target specification, restricted to those that share a variable with the target |
| Structure $\mathsf{Str}(\sigma)$ | parameters of the target specification indexed by several constituents, such as a connectivity weight |
| Organization | the organization of a background record, keeping only the relations on which the behavior depends |

- **The environment of a record is narrower than the environment of a system.** An external system enters the record only through the variables shared with the target. Therefore, when a thing acts on the target through no declared variable, the record omits that thing. That restriction is a modelling decision, and the inquiry may revise it by [moving a variable across the boundary](../../target-system.md).
- **The [role test of a system](#^system-role-test) runs on the declarations.** A constituent kind places its members in $\mathsf{Comp}(\sigma)$, an external system places its members in $\mathsf{Env}(\sigma)$, and an object declared nowhere falls in neither class.

---
## Sources

Marks follow the [legend of reading marks](../../../../CONTRIBUTING.md#^reading-marks).

- [bunge1979] ◐ [Bunge, *Treatise on Basic Philosophy*, vol. 4, *Ontology II: A World of Systems*, Reidel, 1979](https://doi.org/10.1007/978-94-009-9392-1); the triple of composition, environment and structure is confirmed through secondary sources only
- [bunge2004] ◐ [Bunge, "How does it work? The search for explanatory mechanisms", *Philosophy of the Social Sciences* 34(2), 182–210, 2004](https://doi.org/10.1177/0048393103262550); section "The CESM model"
- [craver2007] ◐ [Craver, *Explaining the Brain: Mechanisms and the Mosaic Unity of Neuroscience*, Clarendon Press, 2007](https://doi.org/10.1093/acprof:oso/9780199299317.001.0001)
- [simons1987] ◐ [Simons, *Parts: A Study in Ontology*, Clarendon Press, 1987](https://doi.org/10.1093/acprof:oso/9780199241460.001.0001)
