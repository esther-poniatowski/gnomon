"""Record schemas: the generated files match their sources, and the schemas are valid and complete.

The base schemas are the source of the fields, and the vocabulary registry the source of the closed
vocabularies, so the contracts and the templates are generated copies. These tests check that each
copy equals its generated form, that every schema is valid under draft 2020-12, and that each
contract writes the vocabularies of the registry.
"""

from __future__ import annotations

import re
from collections.abc import Mapping
from pathlib import Path
from typing import Any

import pytest
import yaml
from jsonschema import Draft202012Validator
from referencing import Registry, Resource

from gnomon import generated, schemas
from gnomon.generated import stale_files
from gnomon.specnotes import documentation_notes, documentation_target, flatten

KINDS = schemas.kinds()

FORM_CONTROL_KEYS = {
    "$ref",
    "allOf",
    "anyOf",
    "const",
    "enum",
    "oneOf",
    "type",
    "x-kind",
    "x-vocabulary",
}

SCALAR_FORM_KINDS = {
    "boolean",
    "choice",
    "label",
    "latex",
    "markdown",
    "markdown-line",
    "number",
    "text",
}


def registry() -> Registry:
    """Return the resources of every base schema, keyed by its absolute identifier."""
    resources = [
        (
            schemas.load_base(kind)["$id"],
            Resource.from_contents(schemas.load_base(kind)),
        )
        for kind in KINDS
    ]
    return Registry().with_resources(resources)


def test_every_generated_file_equals_its_generated_form() -> None:
    assert stale_files() == []


