# Sentry.io — `n8n-nodes-base.sentryio`
**Type** `n8n-nodes-base.sentryio` · **action**
**What:** Manage Sentry.io error tracking — events, issues, projects, releases, organizations, and teams.
**Credentials:** `sentryIoApi` (API token) or `sentryIoOAuth2Api`

## Resources / Operations
| Resource | Operation |
|----------|-----------|
| Event | Get by ID, Get All |
| Issue | Delete, Get by ID, Get All, Update |
| Project | Create, Delete, Get by ID, Get All, Update |
| Release | Create, Delete, Get by version, Get All, Update |
| Organization | Create, Get by slug, Get All, Update |
| Team | Create, Delete, Get by slug, Get All, Update |

## Key params & gotchas
- **Issue Update** can set status (`resolved`, `ignored`, `unresolved`) and assignee — primary use case for auto-remediation workflows.
- Events are read-only; you cannot create events via API (Sentry SDKs handle ingestion).
- Organization slug and project slug are URL-identifiable: `sentry.io/organizations/<slug>/projects/<project-slug>/`.
- Release Create is used in CI/CD pipelines to associate commits with a Sentry release for source map and commit tracking.
- API token requires scopes: `event:read`, `issue:write`, `project:write`, `release:write` depending on operations used.
- Sentry Cloud and self-hosted use different base URLs — self-hosted requires custom URL in credentials.

**Source:** n8n-nodes-base.sentryio.md  [doc-verified]
