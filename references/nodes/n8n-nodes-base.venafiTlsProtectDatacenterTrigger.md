# Venafi TLS Protect Datacenter Trigger  (`n8n-nodes-base.venafiTlsProtectDatacenterTrigger`)

- typeVersion (max): **1**  | group: trigger  | trigger: yes
- credentials: venafiTlsProtectDatacenterApi
- resources: certificate, policy
- operations: create, delete, download, get, getMany, renew

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `triggerOn` | Trigger On | options | certificateExpired | true |  |
| `resource` | Resource | options | certificate |  |  |
