# Edit Image  (`n8n-nodes-base.editImage`)

- typeVersion (max): **1**  | group: transform  | trigger: no
- credentials: —
- operations: bmp, gif, information, jpeg, multiStep, png, tiff, webp

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `operation` | Operation | options | border |  |  |
| `dataPropertyName` | Property Name | string | data |  |  |
| `operations` | Operations | fixedCollection | {} |  | op=multiStep |
| `options` | Options | collection | data |  | op=information |
