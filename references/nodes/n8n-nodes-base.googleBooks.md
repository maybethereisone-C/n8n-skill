# Google Books  (`n8n-nodes-base.googleBooks`)

- typeVersion (max): **2**  | group: input,output  | trigger: no
- credentials: googleApi, googleBooksOAuth2Api
- resources: bookshelf, bookshelfVolume, volume
- operations: add, clear, get, getAll, move, remove

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `authentication` | Authentication | options | serviceAccount |  |  |
| `resource` | Resource | options | bookshelf |  |  |
| `operation` | Operation | options | get |  | res=bookshelf |
| `operation` | Operation | options | getAll |  | res=bookshelfVolume |
| `operation` | Operation | options | get |  | res=volume |
| `myLibrary` | My Library | boolean | false | true | res=bookshelf,res=bookshelfVolume,op=get,op=getAll |
| `searchQuery` | Search Query | string |  | true | res=volume,op=getAll |
| `userId` | User ID | string |  | true | res=bookshelf,res=bookshelfVolume,op=get,op=getAll |
| `shelfId` | Bookshelf ID | string |  | true | res=bookshelf,res=bookshelfVolume,op=get,op=add,op=clear,op=move |
| `shelfId` | Bookshelf ID | string |  | true | res=bookshelfVolume,op=getAll |
| `volumeId` | Volume ID | string |  | true | res=bookshelfVolume,res=volume,op=add,op=move,op=remove,op=get |
| `volumePosition` | Volume Position | string |  | true | res=bookshelfVolume,op=move |
| `returnAll` | Return All | boolean | false |  | op=getAll |
| `limit` | Limit | number | 40 |  | op=getAll |
