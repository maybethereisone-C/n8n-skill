# Form.io Trigger — `n8n-nodes-base.formIoTrigger`
**Type** `n8n-nodes-base.formIoTrigger` · **typeVersion** 1 · **trigger**
**What:** Fires on form submission events in a Form.io project form via webhook.
**Credentials:** `formIoApi`

## Events / Trigger configuration

| Param | Notes |
|---|---|
| Project Name or ID | Required — select the Form.io project |
| Form Name or ID | Required — select the form within the project |
| Trigger Events | multiOptions — select one or more: submission events (create, update, delete, etc.) |
| Simplify | Boolean (default true) — return simplified payload vs. raw |

## Key params & gotchas
- Both `projectId` and `formId` are required; the dropdowns populate from the credential.
- `events` is required and is a multiOptions field — no default; must select at least one event.
- `simple=true` strips metadata; set false to get the full Form.io submission envelope.

**Source:** n8n-nodes-base.formiotrigger.md + schema  [doc-verified]
