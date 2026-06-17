# AWS IAM — `n8n-nodes-base.awsIam`
**Type** `n8n-nodes-base.awsIam` · **action**
**What:** Manage AWS IAM users and groups, including group membership.
**Credentials:** AWS credential (access key + secret, with IAM permissions).

## Resources / Operations
| Resource | Operations |
|---|---|
| User | Add to Group, Create, Delete, Get, Get Many, Remove From Group, Update |
| Group | Create, Delete, Get, Get Many, Update |

## Key params & gotchas
- **Doc note:** Group/Delete has a typo in the official docs ("Create a new group") — it actually deletes.
- Does not manage IAM roles, policies, or MFA devices — use HTTP Request node for those.
- User/Update can change username, path, or both.
- Add/Remove from Group requires both username and group name.
- IAM permissions needed: `iam:CreateUser`, `iam:DeleteUser`, `iam:GetUser`, `iam:ListUsers`, `iam:UpdateUser`, `iam:AddUserToGroup`, `iam:RemoveUserFromGroup`, plus group equivalents.

**Source:** n8n-nodes-base.awsiam.md  [doc-verified]
