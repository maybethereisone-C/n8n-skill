# Mistral AI — `n8n-nodes-base.mistralAi`
**Type** `n8n-nodes-base.mistralAi` · **typeVersion** 1 · **action**
**What:** Extract text from documents and images using Mistral AI's OCR capability (`mistral-ocr-latest` model).
**Credentials:** Mistral API key (`mistralApi`).
**Resources / Operations:**
| Resource | Operations |
|---|---|
| Document | Extract Text |

**Key params & gotchas:**
- Currently supports only the `mistral-ocr-latest` model; no chat/completion operations.
- **Document Type**: `Document` (PDF) or `Image`.
- **Input Type**: `Binary Data` (pass binary from upstream node) or `URL` (fetch from remote URL).
- **Enable Batch Processing**: bundles multiple documents into one API call — reduces cost but requires setting `Batch Size`. When batch is enabled, optionally auto-delete files from Mistral Cloud after processing.
- Binary input uses the field name specified in **Input Binary Field** (default: `data`).

**Minimal example:**
```
HTTP Request (download PDF) → Mistral AI (Document / Extract Text, Binary Data)
```

**Source:** n8n-nodes-base.mistralai.md  [doc-verified]
