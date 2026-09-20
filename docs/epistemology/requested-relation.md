---
role: definition
status: stable
index: "[Epistemology](docs/epistemology/_index.md)"
aliases:
  - Specifying the requested relation
  - Requested relation
tags: []
source:
---
# Specifying the requested relation

> [!QUESTION] Goal: what must be fixed to specify the relation that an explanans must bear to the explanandum?

The requested relation is the second dimension of the [epistemic task](epistemic-task.md).

Relevance relation concerns what **kind of dependence between the explanans and the explanandum** counts as the answer.

Two questions can have the same explanandum and modal status but demand different explanatory information.

| Requested relation                                  | What the explanans must provide                                                                                                                                        | Example                                                                                                                                                                                                             | Canonical source                                                           |
| --------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| **Causal dependence under interventions**           | factors that systematically change the explanandum under counterfactual interventions<br>$do(X=x)\rightarrow Y$                                                        | _Why did blood pressure increase?_ Because increasing variable $X$, under an appropriate intervention, increases blood pressure $Y$.                                                                                | Woodward's interventionism; structural causal models                       |
| **Causal-mechanistic production**                   | external entities and a succession of interactions that yield the phenomenon<br>$E \rightarrow P$                                                                      | _Why did this neuron fire at time $t$?_ Presynaptic spikes released glutamate; the glutamate then depolarized the membrane past threshold. Distinct, earlier events produced the spike.                             | Salmon causal-mechanical model; new mechanistic philosophy                 |
| **Constitutive mechanistic organization**           | components, activities and their organization into a *system-level* phenomenon, with mutual manipulability<br>$\{c_i,a_i,O\} \Rightarrow P$                            | _How does a neuron generate an action potential?_ Sodium channels open, then potassium channels open after a delay. The organized activity of the neuron's own parts constitutes the spike while the spike occurs.  | Craver, Machamer–Darden–Craver; constitutive relevance                     |
| **Function**                                        | the contribution a component makes to the system, or the ecological fitness benefit that retains/selects a trait                                                       | _What is the function of the vertebrate heart?_ Pumping blood; in an etiological account, this function is connected to the trait's evolutionary selection and maintenance.                                         | Causal-role / systemic accounts; etiological or selected-effects accounts. |
| **Nomological subsumption**                         | a law that the explanandum follows                                                                                                                                     | _Why did this gas expand?_ Given the relevant gas law and heating at constant pressure, expansion follows.                                                                                                          | Hempel's DN/IS models                                                      |
| **Statistical dependence**                          | a probabilistic regularity under which the explanandum falls                                                                                                           | _Why did this gas expand?_ Probabilistic variants explain outcomes by statistical laws.                                                                                                                             | Salmon's statistical-relevance model                                       |
| **Mathematical derivation / Structural constraint** | a mathematical fact that proves that the explanandum obtains or that alternatives are impossible: structural constraint, symmetry, topology, optimization result, etc. | _Why can no route traverse each Königsberg bridge exactly once?_ The graph has the wrong vertex-degree structure for an Eulerian path.                                                                              | Contemporary non-causal / mathematical explanation                         |

> [!NOTE] Close approaches
> - The **causal family** includes two influential approaches. *Causal mechanistic production* usually supplies richer information than bare *interventionist dependence*.
> - Two types of explanations invoke **mechanisms**. *Causal-mechanistic production* relates entities by ordinary cause-effect succession. In contrast, *constitutive mechanistic organization* relates components by constitution, and the low-level components and system-level phenomenon are *simultaneous parts of the same mechanism*. Therefore, it is usually not treated as ordinary causation between distinct events.
> - The two mechanistic examples share one phenomenon, the spike. The productive explanans lies *outside and before* the spike: it gives the causal history of an event (etiological explanation). The constitutive explanans lies *inside and during* the spike: it analyzes the capacity of the neuron itself [salmon1984].

> [!HINT] Unification
> Unification (Friedman-Kitcher) is more naturally a theory of _what makes an explanation explanatory_ than a relation ordinarily requested in a research question. The same caveat applies, to a lesser extent, to subsumption (Hempel).

---
## Sources

Marks: ✓ the text itself was read · ◐ checked through an abstract, the publisher page or a secondary summary · ○ cited from standard knowledge, not fetched.

- [salmon1984] ◐ Salmon, *Scientific Explanation and the Causal Structure of the World*, Princeton UP, 1984, etiological versus constitutive explanation, via [SEP, Mechanisms in Science](https://plato.stanford.edu/entries/science-mechanisms/)
