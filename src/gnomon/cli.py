"""
Command-line interface for the `gnomon` package.

Defines commands available via `python -m gnomon` or `gnomon` if installed as a script.

Commands
--------
info : Display diagnostic information.
setup : Install Gnomon's schema registry and resources in an Obsidian vault.
init : Create an inquiry folder, with sparse records in the order of filling.
register : Add an existing Gnomon record to its inquiry index.
validate : Validate each record against the schema of its type.
check : Run every check on the records of a directory tree.
explain : Explain the finding of one rule and the state that repairs it.
schemas : Write the contract of each record type and its template.
migrate : Preview record migrations to current published contracts.
status : List the open conditions of the questions of a workspace.
vocabulary : Collect the symbols and operators of one problem into a table.
itinerary : Check every itinerary of one problem against the activity and product-type registries.
tree : Print the question tree of a project, from its problems to the assessments of its answers.
source-state : Print the identifier of the authored records of a workspace.
views : Write the views of the state of an inquiry as YAML records.
export : Write the research units and their relations in the contract of `ekthesis`.
"""

# Each command imports what it runs, so --help stays fast. This module is the Typer command
# registry.
# pylint: disable=import-outside-toplevel,too-many-lines

import json
from collections.abc import Mapping
from dataclasses import dataclass
from enum import Enum
from pathlib import Path, PurePosixPath
from typing import TYPE_CHECKING, Annotated, Any

import typer
import yaml

from . import __version__
from . import info as pkg_info
from .findings import RULES, Finding, Rule, close_match_hint
from .history import git_states
from .itineraries import itinerary_problems
from .sarif import Located, sarif_log
from .views import question_tree, render_tree
from .vocabulary import load_problem, render_yaml

if TYPE_CHECKING:
    from .answerability import Diagnosis
    from .check import FutureWork, Workspace

app = typer.Typer(add_completion=False, no_args_is_help=True, invoke_without_command=True)


class StartKind(str, Enum):
    """The record from which an initialized inquiry starts."""

    PROBLEM = "problem"
    QUESTION = "question"


class ViewResultFormat(str, Enum):
    """Presentation of the files written by ``gnomon views`` on standard output."""

    TEXT = "text"
    JSON = "json"


def _starting_kind(folder: Path, requested: StartKind | None) -> StartKind:
    """Return an explicit starting kind or preserve an existing question-only route."""
    if requested is not None:
        return requested
    if (folder / "question.yml").exists() and not (folder / "problem.yml").exists():
        return StartKind.QUESTION
    return StartKind.PROBLEM


@app.command("info")
def cli_info() -> None:
    """Display version and platform diagnostics."""
    typer.echo(pkg_info())


@app.command("setup")
def cli_setup(
    vault: Annotated[
        Path,
        typer.Argument(
            help="Existing Obsidian vault that will receive the schema registry and resources."
        ),
    ],
    registry: Annotated[
        str,
        typer.Option("--registry", help="Vault-relative path of the generated schema registry."),
    ] = ".gnomon/schema-registry.yml",
    schema_directory: Annotated[
        str,
        typer.Option(
            "--schema-directory",
            help="Vault-relative directory that will receive every schema resource.",
        ),
    ] = ".gnomon/schemas",
    force: Annotated[
        bool,
        typer.Option(
            "--force",
            help="Replace files at the selected generated paths when their content differs.",
        ),
    ] = False,
) -> None:
    """Install a relocatable schema registry and its complete resources in a vault."""
    from .provisioning import ProvisioningError, provision_schemas

    try:
        result = provision_schemas(
            vault,
            registry=registry,
            schema_directory=schema_directory,
            force=force,
        )
    except (OSError, ProvisioningError) as error:
        typer.echo(f"setup failed: {error}", err=True)
        raise typer.Exit(code=1) from error
    typer.echo(
        f"{result.schema_count} schema files available; {result.written_count} files written, "
        f"{result.unchanged_count} unchanged"
    )
    typer.echo(f"Set Ekphrasis Schema registry to: {result.registry.as_posix()}")


