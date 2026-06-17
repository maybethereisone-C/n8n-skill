# Discourse — `n8n-nodes-base.discourse`
**Type** `n8n-nodes-base.discourse` · **action**
**What:** Manage Discourse forum categories, groups, posts, users, and user-group memberships.
**Credentials:** discourseApi (API key + username + base URL).

## Resources / Operations
| Resource | Operations |
|---|---|
| Category | Create, Get All, Update |
| Group | Create, Get, Get All, Update |
| Post | Create, Get, Get All, Update |
| User | Create, Get, Get All |
| User Group | Add User to Group, Remove User from Group |

## Key params & gotchas
- Discourse API key must belong to an admin user; non-admin keys have restricted access.
- **Post Create** requires a `topic_id` to reply to an existing thread, or `title` + `category` to create a new topic.
- **User Get All** returns users in the order they joined; paginates via `page` param.
- "Operation not supported" error can appear for features that require specific Discourse plugins.

**Source:** n8n-nodes-base.discourse.md  [doc-verified]
