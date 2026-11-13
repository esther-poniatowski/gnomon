"""Provisioning of a relocatable schema closure for an arbitrary Obsidian vault."""

from pathlib import Path, PurePosixPath
from typing import cast

import pytest
import yaml
from typer.testing import CliRunner

from gnomon import data_path
from gnomon.cli import app
from gnomon.provisioning import ProvisioningError, provision_schemas

ROOT = Path(__file__).parents[2]


def _mapping(path: Path) -> dict[str, object]:
    """Read one YAML mapping used by the provisioning assertions."""
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def _contract_editability_defects(
    contracts: dict[str, dict[str, object]],
) -> list[tuple[str, str]]:
    """Return contracts whose root editability conflicts with their record class."""
    defects: list[tuple[str, str]] = []
    for identity, contract in contracts.items():
        if identity.startswith("gnomon:view.") and contract.get("readOnly") is not True:
            defects.append((identity, "generated view is editable"))
        elif (
            identity.startswith("gnomon:")
            and not identity.startswith("gnomon:view.")
            and contract.get("readOnly") is True
        ):
            defects.append((identity, "authored record is read-only"))
    return defects


def test_contract_editability_check_rejects_both_reversed_classes() -> None:
    """The boundary check detects an editable view and a locked authored record."""
    contracts: dict[str, dict[str, object]] = {
        "gnomon:view.example@1": {},
        "gnomon:example@1": {"readOnly": True},
    }

    assert _contract_editability_defects(contracts) == [
        ("gnomon:view.example@1", "generated view is editable"),
        ("gnomon:example@1", "authored record is read-only"),
    ]


def test_provisioning_writes_a_complete_relocatable_registry(tmp_path: Path) -> None:
    """Every mapped contract and resource exists below the vault and declares its mapping key."""
    vault = tmp_path / "research-vault"
    vault.mkdir()

    result = provision_schemas(vault)

    registry_path = vault / result.registry
    registry = _mapping(registry_path)
    assert registry["_schema"] == "kleisis:schema-registry@2"
    assert isinstance(registry["schemas"], dict)
    assert isinstance(registry["resources"], dict)
    schemas = cast(dict[str, str], registry["schemas"])
    resources = cast(dict[str, str], registry["resources"])
    assert schemas["gnomon:problem@3"].startswith(".gnomon/schemas/")
    assert schemas["ekthesis:export@1"].startswith(".gnomon/schemas/")
    assert result.schema_count >= len(schemas)

    contracts: dict[str, dict[str, object]] = {}
    for contract, relative in schemas.items():
        path = PurePosixPath(relative)
        assert not path.is_absolute() and ".." not in path.parts
        schema = _mapping(vault / path)
        contracts[contract] = schema
        properties = schema.get("properties")
        assert isinstance(properties, dict)
        assert properties["_schema"]["const"] == contract
    assert not _contract_editability_defects(contracts)
    assert not (vault / ".gnomon/templates").exists()
    for identity, relative in resources.items():
        path = PurePosixPath(relative)
        assert not path.is_absolute() and ".." not in path.parts
        assert _mapping(vault / path)["$id"] == identity

    text = registry_path.read_text(encoding="utf-8")
    assert "src/gnomon" not in text
    assert ".schema-resources" not in text


def test_provisioning_accepts_custom_vault_relative_locations(tmp_path: Path) -> None:
    """Neither the registry nor the schema-resource directory has a fixed hidden-folder name."""
    vault = tmp_path / "vault"
    vault.mkdir()

    result = provision_schemas(
        vault,
        registry="configuration/forms.yml",
        schema_directory="shared/contracts",
    )

    assert result.registry == PurePosixPath("configuration/forms.yml")
    registry = _mapping(vault / result.registry)
    sections = (
        cast(dict[str, str], registry["schemas"]),
        cast(dict[str, str], registry["resources"]),
    )
    assert all(
        path.startswith("shared/contracts/") for section in sections for path in section.values()
    )


