# Help Scout — `n8n-nodes-base.helpscout`
**Type** `n8n-nodes-base.helpscout` · **typeVersion** 1 · **action**
**What:** Manage Help Scout conversations, customers, mailboxes, and chat threads.
**Credentials:** `helpScoutOAuth2Api` (OAuth2).

## Resources / Operations
| Resource | Operations |
|---|---|
| Conversation | Create, Delete, Get, Get All |
| Customer | Create, Get, Get All, Get Property Definitions, Update |
| Mailbox | Get, Get All |
| Thread | Create (chat thread), Get All (chat threads) |

## Key params & gotchas
- **Conversation→Create** requires a `mailboxId` and at least one thread — the conversation is not usable without a thread.
- **Customer Property Definitions** returns the schema for custom customer fields; use it to know what custom fields exist before setting them.
- Conversations cannot be **updated** via this node (only created/deleted/retrieved) — status changes require custom API calls.
- **Thread** operations only cover **chat** threads, not email threads.

**Source:** n8n-nodes-base.helpscout.md  [doc-verified]
