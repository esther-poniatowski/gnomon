# Ontological Design for an Epistemic Object Framework - G3

## I. Necessity

## 1. CONCEPT

### Claimed function

A non-truth-apt semantic circumscription of a theoretical entity, prior to and enabling claims.

### Adversarial pressure

The central difficulty is that the proposal oscillates between two distinct notions:

1. **lexical/conceptual resource**: a term, category, or inferentially usable concept
    
2. **intensional content specification**: applicability conditions, scope, content

The first is clearly non-propositional. The second is rarely non-propositional. Once applicability conditions, scope, and inferential use are made explicit, the content is ordinarily expressed through a network of definitional, exclusionary, comparative, and inferential **claims**. The ontology itself acknowledges this by collapsing **definition** into CLAIM.

This creates a pressure point: if the content of a concept is always carried by claims, then CONCEPT risks being reduced to a **node of semantic reference**, not a full epistemic object type. In that case, it is a registry entity or symbol-table item, not an ontological primitive on a par with QUESTION or MODEL.

### Can it be encoded elsewhere?

Two possibilities exist.

#### Collapse option A: eliminate CONCEPT as a primitive

Treat concepts as:

- typed identifiers or semantic handles
    
- whose content is given by definitional and usage claims
    
- whose relations are carried by claim graphs
    

This is a non-distorting encoding if the ontology is concerned with **epistemic objects in reasoning**, rather than with independent semantic objects.

#### Retention option B: keep CONCEPT, but thin it radically

Then CONCEPT cannot carry “applicability conditions” or “scope” as intrinsic content if those are truth-apt. It must be restricted to:

- referential identity
    
- term variants
    
- links to definitional claims
    
- conceptual lineage or provenance
    
- perhaps inferential role tags, but not truth-apt content
    

Otherwise the boundary with CLAIM collapses.

### Verdict

**Not clearly necessary in the thick form proposed.**  
Only a **thin concept node** is defensible. The current thick formulation is unstable.

---

## 2. CLAIM

### Claimed function

The sole truth-apt primitive.

### Adversarial pressure

This is the strongest part of the ontology. A single truth-apt primitive is an effective compression move. Many rejected candidates are correctly absorbed here.

The only adversarial concern is that CLAIM is doing too much. It absorbs:

- theorem
    
- hypothesis
    
- evaluation
    
- definition
    
- interpretation
    
- norm
    
- distinction
    
- structural mapping
    
- instantiation
    
- counterexample
    

This is acceptable only if those are indeed variations in propositional role rather than genuinely distinct object kinds. For most of them, that is correct.

However, two absorbed cases remain problematic:

1. **normative/prescriptive content**
    
2. **meta-epistemic content about the status of other objects**
    

Normative content can often be represented propositionally, but this does not yet show that its operational role is exhausted by CLAIM. The issue returns under METHOD.

### Verdict

**Necessary.**  
No collapse pressure here. CLAIM should remain the unique truth-apt primitive.

---

## 3. ARGUMENT

### Claimed function

Structured inference from premises to conclusion, with warrant and backing.

### Adversarial pressure

The proposal is correct that an argument is not just an unordered claim-set. However, the key question is whether ARGUMENT is a primitive type or a **structured relation** among claims. That is a much harder question than the proposal admits.

An argument contains:

- input claims
    
- output claim
    
- inferential license
    
- sometimes defeasibility conditions, burdens, dialectical orientation
    

This looks less like a separate ontological object type and more like a **higher-order structure over claims**. In graph-theoretic terms, ARGUMENT may be an **edge-object** or hyperedge with metadata, not a primitive object kind alongside MODEL or QUESTION.

The Carroll regress point is not decisive. It shows that warrant must be explicitly represented; it does **not** show that ARGUMENT must be a primitive ontological type rather than a structured inferential relation.

### Can it be encoded elsewhere?

Three possibilities exist.

#### Collapse option A: ARGUMENT as a typed relation schema

Represent:

- premises: CLAIM-set
    
- conclusion: CLAIM
    
- warrant type
    
- backing claims or methods
    
- defeat conditions
    

This preserves structure without requiring ARGUMENT as a primitive object type. One obtains an ontology of objects plus relations, rather than inflating relations into object kinds.

#### Collapse option B: ARGUMENT under METHOD

