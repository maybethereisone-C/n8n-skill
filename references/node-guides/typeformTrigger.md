# Typeform Trigger — `n8n-nodes-base.typeformTrigger`
**Type** `n8n-nodes-base.typeformTrigger` · **typeVersion** 1 · **trigger**
**What:** Fires when a Typeform form receives a new submission, via Typeform webhook.
**Credentials:** `typeformApi` (personal access token) or `typeformOAuth2Api`.
**Resources / Operations:**
| Event | Notes |
|---|---|
| Form Submitted | Fires on every new completed form response |

**Key params & gotchas:**
- Trigger type: **webhook** — Typeform pushes the full response payload including all field answers.
- Select the specific **Form** to watch in the node parameters.
- The payload includes `form_response.answers` array with each field's `field.ref`, `type`, and value — reference fields by `ref` (stable) rather by position (fragile).
- Hidden fields are included in the payload if configured in the form.
- Typeform allows multiple webhooks per form; test and production URLs can coexist.

**Source:** n8n-nodes-base.typeformtrigger.md  [doc-verified]
