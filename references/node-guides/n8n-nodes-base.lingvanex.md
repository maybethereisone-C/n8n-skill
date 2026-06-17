# LingvaNex — `n8n-nodes-base.lingvanex`
**Type** `n8n-nodes-base.lingvanex` · **typeVersion** 1 · **action**
**What:** Translate text between languages using the LingvaNex translation API.
**Credentials:** `lingvaNexApi` (API key).

## Resources / Operations
| Resource | Operations |
|---|---|
| (flat) | Translate Data |

## Key params & gotchas
- **Translate** requires source text, source language code, and target language code (BCP 47 format, e.g. `en_EN`, `fr_FR`).
- LingvaNex supports 100+ languages including rare and regional languages — broader than Google Translate in some domains.
- Output is the translated string; no batch endpoint exposed — translate one item at a time or loop with a Split In Batches node.
- API rate limits depend on subscription tier.

**Source:** n8n-nodes-base.lingvanex.md  [doc-verified]
