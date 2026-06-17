# RabbitMQ  (`n8n-nodes-base.rabbitmq`)

- typeVersion (max): **1.1**  | group: transform  | trigger: no
- credentials: —
- operations: deleteMessage, sendMessage

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `operation` | Operation | hidden | sendMessage |  |  |
| `deleteMessage` | Will delete an item from the queue triggered earlier in the workflow by a RabbitMQ Trigger node | notice |  |  | op=deleteMessage |
| `mode` | Mode | options | queue |  | op=deleteMessage |
| `queue` | Queue / Topic | string |  |  | op=deleteMessage |
| `exchange` | Exchange | string |  |  |  |
| `exchangeType` | Type | options | fanout |  |  |
| `routingKey` | Routing Key | string |  |  |  |
| `sendInputData` | Send Input Data | boolean | true |  | op=sendMessage |
| `message` | Message | string |  |  |  |
| `options` | Options | collection | {} |  | op=sendMessage |
| `queue` | Queue / Topic | string |  |  |  |
| `options` | Options | collection | immediately |  |  |
| `laterMessageNode` | To delete an item from the queue, insert a RabbitMQ node later in the workflow and use the 'Delete from queue' operation | notice |  |  |  |
