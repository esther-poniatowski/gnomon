# Object candidate — Mechanism

## Role

A mechanism is a structured explanatory model of how entities, activities, and arrangement produce or sustain a target phenomenon.

Its role is to support mechanistic reasoning by tracing how parts and interactions generate the explanandum.

The ontology stores explanatory representations of mechanisms, not world structures themselves.

*Example*: a sodium-potassium pump mechanism explains ion balance by linking membrane proteins, ATP use, and ion transport.

## Properties

**Truth-apt**: Derivative. A mechanism is a structured explanatory model; claims that it exists, fits, or explains are truth-apt.

**Functional stratum**: Explanatory

**Internal structure**:

- **Phenomenon.** Target process, behavior, or pattern to be explained.
- **Entities.** Parts or agents in the mechanism.
- **Activities.** Operations or interactions among entities.
- **Arrangement.** How entities and activities fit together.
- **Productive link.** How the organized activities generate or sustain the phenomenon.
- **Boundary** (context-dependent). Conditions under which the mechanism operates.

## Encoding options

### Causal model subtype

**Category:** Subtype object

**Specification:** Treat `MECHANISM` as the causal subtype of `MODEL` cited by `EXPLANATION`s (e.g., pump mechanism).

**Pros.**
- Preserves organized productive structure as distinct from inferential force.
- Retains the entities, activities, and organization emphasized by mechanistic explanation.
- Fits explanations that cite productive organization.

**Cons.**
- Needs causal process constraints beyond a general model label.
- Must clarify that the ontology stores explanatory representations of mechanisms rather than world structures themselves.

### Explanatory composite

**Category:** Composite object

**Specification:** Combine a causal `MODEL`, component `CLAIM`s, and an explanatory `ARGUMENT` (e.g., protein binding triggers a cascade).

**Pros.**
- Separates the represented process from the inference that cites it.
- Allows claims to describe components while arguments assess adequacy.
- Works when the account must separate process representation from support for an explanandum.

**Cons.**
- Can fragment accounts where the mechanism itself is the central object.

### Model reduction

**Category:** Reduction to another object

**Specification:** Use plain `MODEL` as the carrier cited by `EXPLANATION`s (e.g., causal graph).

**Pros.**
- Avoids a separate type for mature causal models.
- Works when causal organization is already explicit enough for explanation.

**Cons.**
- Makes mechanistic explanation opaque when causal organization is only implicit.
- Risks treating a mechanism as an ordinary model label rather than a productive organization.

## Subtypes

No subtype exists a priori. Mechanisms differ by domain and organization pattern, but entities, activities, arrangement, and productive link already capture those differences inside the mechanism.
