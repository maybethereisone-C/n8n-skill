# Kafka Trigger  (`n8n-nodes-base.kafkaTrigger`)

- typeVersion (max): **1.3**  | group: trigger  | trigger: yes
- credentials: schemaRegistryApi

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `topic` | Topic | string |  | true |  |
| `groupId` | Group ID | string |  | true |  |
| `resolveOffset` | Resolve Offset | options | onCompletion |  |  |
| `allowedStatuses` | Allowed Statuses | multiOptions |  |  |  |
| `useSchemaRegistry` | Use Schema Registry | boolean | false |  |  |
| `schemaRegistryUrl` | Schema Registry URL | string |  |  |  |
| `options` | Options | collection | {} |  |  |
| `sendInputData` | Send Input Data | boolean | true |  |  |
| `message` | Message | string |  |  |  |
| `jsonParameters` | JSON Parameters | boolean | false |  |  |
| `useKey` | Use Key | boolean | false |  |  |
| `key` | Key | string |  | true |  |
| `eventName` | Event Name | string |  | true |  |
| `headersUi` | Headers | fixedCollection | {} |  |  |
| `headerParametersJson` | Headers (JSON) | json |  |  |  |