@app.command("init")
# Typer exposes each independent command option as a parameter of the command function.
# pylint: disable=too-many-arguments,too-many-positional-arguments,too-many-locals,too-many-branches
def cli_init(
    directory: str = typer.Argument(..., help="Inquiry folder, created when it does not exist."),
    start_with: StartKind | None = typer.Option(
        None,
        "--start-with",
        help="Create the starting record for a problem or a question. A new folder defaults to "
        "a problem; an existing question-only folder keeps its question start.",
    ),
    with_kinds: list[str] = typer.Option(
        [],
        "--with",
        "-w",
        help="A further record kind to scaffold, such as question, target-system, phenomenon, "
        "background, operators, model, binding, key, answer, assessment, concept, design or "
        "derivation; repeat the option for several.",
    ),
    full_template: bool = typer.Option(
        False,
        "--full-template",
        help="Write each complete commented template instead of a sparse authored record.",
    ),
    force: bool = typer.Option(
        False,
        "--force",
        help="Preserve and replace the records and index that already exist.",
    ),
    dry_run: bool = typer.Option(
        False,
        "--dry-run",
        help="List the files that would change without writing them.",
    ),
    assume_yes: bool = typer.Option(
        False,
        "--yes",
        "-y",
        help="Confirm preservation and replacement without prompting.",
    ),
) -> None:
    """Create an inquiry folder, with sparse records in the order of filling.

    The folder receives the itinerary, the selected problem or question, the further kinds that
    ``--with`` names, and an index listing them in the order of filling. A new folder defaults to a
    problem. An existing folder that holds a question but no problem retains that starting kind
    when ``--start-with`` is omitted. In a folder that already holds records, only the missing
    records are written, and each is registered in the existing index. The default record omits
    optional branches; ``--full-template`` writes the complete commented template for source-based
    authoring. With ``--force``, every existing target is preserved under ``.gnomon-backup`` before
    its replacement; an existing backup stops the command. ``--dry-run`` lists the complete write
    set without changing the folder. The command exits with status 1 when a kind has no template
    or a safe backup cannot be made.
    """
    from .scaffold import STARTING_KINDS, apply_scaffold, plan_scaffold

    folder = Path(directory)
    effective_start = _starting_kind(folder, start_with)
    try:
        plan = plan_scaffold(
            folder,
            [*STARTING_KINDS[effective_start.value], *with_kinds],
            force,
            full_template,
        )
        if dry_run:
            backups = dict(plan.backups)
            for path in plan.affected:
                if path in backups:
                    typer.echo(f"{path}: would overwrite; would preserve as {backups[path]}")
                else:
                    typer.echo(f"{path}: would write")
            if not plan.affected:
                typer.echo("no files would change")
            return
        if plan.overwritten and not assume_yes:
            typer.confirm(
                f"Preserve and overwrite {len(plan.overwritten)} existing files?",
                abort=True,
            )
        outcome = apply_scaffold(plan)
    except ValueError as error:
        typer.echo(str(error), err=True)
        raise typer.Exit(code=1) from error
    for source, backup in outcome.backups:
        typer.echo(f"{source}: preserved as {backup}")
    for path in outcome.written:
        typer.echo(f"{path}: written")
    typer.echo(f"{outcome.index}: {outcome.index_state}")
    if outcome.kept:
        typer.echo(f"{len(outcome.kept)} existing files kept")
    written_kinds = {path.stem for path in outcome.written}
    if effective_start is StartKind.QUESTION and written_kinds & {
        "target-system",
        "phenomenon",
    }:
        typer.echo(
            f"Fill the new subject records in the order of {outcome.index}, then update "
            f"{folder / 'question.yml'} to name them. Run: gnomon check {directory}"
        )
    elif effective_start is StartKind.QUESTION and "question" in written_kinds:
        typer.echo(
            f"Fill {folder / 'question.yml'} first, then record subsequent acts in "
            f"{folder / 'itinerary.yml'}. Run: gnomon check {directory}"
        )
    elif effective_start is StartKind.QUESTION and outcome.written:
        typer.echo(
            f"Fill the new records in the order of {outcome.index}, then record subsequent acts "
            f"in {folder / 'itinerary.yml'}. Run: gnomon check {directory}"
        )
    else:
        typer.echo(
            f"Fill the records in the order of {Path(directory) / '_index.md'}, then run: "
            f"gnomon check {directory}"
        )


@app.command("register")
def cli_register(
    record: Annotated[
        Path,
        typer.Argument(help="Existing Gnomon YAML record to add to the _index.md of its folder."),
    ],
) -> None:
    """Add an existing Gnomon record to its inquiry index."""
    from .indexing import register_record

    try:
        result = register_record(record)
    except (OSError, ValueError) as error:
        typer.echo(f"registration failed: {error}", err=True)
        raise typer.Exit(code=1) from error
    typer.echo(f"{result.index}: {result.state}")


