# Workable Trigger — `n8n-nodes-base.workableTrigger`
**Type** `n8n-nodes-base.workableTrigger` · **typeVersion** 1 · **trigger**
**What:** Fires on Workable recruiting platform events (candidate created or moved through pipeline stages).
**Credentials:** `workableApi` (API token + subdomain).
**Resources / Operations:**
| Event | Notes |
|---|---|
| Candidate Created | New candidate added to any job |
| Candidate Moved | Candidate moves to a different pipeline stage |

**Key params & gotchas:**
- Trigger type: **webhook** — Workable pushes events to n8n's webhook URL.
- **Candidate Moved** is the key event for pipeline automation — payload includes `stage.slug` (e.g. `applied`, `phone_screen`, `offer`) for routing.
- Scope can be limited to specific jobs or apply workspace-wide depending on Workable plan and API token permissions.

**Source:** n8n-nodes-base.workabletrigger.md  [doc-verified]
