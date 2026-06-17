# Microsoft Teams  (`n8n-nodes-base.microsoftTeams`)

- typeVersion (max): **2**  | group: input  | trigger: no
- credentials: microsoftTeamsOAuth2Api
- resources: channel, channelMessage, chatMessage, task
- operations: create, delete, deleteChannel, deleteTask, get, getAll, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `event` | Trigger On | options | newChannelMessage |  |  |
| `watchAllTeams` | Watch All Teams | boolean | false |  |  |
| `teamId` | Team | resourceLocator |  | true |  |
| `watchAllChannels` | Watch All Channels | boolean | false |  |  |
| `channelId` | Channel | resourceLocator |  | true |  |
| `watchAllChats` | Watch All Chats | boolean | false |  |  |
| `chatId` | Chat | resourceLocator |  | true |  |
| `resource` | Resource | options | channel |  |  |
