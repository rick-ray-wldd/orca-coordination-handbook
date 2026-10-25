# 18. Keeping coordinators responsive: inbox delivery, escalation and reminders

[English](../en/18-responsive-coordinators.md) | [繁體中文](../zh-TW/18-responsive-coordinators.md) | [Home](../../README.md)

This chapter records one evening in the reference workspace when both coordinators went quiet while requests piled up, what was found, and the layered fixes that followed. It is a **private reference architecture [Custom], not a shipped tool**. Nothing here is a script you can download. The facts about the coding-agent tools were checked against their documentation at the time, and they may change.

## 18.1 What went wrong

- **An idle agent session is not woken by mail.** A coordinator is an interactive LLM session. It acts only when something starts a turn: the owner typing, or one of its own background tasks finishing. Mailbox messages sent to its Run did not start a turn. One coordinator sat idle for about 90 minutes waiting on a single background “is the training done?” watcher, while five requests arrived in its mailbox. The other coordinator had been idle since the afternoon and missed a full evening of requests, including one later reassigned because of the silence [Convention: observed in the reference].
- **“Delivered” was not a signal.** Every message in the inbox view showed an empty delivery timestamp, including messages that had been read. An empty field therefore says nothing about whether a message arrived [Native: observed on the installed version].
- **Typing one line into the terminal woke the session at once.** The prompt was accepted and a turn started within a second. The same evening, native mailbox reminders started reaching the coordinator once it switched to consuming mail properly (§18.3), but the cause of the earlier silence was never proven.
- **Seeing mail is not handling it.** One coordinator noticed the waiting requests while doing something else, chose to finish that first, and only mentioned them. The owner had to ask twice.

## 18.2 Layers of defence

No single mechanism is trusted. Each layer catches what the one before it misses.

| Layer | Where it runs | What it does |
|---|---|---|
| 1. Read discipline | Every coordinator | Consume mail with `check`, handle it, then `--ack`. `--peek` is for looking only and never counts as handling [Convention] |
| 2. Short ACK | Every coordinator | Within 10 minutes of a new request, send one line: owner, status, ETA. Do the long work afterwards [Convention] |
| 3. Combined waits | Every coordinator | Any background wait (a build, a training run, a delivery) also watches the inbox, so no single-task wait leaves a blind period [Convention] |
| 4. Session guard | Coding-agent hooks and plugins | New mail prints a line that wakes the session; finishing a turn with unread mail is blocked once (§18.4) [Custom] |
| 5. Desk escalation | The desk's existing health job | Native doorbell at 10 minutes, a one-line terminal nudge at 15, a human alert plus a backup ACK at 30 (§18.5) [Custom] |
| 6. Health view | The desk's existing health job | Shows liveness and responsiveness separately (§18.6) [Custom] |

## 18.3 Read discipline

- Treat the mailbox as an at-least-once queue: take the oldest batch with `check`, handle every message in it (or at least send its short ACK), then `--ack` the batch. An unacknowledged batch can hold back later deliveries, so do not leave one open while doing long work [Native: see chapter 14].
- `--peek` and inbox listings are for looking. They never count as handling, and you never acknowledge on another agent's behalf.
- When something has been handled, write the reply file or reply message before acknowledging. The acknowledgement says “processed”, not “seen”.

## 18.4 Session guard (hooks and a plugin)

Both coding agents support lifecycle hooks, and one also supports plugin monitors [Native: tool documentation].

