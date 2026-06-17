# Toggl Trigger — `n8n-nodes-base.togglTrigger`
**Type** `n8n-nodes-base.togglTrigger` · **typeVersion** 1 · **trigger**
**What:** Polls Toggl Track for new time entries and fires when a new entry is detected.
**Credentials:** `togglApi` (API token).
**Resources / Operations:**
| Trigger | Notes |
|---|---|
| New Time Entry | Fires when a new time entry is created in Toggl Track |

**Key params & gotchas:**
- Trigger type: **polling** — n8n polls the Toggl API on a schedule (no native webhook in Toggl Track public API).
- Poll interval is controlled by the n8n workflow's trigger schedule, not a parameter inside the node.
- Only detects **new** time entries; updates to existing entries are not surfaced.
- Toggl API rate limit: 1 request/second per token — keep poll interval reasonable (≥1 min).

**Source:** n8n-nodes-base.toggltrigger.md  [doc-verified]
