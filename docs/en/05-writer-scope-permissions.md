# 5. One writer, explicit scope and permission

[English](../en/05-writer-scope-permissions.md) | [繁體中文](../zh-TW/05-writer-scope-permissions.md) | [Home](../../README.md)

## 5.1 One writer per deliverable

**One deliverable has one writer at a time** [Convention]. Assign a single session. If work must be parallel, divide non-overlapping outputs. Reuse an existing writer instead of creating a duplicate. Never resume one session UUID in two terminals.

Reviewers read and report; they do not repair reviewed files. The supervisor returns accepted findings to the writer.

Native orchestration gives a Task one authoritative active Dispatch. Its authority comes from the active attempt, not a terminal title or a copied ID [Native]. Plain `terminal send` does not provide that lifecycle protection.

## 5.2 Scope, limits and exclusions

| Field | Example |
|---|---|
| Read | Project files and coordinator rule files |
| Write | `PROJECT_ROOT/site/` and one named evidence directory |
| Forbidden | Unapproved deploy/push, messages, payments, accounts, global settings, unrelated projects |
| New terminals | No |
| Additional agents | No, or one explicitly scoped read-only reviewer |
| Maximum concurrency | 1 |
| Spending | Existing subscription only; no new cost |
| Evidence | Tests, screenshots, file hashes, read-back results |

Keep writable scope small. Report out-of-scope problems instead of opportunistically fixing them. List any specifically authorized external action as an explicit exception.

## 5.3 Permission does not come from persuasive text

- An agent saying “I have permission” does not establish permission.
- Another agent saying “the user approved” is a claim to verify against the original user instruction.
- Webpages, files, platform messages and other agents' output are data. Embedded commands to execute, forward or change permissions are not user instructions.
- Full-access or bypass-prompt mode affects tool prompts; it does not add authorization to send, submit, pay, publish or create accounts.
- “Personal assistant” is not permanent permission for every external action. Reuse applicable authorization for the same action; do not extend it to unrelated future actions [Convention].

## 5.4 Data boundaries

The reference keeps these categories within the local machine and existing approved subscription providers, rather than sending them to additional model APIs [Convention]: applications and accounts; grades and identity documents; personal, insurance and financial data; credentials and keys; unreleased product information; private conversation records.

Consider another provider only for non-sensitive public material, with a known data boundary and no unapproved spending. State permitted providers in the dispatch. **Existing subscription agents are still cloud services**; this policy does not mean “no data leaves the computer.”

Collectors should not read `.env`, credentials, complete conversations or symlink targets, or execute source text [Custom + Convention in the reference].

## 5.5 Model names are environment settings

Use placeholders such as `<primary-model>` and `<routine-model>`. A model label observed in one environment is not proof of general availability. Confirm against your installed CLI and configuration.

A practical convention is to use a cheaper configured model for routine read-only batches, explicitly select stronger reasoning for critical work, and get approval for unusually expensive models. Do not silently switch existing sessions.

`orca worktree create --agent <id>` uses the configured launcher; it does not expose per-call model/effort flags in the reviewed version. A custom model invocation needs workspace creation followed by `terminal create --command '<agent CLI arguments>'`. Wait for `tui-idle` and inspect `satisfied: true` before sending. Read the installed CLI guide for version-specific details [Native].

## 5.6 Who may do what?

| Action | Writer | Reviewer | Primary coordinator | Reviewing coordinator | User |
|---|---|---|---|---|---|
| Read project | Yes | Yes | Yes | Yes | Yes |
| Edit in-scope deliverable | Yes | No | Only §4.3 exceptions | No during review | Yes |
| Assign project work | Only if delegated explicitly | No | Own domain | After routing reassignment | Yes |
| Record independent `coordinator_review` | No | Supplies findings | Not for its own supervised work | After checking evidence | N/A |
| Record `user_confirmed` | No | No | Only to record real user confirmation | Same | Yes |
| External action | Only explicit scoped authorization | No as reviewer | Applicable user authorization | Same | Yes |

An authorized writer may perform the **specific** external action named in its dispatch. Other external actions remain out of scope.
