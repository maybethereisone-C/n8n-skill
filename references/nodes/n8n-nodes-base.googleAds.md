# Google Ads  (`n8n-nodes-base.googleAds`)

- typeVersion (max): **1**  | group: transform  | trigger: no
- credentials: googleAdsOAuth2Api
- resources: campaign
- operations: get, getAll

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | campaign |  |  |
| `campaigsNotice` | Divide field names expressed with <i>micros</i> by 1,000,000 to get the actual value | notice |  |  | res=campaign |
