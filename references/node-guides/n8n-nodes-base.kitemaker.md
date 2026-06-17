# Kitemaker — `n8n-nodes-base.kitemaker`
**Type** `n8n-nodes-base.kitemaker` · **typeVersion** 1 · **action**
**What:** Read org/space/user data and manage work items in Kitemaker (product management tool).
**Credentials:** `kitemakерApi` (API token).

## Resources / Operations
| Resource | Operations |
|---|---|
| Organization | Get (logged-in user's org) |
| Space | Get All (spaces in org) |
| User | Get All (users in org) |
| Work Item | Create, Get, Get All, Update |

## Key params & gotchas
- **Organization / Space / User** are read-only lookups — no create/delete for these entities.
- **Work Item→Create** requires a `spaceId` — get it via Space→Get All first.
- Work items have statuses tied to the space's workflow; setting `statusId` requires knowing the space's status IDs.
- Kitemaker uses GraphQL under the hood; error messages may reference GraphQL field names not visible in the n8n UI.

**Source:** n8n-nodes-base.kitemaker.md  [doc-verified]