def test_the_generated_file_check_rejects_a_changed_copy(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """The generated-copy check must fail when on-disk bytes differ from their source."""
    path = tmp_path / "generated.yml"
    path.write_text("stale\n", encoding="utf-8")
    monkeypatch.setattr(generated, "generated_files", lambda: {path: "current\n"})

    assert generated.stale_files() == [path]


def test_no_field_describes_itself_by_a_placeholder() -> None:
    """A description states what a field holds; the form "The X of the record." names the field
    again and states nothing, so no base schema may carry it."""
    # pylint: disable=import-outside-toplevel
    from gnomon.fieldindex import _schema_fields

    placeholder = re.compile(r"^The .* of the record\.$")
    found = [
        (kind, path)
        for kind in KINDS
        for path, node in _schema_fields(schemas.load_base(kind))
        if placeholder.match(str(node.get("description") or ""))
    ]
    assert not found, found


def test_every_pending_verdict_declares_an_unresolved_research_state() -> None:
    """A pending verdict is valid authored content, but every form must distinguish it from a
    completed judgment and from a validation defect."""
    # pylint: disable=import-outside-toplevel
    from gnomon.fieldindex import _schema_fields

    expected = [{"check": "unresolved-value", "value": "pending"}]
    pending = [
        (kind, path, node.get("x-rules"))
        for kind in KINDS
        for path, node in _schema_fields(schemas.load_base(kind))
        if node.get("x-template") == "pending"
    ]
    assert pending
    assert all(rules == expected for _, _, rules in pending), pending


def form_metadata_defects(schema: Mapping[str, Any]) -> list[tuple[str, str]]:
    """Return fields without canonical guidance or a determinate form interaction."""
    found: list[tuple[str, str]] = []

    def walk(node: Mapping[str, Any], path: str, named: bool) -> None:
        if named and not str(node.get("title") or "").strip():
            found.append((path, "title"))
        if named and not str(node.get("description") or "").strip():
            found.append((path, "description"))
        structural = any(
            isinstance(node.get(key), Mapping)
            for key in ("properties", "items", "additionalProperties")
        )
        if not structural and not FORM_CONTROL_KEYS.intersection(node):
            found.append((path, "interaction"))
        for key, child in (node.get("properties") or {}).items():
            walk(child, f"{path}.{key}" if path else key, True)
        items = node.get("items")
        if isinstance(items, Mapping):
            walk(items, f"{path}[]", False)
        values = node.get("additionalProperties")
        if isinstance(values, Mapping):
            walk(values, f"{path}{{}}", False)

    walk(schema, "", False)
    return found


def test_form_metadata_check_rejects_each_missing_component() -> None:
    """The metadata check must detect absent titles, descriptions, and interaction data."""
    planted = {
        "properties": {
            "untitled": {"description": "Guidance.", "type": "string"},
            "undocumented": {"title": "Undocumented", "type": "string"},
            "undetermined": {"title": "Undetermined", "description": "Guidance."},
            "list": {
                "title": "List",
                "description": "Guidance.",
                "type": "array",
                "items": {},
            },
            "mapping": {
                "title": "Mapping",
                "description": "Guidance.",
                "type": "object",
                "additionalProperties": {},
            },
        }
    }
    assert form_metadata_defects(planted) == [
        ("untitled", "title"),
        ("undocumented", "description"),
        ("undetermined", "interaction"),
        ("list[]", "interaction"),
        ("mapping{}", "interaction"),
    ]


def test_contract_overlay_publishes_template_values_as_standard_examples() -> None:
    """Generated contracts expose each otherwise unrepresented template value to form clients."""
    base = {
        "properties": {
            "title": {"x-template": '"SHORT TITLE"'},
            "authored": {
                "x-template": '"PLACEHOLDER"',
                "examples": ["A representative title"],
            },
            "entries": {"x-template": "[ENTRY]", "items": {}},
            "mapping": {"additionalProperties": {"x-template": "{SYMBOL: MEANING}"}},
        }
    }

    assert schemas.overlay(base, {}) == {
        "propertyNames": {"enum": ["title", "authored", "entries", "mapping"]},
        "properties": {
            "title": {"examples": ["SHORT TITLE"]},
            "entries": {
                "examples": [["ENTRY"]],
                "items": {"examples": ["ENTRY"]},
            },
            "mapping": {"additionalProperties": {"examples": [{"SYMBOL": "MEANING"}]}},
        },
    }


def test_contract_keeps_constraints_when_it_adds_form_annotations() -> None:
    """A generated example composes with the binding constraints of the contract."""
    base = {
        "$id": "https://example.test/question.base.schema.yml",
        "title": "Question",
        "x-version": 1,
        "properties": {"type": {"x-template": "question"}},
    }

    generated_contract = schemas.contract("question", base, {})

    assert generated_contract["properties"]["type"] == {
        "const": "question",
        "examples": ["question"],
    }


def test_contract_publishes_the_canonical_specification_in_field_guidance() -> None:
    """A form obtains the field instruction and its canonical target from one contract layer."""
    contract = schemas.contract(
        "question",
        schemas.load_base("question"),
        schemas.vocabulary_options("question"),
    )
    description = contract["properties"]["task"]["properties"]["epistemic_aim"]["description"]

    assert description.startswith(
        schemas.load_base("question")["properties"]["task"]["properties"]["epistemic_aim"][
            "description"
        ]
    )
    assert description.endswith(
        "[Read the canonical specification](https://github.com/esther-poniatowski/gnomon/"
        "blob/main/docs/specification/question-task.md)."
    )


def test_packaged_documentation_matches_the_specification_notes() -> None:
    packaged = schemas.load_documentation_registry()
    live = {
        kind: schemas.live_documentation_notes(
            kind, schemas.load_base(kind), schemas.vocabulary_options(kind)
        )
        for kind in KINDS
    }

    assert packaged == live


def test_contract_guidance_does_not_require_a_documentation_checkout(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """An installed package retains links without a local Gnomon documentation tree."""
    monkeypatch.setattr(schemas, "DOCS", tmp_path / "absent")
    contract = schemas.contract(
        "question",
        schemas.load_base("question"),
        schemas.vocabulary_options("question"),
    )

    description = contract["properties"]["task"]["properties"]["epistemic_aim"]["description"]
    assert "github.com/esther-poniatowski/gnomon" in description


@pytest.mark.parametrize("kind", KINDS)
def test_each_documented_field_links_only_its_canonical_specification(
    kind: str,
) -> None:
    """Every schema field with a specification exposes its target, without false field links."""
    base, options = schemas.load_base(kind), schemas.vocabulary_options(kind)
    paths = flatten(yaml.safe_load(schemas.render_template(kind, base, options)))
    expected = documentation_notes(kind, paths, schemas.schema_field_paths(base))
    descriptions: dict[str, str] = {}

    def collect(node: Mapping[str, Any], prefix: str = "") -> None:
        for name, child in (node.get("properties") or {}).items():
            path = f"{prefix}.{name}" if prefix else str(name)
            if isinstance(child.get("description"), str):
                descriptions[path] = child["description"]
            collect(child, path)
            items = child.get("items")
            if isinstance(items, Mapping):
                collect(items, f"{path}[]")

    collect(schemas.contract(kind, base, options))
    marker = "[Read the canonical specification]("
    found = {path for path, description in descriptions.items() if marker in description}

    assert found == set(expected)
    for path, note in expected.items():
        assert documentation_target(note) in descriptions[path]


@pytest.mark.parametrize("kind", KINDS)
def test_each_identifier_example_satisfies_its_published_pattern(kind: str) -> None:
    """Form guidance must not present an unfilled template placeholder as valid input."""
    contract = schemas.contract(kind, schemas.load_base(kind), schemas.vocabulary_options(kind))
    identifier = contract["properties"].get("id")
    if identifier is None:
        return

    assert all(re.fullmatch(identifier["pattern"], example) for example in identifier["examples"])


def test_question_contract_publishes_local_aim_requirements_as_form_rules() -> None:
    """A form derives aim-dependent question fields from Gnomon's requirement registry."""
    contract = schemas.contract(
        "question",
        schemas.load_base("question"),
        schemas.vocabulary_options("question"),
    )

    assert contract["x-rules"] == [
        {
            "check": "required-when",
            "field": "task.required_accuracy.outputs_to_match",
            "when": {"field": "task.epistemic_aim", "equals": "prediction"},
        },
        {
            "check": "required-when",
            "field": "task.requested_relation",
            "when": {"field": "task.epistemic_aim", "equals": "explanation"},
        },
        {
            "check": "required-when",
            "field": "task.modal_strength",
            "when": {"field": "task.epistemic_aim", "equals": "modal-knowledge"},
        },
        {
            "check": "required-when",
            "field": "task.proof_obligations",
            "when": {"field": "task.epistemic_aim", "equals": "modal-knowledge"},
        },
        {
            "check": "required-when",
            "field": "task.explicandum",
            "when": {"field": "task.epistemic_aim", "equals": "explication"},
        },
    ]


def collection_kind_defects(schema: Mapping[str, Any]) -> list[str]:
    """Return collection fields that declare a scalar form control."""
    found: list[str] = []

    def walk(node: Mapping[str, Any], path: str) -> None:
        declared_types = node.get("type") or []
        types = {declared_types} if isinstance(declared_types, str) else set(declared_types)
        value_types = types - {"null"}
        if (
            value_types
            and value_types <= {"array", "object"}
            and node.get("x-kind") in SCALAR_FORM_KINDS
        ):
            found.append(path)
        for key, child in (node.get("properties") or {}).items():
            walk(child, f"{path}.{key}" if path else key)
        for key in ("items", "additionalProperties"):
            child = node.get(key)
            if isinstance(child, Mapping):
                walk(child, f"{path}[]")

    walk(schema, "")
    return found


def test_collection_kind_check_rejects_a_scalar_control() -> None:
    """The collection-kind check detects a scalar control on an array."""
    planted = {"properties": {"members": {"type": "array", "x-kind": "label"}}}

    assert collection_kind_defects(planted) == ["members"]


@pytest.mark.parametrize("kind", KINDS)
def test_collection_fields_do_not_declare_scalar_controls(kind: str) -> None:
    """A collection control owns its entries; a scalar control belongs on the item schema."""
    assert not collection_kind_defects(schemas.load_base(kind))


@pytest.mark.parametrize("kind", KINDS)
def test_every_field_has_canonical_form_metadata(kind: str) -> None:
    """Every field supplies guidance and enough schema data to select an interaction."""
    assert not form_metadata_defects(schemas.load_base(kind))


def test_no_description_runs_the_gloss_of_its_row_into_the_content() -> None:
    """A row of a specification note may gloss its name, "Title — gloss", before its content. A
    description that copies both separates them, since "the attitude taken toward the answer
    entertained · hypothesized" reads the gloss and the values as one phrase."""
    # pylint: disable=import-outside-toplevel
    from gnomon.fieldindex import _schema_fields
    from gnomon.specnotes import DOCS  # pylint: disable=import-outside-toplevel

    glosses = {
        line.split("|")[1].split(" — ", 1)[1].strip()
        for note in (DOCS / "specification").glob("*.md")
        for line in note.read_text(encoding="utf-8").splitlines()
        if line.startswith("| ") and " — " in line.split("|")[1]
    }
    found = [
        (kind, path)
        for kind in KINDS
        for path, node in _schema_fields(schemas.load_base(kind))
        for gloss in glosses
        if re.match(re.escape(gloss) + r" [^(]", str(node.get("description") or ""))
    ]
    assert glosses and not found, found


@pytest.mark.parametrize("kind", KINDS)
def test_every_admitted_value_carries_a_gloss(kind: str) -> None:
    """The template lists each admitted value with its gloss, so that a value can be chosen from
    the template line alone; a value without a gloss leaves the reader to find its definition.
    """
    unglossed = [
        f"{field}: {value}"
        for field, values in schemas.vocabulary_options(kind).items()
        for value, gloss in values
        if not gloss.strip()
    ]
    assert not unglossed, unglossed


@pytest.mark.parametrize("kind", KINDS)
def test_no_gloss_holds_a_separator_of_the_template_comment(kind: str) -> None:
    """A template comment separates the values by `|` and the guidance by `;`, so a gloss holding
    either would split its value in two."""
    found = [
        f"{field}: {value}"
        for field, values in schemas.vocabulary_options(kind).items()
        for value, gloss in values
        if "|" in gloss or ";" in gloss
    ]
    assert not found, found


@pytest.mark.parametrize("kind", KINDS)
def test_the_base_schema_and_the_contract_are_valid(kind: str) -> None:
    Draft202012Validator.check_schema(schemas.load_base(kind))
    Draft202012Validator.check_schema(
        yaml.safe_load(schemas.contract_path(kind).read_text(encoding="utf-8"))
    )


MERGE_TAG = "tag:yaml.org,2002:merge"
SCHEMA_FILES = sorted(
    path
    for path in schemas.contract_path(KINDS[0]).parent.rglob("*")
    if path.suffix in {".yml", ".yaml"}
)


def merge_keys(node: yaml.Node) -> list[int]:
    """Return the line of each merge key `<<` in a composed YAML node, counted from one."""
    found: list[int] = []
    if isinstance(node, yaml.MappingNode):
        for key, value in node.value:
            if key.tag == MERGE_TAG:
                found.append(key.start_mark.line + 1)
            found += merge_keys(value)
    elif isinstance(node, yaml.SequenceNode):
        for item in node.value:
            found += merge_keys(item)
    return found


@pytest.mark.parametrize("path", SCHEMA_FILES, ids=lambda path: path.name)
def test_no_packaged_schema_holds_a_merge_key(path: Path) -> None:
    # A YAML 1.2 reader, such as Ekphrasis, takes `<<` as an ordinary key, and Kleisis rejects it.
    assert not merge_keys(yaml.compose(path.read_text(encoding="utf-8"))), path


def enums(node: Mapping[str, Any], path: str = "") -> dict[str, list[Any]]:
    """Return every vocabulary that a contract writes, keyed by the path of its field."""
    found = {path: list(node["enum"])} if "enum" in node else {}
    for key, child in (node.get("properties") or {}).items():
        found.update(enums(child, f"{path}.{key}" if path else key))
    for key in ("items", "additionalProperties"):
        if isinstance(node.get(key), Mapping):
            found.update(enums(node[key], f"{path}[]"))
    return found


@pytest.mark.parametrize("kind", KINDS)
def test_each_vocabulary_of_the_registry_is_bound_by_a_field_of_its_schema(
    kind: str,
) -> None:
    """A vocabulary that no field binds is checked nowhere, since a field selects its vocabulary by
    path."""
    record_type = schemas.load_base(kind)["properties"]["type"]["x-template"]
    bound = set(schemas.vocabulary_paths(schemas.load_base(kind)).values())
    shared = set(schemas.shared_vocabulary_options())
    assert set(schemas.vocabulary_options(record_type)) - shared - bound == set()


def test_each_shared_vocabulary_is_bound_by_a_schema() -> None:
    """A shared vocabulary must govern at least one field of the published record types."""
    bound = {
        vocabulary
        for kind in KINDS
        for vocabulary in schemas.vocabulary_paths(schemas.load_base(kind)).values()
    }
    assert set(schemas.shared_vocabulary_options()) <= bound


@pytest.mark.parametrize("kind", KINDS)
def test_each_vocabulary_of_the_contract_is_its_registry_entry(kind: str) -> None:
    """Every field that names a registry key receives exactly the values of that key, and null."""
    base = schemas.load_base(kind)
    record_type = base["properties"]["type"]["x-template"]
    options = schemas.vocabulary_options(record_type)
    linked: dict[str, list[Any]] = {}

    def walk(node: Mapping[str, Any], path: str) -> None:
        if node.get("x-vocabulary"):
            linked[path] = [value for value, _ in options[node["x-vocabulary"]]] + [None]
        for key, child in (node.get("properties") or {}).items():
            walk(child, f"{path}.{key}" if path else key)
        for key in ("items", "additionalProperties"):
            if isinstance(node.get(key), Mapping):
                walk(node[key], f"{path}[]")

    walk(base, "")
    contract = yaml.safe_load(schemas.contract_path(kind).read_text(encoding="utf-8"))
    assert enums(contract) == linked
    assert contract["properties"]["_schema"]["const"] == schemas.identifier(kind, base["x-version"])


def test_each_published_record_contract_resolves_through_the_registry() -> None:
    """The registry closes each record contract over its base without a template or prose note."""
    published = yaml.safe_load((ROOT / "specs" / "schema-registry.yml").read_text(encoding="utf-8"))
    mappings = {
        logical_id: path
        for logical_id, path in published["schemas"].items()
        if logical_id.startswith("gnomon:") and not logical_id.startswith("gnomon:view.")
    }
    expected = {
        schemas.identifier(kind, int(schemas.load_base(kind).get("x-version", 1))) for kind in KINDS
    }
    assert expected <= set(mappings)
    assert set(mappings) <= set(published["exports"])
    assert len(set(mappings.values())) == len(mappings)

    for logical_id, relative_path in mappings.items():
        contract_file = ROOT / relative_path
        assert contract_file.is_file(), relative_path
        contract = yaml.safe_load(contract_file.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(contract)
        assert contract["properties"]["_schema"]["const"] == logical_id
        assert published["resources"][contract["$id"]] == relative_path
        base_id = contract["allOf"][0]["$ref"]
        base_file = ROOT / published["resources"][base_id]
        assert base_file.is_file(), base_id
        base = yaml.safe_load(base_file.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(base)
        assert base["$id"] == base_id


ROOT = schemas.DATA.parents[2]
RECORDS = sorted(
    (path, record)
    for path in (ROOT / "examples").glob("*/*.yml")
    if isinstance(record := yaml.safe_load(path.read_text(encoding="utf-8")), dict)
    and record.get("type") in schemas.record_kinds()
)


CASES = [
    pytest.param(path, record, id=f"{path.parent.name}/{path.name}") for path, record in RECORDS
]


@pytest.mark.parametrize("path, record", CASES)
def test_every_worked_record_follows_its_contract(path: Any, record: dict[str, Any]) -> None:
    assert record.get("_schema"), f"{path} names no contract"
    assert schemas.record_errors(record) == []


def test_a_record_that_breaks_its_contract_is_reported() -> None:
    record = {
        "_schema": "gnomon:problem@3",
        "type": "problem",
        "id": "prob.a.b",
        "status": "posed",
    }
    assert schemas.record_errors(record) == []
    assert schemas.record_errors({**record, "status": "pending"}) == [
        (
            "status: pending is not admitted; the admitted values are posed, refined, solved,"
            " dissolved, abandoned"
        )
    ]
    assert schemas.record_errors({**record, "type": "question"}) == ["type: must be problem"]
    assert schemas.record_errors({**record, "statement": 3}) == [
        "statement: holds a number where the contract admits text"
    ]
    assert schemas.record_errors({"type": "problem"}) == ["_schema: the record names no contract"]
    assert schemas.record_errors({**record, "_schema": "gnomon:problem@9"}) == [
        "_schema: gnomon:problem@9 is no contract of gnomon"
    ]
    assert schemas.record_errors({**record, "maturity": {"statement": "banana"}}) == [
        (
            "maturity.statement: banana is not admitted; the admitted values are open,"
            " provisional, stabilized"
        )
    ]


def test_a_question_can_point_to_sources_without_an_artificial_problem() -> None:
    """Question-led adoption records external provenance without a problem record."""
    question = {
        "_schema": "gnomon:question@3",
        "type": "question",
        "id": "quest.adoption.active-question",
        "status": "posed",
        "sources": ["notes/active-question.md", "data/run-17.zarr"],
    }

    assert "addresses" not in question
    assert schemas.record_errors(question) == []
    retained = {**question, "_schema": "gnomon:question@2"}
    assert any("sources is no field here" in error for error in schemas.record_errors(retained))


def test_a_problem_can_point_to_each_external_source_kind() -> None:
    """Problem-led adoption points outward without importing the source content."""
    problem = {
        "_schema": "gnomon:problem@3",
        "type": "problem",
        "id": "prob.adoption.active-problem",
        "status": "posed",
        "sources": [
            "notes/open-demand.md",
            "doi:10.example/1234",
            "models/baseline.pkl",
            "data/run-17.zarr",
        ],
    }

    assert schemas.record_errors(problem) == []
    current = schemas.load_base("problem")["properties"]["sources"]["description"]
    retained = yaml.safe_load(
        (schemas.COMPATIBILITY / "problem.v2.base.schema.yml").read_text(encoding="utf-8")
    )["properties"]["sources"]["description"]
    assert "existing material" in current
    assert "existing material" not in retained


@pytest.mark.parametrize(
    "kind,record",
    [
        (
            "model",
            {
                "type": "model",
                "id": "mod.adoption.baseline",
                "status": "provisional",
            },
        ),
        (
            "answer",
            {
                "type": "answer",
                "id": "ans.adoption.candidate",
                "answers": "quest.adoption.active-question",
            },
        ),
    ],
)
def test_a_promoted_model_or_answer_retains_sources_only_under_version_3(
    kind: str, record: dict[str, object]
) -> None:
    """Current contracts admit adoption origins while retained contracts keep version 2 closed."""
    sources = ["notes/candidate.md#selected-unit", "doi:10.example/1234"]
    current = {**record, "_schema": f"gnomon:{kind}@3", "sources": sources}
    retained = {**current, "_schema": f"gnomon:{kind}@2"}

    assert schemas.record_errors(current) == []
    assert any("sources is no field here" in error for error in schemas.record_errors(retained))


@pytest.mark.parametrize("sources", [[], [None], [""]])
@pytest.mark.parametrize("kind", ["model", "answer"])
def test_a_present_model_or_answer_source_list_contains_a_pointer(
    kind: str, sources: list[object]
) -> None:
    """An optional source list may be absent, but a present list contains a non-empty pointer."""
    record: dict[str, object] = {
        "_schema": f"gnomon:{kind}@3",
        "type": kind,
        "id": f"{'mod' if kind == 'model' else 'ans'}.adoption.candidate",
        "sources": sources,
    }

    assert schemas.record_errors(record)


def test_a_record_under_a_retained_contract_keeps_its_previous_validation() -> None:
    """A version-1 maturity value remains readable even though version 2 closes the vocabulary."""
    record = {
        "_schema": "gnomon:problem@1",
        "type": "problem",
        "id": "prob.a.b",
        "status": "posed",
        "maturity": {"statement": "banana"},
    }
    assert schemas.record_errors(record) == []


def test_comparison_rules_and_act_names_are_authored_only_under_itinerary_version_3() -> None:
    """The current itinerary declares a comparison; retained versions keep their prior shape."""
    appraisal = {
        "id": "first-ready-acts",
        "question": "quest.pendulum.explain-growth",
        "route": "selection",
        "rule": "ordinal-dominance",
        "criteria": [
            {
                "id": "feasibility",
                "question": "How likely is completion with the available means?",
                "scale": ["unavailable", "uncertain", "feasible"],
                "preferred": "higher",
            },
            {
                "id": "cost",
                "question": "What effort does the act require?",
                "scale": ["low", "medium", "high"],
                "preferred": "lower",
            },
        ],
        "acts": [
            {
                "id": "explain-term",
                "activity": "explication",
                "acts_on": "definiteness",
                "available_means": ["the source passage that introduces the term"],
                "judgments": [
                    {
                        "criterion": "feasibility",
                        "value": "feasible",
                        "basis": "The source passage and contrasting cases are available.",
                    },
                    {
                        "criterion": "cost",
                        "value": "low",
                        "basis": "No new data or instrument is required.",
                    },
                ],
            }
        ],
    }
    current = {
        "_schema": "gnomon:itinerary@3",
        "type": "itinerary",
        "id": "itin.pendulum.explain-growth",
        "act_appraisals": [appraisal],
    }
    retained_v2 = {**current, "_schema": "gnomon:itinerary@2"}
    retained_v1 = {**current, "_schema": "gnomon:itinerary@1"}

    assert schemas.record_errors(current) == []
    assert any("rule is no field here" in error for error in schemas.record_errors(retained_v2))
    assert any(
        "act_appraisals is no field here" in error for error in schemas.record_errors(retained_v1)
    )


def test_a_key_that_the_contract_does_not_declare_is_reported() -> None:
    """A misspelled key would otherwise pass as an unknown field, at the root and at any depth."""
    record = {"_schema": "gnomon:concept@1", "type": "concept", "id": "concept.a.b"}
    assert schemas.record_errors({**record, "glos": "x"})[0].startswith(
        "(record): glos is no field here; the fields admitted are title, id,"
    )
    nested = {**record, "confusions": [{"with": "fixed point"}]}
    assert schemas.record_errors(nested)[0].startswith("confusions[0]: with is no field here")
    assert schemas.record_errors({**record, "confusions": [{"other": "fixed point"}]}) == []
