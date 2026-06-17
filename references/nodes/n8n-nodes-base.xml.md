# XML  (`n8n-nodes-base.xml`)

- typeVersion (max): **1**  | group: transform  | trigger: no
- credentials: —

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `mode` | Mode | options | xmlToJson |  |  |
| `xmlNotice` | If your XML is inside a binary file, use the 'Extract from File' node to convert it to text first | notice |  |  |  |
| `dataPropertyName` | Property Name | string | data | true |  |
| `options` | Options | collection | $ |  |  |
