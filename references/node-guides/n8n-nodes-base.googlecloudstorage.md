# Google Cloud Storage — `n8n-nodes-base.googleCloudStorage`
**Type** `n8n-nodes-base.googleCloudStorage` · **typeVersion** 1 · **action**
**What:** Manages GCS buckets and objects — create, read, update, delete, and list.
**Credentials:** `googleCloudStorageOAuth2Api` (OAuth2) or `googleApi` (service account).

**Resources / Operations:**

| Resource | Operations |
|---|---|
| Bucket | Create, Delete, Get, Get Many, Update |
| Object | Create, Delete, Get, Get Many, Update |

**Key params & gotchas:**
- Object > Create uploads a binary file; the input item must carry a binary property (e.g. from Read Binary File or HTTP Request).
- Object > Get downloads the object as binary data — wire to Write Binary File or subsequent nodes that consume binary.
- Bucket names are globally unique across all GCS; creation fails if name is taken.
- Object > Update only updates metadata (Content-Type, custom metadata, ACLs) — it does not replace the object body; use Create with the same name to overwrite content.
- Uniform bucket-level access vs. fine-grained ACLs affects whether per-object ACL updates work.

**Source:** n8n-nodes-base.googlecloudstorage.md  [doc-verified]
