# OpenClaw activity-log credential mapping — 2026-10-29

Owner: Cody. Authorized by Jack after he created the shared-vault item and requested agent refresh/restarts.
Tracking: https://github.com/ZedBiz44/ZedBiz-general-tech-issues-updates/issues/98

## Exact configuration additions

VPS1 agents: amanda, edith, gohzed, grogar, inga, maggie, marsha, terry, victor, vivian, wilma.

Added to each `/opt/openclaw/agents/<agent>/.env`:

```dotenv
GITHUB_AGENT_LOG_API=op://openclaw-agents-shared/github-agent-log-api/credential
```

Added to the gateway service environment in each agent's `docker-compose.yml`, beside the existing GITHUB_API_TOKEN mapping:

```yaml
      GITHUB_AGENT_LOG_API: ${GITHUB_AGENT_LOG_API}
```

Existing GITHUB_API_TOKEN and any GH_TOKEN settings were preserved. Recreated only the named gateway via the agent's own service-account context, `op run --env-file .env -- docker compose -p <agent> up -d --no-deps <agent>`. Existing images and Asana sidecars were retained. Inga was the pilot; remaining VPS1 gateways were refreshed in pairs with health gates.

VPS2 agents: frank, harry, suzy. Added the same dotenv reference to `/root/.openclaw-<agent>/.env`, then restarted each existing `openclaw-<agent>.service`, whose wrapper runs op run against that file.

VPS4 Rocky: added beside the existing GitHub read credential in `/home/openclaw/bin/openclaw-gateway-discord`:

```bash
export GITHUB_AGENT_LOG_API="$(op read 'op://openclaw-agents-shared/github-agent-log-api/credential')"
```

Restarted the existing openclaw user's `openclaw-gateway.service` with its existing 1Password environment. No repository permissions or vault values were modified.

## Protected rollback copies

- VPS1: `/opt/openclaw/agents/<agent>/backups/activity-log-20261029/` contains prior .env and docker-compose.yml; mode 0600 for backup files.
- VPS2: `/root/.openclaw-<agent>/backups/activity-log-20261029/.env`.
- VPS4: `/home/openclaw/.openclaw/backups/activity-log-20261029/openclaw-gateway-discord`.

These are host-local protected backups, not files to publish. No full environment file or secret value is included in this record.

## Skill credential selection

The existing Skill variants received only the OpenClaw activity-log credential section, preserving other content. It selects GITHUB_AGENT_LOG_API for this repository, retains general credentials for other uses, and distinguishes a repository metadata 404 from a new file's expected 404.

Maintained description: https://app.notion.com/p/408a3e33d58180339262c3a7c53be324
Published instruction delta: https://github.com/ZedBiz44/Z-Agent-Activity-Log/commit/3b0c9b3460c9f436f73d9a79927c1b602eb98a34
Exact added-section SHA256: a92425f59c9fe4c2651ecccd8c18ab57e737cc1d4c480a45cace08783d53b365

Existing platform-specific full Skill bodies were not replaced with the different repository version. Each of the fifteen installed files passed its platform's quick_validate.py. Inga discovery confirmed eligible, enabled and model-visible. Wilma's existing Skill is under agent workshop-skills; other observed installations are workspace skills. Backups of prior Skill files were retained alongside deployment backups or in `.activity-log-credential-backup-20261029` under the VPS1 workspace.

## Verification references

Inga: old GITHUB_API_TOKEN returned 404 for repository metadata; new GITHUB_AGENT_LOG_API returned 200/private=true. Real write and exact read-back succeeded from Inga's runtime:
https://github.com/ZedBiz44/Z-Agent-Activity-Log/blob/main/activity/2026/10/29/cody-143105-b84d9a4d-50ea-4f8c-b5ba-269056878781.md

Per-agent runtime access and final health results are recorded in issue 98. The pilot establishes credential-level write/read behavior; no autonomous model-turn or fleet-wide logging-completeness claim is made. This dated implementation record does not replace the maintained Notion procedure.
