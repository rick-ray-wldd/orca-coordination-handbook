# 8. Adopt the workflow gradually

[English](../en/08-adoption.md) | [繁體中文](../zh-TW/08-adoption.md) | [Home](../../README.md)

Each stage can work independently. You do not need the private reference automation.

## Stage 0: Prepare

Start with the safe template-copy path from the repository root:

```sh
python3 scripts/init_workspace.py --dest ../my-assistant --language en
```

Python 3.10+ is required. The destination must not already exist. The helper copies rules and templates, writes a starter task list, and does not execute Orca, start models, access accounts or configure services. For Traditional Chinese use `--language zh-TW`. Review placeholders before using any agent rules.

Install/open Orca separately if you want its native features. **Resolve the correct executable before running these macOS examples**: use `ORCA_CLI_COMMAND` if your Orca environment sets it; a development checkout may use `orca-dev`; Linux outside managed terminals uses `orca-ide`. Bare `orca` on Linux may be an unrelated screen reader. Follow your installed skill's instructions.

```text
orca --version
orca status --json
orca skills list
orca skills get orca-cli
orca skills get orchestration
```

Commands were reviewed against Orca CLI 1.4.220. Your installed help takes precedence.

```text
my-assistant/
  AGENTS.md
  CLAUDE.md
  coordination/
    CONTRACT.md
    routing.json
  templates/
  receipts/
  tasks.md
  README.md
  .gitignore
```

Open two coordinator sessions in this private folder, for example Claude Code and Codex CLI. A folder workspace is sufficient; Git is not required.

## Stage 1: Documents only

The manual equivalent is to copy `AGENTS.example.md` into both `AGENTS.md` and `CLAUDE.md`, `CONTRACT.example.md` into `coordination/CONTRACT.md`, and `routing.example.json` into `coordination/routing.json`.

Replace placeholders. Begin with three to five domains, each with a supervisor and another reviewer. Record tracked requests using `task-card.md`, assign using `dispatch-message.md`, and collect reports using `station-report.md`. Append each decision to private `receipts/dispatch-log.md`.

Everything in this stage is a convention. The value is explicit ownership, one writer, evidence and distinct user acceptance.

## Stage 2: Add native Orca features

Write card comments at checkpoints and move delivered work to `in-review`:

```sh
orca worktree set --worktree active --comment "Tests pass; review pending" --json
orca worktree set --worktree active --workspace-status in-review --json
```

Read terminal state and the input field before sending. Replace placeholders:

```text
orca terminal list --json
orca terminal read --terminal <handle> --json
orca terminal send --terminal <handle> --text "<dispatch message>" --enter --wait-submit 10 --json
```

Check `turn_started`, not just acceptance. Do not resend on silence. On an ambiguous transport error use the receipt's retry ID for the same request, following current CLI help.

For isolated code changes:

```text
orca worktree create --name <task-name> --no-parent --agent codex --prompt "<dispatch>" --json
```

For supervised work, read the installed orchestration guide and use its Run/worker/check/settlement lifecycle. A simple ownership handoff and a supervised worker are different workflows. Native automations can schedule work, but this repository does not configure them or establish their suitability for your inspection requirements [Unknown].

## Stage 3: Optional custom assistant layer

If document tracking becomes unwieldy, implement only what you need:

| Capability | Minimal design |
|---|---|
| Store | Local SQLite, transactions, file lock, revision checks |
| Contract | SHA-256 acknowledgement; reject stale hashes |
| Reports | One row per station; require evidence/blockers by state |
| Tasks | Completion evidence, note and reviewer |
| Routing | First-match precedence, locks, backup, version, changelog, validation |
| Board | Compute projections; dry-run by default; write changed cards only |
| Inspection | Ordinary fact collector → tool-disabled summary → private latest report |
| Redaction | Mask credential-shaped text before storage |

Do not read credentials or full conversations, follow symlinks, or execute source text. Mark generated files. Test transactions, compatibility, data retention and read-only source boundaries. These are implementation suggestions, not bundled software.

## Stage 4: Stable coordination

Weekly, audit unclassified work, overload, imbalance and expired overrides. Monthly, review direct-work and dispatch decisions. Synchronize changed rules using §7.6.

## Adoption checklist

- [ ] Correct Orca executable and installed guide verified.
- [ ] Rules, contract, routing and task file present; placeholders reviewed.
- [ ] Each domain has distinct supervisor/reviewer.
- [ ] First-line decisions and all five dispatch fields used.
- [ ] Evidence precedes review; review precedes accepted completion.
- [ ] User confirmation and external authorization recorded truthfully.
- [ ] Recovery has one operator and the original UUID.
- [ ] Active sessions fit this machine's measured capacity.
