# JWT  (`n8n-nodes-base.jwt`)

- typeVersion (max): **1**  | group: transform  | trigger: no
- credentials: —
- operations: decode, sign, verify

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `operation` | Operation | options | sign |  |  |
| `useJson` | Use JSON to Build Payload | boolean | false |  | op=sign |
| `claims` | Payload Claims | collection | {} |  | op=sign |
| `claimsJson` | Payload Claims (JSON) | json | {\n  "my_field_1": "value 1",\n  "my_field_2": "value 2"\n}\n |  | op=sign |
| `headerClaims` | Header Claims (JSON) | json | {} |  | op=sign |
| `token` | Token | string |  | true | op=verify,op=decode |
| `options` | Options | collection | {} |  |  |
