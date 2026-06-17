# Matrix — `n8n-nodes-base.matrix`
**Type** `n8n-nodes-base.matrix` · **typeVersion** 1 · **action**
**What:** Interact with the Matrix decentralized chat protocol — send messages/media, manage rooms, and retrieve account/event data.
**Credentials:** `matrixApi` (homeserver URL + access token).

## Resources / Operations
| Resource | Operations |
|---|---|
| Account | Get Current User Info |
| Event | Get Single Event by ID |
| Media | Send Media to Room |
| Message | Send Message to Room, Get All Messages from Room |
| Room | Create Room, Invite User, Join Room, Kick User, Leave Room |
| Room Member | Get All Members |

## Key params & gotchas
- **Room** operations require a **Room ID** (format: `!roomid:server.tld`) — not the human-readable alias.
- **Media→Send Media** requires binary input from an upstream node (e.g. Read Binary File, HTTP Request); the media is uploaded to the homeserver's content repo first.
- **Message→Get All** returns messages in reverse-chronological order; use the `from` token for pagination.
- Access tokens are generated via `/_matrix/client/v3/login` — not via username/password directly in the credential; generate them first then store in the credential.
- Matrix homeserver must be reachable from the n8n instance — self-hosted Synapse or Dendrite works.

**Source:** n8n-nodes-base.matrix.md  [doc-verified]
