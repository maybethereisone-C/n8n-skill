# Onfleet — `n8n-nodes-base.onfleet`
**Type** `n8n-nodes-base.onfleet` · **typeVersion** 1 · **action**
**What:** Full CRUD integration with the Onfleet last-mile delivery platform — manages admins, tasks, workers, teams, hubs, destinations, recipients, containers, and organizations.
**Credentials:** `onfleetApi` (API key).

## Resources / Operations

| Resource | Operations |
|---|---|
| Admin | Create, Delete, Get All, Update |
| Container | Add task at index (or append), Get container info, Fully replace tasks |
| Destination | Create, Get |
| Hub | Create, Get All, Update |
| Organization | Get own org details, Get delegatee org details |
| Recipient | Create, Get, Update |
| Task | Create, Clone, Force-complete, Delete, Get All, Get, Update |
| Team | Auto-dispatch to on-duty drivers, Create, Delete, Get, Get All, Get time estimates, Update |
| Worker | Create, Delete, Get, Get All, Get schedule, Update |

## Key params & gotchas

- **Container resource:** "Add task at index" appends if no index is given; "Fully replace" overwrites the entire task list for that container — use with caution.
- **Task → Force-complete:** Only works on tasks that are already in a started (active) state; attempting on an unstarted task returns an error.
- **Team → Auto-dispatch:** Triggers Onfleet's own dispatch algorithm for all pending tasks assigned to that team — does not let you control which driver gets which task.
- **Team → Get time estimates:** Returns an estimated driver along with time data; the selected driver is Onfleet's recommendation, not a confirmed assignment.
- **Organization → Get delegatee:** Requires an active Onfleet organization connection (delegatee relationship) to already exist; the node does not create connections.
- Schema confirms `resource` default is `task` — if you drop the node without changing resource, it targets tasks.

**Source:** n8n-nodes-base.onfleet.md + schema n8n-nodes-base.onfleet.md  [doc-verified]
