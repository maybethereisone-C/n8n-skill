# Clockify Trigger — `n8n-nodes-base.clockifyTrigger`
**Type** `n8n-nodes-base.clockifyTrigger` · **typeVersion** 1 · **trigger**

**What:** Polls Clockify for new time entries; fires when new time tracking entries are detected.

**Credentials:** `clockifyApi` (API key).

**Resources / Operations:**
| Trigger type | What fires it |
|---|---|
| Polling | New time entries detected since last poll |

**Key params & gotchas:**
- **Polling** trigger (not webhook).
- Uses the **workflow timezone** setting to interpret time entry start times — set the correct timezone in Workflow Settings to avoid missed/duplicate entries.
- Companion app node: `n8n-nodes-base.clockify`.

**Source:** n8n-nodes-base.clockifytrigger.md  [doc-verified]
