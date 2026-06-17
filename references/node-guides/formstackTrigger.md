# Formstack Trigger — `n8n-nodes-base.formstackTrigger`
**Type** `n8n-nodes-base.formstackTrigger` · **typeVersion** 1 · **trigger**
**What:** Fires on new form submissions from a Formstack form via webhook.
**Credentials:** `formstackApi` / `formstackOAuth2Api`

## Events

| Event | Notes |
|---|---|
| New Submission | Fires when a form receives a new submission |

## Key params & gotchas
- `authentication` — `accessToken` (default) or `oAuth2`.
- `formId` — required; select the form by name or ID from the dropdown (populated by credential).
- `simple` — boolean (default true); returns a simplified submission object; set false for the raw Formstack envelope.

**Source:** n8n-nodes-base.formstacktrigger.md + schema  [doc-verified]
