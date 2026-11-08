"""
Command-line interface for the `gnomon` package.

Defines commands available via `python -m gnomon` or `gnomon` if installed as a script.

Commands
--------
info : Display diagnostic information.
init : Create the folder of a problem, with the record templates in the order of filling.
validate : Validate each record against the schema of its type.
check : Run every check on the records of a directory tree.
status : List the open conditions of the questions of a workspace.
vocabulary : Collect the symbols and operators of one problem into a table.
itinerary : Check every itinerary of one problem against the activity and product-type registries.
tree : Print the question tree of a project, from its problems to the assessments of its answers.
views : Write the views of the state of an inquiry as YAML records.
"""

# pylint: disable=import-outside-toplevel  # each command imports what it runs; --help stays fast

import json
from enum import Enum
from pathlib import Path, PurePosixPath
from typing import TYPE_CHECKING, Any, Mapping

import typer
import yaml

from . import __version__
from . import info as pkg_info
from .findings import Finding
from .history import git_states
from .itineraries import itinerary_problems
from .sarif import Located, sarif_log
from .views import question_tree, render_tree
from .vocabulary import load_problem, render_yaml

if TYPE_CHECKING:
    from .answerability import Diagnosis
    from .check import Workspace

app = typer.Typer(add_completion=False, no_args_is_help=True)


@app.command("info")
def cli_info() -> None:
    """Display version and platform diagnostics."""
    typer.echo(pkg_info())


@app.command("init")
def cli_init(
    directory: str = typer.Argument(
        ..., help="Folder of the new problem, created when it does not exist."
    ),
    with_kinds: list[str] = typer.Option(
        [],
        "--with",
        "-w",
        help="A further record kind to scaffold, such as model, binding, key, answer, assessment, "
        "itinerary, concept, design or derivation; repeat the option for several.",
    ),
    force: bool = typer.Option(
        False, "--force", help="Overwrite the templates and the index that already exist."
    ),
) -> None:
    """Create the folder of a problem, with the record templates in the order of filling.

    The folder receives the templates of the problem, the target system, the background, the
    phenomenon, the question and the operators, the further kinds that ``--with`` names, and an
    index listing them in the order of filling. In a folder that already holds records, only the
    missing templates are written, and each is registered in the existing index; ``--force``
    overwrites every template and the index. The command exits with status 1 when a kind has no
    template.
    """
    from .scaffold import CORE_KINDS, scaffold

    try:
        outcome = scaffold(Path(directory), [*CORE_KINDS, *with_kinds], force)
    except ValueError as error:
        typer.echo(str(error), err=True)
        raise typer.Exit(code=1) from error
    for path in outcome.written:
        typer.echo(f"{path}: written")
    typer.echo(f"{outcome.index}: {outcome.index_state}")
    if outcome.kept:
        typer.echo(f"{len(outcome.kept)} existing files kept")
    typer.echo(
        f"Fill the records in the order of {Path(directory) / '_index.md'}, then run: gnomon check"
        f" {directory}"
    )


@app.command("validate")
def cli_validate(
    paths: list[str] = typer.Argument(..., help="Record files or directories to validate."),
) -> None:
    """Validate each record against the contract that it names, skipping the kinds that have no
    schema and the templates not yet started, whose identifier still holds a placeholder."""
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
) -> None:
    """Run every check on the records of a directory tree.

    Each folder that holds records is checked as one problem, and a reference may reach a record of
    any folder. The text output prints one line per finding, a warning marked as such, and a count.
    The command exits with status 1 when a finding of level error is reported or a file cannot be
    read, and with status 2 when the report cannot be written; a warning fails no check.
    """
    from .check import check_workspace, load_workspace

    source = _directory(directory)
    workspace = load_workspace(source)
    found = check_workspace(workspace)
    errors = [x for x in found if x.finding.rule.level == "error"]
    summary = (
        f"{len(workspace.by_id)} records checked in {len(workspace.problems)} folders,"
        f" {len(errors)} findings, {len(found) - len(errors)} warnings,"
        f" {len(workspace.unfilled)} templates not yet filled"
    )
    for line in workspace.failures:
        typer.echo(line, err=True)
    _emit(_check_report(workspace, found, source, output_format, summary), output, "report")
    if output is not None:
        typer.echo(summary, err=True)
    if errors or workspace.failures:
        raise typer.Exit(code=1)


def _check_report(
    workspace: "Workspace",
    found: list[Located],
    source: Path,
    output_format: CheckFormat,
    summary: str,
) -> str:
    """Return the report of ``gnomon check`` in the form that the command asks for."""
    from .report import render_yaml_report

    if output_format is CheckFormat.TEXT:
        lines = [
            f"{x.file}: {x.record}: {'warning: ' if x.finding.rule.level == 'warning' else ''}"
            f"{x.finding.rule.id}: {x.finding.text}\n"
            for x in found
        ]
        return "".join(lines) + summary + "\n"
    if output_format is CheckFormat.YAML:
        unfilled = [p.relative_to(source).as_posix() for p in workspace.unfilled]
        return render_yaml_report(found, source.name, len(workspace.by_id), unfilled)
    stopped = (
        f"{len(workspace.failures)} record files could not be read" if workspace.failures else None
    )
    return json.dumps(sarif_log(found, __version__, stopped), indent=2, ensure_ascii=False) + "\n"


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
        None, "--output", "-o", help="Write the report to this path instead of standard output."
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
    that a renderer displays through the schema ``gnomon:view.vocabulary@2``."""
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
        False, "--check", help="Report the stale generated files instead of writing them."
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

    The text output prints one line per problem and a count. With ``--format sarif`` and no
    ``--output``, the log takes standard output and those lines go to standard error. The command
    exits with status 1 when a problem is found or a record cannot be read, and with status 2 when
    the log cannot be written.
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
    unreadable: list[str], found: list[tuple[str, Finding]], checked: int, to_stderr: bool
) -> None:
    """Print the files that cannot be read, one line per problem, and the count of problems.

    The problems and the count go to standard error when the SARIF log takes standard output.
    """
    for line in unreadable:
        typer.echo(line, err=True)
    for identifier, problem in found:
        typer.echo(f"{identifier}: {problem.text}", err=to_stderr)
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


@app.command("views")
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
) -> None:
    """Write the views of the state of an inquiry as YAML records, one file per view.

    The views are the state of each problem, the open conditions and the ready acts, the exposure of
    each answer, the progress of each itinerary, the maturity of each record, the question tree, the
    statement of each question composed from its fields, and the LaTeX form of each expression. Each
    view holds no date and no absolute
    path, so two runs on unchanged records write the same files. The command exits with status 1
    when a file cannot be read, and 2 when a view cannot be written.
    """
    from .answerability import as_document
    from .views import all_views

    source = _directory(directory)
    workspace, diagnosis = _diagnosis(source)
    target = output if output is not None else source / "views"
    views = all_views(
        workspace.by_id, as_document(diagnosis), diagnosis.impeached, diagnosis.conditional
    )
    try:
        target.mkdir(parents=True, exist_ok=True)
        for name, view in views.items():
            path = target / f"{name}.yml"
            path.write_text(
                "# Generated by `gnomon views`. Edit the records, not this file.\n"
                + yaml.safe_dump(view, sort_keys=False, allow_unicode=True, width=100),
                encoding="utf-8",
            )
            typer.echo(f"{path}: written")
    except OSError as error:
        typer.echo(f"cannot write the views in {target}: {error}", err=True)
        raise typer.Exit(code=2) from error
    if workspace.failures:
        raise typer.Exit(code=1)


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
