# Airtable Trigger — `n8n-nodes-base.airtableTrigger`
**Type** `n8n-nodes-base.airtableTrigger` · **typeVersion** 1 · **trigger**

**What:** Polls an Airtable table for new or updated records based on a created/last-modified field.

**Credentials:** `airtableTokenApi` (personal access token) or `airtableApi` (API key, legacy).

**Resources / Operations:**
| Event | Mechanism |
|---|---|
| New Airtable event | Polling — compares against Trigger Field timestamp |

**Key params & gotchas:**
- **Polling** trigger (not webhook). Configure **Poll Times**: every minute / hour / day / week / month / every-X / custom cron.
- **Trigger Field** must be a "Created time" or "Last modified time" field — Airtable Trigger uses it to diff what changed since the last poll.
- **Base** and **Table** accept URL or ID (e.g., `appXXX` / `tblXXX`).
- **Download Attachments** toggle: when enabled, specify comma-separated **Download Fields** (field names are case-sensitive).
- **Additional Fields → Fields**: if omitted, output contains only the Trigger Field — always specify the fields you need.
- **Formula** filter applies only in production polling, not manual test runs.
- **View ID**: restrict polling to records visible in a specific view.
- Companion app node: `n8n-nodes-base.airtable`.

**Source:** n8n-nodes-base.airtabletrigger.md  [doc-verified]
