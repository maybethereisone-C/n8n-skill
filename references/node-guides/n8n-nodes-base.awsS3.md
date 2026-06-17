# AWS S3 — `n8n-nodes-base.awsS3`
**Type** `n8n-nodes-base.awsS3` · **action**
**What:** Manage S3 buckets, files, and folders — upload, download, copy, delete, search.
**Credentials:** AWS credential (access key + secret, with S3 permissions).

## Resources / Operations
| Resource | Operations |
|---|---|
| Bucket | Create, Delete, Get All, Search within bucket |
| File | Copy, Delete, Download, Get All, Upload |
| Folder | Create, Delete, Get All |

## Key params & gotchas
- **File/Upload** expects binary data from a previous node (e.g. Read Binary File, HTTP Request). Set the **Binary Property** param to the field name holding the binary.
- **File/Download** outputs binary data — pipe to Write Binary File or HTTP Response node.
- **Bucket/Search** uses S3's ListObjectsV2 with a prefix/delimiter filter, not full-text search.
- S3 "folders" are virtual (prefix-based) — Folder ops create/delete zero-byte prefix objects.
- For private buckets, ensure the IAM user has `s3:PutObject`, `s3:GetObject`, `s3:DeleteObject`, `s3:ListBucket`.
- Region must match the bucket's region in the AWS credential or requests will fail with 301/redirect errors.

**Source:** n8n-nodes-base.awss3.md  [doc-verified]