If inferential schemas are treated procedurally, arguments may be tokens of method application. This is too strong a collapse and likely distorting, because actual arguments are also evaluable products.

#### Retention option C: retain ARGUMENT as a reified relation-object

This is plausible operationally, but the justification must be: “arguments must be addressable, comparable, attacked, reused, and evaluated as first-class objects.” That is a pragmatic and architectural argument, not a pure irreducibility argument.

### Verdict

**Only weakly necessary as a primitive.**  
More plausibly, ARGUMENT is a **reified inferential relation** rather than a basic epistemic object type.

---

## 4. QUESTION

### Claimed function

A structured epistemic gap with answer conditions, presuppositions, and decomposition.

### Adversarial pressure

This type is highly defensible. A question is not simply a negative claim about ignorance. It has:

- answerhood conditions
    
- erotetic dependence
    
- admissible answer type
    
- presuppositions
    
- resolution criteria
    

These are not truth conditions. Reduction to CLAIM is distorting.

A further strength is that research architecture actually depends on questions as organizational attractors. Without QUESTION, decomposition and inquiry control become second-order hacks.

### Verdict

**Necessary.**  
This is one of the most stable primitives.

---

## 5. MODEL

### Claimed function

A structured abstract representational object enabling inferential and generative operations.

### Adversarial pressure

This is the most successful primitive in the proposal. The distinction between:

- claims **about** a structure
    
- and the structure **used as a representational or inferential object**
    

is real and important.

A model can be:

- manipulated
    
- simulated
    
- parameterized
    
- compared
    
- idealized
    
- instantiated
    
- analyzed for consequences
    

without reducing those operations to asserting propositions. This is a strong irreducibility case.

The main challenge is not necessity, but boundary purity with ARGUMENT and CLAIM.

### Verdict

**Necessary.**  
Retention is justified.

---

## 6. METHOD

### Claimed function

A structured procedural or prescriptive schema governing generation, evaluation, and transformation of epistemic objects.

### Adversarial pressure

This is the weakest primitive in the proposal.

The defense relies on the distinction between **knowing-how** and **knowing-that**. Philosophically, that distinction is genuine. Ontologically, however, it does not yet establish that METHOD must be a separate primitive in this system. The actual question is not whether procedural knowledge exists, but whether it is an irreducible **epistemic object type for structured reasoning**.

The proposed METHOD contains:

- step structure
    
- admissible transformations
    
- stopping criteria
    
- expected outputs
    
- decision points
    

This description mixes three heterogeneous things:

1. **algorithmic procedure**
    
2. **normative policy or rule**
    
3. **research plan or strategy**
    

That is already a sign of ontological impurity.

Moreover, much of METHOD can be encoded as:

- a **MODEL** of a process or workflow
    
- plus **CLAIMS** about permissibility, success criteria, and stopping conditions
    
- plus perhaps **QUESTION** links for target states
    

The claim that METHOD is “not a description of a procedure but the prescriptive schema itself” is not sufficient. In a representation system, the method is always represented somehow. Once represented, its structure is accessible as a rule-governed object. The issue is whether this represented object is fundamentally different from a process-model plus normative claims.

### Can it be encoded elsewhere?

Yes, plausibly.

#### Collapse option A: METHOD into MODEL + CLAIM

- workflow/process graph as MODEL
    
- norms, admissibility rules, stopping conditions as CLAIMs
    
- target questions as QUESTION links
    

This encoding is awkward only if one insists that procedures must be executable operators. But executability is an implementation property, not necessarily an ontological primitive.

#### Collapse option B: split METHOD into two types

If METHOD is retained, it likely hides two irreducible objects:

- **RULE / POLICY** for admissibility and transformation norms
    
- **PLAN / PROCEDURE** for ordered action structure
    

But introducing those would enlarge the ontology, not minimize it.

### Verdict

**Not convincingly necessary as a primitive.**  
Strong collapse pressure toward **MODEL + CLAIM**, unless the system explicitly requires executable procedural objects as first-class entities.

---

## Necessity verdict

Under a strict adversarial reading:

- **Clearly necessary**: CLAIM, QUESTION, MODEL
    
- **Conditionally defensible**: ARGUMENT
    
- **Weak / unstable**: CONCEPT, METHOD
    

A strong compression candidate is therefore:

- eliminate **METHOD**
    
