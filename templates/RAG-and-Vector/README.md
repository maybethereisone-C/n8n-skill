# RAG-and-Vector

**35 workflows.** Retrieval-augmented generation and vector-store pipelines.

## What's here
Document ingestion + embedding, vector store loaders and retrievers, RAG chatbots, RAG-workflow-vs-RAG-agent comparisons, and data-analysis-over-knowledge-base flows.

## When Claude should reach for this folder
Reach for `RAG-and-Vector/` when the user needs to answer questions over their own documents, build a knowledge base, embed/chunk content, or wire a retriever into an agent.

## Usage
- Search all templates (result paths are prefixed with the topic folder, so filter on `RAG-and-Vector/`): `python3 scripts/search-templates.py search "<query>"`
- Validate before importing: `python3 scripts/validate-workflow.py templates/RAG-and-Vector/<file>.json`
- All credentials, API keys, and personal emails in these files are redacted (`REDACTED`, `REDACTED_JWT`, `you@example.com`). Re-add your own credentials in n8n after import.
