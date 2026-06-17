# Google Slides  (`n8n-nodes-base.googleSlides`)

- typeVersion (max): **2**  | group: input,output  | trigger: no
- credentials: googleApi, googleSlidesOAuth2Api
- resources: page, presentation
- operations: create, get, getSlides, getThumbnail, replaceText

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `authentication` | Authentication | options | serviceAccount |  |  |
| `resource` | Resource | options | presentation |  |  |
| `operation` | Operation | options | create |  | res=presentation |
| `operation` | Operation | options | get |  | res=page |
| `title` | Title | string |  | true | res=presentation,op=create |
| `presentationId` | Presentation ID | string |  | true | res=presentation,res=page,op=get,op=getThumbnail,op=getSlides,op=replaceText |
| `returnAll` | Return All | boolean | false |  | res=presentation,op=getSlides |
| `limit` | Limit | number | 100 |  | res=presentation,op=getSlides |
| `pageObjectId` | Page Object ID | string |  | true | res=page,op=get,op=getThumbnail |
| `textUi` | Texts To Replace | fixedCollection | {} |  | res=presentation,op=replaceText |
| `options` | Options | collection | {} |  | res=presentation,op=replaceText |
| `download` | Download | boolean | false |  | res=page,op=getThumbnail |
| `binaryProperty` | Put Output File in Field | string | data | true | res=page,op=getThumbnail |
