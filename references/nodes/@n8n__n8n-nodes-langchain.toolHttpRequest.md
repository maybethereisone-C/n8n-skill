# HTTP Request Tool  (`@n8n/n8n-nodes-langchain.toolHttpRequest`)

- typeVersion (max): **1.1**  | group: output  | trigger: no
- credentials: —

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `toolDescription` | Description | string |  |  |  |
| `method` | Method | options | GET |  |  |
| `placeholderNotice` | Tip: You can use a {placeholder} for any part of the request to be filled by the model. Provide more context about them in the placeholders section | notice |  |  |  |
| `url` | URL | string |  | true |  |
| `sendQuery` | Send Query Parameters | boolean | false |  |  |
| `specifyQuery` | Specify Query Parameters |  |  |  |  |
| `parametersQuery` | Query Parameters |  |  |  |  |
| `jsonQuery` | jsonQuery |  |  |  |  |
| `sendHeaders` | Send Headers | boolean | false |  |  |
| `specifyHeaders` | Specify Headers |  |  |  |  |
| `parametersHeaders` | Header Parameters |  |  |  |  |
| `jsonHeaders` | jsonHeaders |  |  |  |  |
| `sendBody` | Send Body | boolean | false |  |  |
| `specifyBody` | Specify Body |  |  |  |  |
| `parametersBody` | Body Parameters |  |  |  |  |
| `jsonBody` | jsonBody |  |  |  |  |
