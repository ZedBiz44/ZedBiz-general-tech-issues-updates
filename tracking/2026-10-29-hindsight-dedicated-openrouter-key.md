# Hindsight dedicated OpenRouter credential

Date: 2026-10-29 | Agent: Cody | Status: Verified

## Authorization and scope
Jack requested all current Hindsight agents use the new shared-vault OpenRouter key for separate usage tracking. Issue: https://github.com/ZedBiz44/ZedBiz-general-tech-issues-updates/issues/99

Credential reference: `op://openclaw-agents-shared/openrouter-hindsight-api-key/credential`. No secret values belong in source or records.

## Live architecture and changes
- Central VPS1 Hindsight 1.1.0 serves Marsha, Maggie, Inga, GohZed, Grogar, Frank, Suzy and Ruby. Its OpenAI-compatible base URL is https://openrouter.ai/api/v1 and existing retain/reflect/consolidation model is openai/gpt-5.6-luna.
- Rocky uses a separate Hindsight 1.1.0 server on VPS4, with the same OpenRouter base URL and existing qwen/qwen3.6-35b-a3b model.
- Rocky pilot first: `/usr/local/sbin/rocky-hindsight-runtime-env` now reads the dedicated vault reference instead of `op://openclaw-agents-shared/openrouter-api-key/credential`. Existing generation of `/run/rocky-hindsight/runtime.env` preserved, including restart/reload behavior.
- Central: replaced only HINDSIGHT_API_LLM_API_KEY in `/opt/openclaw/services/hindsight/.env` with the value securely resolved from the dedicated vault item. Retained the existing protected resolved-secret-file pattern; central Compose does not resolve op:// references itself. A future vault rotation needs this protected file refreshed before API recreation.
- No general agent OpenRouter credentials, models, banks, memory policies, databases or agent gateways changed.

## Verification
- Rocky runtime secret generation passed; recreated only Compose service `api`. Runtime key equals the freshly resolved dedicated key. Dry-run extraction returned HTTP200; health HTTP200.
- Central recreated only service `hindsight` under Compose project hindsight-central. Runtime key equals the freshly resolved dedicated key; API healthy. Database container retained October24 start time.
- Central dry-run extraction of the actual approved credential-separation decision produced one fact containing OpenRouter: 3,031 input tokens, 192 output tokens, 3,223 total, 2,826 cached, 48 thought tokens. No test memory persisted.
- Earlier central synthetic parcel input returned HTTP200 but zero extracted facts; input echoed in chunks was not proof of extraction. Replaced acceptance with the substantive one-fact result above.
- Read-only configured-route recalls for all nine consumers returned HTTP200 and two results each: five VPS1 agents through their own containers, Frank/Suzy from VPS2 with configured auth, Ruby through her Hermes container environment, Rocky through his local configured bank. These prove route/API reads, not a fresh model turn from every agent.
- OpenRouter /api/v1/key accepted the dedicated credential; reported usage increased from zero to 0.0015506 USD during verification/background work. This is key-level aggregate usage, not a per-agent cost breakdown.

## Backups and rollback
- Rocky: `/opt/rocky-hindsight/backups/dedicated-key-20261030T0447Z/rocky-hindsight-runtime-env`. Restore the script, regenerate runtime.env, then recreate API service only.
- Central: `/opt/openclaw/services/hindsight/backups/dedicated-key-20261030T0450Z/.env`. Restore the protected env file, recreate hindsight API only. Do not restart or restore databases for credential rollback.
- Rocky command: `docker compose --env-file /run/rocky-hindsight/runtime.env -f /opt/rocky-hindsight/docker-compose.yml up -d --no-deps --wait api`.
- Central command: `docker compose -p hindsight-central -f /opt/openclaw/services/hindsight/build/docker-compose.yml up -d --no-deps hindsight`.

## Attempts and separate follow-up
- Default bridge helper failed because docker0 was absent; read-only --network none helper succeeded. No network repair made.
- First Rocky Compose service name hindsight-api was incorrect; corrected to live label api. No container change occurred on the rejected attempt.
- Local Python alias unavailable; bundled Python used. First VPS3 key format and first Hermes virtualenv path were incorrect; existing normalized key and /opt/hermes/.venv/bin/python succeeded.
- Initial central health/remote recalls failed during initialization; all passed after startup.
- An overly broad diagnostic filter exposed a database credential in private tool output. Output filter corrected, credential omitted from records, Jack informed; database credential rotation remains a separate follow-up, not completed here.

## Records
Configuration delta is recorded on main here; no application source change or PR required. Daily journal: https://www.notion.so/408a3e33d58181c99224d1482c5d82a0. Registry and SOP unchanged; old Notion overview model/version statements were not used as live proof.