@app.command("validate")
def cli_validate(
    paths: list[str] = typer.Argument(..., help="Record files or directories to validate."),
) -> None:
    """Validate each record against the contract that it names, skipping the kinds that have no
    schema and the templates not yet started, whose identifier still holds a placeholder.
    """
    from .identifiers import PLACEHOLDER_SEGMENT
    from .schemas import record_errors, record_kinds

    files: list[Path] = []
    for given in map(Path, paths):
        if not given.exists():
            typer.echo(f"no such file or directory: {given}", err=True)
            raise typer.Exit(code=1)
        files += sorted(given.rglob("*.yml")) if given.is_dir() else [given]
    known, failed, checked, unfilled = record_kinds(), 0, 0, 0
    for path in files:
        record = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not isinstance(record, dict) or record.get("type") not in known:
            continue
        if PLACEHOLDER_SEGMENT.search(str(record.get("id", ""))):
            unfilled += 1
            continue
        checked += 1
        for message in record_errors(record):
            failed += 1
            typer.echo(f"{path}: {message}")
    typer.echo(
        f"{checked} records checked, {failed} errors found, {unfilled} templates not yet filled"
    )
    raise typer.Exit(code=1 if failed else 0)


def _directory(directory: str) -> Path:
    """Return the directory that a command reads, or exit with status 1 when there is none."""
    source = Path(directory)
    if not source.is_dir():
        typer.echo(f"no such directory: {source}", err=True)
        raise typer.Exit(code=1)
    return source


def _emit(text: str, output: Path | None, what: str) -> None:
    """Write ``text`` to ``output``, creating its folders, or to standard output when it is None.

    The command exits with status 2 when the file cannot be written; ``what`` names the file in the
    message, such as ``report`` or ``log``.
    """
    if output is None:
        typer.echo(text, nl=False)
        return
    try:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(text, encoding="utf-8")
    except OSError as error:
        typer.echo(f"cannot write the {what} {output}: {error}", err=True)
        raise typer.Exit(code=2) from error


def _diagnosis(source: Path) -> "tuple[Workspace, Diagnosis]":
    """Return the workspace of a directory and the merged diagnosis of its problems.

    The files that cannot be read are listed on standard error.
    """
    from .answerability import diagnose, merge
    from .check import load_workspace

    workspace = load_workspace(source)
    for line in workspace.failures:
        typer.echo(line, err=True)
    diagnosis = merge(
        [diagnose(workspace.by_id, local=problem.records) for problem in workspace.problems]
    )
    return workspace, diagnosis


class CheckFormat(str, Enum):
    """The forms in which ``gnomon check`` reports its findings."""

    TEXT = "text"
    YAML = "yaml"
    SARIF = "sarif"


@dataclass(frozen=True)
class _CheckPresentation:
    """Output choices and summary text of one check report."""

    source: Path
    output_format: CheckFormat
    summary: str
    scope: str | None


@app.command("check")
def cli_check(
    directory: str = typer.Argument(
        ..., help="Directory of records, read recursively; each folder is one problem."
    ),
    output_format: CheckFormat = typer.Option(
        CheckFormat.TEXT,
        "--format",
        "-f",
        help="text prints one line per finding; yaml writes a stable report; sarif "
        "writes a SARIF 2.1.0 log in the findings profile of Elenchos.",
    ),
    output: Path | None = typer.Option(
        None,
        "--output",
        "-o",
        help="Write the report to this path instead of standard output; missing folders are"
        " created.",
    ),
    scope: str | None = typer.Option(
        None,
        "--scope",
        help="Classify missing content against one named validation scope.",
    ),
) -> None:
    """Run every check on the records of a directory tree.

    Each folder that holds records is checked as one problem, and a reference may reach a record of
    any folder. The text output prints one line per finding, a warning marked as such, and a count.
    A selected scope lists missing content due later as future work instead of a current finding.
    The command exits with status 1 when a finding of level error is reported or a file cannot be
    read, and with status 2 when the report cannot be written; a warning fails no check.
    """
    from .check import check_workspace_result, load_workspace

    source = _directory(directory)
    workspace = load_workspace(source)
    try:
        checked = check_workspace_result(workspace, scope=scope)
    except ValueError as error:
        raise typer.BadParameter(str(error), param_hint="--scope") from error
    found = list(checked.findings)
    errors = [x for x in found if x.finding.rule.level == "error"]
    summary = (
        f"{len(workspace.by_id)} records checked in {len(workspace.problems)} folders,"
        f" {len(errors)} findings, {len(found) - len(errors)} warnings,"
        f" {len(workspace.unfilled)} templates not yet filled"
    )
    if scope is not None:
        summary += f", {len(checked.future_work)} future requirements"
    for line in workspace.failures:
        typer.echo(line, err=True)
    _emit(
        _check_report(
            workspace,
            found,
            checked.future_work,
            _CheckPresentation(source, output_format, summary, scope),
        ),
        output,
        "report",
    )
    if output is not None:
        typer.echo(summary, err=True)
    if errors or workspace.failures:
        raise typer.Exit(code=1)


