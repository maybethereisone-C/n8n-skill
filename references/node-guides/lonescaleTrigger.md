# LoneScale Trigger — `n8n-nodes-base.lonescaleTrigger`
**Type** `n8n-nodes-base.lonescaleTrigger` · **typeVersion** 1 · **trigger**
**What:** Fires when any workflow event occurs in LoneScale (sales signal intelligence platform).
**Credentials:** `lonescaleApi` (API key).
**Resources / Operations:**
| Event | Notes |
|---|---|
| On new LoneScale event | Generic catch-all; LoneScale pushes the event payload |

**Key params & gotchas:**
- Only one event type is exposed ("On new LoneScale event") — all signal types come through the same trigger; filter by payload fields downstream.
- Pair with the LoneScale action node for creating or updating records in response.

**Source:** n8n-nodes-base.lonescaletrigger.md  [doc-verified]
