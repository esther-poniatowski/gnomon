"""
Record schemas: the base schema of each record type, its bound contract, and its template.

A base schema declares the fields of one record type under JSON Schema draft 2020-12, written in
YAML, and leaves each closed vocabulary open. Its contract composes the base, fixes the binding
``_schema`` to ``gnomon:<type>@<version>``, and writes each closed vocabulary from the vocabulary
registry. The template of the record type is rendered from the base schema and the registry, so
that each field, each placeholder and each guidance is declared once, as the decision on record
schemas states.

Besides the standard keywords, a base schema carries the keywords that render its template:

- ``x-template``: the placeholder written after the key of a field;
- ``x-comment``: the guidance written in the comment of the line of a field;
- ``x-vocabulary``: the key of the registry that declares the closed vocabulary of a field;
- ``x-blank``: a blank line before the field;
- ``x-template-key``: the placeholder key of a mapping whose keys are free, such as ``maturity``;
- ``x-header``, at the root: the comment lines that open the template.

See Also
--------
gnomon.cli : the command ``schemas``, which writes or checks the generated files.
"""

from __future__ import annotations

import datetime
from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass
from functools import cache
from pathlib import Path
from typing import Any

import yaml

from .identifiers import RECORD_SEGMENTS, identifier_pattern
from .relation_registry import relation_vocabularies
from .specnotes import DOCS, documentation_notes, documentation_target, flatten

DATA = Path(__file__).parent / "data"

#: The folder of the base schemas and of their contracts.
SCHEMAS = DATA / "schemas"

#: The retained contracts that current consumers must continue to resolve.
COMPATIBILITY = SCHEMAS / "compatibility"

#: The folder of the templates, rendered from the base schemas.
TEMPLATES = DATA / "templates"

#: The registry declaring the values each closed field admits.
VOCABULARY_REGISTRY = DATA / "vocabularies.yml"

#: Generated map from record fields to their canonical documentation notes.
FIELD_DOCUMENTATION = DATA / "field-documentation.yml"

#: The namespace of the logical identifiers of the contracts.
NAMESPACE = "gnomon"

#: The prefix of the absolute identifier of each schema file.
BASE_URI = "https://github.com/esther-poniatowski/gnomon/schemas"

#: The column at which the comment of a line opens, unless the line is longer.
COMMENT_COLUMN = 33

#: The width beyond which a line separates its comment by three spaces instead.
COMMENT_WIDTH = 30

#: The keywords that render a template, which a contract does not repeat.
TEMPLATE_KEYWORDS = (
    "x-template",
    "x-comment",
    "x-vocabulary",
    "x-blank",
    "x-template-key",
    "x-header",
)


Options = Mapping[str, list[tuple[str, str]]]


def base_path(kind: str) -> Path:
    """Return the file of the base schema of a record type."""
    return SCHEMAS / f"{kind}.base.schema.yml"


def contract_path(kind: str) -> Path:
    """Return the file of the contract of a record type."""
    return SCHEMAS / f"{kind}.contract.schema.yml"


def kinds() -> list[str]:
    """Return the record types that declare a base schema, in alphabetical order."""
    return sorted(
        path.name.removesuffix(".base.schema.yml") for path in SCHEMAS.glob("*.base.schema.yml")
    )


@cache
def load_base(kind: str) -> dict[str, Any]:
    """Return the base schema of a record type, read once; callers do not modify it."""
    schema: dict[str, Any] = yaml.safe_load(base_path(kind).read_text(encoding="utf-8"))
    return schema


def _options(entries: Mapping[str, Any]) -> dict[str, list[tuple[str, str]]]:
    """Return normalized vocabulary entries, keyed by their field key."""
    return {
        name: [(str(entry["value"]), str(entry.get("name") or "")) for entry in values]
        for name, values in entries.items()
    }


