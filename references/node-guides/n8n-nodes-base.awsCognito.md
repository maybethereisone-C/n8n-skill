# AWS Cognito — `n8n-nodes-base.awsCognito`
**Type** `n8n-nodes-base.awsCognito` · **action**
**What:** Manage users, groups, and user pools in AWS Cognito User Pools.
**Credentials:** AWS credential (access key + secret, with Cognito permissions).

## Resources / Operations
| Resource | Operations |
|---|---|
| Group | Create, Delete, Get, Get Many, Update |
| User | Add to Group, Create, Delete, Get, Get Many, Remove From Group, Update |
| User Pool | Get |

## Key params & gotchas
- **User Pool ID** is required for all operations — specify which pool to operate on.
- User/Create provisions a user and can optionally send an invite email (controlled by `MessageAction` param).
- User/Add to Group and Remove From Group require both a username and group name.
- User Pool/Get only retrieves metadata — it does not list pools. Use AWS Console to find pool IDs.
- IAM permissions needed: `cognito-idp:*` scoped to your pool ARN.

**Source:** n8n-nodes-base.awscognito.md  [doc-verified]
