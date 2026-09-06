---
tags:
  - backup
index: "[Object-kind candidates](_index.md)"
aliases:
  - Object boundary comparisons
---
# Comparisons and boundary analysis

> [!NOTE] These comparisons state boundaries between objects only.

Each section uses the same comparative structure:

- **Contrast dimensions.** Axes along which the objects differ.
- **Interaction pattern.** How the objects relate in a graph.
- **Overlap region.** Where usage blurs the boundary.
- **Boundary criterion.** The test that separates the objects.

Encoding choices and tradeoffs belong in the `## Encoding options` sections for each object.

### CONCEPT vs. CLAIM

**Contrast dimensions.**

- **Semantic status.** `CONCEPT` anchors meaning without asserting truth; `CLAIM` asserts propositional content.
- **Graph role.** `CONCEPT` supplies terms, referents, and semantic identity; `CLAIM` asserts, defines, excludes, or commits.
- **Use pattern.** A `CLAIM` can mention a `CONCEPT` as the target of a definition (e.g., "compactness means finite subcover property"), or use it inside another assertion (e.g., "compactness implies boundedness").
- **Revision target.** Revising a concept changes meaning or boundaries; revising a claim changes what the system treats as true, justified, or live.

**Interaction pattern.**

- Definitional `CLAIM`s circumscribe `CONCEPT`s.
- Ordinary `CLAIM`s use `CONCEPT`s as constituents.

**Overlap region.**

- Statement-like properties of a `CONCEPT` often fix concept use while also taking truth conditions. These include definitions, applicability conditions, scope statements, and inferential roles (e.g., "a prime number has exactly two positive divisors").
- Implicit definitions make concepts look fixed by a theory's claim structure (cf. Hilbert-style and Carnap-style theories).
- Holism denies that a finite set of definitional claims exhausts a theoretical concept (cf. Quine and Putnam).

**Boundary criterion.**

- Content belongs to `CONCEPT` when it anchors meaning without asserting truth.
- Content belongs to `CLAIM` when it asserts, denies, defines, or evaluates.

### QUESTION vs. CLAIM

**Contrast dimensions.**

- **Logical status.** `QUESTION` has answer conditions; `CLAIM` has truth conditions.
- **Inquiry direction.** `QUESTION` opens a search space; `CLAIM` closes or proposes a commitment.
- **Dependency form.** A subquestion graph tracks what contributes to an answer; a claim graph tracks support, implication, presupposition, or defeat.

**Interaction pattern.**

- `QUESTION`s license candidate answer `CLAIM`s and presuppose background `CLAIM`s.

**Overlap region.**

- A claim about ignorance (e.g., "whether P remains unknown") reports an epistemic state, but it does not specify admissible answers.
- Erotetic logic emphasizes partitions of possible answers (e.g., "yes", "no", or a parameter range), but research questions also carry presuppositions, partial answers, relevance constraints, and subquestion structure.

**Boundary criterion.**

- Content belongs to `QUESTION` when it controls answer conditions, subquestions, or admissible response type.
- Content belongs to `CLAIM` when it asserts a proposition that can be supported, denied, or used as an answer.

### QUESTION vs. PROBLEM

**Contrast dimensions.**

- **Inquiry mode.** `QUESTION` asks for an answer; `PROBLEM` asks for a construction, proof, resolution, or constraint satisfaction.
- **Closure condition.** `QUESTION` closes through an answer; `PROBLEM` closes through success conditions.
- **Practical force.** `QUESTION` organizes inquiry; `PROBLEM` adds a task commitment.

**Interaction pattern.**

- `PROBLEM` behaves like a constrained `QUESTION` whose resolution may require a `METHOD`, proof, artifact, or construction (e.g., "construct a counterexample").

**Overlap region.**

- Constructive questions and constrained problems share subquestions, presuppositions, candidate answers, and closure structure.

**Boundary criterion.**

- Content belongs to `QUESTION` when an answer is the main closure condition.
- Content belongs to `PROBLEM` when the object adds success criteria, constraints, or required production.

