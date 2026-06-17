# TOTP  (`n8n-nodes-base.totp`)

- typeVersion (max): **1**  | group: transform  | trigger: no
- credentials: totpApi
- operations: generateSecret

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `operation` | Operation | options | generateSecret |  |  |
| `options` | Options | collection | SHA1 |  | op=generateSecret |