def _check_report(
    workspace: "Workspace",
    found: list[Located],
    future_work: tuple["FutureWork", ...],
    presentation: _CheckPresentation,
) -> str:
    """Return the report of ``gnomon check`` in the form that the command asks for."""
    from .report import render_yaml_report

    source = presentation.source
    output_format = presentation.output_format
    summary = presentation.summary
    scope = presentation.scope
    if output_format is CheckFormat.TEXT:
        lines = [_finding_line(f"{x.file}: {x.record}", x.finding) + "\n" for x in found]
        lines.extend(
            f"{item.file}: {item.record or item.kind}: future ({item.due_scope}): "
            f"{item.path}: {item.message}\n"
            for item in future_work
        )
        return "".join(lines) + summary + "\n"
    if output_format is CheckFormat.YAML:
        unfilled = [p.relative_to(source).as_posix() for p in workspace.unfilled]
        return render_yaml_report(
            found,
            source.name,
            len(workspace.by_id),
            unfilled,
            scope=scope,
            future_work=future_work,
        )
    stopped = (
        f"{len(workspace.failures)} record files could not be read" if workspace.failures else None
    )
    return (
        json.dumps(
            sarif_log(found, __version__, stopped, scope=scope),
            indent=2,
            ensure_ascii=False,
        )
        + "\n"
    )


def _finding_line(prefix: str, item: Finding) -> str:
    """Return one human-readable finding with its severity and explainable rule identifier."""
    severity = "warning: " if item.rule.level == "warning" else ""
    return f"{prefix}: {severity}{item.rule.id}: {item.text}"


def _explanation(rule: Rule) -> str:
    """Return the explanation of one rule that ``gnomon explain`` prints, one labelled line per
    field of the catalogue."""
    return (
        f"rule: {rule.id}\n"
        f"level: {rule.level}\n"
        f"meaning: {rule.description}\n"
        f"repair: {rule.repair_condition}\n"
        f"documentation: {rule.documentation_target}\n"
    )


@app.command("explain")
def cli_explain(
    rule_id: str | None = typer.Argument(
        None, help="Rule identifier as a finding prints it, such as itinerary/cycle."
    ),
    list_rules: bool = typer.Option(
        False, "--list", help="Print every rule identifier, one per line, instead."
    ),
) -> None:
    """Explain the finding of one rule: what it means, the state that repairs it, and the
    documentation that owns that state.

    The explanation is read from the catalogue of rules, which supplies the same guidance to every
    finding. The command exits with status 2 when the identifier is unknown, and when neither or
    both of an identifier and `--list` are given.
    """
    rules = {rule.id: rule for rule in RULES}
    if list_rules == (rule_id is not None):
        typer.echo("give either one rule identifier or --list", err=True)
        raise typer.Exit(code=2)
    if rule_id is None:
        typer.echo("".join(f"{identifier}\n" for identifier in sorted(rules)), nl=False)
        return
    rule = rules.get(rule_id)
    if rule is None:
        typer.echo(
            f"unknown rule identifier: {rule_id}{close_match_hint(rule_id, rules)}\n"
            "list the known identifiers with: gnomon explain --list",
            err=True,
        )
        raise typer.Exit(code=2)
    typer.echo(_explanation(rule), nl=False)


class StatusFormat(str, Enum):
    """The forms in which ``gnomon status`` reports its diagnosis."""

    TEXT = "text"
    YAML = "yaml"


@app.command("status")
def cli_status(
    directory: str = typer.Argument(..., help="Directory of records, read recursively."),
    output_format: StatusFormat = typer.Option(
        StatusFormat.TEXT,
        "--format",
        "-f",
        help="text prints the open and refuted conditions; yaml writes the full diagnosis.",
    ),
    output: Path | None = typer.Option(
        None,
        "--output",
        "-o",
        help="Write the report to this path instead of standard output.",
    ),
) -> None:
    """List the open conditions of answerability of each question, and the acts that address them.

    The state of each condition is read from the assertions of the question, else from a field that
    shows it, else it is not established. A condition is open when every condition on which it
    depends is established, and an act on it is ready when its required inputs exist unimpeached.
    The command exits with status 1 when a file cannot be read, and 2 when the report cannot be
    written.
    """
    from .answerability import as_document, render_text

    workspace, diagnosis = _diagnosis(_directory(directory))
    if output_format is StatusFormat.YAML:
        text = (
            "# Generated by `gnomon status`. Edit the records, not this file.\n"
            + yaml.safe_dump(as_document(diagnosis), sort_keys=False, allow_unicode=True, width=100)
        )
    else:
        text = render_text(diagnosis)
    _emit(text, output, "report")
    if workspace.failures:
        raise typer.Exit(code=1)


