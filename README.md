# ZedBiz-general-tech-issues-updates

This repository is the operational home and technical source of truth for **server infrastructure, 1Password fleet, Manus/Cody tooling, and any general tech not specific to one agent**.

## 📋 The Technical Memory System
All technical work is tracked via GitHub Issues in this repository. Notion is for human-readable summaries only; GitHub is the working source of truth.

Canonical GitHub playbook: [docs/github-issue-filing-sop.md](docs/github-issue-filing-sop.md)

That SOP is the current operating rule for repo routing, search-before-create, required labels, issue body templates, parent issue/workstream handling, comment updates, PR/main-branch status, and closeout comments.

### Routing Rule
If you are unsure whether an issue belongs in the VPS1/VPS2 repo or the VPS3 repo, file it here and add the label `needs-routing`.

### The 6-Step Issue Filing Rule
Every agent (Manus, Cody, Ruby, Victor, and future agents) MUST follow this process for every task:

1. **Search first:** `gh issue list --search "[topic]" --state all --limit 10`
2. **If a matching issue exists:** Add a comment there. Do not create a duplicate.
3. **If no match exists:** Create a new issue in the correct repo.
4. **Use exact title format:** `YYYY-MM-DD | [Tool/System] | [Short description]`
5. **Apply required labels:** `system:`, `type:`, `status:` and `agent:` if applicable.
6. **Closeout rule:** Never close an issue without a final comment stating the resolution, verification, documentation updates, and PR/main-branch status.

### Required Labels
Every issue MUST have the minimum labels that make it searchable:
- **Agent:** Only use if a specific agent is involved (`agent:manus`, `agent:cody`, etc.)
- **System:** `system:1password`, `system:whm`, `system:github`, `system:search`, etc.
- **Type:** `type:bug`, `type:config`, `type:integration`, `type:sop`, etc.
- **Status:** `status:open`, `status:blocked`, `status:resolved`

### Issue Body Template
When creating an issue, use the full template in [docs/github-issue-filing-sop.md](docs/github-issue-filing-sop.md), including:
- **What:** One sentence description
- **System Affected:** VPS, platform, or tool
- **Search Performed:** Confirm you searched first
- **Related Existing Issues:** Link dependencies or `None found`
- **What Was Tried:** Bullet list
- **What Failed:** Record every failed attempt
- **What Worked:** The actual fix
- **What Changed:** Files edited, configs updated, PRs or branches created
- **Next Action:** The next practical step

## 🔒 Secret Rules
- NEVER commit API keys, OAuth tokens, passwords, or gateway tokens.
- Live secrets live only on the VPS or in the 1Password vault.

---
*For the human-readable overview, refer to the [Technical Memory System Notion Page](https://app.notion.com/p/397a3e33d581812fa9dcfcfa80e88fab). GitHub SOPs remain the agent-facing technical source of truth.*