def test_packaged_dependency_matches_the_materialized_pinned_contract() -> None:
    """The distributable Ekthesis contract is the exact contract materialized by Kleisis."""
    materialized = ROOT / ".schema-resources/ekthesis/src/ekthesis/data/schemas/export.schema.yaml"
    packaged = data_path() / "resources/ekthesis-export.schema.yaml"

    assert materialized.is_file(), "run `python -m kleisis materialize --root .` first"
    assert packaged.read_bytes() == materialized.read_bytes()


@pytest.mark.parametrize(
    ("registry", "schemas"),
    [
        ("../registry.yml", ".gnomon/schemas"),
        ("/registry.yml", ".gnomon/schemas"),
        ("registry.yml", "../schemas"),
        ("registry.yml", r".gnomon\schemas"),
    ],
)
def test_provisioning_rejects_locations_outside_the_vault(
    tmp_path: Path, registry: str, schemas: str
) -> None:
    """A configured output cannot escape the vault or use host-dependent separators."""
    with pytest.raises(ProvisioningError):
        provision_schemas(tmp_path, registry=registry, schema_directory=schemas)


def test_provisioning_rejects_a_symlink_that_leaves_the_vault(tmp_path: Path) -> None:
    """A lexically local resource path cannot write through a link to another directory."""
    outside = tmp_path / "outside"
    outside.mkdir()
    vault = tmp_path / "vault"
    vault.mkdir()
    (vault / ".gnomon").symlink_to(outside, target_is_directory=True)

    with pytest.raises(ProvisioningError, match="leaves the vault through a symlink"):
        provision_schemas(vault)

    assert not list(outside.iterdir())


def test_provisioning_refuses_a_changed_target_before_writing(tmp_path: Path) -> None:
    """A conflict leaves every still-absent output absent until replacement is explicit."""
    conflict = tmp_path / ".gnomon/schemas/gnomon/problem.contract.schema.yml"
    conflict.parent.mkdir(parents=True)
    conflict.write_text("user content\n", encoding="utf-8")

    with pytest.raises(ProvisioningError, match="existing files differ"):
        provision_schemas(tmp_path)

    assert conflict.read_text(encoding="utf-8") == "user content\n"
    assert not (tmp_path / ".gnomon/schema-registry.yml").exists()

    provision_schemas(tmp_path, force=True)
    assert conflict.read_text(encoding="utf-8") != "user content\n"


def test_provisioning_rejects_an_incomplete_installed_closure(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """An absolute reference without its identified resource makes provisioning fail."""
    package_data = tmp_path / "package-data"
    schemas = package_data / "schemas"
    resources = package_data / "resources"
    schemas.mkdir(parents=True)
    resources.mkdir()
    (schemas / "record.schema.yml").write_text(
        "$id: https://example.test/record.schema.yml\n"
        "properties:\n"
        "  _schema: {const: example:record@1}\n"
        "  field: {$ref: https://example.test/missing.schema.yml}\n",
        encoding="utf-8",
    )
    (resources / "ekthesis-export.schema.yaml").write_text(
        "$id: export.schema.yaml\nproperties:\n  _schema: {const: ekthesis:export@1}\n",
        encoding="utf-8",
    )
    monkeypatch.setattr("gnomon.provisioning.data_path", lambda: package_data)
    vault = tmp_path / "vault"
    vault.mkdir()

    with pytest.raises(ProvisioningError, match="leaves absolute references unresolved"):
        provision_schemas(vault)

    assert not (vault / ".gnomon").exists()


def test_setup_command_names_the_ekphrasis_setting(tmp_path: Path) -> None:
    """The successful command ends with the exact vault-relative value needed by Ekphrasis."""
    result = CliRunner().invoke(app, ["setup", str(tmp_path)])

    assert result.exit_code == 0
    assert "schema files available" in result.stdout
    assert result.stdout.endswith("Set Ekphrasis Schema registry to: .gnomon/schema-registry.yml\n")
