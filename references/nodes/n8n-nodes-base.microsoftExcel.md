# Microsoft Excel 365  (`n8n-nodes-base.microsoftExcel`)

- typeVersion (max): **2.2**  | group: input  | trigger: no
- credentials: microsoftExcelOAuth2Api
- resources: table, workbook, worksheet
- operations: addRow, addTable, addWorksheet, append, clear, convertToRange, deleteTable, deleteWorkbook, deleteWorksheet, getAll, getColumns, getContent, getRows, lookup, readRows, update, upsert

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | workbook |  |  |
| `notice` | This node connects to the Microsoft 365 cloud platform. Use the \ | notice |  |  |  |
