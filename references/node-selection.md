# Node Selection — Pick the Right Node

> Purpose: choose the correct n8n node for a task. The #1 production rule: **prefer the dedicated built-in node over raw `httpRequest` whenever one exists.**

## THE RULE

When a dedicated node exists for a service or action, use it. Reach for `n8n-nodes-base.httpRequest` only when no dedicated node covers the need.

A dedicated node gives you, for free, what you would otherwise hand-build on top of `httpRequest`:

| Concern | Dedicated node | Raw httpRequest |
|---|---|---|
| Auth | Stored credential, OAuth refresh handled | You wire headers/tokens manually, refresh yourself |
| Pagination | Built-in (e.g. "Return All" toggle) | You loop + track cursors by hand |
| Params | Typed dropdowns, resource/operation model | Free-text URL + body, easy to typo |
| Rate limits / retries | Node-level retry + backoff options | You build retry logic in Code |
| API drift | n8n updates the node on API changes | Your URLs/fields silently break |
| Validation | `validate_node` knows the schema | No schema to validate against |

## Task → Best Node

| Task | Use this node | type |
|---|---|---|
| Send WhatsApp message | WhatsApp Business Cloud | `n8n-nodes-base.whatsApp` |
| Post to a Facebook page / FB Graph call | Facebook Graph API | `n8n-nodes-base.facebookGraphApi` |
| Send email (Gmail) | Gmail | `n8n-nodes-base.gmail` |
| Send email (Outlook/365) | Microsoft Outlook | `n8n-nodes-base.microsoftOutlook` |
| Send email (generic SMTP) | Send Email | `n8n-nodes-base.emailSend` |
| Chat — Slack | Slack | `n8n-nodes-base.slack` |
| Chat — Telegram | Telegram | `n8n-nodes-base.telegram` |
| Chat — Discord | Discord | `n8n-nodes-base.discord` |
| Spreadsheet read/write | Google Sheets | `n8n-nodes-base.googleSheets` |
| Database — Postgres | Postgres | `n8n-nodes-base.postgres` |
| Database — MySQL/MariaDB | MySQL | `n8n-nodes-base.mySql` |
| Airtable records | Airtable | `n8n-nodes-base.airtable` |
| Notion pages/DB | Notion | `n8n-nodes-base.notion` |
| Schedule a run (cron) | Schedule Trigger | `n8n-nodes-base.scheduleTrigger` |
| Receive an inbound HTTP call | Webhook | `n8n-nodes-base.webhook` |
| Reply to that inbound call | Respond to Webhook | `n8n-nodes-base.respondToWebhook` |
| Set/rename/compute fields | Edit Fields (Set) | `n8n-nodes-base.set` |
| Branch on a condition | If / Switch | `n8n-nodes-base.if` / `.switch` |
| Combine two streams | Merge | `n8n-nodes-base.merge` |
| Drop rows | Filter | `n8n-nodes-base.filter` |
| Array → items / items → array | Split Out / Aggregate | `n8n-nodes-base.splitOut` / `.aggregate` |
| Dedupe | Remove Duplicates | `n8n-nodes-base.removeDuplicates` |
| Call another workflow | Execute Sub-workflow | `n8n-nodes-base.executeWorkflow` |
| LLM agent w/ tools | AI Agent | `@n8n/n8n-nodes-langchain.agent` |
| Custom JS/Python logic | Code | `n8n-nodes-base.code` |
| Call an API with **no** dedicated node | HTTP Request | `n8n-nodes-base.httpRequest` |

(Full list: `node-catalog.md` — 565 nodes with types + maxVer.)

## When httpRequest IS the right call

Justified, not a fallback-by-laziness:

- **No dedicated node exists** for the target service (check `node-catalog.md` / `search_nodes` first).
- **Internal / private / first-party API** unique to the user's org.
- **Webhook callback** to an arbitrary URL (acking a third party, signed callbacks).
- **A specific endpoint the dedicated node doesn't expose** (rare — the dedicated node usually has a "Custom API Call" operation; prefer that, it reuses the credential).

When you do use it: attach the matching **predefined credential type** if the service has one (`httpRequest` supports auth presets) so you still get managed auth instead of pasting tokens.

## Anti-pattern: "HTTP node for everything"

Building every integration on `httpRequest` is the most common production mistake. Why it's worse:

- **Auth rots** — you hardcode tokens or re-implement OAuth refresh; the dedicated node's credential handles rotation.
- **Pagination bugs** — manual cursor loops silently truncate result sets.
- **Brittle on API changes** — provider renames a field, your workflow breaks silently; the node would have been updated upstream.
- **Unvalidatable** — `validate_workflow` / `validate_node` can't check a freeform HTTP call, so errors surface only at runtime.
- **Harder to read/maintain** — reviewers can't see intent ("Slack: post message") behind a raw URL.

## How to discover the right node

1. **Search the catalog** — grep `node-catalog.md` for the service name; copy the `type` and pin `maxVer` as `typeVersion`.
2. **`search_nodes`** (community `n8n-mcp`) — e.g. `search_nodes("whatsapp")`. ⚠️ Search/validate tools use the short form `nodes-base.whatsApp`; the **workflow JSON uses the full `n8n-nodes-base.whatsApp`**.
3. **`get_node`** — confirm operations, required params, and current max `typeVersion` before writing JSON.
4. If nothing matches → `httpRequest` (see "When justified" above).
