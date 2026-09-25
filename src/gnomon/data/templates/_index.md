# Inquiry specification templates

These templates specify an inquiry: a research project copies and fills them, following the method of `docs/epistemology/inquiry-specification.md`. Each object of the inquiry takes a separate file, because one target system can support several phenomena, and each phenomenon can be the subject of more than one question. A file therefore references each object that it depends on by its identifier.

The templates are filled in this order:

1. `target-system.yml`, once per system studied: to declare the system that every later record refers to.
2. `phenomenon.yml`, once per phenomenon: to state the behavior of that system that questions address.
3. `question.yml`, once per research question: to fix the question before any candidate answer is evaluated.
4. `answer.yml`, once per candidate: to state one proposed answer in the terms that the question has fixed.
5. `assessment.yml`, once per candidate assessed: to record whether the candidate passes the tests of the question. The assessment stays apart from the answer, so that a candidate can be restated without altering its verdicts.

One template stands outside this order: `operators.yml`, filled once per problem as soon as a formula requires an operator beyond the canonical set. It declares every such operator that the records of the problem need.

Each template follows eight conventions of format:

- each file is pure YAML, so that a slot carries its dependent fields as nested keys;
- each closed field lists its options in lowercase, first in the comment of its line, so that a schema can check them, and accepts `open` as well;
- each field that holds prose starts as a placeholder consisting only of an UPPERCASE description of the expected content, and the text replacing it may contain formulas;
- the guidance for filling a field stands in the comment of its line, as terse lowercase instructions that never restate the key: "optional", "omit when the target declares the quantity";
- each value that holds prose consists of complete sentences, with an initial capital and a final period;
- each filled `name` value is a short lowercase label without a final period, capitalized only for a proper noun;
- the slots follow the rows of their method note, and each row names the key of its slot, so that a template can be checked mechanically against its note;
- within one entry, the keys run from designation to construction: name, symbol and notation, type, defining expression, then a prose field stating it in words.

Pure YAML departs from the format rule of `docs/design/2-architecture/data-formats.md`. That rule excludes sources written only in YAML for any framework note carrying prose, proofs and rendered math. The rule does not reach the templates: they hold records, not notes. The architecture note, however, does not yet state this distinction between records and notes.