def shared_vocabulary_options(
    source: Path | None = None,
) -> dict[str, list[tuple[str, str]]]:
    """Return the vocabularies shared by several record types."""
    registry = yaml.safe_load((source or VOCABULARY_REGISTRY).read_text(encoding="utf-8")) or {}
    return _options(registry.get("shared_vocabularies") or {})


def vocabulary_options(kind: str, source: Path | None = None) -> dict[str, list[tuple[str, str]]]:
    """Return, per field of a record type, its admitted values with their glosses.

    >>> options = vocabulary_options("answer")
    >>> options[".status"][0]
    ('entertained', 'put forward as a candidate and not yet adopted for evaluation')
    """
    registry = yaml.safe_load((source or VOCABULARY_REGISTRY).read_text(encoding="utf-8")) or {}
    fields = (registry.get("vocabularies") or {}).get(kind) or {}
    bound = set(vocabulary_paths(load_base(kind)).values()) if kind in kinds() else set()
    shared = {
        key: values for key, values in shared_vocabulary_options(source).items() if key in bound
    }
    return {
        **shared,
        **_options(fields),
        **relation_vocabularies().get(kind, {}),
    }


def comment_of(field: Mapping[str, Any], options: Options) -> str:
    """Return the comment of a field: its admitted values, then its guidance.

    >>> comment_of({"x-vocabulary": "x", "x-comment": "the attitude"},
    ...            {"x": [("a", ""), ("b", "gloss")]})
    'a | b (gloss); the attitude'
    """
    guidance = str(field.get("x-comment") or "")
    vocabulary = field.get("x-vocabulary")
    if not vocabulary:
        return guidance
    listed = " | ".join(
        f"{value} ({name})" if name else value for value, name in options[str(vocabulary)]
    )
    return f"{listed}; {guidance}" if guidance else listed


def line(text: str, comment: str) -> str:
    """Return one line of a template, with its comment aligned at the comment column."""
    if not comment:
        return text
    gap = COMMENT_COLUMN - len(text) if len(text) < COMMENT_WIDTH else 3
    return f"{text}{' ' * gap}# {comment}"


def head(key: str, field: Mapping[str, Any]) -> str:
    """Return the key of a field followed by its placeholder."""
    raw = field.get("x-template")
    return f"{key}: {raw}" if raw not in (None, "") else f"{key}:"


class _TemplateLines:
    """The lines of a template being rendered, and the vocabulary options that its comments list."""

    def __init__(self, options: Options) -> None:
        self.options = options
        self.out: list[str] = []

    def add_field(self, key: str, spec: Mapping[str, Any], indent: int, dash: bool = False) -> None:
        """Append the lines of one field, and of the fields that it holds."""
        if spec.get("x-blank"):
            self.out.append("")
        prefix = " " * indent + ("- " if dash else "")
        inner = indent + 2 if dash else indent
        comment = comment_of(spec, self.options)
        properties = spec.get("properties")
        items = spec.get("items")
        free = spec.get("additionalProperties")
        if isinstance(properties, Mapping) and spec.get("x-template") in (None, ""):
            self.out.append(line(prefix + key + ":", comment))
            for name, child in properties.items():
                self.add_field(name, child, inner + 2)
        elif isinstance(items, Mapping) and spec.get("x-template") in (None, ""):
            self.out.append(line(prefix + key + ":", comment))
            self.add_item(items, inner + 2)
        elif isinstance(free, Mapping) and free.get("x-template-key"):
            self.out.append(line(prefix + key + ":", comment))
            self.out.append(
                line(
                    " " * (inner + 2) + head(str(free["x-template-key"]), free),
                    comment_of(free, self.options),
                )
            )
        else:
            self.out.append(line(prefix + head(key, spec), comment))

    def add_item(self, items: Mapping[str, Any], indent: int) -> None:
        """Append the lines of the one entry that a template list shows."""
        properties = items.get("properties")
        if isinstance(properties, Mapping) and properties:
            for position, (name, child) in enumerate(properties.items()):
                self.add_field(name, child, indent + (2 if position else 0), dash=not position)
        else:
            self.out.append(
                line(
                    " " * indent + f"- {items.get('x-template', '')}",
                    comment_of(items, self.options),
                )
            )


