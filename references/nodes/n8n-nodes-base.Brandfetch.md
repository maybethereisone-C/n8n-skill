# Brandfetch  (`n8n-nodes-base.Brandfetch`)

- typeVersion (max): **1**  | group: output  | trigger: no
- credentials: brandfetchApi
- operations: color, company, font, industry, logo

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `operation` | Operation | options | logo |  |  |
| `domain` | Domain | string |  | true |  |
| `download` | Download | boolean | false | true | op=logo |
| `imageTypes` | Image Type | multiOptions |  | true | op=logo |
| `imageFormats` | Image Format | multiOptions |  | true | op=logo |
