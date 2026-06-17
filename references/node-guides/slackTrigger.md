# Slack Trigger — `n8n-nodes-base.slackTrigger`
**Type** `n8n-nodes-base.slackTrigger` · **typeVersion** 1 · **trigger**
**What:** Fires on Slack workspace events (messages, reactions, new users, etc.) via Slack Events API webhook.
**Credentials:** `slackOAuth2Api` — requires a Slack App with Event Subscriptions enabled and appropriate OAuth scopes.
**Resources / Operations:**
| Event | Description |
|---|---|
| Any Event | Triggers on any Slack event |
| App Home Opened | User opens the App Home tab |
| Bot / App Mention | Bot/app mentioned in a channel |
| File Made Public | File made public |
| File Shared | File shared in a channel |
| New Message Posted to Channel | New message in a watched channel |
| New Public Channel Created | New public channel created |
| New User | New user added to workspace |
| Reaction Added | Emoji reaction added to a message |

**Key params & gotchas:**
- Trigger type: **webhook** — Slack pushes events via Events API.
- **Watch Whole Workspace**: fires one execution per event in every channel the bot is in — can generate very high volume; use with caution.
- **Channel to Watch**: select from list, by ID, or by URL (`https://app.slack.com/client/<channel-address>`).
- **Download Files**: only relevant for File Made Public / File Shared events.
- **Resolve IDs** option: converts Slack user/channel IDs to human-readable names in output.
- **Emoji Names to Filter**: comma-separated, no colons (e.g. `thumbsup,eyes`) — only for Reaction Added.
- Slack only allows one webhook URL per app — test and production URLs cannot coexist; disable production workflow before testing.
- From n8n v1.106.0: set a **Slack Signing Secret** in credentials to verify webhook authenticity.
- Required scopes at minimum: `conversations.list`, `users.list` — add event-specific scopes per event type.

**Source:** n8n-nodes-base.slacktrigger.md  [doc-verified]
