# Session recovery checklist

> Operations supervisor only. Use current installed CLI help.

## 0. Establish need
- [ ] Reconnect/restore failure, exited agent or fallback shell observed; or runtime handle stale.
- [ ] This is not merely silence; lack of contact is not proof of exit.

## 1. Before action
- [ ] List/read target terminal; confirm idle/failure and no pending user draft.
- [ ] Not the other coordinator's own session.
- [ ] Follow active native Dispatch authority, if applicable.

## 2. Preserve
- [ ] Save terminal read output to a private recovery receipt directory.
- [ ] Record original session UUID, provider, model, effort, permissions and cwd.

## 3. Recover
- [ ] Same UUID is not already running elsewhere.
- [ ] Use original UUID and provider resume; preserve configuration.
- [ ] If needed, create one terminal in the exact workspace with the resume command.
- [ ] Wait for tui-idle; inspect satisfied=true before input.

## 4. Verify
- [ ] Re-list; use only replacement handle.
- [ ] Agent can access original task context; point to handoff rather than pasting all history.
- [ ] Record time, cause, action and result privately.
- [ ] Notify domain supervisor; no new project instruction unless you supervise it.

Do not replace a recoverable session without user direction, submit another draft, or restart/upgrade Orca. Use Sleep for later resumption. Supervised workers follow native stop/release/recovery rules.