- thin or eliminate **CONCEPT**
    
- possibly demote **ARGUMENT** from primitive type to reified relation
    

---

## II. Sufficiency

The ontology is close to sufficient for many reasoning tasks, but not fully sufficient without either extending type structure or enriching relation structure.

## 1. Missing meta-epistemic object?

The proposal says objects have “epistemic status,” but status is treated as an attribute. That is often adequate for simple cases such as:

- conjectural
    
- established
    
- refuted
    
- uncertain
    

It becomes inadequate once meta-epistemic structure itself becomes complex and reasoned about, for example:

- justification profile
    
- evidential dependence
    
- defeat status
    
- confidence calibration
    
- domain of validity
    
- robustness under model assumptions
    
- controversy profile
    
- source-sensitive trust structure
    

Those are not mere scalar attributes. They are structured evaluative objects. Still, it does **not** follow that a new primitive type is needed. Much of this can be represented by CLAIMs about other objects, or typed metadata schemas.

### Verdict

No new primitive is forced here.

---

## 2. Missing planning/strategy object?

The ontology asks about research strategy and planning objects. Those are not comfortably housed.

A research strategy is not just a method. It typically includes:

- ordered question priorities
    
- conditional branching under uncertainty
    
- evidential acquisition policy
    
- resource-aware sequencing
    
- fallback criteria
    
- local rationale for path selection
    

This is more than procedure and less than model. It may be encoded as METHOD, but only by stretching METHOD toward planning. That stretch is one reason METHOD is unstable.

Still, strategy can likely be represented as:

- METHOD or process MODEL
    
- plus CLAIMs of rationale and constraints
    
- linked to QUESTIONs
    

### Verdict

No decisive missing primitive, but current METHOD is under-specified and overloaded.

---

## 3. Missing data/evidence object?

This is the most serious sufficiency pressure.

The ontology has CLAIM, MODEL, ARGUMENT, QUESTION, METHOD, CONCEPT. Where are:

- observations
    
- datasets
    
- measurements
    
- source extracts
    
- textual evidence
    
- experimental outputs
    

The proposal may intend to encode all of these as CLAIMs. That is often too coarse.

A dataset or observation record is not merely a claim that “x was observed.” It can function as:

- an evidential base
    
- an input to model fitting
    
- an object of reanalysis
    
- a structured record independent of any single interpretation
    

This parallels the MODEL case: there is a difference between

- a claim about data
    
- and the data structure itself as an epistemic object
    

If the intended domain includes theoretical research broadly, especially empirical or historical science, then **EVIDENCE** or **RECORD** becomes a serious candidate primitive.

### Does EVIDENCE satisfy the criteria?

#### Primary content irreducibility

A dataset, observation record, or source excerpt is not exhausted by claims about it.

#### Operational usefulness

It plays a distinct role as evidential input, not merely as proposition or model.

#### Non-distorting encoding requirement

Encoding evidence solely as claims forces premature propositionalization and loses raw or structured evidential form.

This is a stronger case than METHOD.

### Verdict

There is a genuine sufficiency gap if empirical or source-based reasoning is in scope.  
A primitive such as **EVIDENCE** or **RECORD** may be more justified than METHOD.

---

## 4. Missing representation of transformations or abstractions?

Abstraction, idealization, generalization, and operationalization are important reasoning moves. However, those appear better treated as:

- ARGUMENT patterns
    
- METHOD steps
    
- CLAIM relations
    
- MODEL transformations
    

No new primitive is forced.

---

## Sufficiency verdict

For purely theoretical and formal inquiry, the ontology is **nearly sufficient**.  
For broader philosophy of science or empirical-theoretical research, it likely lacks a primitive for **EVIDENCE / RECORD**.

Paradoxically, the current ontology may be missing a better candidate while retaining a weaker one.

---

## III. Purity: boundary instabilities

## 1. CONCEPT vs CLAIM

### Locus of overlap

Definitions, applicability conditions, scope, and inferential role are often propositional. Once made explicit, they are usually claims.

### Why unstable

The proposal says:

- CONCEPT carries intensional content, applicability conditions, scope
    
- but any truth-apt content migrates to CLAIM
    

This division is unstable because intensional articulation typically appears through truth-apt formulation. A concept without such content becomes a thin label node. A concept with such content becomes claim-like.

