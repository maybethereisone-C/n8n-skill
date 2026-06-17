# Supabase — `n8n-nodes-base.supabase`
**Type** `n8n-nodes-base.supabase` · **typeVersion** 1 · **action**
**What:** Create, read, update, and delete rows in Supabase (PostgreSQL) tables via the Supabase REST API.
**Credentials:** `supabaseApi`
**Resources / Operations:**
| Resource | Operations |
|---|---|
| Row | Create, Delete, Get, Get All, Update |

**Key params & gotchas:**
- Default schema is `public`; enable **Use Custom Schema** to target other schemas.
- Row Level Security (RLS) is enabled by default on tables created via the Table Editor — queries return empty unless a policy is created for the `anon` role. This is the #1 silent failure.
- To filter by metadata (vector store metadata columns), set **Select Type** to **String** and use PostgREST filter syntax: `metadata->>age=gte.21`.
- When running n8n and Supabase in separate Docker containers, use the Supabase Kong container name (`supabase-kong:8000`) as host — `localhost` won't resolve across containers.
- The node uses the Supabase REST API (PostgREST), not direct Postgres. For complex queries, use the Postgres node instead.
- Companion trigger not available; use webhooks or polling with Get All + filter.

**Source:** n8n-nodes-base.supabase/index.md + common-issues.md  [doc-verified]
