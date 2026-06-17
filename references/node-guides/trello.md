# Trello — `n8n-nodes-base.trello`
**Type** `n8n-nodes-base.trello` · **typeVersion** 1 · **action**
**What:** Full Trello board automation: manage boards, lists, cards, checklists, labels, attachments, comments, and board members.
**Credentials:** Trello API key + OAuth token (`trelloApi`).
**Resources / Operations:**
| Resource | Operations |
|---|---|
| Attachment | Create, Delete, Get, Get All |
| Board | Create, Delete, Get, Update |
| Board Member | Add, Get All, Invite, Remove |
| Card | Create, Delete, Get, Update |
| Card Comment | Create, Delete, Update |
| Checklist | Create checklist, Create item, Delete checklist, Delete item, Get, Get All, Get specific, Get completed items, Update item |
| Label | Add to card, Create, Delete, Get, Get All (board), Remove from card, Update |
| List | Archive/Unarchive, Create, Get, Get All, Get All Cards, Update |

**Key params & gotchas:**
- **List ID** is not visible in the Trello UI directly. To find it: open a card in the list → append `.json` to the card URL → look for the `idList` field.
- Card **Update** accepts partial fields — only supply what you want to change.
- **Board Member → Invite** sends an email invitation; **Add** requires the member's Trello ID.
- Attachments on cards accept a URL or binary file upload.
- Can be used as an AI tool node.

**Minimal example (create card):**
```
Resource: Card | Operation: Create
Required: idList (List ID), name (card title)
Optional: desc, due, idLabels
```

**Source:** n8n-nodes-base.trello.md  [doc-verified]
