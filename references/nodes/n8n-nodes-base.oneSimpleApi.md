# One Simple API  (`n8n-nodes-base.oneSimpleApi`)

- typeVersion (max): **1**  | group: transform  | trigger: no
- credentials: oneSimpleApi
- resources: information, socialProfile, utility, website
- operations: exchangeRate, expandURL, imageMetadata, instagramProfile, pdf, qrCode, screenshot, seo, spotifyArtistProfile, validateEmail

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | website | true |  |
| `operation` | Operation | options | pdf |  | res=website |
| `operation` | Operation | options | instagramProfile |  | res=socialProfile |
| `operation` | Operation | options | exchangeRate |  | res=information |
| `operation` | Operation | options | validateEmail |  | res=utility |
| `link` | Webpage URL | string |  | true | res=website,op=pdf |
| `download` | Download PDF? | boolean | false | true | res=website,op=pdf |
| `output` | Put Output In Field | string | data | true | res=website,op=pdf |
| `options` | Options | collection | {} |  | res=website,op=pdf |
| `message` | QR Content | string |  | true | res=utility,op=qrCode |
| `download` | Download Image? | boolean | false | true | res=utility,op=qrCode |
| `output` | Put Output In Field | string | data | true | res=utility,op=qrCode |
| `options` | Options | collection | Small |  | res=utility,op=qrCode |
| `link` | Webpage URL | string |  | true | res=website,op=screenshot |
| `download` | Download Screenshot? | boolean | false | true | res=website,op=screenshot |
| `output` | Put Output In Field | string | data | true | res=website,op=screenshot |
| `options` | Options | collection | {} |  | res=website,op=screenshot |
| `profileName` | Profile Name | string |  | true | res=socialProfile,op=instagramProfile |
| `artistName` | Artist Name | string |  | true | res=socialProfile,op=spotifyArtistProfile |
| `value` | Value | string |  | true | res=information,op=exchangeRate |
| `fromCurrency` | From Currency | string |  | true | res=information,op=exchangeRate |
| `toCurrency` | To Currency | string |  | true | res=information,op=exchangeRate |
| `link` | Link To Image | string |  | true | res=information,op=imageMetadata |
| `link` | Webpage URL | string |  | true | res=website,op=seo |
| `options` | Options | collection | {} |  | res=website,op=seo |
| `emailAddress` | Email Address | string |  | true | res=utility,op=validateEmail |
| `link` | URL | string |  | true | res=utility,op=expandURL |
