# Airtable — `n8n-nodes-base.airtable`
**Type** `n8n-nodes-base.airtable` · **action**
**What:** Read, write, update, and delete records in Airtable bases.
**Credentials:** Airtable API key or OAuth2 credential.

## Resources / Operations
- Append data to a table
- Delete data from a table
- List data from a table
- Read data from a table
- Update data in a table

## Key params & gotchas
- **Record ID** is required for Read, Update, Delete — obtain it from the List operation or by adding a Record ID formula field in Airtable.
- **Filter By Formula** on List uses Airtable formula syntax (e.g. `{Status}='Active'`). Wrapping field names in `{}` is mandatory for multi-word fields.
- `NOT({Org}='n8n')` syntax works for negation.
- Airtable rate-limits at 5 requests/second per base — add a Wait node between bulk operations.
- The node uses the v0 REST API; attachment fields must be uploaded as URLs, not binary.
- n8n provides a separate Airtable Trigger node for polling-based triggers.

**Source:** n8n-nodes-base.airtable/index.md  [doc-verified]
