# MongoDB — `n8n-nodes-base.mongoDb`
**Type** `n8n-nodes-base.mongoDb` · **typeVersion** 1 · **action**
**What:** Full document CRUD and aggregation against MongoDB collections, plus Atlas Search index management.
**Credentials:** MongoDB connection string (`mongoDb`) — supports replica sets and Atlas clusters.
**Resources / Operations:**
| Resource | Operations |
|---|---|
| Document | Aggregate, Delete, Find, Find and Replace, Find and Update, Insert, Update |
| Search Index | Create, Drop, List, Update |

**Key params & gotchas:**
- Uses the official **MongoDB Node.js driver** — aggregation pipelines, filter queries, and update operators are passed as JSON matching the driver's native format.
- **Find and Update** / **Find and Replace** operate on the first matching document by default; use `upsert` option for insert-if-missing behavior.
- **Search Index** operations require MongoDB Atlas with Atlas Search enabled; they will fail on self-hosted MongoDB.
- Aggregation pipelines are passed as a JSON array of stage objects.
- Can be used as an AI tool node.

**Minimal example (find):**
```json
// Filter field: { "status": "active" }
// Projection: { "name": 1, "email": 1 }
```

**Source:** n8n-nodes-base.mongodb.md  [doc-verified]
