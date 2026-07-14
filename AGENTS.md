# General Tech Agent Operating Rules

Date: 2026-07-14 | Agent: Cody | Status: Active

## Purpose

This repo is the fallback and shared lane for ZedBiz technical issues that do not clearly belong to the OpenClaw VPS1/VPS2 repo or the Hermes VPS3 repo.

Use this repo for:

- Cross-system technical questions.
- Routing decisions that are not clear yet.
- General infrastructure, documentation, and source-of-truth cleanup.
- Issues that need a parking spot before the correct repo is confirmed.

## Source Of Truth

- GitHub is the technical source of truth for code, configs, scripts, Docker files, prompts, SOPs, issue history, and PR status.
- Notion is the operational layer for summaries, planning, dashboards, and decisions.
- Do not put long technical instructions only in Notion when they should live in GitHub.

## GitHub Issue Filing Rules

Before creating, updating, or closing any GitHub issue, follow `docs/github-issue-filing-sop.md`.

Minimum behavior:

- Search existing issues before creating a new one.
- If a matching issue exists, comment there instead of making a duplicate.
- Use this repo when routing is unclear and add `needs-routing` where available.
- Add required `agent:`, `system:`, `type:`, and `status:` labels where available.
- Keep ongoing work in one parent issue or workstream instead of making duplicate session issues.
- Comment material attempts, failures, fixes, verification, and PR/main-branch status.
- Do not close until the final comment says what was verified and whether SOPs, tracking files, registry, or Notion summaries were updated.

## Repo Routing

- VPS1/VPS2 OpenClaw agent work: `ZedBiz44/ZedBiz-openclaw-ai-agents-vps1-vps2`
- Ruby/Hermes/VPS3 work: `ZedBiz44/ZedBiz-hermes-ai-agents-vps3`
- General or unclear technical work: `ZedBiz44/ZedBiz-general-tech-issues-updates`

If unsure, file here first and label the issue `needs-routing` where available.

## Work Style

- Prefer a simple working fix, verified against the real surface.
- Record failed attempts because they save future agents from wasting time.
- Link the relevant Notion page, GitHub file, issue, PR, or VPS/SOP when one exists.
- Use Mountain Time for dated notes.
