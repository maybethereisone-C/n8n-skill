# PhantomBuster — `n8n-nodes-base.phantombuster`
**Type** `n8n-nodes-base.phantombuster` · **action**
**What:** Manage and trigger PhantomBuster automation agents (Phantoms).
**Credentials:** `phantombusterApi`

## Resources / Operations
| Resource | Operation |
|----------|-----------|
| Agent | Delete by ID |
| Agent | Get by ID |
| Agent | Get All (organization's agents) |
| Agent | Get output of most recent container |
| Agent | Add to launch queue |

## Key params & gotchas
- "Add to launch queue" is the trigger mechanism — it queues the Phantom for the next available slot, not an immediate synchronous run.
- "Get output of most recent container" returns the last completed run's JSON output; poll after queuing if you need results.
- Agent IDs are found in the PhantomBuster dashboard URL for each Phantom.
- API key must belong to an organization admin to list all agents.

**Source:** n8n-nodes-base.phantombuster.md  [doc-verified]
