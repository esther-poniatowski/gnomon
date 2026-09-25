---
role: definition
status: stable
index: "[Epistemology](docs/epistemology/_index.md)"
aliases:
  - Specifying the contrast
  - Contrast class
tags: []
source:
---
# Specifying the contrast

> [!QUESTION] Goal: what must be fixed to specify the alternatives against which a phenomenon is questioned?

The contrast is the third component of the [subject of inquiry](subject-of-inquiry.md): the foils relative to which the phenomenon is questioned.

The contrast passes the [inclusion test](subject-of-inquiry.md#^inclusion-test) for a specification, because it changes the admissible answers: the foil determines which cause explains the phenomenon.

*Example*: Smith and Doe had syphilis and Jones did not. Only Smith contracted paresis. Syphilis explains why Smith rather than Jones contracted paresis, but not why Smith rather than Doe did [lipton2004].

| Specification | When it is required | Options or frame | Examples | Source |
| ------------- | ------------------- | ---------------- | -------- | ------ |
| Locus | for a contrastive why-question | other outcome (same system and conditions, other value of $P$) · other system ($P$ absent) · other condition (same system, different setting or intervention) | synchronous rather than asynchronous activity (outcome); this network rather than a network without inhibitory neurons (system); a strong rather than a weak stimulus (condition) | [vanfraassen1980]; [lipton2004]; potential outcomes $Y_i(d)$ vs $Y_i(d')$ [lundberg2021] |
| Foil set | for a contrastive why-question, with the other values of the explanandum variable as default | per foil, the expressions over the declared observables that hold in that case, with a reading | asynchronous activity (listed); every other oscillation frequency (rule) | [woodward2003] |
| Compatibility | never stated on its own: the locus fixes it | exclusive · compatible (fact and foil co-occur in different systems) | synchronous versus asynchronous activity of one network (exclusive); Smith versus Jones contracting paresis (compatible) | [vanfraassen1980]; [lipton2004] |
| Foil status | with a foil set | observed (a realized comparison case) · counterfactual | a recorded control network (observed); the same network trained on another task (counterfactual) | [lipton2004] |

- **Compatibility is fixed by the locus.** Outcome foils are exclusive. System and condition foils, by contrast, are compatible. *Example*: one network under fixed conditions cannot be both synchronous and asynchronous, whereas "Smith contracted paresis" and "Jones contracted paresis" can both be true. The formal definition of a contrast class admits exclusive foils only [vanfraassen1980]. Compatible foils nevertheless remain legitimate, because the question then asks for a factor that differs between the two cases [lipton2004].
    
- **Foil status determines the source of the evidence.** A *contrastive explanation* names a factor present in the case of the fact and absent in the case of the foil [lipton2004]. When the foil has been observed (e.g. a control animal, a second trained network), the factor is searched for by *comparing* the two recorded cases. When the foil never occurred (e.g. the same network, trained differently), the case of the foil must first be *produced*, by an intervention or by simulating a model. An observed foil also adds a presupposition: the comparison case exists and has been recorded.
    
- **The form of the question determines whether a contrast $X$ is required:**
    
    - mandatory for contrastive why-questions;
    - implicit in questions about a causal effect, where the contrast is the comparator;
    - optional for how-questions and for descriptive aims.

- **A condition foil may reuse an entry of the conditions of $P$.** A condition foil (i.e. the same system in another setting) often names such an entry, for instance an inhibiting circumstance. The foil then refers to that entry, so the circumstance is described only once.

---
## Sources

Marks follow the [legend of reading marks](../../CONTRIBUTING.md#^reading-marks).

- [lipton2004] ◐ Lipton, _Inference to the Best Explanation_, 2nd ed., ch. 3; [Lipton, "Making a difference"](https://www.hps.cam.ac.uk/files/lipton-making-difference.pdf)
- [lundberg2021] ✓ [Lundberg, Johnson & Stewart, "What is your estimand?", _ASR_ 86(3), 2021](https://journals.sagepub.com/doi/abs/10.1177/00031224211004187)
- [vanfraassen1980] ✓ van Fraassen, _The Scientific Image_, ch. 5; [the chapter text](https://www.fitelson.org/290/vanfraassen_pte.pdf)
- [woodward2003] ○ [Woodward, _Making Things Happen_, OUP, 2003](https://academic.oup.com/book/4324)
