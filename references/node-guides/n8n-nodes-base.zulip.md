# Zulip — `n8n-nodes-base.zulip`
**Type** `n8n-nodes-base.zulip` · **typeVersion** 1 · **action**
**What:** Send and manage messages, manage streams, and create/manage users in Zulip.
**Credentials:** `zulipApi` (Zulip server URL + bot email + bot API key).

## Resources / Operations
| Resource | Operations |
|---|---|
| Message | Delete, Get, Send Private Message, Send to Stream, Update, Upload File |
| Stream | Create, Delete, Get All, Get Subscribed, Update |
| User | Create, Deactivate, Get, Get All, Update |

## Key params & gotchas
- **Send to Stream** requires both a stream name and a topic; Zulip messages are always organized by topic within a stream.
- **Upload File** returns a URI that can be embedded in subsequent message content.
- **Deactivate User** (not Delete) is the correct way to remove a user — Zulip does not permanently delete users.
- Use bot credentials (not personal API keys) in production to avoid tying workflows to a personal account.

**Source:** n8n-nodes-base.zulip.md  [doc-verified]
