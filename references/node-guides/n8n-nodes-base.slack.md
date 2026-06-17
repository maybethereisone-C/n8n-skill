# Slack — `n8n-nodes-base.slack`
**Type** `n8n-nodes-base.slack` · **action**
**What:** Full Slack workspace automation — channels, messages, files, reactions, stars, users, and user groups.
**Credentials:** `slackApi` (Bot Token) or `slackOAuth2Api`

## Resources / Operations
| Resource | Operation |
|----------|-----------|
| Channel | Archive, Close, Create, Get, Get Many, History, Invite, Join, Kick, Leave, Member, Open, Rename, Replies, Set Purpose, Set Topic, Unarchive |
| File | Get, Get Many, Upload |
| Message | Delete, Get Permalink, Search, Send, Send and Wait for Response, Update |
| Reaction | Add, Get, Remove |
| Star | Add, Delete, Get Many |
| User | Get, Get Many, Get Profile, Get Status, Update Profile |
| User Group | Create, Disable, Enable, Get Many, Update |

## Key params & gotchas
- Supports HITL (Human-in-the-Loop) via **Message → Send and Wait for Response** — pauses the workflow until the recipient responds in Slack.
- Each operation maps to a specific Slack API method with its own required OAuth scopes (full table in docs). Scope errors appear as `missing_scope`; add the scope to the Slack app and reinstall.
- **Message → Send**: supports blocks (rich layout), attachments, thread replies (`thread_ts`), and ephemeral messages via Additional Fields.
- **File Upload**: requires binary data from a prior node; `channels` param accepts channel ID or name.
- **Channel → History** / **Message → Search**: returns paginated results; use Return All carefully on active channels.
- **Channel Create**: public vs private is set via the `isPrivate` option.
- Bot token (`xoxb-...`) is required for most operations; user tokens (`xoxp-...`) needed for star/search operations that access user-specific data.
- Slack deprecated the `files.upload` v1 endpoint in 2024 — ensure n8n version uses the new upload flow if errors arise.

**Source:** n8n-nodes-base.slack.md  [doc-verified]
