# OpenThesaurus — `n8n-nodes-base.openThesaurus`
**Type** `n8n-nodes-base.openThesaurus` · **typeVersion** 1 · **action**
**What:** Look up German-language synonyms via the OpenThesaurus API (no credentials required).
**Credentials:** None.
**Resources / Operations:**
| Operation |
|---|
| Get synonyms for a German word |

**Key params & gotchas:**
- German only — not suitable for other languages.
- The API is public and free; no rate-limiting info documented but avoid hammering it in bulk loops.
- Returns synonym groups (synsets) with similarity scores.

**Source:** n8n-nodes-base.openthesaurus.md  [doc-verified]
