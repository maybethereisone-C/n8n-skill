# Elasticsearch — `n8n-nodes-base.elasticsearch`
**Type** `n8n-nodes-base.elasticsearch` · **action**
**What:** Create, read, update, and delete Elasticsearch documents and indexes.
**Credentials:** elasticsearchApi (host URL + basic auth or API key).

## Resources / Operations
| Resource | Operations |
|---|---|
| Document | Create, Delete, Get, Get All, Update |
| Index | Create, Delete, Get, Get All |

## Key params & gotchas
- **Document Get All** uses Elasticsearch's Search API under the hood — pass a query JSON body (DSL) in the "Query" field for filtered searches; omitting it returns all documents (up to size limit).
- **Document Create** without an explicit `_id` auto-generates one; supply your own ID for idempotent upserts.
- **Document Update** uses the Elasticsearch `_update` API with a `doc` partial body — not a full replace.
- Index names must be lowercase; uppercase triggers a 400 error.
- Can be used as an AI tool node.

**Source:** n8n-nodes-base.elasticsearch.md  [doc-verified]
