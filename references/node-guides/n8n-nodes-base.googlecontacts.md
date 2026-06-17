# Google Contacts — `n8n-nodes-base.googleContacts`
**Type** `n8n-nodes-base.googleContacts` · **typeVersion** 1 · **action**
**What:** CRUD operations on Google Contacts (People API).
**Credentials:** `googleContactsOAuth2Api` (OAuth2).

**Resources / Operations:**

| Resource | Operations |
|---|---|
| Contact | Create, Delete, Get, Get All, Update |

**Key params & gotchas:**
- Uses the **People API** v1, not the deprecated Contacts API v3; resource names are in `people/{personId}` format.
- Get All returns contacts from the authenticated user's "My Contacts" group by default; use additional fields to filter by group or source.
- Update requires specifying which fields to update (updatePersonFields mask) — if omitted, n8n may send a partial update that clears un-mentioned fields.
- Contact photos and binary data are not handled by this node.

**Source:** n8n-nodes-base.googlecontacts.md  [doc-verified]
