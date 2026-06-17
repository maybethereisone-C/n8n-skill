# Microsoft Agent 365 Trigger  (`@n8n/n8n-nodes-langchain.microsoftAgent365Trigger`)

- typeVersion (max): **1.1**  | group: trigger  | trigger: yes
- credentials: microsoftAgent365Api

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `previewNotice` | This is an early preview for building Agents with Microsoft Agent 365 and n8n. You need to be part of the <a href="https://adoption.microsoft.com/copilot/frontier-program/" target="_blank">Frontier preview program</a> to get early access to Microsoft Agent 365. <a href="https://github.com/microsoft/Agent365-Samples/tree/main/nodejs/n8n/sample-agent" target="_blank">Learn more</a> | notice |  |  |  |
| `systemPrompt` | System Prompt | string |  |  |  |
| `notice` | notice | notice |  |  |  |
| `needsFallback` | Enable Fallback Model | boolean | false |  |  |
| `fallbackNotice` | Connect an additional language model on the canvas to use it as a fallback if the main model fails | notice |  |  |  |
| `useMcpTools` | Enable Microsoft Work IQ Tools for A365 | boolean | false |  |  |
| `include` | Tools to Include | options | all |  |  |
| `includeTools` | Tools to Include | multiOptions | [] |  |  |
| `hasOutputParser` | Require Specific Output Format | boolean | false |  |  |
| `options` | Options | collection | Hello! I'm here to help you! |  |  |
