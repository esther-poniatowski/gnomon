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

import json
from enum import Enum
from pathlib import Path, PurePosixPath
from typing import Any, Mapping

import typer
import yaml

from . import __version__
from . import info as pkg_info
from .findings import Finding
from .history import git_states
from .itineraries import itinerary_problems
from .sarif import Located, sarif_log
from .views import question_tree, render_tree
from .vocabulary import load_problem, render_markdown, render_yaml

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
        "itinerary, concept or design; repeat the option for several.",
    ),
    force: bool = typer.Option(False, "--force", help="Overwrite the files that already exist."),
) -> None:
    """Create the folder of a problem, with the record templates in the order of filling.

    The folder receives the templates of the problem, the target system, the background, the
    phenomenon, the question and the operators, the further kinds that ``--with`` names, and an
    index listing them in the order of filling. The command exits with status 1 when a file exists
    and ``--force`` is not given, or when a kind has no template.
    """
    from .scaffold import CORE_KINDS, scaffold

    try:
        written = scaffold(Path(directory), [*CORE_KINDS, *with_kinds], force)
    except (FileExistsError, ValueError) as error:
        typer.echo(str(error), err=True)
        raise typer.Exit(code=1) from error
    for path in written:
        typer.echo(f"{path}: written")
    typer.echo(
        f"Fill the records in the order of {Path(directory) / '_index.md'}, then run: gnomon check"
        f" {directory}"
    )


