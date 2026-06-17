# Mattermost — `n8n-nodes-base.mattermost`
**Type** `n8n-nodes-base.mattermost` · **typeVersion** 1 · **action**
**What:** Post messages, manage channels, react to posts, and manage users in self-hosted Mattermost.
**Credentials:** `mattermostApi` (base URL + access token or username/password).

## Resources / Operations
| Resource | Operations |
|---|---|
| Channel | Add User, Create, Delete (soft), Get Members (page), Restore (un-delete), Search, Get Statistics |
| Message | Delete (soft), Post Message, Post Ephemeral Message |
| Reaction | Add Reaction, Remove Reaction, Get All Reactions |
| User | Create, Deactivate, Get All, Get by Email, Get by ID, Invite to Team |

## Key params & gotchas
- **Channel→Get Members** returns a page of members — use the **Page** and **Per Page** params for pagination; there's no single "get all" without looping.
- **Message→Post Ephemeral** sends a message visible only to a specific user in a channel — requires `user_id` and `channel_id`.
- **Channel ID** field: non-admins may see a permissions error ("You do not have the appropriate permissions") — the Mattermost admin must grant `post:channel` permission.
- Find Channel ID: select channel → channel name → **View Info** in the Mattermost UI.
- **User→Deactivate** archives the user object and revokes all sessions — not reversible via this node.
- Delete operations are **soft deletes** — posts/channels are marked deleted but remain in the database.

**Source:** n8n-nodes-base.mattermost.md  [doc-verified]
