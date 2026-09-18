---
role: definition
status: stable
index: "[Epistemology](docs/epistemology/_index.md)"
aliases:
  - Specifying an epistemic task
tags: []
source:
---
#  Specifying an epistemic task

> [!QUESTION] Goal: what must be fixed to specify an epistemic task?

This [layer of inquiry](inquiry-specification.md) specifies the **epistemic problem before any candidate answer is evaluated**. Different aims impose different evidential requirements on a model.

## Sub-levels of specification

> [!IMPORTANT]
> Epistemic aim is the broadest concept. **Explanation is only one epistemic aim among others**. The philosophy-of-modeling literature explicitly distinguishes explaining and understanding from other cognitive functions of models.

An epistemic task can be described by:
$$T=\langle A,R,\mu\rangle $$

| Dimension                  | Role                                                                                     | Typical options                                                                                                          | Canonical tradition                                 |
| -------------------------- | ---------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------- |
| **Epistemic aim $A$**      | What knowledge is the inquiry intended to produce? What cognitive achievement is sought? | description/representation, prediction, explanation, understanding, exploration, possibility proof, theory/model testing |                                                     |
| **Requested relation $R$** | What kind of relation must the explanans bear to the explanandum to answer the question? | causal, mechanistic, constitutive, functional, statistical, nomological, mathematical                                    | van Fraassen ("relevance / dependence relation")    |
| **Modal strength $\mu$**   | How tight the answer must bind the phenomenon                                            | actual, possible, necessary                                                                                              | Verreault-Julien (_how-possibly_ vs _how-actually_) |

## Epistemic aims (achievements)

| Epistemic aim                                 | Operational question                                                         | Epistemic product                                                                 | Status in literature                                                                                                                         |
| --------------------------------------------- | ---------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| **Description / representation**              | _What structure does the target system have?_                                | accurate characterization of states, patterns, properties, relations              | Core aim; de Regt, model-representation literature                                                                                           |
| **Prediction**                                | _Given specified conditions, what will occur?_                               | warranted expectation about unknown outcomes                                      | Core aim; standard philosophy of science                                                                                                     |
| **Explanation**                               | _Why or how does this phenomenon occur?_                                     | identification of explanatory relations — causal, mechanistic, mathematical, etc. | Core aim; major explanation traditions                                                                                                       |
| **Understanding**                             | _Can the relevant structure / dependencies be grasped and reasoned through?_ | cognitive grasp enabling qualitative or counterfactual reasoning                  | Core but philosophically contested in its relation to explanation; de Regt, Strevens, Elgin, Khalifa                                         |
| **Modal knowledge**                           | _What is possible, impossible, necessary, or contingent?_                    | possibility /  impossibility / necessity claims                                   | Legitimate epistemic aim, but better viewed as a *modal dimension of knowledge* than as a coordinate category with explanation or prediction |
| **Knowledge of theories / models themselves** | _What follows from this theory/model? How does it behave?_                   | consequences, regimes, limits, structural properties                              | Recognized especially in exploratory and theoretical modelling                                                                               |

## Relevance relations

Relevance relation concerns what **kind of dependence between the explanans and the explanandum** counts as the answer.

Two questions can have the same explanandum and modal status but demand different explanatory information.

| Requested relation                                  | What the explanans must provide                                                                                                                                        | Example                                                                                                                                                                                     | Canonical source                                                           |
| --------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| **Causal dependence under interventions**           | factors that systematically change the explanandum under counterfactual interventions<br>$do(X=x)\rightarrow Y$                                                        | _Why did blood pressure increase?_ Because increasing variable $X$, under an appropriate intervention, increases blood pressure $Y$.                                                        | Woodward's interventionism; structural causal models                       |
| **Causal-mechanistic production**                   | external entities and a succession of interactions that yield the phenomenon<br>$E \rightarrow P$                                                                      | _How does synaptic input cause a neuron to spike?How does an action potential propagate?_ Ion channels open and close in an organized sequence, altering membrane conductances and voltage. | Salmon causal-mechanical model; new mechanistic philosophy                 |
| **Constitutive mechanistic organization**           | components, activities and their organization into a *system-level* phenomenon, with mutual manipulability<br>$\{c_i,a_i,O\} \Rightarrow P$                            | _How does a synapse transmit a signal?_ Calcium influx, vesicle fusion, neurotransmitter release, receptors, etc. organized together constitute synaptic transmission.                      | Craver, Machamer–Darden–Craver; constitutive relevance                     |
| **Function**                                        | the contribution a component makes to the system, or the ecological fitness benefit that retains/selects a trait                                                       | _What is the function of the vertebrate heart?_ Pumping blood; in an etiological account, this function is connected to the trait's evolutionary selection and maintenance.                 | Causal-role / systemic accounts; etiological or selected-effects accounts. |
| **Nomological subsumption**                         | a law that the explanandum follows                                                                                                                                     | _Why did this gas expand?_ Given the relevant gas law and heating at constant pressure, expansion follows.                                                                                  | Hempel's DN/IS models                                                      |
| **Statistical dependence**                          | a probabilistic regularity under which the explanandum falls                                                                                                           | _Why did this gas expand?_ Probabilistic variants explain outcomes by statistical laws.                                                                                                     | Salmon's statistical-relevance model                                       |
| **Mathematical derivation / Structural constraint** | a mathematical fact that proves that the explanandum obtains or that alternatives are impossible: structural constraint, symmetry, topology, optimization result, etc. | _Why can no route traverse each Königsberg bridge exactly once?_ The graph has the wrong vertex-degree structure for an Eulerian path.                                                      | Contemporary non-causal / mathematical explanation                         |

> [!NOTE] Close approaches
> - The **causal family** includes two influential approaches. *Causal mechanistic production* usually supplies richer information than bare *interventionist dependence*.
> - Two types of explanations invoke **mechanisms**. *Causal-mechanistic production* relates entities by ordinary cause-effect succession. In contrast, *constitutive mechanistic organization* relates components by constitution, and the low-level components and and system-level phenomenon are *simultaneous parts of the same mechanism*. Therefore, it is usually not treated as ordinary causation between distinct events.

> [!HINT] Unification
> Unification (Friedman-Kitcher) is more naturally a theory of _what makes an explanation explanatory_ than a relation ordinarily requested in a research question. The same caveat applies, to a lesser extent, to subsumption (Hempel).