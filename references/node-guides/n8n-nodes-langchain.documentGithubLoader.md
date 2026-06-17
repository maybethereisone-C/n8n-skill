# GitHub Document Loader — `n8n-nodes-langchain.documentGithubLoader`
**Type** `n8n-nodes-langchain.documentGithubLoader` · **ai · sub-node**
**What:** Loads files from a GitHub repository branch for use with vector stores or summarization chains.
**Credentials:** `githubApi` (token-based only — OAuth not supported).

> **Deprecated** — will be removed in a future n8n version.

**Key params & gotchas:**
- **Repository Link**: Full GitHub repo URL.
- **Branch**: Branch name to load from.
- **Text Splitting**: `Simple` (chunk=1000, overlap=200) or `Custom` (connect splitter sub-node).
- **Recursive** (option): Include sub-directories and files (default off).
- **Ignore Paths** (option): Comma-separated directories to skip.
- OAuth credentials are not supported — must use a personal access token.

**Source:** n8n-nodes-langchain.documentgithubloader.md  [doc-verified]
