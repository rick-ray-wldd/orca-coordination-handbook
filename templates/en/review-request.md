# Review request

```text
Task: <T-EXAMPLE0000> | Review <artifact>
Requester: <supervisor> | Reviewer: <independent coordinator/reviewer>
Target paths: <...>
Frozen version: <SHA-256 or commit>
If the target changes during review, stop and report the mismatch.
Original user request and acceptance criteria: <verbatim>
Focus:
1. Every acceptance criterion.
2. Correctness: <...>
3. Privacy, safety and external actions.
4. Changes outside assigned scope.
Rules:
- Read-only; do not edit targets or perform external actions.
- No additional agents/terminals; concurrency 1; existing subscription only.
- Findings: location, high/medium/low severity, evidence and recommendation.
- Say “No issues found” when appropriate; no quota.
- Deliver review-report to <private receipts/.../REVIEW.md>.
- Report your own station.
```
