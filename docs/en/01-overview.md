# 1. What this handbook provides

[English](../en/01-overview.md) | [繁體中文](../zh-TW/01-overview.md) | [Home](../../README.md)

This handbook describes a **personal, two-coordinator workflow** in Orca. A user appoints two AI coding-agent sessions as coordinators. They route requests to project agents, collect evidence, and ask the other coordinator to review important work. User acceptance and authorization for external actions remain separate records.

The workflow comes from a working personal deployment. The 2026-10 edition reflects its latest changes: supervised native workers with one resident Run per coordinator (chapter 14), rule synchronization by mailbox, hard safety boundaries (§5.7), stricter acceptance language (§6.9) and a client message intake gateway (chapter 15). It has been rewritten and anonymized. “Website A” and “Research B” are fictional examples. Public repository links identify this publication; private projects, accounts, machine paths, conversations and operational IDs are not included.

## 1.1 Included and excluded

| Included | Excluded |
|---|---|
| Architecture, terminology, routing, dispatch, review and acceptance rules | The reference deployment's private automation, including `assistant.py` |
| Copyable agent rules, contract, routing example, task, dispatch, report, handoff, review and decision templates | Real configurations, logs, conversations, databases or screenshots |
| Explicit labels distinguishing conventions from implemented behavior | Guarantees about future Orca versions |
| Adoption steps, troubleshooting and a sharing checklist | Authority to submit, pay, publish or contact anyone |
| A local template-copy helper and documentation build/check tools | A running assistant service, scheduler or database |

Downloading this repository does **not** install `assistant.py`. References to that private CLI explain the reference deployment, not commands available here. The bundled `scripts/init_workspace.py` only copies templates. Orca commands require your own Orca installation.

## 1.2 Capability labels

| Label | Meaning | Example |
|---|---|---|
| **[Convention]** | Agents and people must follow a written rule; code does not enforce it | Only the domain supervisor may send project instructions |
| **[Code]** | Verified implementation performs or enforces a behavior | The reference task CLI rejects completion without evidence and a reviewer |
| **[Unknown]** | Not verified here, or dependent on version/environment | Details of the mobile app interface |

Code has two sources:

- **[Native]**: Orca or the agent CLI provides it. Check your installed `--help` and `orca skills get <name>`. The reference review used Orca CLI **1.4.220**.
- **[Custom]**: private reference-deployment code provides it. Those scripts are **not shipped** here.

A convention is not enforcement. If an agent forgets a written rule, the system may not stop it. Evidence and independent review are therefore essential.

## 1.3 Intended readers

- People with many Orca workspaces or agent terminals who need clear ownership.
- People who want different agents to check each other's work.
- People who need to distinguish “the agent finished a turn” from “I accepted the result.”

## 1.4 Reading paths

| Goal | Start here |
|---|---|
| Understand the whole workflow | Chapters 2, 4 and 6 |
| Understand IDs and terms | Chapter 3 |
| Start today | Chapter 8 and the templates |
| Follow worked examples | Chapter 9 |
| Run supervised workers in Orca | Chapter 14 |
| Take client requests through a messaging gateway | Chapter 15 |
| Diagnose problems | Chapter 11 |
| Share your own adaptation | Chapter 12 |

Number 13 belongs to Appendix A (capability matrix), which keeps its original filename so existing links stay valid; the offline reader prints it after chapter 15.

## 1.5 Terms used throughout

- **User**: the human who requests work, makes decisions, confirms personal acceptance and authorizes external actions.
- **Coordinator**: an agent session responsible for intake, routing, dispatch, tracking and evidence. The reference uses Claude Code and Codex CLI, called A and B. Their labels are organizational, not a ranking.
- **Writer**: the agent that edits the deliverable.
- **Reviewer**: someone other than the writer who checks a fixed version read-only.
- `HUB_ROOT`: your private coordinator workspace; `PROJECT_ROOT`: a project directory.
- `example.invalid`: a reserved example domain, not a real project endpoint.
- IDs such as `T-EXAMPLE0001` and `S-EXAMPLE-A` are invented placeholders.
