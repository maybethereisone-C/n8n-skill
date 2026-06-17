# Microsoft Excel 365 — `n8n-nodes-base.microsoftExcel`
**Type** `n8n-nodes-base.microsoftExcel` · **typeVersion** 2 · **action**
**What:** Reads and writes Excel 365 workbooks/worksheets/tables stored in OneDrive via Microsoft Graph.
**Credentials:** `microsoftExcelOAuth2Api` (OAuth2) — requires Microsoft 365 account.

**Resources / Operations:**

| Resource | Operations |
|---|---|
| Table | Add Rows, Get Columns, Get Rows, Lookup (find row by column value) |
| Workbook | Add Worksheet, Get All Workbooks |
| Worksheet | Get All, Get Content |

**Key params & gotchas:**
- **Government Cloud**: set the appropriate Microsoft Graph API Base URL in credentials.
- Table operations require the file to have a **named Excel Table** (Insert > Table in Excel) — operating on a plain cell range is not supported; it must be a structured Table object.
- Table > Lookup searches for exact match on a column value and returns the first matching row; it does not support wildcards or ranges.
- Workbook ID: use Get All Workbooks to find the file ID, or extract it from the OneDrive/SharePoint URL.
- Worksheet > Get Content returns all used cells; for large sheets this can be a very large payload — filter downstream with a Set or Filter node.
- Files must be in OneDrive or SharePoint (Microsoft 365); local `.xlsx` files are not supported.

**Minimal example — append rows to a table:**
```json
{
  "resource": "table",
  "operation": "addRow",
  "workbookId": "<file-id>",
  "worksheetId": "Sheet1",
  "tableId": "Table1",
  "additionalFields": {},
  "values": { "Name": "Alice", "Score": 95 }
}
```

**Source:** n8n-nodes-base.microsoftexcel.md  [doc-verified]
