# Mindee  (`n8n-nodes-base.mindee`)

- typeVersion (max): **3**  | group: input  | trigger: no
- credentials: mindeeInvoiceApi, mindeeReceiptApi
- resources: invoice, receipt
- operations: predict

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `apiVersion` | API Version | options | 1 |  |  |
| `resource` | Resource | options | receipt |  |  |
| `operation` | Operation | options | predict |  |  |
| `binaryPropertyName` | Input Binary Field | string | data | true | res=receipt,res=invoice,op=predict |
| `rawData` | RAW Data | boolean | false |  |  |
