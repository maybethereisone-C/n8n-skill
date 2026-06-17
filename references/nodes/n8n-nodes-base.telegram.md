# Telegram  (`n8n-nodes-base.telegram`)

- typeVersion (max): **1.3**  | group: output  | trigger: no
- credentials: telegramApi
- resources: bot, callback, chat, file, message
- operations: administrators, answerInlineQuery, answerQuery, deleteMessage, editMessageText, get, info, leave, member, pinChatMessage, sendAnimation, sendAudio, sendChatAction, sendDocument, sendLocation, sendMediaGroup, sendMessage, sendPhoto, sendSticker, sendVideo, setDescription, setTitle, unpinChatMessage

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | message |  |  |
| `operation` | Operation | options | info |  | res=bot |
| `operation` | Operation | options | get |  | res=chat |
| `operation` | Operation | options | answerQuery |  | res=callback |
| `operation` | Operation | options | get |  | res=file |
| `operation` | Operation | options | sendMessage |  | res=message |
| `chatId` | Chat ID | string |  | true | res=chat,res=message,op=administrators,op=deleteMessage,op=get,op=leave |
| `messageId` | Message ID | string |  | true | res=message,op=deleteMessage |
| `messageId` | Message ID | string |  | true | res=message,op=pinChatMessage,op=unpinChatMessage |
| `additionalFields` | Additional Fields | collection | {} |  | res=message,op=pinChatMessage |
| `userId` | User ID | string |  | true | res=chat,op=member |
| `description` | Description | string |  | true | res=chat,op=setDescription |
| `title` | Title | string |  | true | res=chat,op=setTitle |
| `queryId` | Query ID | string |  | true | res=callback,op=answerQuery |
| `additionalFields` | Additional Fields | collection | {} |  | res=callback,op=answerQuery |
| `queryId` | Query ID | string |  | true | res=callback,op=answerInlineQuery |
| `results` | Results | string |  | true | res=callback,op=answerInlineQuery |
| `additionalFields` | Additional Fields | collection | {} |  | res=callback,op=answerInlineQuery |
| `fileId` | File ID | string |  | true | res=file,op=get |
| `download` | Download | boolean | true |  | res=file,op=get |
| `additionalFields` | Additional Fields | collection | {} |  | res=file,op=get |
| `messageType` | Message Type | options | message |  | res=message,op=editMessageText |
| `chatId` | Chat ID | string |  | true | res=message,op=editMessageText |
| `binaryData` | Binary File | boolean | false | true | res=message,op=sendAnimation,op=sendAudio,op=sendDocument,op=sendPhoto,op=sendVideo |
| `binaryPropertyName` | Input Binary Field | string | data | true | res=message,op=sendAnimation,op=sendAudio,op=sendDocument,op=sendPhoto,op=sendVideo |
| `messageId` | Message ID | string |  | true | res=message,op=editMessageText |
| `inlineMessageId` | Inline Message ID | string |  | true | res=message,op=editMessageText |
| `replyMarkup` | Reply Markup | options | none |  | res=message,op=editMessageText |
| `file` | Animation | string |  |  | res=message,op=sendAnimation |
| `file` | Audio | string |  |  | res=message,op=sendAudio |
| `action` | Action | options | typing |  | res=message,op=sendChatAction |
| `file` | Document | string |  |  | res=message,op=sendDocument |
| `latitude` | Latitude | number | 0.0 |  | res=message,op=sendLocation |
| `longitude` | Longitude | number | 0.0 |  | res=message,op=sendLocation |
| `media` | Media | fixedCollection | photo |  | res=message,op=sendMediaGroup |
| `text` | Text | string |  | true | res=message,op=editMessageText,op=sendMessage |
| `file` | Photo | string |  |  | res=message,op=sendPhoto |
| `file` | Sticker | string |  |  | res=message,op=sendSticker |
| `file` | Video | string |  |  | res=message,op=sendVideo |
| `replyMarkup` | Reply Markup | options | none |  | res=message,op=sendAnimation,op=sendDocument,op=sendMessage,op=sendPhoto,op=sendSticker |
| `forceReply` | Force Reply | collection | {} |  | res=message |
| `inlineKeyboard` | Inline Keyboard | fixedCollection | {} |  | res=message |
| `replyKeyboard` | Reply Keyboard | fixedCollection | {} |  |  |
| `replyKeyboardOptions` | Reply Keyboard Options | collection | {} |  |  |
| `replyKeyboardRemove` | Reply Keyboard Remove | collection | {} |  |  |
| `additionalFields` | Additional Fields | collection | {} |  | res=message,op=editMessageText,op=sendAnimation,op=sendAudio,op=sendDocument,op=sendLocation |
| `chatId` | Chat ID | string |  | true |  |
| `telegramTriggerNotice` | Due to Telegram API limitations, you can use just one Telegram trigger for each bot at a time | notice |  |  |  |
| `updates` | Trigger On | multiOptions | [] | true |  |
| `attachmentNotice` | Every uploaded attachment, even if sent in a group, will trigger a separate event. You can identify that an attachment belongs to a certain group by <code>media_group_id</code> . | notice |  |  |  |
| `additionalFields` | Additional Fields | collection | large |  |  |
