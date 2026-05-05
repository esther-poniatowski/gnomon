# Ontological Design for an Epistemic Object Framework - C2

## Primitive Types

| Type         | Role                                                                                                                                                                                                                                                                         | Status vs. Proposal       |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- |
| **CONCEPT**  | Non-truth-apt semantic circumscription                                                                                                                                                                                                                                       | Retained unchanged        |
| **CLAIM**    | Truth-apt propositional content; absorbs EXAMPLE, definitional content, analogical structural correspondences                                                                                                                                                                | Expanded scope            |
| **ARGUMENT** | Structured inference with typed warrant; absorbs analogical inference                                                                                                                                                                                                        | Expanded warrant taxonomy |
| **QUESTION** | Erotetic gap with answer-type constraints and decomposition structure                                                                                                                                                                                                        | Retained unchanged        |
| **MODEL**    | Structured abstract representation specifying a domain's variables, parameters, constraints, and structural relations, enabling analysis, prediction, or simulation. Subtypes (handled via attributes): causal-mechanistic, mathematical-formal, computational, statistical. | New — replaces MECHANISM  |
| **METHOD**   | Procedural-prescriptive schema governing epistemic operations                                                                                                                                                                                                                | New                       |

## Derived or Marginal Types

| Type                                   | Obtained as                                                                                                                                                                                                                                                 |
| -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MECHANISM                              | Specific kind of productive-causal MODEL<br>ARGUMENT (explanatory warrant) + MODEL (causal)                                                                                                                                                                 |
| DERIVATION (formal)                    | ARGUMENT (deductive warrant)                                                                                                                                                                                                                                |
| ANALOGY                                | ARGUMENT (analogical warrant) + CLAIM (structural mapping)                                                                                                                                                                                                  |
| COMPARISON                             | CLAIM (comparative subtype) + ARGUMENT                                                                                                                                                                                                                      |
| DISTINCTION (conceptual clarification) | CONCEPT + CLAIM (definitional)                                                                                                                                                                                                                              |
| TAXONOMY / CLASSIFICATION              | Taxonomic structures (phylogenies, type hierarchies, formal ontologies)  <br>Structured CLAIM-graphs (hierarchical inclusion claims) + CONCEPTs at each node, or classificatory MODEL                                                                       |
| EXAMPLE                                | CLAIM (instantiating/boundary-probing role) + ARGUMENT                                                                                                                                                                                                      |
| INTERPRETATION (semantic grounding)    | CONCEPT + CLAIM (instantiating, via former EXAMPLE role)                                                                                                                                                                                                    |
| Question decomposition                 | QUESTION + QUESTION (erotetic subordination)                                                                                                                                                                                                                |
| NORM                                   | Methodological norms ("prefer parsimonious explanations," "require reproducibility") and evaluative criteria, prescriptive norms.<br>CLAIM attribute (epistemic-status: normative, prescriptive, evaluative) combined with a METHOD (that applies the norm) |
| PROCEDURE / HEURISTIC                  | METHOD + QUESTION                                                                                                                                                                                                                                           |

## Boundaries

### Concept vs. Claim

**For collapse**: 
- A CONCEPT can be viewed as a labeled cluster of definitional CLAIMs. The intensional content of a CONCEPT and the content of its definitional CLAIM overlap maximally.
- Some CONCEPTs are _implicitly defined_ by the structure of a theory (Hilbert's implicit definitions, Carnap's Ramsey-sentences). Here the CONCEPT's content is entirely constituted by the CLAIM-structure of the theory. The CONCEPT type cannot maintain strict independence from CLAIMs in these cases.

**Against collapse**:
- CLAIMs are formulated _in terms of_ CONCEPTs. The intensional content of a CONCEPT is the semantic precondition for the truth-aptness of any CLAIM that deploys it. 
- Collapsing CONCEPT into CLAIM produces circular grounding: a definitional CLAIM already presupposes CONCEPTs. 
- The CONCEPT type is the non-propositional referential bedrock of the system. Without it, the ontology loses the ability to represent semantic circumscription independently of propositional commitment.

**Design improvement**: 
- The _definition_ relation (CLAIM → CONCEPT) must be made explicit in the schema, or definitions will be confused with arbitrary propositional CLAIMs about the concept's extension.
- The boundary is defensible if and only if the distinction between _semantic circumscription_ (CONCEPT) and _propositional commitment_ (CLAIM) is maintained strictly. The CONCEPT type must be understood as specifying applicability conditions and intensional role _without asserting truth_. Any truth-apt content — including definitions — migrates to CLAIM. This requires that CONCEPTs carry no internal propositional assertions, only intensional schema. 