### ARGUMENT vs. CLAIM

**Contrast dimensions.**

- **Unit of content.** `CLAIM` is propositional content; `ARGUMENT` gives reasons.
- **Internal relation.** `CLAIM` has truth conditions, modality, and status; `ARGUMENT` has premises, conclusion, warrant, backing, and defeaters.
- **Assessment target.** Claims are checked for truth, warrant, status, or acceptance; arguments are checked for support, validity, warrant strength, and defeat.

**Interaction pattern.**

- `ARGUMENT`s connect premise `CLAIM`s to a conclusion `CLAIM`.
- The same `CLAIM` can serve as premise, conclusion, backing, assumption, or defeater in different arguments while retaining its own epistemic status.

**Overlap region.**

- A warrant may be expressed as a claim (e.g., "modus ponens preserves truth"), but in an argument it licenses the move from premises to conclusion.
- Toulmin-style warrant and backing separate a proposition used in reasoning from the inferential license that organizes the reasoning.
- Warrant families differ in evaluation criteria: validity for deduction, best explanation for abduction, mapping depth for analogy, and defeat for dialectic.

**Boundary criterion.**

- Content belongs to `CLAIM` when it states what is asserted.
- Content belongs to `ARGUMENT` when it states why a conclusion follows from, or is supported by, premises.

### MODEL vs. ARGUMENT

**Contrast dimensions.**

- **Object function.** `MODEL` represents structure; `ARGUMENT` supports a conclusion.
- **Reuse pattern.** One `MODEL` can ground many arguments; one `ARGUMENT` can cite a model without containing its structure.
- **Operation type.** Models are solved, simulated, instantiated, compared, perturbed, or fitted; arguments are reconstructed, evaluated, attacked, or strengthened.

**Interaction pattern.**

- `ARGUMENT`s cite `MODEL`s as premises, warrants, backing, or sources of derived claims.

**Overlap region.**

- Causal models can resemble arguments because they support claims, but they primarily represent dependency structure (e.g., a graph with arrows among variables).
- Pearl-style causal graphs encode several dependency forms (e.g., conditional independences, interventions, and structural equations) that generate many possible arguments.

**Boundary criterion.**

- Content belongs to `MODEL` when it represents a structure on which operations act.
- Content belongs to `ARGUMENT` when it uses premises and warrant to support a conclusion.

### MODEL vs. CLAIM

**Contrast dimensions.**

- **Semantic role.** `MODEL` supplies the structure against which claims are checked; `CLAIM` states content in or about a structure.
- **Ontological form.** `MODEL` can be an interpretation, system, or surrogate; `CLAIM` is a proposition.
- **Operation target.** Model operations act on the structure; claim operations act on support, truth, status, or revision.

**Interaction pattern.**

- `CLAIM` clusters can characterize `MODEL`s.
- `MODEL`s can make `CLAIM`s true, false, applicable, or derivable.
- `MODEL`s organize `CONCEPT`s and generate or support `CLAIM`s.

**Overlap region.**

- Formal axiomatic theories blur the boundary: axioms and theorems are claims, while satisfying structures are models (e.g., models of ZFC, groups satisfying group axioms).
- Tarskian model theory separates the proposition from the interpretation that satisfies it.
- A theory description can look like a set of claims over concepts while functioning as a representational structure.

**Boundary criterion.**

- Content belongs to `CLAIM` when it asserts an axiom, theorem, constraint, or description.
- Content belongs to `MODEL` when it is the satisfying or manipulable structure.

### MECHANISM vs. ARGUMENT vs. CLAIM

**Contrast dimensions.**

- **Productive structure.** `MECHANISM` represents organized production; `ARGUMENT` supplies support; `CLAIM` describes or commits.
- **Component role.** Mechanisms contain entities, activities, organization, levels, and conditions; arguments contain premises, conclusion, warrant, and backing; claims contain propositions.
- **Assessment target.** Mechanisms are checked for adequacy, organization, and explanatory fit; arguments for support; claims for truth or status.

