# Google Cloud Realtime Database — `n8n-nodes-base.googleCloudRealtimeDatabase`
**Type** `n8n-nodes-base.googleCloudRealtimeDatabase` · **typeVersion** 1 · **action**
**What:** Read, write, append, update, and delete data in Firebase Realtime Database.
**Credentials:** `googleFirebaseRealtimeDatabaseApi` (service account with Firebase Admin SDK access).

**Resources / Operations:**

| Resource | Operations |
|---|---|
| (top-level) | Write (set), Delete, Get, Append (push to list), Update (patch) |

**Key params & gotchas:**
- **Write** (set) replaces the node entirely — all existing data at that path is overwritten.
- **Append** uses Firebase `push()` — creates a new child with an auto-generated key; good for lists/queues.
- **Update** (patch) merges only the provided keys; sibling keys at the path are preserved.
- Path must start with `/` (e.g. `/users/123`); omitting the leading slash causes a 400.
- Database URL must be specified (format: `https://<project-id>.firebaseio.com` or regional variant).
- Service account must have `roles/firebasedatabase.admin` or equivalent rules configured in the Realtime Database rules.

**Source:** n8n-nodes-base.googlecloudrealtimedatabase.md  [doc-verified]