def render_template(kind: str, base: Mapping[str, Any], options: Options) -> str:
    """Return the template of a record type, opened by the binding to its contract and rendered from
    its base schema."""
    lines = _TemplateLines(options)
    lines.out += [f"# {text}" if text else "#" for text in base.get("x-header") or []]
    if lines.out:
        lines.out.append("")
    lines.out.append(f"_schema: {identifier(kind, int(base.get('x-version', 1)))}")
    for name, spec in (base.get("properties") or {}).items():
        lines.add_field(name, spec, 0)
    return "\n".join(lines.out) + "\n"


def _initial_annotations(
    field: Mapping[str, Any],
    options: Options,
    documentation: Callable[[str], str | None] | None,
    path: str,
) -> tuple[dict[str, Any], Any]:
    """Return the direct annotations of one field and its parsed template value."""
    added: dict[str, Any] = {}
    target = documentation(path) if documentation and path else None
    description = field.get("description")
    if target and isinstance(description, str):
        added["description"] = f"{description}\n\n[Read the canonical specification]({target})."
    template = field.get("x-template")
    template_value = yaml.safe_load(template) if isinstance(template, str) else template
    if template not in (None, "") and not field.get("examples"):
        added["examples"] = [template_value]
    vocabulary = field.get("x-vocabulary")
    if vocabulary:
        added["enum"] = [value for value, _ in options[str(vocabulary)]] + [None]
    return added, template_value


def overlay(
    field: Mapping[str, Any],
    options: Options,
    documentation: Callable[[str], str | None] | None = None,
    path: str = "",
) -> dict[str, Any] | None:
    """Return the annotations and constraints that a contract adds to a field, recursively.

    A field with a template value but no authored example receives that value as its standard JSON
    Schema example. The value is parsed as YAML because ``x-template`` stores the YAML source that
    the generated template writes. Authored examples remain authoritative.

    The constraints comprise the values of each vocabulary and the keys that an object may hold.

    The keys are closed by ``propertyNames``, since each subschema of ``allOf`` is validated alone,
    so ``additionalProperties`` in the contract would reject the keys that the base declares.
    """
    added, template_value = _initial_annotations(field, options, documentation, path)
    declared = field.get("properties")
    if isinstance(declared, Mapping) and declared:
        added["propertyNames"] = {"enum": list(declared)}
    nested = {}
    for name, child in (field.get("properties") or {}).items():
        child_path = f"{path}.{name}" if path else str(name)
        if sub := overlay(child, options, documentation, child_path):
            nested[name] = sub
    if nested:
        added["properties"] = nested
    items = field.get("items")
    item_annotations = (
        overlay(items, options, documentation, f"{path}[]") if isinstance(items, Mapping) else None
    )
    if isinstance(template_value, list) and template_value:
        item_annotations = dict(item_annotations or {})
        if not isinstance(items, Mapping) or not items.get("examples"):
            item_annotations.setdefault("examples", template_value)
    if item_annotations:
        added["items"] = item_annotations
    free = field.get("additionalProperties")
    if isinstance(free, Mapping) and (sub := overlay(free, options, documentation, f"{path}{{}}")):
        added["additionalProperties"] = sub
    return added or None


