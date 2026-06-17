# HTML  (`n8n-nodes-base.html`)

- typeVersion (max): **1.2**  | group: transform  | trigger: no
- credentials: —
- operations: convertToHtmlTable, extractHtmlContent, generateHtmlTemplate

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `operation` | Operation | options | generateHtmlTemplate |  |  |
| `html` | HTML Template | string |  |  | op=generateHtmlTemplate |
| `notice` | <b>Tips</b>: Type ctrl+space for completions. Use <code>{{ }}</code> for expressions and <code>&lt;style&gt;</code> tags for CSS. JS in <code>&lt;script&gt;</code> tags is included but not executed in n8n. | notice |  |  | op=generateHtmlTemplate |
| `sourceData` | Source Data | options | json |  | op=extractHtmlContent |
| `dataPropertyName` | Input Binary Field | string | data | true | op=extractHtmlContent |
| `options` | Options | collection | {} |  | op=extractHtmlContent |
| `options` | Options | collection | {} |  | op=convertToHtmlTable |
