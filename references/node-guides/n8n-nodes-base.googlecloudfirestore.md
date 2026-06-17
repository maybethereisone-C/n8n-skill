# Google Cloud Firestore — `n8n-nodes-base.googleCloudFirestore`
**Type** `n8n-nodes-base.googleCloudFirestore` · **typeVersion** 1 · **action**
**What:** CRUD operations on Firestore documents and listing root collections.
**Credentials:** `googleFirebaseCloudFirestoreApi` (service account — requires Firestore API enabled).

**Resources / Operations:**

| Resource | Operations |
|---|---|
| Document | Create, Create/Update (upsert), Delete, Get, Get All (from collection), Query |
| Collection | Get All (root collections) |

**Key params & gotchas:**
- **Project ID** and **Database** (usually `(default)`) are required on every call.
- Document paths: use `collectionId/documentId` for nested paths; subcollections use `parent/docId/subcollection`.
- **Create/Update (upsert)**: merges fields if the document exists; does not replace the whole document unless you send all fields.
- **Query**: supports `where` filters with field, operator, and value; complex queries (compound `where` with range + inequality on different fields) require composite indexes in Firestore — missing indexes cause runtime errors.
- Firestore is eventually consistent for some read scenarios; for strong consistency use the default single-document Get.

**Source:** n8n-nodes-base.googlecloudfirestore.md  [doc-verified]
