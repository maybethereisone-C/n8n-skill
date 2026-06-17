# CircleCI — `n8n-nodes-base.circleci`
**Type** `n8n-nodes-base.circleci` · **action**
**What:** Get or trigger CircleCI pipelines.
**Credentials:** circleciApi (API token).

## Resources / Operations
| Resource | Operations |
|---|---|
| Pipeline | Get, Get All, Trigger |

## Key params & gotchas
- **Trigger a pipeline** requires a project slug (`gh/org/repo`) and optionally a branch or tag; passing both branch and tag is an error.
- **Get All** paginates; set a reasonable limit or use "Return All" cautiously on busy projects.

**Source:** n8n-nodes-base.circleci.md  [doc-verified]