def vocabulary_paths(base: Mapping[str, Any]) -> dict[str, str]:
    """Return the vocabulary bound to each closed field of a base schema, keyed by the path of the
    field.

    The path joins the keys from the root with dots; an entry of a list adds no segment.

    >>> vocabulary_paths({"properties": {"status": {"x-vocabulary": ".status"},
    ...     "laws": {"items": {"properties": {"role": {"x-vocabulary": "laws.role"}}}}}})
    {'status': '.status', 'laws.role': 'laws.role'}
    """
    bound: dict[str, str] = {}

    def walk(node: Mapping[str, Any], path: tuple[str, ...]) -> None:
        for name, child in (node.get("properties") or {}).items():
            if not isinstance(child, Mapping):
                continue
            if child.get("x-vocabulary"):
                bound[".".join((*path, name))] = str(child["x-vocabulary"])
            walk(child, (*path, name))
        items = node.get("items")
        if isinstance(items, Mapping):
            walk(items, path)
        free = node.get("additionalProperties")
        if isinstance(free, Mapping):
            if free.get("x-vocabulary"):
                bound[f"{'.'.join(path)}[]"] = str(free["x-vocabulary"])
            walk(free, path)

    walk(base, ())
    return bound


def schema_field_paths(base: Mapping[str, Any]) -> list[str]:
    """Return every named field path of a schema, marking list entries with ``[]``."""
    found: list[str] = []

    def walk(node: Mapping[str, Any], prefix: str) -> None:
        for name, child in (node.get("properties") or {}).items():
            path = f"{prefix}.{name}" if prefix else str(name)
            found.append(path)
            walk(child, path)
            items = child.get("items")
            if isinstance(items, Mapping):
                walk(items, f"{path}[]")

    walk(base, "")
    return found


def live_documentation_notes(
    kind: str, base: Mapping[str, Any], options: Options
) -> dict[str, str]:
    """Return field documentation derived from the specification notes in a checkout."""
    paths = flatten(yaml.safe_load(render_template(kind, base, options)))
    return documentation_notes(kind, paths, schema_field_paths(base))


def load_documentation_registry(
    source: Path | None = None,
) -> dict[str, dict[str, str]]:
    """Return the packaged field-documentation map, keyed by record kind and field path."""
    document = yaml.safe_load((source or FIELD_DOCUMENTATION).read_text(encoding="utf-8"))
    return {
        str(kind): {str(path): str(note) for path, note in fields.items()}
        for kind, fields in (document or {}).items()
    }


def field_documentation_notes(
    kind: str, base: Mapping[str, Any], options: Options
) -> dict[str, str]:
    """Return field documentation from its notes in a checkout, else from package data."""
    if DOCS.is_dir():
        return live_documentation_notes(kind, base, options)
    return load_documentation_registry().get(kind, {})


def identifier(kind: str, version: int) -> str:
    """Return the logical identifier of the contract of a record type."""
    return f"{NAMESPACE}:{kind}@{version}"


def identifier_prefix(base: Mapping[str, Any]) -> str | None:
    """Return the prefix of the identifiers of a record type, read from the placeholder of its
    field ``id``, or None when the type declares no identifier.

    >>> identifier_prefix({"properties": {"id": {"x-template": "quest.TOPIC.NAME"}}})
    'quest'
    """
    template = ((base.get("properties") or {}).get("id") or {}).get("x-template")
    return str(template).split(".", 1)[0] if template else None


def identifier_example(prefix: str) -> str:
    """Return a valid illustrative record identifier for ``prefix``.

    The prefix registry fixes the number of segments. The example uses ordinary lowercase values,
    rather than the uppercase placeholders reserved for unfilled source templates.

    >>> identifier_example("system")
    'system.topic'
    >>> identifier_example("prob")
    'prob.topic.name'
    """
    return ".".join([prefix, "topic", *(["name"] * (RECORD_SEGMENTS[prefix] - 2))])