@app.command("vocabulary")
def cli_vocabulary(
    directory: str = typer.Argument(
        ..., help="Directory holding the filled records of one problem."
    ),
    output: str = typer.Option(
        "vocabulary.yml", "--output", "-o", help="Record written inside that directory."
    ),
) -> None:
    """Collect the symbols and operators of one problem into its vocabulary record, a YAML view
    that a renderer displays through the schema ``gnomon:view.vocabulary@3``."""
    source = _directory(directory)
    problem = load_problem(source)
    target = source / output
    target.write_text(render_yaml(problem), encoding="utf-8")
    repeated = problem.collisions()
    typer.echo(
        f"{target}: {len(problem.declarations)} symbols, "
        f"{len(problem.local)} operators of the problem, "
        f"{len(repeated)} symbols reused across records"
    )


class OutputFormat(str, Enum):
    """The forms in which a check reports its findings."""

    TEXT = "text"
    SARIF = "sarif"


def _read_records(
    source: Path, tolerant: bool, pattern: str = "*.yml"
) -> tuple[dict[str, Mapping[str, Any]], dict[str, Path], list[str]]:
    """Return the records of ``source`` keyed by identifier, the file of each, and the read
    failures.

    The files are those that ``pattern`` matches, such as ``**/*.yml`` for a whole tree. A later
    file carrying an identifier already read replaces the earlier one. When ``tolerant`` is
    false, a file that cannot be read or parsed raises its error; otherwise the failure is returned
    as a line naming the file, and the remaining files are read.
    """
    from .check import parse_file

    records: dict[str, Mapping[str, Any]] = {}
    files: dict[str, Path] = {}
    failures: list[str] = []
    for path in sorted(source.glob(pattern)):
        if tolerant:
            record, failure = parse_file(path)
            if failure is not None:
                failures.append(failure)
                continue
        else:
            record = yaml.safe_load(path.read_text(encoding="utf-8"))
        if isinstance(record, Mapping) and "id" in record:
            records[str(record["id"])] = record
            files[str(record["id"])] = path
    return records, files, failures


@app.command("schemas")
def cli_schemas(
    check: bool = typer.Option(
        False,
        "--check",
        help="Report the stale generated files instead of writing them.",
    ),
) -> None:
    """Write the contracts and the templates generated from the base schemas and the vocabulary
    registry, and the field index of the user guide."""
    from .generated import generated_files, stale_files

    if check:
        stale = stale_files()
        for path in stale:
            typer.echo(f"{path}: differs from its generated form", err=True)
        raise typer.Exit(code=1 if stale else 0)
    for path, text in generated_files().items():
        path.write_text(text, encoding="utf-8")
        typer.echo(f"{path}: written")


def _migration_mode(check: bool, apply_changes: bool, assume_yes: bool) -> str:
    """Return the explicit migration mode or exit with a command-usage error."""
    if check == apply_changes:
        typer.echo("choose exactly one migration mode: --check or --apply", err=True)
        raise typer.Exit(code=2)
    if assume_yes and not apply_changes:
        typer.echo("the option --yes requires the migration mode --apply", err=True)
        raise typer.Exit(code=2)
    return "check" if check else "apply"


def _report_migration_failure(error: Any) -> None:
    """Report every recovery file and completed write carried by a failed application."""
    for source, backup in error.backups:
        typer.echo(f"{source}: preserved as {backup}")
    for path in error.changed:
        typer.echo(f"{path}: migrated before failure")
    typer.echo(str(error), err=True)
    typer.echo(
        f"migration stopped after {len(error.changed)} completed writes; "
        f"{len(error.backups)} recovery files available",
        err=True,
    )


