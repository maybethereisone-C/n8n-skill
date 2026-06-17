# MISP — `n8n-nodes-base.misp`
**Type** `n8n-nodes-base.misp` · **typeVersion** 1 · **action**
**What:** Full CRUD integration with a MISP (Malware Information Sharing Platform) instance for threat intelligence automation.
**Credentials:** MISP API key (`mispApi`) — base URL of your MISP instance + API key.
**Resources / Operations:**
| Resource | Operations |
|---|---|
| Attribute | Create, Delete, Get, Get All, Search, Update |
| Event | Create, Delete, Get, Get All, Publish, Search, Unpublish, Update |
| Event Tag | Add, Remove |
| Feed | Create, Disable, Enable, Get, Get All, Update |
| Galaxy | Delete, Get, Get All |
| Noticelist | Get, Get All |
| Object | Search |
| Organisation | Create, Delete, Get, Get All, Update |
| Tag | Create, Delete, Get All, Update |
| User | Create, Delete, Get, Get All, Update |
| Warninglist | Get, Get All |

**Key params & gotchas:**
- **Event → Publish / Unpublish** changes the distribution state; only published events are shared with connected instances.
- Attributes live inside Events; you need the Event ID to create or retrieve attributes.
- Feed operations manage the list of external MISP feeds, not the fetched data itself.
- Self-hosted MISP — ensure SSL cert is valid or configure the credential to skip verification for internal CAs.

**Source:** n8n-nodes-base.misp.md  [doc-verified]
