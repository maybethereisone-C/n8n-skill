# Onfleet Trigger — `n8n-nodes-base.onfleetTrigger`
**Type** `n8n-nodes-base.onfleetTrigger` · **typeVersion** 1 · **trigger**
**What:** Fires when a delivery or worker event occurs in Onfleet (last-mile logistics platform).
**Credentials:** `onfleetApi` (API key).
**Resources / Operations:**
| Event | Notes |
|---|---|
| Task Created | New delivery task added |
| Task Assigned | Task assigned to a worker |
| Task Unassigned | Assignment removed |
| Task Started | Worker started the task |
| Task Completed | Successful delivery |
| Task Failed | Failed delivery attempt |
| Task Cloned | Task duplicated |
| Task Updated | Task data changed |
| Task Delayed | ETA delayed |
| Task ETA | ETA update |
| Task Arrival | Worker arrived at destination |
| SMS Recipient Opt Out | Recipient unsubscribed from SMS |
| SMS Recipient Response Missed | SMS response not handled |
| Worker Created | New worker account |
| Worker Deleted | Worker account removed |
| Worker Duty | Worker clock-in/out |

**Key params & gotchas:**
- n8n auto-registers the Onfleet webhook on activation.
- Each trigger node can listen to one event type — chain multiple trigger nodes or use a Webhook node if you need several.
- Task payloads include `trackingURL`, worker location, and recipient details.

**Source:** n8n-nodes-base.onfleettrigger.md  [doc-verified]