@app.command("migrate")
# Migration is a transactional command boundary that reports every preview and recovery outcome.
# pylint: disable-next=too-many-locals
def cli_migrate(
    directory: str = typer.Argument(..., help="Directory tree holding authored Gnomon records."),
    check: bool = typer.Option(
        False,
        "--check",
        help="Report required migrations and unified diffs without writing files.",
    ),
    apply_changes: bool = typer.Option(
        False,
        "--apply",
        help="Review, preserve and apply every safe binding-only migration.",
    ),
    assume_yes: bool = typer.Option(
        False,
        "--yes",
        "-y",
        help="Confirm the reviewed migrations without prompting.",
    ),
) -> None:
    """Preview or apply migrations from retained record contracts to current contracts.

    Check mode writes no file. Apply mode prints the same diffs, preserves every prior record under
    ``.gnomon-backup`` and requires confirmation. A record that requires semantic changes blocks
    the complete application. Generated views remain outside migration. The command exits with
    status 1 when previewed work remains or application is blocked, and status 2 when the mode is
    absent or ambiguous.
    """
    from .migration import (
        MigrationApplyError,
        apply_migration,
        plan_migration,
        render_migration_plan,
    )

    _migration_mode(check, apply_changes, assume_yes)
    try:
        plan = plan_migration(Path(directory))
    except ValueError as error:
        typer.echo(str(error), err=True)
        raise typer.Exit(code=1) from error
    cannot_apply = bool(plan.blocked or plan.failures)
    report = render_migration_plan(plan, confirm_no_writes=check or cannot_apply)
    for line in report.output:
        typer.echo(line)
    for line in report.errors:
        typer.echo(line, err=True)
    if check:
        if plan.pending:
            raise typer.Exit(code=1)
        return
    if cannot_apply:
        raise typer.Exit(code=1)
    if not plan.changes:
        return
    if not assume_yes:
        typer.confirm(
            f"Preserve and migrate {len(plan.changes)} authored records?",
            abort=True,
        )
    try:
        outcome = apply_migration(plan)
    except MigrationApplyError as error:
        _report_migration_failure(error)
        raise typer.Exit(code=1) from error
    for source, backup in outcome.backups:
        typer.echo(f"{source}: preserved as {backup}")
    for path in outcome.changed:
        typer.echo(f"{path}: migrated")
    count = len(outcome.changed)
    noun = "file" if count == 1 else "files"
    typer.echo(f"{count} {noun} migrated")


@app.command("itinerary")
def cli_itinerary(
    directory: str = typer.Argument(
        ..., help="Directory holding the filled records of one problem."
    ),
    output_format: OutputFormat = typer.Option(
        OutputFormat.TEXT,
        "--format",
        "-f",
        help="text prints one line per problem; sarif also writes a SARIF 2.1.0 log in the"
        " findings profile of Elenchos, on standard output or at --output.",
    ),
    output: Path | None = typer.Option(
        None,
        "--output",
        "-o",
        help="With --format sarif, write the log to this path instead of standard output; "
        "missing folders are created.",
    ),
    root: Path = typer.Option(
        Path("."),
        "--root",
        "-r",
        help="With --format sarif, the repository root from which the log states every path.",
    ),
) -> None:
    """Check every itinerary of one problem against the registries and the records it names.

    The text output prints one line per problem with its rule identifier, followed by a count. With
    ``--format sarif`` and no ``--output``, the log takes standard output and those lines go to
    standard error. The command exits with status 1 when a problem is found or a record cannot be
    read, and with status 2 when the log cannot be written.
    """
    source = _directory(directory)
    sarif = output_format is OutputFormat.SARIF
    if output is not None and not sarif:
        raise typer.BadParameter("requires --format sarif", param_hint="--output")
    folder = _log_folder(source, root) if sarif else PurePosixPath(".")
    records, files, unreadable = _read_records(source, tolerant=sarif)
    checked, found, stopped = _check_itineraries(records, files, sarif)
    if unreadable and stopped is None:
        stopped = (
            f"{len(unreadable)} record files could not be read, so the itineraries naming their"
            " records were not fully checked"
        )
    _echo_itineraries(unreadable, found, checked, sarif and output is None)
    if sarif:
        located = [Located(p, folder / files[i].name, i) for i, p in found]
        log = json.dumps(sarif_log(located, __version__, stopped), indent=2, ensure_ascii=False)
        _emit(log + "\n", output, "log")
    if found or stopped:
        raise typer.Exit(code=1)


def _echo_itineraries(
    unreadable: list[str],
    found: list[tuple[str, Finding]],
    checked: int,
    to_stderr: bool,
) -> None:
    """Print unreadable files, each problem with its rule identifier, and the problem count.

    The problems and the count go to standard error when the SARIF log takes standard output.
    """
    for line in unreadable:
        typer.echo(line, err=True)
    for identifier, problem in found:
        typer.echo(_finding_line(identifier, problem), err=to_stderr)
    typer.echo(f"{checked} itineraries checked, {len(found)} problems found", err=to_stderr)