def question_aim_rules(base: Mapping[str, Any]) -> list[dict[str, Any]]:
    """Return form rules for question fields required by an epistemic aim.

    The requirement registry may also name fields of a phenomenon or another record. Such a
    dependency cannot be checked by a rule over one question instance, so only paths within the
    question contract are published here. A rule is omitted when its root field is absent from the
    supplied base, which keeps partial schema fixtures self-contained.
    """
    # Import after schema initialization: completeness.maturity depends on this module.
    # pylint: disable=import-outside-toplevel
    from .completeness.requirements import requirements_by_aim

    properties = base.get("properties") or {}
    record_type = (properties.get("type") or {}).get("x-template")
    if record_type != "question":
        return []
    rules: list[dict[str, Any]] = []
    for aim, declaration in requirements_by_aim().items():
        for path in declaration["required"]:
            owner, separator, field = path.partition(".")
            if owner != "question" or not separator or field.split(".", 1)[0] not in properties:
                continue
            rules.append(
                {
                    "check": "required-when",
                    "field": field,
                    "when": {"field": "task.epistemic_aim", "equals": aim},
                }
            )
    return rules


def contract(
    kind: str,
    base: Mapping[str, Any],
    options: Options,
    field_notes: Mapping[str, str] | None = None,
) -> dict[str, Any]:
    """Return the contract of a record type: the base, the binding of ``_schema``, and its
    vocabularies."""
    version = int(base.get("x-version", 1))
    schema: dict[str, Any] = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": f"{BASE_URI}/{kind}.contract.schema.yml",
        "title": f"{base.get('title', kind)} contract",
        "description": f"The record type `{kind}`, bound to `{identifier(kind, version)}`,"
        " with its closed vocabularies.",
        "allOf": [{"$ref": str(base["$id"])}],
        "required": ["_schema"],
        "properties": {
            "_schema": {
                "const": identifier(kind, version),
                "title": "Schema",
                "description": "The logical identifier of the contract that the record follows.",
            },
            "type": {"const": kind},
        },
        "x-identifier": base.get("x-identifier", "id"),
    }
    prefix = identifier_prefix(base)
    if prefix in RECORD_SEGMENTS:
        schema["properties"]["id"] = {"pattern": identifier_pattern(str(prefix))}
    notes = (
        field_notes if field_notes is not None else field_documentation_notes(kind, base, options)
    )
    added: dict[str, Any] = (
        overlay(
            base,
            options,
            lambda path: documentation_target(notes[path]) if path in notes else None,
        )
        or {}
    )
    if "properties" in added:
        for name, annotations in added["properties"].items():
            schema["properties"][name] = {
                **schema["properties"].get(name, {}),
                **annotations,
            }
    if prefix in RECORD_SEGMENTS:
        schema["properties"]["id"]["examples"] = [identifier_example(str(prefix))]
    if aim_rules := question_aim_rules(base):
        schema["x-rules"] = aim_rules
    schema["propertyNames"] = {"enum": ["_schema", *(base.get("properties") or {})]}
    return schema


def dump(document: Mapping[str, Any]) -> str:
    """Return a schema written in YAML, keys in their declared order."""
    return yaml.safe_dump(dict(document), sort_keys=False, allow_unicode=True, width=100)


def schema_files() -> dict[Path, str]:
    """Return the contracts and the templates generated from the base schemas and the registry,
    with their content."""
    files: dict[Path, str] = {}
    notes_by_kind: dict[str, dict[str, str]] = {}
    for kind in kinds():
        base, options = load_base(kind), vocabulary_options(kind)
        notes_by_kind[kind] = field_documentation_notes(kind, base, options)
        files[contract_path(kind)] = (
            f"# Generated by `gnomon schemas` from `{kind}.base.schema.yml` and the vocabulary"
            " registry. Edit those, not this file.\n"
            + dump(contract(kind, base, options, notes_by_kind[kind]))
        )
        files[TEMPLATES / f"{kind}.yml"] = render_template(kind, base, options)
    files[FIELD_DOCUMENTATION] = (
        "# Generated by `gnomon schemas` from the specification notes and base schemas.\n"
        "# Edit those sources, not this file.\n" + dump(notes_by_kind)
    )
    return files


@cache
def identifier_prefixes() -> dict[str, str]:
    """Return the prefix of the identifiers of each record type that declares one, keyed by the
    value of its field ``type``.

    >>> identifier_prefixes()["target-system"], identifier_prefixes()["question"]
    ('system', 'quest')
    """
    found: dict[str, str] = {}
    for kind in kinds():
        base = load_base(kind)
        prefix = identifier_prefix(base)
        if prefix:
            found[str(base["properties"]["type"]["x-template"])] = prefix
    return found


