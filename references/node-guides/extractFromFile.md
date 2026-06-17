# Extract From File — `n8n-nodes-base.extractFromFile`
**Type** `n8n-nodes-base.extractFromFile` · **core**

**What:** Converts binary file data (CSV, PDF, XLSX, etc.) into JSON for downstream processing.

**Credentials:** none.

**Resources / Operations:**
| Operation | Notes |
|-----------|-------|
| Extract From CSV | Tabular → JSON row objects |
| Extract From HTML | Parses HTML file |
| Extract From JSON | Binary JSON file → parsed JSON |
| Extract From ICS | iCalendar fields |
| Extract From ODS | OpenDocument spreadsheet |
| Extract From PDF | PDF text extraction |
| Extract From RTF | Rich Text Format |
| Extract From Text File | Plain text |
| Extract From XLS | Legacy Excel |
| Extract From XLSX | Modern Excel |
| Move File to Base64 String | Binary → base64 text |

**Key params & gotchas:**
- **Input Binary Field** defaults to `data` — change if your upstream node stores the binary under a different key.
- **Destination Output Field** only appears for JSON, ICS, Text File, and Base64 operations.
- When receiving files via Webhook, enable **Raw body** in the Webhook node's Add Options or the binary data won't be present.
- Inverse node: `n8n-nodes-base.convertToFile`.

**Source:** n8n-nodes-base.extractfromfile.md  [doc-verified]
