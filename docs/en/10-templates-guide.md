# 10. Template index

[English](../en/10-templates-guide.md) | [繁體中文](../zh-TW/10-templates-guide.md) | [Home](../../README.md)

Templates are plain text. Replace `<placeholders>` before use. English is in `templates/en/`; Traditional Chinese is in `templates/zh-TW/`. The offline handbook includes their full text.

| File | Purpose | Used by / when |
|---|---|---|
| [AGENTS.example.md](../../templates/en/AGENTS.example.md) | Coordinator and project rules | Workspace setup |
| [CONTRACT.example.md](../../templates/en/CONTRACT.example.md) | Shared contract | All agents at session start and after updates |
| [routing.example.json](../../templates/en/routing.example.json) | Anonymous domains, precedence, dispatch and data policy | Coordinators; user adjusts |
| [task-card.md](../../templates/en/task-card.md) | Manual tracked task | Coordinator at intake |
| [dispatch-message.md](../../templates/en/dispatch-message.md) | Assignment with five required fields | Domain supervisor for options 2-5 |
| [station-report.md](../../templates/en/station-report.md) | Own-station checkpoint | Writer/coordinator on material progress |
| [handoff.md](../../templates/en/handoff.md) | Transfer context and evidence | Outgoing owner |
| [review-request.md](../../templates/en/review-request.md) | Read-only, version-bound review | Supervisor/review coordinator |
| [review-report.md](../../templates/en/review-report.md) | Findings, severity, evidence | Reviewer after checking |
| [decision-record.md](../../templates/en/decision-record.md) | User options and decision | Coordinator when waiting_user |
| [resume-recovery-checklist.md](../../templates/en/resume-recovery-checklist.md) | Safe session recovery | Operations supervisor |
| [delivery-receipt.md](../../templates/en/delivery-receipt.md) | Evidence directory guide | Writer on delivery |
| [pre-share-checklist.md](../../templates/en/pre-share-checklist.md) | Privacy and packaging checks | Anyone before sharing |

## Practical rules

Keep the exclusions field even when the task appears simple. “No external actions” records a considered boundary; a blank field does not. Evidence fields need paths and results, not just “tested.” Adapt domain assignments, model choices and limits to your own environment. Recheck privacy after personalizing templates.

For dedicated-channel design, use [channel-intake-record.md](../../templates/en/channel-intake-record.md): an operator worksheet for anonymous bindings, receipt and delivery evidence. It is illustrative and non-executable, not gateway configuration (chapter 16).
