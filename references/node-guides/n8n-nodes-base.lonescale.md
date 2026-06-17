# LoneScale — `n8n-nodes-base.lonescale`
**Type** `n8n-nodes-base.lonescale` · **typeVersion** 1 · **action**
**What:** Create lists and add items in LoneScale (sales prospecting / buying signal platform).
**Credentials:** `loneScaleApi` (API key).

## Resources / Operations
| Resource | Operations |
|---|---|
| List | Create |
| Item | Create |

## Key params & gotchas
- **Item→Create** requires a `listId` — create the list first or use an existing list ID.
- LoneScale items represent prospects/signals; the fields accepted depend on the list's schema configured in LoneScale.
- Very limited write-only node — no read, update, or delete operations. Use LoneScale's UI or the LoneScale Trigger node for incoming events.
- For receiving LoneScale events see `n8n-nodes-base.loneScaleTrigger`.

**Source:** n8n-nodes-base.lonescale.md  [doc-verified]
