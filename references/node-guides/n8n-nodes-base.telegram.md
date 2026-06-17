# Telegram — `n8n-nodes-base.telegram`
**Type** `n8n-nodes-base.telegram` · **typeVersion** 1.3 · **action**
**What:** Send messages, files, and media; manage chats; respond to callbacks; and download files via the Telegram Bot API.
**Credentials:** `telegramApi` (Bot token)
**Resources / Operations:**
| Resource | Operations |
|---|---|
| Chat | Get, Get Administrators, Get Member, Leave, Set Description, Set Title |
| Callback | Answer Query, Answer Inline Query |
| File | Get File |
| Message | Delete Chat Message, Edit Message Text, Pin/Unpin Chat Message, Send Animation, Send Audio, Send Chat Action, Send Document, Send Location, Send Media Group, Send Message, Send Photo, Send Sticker, Send Video, **Send and Wait for Response** |

**Key params & gotchas:**
- Bot must be added as an admin to channels/groups before it can send messages or manage chat — most common failure cause.
- **Chat ID** accepts `@channelusername` (public) or numeric ID. Use the Telegram Trigger node to get Chat ID dynamically from incoming messages.
- **Send Message** rate limit is 30 messages/second per bot. Exceed this and Telegram returns 429 errors.
- By default, Send Message appends `This message was sent automatically with n8n` — disable via Additional Fields → **Append n8n Attribution**.
- Parse Mode options: `HTML` (default), `Markdown (Legacy)`, `MarkdownV2`. MarkdownV2 requires escaping most special chars; use HTML to avoid this.
- File sends accept either a `file_id` (already on Telegram servers, recommended) or an HTTP URL. To send a local file, enable **Binary File** and provide the binary field name.
- **Send and Wait for Response** pauses workflow execution until the recipient responds (Approval / Free Text / Custom Form) — implements HITL patterns.
- Callback→Answer Inline Query: max 50 results per query; cache time defaults to 300s.
- File→Get File: enable **Download** to retrieve file binary into the workflow; without it only metadata is returned.
- Media Group supports Photo and Video types only.
- Message Thread ID param targets forum supergroup topics.
- Companion trigger: `n8n-nodes-base.telegramTrigger` — only one trigger per bot allowed at a time due to Telegram API limits.

**Source:** n8n-nodes-base.telegram/index.md + message-operations.md + chat-operations.md + callback-operations.md + file-operations.md  [doc-verified]
