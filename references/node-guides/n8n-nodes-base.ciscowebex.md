# Webex by Cisco — `n8n-nodes-base.ciscowebex`
**Type** `n8n-nodes-base.ciscowebex` · **action**
**What:** Manage Cisco Webex meetings and messages (CRUD).
**Credentials:** ciscoWebexOAuth2Api.

## Resources / Operations
| Resource | Operations |
|---|---|
| Meeting | Create, Delete, Get, Get All, Update |
| Message | Create, Delete, Get, Get All, Update |

## Key params & gotchas
- Webex meetings require `start`/`end` times in ISO 8601 UTC; timezone mismatches silently create wrong-time meetings.
- Message `Create` can target a room ID or a person email — pick one, not both.
- "Operation not supported" error surfaces when the API endpoint is unavailable for your Webex plan tier.

**Source:** n8n-nodes-base.ciscowebex.md  [doc-verified]
