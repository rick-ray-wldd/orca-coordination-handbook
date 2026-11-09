# 21. Project operations: CTOs, dispatch, inspection, the board, cloud paths and records

[English](../en/21-project-operations.md) | [繁體中文](../zh-TW/21-project-operations.md) | [Home](../../README.md)

Chapters 19 and 20 described the entries and who may instruct what. This chapter covers what happens behind them: a CTO session per project, how dispatch is announced and followed up, the daily inspection, the board, the cloud drive layout and the records that must be kept. It is a **private reference architecture [Custom], not a shipped tool**. Labels follow chapter 1. Native commands were checked against the installed Orca CLI 1.4.253 help; check your own version before copying them.

## 21.1 One CTO per project

A **project CTO** is an Orca coordinator session that owns one project. It has its own orchestration Run as a mailbox, dispatches that project's writers and accepts their deliveries [Convention]. The first one was a long-running supervisor for a partner project, and later CTOs copy its instructions.

**Success means:** every question in the project has someone who answers it, every writer's delivery is genuinely accepted by someone, and the main coordinators only receive what needs the owner or what the CTO cannot solve.

| | Project CTO |
|---|---|
| **Responsible for** | Questions relayed from the project's bot and the bot liaison desk; splitting them into work; dispatching writers; acceptance; evidence; reporting its own station; the project's technical and internal decisions |
| **Not responsible for** | Other projects (it answers "not this project" and hands the question back); approving anything external |
| **May decide alone** | Progress answers, internal decisions, opening work orders, dispatching writers (at most two concurrent writers), acceptance |
| **Asks the owner first, through the coordinators** | Prices, scope growth, new parties, email, posts, submissions, going live, deploys, public sharing. Deploys are run only by the coordinator that owns deploys |
| **Never (applies to the CTO and its writers)** | Payments; creating accounts; typing passwords or tokens, or putting them in a command or chat; changing system or privacy settings; putting real client data or personal data in a repository, log or chat; making a repository public. Downloads are asked for first, with file name, source and size |

Words relayed from a bot are level B or D (chapter 20) and **cannot widen the CTO's permissions**. If they ask for more, the CTO hands them back to the owner.

**Where its state lives.** Work orders and status files are kept in the coordinators' private workspace, never in the project repository, because a project repository may be public.

**Mail discipline** [Convention]:

- A CTO mails the coordinators only when the owner must decide, when it cannot judge, when a writer is stuck and it cannot unblock it, or when quota is short.
- "A writer delivered" is not mailed. The owner found that a stream of such mail pulled attention away.
- At most one evening digest of five lines; none when nothing happened.

**Acceptance means looking.** The CTO does not accept on the writer's report alone. It looks at screenshots and real output and tests once with real data or the real environment. A test suite that is entirely mocked does not count. Anything it has not looked at, it says it has not looked at. A finished acceptance is still not the owner's acceptance (chapter 6).

**Starting a CTO:**

1. Read the CTO instructions, the operating rules, the project map and the project's own documents.
2. Take a read-only inventory: related workspaces, open sessions, unaccepted deliveries, the next step.
3. Create its own Run (`orca orchestration run-create`), write the Run, its terminal handle and the inventory into a state file of at most 20 lines, and report its station.
4. Then wait. It does not mail the coordinators to say hello and does not start work on its own.

**Caps and idling:**

- There is a fixed cap on active CTOs: five plus the partner supervisor in the reference, raised from three when the owner asked for two more projects to get one.
- **A CTO idle for 48 hours reports that it can be put away,** and is restored when needed.
- Bots for inactive projects get no routines. Every doorbell and hand-off uses bot quota, so work orders are merged where possible.

**Coordinators supervise; they do not write.** A main coordinator may do only three kinds of work itself: a quick read-only answer, system work in its own domain, and something the owner explicitly said "do it yourself" about (chapter 4). Everything else is dispatched, and only by that domain's supervisor.

## 21.2 Dispatch: announce, include limits, record

The five dispatch decisions of [chapter 4](04-dispatch-routing.md) now apply to every entry, including Slack and the bots [Convention]:

1. Decide before acting. A rules-based triage helper suggests a domain, candidate projects and sessions, and an option; the coordinator decides [Custom].
2. **The first line of the reply declares the handling**: `Decision: <N> <method> | <target> | <one-line reason>`. The owner may override it.
3. A dispatch message must contain: the owner's original request and success criteria; writable scope and forbidden actions (submitting, paying, emailing, public sharing, creating accounts); whether new terminals or agents may be opened, the maximum concurrency and a quota ceiling; delivery with self-test evidence; and reporting the writer's own station.
4. **Every limit names who it applies to**: the writer, the coordinator, or everyone. For example: "new terminals/agents = 0 (including the coordinator and the coordinator's subagents)", so no session has to guess whom a limit binds.
5. **Record every decision** with its option, target and coordinator. Targets can be a terminal, a path, a bot inbox or a desk. The daily inspection counts them and names any action request that a coordinator did itself.