def _log_folder(source: Path, root: Path) -> PurePosixPath:
    """Return the folder of ``source`` relative to ``root``, or exit with status 1 outside it."""
    try:
        return PurePosixPath(source.resolve().relative_to(root.resolve()).as_posix())
    except ValueError:
        typer.echo(f"{source} lies outside the root {root}", err=True)
        raise typer.Exit(code=1) from None


def _check_itineraries(
    records: dict[str, Mapping[str, Any]], files: dict[str, Path], sarif: bool
) -> tuple[int, list[tuple[str, Finding]], str | None]:
    """Return the number of itineraries checked, their problems, and the error that stopped them.

    An error of reading stops the check; with ``sarif`` it is returned for the log, and otherwise
    it is raised.
    """
    itineraries = [record for record in records.values() if record.get("type") == "itinerary"]
    found: list[tuple[str, Finding]] = []
    try:
        for itinerary in itineraries:
            problems = itinerary_problems(itinerary, records, states=git_states(files))
            found += [(str(itinerary["id"]), problem) for problem in problems]
    except (OSError, ValueError, yaml.YAMLError) as error:
        if not sarif:
            raise
        return len(itineraries), found, f"the check stopped on an error: {error}"
    return len(itineraries), found, None


@app.command("source-state")
def cli_source_state(
    directory: str = typer.Argument(
        ..., help="Directory of records, read recursively; each folder is one problem."
    ),
) -> None:
    """Print the source identifier that current views of a workspace must carry.

    This command is the integration boundary for freshness checks. A consumer calls Gnomon instead
    of reproducing its record selection, cleanup and canonical serialization. The command exits
    with status 1 without printing an identifier when a record cannot be read.
    """
    from .check import load_workspace
    from .source_state import source_state

    source = _directory(directory)
    workspace = load_workspace(source)
    for line in workspace.failures:
        typer.echo(line, err=True)
    if workspace.failures:
        raise typer.Exit(code=1)
    typer.echo(source_state(workspace.by_id))


@app.command("views")
# View generation keeps command options, diagnosed source state and emitted paths in one boundary.
# pylint: disable-next=too-many-locals
def cli_views(
    directory: str = typer.Argument(
        ..., help="Directory of records, read recursively; each folder is one problem."
    ),
    output: Path | None = typer.Option(
        None,
        "--output",
        "-o",
        help="Folder receiving the views; the folder `views` of the directory by default.",
    ),
    scope: str | None = typer.Option(
        None,
        "--scope",
        help="Write only the primary view for this named completion target.",
    ),
    result: ViewResultFormat = typer.Option(
        ViewResultFormat.TEXT,
        "--result",
        help=(
            "Report written files as human-readable text or one JSON result; JSON requires "
            "--scope."
        ),
    ),
) -> None:
    """Write generated views of the state of an inquiry as YAML records.

    The views are the state of each problem, the open conditions, the ready acts and their declared
    comparisons, the exposure of each answer, the assembly of each level, the progress of each
    itinerary, the maturity of each record, the operational inquiry graph, the statement of each
    question composed from its fields, and the LaTeX form of each expression. Each view identifies
    the canonical authored records used to generate it and holds no date or absolute path, so two
    runs on unchanged records write the same files. A named scope writes only the primary view for
    the research task associated with that completion target. The command exits with status 1 when
    a scope is unknown or a file cannot be read, and 2 when a view cannot be written.
    """
    from .answerability import as_document
    from .check import future_record_requirements
    from .view_coverage import attach_view_coverage, view_coverage
    from .view_routes import view_route
    from .views import all_views

    if result is ViewResultFormat.JSON and scope is None:
        raise typer.BadParameter("requires --scope", param_hint="--result json")
    source = _directory(directory)
    try:
        route = view_route(scope) if scope is not None else None
    except ValueError as error:
        typer.echo(str(error), err=True)
        raise typer.Exit(code=1) from error
    workspace, diagnosis = _diagnosis(source)
    target = output if output is not None else source / "views"
    views = all_views(
        workspace.by_id,
        as_document(diagnosis),
        diagnosis.impeached,
        diagnosis.conditional,
    )
    if route is not None:
        assert scope is not None
        selected = attach_view_coverage(
            views[route.view],
            view_coverage(
                scope,
                workspace.by_id,
                future_record_requirements(workspace, scope=scope),
            ),
        )
        views = {route.view: selected}
    try:
        target.mkdir(parents=True, exist_ok=True)
        written: list[Path] = []
        for name, view in views.items():
            path = target / f"{name}.yml"
            path.write_text(
                "# Generated by `gnomon views`. Edit the records, not this file.\n"
                + yaml.safe_dump(view, sort_keys=False, allow_unicode=True, width=100),
                encoding="utf-8",
            )
            written.append(path)
            if result is ViewResultFormat.TEXT:
                typer.echo(f"{path}: written")
        if route is not None and scope is not None:
            path = target / f"{route.view}.yml"
            if result is ViewResultFormat.JSON:
                typer.echo(
                    json.dumps(
                        {"path": str(path), "target": scope, "purpose": route.purpose},
                        ensure_ascii=False,
                    )
                )
            else:
                typer.echo(f"{scope}: open {path} to {route.purpose}")
    except OSError as error:
        typer.echo(f"cannot write the views in {target}: {error}", err=True)
        raise typer.Exit(code=2) from error
    if workspace.failures:
        raise typer.Exit(code=1)


