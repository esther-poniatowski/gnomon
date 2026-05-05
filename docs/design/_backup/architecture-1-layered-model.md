# Architecture - Layered Model

## Core design principle

A layer model is appropriate only if each layer:

- relies on **one clear kind of object**
- has a **clear dependency direction** with other layers
- can be replaced **without redefining the other layers**

## Stratification

The architecture is a **five-layer model**, preceded by a **meta-layer**. Each layer has a distinct ontological status, thereby separating different kinds of entities:

| Level | Layer                                 | Function                                                                                                                                                                                                                                                                 | Components (examples)                                                                                                                                   |
| ----- | ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| M     | **Meta-model**                        | Defines the **language of the system itself**. It contains the formal contracts that specify how to represent the research content.                                                                                                                                      | - object types<br>- relation types<br>- vocabulary<br>- field schemas, validation invariants<br>- namespace rules<br>- allowed cross-layer dependencies |
| 1     | **Canonical objects**                 | *What knowledge exists canonically*<br>Stores the **primary epistemic units** themselves, that form the *single source of truth for content*. Each object corresponds to one stable epistemic role.                                                                      | - question<br>- definition<br>- claim<br>- proof<br>- assumption<br>- example                                                                           |
| 2     | **Structural graphs and indexes**     | *How knowledge is organized and queried*<br>Contains the **organizational and computational structures** that make the canonical objects queryable and navigable.                                                                                                        | - identity registry<br>- relation registry<br>- dependency graph<br>- terminology index                                                                 |
| 3     | **Inquiry and arguments**             | *How knowledge is assembled to answer a question*<br>Contains **target-oriented assemblies** built from canonical objects and indexed relations. This layer captures the logic of inquiry itself: the act of constructing **minimal answer paths** relative to a target. | - argument bundle<br>- question decomposition<br>- minimal answer subgraph                                                                              |
| 4     | **View and rendering specifications** | *What to show to which audience and how*<br>Contains the **declarative specifications** that determine how content is turned into human-facing artifacts.                                                                                                                | - note manifest<br>- audience-specific rules<br>- rendering templates                                                                                   |
| 5     | **Derived artifacts**                 | *Concrete outputs and services*<br>Contains the **compiled documents** for exposition.                                                                                                                                                                                   | - summary note<br>- glossary<br>- dependency map<br>- unresolved issues dashboard                                                                       |

## Meta model - Architecture of the knowledge representation language

|Component|Role|
|---|---|
|**Type system**|Defines the admissible object types such as `question`, `definition`, `claim`, `proof`, `mechanism`, `assumption`|
|**Relation vocabulary**|Defines admissible edge types such as `answers`, `depends_on`, `requires_for_interpretation`, `proves`, `illustrates`|
|**Status schema**|Defines epistemic maturity categories|
|**Relevance schema**|Defines relevance roles and epistemic necessity|
|**Field contracts**|Required and optional fields per object type|
|**Cross-reference constraints**|Rules such as “a proof must prove exactly one claim-like object”|
|**Namespace model**|Scoping and modularity rules|
|**Versioning rules**|Identity, revision, provenance semantics|

**Invariants**:

- No canonical object may introduce an ad hoc field outside the schema without explicit schema extension
- No relation label may exist outside the declared vocabulary
- Every object type must have a formally specified identity contract

## Cross-layer dependency rules

To preserve single-source consistency, the architecture must enforce a **strict dependency direction between layers**. Each layer can only refer to objects and structures from the same layer or from layers upstream it in the hierarchy.

**Allowed direction**:

- the **canonical layer** conforms to the **meta-model**  
- the **graph/index layer** is built from the canonical layer  
- the **argument layer** selects from canonical objects and graph structures  
- the **view specification layer** selects from argument bundles and canonical/index data  
- the **artifact layer** is rendered from view specifications

Meta-model → Canonical objects → Indexes/graphs → Argument bundles → View specifications → Derived artifacts

==TODO: There might be indexes or graphs that reference arguments. Should the layer model be revise, or is it sufficient to inverse the order of dependencies?==

**Forbidden inversions**:

- a canonical object depending on a rendered note  
- an ontology decision inferred from a generated artifact  
- a graph edge created only in a note and not in the relation registry  
- an argument bundle containing content not represented in the canonical layer  
- a note manifest inventing relations absent from the graph layer  

## Functional distinctions

### Meta-model vs. Instances

This separation is essential for *stability*. Otherwise, every revision of the ontology (object types, relation types, status vocabularies, and invariants) destabilizes the whole knowledge base (the stored epistemic objects).

### Canonical objects vs. Graph structures

The object layer should contain objects that have **independent epistemic identity**. It should **not** contain search indexes, note manifests, dashboards, transitive closure tables, session plans, generated summaries...

