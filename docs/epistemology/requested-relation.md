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

The requested relation is the second dimension of the [epistemic task](epistemic-task.md), the layer that sets the kind of knowledge sought. The requested relation acts as a relevance relation: it fixes the **kind of dependence between the explanans and the explanandum** that counts as the answer. The relation is specified separately because two questions can share the explanandum and the modal status yet demand different explanatory information.

| Requested relation                                  | Content the explanans must provide                                                                                                                                       | Example                                                                                                                                                                                                             | Canonical source                                                           |
| --------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| **Causal dependence under interventions**           | factors that systematically change the explanandum under counterfactual interventions<br>$do(X=x)\rightarrow Y$                                                        | _Why did blood pressure $Y$ rise?_ Because an appropriate intervention that increases variable $X$ raises $Y$.                                                                                | interventionism [woodward2003]; structural causal models                     |
| **Causal-mechanistic production**                   | external entities and a succession of interactions that yield the phenomenon<br>$E \rightarrow P$                                                                      | _Why did this neuron fire at time $t$?_ Presynaptic spikes released glutamate. The glutamate then depolarized the membrane past threshold. Distinct, earlier events thus produced the spike.                             | causal-mechanical model [salmon1984]; new mechanistic philosophy              |
| **Constitutive mechanistic organization**           | components, activities and their organization into a phenomenon of the *whole system*, with mutual manipulability<br>$\{c_i,a_i,O\} \Rightarrow P$                            | _How does a neuron generate an action potential?_ Sodium channels open first, and potassium channels open after a delay. The organized activity of the neuron's own parts constitutes the spike as it occurs.  | constitutive relevance [craver2007]; mechanisms as entities and activities [machamer2000]                |
| **Function**                                        | the contribution that a component makes to the system, or the benefit to ecological fitness that retains or selects a trait                                                       | _What is the function of the vertebrate heart?_ Pumping blood. An etiological account further ties the pumping to the evolutionary selection and maintenance of the trait.                                         | Causal-role / systemic accounts; etiological or selected-effects accounts. |
| **Nomological subsumption**                         | a law that the explanandum follows                                                                                                                                     | _Why did this gas expand?_ Given the relevant gas law and heating at constant pressure, the volume must increase.                                                                                                          | DN model [hempel1948]; IS model (Hempel)                                |
| **Statistical dependence**                          | a probabilistic regularity under which the explanandum falls                                                                                                           | _Why did this gas expand?_ The statistical variant of the answer explains the expansion by a statistical law.                                                                                                                             | statistical-relevance model [salmon1971]                                 |
| **Mathematical derivation / Structural constraint** | a mathematical fact that proves that the explanandum obtains or that alternatives are impossible: structural constraint, symmetry, topology, optimization result, etc. | _Why can no route traverse each Königsberg bridge exactly once?_ The graph has more than two vertices of odd degree, so no Eulerian path exists.                                                                              | non-causal and mathematical explanation [lange2016]                         |

> [!NOTE] Close approaches
> - The **causal family** includes two approaches: *interventionist dependence* and *causal-mechanistic production*. *Causal-mechanistic production* usually supplies more information than interventionist dependence alone.
> - Two types of explanations invoke **mechanisms**. *Causal-mechanistic production* relates entities by an ordinary succession of cause and effect. In contrast, *constitutive mechanistic organization* relates the parts of a system to the whole that they compose. The components at the lower level and the phenomenon of the whole system are *simultaneous parts of the same mechanism*. Constitution is therefore usually not treated as ordinary causation between distinct events.
> - The two mechanistic examples share one phenomenon, the spike. The productive explanans lies *outside and before* the spike: it gives the causal history of an event (etiological explanation). The constitutive explanans lies *inside and during* the spike: it analyzes the capacity of the neuron itself [salmon1984].

> [!HINT] Unification
> Unification is absent from the table because it fits a theory of _the source of explanatory power_ more closely than a relation that a research question ordinarily requests [friedman1974] [kitcher1981]. Nomological subsumption, although it stays in the table, fits such a theory in the same way, to a lesser extent [hempel1948].

---
## Sources

Marks follow the [legend of reading marks](../../CONTRIBUTING.md#^reading-marks).

- [craver2007] ◐ [Craver, *Explaining the Brain*, OUP, 2007](https://philpapers.org/rec/CRAETB-2)
- [friedman1974] ◐ [Friedman, "Explanation and scientific understanding", _The Journal of Philosophy_ 71(1), 5–19, 1974](https://philpapers.org/rec/FRIEAS)
- [hempel1948] ○ Hempel & Oppenheim, "Studies in the logic of explanation", _Philosophy of Science_ 15(2), 1948
- [kitcher1981] ◐ [Kitcher, "Explanatory unification", _Philosophy of Science_ 48(4), 507–531, 1981](https://philpapers.org/rec/KITEU)
- [lange2016] ◐ [Lange, _Because Without Cause: Non-Causal Explanations in Science and Mathematics_, OUP, 2016](https://global.oup.com/academic/product/because-without-cause-9780190269487), part I on explanations by constraint
- [machamer2000] ◐ [Machamer, Darden & Craver, "Thinking about mechanisms", _Philosophy of Science_ 67(1), 1–25, 2000](https://doi.org/10.1086/392759)
- [salmon1971] ◐ [Salmon, with Jeffrey & Greeno, *Statistical Explanation and Statistical Relevance*, University of Pittsburgh Press, 1971](https://philpapers.org/rec/SALSE)
- [salmon1984] ◐ Salmon, *Scientific Explanation and the Causal Structure of the World*, Princeton UP, 1984, etiological versus constitutive explanation, via [SEP, Mechanisms in Science](https://plato.stanford.edu/entries/science-mechanisms/)
- [woodward2003] ○ [Woodward, _Making Things Happen_, OUP, 2003](https://academic.oup.com/book/4324)
