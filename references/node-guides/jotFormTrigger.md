# Jotform Trigger — `n8n-nodes-base.jotFormTrigger`
**Type** `n8n-nodes-base.jotFormTrigger` · **typeVersion** 1 · **trigger**
**What:** Fires on new Jotform form submissions via webhook.
**Credentials:** `jotFormApi`

## Events

| Event | Notes |
|---|---|
| New Submission | Fires when a form receives a new submission |

## Key params & gotchas
- `form` — required options field; select the form by name or ID (dropdown populated from credential).
- `resolveData` — boolean (default true); resolves field IDs to human-readable labels in the output.
- `onlyAnswers` — boolean (default true); strips Jotform metadata and returns only the answer fields. Set false to get the full submission envelope (timestamps, IPs, form metadata).
- API-key auth only.

**Source:** n8n-nodes-base.jotformtrigger.md + schema  [doc-verified]
