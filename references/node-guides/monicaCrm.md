# Monica CRM — `n8n-nodes-base.monicaCrm`
**Type** `n8n-nodes-base.monicaCrm` · **typeVersion** 1 · **action**
**What:** Automate personal CRM workflows in Monica: manage contacts, activities, calls, conversations, notes, tasks, reminders, tags, and journal entries.
**Credentials:** Monica CRM API token (`monicaCrmApi`).
**Resources / Operations:**
| Resource | Operations |
|---|---|
| Activity | Create, Delete, Retrieve, Retrieve All, Update |
| Call | Create, Delete, Retrieve, Retrieve All, Update |
| Contact | Create, Delete, Retrieve, Retrieve All, Update |
| Contact Field | Create, Delete, Retrieve, Update |
| Contact Tag | Add, Remove |
| Conversation | Create, Delete, Retrieve, Update |
| Conversation Message | Add message, Update message |
| Journal Entry | Create, Delete, Retrieve, Retrieve All, Update |
| Note | Create, Delete, Retrieve, Retrieve All, Update |
| Reminder | Create, Delete, Retrieve, Retrieve All, Update |
| Tag | Create, Delete, Retrieve, Retrieve All, Update |
| Task | Create, Delete, Retrieve, Retrieve All, Update |

**Key params & gotchas:**
- Monica is self-hostable; the credential requires your instance's base URL.
- Contact Fields are typed (phone, email, address, etc.) — specify the type when creating.
- Conversation Messages are sub-resources of a Conversation; create the Conversation first.

**Source:** n8n-nodes-base.monicacrm.md  [doc-verified]
