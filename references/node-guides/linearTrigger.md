# Linear Trigger — `n8n-nodes-base.linearTrigger`
**Type** `n8n-nodes-base.linearTrigger` · **typeVersion** 1 · **trigger**
**What:** Fires when an issue, comment, label, cycle, or project event occurs in Linear.
**Credentials:** `linearApi` (API key or OAuth2).
**Resources / Operations:**
| Event | Notes |
|---|---|
| Issue | Created, updated, removed, assigned, etc. |
| Issue Comment | New comment on an issue |
| Comment Reaction | Emoji reaction added to a comment |
| Issue Label | Label applied or removed |
| Cycle | Sprint cycle created or updated |
| Project | Project created or updated |

**Key params & gotchas:**
- n8n registers a Linear webhook automatically; the credential must have webhook write permission.
- Each trigger node can watch only one event type — use multiple trigger nodes or a single webhook node with custom routing if you need several events.
- Linear sends a `type` field in the payload (`Issue`, `Comment`, etc.) that can be used for routing.

**Source:** n8n-nodes-base.lineartrigger.md  [doc-verified]
