# FileMaker — `n8n-nodes-base.filemaker`
**Type** `n8n-nodes-base.filemaker` · **action**
**What:** Interact with FileMaker databases — find, create, edit, duplicate, delete records, and run scripts.
**Credentials:** fileMakerApi (host, database, username, password — uses FileMaker Data API).

## Resources / Operations
| Operations |
|---|
| Find Records |
| Get Records |
| Get Records by Id |
| Perform Script |
| Create Record |
| Edit Record |
| Duplicate Record |
| Delete Record |

## Key params & gotchas
- All operations target a **Layout** name — layouts control which fields are exposed; the layout must exist in the FileMaker file.
- **Find Records** uses FileMaker find requests (field-value pairs); multiple find requests are OR'd together.
- **Perform Script** executes a FileMaker script by name; optionally pass a script parameter as a string.
- **Get Records by Id** requires the FileMaker internal record ID (`recordId`), not any field value.
- Can be used as an AI tool node.
- The FileMaker Data API must be enabled on the FileMaker Server.

**Source:** n8n-nodes-base.filemaker.md  [doc-verified]