@app.command("validate")
def cli_validate(
    paths: list[str] = typer.Argument(..., help="Record files or directories to validate."),
) -> None:
    """Validate each record against the contract that it names, skipping the kinds that have no
    schema."""
    from .schemas import record_errors, record_kinds

    files: list[Path] = []
    for given in map(Path, paths):
        files += sorted(given.rglob("*.yml")) if given.is_dir() else [given]
    known, failed, checked = record_kinds(), 0, 0
    for path in files:
        record = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not isinstance(record, dict) or record.get("type") not in known:
            continue
        checked += 1
        for message in record_errors(record):
            failed += 1
            typer.echo(f"{path}: {message}")
    typer.echo(f"{checked} records checked, {failed} errors found")
    raise typer.Exit(code=1 if failed else 0)


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
    any folder. The text output prints one line per finding and a count. The command exits with
    status 1 when a finding is reported or a file cannot be read, and with status 2 when the
    report cannot be written.
    """
    from .check import check_workspace, load_workspace
    from .report import render_yaml_report

    source = Path(directory)
    if not source.is_dir():
        typer.echo(f"no such directory: {source}", err=True)
        raise typer.Exit(code=1)
    workspace = load_workspace(source)
    found = check_workspace(workspace)
    count = len(workspace.by_id)
    summary = (
        f"{count} records checked in {len(workspace.problems)} folders, {len(found)} findings, "
        f"{len(workspace.unfilled)} templates not yet filled"
    )
    for line in workspace.failures:
        typer.echo(line, err=True)
    if output_format is CheckFormat.TEXT:
        text = (
            "".join(f"{x.file}: {x.record}: {x.finding.rule.id}: {x.finding.text}\n" for x in found)
            + summary
            + "\n"
        )
    elif output_format is CheckFormat.YAML:
        unfilled = [p.relative_to(source).as_posix() for p in workspace.unfilled]
        text = render_yaml_report(found, source.name, count, unfilled)
    else:
        stopped = (
            f"{len(workspace.failures)} record files could not be read"
            if workspace.failures
            else None
        )
        text = (
            json.dumps(sarif_log(found, __version__, stopped), indent=2, ensure_ascii=False) + "\n"
        )
    if output is None:
        typer.echo(text, nl=False)
    else:
        try:
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_text(text, encoding="utf-8")
        except OSError as error:
            typer.echo(f"cannot write the report {output}: {error}", err=True)
            raise typer.Exit(code=2) from error
        typer.echo(summary, err=True)
    if found or workspace.failures:
        raise typer.Exit(code=1)


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
    from .answerability import as_document, diagnose, merge, render_text
    from .check import load_workspace

    source = Path(directory)
    if not source.is_dir():
        typer.echo(f"no such directory: {source}", err=True)
        raise typer.Exit(code=1)
    workspace = load_workspace(source)
    for line in workspace.failures:
        typer.echo(line, err=True)
    diagnosis = merge(
        [diagnose(workspace.by_id, local=problem.records) for problem in workspace.problems]
    )
    if output_format is StatusFormat.YAML:
        text = (
            "# Generated by `gnomon status`. Edit the records, not this file.\n"
            + yaml.safe_dump(as_document(diagnosis), sort_keys=False, allow_unicode=True, width=100)
        )
    else:
        text = render_text(diagnosis)
    if output is None:
        typer.echo(text, nl=False)
    else:
        try:
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_text(text, encoding="utf-8")
        except OSError as error:
            typer.echo(f"cannot write the report {output}: {error}", err=True)
            raise typer.Exit(code=2) from error
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
    markdown: bool = typer.Option(
        False, "--markdown", "-m", help="Also build the Markdown view beside the record."
    ),
    root: str = typer.Option(
        ".", "--root", "-r", help="Workspace root from which the Markdown view links its index."
    ),
) -> None:
    """Collect the symbols and operators of one problem into a table its author can consult."""
    source = Path(directory)
    if not source.is_dir():
        typer.echo(f"no such directory: {source}", err=True)
        raise typer.Exit(code=1)
    try:
        index_path = (source / "_index.md").resolve().relative_to(Path(root).resolve())
    except ValueError:
        typer.echo(f"{source} lies outside the workspace root {root}", err=True)
        raise typer.Exit(code=1) from None
    problem = load_problem(source)
    target = source / output
    target.write_text(render_yaml(problem), encoding="utf-8")
    if markdown:
        page = render_markdown(problem, index_path=index_path.as_posix())
        (source / f"{target.stem}.md").write_text(page, encoding="utf-8")
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
    records: dict[str, Mapping[str, Any]] = {}
    files: dict[str, Path] = {}
    failures: list[str] = []
    from .check import parse_file

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


def _write_log(log: dict[str, Any], output: Path | None) -> None:
    """Write ``log`` to ``output``, creating its folders, or to standard output when it is None."""
    text = json.dumps(log, indent=2, ensure_ascii=False) + "\n"
    if output is None:
        typer.echo(text, nl=False)
        return
    try:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(text, encoding="utf-8")
    except OSError as error:
        typer.echo(f"cannot write the log {output}: {error}", err=True)
        raise typer.Exit(code=2) from error


@app.command("schemas")
def cli_schemas(
    check: bool = typer.Option(
        False, "--check", help="Report the stale generated files instead of writing them."
    ),
) -> None:
    """Write the contracts and the templates generated from the base schemas and the vocabulary
    registry."""
    from .schemas import generated_files, stale_files

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
    source = Path(directory)
    if not source.is_dir():
        typer.echo(f"no such directory: {source}", err=True)
        raise typer.Exit(code=1)
    sarif = output_format is OutputFormat.SARIF
    if output is not None and not sarif:
        raise typer.BadParameter("requires --format sarif", param_hint="--output")
    folder = PurePosixPath(".")
    if sarif:
        try:
            folder = PurePosixPath(source.resolve().relative_to(root.resolve()).as_posix())
        except ValueError:
            typer.echo(f"{source} lies outside the root {root}", err=True)
            raise typer.Exit(code=1) from None
    records, files, unreadable = _read_records(source, tolerant=sarif)
    stopped = (
        f"{len(unreadable)} record files could not be read, so the itineraries naming their records"
        " "
        "were not fully checked"
        if unreadable
        else None
    )
    itineraries = [record for record in records.values() if record.get("type") == "itinerary"]
    found: list[tuple[str, Finding]] = []
    try:
        for itinerary in itineraries:
            found += [
                (str(itinerary["id"]), problem)
                for problem in itinerary_problems(itinerary, records, states=git_states(files))
            ]
    except (OSError, ValueError, yaml.YAMLError) as error:
        if not sarif:
            raise
        stopped = f"the check stopped on an error: {error}"
    problems = [f"{identifier}: {problem.text}" for identifier, problem in found]
    to_stderr = sarif and output is None
    for line in unreadable:
        typer.echo(line, err=True)
    for line in problems:
        typer.echo(line, err=to_stderr)
    typer.echo(
        f"{len(itineraries)} itineraries checked, {len(problems)} problems found", err=to_stderr
    )
    if sarif:
        located = [
            Located(problem, folder / files[identifier].name, identifier)
            for identifier, problem in found
        ]
        _write_log(sarif_log(located, __version__, stopped), output)
    if problems or stopped:
        raise typer.Exit(code=1)


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
    each answer, the progress of each itinerary, the maturity of each record, the question tree, and
    the statement of each question composed from its fields. Each view holds no date and no absolute
    path, so two runs on unchanged records write the same files. The command exits with status 1
    when a file cannot be read, and 2 when a view cannot be written.
    """
    from .answerability import as_document, diagnose, merge
    from .check import load_workspace
    from .views import all_views

    source = Path(directory)
    if not source.is_dir():
        typer.echo(f"no such directory: {source}", err=True)
        raise typer.Exit(code=1)
    workspace = load_workspace(source)
    for line in workspace.failures:
        typer.echo(line, err=True)
    diagnosis = merge(
        [diagnose(workspace.by_id, local=problem.records) for problem in workspace.problems]
    )
    target = output if output is not None else source / "views"
    try:
        target.mkdir(parents=True, exist_ok=True)
        for name, view in all_views(
            workspace.by_id, as_document(diagnosis), diagnosis.impeached, diagnosis.conditional
        ).items():
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
    source = Path(directory)
    if not source.is_dir():
        typer.echo(f"no such directory: {source}", err=True)
        raise typer.Exit(code=1)
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
