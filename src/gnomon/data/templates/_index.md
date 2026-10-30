# Record templates

These templates specify an inquiry: a research project copies and fills them, following the method of `docs/epistemology/objects/question/question-specification.md`. Each object of the inquiry takes a separate file, because one target system can support several phenomena, and each phenomenon can be the subject of more than one question. A file therefore references each object that it depends on by its identifier.

The templates are filled in this order:

1. [Problem](problem.yml): states one research problem, with the demand and the constraints that its questions serve
2. [Target system](target-system.yml): delimits one system studied, which every later record refers to, and declares its quantities
3. [Background](background.yml): states one body of laws admitted about a target system, with their closure and their organization
4. [Phenomenon](phenomenon.yml): states one behavior of the target system that questions address, with what its data depend on
5. [Question](question.yml): fixes one research question before any candidate answer is evaluated
6. [Model](model.yml): declares one system that stands in for the target, which several answers can ground
7. [Key](key.yml): states one versioned map from the side of a model to the side of the target, which several bindings share
8. [Binding](binding.yml): relates one model to one phenomenon through the inferences that its asserter licenses
9. [Answer](answer.yml): states one candidate answer to an atomic question, as a typed claim with its grounds and the block of its aim
10. [Assessment](assessment.yml): records whether one candidate passes the tests of its question

A model is filled only when the route of an answer runs on a model other than the target, and a binding with its keys only when the claim of that answer also bears on the target. The assessment stays apart from the answer, so that a candidate can be restated without altering its verdicts.

Two templates stand outside this order:

- [Operators](operators.yml): declares, once per problem, every operator beyond the canonical set that a formula of the problem requires
- [Itinerary](itinerary.yml): records each step of one itinerary of inquiry as an instance of a registered epistemic activity, for `gnomon itinerary` to check against the registries

A target system and a phenomenon can be recorded at commitment `identified`, with a definite description and pointers, before their quantities are declared. A question can name a placeholder in place of either record.

Each template follows ten conventions of format:

- each file is pure YAML, so that a slot carries its dependent fields as nested keys;
- each closed field lists its options in lowercase, first in the comment of its line, so that a schema can check them;
- a field stays empty while it is not filled, and the requirement registry decides whether an empty field is a gap or a product of the inquiry;
- each field that holds prose starts as a placeholder consisting only of an UPPERCASE description of the expected content, and the text replacing it may contain formulas;
- the guidance for filling a field stands in the comment of its line, as terse lowercase instructions that never restate the key: "optional", "omit when the target declares the quantity";
- each value that holds prose consists of complete sentences, with an initial capital and a final period;
- each filled `name` value is a short lowercase label without a final period, capitalized only for a proper noun;
- each filled `description` of an identification is a definite description: a noun phrase, lowercase unless it opens on a proper noun, without a final period;
- the slots follow the rows of their specification note, and each row names the key of its slot, so that a template can be checked mechanically against its note; the [alignment tests](../../../../tests/test_gnomon/test_template_alignment.py) pair each table of specifications of a specification note with its template;
- within one entry, the keys run from designation to construction: name, symbol and notation, type, defining expression, then a prose field stating it in words.

Two conventions govern the names of fields:

- each field is named after the distinction that it decides, so two fields of one record that decide different distinctions never share a name;
- `status` names the lifecycle of a record in every record kind, and only its admissible states depend on the kind.
