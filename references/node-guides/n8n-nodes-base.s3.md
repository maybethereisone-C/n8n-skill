# S3 (non-AWS) — `n8n-nodes-base.s3`
**Type** `n8n-nodes-base.s3` · **action**
**What:** Manage objects and buckets on S3-compatible storage (MinIO, Wasabi, DigitalOcean Spaces, etc.). For AWS S3 use `n8n-nodes-base.awsS3`.
**Credentials:** `s3` (endpoint, access key, secret key, region, SSL toggle)

## Resources / Operations
| Resource | Operation |
|----------|-----------|
| Bucket | Create, Delete, Get All, Search |
| File | Copy, Delete, Download, Get All, Upload |
| Folder | Create, Delete, Get All |

## Key params & gotchas
- Supports use as an AI tool node.
- Credential requires the **custom endpoint URL** of the S3-compatible service (e.g., `https://s3.wasabisys.com`); leave blank for AWS.
- **File Upload**: binary data must come from a previous node (Read/Write Files from Disk, HTTP Request, etc.) — the node does not accept raw text directly.
- **Wasabi ACL gotcha**: when uploading to Wasabi, set file permissions via the **ACL dropdown** in options, NOT the toggle switches — toggles are ignored by Wasabi.
- **Bucket Search** filters objects within a bucket by prefix/key pattern.
- Folders are virtual (prefix-based); creating a folder creates a zero-byte key ending in `/`.
- SSL/TLS is configurable in credentials; required for most hosted S3-compatible services.

**Source:** n8n-nodes-base.s3.md  [doc-verified]
