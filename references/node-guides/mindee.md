# Mindee — `n8n-nodes-base.mindee`
**Type** `n8n-nodes-base.mindee` · **typeVersion** 1 · **action**
**What:** Extract structured data from invoices and receipts using Mindee's document AI (OCR + ML parsing).
**Credentials:** Mindee API key (`mindeeApi`).
**Resources / Operations:**
| Resource | Operations |
|---|---|
| Invoice | Predict |
| Receipt | Predict |

**Key params & gotchas:**
- **Predict** sends a document (PDF or image binary) to Mindee and returns structured fields: line items, totals, dates, vendor info, etc.
- Pass the document as binary data from a previous node (e.g., HTTP Request downloading a PDF).
- Mindee bills per page; multipage PDFs consume multiple API credits.

**Source:** n8n-nodes-base.mindee.md  [doc-verified]
