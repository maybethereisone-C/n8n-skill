# Email Trigger (IMAP)  (`n8n-nodes-base.emailReadImap`)

- typeVersion (max): **2.1**  | group: trigger  | trigger: no
- credentials: —

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `mailbox` | Mailbox Name | string | INBOX |  |  |
| `postProcessAction` | Action | options | read |  |  |
| `downloadAttachments` | Download Attachments | boolean | false |  |  |
| `format` | Format | options | simple |  |  |
| `dataPropertyAttachmentsPrefixName` | Property Prefix Name | string | attachment_ |  |  |
| `options` | Options | collection | ["UNSEEN"] |  |  |
