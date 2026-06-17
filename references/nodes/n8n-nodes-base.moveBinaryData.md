# Convert to/from binary data  (`n8n-nodes-base.moveBinaryData`)

- typeVersion (max): **1.1**  | group: transform  | trigger: no
- credentials: —

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `mode` | Mode | options | binaryToJson |  |  |
| `setAllData` | Set All Data | boolean | true |  |  |
| `sourceKey` | Source Key | string | data | true |  |
| `destinationKey` | Destination Key | string | data | true |  |
| `convertAllData` | Convert All Data | boolean | true |  |  |
| `options` | Options | collection | utf8 |  |  |
