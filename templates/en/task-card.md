# Task card

> Use in private HUB_ROOT/tasks.md when there is no custom task CLI. Register work needing cross-turn tracking.

```text
Task: <T-EXAMPLE0000> | <title>
Project: <P-EXAMPLE-XXX> | Domain: <domain> | Supervisor: <A/B> | Reviewer: <B/A>
Owner station: <S-EXAMPLE-X>
State: <inbox|planned|working|blocked|waiting_user|review|done|paused|cancelled>
Revision: <n> | Priority: <1|2|3>
Due: <YYYY-MM-DD> | Kind: <target|confirmed_deadline|source_unverified>
Source: <original request/document and date>
Next: <concrete executable step>
Blocker: <none / cause>
Decision: <none / D-EXAMPLE-00>
Evidence: <paths; required for review/done>
Review: <note and coordinator_review / user_confirmed, with real evidence>
History:
- <date> created (inbox)
- <date> assigned to <workspace/session> (working)
```

Review requires evidence. Done requires evidence, review note and reviewer. Blocked needs a cause; waiting_user needs a clear request/decision. Only the user resumes paused work. Increment revision after reading the current version.
