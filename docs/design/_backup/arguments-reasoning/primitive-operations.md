
# Primitive operations to avoid infinite regress

Infinite regress appears whenever a component is defined only by an informal placeholder such as:

- method
- procedure
- intermediate result
- comparison
- derivation
- interpretation

All complexity is merely displaced into vague labels, answer is reduced to "a step containing smaller steps". Each such term immediately raises the question:

- what exactly is this
- how is it internally articulated
- what makes it a legitimate move
- how are its subparts connected

The framework need a **closed operational core** defined by a **typed calculus of epistemic operations**. This requires **library of primitive epistemic operation types**, with fixed functional semantics, i.e. each with a precise signature.

> The executable core of the framework is an **application of a typed operation schema** to explicitly bound operands, under explicit preconditions, producing explicitly typed outputs.

The framework explicitly declares some operation schemas to be **primitive** with respect to the framework.

**Stopping rule**: An object is primitive if:

- the operation is part of the accepted operation library
- its semantics is taken as given inside the system: its input and output contracts are explicit
- it does not need further decomposition unless desired for exposition or audit
- its justification is by **schema validity**, not by a further nested chain

A **schema** may be treated as primitive only if the framework can provide all of the following:

|Requirement|Meaning|
|---|---|
|fixed typed signature|exact input and output roles|
|explicit admissibility conditions|when it may be used|
|explicit transformation semantics|what it does|
|explicit success condition|what completion means|
|explicit license kind|how it is justified|

If one of these elements is missing, the schema is still too vague and should not enter the primitive library.

> [!NOTE] Analogy
> This is exactly how [formal systems](vendor/gnomon/docs/references-methods/overview-formal-frameworks) avoid regress: 
> - proof theory: inference rules
> - programming languages: primitive instructions
> - workflow systems: typed tasks with contracts
> - category-theoretic semantics: morphisms with domain and codomain constraints

Then:

- a proof and an informal argument are graphs of operation applications
- higher-level "steps" are only **macro-structures over that graph**
- the regress stops at a finite set of **primitive operation types** whose semantics is given by the framework itself

The primitive operation library can be initialized by building a first **formal signature table** of perhaps 10 to 15 primitive schemas, split into:

- proof-theoretic operations
- analytic/computational operations
- evidential operations
- interpretive operations