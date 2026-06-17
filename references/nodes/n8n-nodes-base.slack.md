# Slack  (`n8n-nodes-base.slack`)

- typeVersion (max): **2.5**  | group: output  | trigger: no
- credentials: slackApi, slackOAuth2Api
- resources: channel, file, message, reaction, star, user, userGroup, userProfile
- operations: add, archive, close, create, delete, disable, enable, get, getAll, getPermalink, getPresence, getProfile, getUsers, history, info, invite, join, kick, leave, member, open, post, postEphemeral, remove, rename, replies, search, setPurpose, setTopic, unarchive, update, updateProfile, updateUsers, upload

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `authentication` | Authentication | hidden | accessToken |  |  |
| `notice` | Set up a webhook in your Slack app to enable this node. <a href="https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.slacktrigger/#configure-a-webhook-in-slack" target="_blank">More info</a>. We also recommend setting up a <a href="https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.slacktrigger/#verify-the-webhook" target="_blank">signing secret</a> to ensure the authenticity of requests. | notice |  |  |  |
| `trigger` | Trigger On | multiOptions | [] |  |  |
| `watchWorkspace` | Watch Whole Workspace | boolean | false |  |  |
| `channelId` | Channel to Watch | resourceLocator |  | true |  |
| `downloadFiles` | Download Files | boolean | false |  |  |
| `options` | Options | collection | {} |  |  |
| `resource` | Resource | options | message |  |  |
