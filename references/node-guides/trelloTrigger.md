# Trello Trigger — `n8n-nodes-base.trelloTrigger`
**Type** `n8n-nodes-base.trelloTrigger` · **typeVersion** 1 · **trigger**
**What:** Fires on Trello board/card/list events via Trello webhook.
**Credentials:** `trelloApi` (API key + token).
**Resources / Operations:**
| Events | Notes |
|---|---|
| All Trello actions on the model | Card created/moved/updated, list created, members added, etc. |

**Key params & gotchas:**
- Trigger type: **webhook** — Trello pushes action events for the specified **Model ID**.
- **Model ID**: the ID of any Trello model (board, list, card, user) to watch. For a list, retrieve it by opening a card in that list, appending `.json` to the card URL, and copying the `idList` field.
- A single webhook subscription covers all actions on that model; use downstream Switch/IF nodes to filter by `action.type`.
- Trello webhooks fire for both test and production URLs; unlike Slack/WhatsApp, Trello supports multiple webhook registrations per model.

**Source:** n8n-nodes-base.trellotrigger.md  [doc-verified]
