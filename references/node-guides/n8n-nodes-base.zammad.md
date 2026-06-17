# Zammad — `n8n-nodes-base.zammad`
**Type** `n8n-nodes-base.zammad` · **typeVersion** 1 · **action**
**What:** Create and manage groups, organizations, tickets, and users in the Zammad helpdesk platform.
**Credentials:** `zammadApi` (Zammad instance URL + API token or basic auth).

## Resources / Operations
| Resource | Operations |
|---|---|
| Group | Create, Delete, Get, Get Many, Update |
| Organization | Create, Delete, Get, Get Many, Update |
| Ticket | Create, Delete, Get, Get Many, Update |
| User | Create, Delete, Get, Get Many, Get Self, Update |

## Key params & gotchas
- **Get Self** on User returns the authenticated API user's own record — useful for verifying credentials and retrieving the agent's ID.
- Ticket Create requires a valid `group_id` and `title`; without a group assignment, the ticket creation will fail.
- Zammad uses token-based auth; generate a token in Zammad under Profile → Token Access, not via username/password directly.

**Source:** n8n-nodes-base.zammad.md  [doc-verified]