**Interaction pattern.**

- `CLAIM`s describe mechanism components.
- `MECHANISM`s represent the organization of those components.
- `ARGUMENT`s support claims about mechanism adequacy or existence.

**Overlap region.**

- Mechanism narratives often combine three contents in one prose passage: component descriptions (e.g., "protein X binds receptor Y"), process representation (e.g., "binding triggers cascade Z"), and explanatory argument (e.g., "therefore the phenotype arises").
- Machamer-Darden-Craver mechanisms sharpen the contrast by centering productive organization.

**Boundary criterion.**

- Content belongs to `MECHANISM` when organized productive structure is the object.
- Content belongs to `ARGUMENT` when support for a conclusion is the object.
- Content belongs to `CLAIM` when a component fact, existence claim, or adequacy judgment is asserted.

### EXPLANATION vs. ARGUMENT

**Contrast dimensions.**

- **Relation type.** `EXPLANATION` relates explanans to explanandum; `ARGUMENT` relates premises to conclusion.
- **Asymmetry type.** Explanation tracks relevance; argument tracks support.
- **Question answered.** Explanation answers why or how; argument answers why a conclusion is acceptable.

**Interaction pattern.**

- Explanatory `ARGUMENT`s can support an explanandum `CLAIM`.
- `EXPLANATION`s relate explanans material to what is explained.

**Overlap region.**

- The same propositions can appear in both explanatory and argumentative relations (e.g., flagpole height and shadow length).
- The flagpole problem shows that logical support and explanation can diverge in direction and relevance (cf. Bromberger and Hempel-Oppenheim).
- Explanations differ by relation type: mechanistic (e.g., "how the pump works"), causal (e.g., "what caused the event"), teleological (e.g., "what goal it serves"), contrastive (e.g., "why P rather than Q"), functional (e.g., "what role it plays"), or unificationist (e.g., "which law unifies the cases").

**Boundary criterion.**

- Content belongs to `EXPLANATION` when the central relation is explanatory relevance between explanans and explanandum.
- Content belongs to `ARGUMENT` when the central relation is support from premises to conclusion.

### INTERPRETATION vs. CLAIM vs. ANALOGY

**Contrast dimensions.**

- **Semantic map.** `INTERPRETATION` maps a symbol, concept, formal object, or model to semantic values.
- **Assertion.** `CLAIM` asserts that a mapping holds, fits, fails, or has consequences.
- **Cross-domain map.** `ANALOGY` maps structure across domains to support transfer or comparison.

**Interaction pattern.**

- `CLAIM`s can evaluate `INTERPRETATION`s or `ANALOGY`s.
- `ANALOGY`s can relate interpreted structures across domains.

**Overlap region.**

- Interpretation sits near three neighboring activities: semantic grounding resembles concept work (e.g., "what does mass mean here?"), mapping assertions resemble claim work (e.g., "R denotes resistance"), and correspondence across domains resembles analogy (e.g., "current corresponds to water flow").
- A broad notion of interpretation becomes unstable unless the object is restricted to a semantic map or model assignment (e.g., symbols to physical quantities).

**Boundary criterion.**

- Content belongs to `INTERPRETATION` when it assigns semantic values.
- Content belongs to `CLAIM` when it asserts or evaluates an assignment.
- Content belongs to `ANALOGY` when it maps structure across domains.

### ANALOGY vs. ARGUMENT

**Contrast dimensions.**

- **Mapping vs. use.** `ANALOGY` stores structural correspondence; `ARGUMENT` uses that correspondence to support a conclusion.
- **Reusability.** One analogy can support several arguments; one argument can cite several analogies.
- **Assessment axis.** Analogy is checked for structural depth, scope, relevance, disanalogy, and breakdown; argument is checked for inferential support.

**Interaction pattern.**

- Analogical `ARGUMENT`s cite `ANALOGY`s as warrant, backing, or structured premise.

**Overlap region.**

- Analogical reasoning often merges the mapping and the inference that uses it (e.g., "atoms are like solar systems, so electrons orbit like planets").

