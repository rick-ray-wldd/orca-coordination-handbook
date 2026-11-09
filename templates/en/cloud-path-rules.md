# Cloud drive path rules

Illustrative rules for one shared cloud-drive root that every platform (Orca, chat, phone bot) refers to the same way. All EXAMPLE values are fictional. Keep your completed copy private.

## One address form

```text
<ROOT-EXAMPLE>/<group>/<project>/<type>/<YYYY-MM-DD_topic_description_vN.ext>
```

Example: `HQ-EXAMPLE/2-projects/website-a/media/2099-01-01_launch-demo_mobile_v1.mp4`

Messages, documents and work orders always use this address, never a machine-specific path. Group numbers match the chat channel groups.

## Groups

| Group | Contains | Chat channels |
|---|---|---|
| `00-read-first` | These rules, the project map | none |
| `1-entry` | Cross-project documents | 1- |
| `2-projects` | `website-a`, `research-b` | 2- |
| `3-partners` | `partner-x` | 3- |
| `4-study` | `courses`, `applications` | 4- |
| `5-life` | `finance`, `insurance` (non-confidential only) | 5- |
| `8-encrypted` | Encrypted bundles only | none |
| `9-archive` | Media and closed projects older than RETENTION-EXAMPLE days, by group/project | none |

Add a new project to the project map first, then create its folder. Client folders use the client's public name, not an internal code.

## Four types (create on first use)

| Type | Contents |
|---|---|
| `deliverables` | Handed over or final |
| `media` | Video, images, 3D, assets |
| `documents` | Research, specs, notes, slides |
| `receipts` | Verification evidence, screenshots, QA reports |

## File names

- `YYYY-MM-DD_topic_description_vN.ext`; take the date from the clock, do not type it.
- A new version gets a new number; never overwrite.
- No internal case codes, tool names, amounts or personal data: names are visible whenever a file is shared.

## How each platform reaches a file

| Platform | How | Can |
|---|---|---|
| Orca | Desktop sync client folder + address (streaming mode) | Read, write |
| Phone/chat bot | Its drive connection, search by name | Read only; saving goes through Orca |
| Chat (Slack) | Paste a drive link (preview); PDFs may also be posted to the project channel | View, link. The original stays in the drive |

## What may go where

| Level | Content | Rule |
|---|---|---|
| Put directly | Deliverables, media, research, public material, rule documents | Project folder |
| Only encrypted | Confidential project data, client records, personal data, grades, ID documents, finances, insurance, quotes and costs, repositories without a remote backup | Only `8-encrypted`, encrypted to the owner's public key; agents never hold the private key |
| Never | Passwords, keys, tokens, `.env`, private keys | Not even encrypted |
| Do not move | Live repository folders, `.git`, dependency folders, databases | Sync corrupts them; back code up with Git, store only encrypted bundles |

Why so strict: a bot platform's drive connection usually covers the whole account and every bot, and cannot be limited to one folder.

## Sharing and moving

- Default: shared with nobody. Sharing or a public link is an external action → decision card.
- Moving to the drive: copy → verify hash → confirm it is in the cloud → only then delete locally. Delete local copies only for media and closed projects.
- Pre-existing shared folders that must stay public are left where they are; list them here: EXISTING-SHARED-EXAMPLE.
