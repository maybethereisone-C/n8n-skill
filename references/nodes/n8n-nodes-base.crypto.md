# Crypto  (`n8n-nodes-base.crypto`)

- typeVersion (max): **2**  | group: transform  | trigger: no
- credentials: —

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `action` | Action | options | hash |  |  |
| `binaryData` | Binary File | boolean | false | true |  |
| `binaryPropertyName` | Binary Property Name | string | data | true |  |
| `type` | Type | options | MD5 | true |  |
| `value` | Value | string |  | true |  |
| `dataPropertyName` | Property Name | string | data | true |  |
| `encoding` | Encoding | options | hex | true |  |
| `secret` | Secret | string |  | true |  |
| `algorithm` | Algorithm Name or ID | options |  | true |  |
| `privateKey` | Private Key | string |  | true |  |
| `encodingType` | Type | options | uuid | true |  |
| `stringLength` | Length | number | 32 |  |  |
| `mode` | Mode | options | symmetric | true |  |
| `cipher` | Cipher | options | aes-256-gcm | true |  |
