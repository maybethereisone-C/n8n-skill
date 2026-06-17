# Elastic Security — `n8n-nodes-base.elasticSecurity`
**Type** `n8n-nodes-base.elasticSecurity` · **action**
**What:** Manage Elastic Security cases, comments, tags, and connectors for SOAR/SecOps workflows.
**Credentials:** elasticSecurityApi (Kibana URL + API key or username/password).

## Resources / Operations
| Resource | Operations |
|---|---|
| Case | Create, Delete, Get, Get All, Get Activity Summary, Update |
| Case Comment | Add, Get, Get All, Remove, Update |
| Case Tag | Add, Remove |
| Connector | Create |

## Key params & gotchas
- Operates against the **Kibana Cases API**, not the Elasticsearch API — the host URL must point to Kibana (port 5601 by default), not Elasticsearch (9200).
- **Case Get All** supports filtering by status, tags, and assignees.
- **Connector Create** sets up an action connector (e.g., ServiceNow, Jira) for case escalation — requires the connector type and its configuration.
- Case IDs are UUIDs; use Get All to discover them dynamically.

**Source:** n8n-nodes-base.elasticsecurity.md  [doc-verified]