### Defensible separation?

Only under a thin conception:

- CONCEPT as semantic anchor or typed term
    
- CLAIM as all explicit content about that term
    

### Recommendation

**Refine, not merge completely**, unless the system is willing to treat concepts as non-epistemic registry entities.  
If retained, redefine CONCEPT minimally:

- identifier
    
- lexical forms
    
- referential target
    
- links to definitional claims
    
- maybe family resemblance to other concepts
    

Do not place applicability conditions intrinsically inside CONCEPT.

---

## 2. CLAIM vs MODEL

### Locus of overlap

A richly structured theory description can look like a claim-complex; a model can be described propositionally.

### Why unstable

A mathematical structure may be encoded as:

- an object with variables, constraints, equations
    
- or a set of claims describing those equations and relations
    

### Defensible separation?

Yes, but only if the criterion is not syntax but **epistemic use**.

A MODEL is the object on which operations are performed:

- solve
    
- simulate
    
- instantiate
    
- compare
    
- perturb
    
- fit
    

A CLAIM is an assertion that something is the case, including claims about models.

### Recommendation

**Retain both**, but define MODEL functionally:

> a manipulable representational structure used as an inferential object

Without that operational criterion, the distinction collapses.

---

## 3. ARGUMENT vs MODEL

### Locus of overlap

Mechanistic explanation often appears as both:

- a causal model of how a system works
    
- an explanatory argument from model structure to explanandum
    

### Why unstable

The same content may be represented either as:

- model components and their productive organization
    
- or a sequence of premises yielding the explanatory conclusion
    

### Defensible separation?

Yes, if the distinction is:

- **MODEL** = representational structure of the system
    
- **ARGUMENT** = inferential move using that structure to support a claim
    

The instability arises when explanation is treated as a model alone or as an argument alone. In practice, explanatory episodes involve both.

### Recommendation

**Retain both**, but prohibit explanatory ARGUMENT from containing internal mechanism structure that belongs in MODEL. The model represents; the argument licenses the explanatory conclusion from it.

---

## 4. ARGUMENT vs METHOD

### Locus of overlap

Both contain rules, step structure, admissible moves, and sometimes warrants.

### Why unstable

A proof method, diagnostic heuristic, or abduction procedure may look like:

- a method for generating conclusions
    
- or an argument schema
    

For example, inference to best explanation can be:

- a warrant type in ARGUMENT
    
- or a method for theory choice
    

### Defensible separation?

Only partially. The cleanest distinction is:

- **ARGUMENT** = token or type of support relation from premises to conclusion
    
- **METHOD** = procedure for constructing, selecting, or evaluating arguments, models, or claims
    

But the current METHOD definition includes “transformation of epistemic objects,” which overlaps heavily with inferential activity.

### Recommendation

This boundary is weak.  
Either:

- **collapse METHOD**, or
    
- drastically restrict METHOD to inquiry procedures external to inferential support itself
    

As written, overlap is too high.

---

## 5. QUESTION vs METHOD

### Locus of overlap

Question decomposition and investigative procedure are tightly coupled.

### Why unstable

A research method often is a structured way of answering a kind of question. Conversely, a decomposition tree of questions can function as a procedural roadmap.

### Defensible separation?

Yes, but only if:

- QUESTION encodes what counts as an answer and how subquestions bear on it
    
- METHOD encodes how an agent should proceed operationally to obtain such answers
    

The distinction is teleological versus procedural.

### Recommendation

Retain the distinction only if METHOD is restricted to operational procedure. Otherwise QUESTION and METHOD partially absorb each other.

---

## 6. CLAIM vs METHOD

### Locus of overlap

Norms, rules, and procedures can be stated propositionally.

### Why unstable

“Use cross-validation before model comparison” is both:

- a prescriptive claim
    
- and a method fragment
    

### Defensible separation?

Only if METHOD is treated as an executable or operational schema, not as a proposition about what should be done.

### Recommendation

Current separation is weak.  
The system needs a decision:

- either procedures are first-class operational objects, then METHOD survives
    
- or procedures are represented descriptively and normatively, then METHOD collapses into CLAIM + MODEL
    

---

## IV. Global optimality

## Main verdict

The six-type ontology is **not globally optimal** under the stated minimization criterion.

