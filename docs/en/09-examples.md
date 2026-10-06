# 9. Worked examples: Website A and Research B

[English](../en/09-examples.md) | [繁體中文](../zh-TW/09-examples.md) | [Home](../../README.md)

All projects, IDs, dates and paths below are fictional. Coordinator A (Claude Code) supervises `web_sites` and `infra_ops`; B (Codex CLI) supervises `research` and `triage`. Each reviews the other's domains. Website A has a Git repository and an existing copywriting session. Research B does not yet exist.

## Example 1: Website A's homepage

### 1. Request

> Replace the homepage events with next month's three events from events.csv. Show me the result; do not publish it yet.

### 2. Route and announce

Project routing selects A as supervisor and B as reviewer. The usual session is healthy and empty, but another worktree is refactoring navigation. A chooses isolation:

```text
Decision: 4 New worktree | Website A | Homepage code changes need isolation from navigation work
```

### 3. Register

```text
T-EXAMPLE0101 | Homepage events | owner S-EXAMPLE-WEBA-2 | priority 2
due 2099-01-15 (target)
next: Implement events.csv content; attach screenshots and tests
source: User's request today
```

### 4. Dispatch

```text
Original request: [paste the request above]
Acceptance: Exactly three CSV events; usable phone/desktop layout; existing tests pass.
Read: PROJECT_ROOT_A
Write: src/sections/events/ in the new worktree; receipts/web-a-events-2099-01/
Forbidden: Deployment, remote push, main-branch merge, external messages, payment,
           accounts, other projects.
Terminals/agents: No additional ones. Concurrency 1. Existing subscription only.
Evidence: Test output, phone/desktop screenshots, changed files and SHA-256.
After delivery: Report own station as review.
```

```text
orca worktree create --name web-a-events --no-parent --agent claude --prompt "<dispatch>" --json
```

Record the actual returned workspace ID and terminal handle. Do not treat acceptance alone as proof work started.

### 5. Writer delivery

```text
state: review
summary: Three events displayed; two meaningful component tests added; all 48 tests pass.
next: Review receipts/web-a-events-2099-01/
evidence: REPORT.md with screenshots, test output and hashes
```

### 6. Independent review

A requests B to review commit `abc1234`. B finds:

```text
Medium | src/sections/events/Card.tsx:40
Evidence: UTC formatting shifts late-night local events to the next date.
Recommendation: Format in the event's intended local timezone.
Other findings: None.
```

A verifies the issue and returns it to the **same writer**. The fix becomes commit `def5678`. B reviews the changes and finds no remaining issue. A records evidence and the exact reviewed commit; preview acceptance remains pending.

### 7. User acceptance and publication

The user says: “The content is good. I will decide when it goes live.” Record `user_confirmed` for the content with its version and confirmation source. Publication is a separate `waiting_user` task because it is not yet authorized.

If the user instead says “Publish def5678 next Monday morning,” record that specific authorization and schedule the work. **Do not ask for the same authorization again.** Reconfirm only a changed version, ambiguous time or expanded scope.

## Example 2: Research B, a new topic

### 1. Request

> Compare offline synchronization approaches for small teams. I need a table next week.

### 2. Routing

A receives the request, but keyword routing selects B's research domain. A prepares a handoff rather than assigning another domain's terminals:

```text
Decision: 5 New project | Research B, supervised by B | No existing project fits
```

### 3. Takeover

B reads the handoff, creates a plain project folder, registers its domain, then opens a project session (option 3). Scope: write only `PROJECT_ROOT_B`; use public sources; no private notes or account data in additional model APIs; no service registrations or paid reports. Deliver a Markdown comparison, per-row source links and an unverified-items list.

### 4. A decision is needed

The writer identifies two materially different scopes. B creates decision `D-EXAMPLE-07`:

- Open-source only: about six approaches, faster.
- Include commercial products: about twelve, some requiring separately authorized trial accounts.
- Recommendation: open-source first; commercial research separately.

The board shows “Needs you.” The user selects open-source. Record the choice and time, then resume `working`.

### 5. Supervisor unavailable

B reaches its quota and the user asks it to rest for the day. Routing records B's unavailability and return time, making A the acting supervisor. A handles necessary questions and evidence, preserves B's organization, and hands back a checkpoint when B returns.

### 6. Writer disconnected

Operations supervisor A owns recovery even though research belongs to B. Confirm idle/failure and no draft; preserve output privately; resume the original UUID with unchanged model/permissions; get the replacement handle; notify B. Silence alone is not exit evidence.

### 7. Delivery

The writer delivers the comparison. B asks A to review; A checks three primary-source links, completeness of the unknowns list and the file hash. Record `coordinator_review`, then deliver to the user. Record `user_confirmed` only after actual user confirmation.

## Shared lessons

Announce, keep one writer, bind review to a version, separate acceptance from external action, and route work to the responsible supervisor. A handoff is not accepted until the recipient actually takes it up.