### Argument vs. Claim

**For collapse**: An ARGUMENT can be viewed as a set of CLAIMs with a labeled support relation. If the dependency graph of CLAIMs can carry typed edges (deductive-entailment, abductive-support, inductive-generalization), then a dedicated ARGUMENT type is redundant.

**Against collapse**: An ARGUMENT must carry a *warrant* as a distinct component, not collapsible into the CLAIM set. The _warrant_ is the inferential license (rule, schema, or principle) that _justifies_ the transition from premises ${P_1, \ldots, P_n}$ to conclusion $C$. This warrant is not itself a CLAIM in the ordinary sense; it is a _rule of inference_ (Toulmin's sense).  

**Design improvement**: The ARGUMENT schema must distinguish: 
- premise CLAIMs
- conclusion CLAIM
- warrant type (deductive, abductive, inductive, analogical, transcendental)
- backing (the epistemic authority for the warrant)
Collapsing these into a CLAIM-graph without preserving $(iii)$ and $(iv)$ distorts inferential structure.

### Question vs. Claim

- A QUESTION is not truth-apt; it has answer conditions, not truth conditions. 
- A QUESTION carries presuppositional structure (the background CLAIMs that must hold for the question to be well-formed) that is not encoded in a negative CLAIM. 
- A QUESTION carry answer-type constraints — whether the expected answer is a CONCEPT, a CLAIM, a MECHANISM, a value, etc. — which constitutes a form of intentional structure absent from CLAIMs.
- Erotetic decomposition (the relation between a QUESTION and its sub-QUESTIONs) is a structural operation with no analogue in CLAIM-to-CLAIM relations.

### Question vs. Method

**For collapse**: Research METHODs are often formulated as responses to QUESTIONs, and complex QUESTIONs carry decomposition structure that resembles a METHOD (a sequence of sub-QUESTIONs to answer in order). A methodological heuristic like "to answer Q, first answer $Q_1$, then $Q_2$" lies at the intersection.

**Against collapse**: A QUESTION specifies _what_ is epistemically open; a METHOD specifies _how_ to proceed. The decomposition structure of a QUESTION (its erotetic subordination graph) is a _structural property of the question's content_, not a prescriptive procedure. A METHOD is prescriptive and domain-general; a QUESTION is content-specific and answer-directed.

### Mechanism vs. Claim

**For collapse**: A MECHANISM can be viewed as a _structured CLAIM-complex_ about causal-productive organization. It specifies entities ${e_i}$, their properties ${p_j}$, the activities ${a_k}$ they engage in, and the productive organization $O$ relating them. All of this is propositionally expressible:
- "$e_i$ has property $p_j$" — CLAIM
- "$e_i$ engages in activity $a_k$ under condition $c$" — CLAIM
- "$O$ produces phenomenon $\phi$ from ${e_i, a_k}$" — CLAIM
What distinguishes it from an arbitrary CLAIM-cluster is its _compositional schema_ — but this schema can be encoded as a CLAIM-cluster template governed by a METHOD (the method of mechanistic explanation).

**Against collapse**: 
- Mechanisms are _models_ of productive continuity (Machamer, Darden, and Craver) — they represent _how_ a process unfolds at a given level of organization, including levels of analysis, emergent regularities, and inter-level causation. This is qualitatively different from a CLAIM _about_ a mechanism.
- A CLAIM is a propositional snapshot.
- A MECHANISM is a dynamic generative structure, it can be _instantiated_, _parameterized_, _simulated_, and _decomposed_.

### Model vs. Argument vs. Claim

**For collapse**:  An ARGUMENT with explanatory warrant (abductive or causal) and a MECHANISM are nearly coextensive in practice. A mechanistic explanation appears as: premise CLAIMs specifying the mechanism's components → conclusion CLAIM asserting the explanandum.

**Against collapse**: 
- MODELs are _structures_ that generate CLAIMs and ARGUMENTs, and are subject to evaluation by METHODs. 
- It is not a CLAIM (though it entails CLAIMs):
	- MODEL is not a propositional assertion about a structure — it _is_ the structure, understood as an abstract object that can be instantiated, parameterized, compared, and analyzed independently of any particular truth claim about it. 
	- In the sense of model theory, a MODEL is an _interpretation_ — a structured entity that CLAIMs are evaluated _against_, not a CLAIM itself. 
	- This provides the irreducibility criterion: a MODEL is the semantic evaluator of CLAIMs, which cannot coherently be a CLAIM without self-referential collapse.
- It is not an ARGUMENT (though it generates them):
	- An ARGUMENT is an _inferential schema_ — it licenses a conclusion given premises. ARGUMENTs _use_ MODELs as premises.
	- A MODEL is an _abstract structure_ — it specifies a domain's productive organization independently of any particular inferential move. 
	- The same MODEL can ground multiple ARGUMENTs (explanation, prediction, intervention analysis). Conversely, an ARGUMENT can reference a MODEL without fully specifying it.
- Consider: a Bayesian network, a dynamical system $\dot{x} = f(x, u)$, a formal grammar, a utility function in decision theory, the Standard Model in physics. None of these are naturally represented as CLAIMs or ARGUMENTs without severe distortion.

### Analogy vs. Argument

**For collapse**: ANALOGY is fully encodable as CLAIM + ARGUMENT without structural loss. ANALOGY = {structural-correspondence CLAIM} + {analogical ARGUMENT using it}.
- Structural correspondence → CLAIM (type attribute: structural-mapping). An ANALOGY consists of: source domain $\mathcal{S}$, target domain $\mathcal{T}$, structural mapping $\mu: \mathcal{S} \to \mathcal{T}$, scope $\sigma$, and breakdown conditions $\delta$. Each component is propositionally representable:
	- "Element $s_i \in \mathcal{S}$ corresponds to $t_i \in \mathcal{T}$ under relation $R$" — CLAIM
	- "The mapping fails under condition $\delta$" — CLAIM
- Analogical inference → ARGUMENT (warrant: analogical, citing the structural-correspondence CLAIM). The inferential use of an analogy is an ARGUMENT with _analogical warrant_: $\mathcal{S}$ and $\mathcal{T}$ share structure $\mu$; $P$ holds in $\mathcal{S}$; therefore $P'$ (the $\mu$-image of $P$) plausibly holds in $\mathcal{T}$.
- The structural-correspondence CLAIM persists as a reusable object; different ARGUMENTs can invoke it.

**Against collaspe**: The analogical argument uses a structural mapping as its warrant. If ANALOGY is retained, an analogical ARGUMENT would reference an ANALOGY object — creating a layered structure (ARGUMENT referencing an ANALOGY referencing CLAIMs) but it introduces a redundant level of indirection.

**Design improvement**: If the ontology intends ANALOGIEs to function as _persistent reusable mapping objects_ (i.e., not consumed by a single ARGUMENT but referenced across multiple inferential moves), then representing them as CLAIMs preserves this reusability exactly as well as a dedicated type — a CLAIM is already a persistent, cross-referenceable object. No structural loss occurs.

### Example vs. Claim

**For collapse**: An EXAMPLE can be viewed as a CLAIM  with a role attribute, either:
- instantiating (positive instantiation): "x is an instance of C"
- boundary-probing: "x is a marginal case of C"
- counterexample / refuting: "x refutes CLAIM P"
- illustrative
Each is truth-apt and expressible as a CLAIM with a role attribute.
The _concreteness_ of an example is a feature of its CLAIM's subject matter, not an independent epistemic type.

**Against collapse**: Pedagogically or rhetorically, EXAMPLEs serve a _grounding function_ in exposition. 

### Method vs. Claim

**For collapse**: A METHOD can be viewed as a structured CLAIM about a procedure. Example: "To achieve X, perform steps ${s_1, \ldots, s_n}$ checking condition $c_k$ at each stage" is expressible as a CLAIM.

**Against collapse**:
- The distinction between procedural knowledge (knowing-how) and propositional knowledge (knowing-that) is foundational in epistemology and supports type irreducibility here.
	- A METHOD is prescriptive/normative: it has the form of a _schema of operations_ that specifies _admissible transformations_, _stopping criteria_, _decision points_, and _expected outputs_.
	- A CLAIM is descriptive: it has the form of a proposition. It can describe the method, but is not the method itself.
- METHODs serve as the _operators_ of the reasoning system: they specify how to generate, evaluate, and transform other epistemic objects. This meta-level function distinguishes them from CLAIMs.