@app.command("export")
def cli_export(
    directory: str = typer.Argument(
        ..., help="Directory of records, read recursively; each folder is one problem."
    ),
    output: Path | None = typer.Option(
        None,
        "--output",
        "-o",
        help="File receiving the export; `export.yml` in the directory by default.",
    ),
    check: bool = typer.Option(
        False,
        "--check",
        help="Compare the committed export with a fresh generation, and write nothing.",
    ),
    allow_findings: bool = typer.Option(
        False,
        "--allow-findings",
        help="Write the export although `gnomon check` reports an error, and record it there.",
    ),
) -> None:
    """Write the export of the research units and their relations, in the contract of `ekthesis`.

    The repository is named by `repository.id` in the nearest `repository.yml`. A relation whose end
    is not an exported unit is dropped and listed on standard error. The command refuses to write
    while `gnomon check` reports an error, unless `--allow-findings` is given. It exits with status
    1 when the repository is not named, a file cannot be read, the check reports an error without
    the override, or `--check` finds the export stale, and with status 2 when the export cannot be
    written.
    """
    source = _directory(directory)
    text, unread = _export_text(source, allow_findings)
    target = output if output is not None else source / "export.yml"
    if check:
        current = target.read_text(encoding="utf-8") if target.is_file() else None
        if current != text:
            typer.echo(f"{target}: stale; run gnomon export", err=True)
            raise typer.Exit(code=1)
        typer.echo(f"{target}: current")
        return
    _emit(text, target, "export")
    typer.echo(f"{target}: written")
    if unread:
        raise typer.Exit(code=1)


def _export_text(source: Path, allow_findings: bool) -> tuple[str, bool]:
    """Return the text of the export of a directory and whether a file could not be read, or exit
    with status 1 when no repository is named or the check reports an error without the override.
    """
    from .check import check_workspace, load_workspace
    from .export import build_export, render_export, repository_identifier

    repository = repository_identifier(source)
    if repository is None:
        typer.echo(f"no repository.yml naming repository.id above {source}", err=True)
        raise typer.Exit(code=1)
    workspace = load_workspace(source)
    for line in workspace.failures:
        typer.echo(line, err=True)
    errors = [x for x in check_workspace(workspace) if x.finding.rule.level == "error"]
    if errors and not allow_findings:
        typer.echo(f"gnomon check reports {len(errors)} errors; no export written", err=True)
        raise typer.Exit(code=1)
    export, dropped = build_export(workspace.by_id, repository, bool(errors))
    for ident in dropped:
        typer.echo(f"dropped: {ident}: an end is not an exported unit", err=True)
    return render_export(export), bool(workspace.failures)


@app.command("tree")
def cli_tree(
    directory: str = typer.Argument(
        ..., help="Directory holding the records of a project, read recursively."
    ),
) -> None:
    """Print the question tree of a project, from its problems to the assessments of its answers."""
    source = _directory(directory)
    records, _, failures = _read_records(source, tolerant=True, pattern="**/*.yml")
    for failure in failures:
        typer.echo(failure, err=True)
    typer.echo(render_tree(question_tree(records)), nl=False)


@app.callback()
def main_callback(
    version: bool = typer.Option(
        False, "--version", "-v", help="Show the package version and exit."
    )
) -> None:
    """Formal epistemic framework for organizing mathematical research."""
    if version:
        typer.echo(__version__)
        raise typer.Exit()


if __name__ == "__main__":
    app()