def record_kinds() -> dict[str, str]:
    """Return the base schema of each record type, keyed by the value of the field ``type``."""
    return {str(load_base(kind)["properties"]["type"]["x-template"]): kind for kind in kinds()}


@cache
@cache
def published_contracts() -> dict[str, dict[str, Any]]:
    """Return current and retained record contracts, keyed by logical identifier."""
    paths = [contract_path(kind) for kind in kinds()]
    paths += sorted(COMPATIBILITY.glob("*.contract.schema.yml"))
    contracts = [yaml.safe_load(path.read_text(encoding="utf-8")) for path in paths]
    return {str(document["properties"]["_schema"]["const"]): document for document in contracts}


@cache
def contract_validator(contract_id: str) -> Any:
    """Return a validator for a current kind or a published logical contract identifier."""
    # pylint: disable=import-outside-toplevel  # jsonschema loads only when a record is validated
    from jsonschema import Draft202012Validator
    from referencing import Registry, Resource

    named = (
        contract_id
        if contract_id.startswith(f"{NAMESPACE}:")
        else identifier(contract_id, int(load_base(contract_id).get("x-version", 1)))
    )
    bases = [load_base(name) for name in kinds()]
    bases += [
        yaml.safe_load(path.read_text(encoding="utf-8"))
        for path in sorted(COMPATIBILITY.glob("*.base.schema.yml"))
    ]
    resources = [(base["$id"], Resource.from_contents(base)) for base in bases]
    return Draft202012Validator(
        published_contracts()[named],
        registry=Registry().with_resources(resources),
    )


#: The words that name the types of JSON Schema in a message.
TYPE_NAMES: Mapping[str, str] = {
    "string": "text",
    "array": "a list",
    "object": "a mapping",
    "number": "a number",
    "integer": "a whole number",
    "boolean": "true or false",
    "null": "nothing",
}


@dataclass(frozen=True)
class Violation:
    """One violation of a contract, with the path of its field and a message that states the
    repair.

    Attributes
    ----------
    path : tuple
        The keys and the list positions from the root of the record to the field.
    keyword : str
        The kind of the violation: ``type``, ``unknown-key``, ``enum``, ``required``,
        ``pattern``, ``const``, ``contract``, or the keyword of JSON Schema otherwise.
    message : str
        The violation and its repair, in words.
    """

    path: tuple[Any, ...]
    keyword: str
    message: str


def field_path(path: Sequence[Any]) -> str:
    """Return the path of a field as the messages print it: keys joined by dots, positions in
    brackets.

    >>> field_path(("steps", 0, "norm", "judged"))
    'steps[0].norm.judged'
    """
    text = ""
    for part in path:
        text += f"[{part}]" if isinstance(part, int) else (f".{part}" if text else str(part))
    return text


def _found_type(value: Any) -> str:
    """Return the name of the type of a value, as a message prints it."""
    if isinstance(value, bool):
        return "true or false"
    if isinstance(value, (int, float)):
        return "a number"
    if isinstance(value, list):
        return "a list"
    if isinstance(value, Mapping):
        return "a mapping"
    return "text" if isinstance(value, str) else type(value).__name__


def _unknown_key(path: tuple[Any, ...], error: Any) -> Violation:
    """A key that is no field of the mapping that holds it."""
    admitted = ", ".join(str(v) for v in error.validator_value if v != "_schema")
    message = f"{error.instance} is no field here; the fields admitted are {admitted}"
    return Violation(path, "unknown-key", message)


def _unadmitted(path: tuple[Any, ...], error: Any) -> Violation:
    """A value outside the closed vocabulary of its field."""
    admitted = ", ".join(str(v) for v in error.validator_value if v is not None)
    message = f"{error.instance} is not admitted; the admitted values are {admitted}"
    return Violation(path, "enum", message)


