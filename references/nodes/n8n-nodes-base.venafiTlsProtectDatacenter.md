# Venafi TLS Protect Datacenter  (`n8n-nodes-base.venafiTlsProtectDatacenter`)

- typeVersion (max): **1**  | group: input  | trigger: no
- credentials: venafiTlsProtectDatacenterApi
- resources: certificate, policy
- operations: create, delete, download, get, getMany, renew

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | certificate |  |  |
| `triggerOn` | Trigger On | options | certificateExpired | true |  |
