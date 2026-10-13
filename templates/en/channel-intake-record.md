# Dedicated-channel binding and receipt worksheet

Illustrative, non-executable design record. Not a gateway configuration, schema or installed service. All EXAMPLE values are fictional. Keep completed records private; never add credentials or raw conversations to a public copy.

## Operator-owned binding (chat cannot modify it)

- Binding revision: EXAMPLE-REVISION
- Platform/profile: Discord / default personal intake
- Allowed server/channel: SERVER-EXAMPLE / CHANNEL-EXAMPLE
- Authenticated owner: OWNER-EXAMPLE (reject every other member, bots, webhooks and system messages)
- Native project ID: NATIVE-PROJECT-EXAMPLE
- Separate private ledger project ID: P-EXAMPLE-PROJECT
- Approved workspace: PROJECT_ROOT
- Fixed sources: STATUS.md; NOTES.md (illustrative; operator must verify actual files and freshness)
- Supervisor route: COORDINATOR-EXAMPLE; current mailbox/terminal binding verification: UNKNOWN
- Initial writer owner: UNASSIGNED (later assignment must belong to the ledger project)
- Supported input: direct server-channel text without mentions; no threads/slash commands
- Cross-project input: direct the owner to the correct channel; no automatic rerouting
- Attachment policy: safe metadata only; extension does not read/execute contents or pass them to the model; upstream adapter caching remains possible

## One source message, one intake record

- Receipt: RECEIPT-EXAMPLE
- Stable source key: PLATFORM-EXAMPLE / CHANNEL-EXAMPLE / MESSAGE-EXAMPLE
- Stable task key: INTAKE-EXAMPLE (reuse during recovery)
- Sanitized request summary and private source reference: TO-BE-RECORDED
- Action intent detection: simple rules/keywords; coordinator must read actual intent
- Hold/do-not-execute: YES; preserve until explicitly changed
- Ledger task receipt: NOT-YET-CREATED
- Notification: PENDING (no send yet); native mailbox receipt: NONE
- Conversational reply delivery: NOT-ATTEMPTED (separate from notification)
- Coordinator read/accepted evidence: NONE / NONE
- Native execution Run / Task / Dispatch: NONE / NONE / NONE
- Writer result / fixed-version review / user acceptance: NONE / NONE / NONE
- External action: NONE; scoped authorization and authorized executor required

## Recovery and validation

Pending prerequisite: TO-BE-RECORDED. If a send becomes UNKNOWN, inspect its exact transport receipt before any retry; never request a duplicate message or task. Reverify the coordinator binding after session replacement. Keep supervisor routing separate from project writer membership.

Before reload: check active work, replies, pending messages, arrival spool and lock. After graceful reload: verify loaded hashes, connection and unrelated LINE profile preservation. Record evidence separately for synthetic tests, real model call, human Q&A, operator recovery and fresh end-to-end action. Unknown tiers stay unknown.
