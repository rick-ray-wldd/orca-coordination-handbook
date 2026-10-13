# 7. Inspections, boards, checkpoints and recovery

[English](../en/07-operations.md) | [繁體中文](../zh-TW/07-operations.md) | [Home](../../README.md)

## 7.1 Avoid endless coordinator polling

Do not continually wake an LLM to watch every terminal. Ordinary code can collect facts; a scheduled, tool-disabled model can summarize; coordinators act on user requests and meaningful handoffs [Convention]. This reduces cost, context growth and accidental input.

## 7.2 Reference background services

These were verified in one deployment. **They are examples, not recommended universal thresholds. None of these services is installed by this repository.**

| Service | Frequency | Behavior | Writes [Custom] |
|---|---|---|---|
| Collector and board sync | Every 60 seconds | Read workspace/terminal lists, reports and source timestamps; regenerate projections; update changed cards | Own database, summaries, board, and backed-up rule-entry adapters in registered workspaces; project status sources remain read-only |
| Inspection | Three fixed times daily | Read-only. Collect waiting-user, blockers, deadlines, stale reports, failed-session hints, dispatch statistics; summarize | Private latest report, inspection task, one configured notification; model has no tools and a budget; code-only fallback |
| Machine health | Every 30 minutes | Swap, pipe capacity, disk, AI-related processes and Codex session count | Notify only on threshold breach; suppress identical warnings for three hours |

Reference thresholds:

- Working/blocked station report older than 72 hours: stale-progress list.
- Deadline within three days: approaching deadline.
- Report older than 24 hours: stale in aggregate views.
- Swap >12 GB; pipe capacity <4096 bytes; free disk <25 GB; AI-related processes >200; **Codex session processes >12**: warning only, not a hard limit.

Resource limits depend on hardware and workload. The reference practice aimed for roughly ten active sessions and put finished work to sleep or closed it after ownership checks [Convention]. Read the latest inspection before repeating a full scan.

## 7.3 Workspace board

The reviewed Orca version has `todo`, `in-progress`, `in-review`, `completed`. A workspace has a card, status and short comment [Native].

```sh
orca worktree set --worktree active --workspace-status in-review --json
orca worktree set --worktree active --comment "Tests pass; review pending" --json
```

| Assistant state | Column | Suggested label |
|---|---|---|
| waiting_user | todo | Needs you |
| blocked | todo | Blocked |
| review | in-review | Review pending |
| working | in-progress | Working |
| planned | todo | Planned |
| inbox | todo | Received |
| User-confirmed completion | completed | Human move; not automatic sync |

For multiple tasks on one card, the reference ranks waiting_user, blocked, review, working, planned, inbox. Its generated comments start with `◆` and include label, task, other-task count, next action and supervisor. Agent-written comments omit that prefix, so sync preserves them while updating status. Manual moves are respected until the underlying task state changes [Custom]. Custom-column behavior is version-dependent [Unknown].

## 7.4 Small checkpoints and incremental reads

| Technique | How | Source |
|---|---|---|
| Short checkpoint | Comment after reproduction, fix, verification, handoff or blocker | Native command; timing is convention |
| Incremental terminal reading | `terminal read --cursor <n> --limit 1000 --json`; follow `nextCursor` | Native |
| Unprocessed inbox batches | `orchestration check`; process before acknowledging | Native |
| Own station context | Private `brief` returns identity, hash, revision and project tasks | Custom |
| Summary before raw output | Latest inspection → task list → necessary terminal | Convention |
| Identical reports no-op | Do not rewrite unchanged content | Custom |

## 7.5 Recovery and lost contact

Recovery hints include reconnection errors, failed restore text, fallback to a shell, or a stale terminal handle. Preview-text detection is heuristic [Custom]; a stale handle error is native.

Only the operations supervisor performs recovery [Convention]:

1. Confirm the agent is idle or failed, not working and not holding a user draft.
2. Save terminal output privately as evidence.
3. Use the **original session UUID**, preserving provider, model, reasoning and permissions. Check that provider CLI's current resume syntax.
4. Ensure the UUID is not active in another terminal.
5. Re-list terminal handles; use only the replacement.
6. Record evidence and inform the project supervisor.

Silence is not proof of exit. Native orchestration requires positive evidence before stop, abandon or retry. Use workspace Sleep when intending to resume later; closing a workspace's terminals removes terminal/resume records in the reviewed version. Do not restart or upgrade Orca on behalf of this coordinator role.

If a coordinator is unavailable, record availability and the expected return; routing computes an acting coordinator [Custom], while actual takeover remains a convention. Unreachable or stale sources stay unknown, never presumed complete.

## 7.6 Synchronize rule changes

Running sessions do not automatically reread their instruction files. Since 2026-10 the reference sends a durable `status` message to the other coordinator's resident Run instead of typing into its terminal. Orca shows an idle-only pointer, never interrupts a busy pane and does not repeat itself [Native]; synchronization counts only after the recipient acknowledges and replies with the version it reread [Convention]. Details and command: §14.7. On contract changes, stations obtain the new hash through `brief` and `join` it after reading; the old hash cannot authorize a new report in the reference [Custom].

## 7.7 Existing capabilities and gaps

| Capability | Status | Qualification |
|---|---|---|
| Workspaces, terminals, board statuses/comments | Available | Native |
| Reports, tasks, evidence/review field validation | Available | Private custom code, not shipped |
| Routing, triage, validated versioned updates | Available | Private custom code |
| Collection, board sync, inspection, health alerts | Available | Private custom code |
| Dispatch statistics and direct-work flags | Partial | Accurate only if decisions are recorded |
| First-line declaration | Partial | Written convention, no program gate |
| Only supervisor sends input | Gap | Native terminal input does not enforce domain routing |
| One writer for a session | Gap for plain input | Native Dispatch authority applies only to the native supervised lifecycle |
| Artifact-hash-bound review | Gap | Template/convention, not enforced |
| Rule-change notification | Partial | Native durable mailbox and idle pointer; acknowledgement is a convention (§14.7) |
| Sharing privacy audit | Partial in this publication | Generic validator plus local private scan; no universal automatic personal-data detection |
| All progress on mobile | Unknown | Interface not verified; reference used a text summary |
| Missing intake | Gap | Chat-only requests can be forgotten; plain terminal input bypasses registration |
| Assistant task ↔ native Run/Task/Dispatch | Partial | Evidence cites report path and run/task/dispatch IDs by convention; no program binding (§14.8) |
| Stale worker heartbeat alert | Partial | Native alert exists only in the retired loop; reference uses a 30-minute checklist (§14.5) |
| Unaccepted assignments, missing owners, overdue decisions | Partial | General stale/waiting/blocker lists exist, not comprehensive detectors for each category |
| “Subscription” means “data stays local” | False | Existing agents may use cloud services |
