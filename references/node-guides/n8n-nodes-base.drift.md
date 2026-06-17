# Drift — `n8n-nodes-base.drift`
**Type** `n8n-nodes-base.drift` · **action**
**What:** Manage Drift contacts and retrieve custom attributes.
**Credentials:** driftApi (API key) or driftOAuth2Api.

## Resources / Operations
| Resource | Operations |
|---|---|
| Contact | Create, Get Custom Attributes, Delete, Get, Update |

## Key params & gotchas
- **Get Custom Attributes** returns the schema of custom fields defined in Drift — use this to discover available attribute keys before creating/updating contacts.
- Contact identification uses Drift's internal contact ID, not email; look up the ID first if you only have an email.
- "Operation not supported" error applies to API-restricted operations on your Drift plan.

**Source:** n8n-nodes-base.drift.md  [doc-verified]
