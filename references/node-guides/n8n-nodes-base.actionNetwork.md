# Action Network — `n8n-nodes-base.actionNetwork`
**Type** `n8n-nodes-base.actionNetwork` · **typeVersion** 1 · **action**
**What:** Create, read, update, and manage people, events, petitions, attendances, tags, and signatures inside Action Network — a civic engagement platform for progressive campaigns.
**Credentials:** `actionNetworkApi`

## Resources / Operations

| Resource | Operations |
|---|---|
| Attendance | Create · Get · Get All |
| Event | Create · Get · Get All |
| Person | Create · Get · Get All · Update |
| Person Tag | Add · Remove |
| Petition | Create · Get · Get All · Update |
| Signature | Create · Get · Get All · Update |
| Tag | Create · Get · Get All |

## Key params & gotchas

- **Person Tag Add/Remove** — these are relationship operations (link a tag to a person), not tag CRUD. You need both a person identifier and a tag identifier. Don't confuse with Tag Create/Get.
- **Get All** — Action Network paginates via OSDI HAL links; n8n will handle pagination but large result sets on busy advocacy orgs can be slow. Test with a filter first.
- **Attendance** — represents a person attending a specific event; requires both an event ID and a person ID. You cannot get attendances without scoping to an event.
- **Signature** — represents a person signing a petition; similarly scoped to a petition. Creating a signature also creates the person record if they don't exist.
- **AI Tools compatible** — the doc notes this node can be used as an AI Tool within an AI agent workflow (via the `ai-tools` snippet), so it works inside LangChain-style tool nodes.
- **typeVersion is 1** — no version branching; all operations are on the single version.

## Minimal example

```json
{
  "type": "n8n-nodes-base.actionNetwork",
  "typeVersion": 1,
  "credentials": {
    "actionNetworkApi": {
      "id": "YOUR_CRED_ID",
      "name": "Action Network account"
    }
  },
  "parameters": {
    "resource": "person",
    "operation": "getAll"
  }
}
```

**Source:** `n8n-nodes-base.actionnetwork.md`  [doc-verified]
