# crowd.dev — `n8n-nodes-base.crowdDev`
**Type** `n8n-nodes-base.crowdDev` · **action**
**What:** Manage community data in crowd.dev — activities, automations, members, notes, organizations, and tasks.
**Credentials:** crowdDevApi.

## Resources / Operations
| Resource | Operations |
|---|---|
| Activity | Create or Update with Member, Create |
| Automation | Create, Destroy, Find, List, Update |
| Member | Create or Update, Delete, Find, Update |
| Note | Create, Delete, Find, Update |
| Organization | Create, Delete, Find, Update |
| Task | Create, Delete, Find, Update |

## Key params & gotchas
- **Activity Create or Update with Member** is the primary ingestion operation — it upserts both the activity and links/creates the member in one call.
- A companion trigger node exists: `n8n-nodes-base.crowdDevTrigger` for event-driven workflows.
- "Operation not supported" can appear for plan-restricted features.

**Source:** n8n-nodes-base.crowddev.md  [doc-verified]
