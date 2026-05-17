
# Ontology of epistemic entities — Quality Criteria and Principles


> [!QUESTION] Which entities possess enough epistemic autonomy to deserve canonical persistence?

## Objectives and Criteria

### Ontological criterion

A canonical object should exist only if it satisfies all five conditions below:

| Criterion                      | Meaning                                                                                                                                                                                                                          |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Unitary epistemic role**     | The object performs one intelligible epistemic function: define, ask, assert, justify, exemplify, construct. Types must differ in the _reasoning operations_ they license, not merely in surface content or rhetorical function. |
| **Independent identity**       | The object can be referred to, revised, compared, or reused without referring to a particular note, query, or rendering.                                                                                                         |
| **Context-transcendent reuse** | The same object can participate in multiple inquiries, bundles, and outputs.                                                                                                                                                     |
| **Local validity conditions**  | It has intrinsic well-formedness criteria.                                                                                                                                                                                       |
| **Independent editability**    | Revising the object does not amount to merely changing an index, a path, or a display format.                                                                                                                                    |
| **Irreducibility**             | A type is admissible only if it cannot be faithfully encoded as a configuration of existing types without loss of structural information or inferential role.                                                                    |

The correct standard is not mere linguistic convenience, but **ontological compression under operational adequacy**. A type is justified only if all three conditions hold:

1. **Primary content condition**: the object carries content that is not merely parasitic on another object plus metadata
    
2. **Operational condition**: the framework would need to query, validate, compare, compose, or reuse that content directly
    
3. **Non-distortion condition**: encoding it through another type would either erase structure, force heterogeneous objects into one schema, or shift essential content into opaque fields

This criterion excludes candidates that are **not epistemic units**, such as:

- search indexes  
- dependency closures  
- dashboards  
- answer paths  
- session plans  
- summary notes  
- relevance rankings  
- pedagogical views
- rendered documents  

### Functional criterion

