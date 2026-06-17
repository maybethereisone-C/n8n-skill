# APITemplate.io  (`n8n-nodes-base.apiTemplateIo`)

- typeVersion (max): **1**  | group: transform  | trigger: no
- credentials: apiTemplateIoApi
- resources: account, image, pdf
- operations: create, get

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | image |  |  |
| `operation` | Operation | options | create | true | res=image |
| `operation` | Operation | options | create | true | res=pdf |
| `operation` | Operation | options | get | true | res=account |
| `imageTemplateId` | Template Name or ID | options |  | true | res=image,op=create |
| `pdfTemplateId` | Template Name or ID | options |  | true | res=pdf,op=create |
| `jsonParameters` | JSON Parameters | boolean | false |  | res=pdf,res=image,op=create |
| `download` | Download | boolean | false |  | res=pdf,res=image,op=create |
| `binaryProperty` | Put Output File in Field | string | data | true | res=pdf,res=image,op=create |
| `overridesJson` | Overrides (JSON) | json |  |  | res=image,op=create |
| `propertiesJson` | Properties (JSON) | json |  |  | res=pdf,op=create |
| `overridesUi` | Overrides | fixedCollection | {} |  | res=image,op=create |
| `propertiesUi` | Properties | fixedCollection | {} |  | res=pdf,op=create |
| `options` | Options | collection | {} |  | res=pdf,res=image,op=create |
