# Station report

> Use at material work, results, blockers, decisions or delivery. Ordinary Q&A needs no progress report. Report your own station only.

```text
Station: <S-EXAMPLE-X> | Workspace/provider: <...>
Task: <T-EXAMPLE0000>
Last read revision: <n; re-read on conflict>
State: <inbox|planned|working|blocked|waiting_user|review|done|paused|cancelled>
Summary: <specific result, with numbers when useful>
Next: <executable step, reviewer and exact version if applicable>
Evidence: <path1; path2; required for review/done>
Blocker: <cause, required actor/action; required for blocked>
Out-of-scope findings: <report without editing>
Acceptance: unverified (a station report is always self-reported)
```

| Weak | Better |
|---|---|
| Finished | Three events displayed; 48/48 tests pass |
| Continue | Ask B to review REPORT.md at commit def5678 |
| Tested | receipts/web-a-events-2099-01/test-output.txt |
| Problem | CSV row 3 lacks a date; user must supply it |