**Boundary criterion.**

- Content belongs to `ANALOGY` when it states what corresponds to what under structural preservation and breakdown conditions.
- Content belongs to `ARGUMENT` when it states how that correspondence supports a conclusion.

### DISTINCTION vs. CONCEPT

**Contrast dimensions.**

- **Unit of meaning.** `CONCEPT` is a semantic object; `DISTINCTION` contrasts semantic or propositional objects.
- **Arity.** A concept can stand alone; a distinction requires at least two targets.
- **Graph function.** Concepts support reference and classification; distinctions mark lack of equivalence, contrast basis, or conflation risk.

**Interaction pattern.**

- `DISTINCTION`s or distinction edges relate `CONCEPT`s and can cite `CLAIM`s, `EXAMPLE`s, or `OBJECTION`s.

**Overlap region.**

- Some distinctions merely sharpen concept boundaries (e.g., "selection vs. gain"), while others become durable contrast analyses with debate history.

**Boundary criterion.**

- Content belongs to `CONCEPT` when a single semantic object is being anchored.
- Content belongs to `DISTINCTION` when contrast, lack of equivalence, or conflation risk is the object.

### METHOD vs. QUESTION

**Contrast dimensions.**

- **Target vs. procedure.** `QUESTION` specifies what counts as an answer; `METHOD` specifies how to proceed.
- **Part-whole form.** A subquestion graph tracks answer dependency; method steps track operational order.
- **Applicability.** Questions depend on their content; methods can be reused across targets.

**Interaction pattern.**

- `METHOD`s can be selected to answer `QUESTION`s.
- A subquestion graph can guide method choice.

**Overlap region.**

- Research protocols often present a sequence of subquestions as if it were a procedure (e.g., "estimate data quality, then fit the model").
- A method can be described as a way of answering a question.

**Boundary criterion.**

- Content belongs to `QUESTION` when it defines the epistemic gap and answer condition.
- Content belongs to `METHOD` when it defines the procedure for obtaining, testing, or selecting answers.

### METHOD vs. CLAIM

**Contrast dimensions.**

- **Knowledge form.** `METHOD` expresses procedural knowledge; `CLAIM` expresses propositional knowledge.
- **Assessment.** Methods are checked for applicability, effectiveness, admissibility, or efficiency; claims are checked for truth, warrant, or status.
- **Execution.** Methods are applied or performed; claims are asserted, supported, challenged, or revised.

**Interaction pattern.**

- Prescriptive `CLAIM`s can describe, justify, or evaluate `METHOD`s.

**Overlap region.**

- Claims about action or procedure can resemble method fragments (e.g., "use cross-validation before model comparison").
- A procedure stated in prose can look like a claim about what to do.

**Boundary criterion.**

- Content belongs to `METHOD` when operational structure is central.
- Content belongs to `CLAIM` when the content is a contestable proposition about procedure, admissibility, or preference.

### METHOD vs. ARGUMENT

**Contrast dimensions.**

- **Procedure vs. instance.** `METHOD` is a reusable procedure; `ARGUMENT` is a support move in a specific context.
- **Function.** Methods construct, select, or evaluate objects; arguments support conclusions.
- **Warrant link.** An argument can instantiate a method, and a method can define a warrant pattern.

**Interaction pattern.**

- `ARGUMENT`s can instantiate `METHOD`s, especially in proof and inference contexts.

**Overlap region.**

- Proof strategies and inference procedures can function as methods or as argument warrants (e.g., proof by contradiction, induction).
- Inference to the best explanation, proof by contradiction, proof by induction, and reflective equilibrium sit near this boundary.

**Boundary criterion.**

- Content belongs to `METHOD` when the reusable procedure is the object.
- Content belongs to `ARGUMENT` when support from premises to conclusion is the object.

### METHOD vs. FRAMEWORK

**Contrast dimensions.**