def _mistyped(path: tuple[Any, ...], error: Any) -> Violation:
    """A value of another type than the field admits; a date read from an unquoted text."""
    value = error.instance
    if isinstance(value, (datetime.date, datetime.datetime)):
        message = f'a date written without quotes; write it in quotes, as "{value}"'
        return Violation(path, "type", message)
    wanted = error.validator_value
    names = wanted if isinstance(wanted, list) else [wanted]
    admitted = " or ".join(TYPE_NAMES.get(str(t), str(t)) for t in names if t != "null")
    return Violation(
        path, "type", f"holds {_found_type(value)} where the contract admits {admitted}"
    )


def _missing(path: tuple[Any, ...], error: Any) -> Violation:
    """A required field absent from its mapping."""
    held = error.instance if isinstance(error.instance, Mapping) else {}
    missing = [name for name in error.validator_value if name not in held]
    return Violation(path, "required", f"the field {', '.join(missing)} is required")


#: The message of each kind of violation, keyed by the keyword of JSON Schema.
READABLE: Mapping[str, Any] = {
    "enum": _unadmitted,
    "type": _mistyped,
    "required": _missing,
    "const": lambda path, error: Violation(path, "const", f"must be {error.validator_value}"),
    "pattern": lambda path, error: Violation(
        path, "pattern", f"{error.instance} does not have the required form"
    ),
}


def _readable(error: Any) -> Violation:
    """Return a violation of a contract in words, with its repair."""
    path = tuple(error.absolute_path)
    if error.validator == "enum" and "propertyNames" in error.schema_path:
        return _unknown_key(path, error)
    handler = READABLE.get(str(error.validator))
    if handler is None:
        return Violation(path, str(error.validator), str(error.message))
    result: Violation = handler(path, error)
    return result


def contract_violations(record: Mapping[str, Any]) -> list[Violation]:
    """Return every violation of the contract that a record names in its field ``_schema``,
    each in words with its repair.

    A record names no contract, or a contract that `gnomon` does not publish, when its binding is
    missing or unknown.

    >>> import datetime
    >>> for v in contract_violations({"_schema": "gnomon:itinerary@1", "type": "itinerary",
    ...     "steps": [{"norm": {"judged": datetime.date(2026, 11, 5)}}], "extra": 1}):
    ...     print(field_path(v.path) or "(record)", v.keyword)
    (record) unknown-key
    steps[0].norm.judged type
    """
    named = record.get("_schema")
    published = {
        logical_id: str(contract["properties"]["type"]["const"])
        for logical_id, contract in published_contracts().items()
    }
    if not named:
        return [Violation(("_schema",), "contract", "the record names no contract")]
    if named not in published:
        return [Violation(("_schema",), "contract", f"{named} is no contract of {NAMESPACE}")]
    kind = published[named]
    validator = contract_validator(str(named))
    errors = sorted(
        validator.iter_errors(dict(record)),
        key=lambda e: list(map(str, e.absolute_path)),
    )
    found = [_readable(error) for error in errors]
    prefix = identifier_prefix(load_base(kind))
    if prefix in RECORD_SEGMENTS:
        count = RECORD_SEGMENTS[str(prefix)] - 1
        form = (
            f"is not {prefix} followed by {count} segment{'s' if count > 1 else ''} of lowercase"
            " words joined by hyphens"
        )
        found = [
            (
                Violation(v.path, v.keyword, f"{record.get('id')} {form}")
                if v.keyword == "pattern" and v.path == ("id",)
                else v
            )
            for v in found
        ]
    return found


def record_errors(record: Mapping[str, Any]) -> list[str]:
    """Return every violation of the contract that a record names, each as one line: the path of
    the field, then the violation and its repair."""
    return [f"{field_path(v.path) or '(record)'}: {v.message}" for v in contract_violations(record)]