- **Monitor:** a plugin monitor starts with the session and runs in the background. Each line it prints reaches the session as a notification, which wakes an idle session. The reference monitor peeks the coordinator's Run every 60 seconds and prints one line per new message ID. It prints nothing for message IDs it has already seen.
- **Stop guard:** before a turn ends, a Stop hook peeks the mailbox. If there is unread mail, it blocks the stop once, giving the subjects and the exact `check … --ack` steps. It blocks at most once per prompt to avoid loops.
- **Scope:** both run only when the session is the coordinator of a Run (the Run's coordinator handle equals the current terminal). Workers, desks and ordinary chats are not affected. Any error lets the turn finish (fail-open).
- **Human trust step:** one agent requires the owner to review and trust a newly added hook in its own hooks menu before it runs. Do not bypass that review.
- **Limit:** a hook cannot wake a session that is already idle. That is the job of the monitor and of layer 5.

## 18.5 Desk escalation ladder

The desk's existing health job (every 5 minutes, no new daemon) tracks every request it forwarded to a coordinator.

| Time after forwarding | Action | Guard rails |
|---|---|---|
| 10 min, no reply | Native doorbell: queue a message into the coordinator's own session through the agent's queue command. The session wakes and checks its mail | Once per request; the agent's home directory must match the running session; on failure, fall through |
| 15 min, no reply | Type one line into the owner coordinator's terminal | Read the terminal twice first; skip if the owner's draft or any text is in the input box; once per request and coordinator |
| 30 min, no reply | Alert the owner in the private chat channel; ask the other coordinator to send a short “owner has not picked this up” ACK, without taking over the work | One alert per health run, at most six an hour; no other recipients |
| ETA in the reply has passed and the work is not done | Mark red and run the same ladder | Uses the same once-per-request reservation |

Implementation notes [Custom]:

- **Who owes a reply** comes from the machine-written forwarding receipts (recipient and time), not from what an LLM remembered to write in the request file. A request sent to both coordinators is tracked separately for each. Each coordinator's own reply file stops only its own ladder.
- **Intent is saved before every outward action.** After a timeout or an uncertain result the action is not repeated; a person checks the receipt instead.
- **A pause file stops the ladder.** Deleting the state file is not a way to retry, because that destroys the deduplication evidence.
- Requests that are merged, closed or notification-only are skipped. Requests whose owner cannot be determined are listed as “uncovered” in the health view, not guessed.

## 18.6 Health: liveness is not responsiveness

A green “alive” light only proves processes and routes exist. The health view therefore adds, per coordinator:

- **Oldest unanswered request**, in minutes: yellow from 10, red from 30, or red once a stated ETA has passed.
- **Oldest unread mail**, in minutes.
- **Mailbox preconditions:** whether each Run is bound to the coordinator's live terminal, whether any waiter without type filters is still running, and the age of the oldest unread message. Anything the tools cannot report is shown as “unknown”, never as healthy.

This is the queueing world's “age of the oldest message” metric, with the ETA from the short ACK serving as a lease.

## 18.7 Merging voice fragments

Spoken requests arrive in pieces: an addition, a correction, “why no reply yet?”. The desk now applies these rules [Custom]:

- A 90-second quiet window per channel and source: fragments become one request, with the latest correction taking precedence and every original kept in an appendix.
- Identical text within the deduplication window is rejected as a duplicate of the first request.
- Status pings (“any update?”) are not forwarded as new work. The desk answers from its ledger with the owner, status and ETA, and triggers an escalation check.
- Control words (cancel, urgent, stop, correction) skip the window and are handled at once.
- The cost is up to about 90 seconds of added delay, which the owner accepted.

## 18.8 Desktop automation pitfalls

These came from turning “remind me about this event” into calendar entries on a desktop computer [Convention: observed in the reference].

- **A pending consent dialog looks like a hang.** The first time an app controls another app, the operating system asks the owner to allow it. Until someone clicks, every automation call waits and then times out, with no error. For about a week this looked like “the calendar is broken”. Fix: run a five-second preflight before any write; when it stalls, alert the owner (a remote screen-sharing session is enough to click Allow). Never change privacy settings automatically.
- **Read the privacy panes before designing a route.** Folder and app-data access for one app (for example, an entry bot allowed to read the calendar app's data folder) is not the calendar permission. Writing an app's database files directly would break sync. In the reference, only the coordinator host app holds calendar, reminders and automation rights, so entry bots only forward requests.
- **Scripting quirks:** one calendar version failed when reading a calendar's own ID or properties, while event-level reads and filters worked. Read only the fields you need, and look objects up by ID instead of dumping properties.
- **One GUI operator at a time.** Take a lock before clicking, find elements by name in a fresh snapshot, retry a stale element once, and never fall back to coordinate clicks or click on an empty calendar grid. One stale click left a stray empty event behind, which was reported to the owner instead of being deleted.

## 18.9 Pattern: “remind me”

One skill handles personal reminders, whichever entry they arrive through [Custom]:

1. Only the owner's own words count. A pasted invitation or email supplies time and place, not authority.
2. Normalise to an intake record. An item with a firm start time is a calendar event; anything else is a to-do. Missing or contradictory times trigger one question, never a guess.
3. Preflight both apps (§18.8).
4. To-dos go to a reminders list shared to the owner's phone, after a duplicate check, with a readback.
5. Events go only through the single calendar writer. That writer deduplicates, creates the event, reads back the real alarms, then adds exactly one invitee (the owner's own account, under a standing authorization) and sends once. “Sent” is reported as sent, not as “received on the phone”.
6. Defaults when the owner gives none: the evening before at 20:00 plus one hour before; alarms already in the past are skipped.
7. Entry bots get a short paste-in block with a fixed request template, because they cannot create calendar entries themselves.

## 18.10 What was considered and not adopted

- An extra mailbox product: it is still pull-based, so it does not solve waking and would duplicate the native mailbox. The ack-overdue view was borrowed as an idea.
- Heavy formal verification of the coordination protocol: too much effort. The rule kept from that line of work is that **every wait needs a timeout and an escalation**.
- Fixed-interval polling loops inside the session: each poll costs a turn and does not survive a resume.

See also: [7. Operations](07-operations.md), [11. Troubleshooting](11-troubleshooting.md), [14. Native orchestration](14-native-orchestration.md), [17. Multi-bot entry channels](17-entry-channels.md).
