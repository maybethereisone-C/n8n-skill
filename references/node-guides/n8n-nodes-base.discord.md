# Discord — `n8n-nodes-base.discord`
**Type** `n8n-nodes-base.discord` · **typeVersion** 2 · **action**
**What:** Send and manage Discord messages, channels, and server member roles; supports "Send and Wait" for human-in-the-loop flows.
**Credentials:** discordApi (bot token) or discordOAuth2Api.

## Resources / Operations
| Resource | Operations |
|---|---|
| Channel | Create, Delete, Get, Get Many, Update |
| Message | Delete, Get, Get Many, React with Emoji, Send, Send and Wait for Response |
| Member | Get Many, Role Add, Role Remove |

## Key params & gotchas
- **Send and Wait for Response** pauses workflow execution until a Discord user replies to the message — the reply content is injected into the next node. Requires the bot to have `MESSAGE_CONTENT` intent enabled in the Discord Developer Portal.
- Bot must be invited to the server with appropriate permissions (Send Messages, Manage Channels, Manage Roles) for each operation.
- Channel ID (not name) is required; use Channel → Get Many to look up IDs.
- **React with Emoji** requires the emoji in the format `<:name:id>` for custom emojis; standard Unicode emoji can be passed as-is (e.g., `👍`).
- Can be used as an AI tool node and HITL (human-in-the-loop) tool.
- "Operation not supported" error indicates a missing bot permission or intent.

**Source:** n8n-nodes-base.discord/index.md  [doc-verified]
