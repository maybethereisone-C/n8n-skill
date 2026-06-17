# Notion Trigger — `n8n-nodes-base.notionTrigger`
**Type** `n8n-nodes-base.notionTrigger` · **typeVersion** 1 · **trigger**
**What:** Polls a Notion database and fires when a page is added or updated.
**Credentials:** `notionApi` (integration token) or `notionOAuth2Api`.
**Resources / Operations:**
| Event | Notes |
|---|---|
| Page added to database | New row/page appears in the database |
| Page updated in database | Existing page's properties or content changes |

**Key params & gotchas:**
- **Polling** trigger (not webhook) — Notion's API does not support push webhooks; n8n polls at the configured interval.
- Must specify a **Database ID** — use the 32-char hex from the Notion URL or the "Share" link.
- The Notion integration must be **added to the database** (Share → Invite integration) or it will return 0 results silently.
- Poll dedupe is based on `last_edited_time`; very rapid sequential edits within the same poll window may be missed.
- Returns full page object including properties — use a Set node to extract specific property values.

**Minimal example:**
```
Notion Trigger (Database ID: abc123..., Event: Page added) 
  → Set (extract $json.properties.Name.title[0].text.content)
```

**Source:** n8n-nodes-base.notiontrigger.md  [doc-verified]
