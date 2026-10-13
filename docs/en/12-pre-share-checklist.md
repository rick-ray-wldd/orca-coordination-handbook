# 12. Before sharing your adaptation

[English](../en/12-pre-share-checklist.md) | [繁體中文](../zh-TW/12-pre-share-checklist.md) | [Home](../../README.md)

## 12.1 Separate public and private material

Prefer writing an anonymous explanation over copying private files and replacing a few strings. Names and IDs also hide in comments and changelogs. Keep public sources separate from private source indexes, evidence, conversations and personal scanning rules. Package an explicit allowlist.

**Your private denylist is itself private. Never publish it.** The generic validator shipped here cannot know your identity, colleagues or confidential project names.

## 12.2 What to inspect

| Category | Examples |
|---|---|
| Identity | Names, handles, emails, phone numbers, student/employee IDs |
| Organizations | School, department, lab, company, community |
| Relationships | Collaborators and identifying relationship descriptions |
| Projects | Private names, product codenames, course codes |
| Paths | Absolute home paths containing a username |
| IDs | Real session, task, project, workspace, terminal, message, Run or cloud IDs |
| URLs | Private/internal endpoints or unpublished deployments |
| Raw data | Screenshots, logs, database rows, settings, conversation transcripts |
| Secrets | API keys, tokens, `.env`, certificates |
| Environment | Identifying schedules, location, hardware, model/subscription details |

## 12.3 Where to look

Inspect Markdown, HTML, extracted PDF text, filenames, ZIP paths, hidden HTML, SVG text, raster EXIF, screenshot pixels, code defaults/comments and JSON changelogs. Inspect PDF metadata and disable print headers/footers that could expose a local path.

For GitHub, inspect **all Git history**, commit/tag author and committer identities, removed files, release attachments and build logs. A clean current tree does not clean an earlier commit. Start public material in a separate repository rather than reusing private history.

## 12.4 Automated checks

1. Privately list your names, handles, organizations, project names, home paths and email domains. Add patterns for real-looking task IDs, terminal/Run/message IDs, UUIDs and secrets.
2. Scan every public path and textual content, including extracted PDF text and metadata. Generic patterns complement, not replace, the personal list.
3. Check offline HTML for external asset loading, scripts and tracking. Public source/repository **navigation links** may remain; offline reading must not depend on external resources.
4. Extract the release ZIP into a temporary directory. Compare its exact file set and hashes with the frozen manifest; verify no extra private file slipped in.
5. Render PDF pages and visually inspect text, diagrams and page boundaries.
6. Test a fresh anonymous clone and the documented quickstart.

## 12.5 Final human checklist

- [ ] Examples are fictional and placeholder IDs are visibly marked.
- [ ] No personal home paths, private endpoints, original screenshots or conversations.
- [ ] Public repository/support links are intentional; sample project links use `example.invalid`.
- [ ] Environment-dependent models and capabilities are labeled accurately.
- [ ] Shipped tools actually work; private reference tools are clearly excluded.
- [ ] Private source indexes, denylist and evidence are absent from both archive and Git history.
- [ ] Commit metadata is appropriate for public use.
- [ ] Archive matches its SHA256SUMS manifest.
- [ ] The exact version being published is authorized.

Use `templates/en/pre-share-checklist.md` for a repeatable record. Automated checks reduce risk; they cannot prove the absence of every identifying inference.

## 12.6 Publishing an intake architecture

Publish anonymous architecture and illustrative templates, not a private runtime. Remove real channel/server/project IDs, source indexes, receipts, messages and identifying channel counts. For a main-source update, disclose that historical release assets omit it. Separate synthetic tests, real model calls, human Q&A, operator recovery and a fresh post-fix end-to-end action; label the last unobserved when evidence is absent.
