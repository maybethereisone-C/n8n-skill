# Code Tool  (`@n8n/n8n-nodes-langchain.toolCode`)

- typeVersion (max): **1.3**  | group: transform  | trigger: no
- credentials: —

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `noticeTemplateExample` | See an example of a conversational agent with custom tool written in JavaScript <a href="/templates/1963" target="_blank">here</a>. | notice |  |  |  |
| `name` | Name | string |  |  |  |
| `description` | Description | string |  |  |  |
| `language` | Language | options | javaScript |  |  |
| `jsCode` | JavaScript | string | // Example: convert the incoming query to uppercase and return it\nreturn query.toUpperCase() |  |  |
| `pythonCode` | Python | string | # Example: convert the incoming query to uppercase and return it\nreturn _query.upper() |  |  |
| `specifyInputSchema` | Specify Input Schema | boolean | false |  |  |