It is good, but not minimal. It preserves at least one primitive that is weaker than a plausible missing one. The strongest improvement is to remove **METHOD** and possibly thin or demote **CONCEPT**.

---

## Better alternatives

## Option A: Five-type ontology

1. **CONCEPT**
    
2. **CLAIM**
    
3. **QUESTION**
    
4. **MODEL**
    
5. **ARGUMENT**
    

with:

- METHOD collapsed into MODEL + CLAIM
    
- normative and procedural content represented by claims about transformations and process models
    

### Why superior

This ontology removes the weakest primitive while preserving most expressive coverage.

### Cost

Procedural knowledge becomes less native. Some operational workflows will require richer schemas on MODEL and CLAIM.

### Assessment

This is a credible improvement if the framework is primarily for **reasoning representation**, not executable research orchestration.

---

## Option B: Five-type ontology, stronger and cleaner

1. **CLAIM**
    
2. **QUESTION**
    
3. **MODEL**
    
4. **ARGUMENT**
    
5. **EVIDENCE**
    

with CONCEPT demoted to semantic infrastructure rather than primitive epistemic object type.

### Why this is stronger

This alternative does two things:

- removes the weak and unstable primitive **METHOD**
    
- introduces the more substantively irreducible primitive **EVIDENCE**
    

It also treats concepts as semantic handles rather than epistemic objects proper.

### Superiority argument

If the target domain includes philosophy of science and theoretical research broadly, the distinction between:

- propositions,
    
- questions,
    
- inferential structures,
    
- models,
    
- evidential records
    

is cleaner and more operationally robust than the current inclusion of METHOD.

### Cost

This requires accepting that conceptual content is mostly carried by claims and that concept nodes are infrastructural rather than epistemic primitives.

### Assessment

This is, under adversarial standards, the strongest candidate.

---

## Option C: Four-type compressed ontology

1. **CLAIM**
    
2. **QUESTION**
    
3. **MODEL**
    
4. **OBJECTIFIED RELATION**
    

where ARGUMENT becomes a subtype of structured relation, and concepts are semantic infrastructure.

This is ontologically elegant, but likely too austere for the intended framework because ARGUMENT would lose first-class visibility unless reified anyway. In practice, it would reintroduce ARGUMENT under another name.

### Assessment

Theoretically elegant, but architecturally less useful.

---

## Recommended adversarial conclusion

The most defensible judgment is the following:

### 1. The ontology is not yet minimal

Because **METHOD** is not shown to be irreducible, and **CONCEPT** is over-thickened.

### 2. The ontology may not be fully sufficient

Because **EVIDENCE / RECORD** is a stronger missing candidate than METHOD is a justified retained primitive.

### 3. The strongest stable core is

- CLAIM
    
- QUESTION
    
- MODEL
    

### 4. The next most defensible layer is

- ARGUMENT as a reified inferential structure
    

### 5. The least stable elements are

- CONCEPT in its current thick formulation
    
- METHOD as a primitive
    

---

## Final recommendation

Under the stated criteria, the best current revision is:

## Revised ontology

1. **CLAIM**
    
2. **QUESTION**
    
3. **MODEL**
    
4. **ARGUMENT**
    
5. **EVIDENCE**
    

with:

- **CONCEPT** reduced to semantic infrastructure or a very thin auxiliary node type, not a full epistemic primitive
    
- **METHOD** collapsed into structured MODELs of procedure plus CLAIMs of admissibility, normativity, and stopping criteria
    

---

## Structural comparison

|Criterion|Six-type proposal|Revised five-type proposal|
|---|--:|--:|
|Primitive count|6|5|
|Boundary stability|Moderate|Higher|
|Coverage of formal reasoning|Strong|Strong|
|Coverage of inquiry decomposition|Strong|Strong|
|Coverage of modeling|Strong|Strong|
|Coverage of evidential practice|Weak|Stronger|
|Risk of type inflation|Higher|Lower|
|Weakest primitive present|METHOD|none of comparable weakness|

---

## Bottom-line judgment

The proposal is **high quality but not optimal**. It over-retains **METHOD**, over-thickens **CONCEPT**, and likely under-recognizes **EVIDENCE**. The best adversarial compression is therefore not merely to shrink, but to **replace a weak primitive by a stronger missing one**.

That is the principal failure mode of the current ontology: not excess size alone, but **misallocated primitiveness**.
