# Google Docs — `n8n-nodes-base.googleDocs`
**Type** `n8n-nodes-base.googleDocs` · **typeVersion** 2 · **action**
**What:** Creates, reads, and appends/updates content in Google Docs documents.
**Credentials:** `googleDocsOAuth2Api` (OAuth2) or `googleApi` (service account).

**Resources / Operations:**

| Resource | Operations |
|---|---|
| Document | Create, Get, Update |

**Key params & gotchas:**
- **Create** creates a blank document or from a title; it does NOT copy a template — for template-based docs, use Google Drive > Copy + then Update.
- **Get** returns the full document JSON (body content, lists, tables, inline objects); this is verbose — use expressions to extract the text runs.
- **Update** uses the Docs batchUpdate API under the hood; it appends text or replaces named ranges. The node's "Action" param controls what update to perform.
- Document ID is the alphanumeric string in the URL: `docs.google.com/document/d/<ID>/edit`.
- Service accounts cannot access user-owned docs unless the doc has been shared with the service account email.

**Source:** n8n-nodes-base.googledocs.md  [doc-verified]
