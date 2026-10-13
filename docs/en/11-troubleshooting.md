# 11. Troubleshooting

[English](../en/11-troubleshooting.md) | [繁體中文](../zh-TW/11-troubleshooting.md) | [Home](../../README.md)

| Symptom | Likely cause | Response |
|---|---|---|
| No reaction after sending | Acceptance is not a started turn | Observe `turn_started` with `--wait-submit`; do not resend on silence. Use the same request's retry ID after ambiguous transport failure |
| New agent never received prompt | TUI not ready | Wait for `tui-idle`, inspect `satisfied: true`; if still false report not started, do not force input |
| Stale/missing terminal handle | Runtime restarted | Re-list and address only the replacement |
| Extra shell after creating agent | Bare create followed by another terminal, or repo setup defaults | Prefer agent-first create; inspect any shell before closing it |
| Two sessions edit the same files | Duplicate assignment or resume | Preserve both work states; have the supervisor resolve current owner, active Dispatch, latest user instruction, liveness and uncommitted changes. Select one writer and transfer the other's work. Do not decide by age or treat silence as exit. Follow native settlement/recovery rules for supervised workers |
| Board status not visibly updated | Failed write or stale UI | Read workspace metadata to distinguish write failure from UI display; version/remote behavior may vary |
| Agent comment overwritten | Used sync prefix or recognized placeholder text | Keep manual comments outside the generated prefix namespace |
| Several sessions but one card | Workspace-level board | Use terminal-level views or a separate projection |
| Custom report revision conflict | Concurrent update | Re-run brief, read current content, then decide whether to write |
| Report asks for join | Contract changed | Read the current contract and acknowledge its actual hash |
| Task cannot become done | Missing evidence, review note or reviewer | Supply real evidence/review; never invent user confirmation |
| Coordinator implements everything | Forgot the three direct-work exceptions | Reclassify and log; check dispatch statistics |
| Both coordinators claim a task | Ambiguous or recently changed route | Query canonical routing; unresolved ownership goes to triage/user |
| Other coordinator ignores new rules | Running session did not reread them | Notify only while idle and with empty input; request acknowledgement |
| Machine slows or UI freezes | Excess sessions, memory pressure, resource exhaustion | Measure first; sleep or close completed sessions only after ownership checks; arrange restart with the user if necessary |
| `worker_done` never appears in `check` | Coordinator switched to another Run; the old Run's deliveries were fenced or are not in scope | Keep one resident Run; `run-use` the Run that owns the worker and check again; confirm no live workers before switching (§14.2) |
| `check` keeps returning the same messages | Previous batch was never acknowledged | Process the batch, then `check --ack <deliveryId>` (§14.4) |
| `worker-start` did not return `ready` | Agent turn never observed to start | Read `failedStage` and the recovery commands; do not substitute an invisible sub-agent |
| Worker silent for a long time | Slow, blocked on a question, or stuck | Check `worker-list` liveness/attention; `unverifiable` is not stuck; after 30 minutes with no signal while live, record a blocker and tell the user (§14.5) |
| Other coordinator never acts on a rule change | It holds no bound Run, or the message was not acknowledged | Address its resident Run; wait for an explicit “reread, version X” reply (§14.7) |
| Client reply says “done” or quotes a time without a receipt | Output guard gap | Treat as a defect; fix the guard and correct the client message with the user's approval (§15.5) |
| Many unknown inspection results | Collector failure, unreachable Orca, stale reports | Unknown is honest; fix collection and request new reports, never assume completion |
| Reviewed file differs from delivered file | Modified after review | Compare hashes and review the changed version |
| Writer says “user approved publication” | Relayed claim | Locate original authorization and verify its scope. Use it if applicable; ask only if missing or unclear |
| Copy helper refuses the destination | Directory already exists | Choose a new private folder. It intentionally never merges or overwrites |
| `python3` / build dependency missing | Runtime not installed | Copy templates manually, or install the documented optional tools |

Native flags may change. Consult your installed version's guide before recovery or command retries.
