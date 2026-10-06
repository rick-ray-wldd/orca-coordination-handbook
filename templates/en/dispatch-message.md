# Dispatch message

> Use for options 2-5. Keep every field; write “none” when not applicable.

```text
Task: <T-EXAMPLE0000> | <title>
Supervisor: <A/B> | Reviewer: <other> | User decision: <none / D-EXAMPLE-00>

Original user request: <paste verbatim>
Acceptance criteria:
1. <observable result>
2. <quality requirement>
3. <appropriate verification>

Read: <PROJECT_ROOT/...>
Write: <specific paths>; evidence: <HUB_ROOT/receipts/topic-date/>
Forbidden by default: deploy, push, merge main, external messages, public sharing,
payment, account creation, global settings, unrelated project edits.
Explicit exception: <specific authorized action, scope, original user authorization>
Data boundary: <permitted providers; prohibited data transfers>

New terminals: <no>
Additional agents: <no / at most N read-only reviewers>
Maximum concurrency: <1>
Spending: <existing subscription only; no new spending>

Required evidence: test commands/results; file paths and SHA-256 or commit;
<screenshots / rendered pages / read-back results>.

After delivery:
1. Write a short Orca workspace comment.
2. Report only your station using station-report, state review.
3. Do not claim accepted completion. Perform only the explicitly authorized
   external exception, if any; report out-of-scope findings without editing them.

If blocked: state the cause and needed actor. If waiting_user: provide options
and a recommendation; do not invent an answer.
```
