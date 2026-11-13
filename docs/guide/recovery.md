---
tags:
  - guide
index: "[User guide](docs/guide/_index.md)"
aliases:
  - Recovering the integrated workflow
---
# Recovering the integrated workflow

Recovery preserves authored research records when the Gnomon–Ekphrasis workflow stops. The verified scope covers six failures across the desktop and command-line workflow.

> [!IMPORTANT] Prerequisites
> Install Gnomon with a dedicated Python interpreter and enable Ekphrasis in the research vault. Run `gnomon setup .` from the vault root to provision the portable registry and schema closure. Then complete the shared [Ekphrasis configuration](first-inquiry.md#^ekphrasis-setup), adapting its inquiry path to the current inquiry. Afterward, the records may follow either the [greenfield route](first-inquiry.md) or the [adoption route](adopting-existing-research.md).

## Choose the failure

Keep every authored YAML record in place. Repair only the syntax or Gnomon–Ekphrasis dependency named by the failure. Never run the command `gnomon init --force` for these failures.

| Visible result | Failed capability | Recovery is complete when |
| --- | --- | --- |
| *Invalid YAML* | Ekphrasis cannot parse the authored record | The form opens and Gnomon can check the record |
| *Schema not found* or *Schema not loaded*, with a recoverable cause in *Diagnose setup* | Ekphrasis fails to resolve the record contract | The schema checks pass and the form opens |
| *Python interpreter file: Fail* | Configured Gnomon commands cannot start | Both interpreter checks pass |
| A warning at *Source state* | The generated view no longer represents the current records | The regenerated view states *Source state: current* |
| A post-creation failure notice | The inquiry index lacks the new record | The index contains one canonical entry for the existing record |
| The contracts named by backups must be restored, or apply mode reports recovery files | Some sources may carry newer contracts or incomplete writes | Every source in the recovery set matches its exact backup and validates under its restored contract |

## Invalid YAML

**Preserved state:** The authored file remains on disk, but Ekphrasis cannot derive its form.

**Failure:** The *Invalid YAML* message names the line and column that the parser could not read.

**Repair and resume:**

1. Activate *Open the source view* in the error message.
2. Use the reported reason, line and column to inspect the nearby source. Correct only the syntax defect, and let Obsidian save the file.
3. Activate *Open the form view*.
4. Run the check command on the inquiry because this repair changed an authored record:

   ```sh
   gnomon check <inquiry>
   ```

**Recovered state:** The form opens. The check reads the repaired record. Any subsequent method finding concerns the record content rather than its YAML syntax.

## Unresolved schema

**Preserved state:** The authored record remains on disk, but Ekphrasis cannot derive a form from its logical contract.

**Failure:** The messages *Schema not found* and *Schema not loaded* identify the failed schema dependency. The verified route covers an incorrect registry path in Ekphrasis, a missing portable registry or schema closure, and a hidden generated schema that changed after Ekphrasis loaded it.

**Repair and resume:**

1. Run *Diagnose setup* and read the *Next action* of the first failed schema check.
2. If the registry exists but the Ekphrasis setting points elsewhere, enter the existing registry path under **Settings → Ekphrasis → Schema registry**.
3. If the documented portable registry or its schema closure is missing, run the setup command from the vault root:

   ```sh
   gnomon setup .
   ```

4. If the setup command reports a differing generated target, stop. Because this result is outside the verified automatic recovery route, preserve the target, inspect the discrepancy and never pass `--force` as a generic repair.
5. After a successful setup command, enter its printed registry path under **Settings → Ekphrasis → Schema registry**.
6. If the diagnostic states that a hidden generated schema changed after Ekphrasis loaded it, restart Obsidian.
7. Run *Diagnose setup* again, and reopen the record after the schema checks pass.

**Recovered state:** The schema and form checks pass, and the authored record opens as a form.

## Unavailable Python runtime

**Preserved state:** Authored records and built-in form checks remain available. Primary views and post-creation commands remain unavailable until Ekphrasis can start the configured interpreter. ^python-runtime-recovery

**Failure:** The setup diagnostic marks *Python interpreter file* as *Fail* and names the affected commands.

**Repair and resume:**

1. Activate Gnomon's dedicated Python environment.
2. Print the absolute path of that environment's interpreter:

   ```sh
   python -c "import sys; print(sys.executable)"
   ```

3. Enter the printed path under **Settings → Ekphrasis → Python interpreter**.
4. Run *Diagnose setup* again.
5. Continue according to the failed command:
   - for a primary-view failure, run *Open primary view* again;
   - for a creation failure, keep the created record and follow the [procedure for an unindexed record](#^unindexed-record).

**Recovered state:** *Python interpreter file* reads *Pass*. *Start of the Python interpreter* also reads *Pass*. The selected resumption route completes.

## Stale primary view

**Preserved state:** The authored records remain current. Only the generated view is stale.

**Failure:** The field *Source state* reports that the generated view is stale.

**Repair and resume:**

1. Leave the generated YAML file unchanged.
2. Run *Open primary view* and enter the same completion target that produced the stale view.
3. Activate *Generate and open*.
4. If Ekphrasis cannot generate the view because the interpreter failed, complete the [Python-runtime recovery](#^python-runtime-recovery), then generate the view again.

**Recovered state:** The regenerated view displays *Source state: current* and no stale-source warning.

## Record missing from inquiry index

**Preserved state:** Ekphrasis has already created and opened the record. Only its canonical entry in the inquiry index is missing. ^unindexed-record

**Failure:** The creation notice states that the post-creation command failed and names *Retry failed post-creation action*.

**Repair and resume:**

1. Keep the newly created record. Do not run *Create instance* for the same path again.
2. Correct the cause named by the notice.
3. If the notice names the interpreter, complete the [Python-runtime recovery](#^python-runtime-recovery).
4. For the standard Gnomon route, enter this post-creation command:

   ```json
   ["-m", "gnomon", "register", "{vault}/{path}"]
   ```

5. Without restarting Ekphrasis, run *Retry failed post-creation action*.
6. Inspect the inquiry index and confirm that it contains one entry for the new record.

Ekphrasis offers the retry command only until the plugin restarts. After a restart, the idempotent registration command can update the index for the existing record:

```sh
gnomon register <record>
```

The [registration command](cli-reference.md#^cli-register) leaves an existing canonical entry unchanged when repeated.

**Recovered state:** The inquiry index contains exactly one canonical entry, and the retry command is no longer available.

## Record migration

**Preserved state:** Apply mode first copies every approved record. The directory `.gnomon-backup/migrations` retains the exact source bytes. Then, apply mode changes the contracts. A write can still change source bytes. Gnomon counts the source as migrated only after the write succeeds. Therefore, a failed write may leave changed bytes without a `migrated` output line. ^migration-recovery

**Failure:** Apply mode changed contracts that must return to their prior state. Alternatively, apply mode stopped after creating recovery files. Each output line of the form `<source>: preserved as <backup>` identifies one recovery pair.

**Repair and resume:**

1. Stop editing every source named by a recovery pair.
2. Select the complete recovery set. After a successful apply, select every pair from that run. After a failed apply, select every reported recovery pair, including sources not reported as migrated before failure.
3. Copy every selected source into a separate folder outside the inquiry. Preserve the relative paths so that this copy can restore the newer sources.
4. Copy each backup onto its paired source. Keep the backup itself unchanged and in place.
5. Validate the restored contracts with this command:

   ```sh
   gnomon validate <inquiry>
   ```

6. Preview the restored migration state without writing:

   ```sh
   gnomon migrate <inquiry> --check
   ```

7. Confirm that each restored record would update to its current contract. The preview must report zero blocked records, zero unreadable records and zero files written. The write-free preview exits with status `1` because work remains.
8. If `gnomon validate` fails or the preview reports a blocker, restore the newer sources from the separate copy and keep the recovery files unchanged.
9. After accepting the restored state, regenerate the views of the inquiry.

**Recovered state:** Each selected source exactly matches its backup. The separate folder preserves the sources that existed before recovery. Apply mode cannot overwrite the unchanged backup.

## Verified boundary

Three limits bound the verified recovery routes:

- Five procedures were verified in the desktop app, and the migration procedure was verified through the command-line interface. In the mobile app, forms and built-in checks remain available, but Python project commands do not run.
- A missing custom-checker package has no verified recovery procedure.
- A differing generated target stops the schema procedure because no automatic recovery has been verified.
