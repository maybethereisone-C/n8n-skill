# Chat  (`@n8n/n8n-nodes-langchain.chat`)

- typeVersion (max): **1.4**  | group: input  | trigger: no
- credentials: —
- operations: send

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `generalNotice` | Verify you're using a chat trigger with the 'Response Mode' option set to 'Using Response Nodes' | notice |  |  |  |
| `operation` | Operation | options | send |  |  |
| `message` | Message | string |  | true |  |
| `options` | Options | collection | {} |  |  |
| `public` | Make Chat Publicly Available | boolean | false |  |  |
| `mode` | Mode | options | hostedChat |  |  |
| `hostedChatNotice` | Chat will be live at the URL above once this workflow is published. Live executions will show up in the ‘executions’ tab | notice |  |  |  |
| `embeddedChatNotice` | Follow the instructions <a href="https://www.npmjs.com/package/@n8n/chat" target="_blank">here</a> to embed chat in a webpage (or just call the webhook URL at the top of this section). Chat will be live once you publish this workflow | notice |  |  |  |
| `authentication` | Authentication | options | none |  |  |
| `initialMessages` | Initial Message(s) | string | Hi there! 👋\nMy name is Nathan. How can I assist you today? |  |  |
| `availableInChat` | Make Available in n8n Chat Hub | boolean | false |  |  |
| `availableInChatNotice` | Your Chat Trigger node is out of date. To update, delete this node and insert a new Chat Trigger node. | notice |  |  |  |
| `agentIcon` | Agent Icon | icon |  |  |  |
| `agentName` | Agent Name | string |  |  |  |
| `agentDescription` | Agent Description | string |  |  |  |
| `suggestedPrompts` | Suggestions | fixedCollection | {} | true |  |
