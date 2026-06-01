# AGENTS.md

This repository is a personal knowledge base for preparing and following the advertising Agent project related to 钛动科技.

## Working Language

- Prefer Chinese for notes, summaries, and user-facing output.
- Keep English technical names as-is, for example OpenAI Agents SDK, LangGraph, Google ADK, Pydantic AI.

## Read First

Before making substantive changes, read these files:

1. `README.md`
2. `docs/10-projects/taidong-ad-agent/brief.md`
3. Any file under `docs/20-research`, `docs/30-decisions`, or `docs/40-playbooks` that matches the task.

## Knowledge Rules

- Preserve public-safe raw inputs before turning them into conclusions.
- Put private or internal-learning raw material under `private/internal-learning/`, mark it as private, and do not add it to `SUMMARY.md`.
- Separate facts, assumptions, judgments, and open questions.
- Add dates to research notes. If the topic may change quickly, verify with current official sources before writing recommendations.
- Prefer primary sources: official docs, product docs, API docs, engineering blogs, GitHub repositories, or standards documents.
- Record source links near the claim they support.
- Do not store secrets, tokens, account credentials, customer data, private campaign data, or sensitive internal documents in this repository.
- When preparing GitBook-facing pages, keep only clean-room summaries, general methodology, public source links, and personal learning plans.

## File Placement

- Project context, goals, roadmap: `docs/10-projects/taidong-ad-agent/`
- Framework and platform research: `docs/20-research/`
- Architecture or product decisions: `docs/30-decisions/`
- Reusable operating methods: `docs/40-playbooks/`
- Templates: `docs/90-templates/`
- GitBook publishing notes: `docs/publishing/`
- Private learning material not intended for GitBook navigation: `private/internal-learning/`

## Research Output Standard

Each research note should include:

- Date
- Question being answered
- Short answer
- Candidate options
- Evaluation criteria
- Recommendation or next experiment
- Source links
- Open questions

## Decision Output Standard

Each decision record should include:

- Status: proposed, accepted, superseded, or rejected
- Context
- Options considered
- Decision
- Consequences
- Follow-up actions

## Codex Task Standard

When a Codex cloud task changes knowledge files, it should end with:

- What changed
- Which files changed
- What remains uncertain
- Suggested next task
