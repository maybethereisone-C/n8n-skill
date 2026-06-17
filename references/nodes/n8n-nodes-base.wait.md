# Wait  (`n8n-nodes-base.wait`)

- typeVersion (max): **1.1**  | group: organization  | trigger: no
- credentials: —

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resume` | Resume | options | timeInterval |  |  |
| `incomingAuthentication` | Authentication | options | none |  |  |
| `dateTime` | Date and Time | dateTime |  | true |  |
| `webhookNotice` | The webhook URL will be generated at run time. It can be referenced with the <strong>$execution.resumeUrl</strong> variable. Send it somewhere before getting to this node. <a href="https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.wait/?utm_source=n8n_app&utm_medium=node_settings_modal-credential_link&utm_campaign=n8n-nodes-base.wait" target="_blank">More info</a> | notice |  |  |  |
| `formNotice` | The form url will be generated at run time. It can be referenced with the <strong>$execution.resumeFormUrl</strong> variable. Send it somewhere before getting to this node. <a href="https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.wait/?utm_source=n8n_app&utm_medium=node_settings_modal-credential_link&utm_campaign=n8n-nodes-base.wait" target="_blank">More info</a> | notice |  |  |  |
| `options` | Options | collection | {} |  |  |