- **Scope.** `METHOD` governs local operations or reusable procedures; `FRAMEWORK` governs a whole reasoning space.
- **Composition.** Frameworks can include methods, norms, commitments, concepts, and model preferences; methods do not include the whole background.
- **Permission level.** Methods specify moves; frameworks specify which moves count as admissible.

**Interaction pattern.**

- `FRAMEWORK`s endorse, constrain, or rank `METHOD`s.

**Overlap region.**

- Procedure families differ in scope and status: formal inference rules (e.g., modus ponens), proof strategies (e.g., induction), scientific methods (e.g., randomized trial), research heuristics (e.g., decompose and recombine), and computational procedures (e.g., dynamic programming).
- A method can function as a background standard across an inquiry (e.g., "always compare models by held-out error").

**Boundary criterion.**

- Content belongs to `METHOD` when a local or reusable procedure is the object.
- Content belongs to `FRAMEWORK` when a background system that governs admissible moves is the object.

### FRAMEWORK vs. MODEL

**Contrast dimensions.**

- **Global frame vs. representation.** `FRAMEWORK` conditions a reasoning space; `MODEL` represents a domain structure.
- **Component relation.** A framework can contain model preferences and standards; a model does not contain the whole background that governs admissible moves.
- **Revision pattern.** Revising a model changes a representation; revising a framework changes what counts as admissible or salient.

**Interaction pattern.**

- `FRAMEWORK`s condition how `MODEL`s are built, accepted, compared, or interpreted.

**Overlap region.**

- Frameworks often fuse several components: commitments, norms, exemplars, methods, and model preferences (e.g., hard core, accepted standards, canonical cases, favored methods).
- Philosophical accounts emphasize different internal structures: Quinean holism (e.g., web of belief), Kuhnian paradigms (e.g., exemplars), Lakatosian research programmes (e.g., hard core and heuristics), Wittgensteinian hinges (e.g., fixed commitments), and logical empiricist frameworks (e.g., constitutive rules).

**Boundary criterion.**

- Content belongs to `MODEL` when it represents a domain structure.
- Content belongs to `FRAMEWORK` when it conditions the space in which models, claims, methods, and arguments count as admissible.

### FRAMEWORK vs. NORM

**Contrast dimensions.**

- **Scope.** `NORM` is a standard, criterion, rule, or principle; `FRAMEWORK` is an integrated background.
- **Dependency.** A framework can contain norms; a norm does not contain the whole framework.
- **Graph role.** Norms govern acceptance, comparison, design, or assessment; frameworks coordinate norms with commitments, methods, concepts, and models.

**Interaction pattern.**

- `FRAMEWORK`s contain or endorse `NORM`s, and `NORM`s govern objects inside a framework.

**Overlap region.**

- Local norms and framework standards can look similar when the same principle applies broadly (e.g., "prefer simpler hypotheses").
- Commitments and norms can determine each other inside a framework.

**Boundary criterion.**

- Content belongs to `NORM` when a standard or criterion is the object.
- Content belongs to `FRAMEWORK` when the object is the integrated system in which standards and commitments jointly condition reasoning.

### COMPARISON vs. CLASSIFICATION

**Contrast dimensions.**

- **Arity and scope.** `COMPARISON` judges selected targets; `CLASSIFICATION` organizes a domain.
- **Output.** Comparison yields a relation or judgment; classification yields a class structure, hierarchy, typology, or partition.
- **Criterion role.** Comparison criteria structure local judgment; classification criteria structure organization of a domain.

**Interaction pattern.**

- `COMPARISON`s can motivate changes to `CLASSIFICATION`s, and `CLASSIFICATION`s can supply dimensions for comparison.

**Overlap region.**

- Taxonomic revision often starts from comparisons among selected cases (e.g., "does this case fit type A or type B?").
- Similarity, contrast, and correspondence relations may appear inside both comparison and classification work (e.g., "similar symptoms", "opposed mechanisms", "matching roles").

**Boundary criterion.**

- Content belongs to `COMPARISON` when finite targets are judged along dimensions.
- Content belongs to `CLASSIFICATION` when a domain is organized into classes under a criterion.
