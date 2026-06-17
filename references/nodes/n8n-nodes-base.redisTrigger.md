# Redis Trigger  (`n8n-nodes-base.redisTrigger`)

- typeVersion (max): **1**  | group: trigger  | trigger: yes
- credentials: —
- operations: delete, get, incr, info, keys, llen, pop, publish, push, set

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `channels` | Channels | string |  | true |  |
| `options` | Options | collection | {} |  |  |
| `operation` | Operation | options | info |  |  |
| `key` | Key | string |  | true | op=delete |
| `propertyName` | Name | string | propertyName | true | op=get |
| `key` | Key | string |  | true | op=get |
| `keyType` | Key Type | options | automatic |  | op=get |
| `options` | Options | collection | {} |  | op=get |
| `key` | Key | string |  | true | op=incr |
| `expire` | Expire | boolean | false |  | op=incr |
| `ttl` | TTL | number | 60 |  | op=incr |
| `keyPattern` | Key Pattern | string |  | true | op=keys |
| `getValues` | Get Values | boolean | true |  | op=keys |
| `list` | List | string |  | true | op=llen |
| `key` | Key | string |  | true | op=set |
| `value` | Value | string |  |  | op=set |
| `keyType` | Key Type | options | automatic |  | op=set |
| `valueIsJSON` | Value Is JSON | boolean | true |  |  |
| `expire` | Expire | boolean | false |  | op=set |
| `ttl` | TTL | number | 60 |  | op=set |
| `channel` | Channel | string |  | true | op=publish |
| `messageData` | Data | string |  | true | op=publish |
| `list` | List | string |  | true | op=push,op=pop |
| `messageData` | Data | string |  | true | op=push |
| `tail` | Tail | boolean | false |  | op=push,op=pop |
| `propertyName` | Name | string | propertyName |  | op=pop |
| `options` | Options | collection | {} |  | op=pop |