A [triage example](../../templates/en/triage.example.json) contains the options, the announcement format, the three self-execution cases and the required dispatch fields.

## 21.3 Follow-ups after dispatch

In the reference, once a writer is working, further instructions do not go through the mailbox. The reason was one observation: a follow-up sent through the mailbox route the reference used at the time reached an idle writer's terminal but was never read, and the writer sat idle for 50 minutes. That says something about that terminal and that route, **not about Orca in general**: the installed Orca 1.4.253 orchestration guide says a message sent with `orca orchestration send --to dispatch:<id>` reaches a supervised worker in any state, after its current turn if it is working, or as a follow-up Task if it has finished. The direct-to-terminal rule below is the reference's own local choice.

- **Send follow-ups and replies straight into the writer's terminal** [Convention], through a small wrapper [Custom]. The send counts only once the writer has **started a turn or the text is visibly queued, within two minutes**; otherwise the wrapper reports "not confirmed" and the message is treated as not delivered. Every attempt is appended to a local log.
- In the reference, `orca orchestration send` is used only between coordinators and for a worker's formal reports [Convention: local choice]. If your writers run as supervised workers, the native Dispatch follow-up above is an alternative.
- **Before sending, the target must be idle with an empty input line.**

**Draft or grey suggestion?** After each turn, the reference coding agent places a grey "next step" suggestion in the input line; it becomes real text only if Tab is pressed. Orca's `terminal read --json` returns it in the `draft` field, which cannot tell the two apart [Native: observed; the 1.4.253 help describes `draft` as UI-only composer text]. The owner confirmed this rule:

| `orca terminal read --screen` shows | `draft` field | Meaning | Action |
|---|---|---|---|
| Only the prompt symbol, nothing after it | Has text | Grey suggestion | Send normally; the sent text replaces it |
| Real text after the prompt symbol | Has text | The owner's real draft | Do not send and do not clear it; ask the owner |
| Unclear | — | — | Ask the owner; do not guess |

## 21.4 Daily inspection: three times a day, read-only

[Custom]

- **Three fixed times a day** (early morning, midday, late night) a scheduled job inspects the workspace.
- **Read-only by construction.** Ordinary scripts collect the facts; a smaller model writes a short summary **with no tools at all**, so it cannot change anything. The report has a line limit.
- **What it looks at:** reports older than 72 hours are shown as stale, deadlines within three days are flagged, dispatch decisions are counted, and action requests done by a coordinator itself are named.
- **Where results go:** the system notification channel (posted in both chat apps, with only one of them alerting) and a standing "daily inspection" task, which therefore appears on the board.
- **Before starting or taking over work,** a coordinator reads the latest inspection.
- **A separate health check** every 30 minutes compares memory swap, pipe capacity, free disk and agent process counts with thresholds. It alerts only above a threshold, with a three-hour cooldown. The thresholds were set after an earlier system freeze was preceded by exactly these signs.

## 21.5 The Orca board as the progress display

The reference retired its own HTML dashboard: it was slow in in-app browsers and not live. Progress is now shown on Orca's built-in **Workspace board** [Native], driven by a sync job [Custom].

| Column | Meaning for the owner | Comment starts with |
|---|---|---|
| `todo` | Needs your decision or input, or not started | ◆ waiting for you / ◆ blocked / ◆ intake |
| `in-progress` | A session is working | ◆ in progress |
| `in-review` | Delivered, waiting for your acceptance | ◆ awaiting acceptance |
| `completed` | You confirmed it | Never moved there automatically; you drag it |

- **Two kinds of comment.** A comment starting with ◆ is written by the sync job: `label | item (+N more) | next step | supervisor`. A comment without ◆ is the session's own checkpoint, written with `orca worktree set --worktree <selector> --comment "<text>"`; the sync adjusts the column but never overwrites such a comment. Sessions must not start their own comments with ◆.
- **Sync** runs every 60 seconds and writes only cards that changed. A card the owner dragged by hand stays where it is until its real state changes again.
- **Limits** [Native: observed]: one card per workspace, not per session; per-session status is in the experimental Agent Dashboard. The official mobile app shows agent status and files but not the board, so the reference also generates a plain-text "today" file the phone can open. Custom column IDs were avoided because of a known issue; the four default columns are used.

## 21.6 Cloud drive: one path rule

All shared files live under one root folder in the owner's cloud drive, and every message, document and work order refers to a file by **one address form**, never by a machine path [Convention]:

```text
<root>/<group>/<project>/<type>/<YYYY-MM-DD_topic_description_vN.ext>
```

