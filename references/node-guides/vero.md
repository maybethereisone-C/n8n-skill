# Vero — `n8n-nodes-base.vero`
**Type** `n8n-nodes-base.vero` · **typeVersion** 1 · **action**
**What:** Manage user profiles and track behavioral events in Vero (email marketing automation).
**Credentials:** `veroApi` (Auth Token from Vero account settings).
**Resources / Operations:**
| Resource | Operations |
|----------|-----------|
| User | Create/Update, Change identifier, Unsubscribe, Resubscribe, Delete, Add tag, Remove tag |
| Event | Track (for a specific customer) |

**Key params & gotchas:**
- "Create or Update" is an upsert — if the user ID already exists it updates, otherwise creates.
- "Change identifier" renames the user's ID; use with caution as it is permanent.
- Events are used to trigger Vero campaigns; the event name must exactly match what is configured in Vero campaign triggers.
- Tags on users can be used as segmentation filters in Vero.

**Source:** n8n-nodes-base.vero.md  [doc-verified]
