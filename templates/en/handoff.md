# Handoff

> Save privately under receipts/topic-date/HANDOFF.md. The recipient reads it before claiming takeover and reports from its own station.

```text
Task: <T-EXAMPLE0000>
From: <A/B/S-EXAMPLE-X> | To: <A/B/S-EXAMPLE-Y>
Reason: <unavailable / routing change / review / recovery>
Time: <local date/time>
Original request and acceptance criteria: <verbatim>
Current state: <working|review|waiting_user|blocked>
Completed: <...>
Remaining: <...>
Current single writer: <workspace/session or none>
Evidence: <artifact | path | SHA-256/commit>
Decisions: <D-EXAMPLE-00, original user choice/source/time>
Known risks and unresolved issues: <...>
Write scope: <unchanged from dispatch>
Forbidden: <...>
External authorization: <none / exact authorized action and original source>
Next:
1. Read this handoff and evidence.
2. <specific action>
3. Report own takeover.
```

Orchestration send proves enqueue, not acceptance. Prefer stable Run/Dispatch addresses over terminal-only mailboxes. Do not type into a busy session or a user draft; record pending delivery instead.
