# Webflow — `n8n-nodes-base.webflow`
**Type** `n8n-nodes-base.webflow` · **typeVersion** 2 · **action**
**What:** Create, read, update, and delete CMS Collection Items in Webflow sites.
**Credentials:** `webflowOAuth2Api` (OAuth2) or `webflowApi` (API token — legacy).
**Resources / Operations:**
| Resource | Operations |
|----------|-----------|
| Item | Create, Delete, Get, Get All, Update |

**Key params & gotchas:**
- Items belong to a specific Collection within a Site — both Site ID and Collection ID are required parameters.
- Creating/updating items sets them to Draft by default; pass `"isArchived": false, "isDraft": false` plus publish via Webflow's publish API to make them live (the node does not auto-publish).
- "Get All" paginates automatically but Webflow's API has a max of 100 items per page.
- Can be used as an AI tool sub-node.
- typeVersion 2 uses OAuth2; v1 used the legacy API token.

**Source:** n8n-nodes-base.webflow.md  [doc-verified]
