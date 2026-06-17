# SyncroMSP — `n8n-nodes-base.syncromsp`
**Type** `n8n-nodes-base.syncromsp` · **typeVersion** 1 · **action**
**What:** Manage SyncroMSP PSA contacts, customers, RMM alerts, and tickets for MSP workflow automation.
**Credentials:** `syncromspApi`
**Resources / Operations:**
| Resource | Operations |
|---|---|
| Contact | Create, Delete, Retrieve, Retrieve All, Update |
| Customer | Create, Delete, Retrieve, Retrieve All, Update |
| RMM | Create Alert, Delete Alert, Retrieve Alert, Retrieve All Alerts, Mute Alert |
| Ticket | Create, Delete, Retrieve, Retrieve All, Update |

**Key params & gotchas:**
- RMM Alert "Mute" silences an alert without deleting it — useful for suppressing noise during maintenance.
- Customer and Contact are separate resources; Contact records are linked to a Customer.

**Source:** n8n-nodes-base.syncromsp.md  [doc-verified]
