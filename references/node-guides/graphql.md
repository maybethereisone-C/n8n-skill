# GraphQL — `n8n-nodes-base.graphql`
**Type** `n8n-nodes-base.graphql` · **core**

**What:** Sends a GraphQL query or mutation to any GraphQL endpoint.

**Credentials:** Supports multiple auth types (Basic, Bearer, Header, OAuth2, etc.) or none.

**Resources / Operations:** Single operation — execute a GraphQL query.

**Key params & gotchas:**
- **HTTP Request Method**: GET or POST. POST requires selecting **Request Format**: `GraphQL (Raw)` or `JSON`.
- **Ignore SSL Issues** bypasses certificate validation.
- **Response Format**: JSON (default) or String (requires a Response Data Property Name).
- Headers are added as Name/Value pairs.
- Can be used as an AI tool node (supports `--8<-- ai-tools` snippet).

**Source:** n8n-nodes-base.graphql.md  [doc-verified]
