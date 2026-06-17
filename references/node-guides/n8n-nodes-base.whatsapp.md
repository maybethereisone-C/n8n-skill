# WhatsApp Business Cloud — `n8n-nodes-base.whatsapp`
**Type** `n8n-nodes-base.whatsapp` · **typeVersion** 1 · **action**
**What:** Send WhatsApp messages (including templates), wait for replies (HITL), and upload/download/delete media via the WhatsApp Business Cloud API.
**Credentials:** `whatsAppApi` (Meta App access token + phone number ID).

## Resources / Operations
| Resource | Operations |
|---|---|
| Message | Send, Send and Wait for Response, Send Template |
| Media | Upload, Download, Delete |

## Key params & gotchas
- **Send Template** requires a pre-approved message template in Meta Business Manager; free-form messages can only be sent within a 24-hour customer-initiated window.
- **Send and Wait for Response** is a Human-in-the-Loop (HITL) operation — the workflow pauses until the recipient replies or a timeout is reached.
- **Media Upload** returns a `media_id` that can be referenced in subsequent Message Send calls.
- Phone number ID (not the display number) is required in the credential and message parameters.
- Production usage requires a verified Meta Business account and approved WhatsApp Business API access.

**Source:** n8n-nodes-base.whatsapp/index.md  [doc-verified]
