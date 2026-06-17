# Zendesk — `n8n-nodes-base.zendesk`
**Type** `n8n-nodes-base.zendesk` · **typeVersion** 1 · **action**
**What:** Create and manage tickets, ticket fields, users, and organizations in Zendesk.
**Credentials:** `zendeskApi` (subdomain + email + API token) or `zendeskOAuth2Api`.

## Resources / Operations
| Resource | Operations |
|---|---|
| Ticket | Create, Delete, Get, Get All, Recover Suspended, Update |
| Ticket Field | Get, Get All (system + custom) |
| User | Create, Delete, Get, Get All, Get Organizations, Get Related Data, Search, Update |
| Organization | Create, Delete, Count, Get, Get All, Get Related Data, Update |

## Key params & gotchas
- **Tag replacement gotcha (critical):** Updating a ticket with `Tag Names or IDs` **replaces all existing tags**. To add tags without removing existing ones: (1) fetch current tags first and merge, (2) use HTTP Request with Zendesk's `additional_tags` property, or (3) call the ticket's `/tags` endpoint directly.
- **Recover Suspended Ticket** only works for tickets in the `suspended` state.
- User Search accepts a query string using Zendesk's search syntax (e.g., `email:foo@bar.com`).
- This node supports use as an **AI tool** (can be called by AI Agent nodes).

**Source:** n8n-nodes-base.zendesk.md  [doc-verified]
