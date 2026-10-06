# Appendix A. Capability matrix

[English](../en/13-capability-matrix.md) | [繁體中文](../zh-TW/13-capability-matrix.md) | [Home](../../README.md)

The source edition checked native behavior against Orca CLI 1.4.220 help and installed `orca-cli` / `orchestration` guides. Private capabilities were checked against implementation, included tests and scheduler configuration without reading secrets. **That private code is not included.** Conventions are documented rules, not enforcement. Unknown means unverified or version-dependent.

| # | Capability | Classification | Evidence / limitation |
|---|---|---|---|
| 1 | Create worktree, agent in first terminal, initial prompt | Native | `worktree create --agent --prompt` |
| 2 | List/read/wait/send terminal; cursor reads | Native | Terminal help |
| 3 | Input acceptance/turn-start stages; wait/retry request | Native | Send help and installed guide |
| 4 | Default board columns and comments | Native | Worktree set help |
| 5 | One workspace per board card | Native observation | Version-dependent |
| 6 | Run, Task, Dispatch, messages, gates, supervised workers | Native | Orchestration guide |
| 7 | Successful send proves enqueue, not read | Native | Orchestration guide |
| 8 | Terminal-only mailbox durability warning | Native observation | Send receipt |
| 9 | Artifact publishing defaults off; human UI switch | Native | Artifact guide |
| 10 | Sleep preserves resume; close removes terminal records | Native | Terminal guide |
| 11 | Automations | Native | Suitability for a given inspection is unknown |
| 12 | Per-agent dashboard | Unknown | Experimental interface not verified |
| 13 | Mobile interface coverage | Unknown | Not verified |
| 14 | Resume original session UUID | Agent-native | Exact syntax depends on installed provider CLI |
| 15 | Exact contract SHA-256 acknowledgement | Custom | Implementation checked |
| 16 | Current contract required before reporting | Custom | Implementation checked |
| 17 | Evidence for review/done; blocker for blocked report | Custom | Field validation |
| 18 | Task completion needs review note and accepted reviewer type | Custom | Field validation |
| 19 | Revision lock and identical-report no-op | Custom | Implementation checked |
| 20 | Reports always marked unverified acceptance | Custom | Self-report distinction |
| 21 | Supplied owner must belong to project; omission allowed | Custom | Universal owner requirement remains a convention |
| 22 | Mask key-shaped text before storage | Custom | Heuristic, not complete privacy protection |
| 23 | Task → project → keyword → default routing | Custom | Implementation and tests |
| 24 | Availability failover and expiry calculation | Custom | Query-time calculation, not automatic human takeover |
| 25 | Routing lock, backup, version, changelog, validation | Custom | Supports expected-version checks |
| 26 | Five-option dispatch suggestion | Custom | Keyword heuristic; advisory |
| 27 | Decision JSONL and inspection statistics | Custom | Depends on decisions actually being recorded |
| 28 | Workload/imbalance warnings | Custom | Warns; does not block |
| 29 | 60-second collection/board sync | Custom | Reference scheduler |
| 30 | Dry-run default, changed cards only, manual-move respect | Custom | Does not automatically move completed |
| 31 | Three daily tool-disabled inspection summaries | Custom | Reference scheduler and budget controls |
| 32 | 30-minute health checks; three-hour alert cooldown | Custom | Reference scheduler |
| 33 | First-line decision | Convention | Not code-enforced |
| 34 | Three coordinator direct-work exceptions | Convention | Not code-enforced |
| 35 | Five required dispatch fields | Convention | Suggestion tool creates skeleton, not an actual-message gate |
| 36 | Only domain supervisor sends input | Convention | Not enforced by Orca terminal input |
| 37 | Operations supervisor owns recovery | Convention | Organizational boundary |
| 38 | No duplicate writer for one session | Convention | Native Dispatch authority helps only in supervised workflow |
| 39 | Specific authorization for external actions | Convention | Applicable prior authorization persists |
| 40 | Agent text/full access does not grant authorization | Convention | Check original user instruction |
| 41 | No private data in additional model APIs | Convention | Existing approved subscriptions can still be cloud services |
| 42 | Read-only, structured, severity-based review | Convention | Say when no issues were found |
| 43 | Artifact hash bound to review | Convention | No private program enforcement |
| 44 | Never invent user_confirmed | Convention | Program checks field, not truth |
| 45 | Notify other coordinator after rule changes | Convention | Not automatic |
| 46 | No endless polling | Convention | Bounded, purposeful checks |
| 47 | Read latest inspection first | Convention | Reduce duplicate collection |
| 48 | Station attribution is not spoof-proof authentication | Custom limitation | Workspace/provider checks only |
| 49 | ensure-rules can write rule adapters in registered workspaces | Custom | Backs up before updating |
| 50 | Missing cross-review alert is domain/priority/state specific | Custom | Applications, P1, waiting_user/review only |
| 51 | Evidence validation checks nonempty field, not contents | Custom limitation | Reviewer still evaluates evidence |
| 52 | Assistant task ↔ native Run/Task/Dispatch binding | Convention / gap | Record real returned IDs and receipts manually |

Publication utilities (`init_workspace.py`, validation, document building and release packaging) are separate from these 52 reference-deployment capabilities. They are included and tested in this repository; they do not implement the private assistant layer.
