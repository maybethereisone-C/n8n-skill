# LingvaNex  (`n8n-nodes-base.lingvaNex`)

- typeVersion (max): **1**  | group: output  | trigger: no
- credentials: lingvaNexApi
- operations: create, getAll, translate

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `operation` | Operation | options | translate |  |  |
| `text` | Text | string |  | true | op=translate |
| `translateTo` | Translate To | options |  | true | op=translate |
| `options` | Additional Options | collection | {} |  | op=translate |
