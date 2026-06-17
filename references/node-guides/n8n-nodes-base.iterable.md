# Iterable — `n8n-nodes-base.iterable`
**Type** `n8n-nodes-base.iterable` · **typeVersion** 1 · **action**
**What:** Manage Iterable users, user lists, and track custom events for campaign automation.
**Credentials:** `iterableApi` (API key).

## Resources / Operations
| Resource | Operations |
|---|---|
| Event | Record (track a custom event for a user) |
| User | Create/Update (upsert), Delete, Get |
| User List | Add User to List, Remove User from List |

## Key params & gotchas
- **User→Create/Update** is always an upsert keyed on `email` — if the email exists, fields are merged/updated.
- **Event→Record** tracks a named custom event against a user email; include `dataFields` (JSON object) for event properties used in campaign personalization.
- **User List** operations require the numeric `listId` — find it in Iterable's Audience → Lists section.
- Deleting a user is permanent and removes all associated event history; use with caution in production.
- Iterable is campaign-centric: users in lists trigger journeys — ensure the list ID maps to the correct campaign workflow.

**Source:** n8n-nodes-base.iterable.md  [doc-verified]
