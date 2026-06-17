# Cockpit — `n8n-nodes-base.cockpit`
**Type** `n8n-nodes-base.cockpit` · **action**
**What:** Interact with the Cockpit headless CMS — manage collection entries, form submissions, and singletons.
**Credentials:** cockpitApi (API key + base URL).

## Resources / Operations
| Resource | Operations |
|---|---|
| Collection | Create Entry, Get All Entries, Update Entry |
| Form | Store Submission |
| Singleton | Get |

## Key params & gotchas
- **Collection name** must match exactly (case-sensitive) the collection defined in the Cockpit admin.
- **Form** Store Submission sends data to a named Cockpit form — useful for logging webhook payloads.
- **Singleton** returns a single structured document (not a list); useful for global site settings.

**Source:** n8n-nodes-base.cockpit.md  [doc-verified]
