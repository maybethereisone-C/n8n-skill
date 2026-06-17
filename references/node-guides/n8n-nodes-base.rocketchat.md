# Rocket.Chat — `n8n-nodes-base.rocketchat`
**Type** `n8n-nodes-base.rocketchat` · **action**
**What:** Post messages to Rocket.Chat channels or send direct messages.
**Credentials:** `rocketchatApi`

## Resources / Operations
| Resource | Operation |
|----------|-----------|
| Chat | Post a message to a channel or direct message |

## Key params & gotchas
- Supports use as an AI tool node.
- Target can be a channel (`#general`) or a direct message (`@username`).
- Credentials use User ID + Auth Token (not username/password); generate from Rocket.Chat user admin panel under Personal Access Tokens.
- Supports message attachments and aliases via Additional Fields.
- Self-hosted Rocket.Chat instances require the server URL to be set in the credential.

**Source:** n8n-nodes-base.rocketchat.md  [doc-verified]
