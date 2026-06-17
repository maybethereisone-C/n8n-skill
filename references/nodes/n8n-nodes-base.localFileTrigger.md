# Local File Trigger  (`n8n-nodes-base.localFileTrigger`)

- typeVersion (max): **1**  | group: trigger  | trigger: yes
- credentials: —

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `triggerOn` | Trigger On | options |  | true |  |
| `path` | File to Watch | string |  |  |  |
| `events` | Watch for | multiOptions | [] | true |  |
| `options` | Options | collection | {} |  |  |
