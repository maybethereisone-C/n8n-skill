# Venafi TLS Protect Cloud  (`n8n-nodes-base.venafiTlsProtectCloud`)

- typeVersion (max): **1**  | group: input  | trigger: no
- credentials: venafiTlsProtectCloudApi
- resources: certificate, certificateRequest, delete, download, get, getMany, renew
- operations: create, delete, download, get, getMany, renew

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | certificateRequest |  |  |
| `triggerOn` | Trigger On | multiOptions | [] | true |  |
