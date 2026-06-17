# AWS SQS  (`n8n-nodes-base.awsSqs`)

- typeVersion (max): **1**  | group: output  | trigger: no
- credentials: —
- operations: sendMessage

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `operation` | Operation | options | sendMessage |  |  |
| `queue` | Queue Name or ID | options |  | true | op=sendMessage |
| `queueType` | Queue Type | options | standard |  |  |
| `sendInputData` | Send Input Data | boolean | true |  |  |
| `message` | Message | string |  | true | op=sendMessage |
| `messageGroupId` | Message Group ID | string |  | true |  |
| `options` | Options | collection | {} |  | op=sendMessage |
