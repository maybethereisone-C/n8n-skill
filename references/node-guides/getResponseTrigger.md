# GetResponse Trigger — `n8n-nodes-base.getResponseTrigger`
**Type** `n8n-nodes-base.getResponseTrigger` · **typeVersion** 1 · **trigger**
**What:** Fires on GetResponse email-marketing events (subscribes, unsubscribes, opens, clicks, survey submissions) via webhook.
**Credentials:** `getResponseApi` / `getResponseOAuth2Api`

## Events

| Event | Description |
|---|---|
| subscribed | Contact subscribes to a list |
| unsubscribed | Contact unsubscribes from a list |
| email_opened | Contact opens an email |
| email_clicked | Contact clicks a link in an email |
| survey_submitted | Contact submits a survey |

## Key params & gotchas
- `events` — multiOptions, required, no default; select at least one.
- `listIds` — optional multiOptions; scope the webhook to specific lists. Leave empty to catch events across all lists.
- `options` — additional collection for filtering.
- `authentication` — `apiKey` (default) or OAuth2.

**Source:** n8n-nodes-base.getresponsetrigger.md + schema  [doc-verified]
