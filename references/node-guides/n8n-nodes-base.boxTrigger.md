# Box Trigger — `n8n-nodes-base.boxTrigger`
**Type** `n8n-nodes-base.boxTrigger` · **typeVersion** 1 · **trigger**

**What:** Fires on file/folder activity events in Box (cloud storage and collaboration).

**Credentials:** `boxOAuth2Api` (OAuth2).

**Resources / Operations:**
| Trigger type | What fires it |
|---|---|
| Webhook | File or folder events on the configured target (upload, download, preview, move, copy, rename, delete, etc.) |

**Key params & gotchas:**
- Webhook-based. Requires a **Target ID**: the folder/file ID from the Box URL. Extract it from `https://app.box.com/folder/<TARGET_ID>`.
- Event types are selected in the n8n node configuration (not in Box directly).
- Companion app node: `n8n-nodes-base.box`.

**Source:** n8n-nodes-base.boxtrigger.md  [doc-verified]
