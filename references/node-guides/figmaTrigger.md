# Figma Trigger (Beta) — `n8n-nodes-base.figmaTrigger`
**Type** `n8n-nodes-base.figmaTrigger` · **typeVersion** 1 · **trigger**
**What:** Fires on Figma file/library events via Figma webhooks.
**Credentials:** `figmaApi` / `figmaOAuth2Api`

## Events

| Event | When it fires |
|---|---|
| File Commented | Someone posts a comment on a file |
| File Deleted | An individual file is deleted (not a whole folder) |
| File Updated | File saved (within 30 s of changes) or deleted |
| File Version Updated | A named version is created in version history |
| Library Publish | A library file is published |

## Key params & gotchas
- `teamId` — required; the Figma Team ID to scope the webhook to.
- `triggerOn` — select one of the five events.
- **Paid plan required:** Figma webhooks are unavailable on the free "Starter" plan; your team must be on the "Professional" plan or above.
- File Deleted does NOT fire for folder deletions — only individual files.
- File Updated fires on *save* (not every keystroke); a save occurs when the file closes within 30 s of edits.

**Source:** n8n-nodes-base.figmatrigger.md  [doc-verified]
