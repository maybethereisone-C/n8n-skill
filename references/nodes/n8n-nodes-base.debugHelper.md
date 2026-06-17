# DebugHelper  (`n8n-nodes-base.debugHelper`)

- typeVersion (max): **1**  | group: output  | trigger: no
- credentials: —

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `category` | Category | options | throwError |  |  |
| `throwErrorType` | Error Type | options | NodeApiError |  |  |
| `throwErrorMessage` | Error Message | string | Node has thrown an error |  |  |
| `memorySizeValue` | Memory Size to Generate | number | 10 |  |  |
| `randomDataType` | Data Type | options | user |  |  |
| `nanoidAlphabet` | NanoId Alphabet | string | 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ |  |  |
| `nanoidLength` | NanoId Length | string | 16 |  |  |
| `randomDataSeed` | Seed | string |  |  |  |
| `randomDataCount` | Number of Items to Generate | number | 10 |  |  |
| `randomDataSingleArray` | Output as Single Array | boolean | false |  |  |