The structural layer is derived from the canonical layer but maintained as a first-class structure because graph queries, indexing, ranking, and dependency analysis cannot be reduced to object-local fields.

### Inquiry assemblies vs. Canonical objects, Graph structures

An argument bundle is a **selected configuration** of existing objects _relative to a target question_. It is not reducible to:

- a canonical object (like a definition or theorem),
- a simple view,
- a mere graph index.

*Example*:

- A definition and a theorem exist independently.
- An argument bunfle is the assembly recognizing that these objects answer a specific queestion.

### View specifications vs. Rendered artifacts

This separation is essential for reproducible compilation.

- The generated outputs are ephemeral and derived.  
- The note specifications (contract that indicates what to include and how to render a note) are stable, auditable, and declarative. They do not store substantive epistemic content, but rather rendering intentions.

The distinction is analogous to:

- source code vs executable
- query plan vs query result
- template vs rendered page

### Rendered artifacts vs. Canonical objects

No artifact should become the primary source of truth. If manual edits were allowed in rendered notes, the architecture collapses back into document-centric drift.

Instead, only the canonical content can be edited, while rendered artifacts are regenerated from them, following stable specifications and rules.

### Meta-model vs. View specification

Both layers share three superficial properties:

- both contain declarative rules, static formal specifications
- both are relatively stable compared with instance data,
- both may be edited infrequently and reused many times.

However, they regulate different objects and kind of validity:

| Layer                                      | **Meta-model**                                                                                                                                                                                                                             | **View specification**                                                                                                                                                |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Role                                       | Constitutive: determines **what the system is allowed to mean** (i.e. representational language of the system, the identity conditions of the epistemic objects)                                                                           | Instrumental: determines **what the system is asked to produce** (how existing objects are operationally used to produce output artifacts)                            |
| Governing question                         | What kinds of epistemic objects and relations are admissible in the knowledge base, and under what formal conditions?                                                                                                                      | How *existing* objects should be selected, ordered, transformed, and displayed?                                                                                       |
| Constraints                                | Constitutive constraints (semantic admissibility, knowledge representation rules)                                                                                                                                                          | Derivational constraints (rendering admissibility, presentation compilation rules)                                                                                    |
| A rule belongs here if violating it means: | - the object is ill-formed as an epistemic object<br>- the graph is semantically invalid<br>- the knowledge base loses representational coherence                                                                                          | - the output is ill-formatted<br>- inappropriate objects were selected<br>- the exposition is unsuitable for the audience                                             |
| Examples                                   | - `definition` objects may have a `notation` field<br>- `proof` must prove exactly one claim-like object<br>- `answers` may link only from claim-like objects to question-like objects<br>- `status` must belong to a fixed vocabulary<br> | - suppress proof bodies in pedagogical summaries<br>- order definitions before theorems<br>- include only load-bearing objects<br>- render examples as callout blocks |

This is analogous to the distinction between:

- a **database schema** and a **report template**
- a **logical language** and a **document layout specification**

Dependency asymmetry:

- The view layer _presupposes_ the meta-model layer, because a rendering rule can only refer to object types, fields, and relations that have fixed meanings.
- The reverse does not hold: the ontology of an object does not depend on the existence of any particular rendering template.

### Canonical objects vs. View specifications

|Layer|**Canonical layer**|**Expository layer**|
|---|---|---|
|Role|Source of truth|Rendered views for particular audiences|
|Contents|- formal objects  <br>- metadata  <br>- relations  <br>- status  <br>- justification structure|- pedagogical notes  <br>- summaries  <br>- presentations for different audiences  <br>- context-specific formulations|

The note generation step is architecturally analogous to **literate programming** (Knuth) and to the **model-view separation** in MVC. The structured object files constitute the **canonical model**; notes, summaries, and presentations are **views** compiled from subsets of this model via explicit selection and rendering pipelines.

This makes the note a **derived artifact** with a computable provenance, rather than a manually curated document that may silently diverge from the underlying framework. Changes to the underlying objects automatically propagate as detectable diffs in derived notes.

> [!NOTE]
> If the term "meta-model" seems too broad because the view layer is also "meta" with respect to instances, an alternative terminology is:
> - **Representational specification layer**
> - **Rendering specification layer**

### "Query layer"?

A *query* defines an *operation* over:

- canonical objects
- typed relations
- argument bundles
- status and relevance indexes

*Examples*:

- what is necessary to answer a question
- which claims depend on an answer
- which proofs remain incomplete

Thus, a query does *not* define a new kind of stored object. 

Therefore, a "query layer" should **not** be treated as a persistence architectural layer parallel to the others. It is better understood as a **service interface** operating over the structural and inquiry layers.