> [!INFO] The "unit of progression vs. unit of epistemic work" distinction is migrated to [functional separation of concerns](../../1-framework/framework-foundations#^t1-functional-separation). The motivation-encoding and epistemic-work-encoding decisions remain as theme-local D's.

The framework must introduce object types that are necessary to encode the local advancement of inquiry and preserve intelligibility. 

To be stable, object types must be distinguished by they **function**, not their superficial structure.
Otherwise, the distinction risks becoming merely **size-based** ("atomic" vs "composite"), which is unstable and leads to regress.

*Example*: The taxonomy of reasoning types (deduction, induction, abduction) must no be the right primary axis for the object model. It is usually too coarse, too heterogeneous, and classifies completed arguments from the outside. That distinction remains useful at most as a secondary annotation on some inferential moves.

The framework must distinguish:

1. **the unit of progression**, the function of **guiding the inquiry**
2. **the unit of actual epistemic work**, the function of **executing the epistemic work**

A framework that represents only motivated progression remains too rhetorical.  
A framework that represents only concrete analyses remains unintelligible.  

A research argument usually contains at least three dimensions, that map to distinct **system components**:

| Dimension   | Function                                        | Typical content                              | System components                                                                                     |
| ----------- | ----------------------------------------------- | -------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| Orientation | Explains why the next move is introduced        | obstacle, local goal, strategic idea         | the _question/goal_ objects + the strategic annotation on assemblies (what the inquiry pursues)       |
| Execution   | Performs the actual work                        | derivation, comparison, construction         | the _operation schema_ + the _canonical object_ it produces (where the actual epistemic work lives)   |
| Integration | Connects the local result to the larger inquiry | what has been established, what remains open | the _dependency graph_ + the _explanatory annotation_ on assemblies (how moves cohere into an answer) |

That is genuinely useful to justify _why the architecture introduces those particular kinds of objects_. It belongs at the architectural level (a Tier 2 commitment about object kinds). 
This classification is distinct from the _justificatory level_ (annotation kind on a move), it concerns the _system component_ (where in the architecture an annotation lives or what carries the work).

### Architectural criterion

The ontology should remain **narrow in object kinds** and **rich in typed relations and fields**.

A weak ontology usually proliferates object types because it tries to encode every practical distinction as a distinct entity class. A strong ontology does the opposite:

- only stable epistemic roles become object kinds
- rhetorical, procedural, target-relative, or presentational distinctions become fields, statuses, or higher-layer annotations

This yields a knowledge base that is both more rigorous and more adaptable.


A robust ontology should therefore remain **small, closed, and role-pure**, while more local distinctions are pushed into fields or layer-specific annotations.

### Tradeoffs and warnings

**Excessive granularity**. If every sentence becomes an object, the system becomes unmanageable. If objects are too coarse, retrieval loses precision. A good practical unit is: one stable conceptual or argumentative function per object.

**Ontology instability**. If object types are redesigned continuously, the framework becomes unstable. Therefore:

- begin with a small ontology
- allow subtypes gradually
- version the ontology itself

### Backup

The principal risk is **misfactoring**. Several kinds may be compressed into attributes (e.g. in `CLAIM`) or broad formulations (e.g. in `MODEL`), but they differ too strongly in **epistemic function**, **dependency profile**, and **graph behavior** to remain transparent under that compression. Then, the ontology is **not optimally expressive**, because:

> It suppresses a small number of distinctions that *materially improve intelligibility*. Some central reasoning structures become artificially flattened.

The main recommendation is not to expand indiscriminately. The correct axis for a typed reasoning graph is to center the ontology on **epistemic role** rather than on surface linguistic form. Each primitive must capture a major organizational pole of theoretical inquiry.

The principal architectural lesson is the following: the ontology should privilege **content-bearing reusable structures** over discourse labels, but it must not confuse **search-guiding practical rationality** with mere annotation.

> [!FAIL]
> The central sufficiency problem is that the ontology is better at representing **content units** than **orientation structures**. 

Theoretical research is not only a sequence of claims and arguments. It is also guided by:

- background commitments
- standards of admissibility
- preferred explanatory ideals
- problem-framing lenses
- strategic motivations for certain decompositions

---

## Remaining Unresolved Risks (backup)

- **Hybrid objects remain unavoidable**: Definitions, explanations, interpretations, and mechanistic accounts are genuinely cross-cutting. No ontology will remove all mixed cases. The aim should be **controlled hybridity**, not impossible purity.

- **Overreliance on attributes may reintroduce opacity**: Even with seven primitives, excessive attribute compression can silently collapse important differences. Subtype policy matters almost as much as primitive choice.

- **Relation design is as important as node design**: A node ontology with weak relation semantics will still yield poor structural intelligibility. This proposal’s final success depends heavily on relation families.

- **FRAMEWORK can become a junk drawer**: Unless defined narrowly, `FRAME` risks absorbing everything background-like. That would destroy its usefulness. It must be reserved for coherent background configurations that condition admissibility, relevance, and evaluation.

- **Token/type ambiguity must be controlled**: Several tensions arise because token-level reasoning events and type-level reusable structures are mixed. This is especially acute for argument, method, analogy, and model. The implementation must enforce this distinction clearly.

---

**Cross-FRAMEWORK reasoning.** Framework comparison, paradigm shift, and incommensurability analysis all require structure that spans multiple FRAMEWORKs. The current ontology provides no cross-FRAMEWORK relational primitives. FRAMEWORK-to-FRAMEWORK relations (INCOMMENSURABLE-WITH, TRANSLATES-INTO, SUBSUMES, CONFLICTS-WITH) are necessary for paradigm-level reasoning to be structurally transparent rather than merely asserted.

**Dynamics.** ==CRUCIAL== The ontology is essentially static — it represents the structure of epistemic objects but not their dynamics, how knowledge is constructed via inferential moves. The ontology cannot represent the epistemic dynamics of ongoing inquiry. 

**Token–type distinction**: This distinction is not optimally structurally unresolved. The ontology sometimes conflates type-level schemas (an argument form, a modeling strategy, a method class) with token-level instantiations (a specific proof, a concrete model, an applied procedure).

**Granularity calibration.** ==IMPORTANT== The token/type stratification resolves one dimension of granularity but not all. The ontology does not specify the granularity criteria for node individuation — when two similar CLAIMs are distinct nodes versus variants of one node, or when a sub-argument warrants its own ARGUMENT node versus being internal to a parent ARGUMENT. Without explicit individuation criteria, different annotators will produce structurally incomparable graphs, undermining the ontology's utility for systematic reasoning representation.

## Design Constraints

**Coverage completeness**: the set must span the full space of epistemic moves required — formal derivation, mechanistic explanation, semantic grounding, motivational scaffolding, contrastive clarification, and inquiry direction.

### Attributes vs. Objects

> What is merely **attributive** or **relational** should not be reified into a standalone object unless independent identity, reuse, addressability, or internal structure is required.

A candidate epistemic entity should become a standalone object only if at least one of these conditions holds:

| Criterion                  | Meaning                                                                                     |
| -------------------------- | ------------------------------------------------------------------------------------------- |
| **Independent identity**   | It must be referred to independently of a host object and linked from several places        |
| **Reuse**                  | The same entity can be involved in multiple objects                                         |
| **Internal structure**     | It has nontrivial substructure worth encoding                                               |
| **Independent evaluation** | It can be accepted, rejected, revised on its own, or compared and classified across objects |
| **Graph participation**    | It participates in many relations as a node, not merely as an attribute                     |

If none of these holds, the candidate should remain:

- a role-bearing field: intrinsic metadata attributed to a host object
- a structured record: embedded component or row in a table (not a top-level epistemic object)
- a typed relation

_Examples_: 

- A *motivation* is not usually an independent epistemic entity. It is the answer to a meta-question associated to a host object:
	- a question: why is it worth asking?
	- an answer: why is it relevant?
	- an inferential move: why is it introduced here?
	- a concept: why is it needed?
  A `motivation` field of type `str | Ref[Question | Problem]` is sufficient and avoids polluting the ontology with an object whose schema is simply a `Claim` with a rhetorical role tag.
	
- A *dependency* is normally a typed relation between objects. They are typed edges in the epistemic graph. A dependency would deserve reification as structured relation instances only when the relation itself has substantial internal content, such as a modality (necessary, sufficient, defeasible, heuristic), a justification of the dependency, a scope restriction...
	
- A *limitation* is typically a qualified property of another object:
	- an answer has a domain of validity
	- a method has failure conditions
	- an inferential move has non-established consequences
	- a model has idealizing assumptions
	A reusable limitation object may be justified only if the same limitation applies to several answers or methods.

### Inheritance over duplication

The `EpistemicObject` base class enforces interface contracts (dependency graph participation, cross-referencing, registry enrollment) without requiring subtype proliferation for what are properly attribute variations.

The ontology should remain **narrow in object kinds** and **rich in typed relations and fields**.

A weak ontology usually proliferates object types because it tries to encode every practical distinction as a distinct entity class. A strong ontology does the opposite:

- only stable epistemic roles become object kinds  
- rhetorical, procedural, target-relative, or presentational distinctions become fields, statuses, or higher-layer annotations  

A robust ontology should therefore remain **small, closed, and role-pure**, while more local distinctions are pushed into fields or layer-specific annotations.

This yields a knowledge base that is both more rigorous and more adaptable.

**No strict inheritance relation**:

The analogy with OOP is productive for **composition** and **interface contracts**, but **inheritance** in the classical OOP sense (subtype polymorphism, behavioral substitutability via the Liskov principle) does not map cleanly onto epistemic objects.

_Example_: A `lemma` is not substitutable for a `theorem` in a proof context — their roles in the dependency graph differ structurally.

The correct analogy is closer to **algebraic data types** with **tagged unions** (sum types), where subtypes are disjoint variants of a broader epistemic category, not extensions of a shared behavioral interface.

_Example_: `{theorem, lemma, corollary, conjecture}` are better modeled as variants of a `formal_claim` sum type than as a subtype hierarchy.

## Ontological confusions

To avoid ontology inflation and instability, distinct ontological categories must be separated:

| Category                                                                                      | Example                                                              |
| --------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| **Object kind** (epistemic units)                                                             | `claim`                                                              |
| **Relations** (edges of the dependency graph schema, not the type registry)                   | _entailment_, _contradiction_, _instantiation_, _refinement_         |
| **Derived computational structures** (belong to the graph/index or service layer)             | dependency set, top-ranked answer path, similarity cluster           |
| **Expository or rhetorical role** (attribute of a claim inside an argument or exposition)     | `lemma`, `theorem`, `corollary`, `premise`, `remark`, `illustration` |
| **Inquiry-relative role, motivation** (why a concept is introduced, why an approach is taken) | `relevant-to-question`, `load-bearing`, `optional`, `prerequisite`   |
| **Epistemic status** (applies uniformly across types, must not proliferate subtypes)          | `proved`, `open`, `draft`, `contested`                               |

## Ontology decision table

Construct an **ontology decision table** to force every ambiguous candidate into exactly one ontological slot and will eliminate most later inconsistencies.

|Candidate entity|Canonical object kind|Field/status/relation instead|Reason|
|---|---|---|---|

Typical rows should include:

- theorem  
- lemma  
- conjecture  
- proof sketch  
- question  
- open problem  
- dependency path  
- answer plan  
- summary note  
- example  
- counterexample  
- source excerpt  
- relevance score  

