# Kafka  (`n8n-nodes-base.kafka`)

- typeVersion (max): **1.3**  | group: transform  | trigger: no
- credentials: schemaRegistryApi

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `topic` | Topic | string |  |  |  |
| `sendInputData` | Send Input Data | boolean | true |  |  |
| `message` | Message | string |  |  |  |
| `jsonParameters` | JSON Parameters | boolean | false |  |  |
| `useSchemaRegistry` | Use Schema Registry | boolean | false |  |  |
| `schemaRegistryUrl` | Schema Registry URL | string |  |  |  |
| `useKey` | Use Key | boolean | false |  |  |
| `key` | Key | string |  | true |  |
| `eventName` | Event Name | string |  | true |  |
| `headersUi` | Headers | fixedCollection | {} |  |  |
| `headerParametersJson` | Headers (JSON) | json |  |  |  |
| `options` | Options | collection | {} |  |  |
| `groupId` | Group ID | string |  | true |  |
| `resolveOffset` | Resolve Offset | options | onCompletion |  |  |
| `allowedStatuses` | Allowed Statuses | multiOptions |  |  |  |
