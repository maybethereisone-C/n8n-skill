# Compression — `n8n-nodes-base.compression`

**Type** `n8n-nodes-base.compression` · **typeVersion** 1 · **core**

**What:** Compresses binary files to Zip or Gzip, or decompresses existing archives.

**Credentials:** None.

**Resources / Operations:**

| Operation | Key Params |
|-----------|-----------|
| Compress | Input Binary Field(s), Output Format (Zip/Gzip), File Name, Put Output File in Field |
| Decompress | Put Output File in Field (input field names), Output Prefix |

**Key params & gotchas:**
- **Input Binary Field(s)** (Compress): comma-separated list of binary field names to compress into a single archive.
- **Gzip** compresses a single stream; **Zip** supports multiple files in one archive — use Zip when bundling multiple binary fields.
- Decompress output field naming uses a prefix (e.g., `file_`) prepended to each extracted file name.
- Input must be binary data; ensure an upstream node (HTTP Request, Read File, etc.) has placed the file in a binary property.

**Source:** n8n-nodes-base.compression.md  [doc-verified]
