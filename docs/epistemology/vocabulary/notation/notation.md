---
tags:
  - theory
index: "[Notation](docs/epistemology/vocabulary/notation/_index.md)"
aliases:
  - Notation of the theory
  - Notation
---
# Notation

> [!QUESTION] Goal: which symbol denotes which object, across the theory notes?

A single registry assigns every symbol that a note may use without defining it: the symbols of the objects of the method, and of the objects of the vocabulary that several notes share. One registered letter denotes one object, so that a formula reads the same in every note. Each row names the theory note that declares the symbol and defines its object. A specification note may use a registered symbol, and it never declares one. ^registry

## Problem and state of an inquiry

| Symbol | Denotes | Declared in |
| --- | --- | --- |
| $\pi$ | an epistemic problem, $\pi=\langle K,d,\Phi\rangle$; several problems are written $\pi_1,\pi_2,\ldots$ | [epistemic problem](../../objects/problem/epistemic-problem.md#^problem-triple) |
| $K$ | the accepted knowledge: the finite set of claims accepted by an act of the researcher, relative to which a problem is posed, a belief base not closed under consequence; a claim $s$ is accepted when $s\in K$ | [state of an inquiry](../../foundations/inquiry-and-state.md#^state) |
| $H$ | the proposed candidates: answers put forward and not yet accepted | [state of an inquiry](../../foundations/inquiry-and-state.md#^state) |
| $h$ | a candidate answer, a member of $H$ | [conditions of satisfaction](../../objects/answer/satisfaction-conditions.md#^conditions-satisfaction) |
| $\mathcal{M}$ | the available means: the methods, data, instruments and proof techniques that can be applied | [epistemic problem](../../objects/problem/epistemic-problem.md) |
| $\mathrm{Obt}_{\mathcal{M}}$ | $\mathrm{Obt}_{\mathcal{M}}(s)$: the available means $\mathcal{M}$ have yielded the claim $s$; obtaining a claim is distinct from accepting it, which is written $s\in K$ | [obtained and accepted](../../foundations/inquiry-and-state.md#^obtained-accepted) |
| $d$ | the demand of a problem, $d=\langle\mathsf{type},\mathsf{req},\Xi\rangle$, with the type of result $\mathsf{type}$ and the request $\mathsf{req}$, which is the request of its associated question | [epistemic problem](../../objects/problem/epistemic-problem.md) |
| $\Xi$ | the explicanda of a demand | [epistemic problem](../../objects/problem/epistemic-problem.md) |
| $\Phi$ | the constraints of a problem, $\Phi_1$ on each candidate and $\Phi^*$ on the set of results | [epistemic problem](../../objects/problem/epistemic-problem.md) |
| $Q_\pi$ | the question associated with the problem $\pi$: the question that asks for the demanded results, and only for them | [epistemic problem](../../objects/problem/epistemic-problem.md#^associated-question) |
| $\pi_Q$ | the minimal problem of the question $Q$, $\pi_Q=\langle K,d_Q,\Phi_Q\rangle$, whose demand $d_Q$ has the explicanda $\Xi_Q$ | [epistemic problem](../../objects/problem/epistemic-problem.md#^minimal-problem) |

## Question

| Symbol | Denotes | Declared in |
| --- | --- | --- |
| $Q$ | a question: a request whose answers form a definite set, whose possible answers are fixed by its subject $\Sigma$ and its task $T$; $Q$ is specified by $\langle\Sigma,T,\mathcal{V}\rangle$, in which the virtues $\mathcal{V}$ fix the standards of its answers, and asked under a request $\mathsf{req}$ | [answer sets of a question](../../objects/question/question.md#^answer-sets); [specification of a question](../../objects/question/question-specification.md#^three-layers) |
| $\Sigma$ | the subject of inquiry, $\Sigma=\langle S,P,X,D\rangle$ | [subject of inquiry](../../objects/subject/subject-of-inquiry.md) |
| $S$ | the target: the system, or the class of systems, that the inquiry is about; the target is relational, and a target-system record specifies it | [target system](../../objects/subject/target-system.md); [two senses of target](../../foundations/things-and-constructs.md#^target-senses) |
| $N$ | a number of units: of a kind in $S$, or of the constituents $C$ of a model | [target system](../../objects/subject/target-system.md); [mechanistic answer](../../objects/answer/mechanism.md) |
| $P$ | the phenomenon: the behavior of the target that the question concerns; it is an explanandum only when the aim is explanation | [phenomenon](../../objects/subject/phenomenon.md) |
| $f_P$ | the input–output map of a phenomenon, from a space of inputs to a space of outputs | [mechanistic answer](../../objects/answer/mechanism.md) |
| $Y$ | an observable that expresses $P$; an explanandum variable when the aim is explanation | [phenomenon](../../objects/subject/phenomenon.md) |
| $X$ | the contrast class, whose members are the foils | [contrast](../../objects/subject/contrast.md) |
| $D$ | the conditions held fixed: the restrictions that the question imposes on admitted values, which Mackie calls the causal field | [domain of conditions](../../objects/subject/domain.md) |
| $i$, $k$, $t$ | the index families of parts, of instances, and of the course, each admitting several indices | [phenomenon](../../objects/subject/phenomenon.md) |
| $T$ | the epistemic task, $T=\langle A,R,\mu,\lambda,\tau,\omega\rangle$ | [epistemic task](../../objects/task/epistemic-task.md) |
| $A$ | the epistemic aim | [epistemic aim](../../objects/task/epistemic-aim.md) |
| $R$ | the requested relation | [requested relation](../../objects/task/requested-relation.md) |
| $\mu$ | the modal strength | [modal strength](../../objects/task/modal-strength.md) |
| $\lambda$ | the bound on the explanans: a value on each of its two axes; the set of variables that it admits is a function of $\lambda$ and of the target $S$ | [admissible explanans](../../objects/task/admissible-explanans.md) |
| $\tau$ | the required accuracy: the metric and the tolerance within which a value of the answer must match the target | [epistemic task](../../objects/task/epistemic-task.md) |
| $\omega$ | the proof obligations: the statements that the answer must derive | [epistemic task](../../objects/task/epistemic-task.md) |
| $\mathcal{V}$ | the virtues weighed by a question, each marked constitutive or preferred: a constitutive virtue narrows the admissible answers, and a preferred virtue ranks them | [virtues](../../objects/task/epistemic-pragmatic-virtues.md) |

## Answer, assessment and model

| Symbol | Denotes | Declared in |
| --- | --- | --- |
| $\mathrm{Sat}$, $\mathrm{Admissible}$, $\mathrm{Warranted}$ | $\mathrm{Sat}(h\mid Q)$: the candidate $h$ satisfies the question $Q$, that is, it passes the tests of admissibility, $\mathrm{Admissible}(h\mid Q)$, and of warrant, $\mathrm{Warranted}(h\mid Q)$ | [conditions of satisfaction](../../objects/answer/satisfaction-conditions.md#^conditions-satisfaction) |
| $\mathrm{Adequate}$ | $\mathrm{Adequate}(M\mid Q,\Gamma)$: the model $M$ is adequate for the purpose that $Q$ sets, under the circumstances $\Gamma$ | [virtues](../../objects/task/epistemic-pragmatic-virtues.md) |
| $\Gamma$ | the circumstances, such as resources, use and audience, under which the adequacy of a model for a purpose is judged | [virtues](../../objects/task/epistemic-pragmatic-virtues.md) |
| $E$ | the explanans: the factors of the block of an explanation | [answer form](../../objects/answer/answer-form.md#^explanation-block) |
| $I$ | the idealizations among the grounds of an answer, each relative to the target of the answer | [answer form](../../objects/answer/answer-form.md#^idealizations) |
| $M$ | a model in the representational sense, $M=\langle C,V,L,O\rangle$, which grounds the answers whose route runs on it | [model](../representations/model.md#^model-elements) |
| $C$ | the constituents: the units that the model treats as bearers, $C=\{c_1,\ldots,c_N\}$; in a mechanistic model, the components of the mechanism | [model](../representations/model.md#^model-elements); [mechanistic answer](../../objects/answer/mechanism.md) |
| $V$ | the terms of the model: its variables and parameters | [model](../representations/model.md#^model-elements) |
| $L$ | the laws of the model; in a mechanistic model, each law represents one activity $a_j$ | [model](../representations/model.md#^model-elements); [mechanistic answer](../../objects/answer/mechanism.md) |
| $a_j$ | an activity of a mechanism, indexed by $j\in J$: an action or an interaction, which one law of $L$ represents | [mechanistic answer](../../objects/answer/mechanism.md); [mechanistic activity](../change/mechanistic-activity.md) |
| $O$ | the organization of the model: the relations among its constituents and its laws on which its behavior depends; in a mechanistic model, the relations among parts and activities | [model](../representations/model.md#^model-elements); [mechanistic answer](../../objects/answer/mechanism.md) |
| $f_j$, $J$ | the terms $f_j$ of an additive decomposition of a dynamic, indexed by $j\in J$, each a candidate activity | [criterion of an activity](../change/mechanistic-activity.md#^activity-term); [mechanistic answer](../../objects/answer/mechanism.md) |
| $\mathcal{R}$ | the realization map of a mechanism: the map from its components, activities and organization to the behavior that they produce | [mechanistic answer](../../objects/answer/mechanism.md) |
| $Z$ | the external entities of a causal-mechanistic production: entities outside the target system, whose activities precede the phenomenon | [production and constitution](../../objects/answer/mechanism.md#^production-constitution) |
| $\eta$ | the resistance hypothesis: the structural hypothesis that explains a resistance met by an inquiry, on which an abductive serving question is conditioned | [decomposition of a question](../../processes/inquiry/question-decomposition.md#^functional-types) |

## Systems, states and change

| Symbol | Denotes | Declared in |
| --- | --- | --- |
| $\sigma$ | a system, described by its composition $\mathsf{Comp}(\sigma)$, its environment $\mathsf{Env}(\sigma)$, its structure $\mathsf{Str}(\sigma)$, and in one version its mechanism $\mathsf{Mech}(\sigma)$ | [system, constituent and environment](../systems/system-constituent-environment.md) |
| $\rho$ | a relation, as the set of tuples that satisfy it | [property, attribute, predicate and relation](../systems/property-attribute-predicate.md) |
| $\mathcal{X}$ | a state space | [state and configuration](../quantities/state-and-configuration.md) |
| $x$ | a state, a point of $\mathcal{X}$ | [state and configuration](../quantities/state-and-configuration.md) |
| $x_i$, $\mathcal{X}_i$ | $x_i(t)\in\mathcal{X}_i$: the state of the component $c_i$ at the point $t$ of the course, in the state space $\mathcal{X}_i$ of that component | [mechanistic answer](../../objects/answer/mechanism.md) |
| $x_0$ | the initial state: the state at the first point of the course | [condition](../quantities/condition.md) |
| $\mathbb{T}$ | the course: the ordered index set along which a behavior unfolds, such as time, the steps of training or a swept parameter; the course is only ordered, so the time set of a dynamic, which also carries an addition, takes a local symbol | [process, event and history](../change/process-event-history.md#^course) |
| $\theta$ | a parameter, or the vector of the parameters of a model | [variable, value, observable, parameter and data](../quantities/variable-value-observable.md) |
| $\mathcal{D}$, $\mathcal{W}$ | the domain and the codomain of a variable $F:\mathcal{D}\to\mathcal{W}$; the codomain is the value set of the variable | [variable, value, observable, parameter and data](../quantities/variable-value-observable.md) |
| $\kappa_1,\ldots,\kappa_m$ | the antecedent conditions of a deductive-nomological explanation: particular facts that, together with laws, entail the explanandum | [condition](../quantities/condition.md) |
| $\mathsf{K}$, $\mathsf{I}$ | the core $\mathsf{K}=\langle\mathsf{M}_p,\mathsf{M},\mathsf{M}_{pp},\mathsf{GC},\mathsf{GL}\rangle$ and the intended applications $\mathsf{I}$ of a structuralist theory-element | [theory](../representations/theory.md) |

## Rules of the registry

- **A registered letter keeps one meaning in every note.** Upper and lower case are distinct letters: $\Sigma$ is the subject and $\sigma$ a system.

- **Typeface distinguishes letters.** The italic, calligraphic, sans-serif and blackboard forms of one letter are distinct letters, each with its own row: $K$ is the accepted knowledge and $\mathsf{K}$ the core of a theory-element, $R$ the requested relation and $\mathcal{R}$ the realization map, $D$ the conditions held fixed and $\mathcal{D}$ the domain of a variable. A name of several letters in upright type, such as $\mathrm{Sat}$ or $\mathrm{Obt}$, is one symbol. An upright label inside a formula, such as $\text{E}$ and $\text{I}$ for an excitatory and an inhibitory population, names an object of an example and is not a symbol of the registry.

- **A subscript or a prime marks a member of one object, and it never introduces another object.** Three constructions of a subscript are admitted:
    - an index letter ranges over the members of one family, as $c_i\in C$, the activity $a_j$ and the term $f_j$ with $j\in J$, or the state $x_i$ of the component $c_i$; a numeral marks one member, as $c_1$ and $c_2$, or $\pi_1$ and $\pi_2$;
    - on a state, the numeral $0$ marks the first point of the course, so $x_0$ is the initial state, and no component is numbered $0$;
    - a registered symbol as subscript names the object to which the symbol belongs, as $f_P$ the map of the phenomenon $P$, $Q_\pi$ the question of the problem $\pi$, and $\pi_Q$ the problem of the question $Q$.

  A prime marks another member of the same object, as $Q'$ for a second question.

- **The letter $f$ denotes maps.** With a registered subscript or index, it names a registered map: $f_P$, the input–output map of the phenomenon $P$, and $f_j$, the term $j$ of an additive decomposition. A bare $f$ is a local map, defined in the note that uses it, as the homomorphism $f$ of a [scale of measurement](../quantities/scale-and-level.md) or the function $f$ computed by a system.

- **A mechanism is written with the symbols of a model.** A mechanistic model fills the [elements of a model](../representations/model.md#^model-elements): its components are the constituents $C$, each of its activities $a_j$ is represented by one law of $L$, and its organization is $O$. The [constituents of a mechanism](../../objects/answer/mechanism.md) therefore receive no private symbols. The [mapping onto the answer form](../../objects/answer/answer-form.md) states which aspect of a mechanism fills which element.

- **A local symbol stays free of the registry.** A symbol is local when the note that uses it defines it in the formula or the sentence in which it first appears. A local symbol never takes a registered letter, and two notes may give one free letter two local meanings, each defined in its own note. *Examples*:
    - the evolution map $\varphi$ and the time set $\mathcal{T}$ of a [dynamic](../change/dynamic.md), and the encoding $e$ and the readout $r$ of a [representation](../representations/representation-and-encoding.md);
    - the activation function $\phi$ and the matrix of connection weights $W$ of a rate model, defined in each note that writes one;
    - the neighborhood $\mathcal{N}_i$ of a component;
    - the predicate $\Pi$ on the segments of a course;
    - the letter $F$, which names a variable in the [vocabulary of variables](../quantities/variable-value-observable.md) and the vector field of a flow in the [vocabulary of dynamics](../change/dynamic.md).

- **Three constructions keep a registered letter outside its registered meaning.** *Exception*:
    - a mathematical constant, such as the number $\pi$ in the period $2\pi\sqrt{\ell/g}$ of a pendulum;
    - a variable bound within one formula, such as the endpoints $a$ and $b$ of an interval $[a,b]$, the coefficients of an affine map $x\mapsto ax+b$, or the times $s$ and $t$ in the composition law of a flow;
    - a symbol of a record, quoted as the record declares it. The records carry their own symbols, registered nowhere here: a [symbol of an inquiry](../../../specification/expressions.md) names a quantity of one studied system and is unique only within its record. A target system declaring $L$ for a length therefore collides with no entry of the registry, and neither do the energy $H$ and the couplings $J_{ij}$ of a spin system quoted from a [background record](../../objects/knowledge/background.md).

- **Bold letters are not used.** A structure or a class of structures is named in sans-serif, as the classes of models $\mathsf{M}_p$ and $\mathsf{M}$ of a [structuralist theory](../representations/theory.md).

- **The registry is a constraint on new notes.** A note that needs a symbol for a new object of the method, or a symbol that it will use without defining it, first adds a row to the registry and declares the symbol in a theory note, so that no registered letter denotes two objects.
