# ZedBiz-general-tech-issues-updates

This repository is the operational home and technical source of truth for **server infrastructure, 1Password fleet, Manus/Cody tooling, and any general tech not specific to one agent**.

## 📋 The Technical Memory System
All technical work is tracked via GitHub Issues in this repository. Notion is for human-readable summaries only; GitHub is the working source of truth.

### Routing Rule
If you are unsure whether an issue belongs in the VPS1/VPS2 repo or the VPS3 repo, file it here and add the label `needs-routing`.

### The 6-Step Issue Filing Rule
Every agent (Manus, Cody, Ruby) MUST follow this process for every task:

1. **Search first:** `gh issue list --search "[topic]" --state all --limit 10`
2. **If a matching issue exists:** Add a comment there. Do not create a duplicate.
3. **If no match exists:** Create a new issue in this repo.
4. **Use exact title format:** `YYYY-MM-DD | [Tool/System] | [Short description]`
5. **Apply required labels:** `system:`, `type:`, `status:` (and `agent:` if applicable)
6. **Closeout rule:** Never close an issue without a final comment stating the Resolution and what was Verified.

### Required Labels
Every issue MUST have at least one label from the system, type, and status categories:
- **Agent:** Only use if a specific agent is involved (`agent:manus`, `agent:cody`, etc.)
- **System:** `system:1password`, `system:whm`, `system:github`, `system:search`, etc.
- **Type:** `type:bug`, `type:config`, `type:integration`, `type:sop`, etc.
- **Status:** `status:open`, `status:blocked`, `status:resolved`

### Issue Body Template
When creating an issue, use this structure:
- **What:** One sentence description
- **System Affected:** VPS, platform, or tool
- **Search Performed:** Confirm you searched first
- **What Was Tried:** Bullet list
- **What Failed:** Record every failed attempt (crucial for future agents)
- **What Worked:** The actual fix
- **What Changed:** Files edited, configs updated

## 🔒 Secret Rules
- NEVER commit API keys, OAuth tokens, passwords, or gateway tokens.
- Live secrets live only on the VPS or in the 1Password vault.

---
*For the complete GitHub Issue Filing Rules, refer to the [Technical Memory System Notion Page](https://app.notion.com/p/397a3e33d581812fa9dcfcfa80e88fab).*