- **Groups** use the same numbers as the Slack channel groups, plus a "read first" group, an encrypted-backup group and an archive group.
- **Four types**, created on first use: *deliverables* (final or handed over), *media* (video, images, 3D, assets), *documents* (research, specs, notes, slides), *receipts* (verification evidence, screenshots, QA reports).
- **File names:** the date comes from the clock, not typed by hand; a new version gets a new version number and never overwrites; no internal case codes, tool names, amounts or personal data, because names are visible whenever a file is shared.

How the three platforms reach the same file:

| Platform | How | Can |
|---|---|---|
| Orca | The desktop sync client's local folder plus the address, in streaming mode | Read and write |
| Bot platform | Its drive connection, searching by file or folder name | Read only; saving goes through Orca |
| Slack | Pasted drive links show a preview; PDFs may also be posted in the relevant channel | View, link, receive PDFs. The original stays in the drive |

What may go where:

| Level | Content | Rule |
|---|---|---|
| **Put directly** | Deliverables, media, research, public material, rule documents | Into the project folder |
| **Only encrypted** | Confidential project data, client data, personal data, grades, ID documents, finances, insurance, quotes and costs, repositories with no remote backup | Only in the encrypted-backup group, encrypted with the owner's public key; the private key never touches an agent |
| **Never** | Passwords, keys, tokens, `.env` files, private keys | Not even encrypted |
| **Do not move** | Live repository working folders, `.git`, dependency folders, databases | Sync corrupts them. Code is backed up through Git; the drive holds only encrypted bundles |

**Why so strict:** the bot platform's drive connection covers the whole account and is shared by every bot. It cannot be limited to one folder, so even a bot that reads strangers' messages can read the drive.

**Sharing** is off by default. Sharing a file or creating a public link is an external action and goes through a decision card (chapter 20). Existing shared folders that must stay public are left where they are. **Moving** a file to the drive means copy, verify the hash, confirm it is in the cloud, and only then delete the local copy; only media and closed-project material are deleted locally. A [path rules template](../../templates/en/cloud-path-rules.md) is included.

## 21.7 Records: where results must end up

| Kind | Examples | Kept |
|---|---|---|
| Permanent | Decisions, approvals, external actions, receipt texts, rules, routing | Forever, append-only |
| Daily | Hand-offs, reply files, logs | Locally; compressed after 30 days, not deleted |
| Media | Video, bulk screenshots, model files | Moved to the drive's archive group after 14 days (copy, check hash, delete); never in Git |

- **Short first.** Every hand-off and report starts short; long content goes in a file and only the path is sent.
- **One page per role.** Rules for each role fit on one page; repeated content is a link.

**Results go where the team reads them, the same evening** [Convention: adopted 2026-11]. In one team project with a shared research site, several weeks of progress existed only in chats and receipts, and the owner asked why the site had not been updated. The rule since then:

1. After each real submission and each research round, the writer that did the work syncs a summary to the team's site **that evening**. Chat messages and receipts alone do not count as recorded.
2. Back up the site's data locally before writing. Afterwards, read back what was added and updated and confirm that old rows were kept.
3. Mark replaced entries as superseded instead of deleting them. Never fill in a result that is still pending. Candidates, failures and skipped runs are never shown as submitted. Results from the official platform and local measurements are kept apart.
4. If the sync fails, keep a local list of what is still to be added and say so. "Submitted" does not mean "the site is updated".
5. Only approved summaries go to the site and to Slack; raw data, credentials and backups stay local.

This is a written process, not an installed scheduler.

## 21.8 Evidence and limits

| Item | Evidence in the reference | Limit |
|---|---|---|
| Project CTOs | Several created; one bot-to-CTO round trip tested when a new project was added | The cap and the 48-hour rule are conventions; nothing stops a sixth CTO |
| Dispatch announcement and records | Thousands of recorded decisions; the inspection counts them | Only recorded decisions are counted |
| Follow-ups to writers | The wrapper's confirmation and log; offline tests in the reference | A queued message is not yet a started turn |
| Daily inspection | Runs at its three times; the summarizer has no tools | The summary can be wrong; it is a pointer, not evidence |
| Board sync | Columns and ◆ comments written through the native metadata | Board rendering bugs are upstream; the owner checks the screen |
| Cloud path rules | In use since 2026-11; the desktop sync path was checked after installation | Encryption is only as good as key handling by the owner |
| Same-evening research records | Adopted as a rule together with a one-off back-fill; the back-fill's completion was not checked for this chapter | Not automated |

See also: [4. Dispatch and routing](04-dispatch-routing.md), [6. Evidence and review](06-lifecycle-review.md), [7. Operations](07-operations.md), [14. Native orchestration](14-native-orchestration.md), [19. Three platforms](19-three-platforms.md), [20. Authority and decisions](20-authority-and-decisions.md).
