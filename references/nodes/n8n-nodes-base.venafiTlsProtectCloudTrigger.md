# Venafi TLS Protect Cloud Trigger  (`n8n-nodes-base.venafiTlsProtectCloudTrigger`)

- typeVersion (max): **1**  | group: trigger  | trigger: yes
- credentials: venafiTlsProtectCloudApi
- resources: certificate, certificateRequest, delete, download, get, getMany, renew
- operations: create, delete, download, get, getMany, renew

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | [] | true |  |
| `triggerOn` | Trigger On | multiOptions | [] | true |  |
