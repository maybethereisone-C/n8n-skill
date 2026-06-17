# AI-Agents

**107 workflows.** LLM-driven agent and orchestration workflows.

## What's here
Single AI agents, multi-agent orchestrators, prompt chaining, routing, parallelization, evaluator-optimizer loops, OpenAI/LLM chat and image-generation flows, customer-support and research agents.

## When Claude should reach for this folder
Reach for `AI-Agents/` when the user wants an autonomous or semi-autonomous LLM agent, an orchestrator that delegates to sub-workflows, a chat assistant, or any pattern from the agentic-design playbook (chaining, routing, parallelization, HITL).

## Usage
- Search all templates (result paths are prefixed with the topic folder, so filter on `AI-Agents/`): `python3 scripts/search-templates.py search "<query>"`
- Validate before importing: `python3 scripts/validate-workflow.py templates/AI-Agents/<file>.json`
- All credentials, API keys, and personal emails in these files are redacted (`REDACTED`, `REDACTED_JWT`, `you@example.com`). Re-add your own credentials in n8n after import.
