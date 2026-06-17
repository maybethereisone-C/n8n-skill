# n8n Form Trigger  (`n8n-nodes-base.formTrigger`)

- typeVersion (max): **2.6**  | group: trigger  | trigger: yes
- credentials: —
- operations: completion, page

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `triggerNotice` | An n8n Form Trigger node must be set up before this node | notice |  |  |  |
| `operation` | Page Type | options | page |  |  |
| `options` | Options | collection | Your response has been recorded |  |  |
| `Basic Auth` | Authentication | options | none |  |  |
| `formNotice` | In the 'Respond to Webhook' node, select 'Respond With JSON' and set the <strong>formSubmittedText</strong> key to display a custom response in the form, or the <strong>redirectURL</strong> key to redirect users to a URL | notice |  |  |  |
