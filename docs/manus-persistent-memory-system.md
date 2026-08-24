# Manus Persistent Memory System

**Date:** 2026-08-23 MDT  
**Owner:** Jack Zenert  
**Prepared by:** Manus  
**Status:** Proposed, not yet deployed

## Purpose

This document defines a practical memory system for Manus that preserves useful organizational knowledge across separate tasks while keeping **GitHub as the technical authority**, **Notion as the operating and decision layer**, and an external retrieval service as the recall engine. The design deliberately treats a chat transcript as evidence, not as permanent truth.

> **Core principle:** Manus should not attempt to remember everything. It should receive a short, scoped, current context pack at the beginning of work, retrieve deeper evidence only when needed, and promote durable facts into reviewed source-of-truth records.

This is adapted from the existing OpenClaw model of layered memory, isolation, tested recall, and a separately reviewed knowledge layer. The existing OpenClaw SOP remains the reference point for bank isolation, verification, and rollback discipline: [OpenClaw Memory and Hindsight Management SOP](https://app.notion.com/p/0aea3e33d58182d4b93681fe1bcd7a41).

## The Actual Constraint

A new Manus task should be designed as if it starts without trustworthy long-term recollection of prior chats. Individual task context is useful working memory, but it is not an adequate system of record for company decisions, credentials, client history, operating procedures, or technical changes.

The fix is **not** dumping every chat into a vector database. That creates recall noise, stale facts, privacy risk, and confident nonsense. The fix is a layered system in which each kind of memory has an owner, source, authority level, and retention rule.

## Recommended Architecture

| Layer | Role | System of Record | What Manus Receives | Write Rule |
|---|---|---|---|---|
| Session memory | Current task reasoning and user instructions | Current task | Full current conversation | Temporary only |
| Operating memory | Stable user preferences, operating rules, active priorities, route rules | Small reviewed Markdown files and project instructions | A concise boot context on every task | Human or designated agent approval for material changes |
| Episodic memory | What happened in past tasks, outcomes, attempts, failures, and lessons | Daily journals, GitHub issues, task logs, retrieval index | Top relevant summaries only | Append automatically after filtering and redaction |
| Canonical knowledge | SOPs, code, architecture, decisions, client standards, technical state | GitHub for technical content; Notion for operational decisions and dashboards | Links plus excerpts selected by task scope | Reviewed promotion only |
| Semantic recall | Discovery of relevant past evidence across many records | Hindsight, or equivalent retrieval service | Ranked evidence with source links, authority and date | Index approved and low-risk episodic records |

## The Practical Model

### Start with a Manus Operating Memory Project

Create one dedicated Manus project, for example **ZedBiz AI Operating System**, and use it for all work that needs company continuity. The project should hold a compact, stable boot instruction and a small set of shared files. It must not contain a giant biography or a historical transcript.

The project boot instruction should require the following sequence before material work begins:

- Identify the task's business and technical scope.
- Load the matching current-state file and one relevant SOP or decision record.
- Use the memory index or retrieval gateway to obtain only scoped past context.
- Prefer sources in this order: current verified system state, GitHub technical records, approved Notion decision pages, then episodic retrieval.
- Treat conflicts, unverified retrieval, and stale records as questions to resolve, not instructions to follow.
- Record important work in the appropriate GitHub issue and the daily journal.

The stable boot files should be deliberately small:

| File | Purpose | Target Size | Owner |
|---|---|---:|---|
| `MANUS_OPERATING_MEMORY.md` | Identity, tone, core rules, timezone, source hierarchy, privacy rules, task protocols | Under 1,500 words | Jack plus Manus |
| `CURRENT_STATE.md` | Current technical work index, active systems, known blockers, next decisions | Under 1,500 words | Technical agents |
| `MEMORY_INDEX.md` | Links to domains, projects, clients, SOPs, decision logs, and knowledge-bank scopes | Under 1,000 words | Manus |
| `ACTIVE_PRIORITIES.md` | Current business objectives, owners, deadlines, and non-goals | Under 750 words | Jack |
| `MEMORY_CHANGELOG.md` | Short log of material additions, corrections, deprecations, and review dates | Append-only | Manus |

`CURRENT_STATE.md` is an index of technical changes and ongoing technical work only. Marketing, business strategy, and operational material belong in their own scoped records rather than polluting the technical state file.

### Keep Canonical Knowledge Separate from Recall

GitHub should continue to hold technical source-of-truth material: code, configurations, scripts, prompts, Docker files, approved SOPs, tested command sequences, architectural decisions, and issue history. Notion should hold planning, operational summaries, approvals, dashboards, and daily journals. This matches the existing repository and operating rules.

A retrieval service such as the existing Hindsight setup should be a **discovery layer**, not the authority. It can find related previous work and produce a context pack, but it must point back to the GitHub file, Notion page, issue, or live-system evidence that governs the answer.

## Memory Domains and Isolation

Use named domains. This avoids one agent recalling a client secret or an irrelevant marketing preference while fixing a VPS.

| Scope | Examples | Read Policy | Write Policy |
|---|---|---|---|
| `manus:global` | Jack's timezone, communication style, company structure, universal safety rules | All authorized Manus work | Reviewed changes only |
| `manus:technical` | Architecture, service state, SOPs, incidents, confirmed fixes | Technical tasks only | GitHub-backed records only |
| `manus:marketingjack` | Brand voice, offers, campaigns, target personas, content rules | Marketing tasks only | Approved campaign outcomes and standards |
| `manus:farmerjack` | Personal social media voice and content preferences | Personal-content tasks only | Jack-approved preferences |
| `manus:client:<client-id>` | Client facts, credentials references, deliverables, account context | Explicit client scope only | Strictly isolated, reviewed, expiry-aware |
| `manus:project:<project-id>` | Decision history, task outcomes, active assumptions, current plan | Named project only | Task summary plus promotion review |
| `manus:episodic` | Low-authority work summaries and attempted fixes | Retrieval only | Automatic filtered capture allowed |

Never place passwords, access tokens, complete `.env` files, private keys, session cookies, or raw OAuth files in any memory bank, index, GitHub document, journal, or retrieval payload. Store only the secret name, approved vault location, required permission, and verification date.

## Memory Record Contract

Every retained memory, whether held in Markdown, Notion, or a retrieval index, should include enough metadata to judge whether it is relevant and trustworthy.

| Field | Requirement | Example |
|---|---|---|
| `memory_id` | Stable unique ID | `dec-2026-08-23-manus-memory-architecture` |
| `scope` | One or more approved domains | `manus:technical`, `manus:project:ai-memory` |
| `type` | Operating, decision, SOP, incident, client, episodic, preference, or reference | `decision` |
| `authority` | Canonical, reviewed, provisional, or retrieved-only | `reviewed` |
| `source_url` | Link to GitHub, Notion, issue, task, or live evidence | GitHub issue URL |
| `summary` | Short factual statement suitable for retrieval | `Retrieval finds evidence but does not override canonical records.` |
| `confidence` | Confirmed, reported, or hypothesis | `confirmed` |
| `created_at` | Mountain Time timestamp | `2026-08-23T21:42:00-06:00` |
| `review_after` | Optional review or expiry date | `2026-11-23` |
| `sensitivity` | Public, internal, confidential, or restricted | `internal` |
| `supersedes` | Optional previous record ID | `dec-2026-07-08-memory-rules` |

## Retrieval and Context Assembly

### Context Pack Rules

At the beginning of a task, assemble a short context pack rather than injecting an unbounded history. The pack should normally contain:

- The task goal and the explicitly selected scope.
- Relevant global operating rules.
- The active project or client state.
- The top canonical records, with links and dates.
- A small number of episodic lessons or unresolved risks.
- Conflicts, staleness warnings, and questions that must be verified.

The first version should enforce a hard size budget. Start at approximately 1,500 to 2,500 words. If deeper context is needed, retrieve it on demand by topic, date, or source. More memory is not automatically better memory.

### Authority and Conflict Rules

Use this precedence order whenever memories disagree:

| Rank | Evidence Type | Handling |
|---:|---|---|
| Highest | Current verified live state or directly supplied evidence | Use after validating scope and date |
| High | GitHub main-branch technical record, approved SOP, decision record | Default authority for durable facts |
| Medium | Approved Notion operational page or current daily journal | Use for planning and status, verify technical claims |
| Low | Retrieval result, old transcript, loose note, or search snippet | Lead only, never final authority |

A retrieved memory may suggest a useful direction, but it must not silently override a newer canonical record. When a material conflict appears, Manus should present the discrepancy and ask or verify before acting.

## Write Workflow

### Capture

After a task, create an episodic summary only if it contains a decision, an important fact, a failed attempt, a verified fix, a user preference, a reusable procedure, or an unresolved risk. Do not retain filler conversation.

The summary should include what happened, what was attempted, what failed, what worked, source links, scope, confidence, and whether promotion is needed. It is initially `retrieved-only` or `provisional`.

### Promote

Promote a memory only when it is useful beyond the immediate task and has a durable home:

- Technical procedure or configuration change: GitHub file or issue.
- Operating decision, priority, or approval: Notion decision page and linked GitHub issue when technical.
- Stable personal or agent preference: the reviewed operating-memory file.
- Client fact: isolated client record with sensitivity and review date.

Promotion should update the memory index with a source link. The retrieval system may then index the approved summary, not a second competing source of truth.

### Correct and Retire

When evidence changes, create a replacement record that points to the source and the superseded entry. Do not silently delete historical memory unless it contains sensitive material or an explicit retention obligation requires removal. A clean audit trail lets future agents understand why a prior approach was abandoned.

## Two Implementation Options

| Approach | What It Delivers | Tradeoffs | Cost | Setup Complexity |
|---|---|---|---|---|
| **Lean project memory, recommended first** | A Manus project with concise boot instructions, shared operating files, GitHub and Notion indexes, and a disciplined end-of-task capture ritual | Relies on Manus following the boot sequence; semantic discovery is manual or light-touch | No new infrastructure | Low |
| **Retrieval-backed memory gateway** | A context service that queries Hindsight and source indexes, assembles a scoped context pack, creates or primes Manus tasks, and records post-task memory candidates | Requires service ownership, API access, observability, indexing policy, and maintenance | Existing infrastructure plus service/API usage | Medium to high |

The lean option should be built first. It gives an immediate improvement, establishes clean source records, and produces the training data and taxonomy needed for the gateway. Building a clever retrieval system on top of messy knowledge merely gives you a faster way to retrieve chaos.

## Memory Wiki First Architecture

The existing OpenClaw Memory Wiki is the right conceptual model for Manus, but its plugin cannot be installed inside Manus itself. Instead, Manus should use a **GitHub-backed, Markdown Memory Wiki** as its reviewed knowledge layer, with Notion remaining the operational layer. Manus can then read the index and the relevant pages at the start of work, write proposed knowledge as a reviewable change, and preserve full change history through Git.

| Wiki bucket | Purpose | Canonical home | Manus access rule |
|---|---|---|---|
| `sources/` | Evidence, original documents, research snapshots, source links | GitHub Markdown | Read when validating a claim; never overwrite external evidence |
| `entities/` | Durable things: agents, clients, tools, systems, projects, vendors | GitHub Markdown | Read by named scope; write only when new facts have sources |
| `concepts/` | Reusable methods, operating patterns, brand rules, decision frameworks | GitHub Markdown | Prefer reviewed concepts over recalled chat memory |
| `syntheses/` | Source-linked conclusions, decision summaries, and reusable recommendations | GitHub Markdown and linked Notion decision page | Create or update only after a task produces a validated conclusion |
| `current/` | Compact current-state and active-priorities indexes | GitHub Markdown | Load at every relevant task start; keep short and dated |
| `reports/` | Audits, retrieval tests, and generated operational checks | GitHub Markdown | Append with date, scope, method, and result |

The Memory Wiki should sit **in front of Hindsight**. Hindsight can surface likely relevant past facts and handoff clues, but the wiki supplies reviewed and source-linked knowledge. This mirrors the existing ZedBiz Memory Wiki routing rule: raw conversational memory is not durable knowledge until it is promoted into a small, source-backed artifact.

> Start with a small `manus-memory-wiki/` directory in the general technical repository, not a giant second knowledge base. It should index and link the existing OpenClaw shared wiki, GitHub records, and Notion decision pages rather than copy them. One authority, many pointers.

### Manus Task Flow with a Wiki

| Stage | Manus behavior |
|---|---|
| Scope | Identify the business area, project, client boundary, and required authority level |
| Load | Read `current/README.md`, the relevant entity or concept page, and one matching synthesis or SOP |
| Retrieve | When enabled later, call Hindsight only for scoped leads, then validate them against wiki and canonical sources |
| Work | Perform the task using the retrieved source set; flag conflicts and stale records |
| Capture | Write a short episodic journal/issue record only when the outcome contains a reusable lesson, decision, fact, failure, or verified fix |
| Promote | Create a pull-requestable wiki update for durable knowledge, linking sources and Notion operational records where appropriate |

### Recommended Manus Wiki Pilot

| Week | Outcome |
|---|---|
| First | Create the skeleton, the root index, a technical current-state index, and five high-value entity/concept pages. Use it manually in Manus tasks. |
| Second | Add the end-of-task capture template and promote only confirmed, reusable learnings. Measure whether the index reduces repeated explanation. |
| Third | Enable the dedicated Hindsight bank as a **recall-only** assistant to find candidates and compare its results against the wiki. Retain only source-linked summaries. |

## Direct Hindsight Connection Feasibility

**Yes.** Hindsight exposes a built-in MCP endpoint per memory bank. Manus can use it as a custom MCP connection, so `recall`, `retain`, and other Hindsight tools become available during a Manus task. This adds a memory tool, not automatic hidden memory: Manus must be instructed to recall before relevant work and retain only approved summaries after it.

| Option | Connection pattern | Strength | Constraint |
|---|---|---|---|
| Direct bank-scoped MCP, recommended | `https://<protected-hindsight-host>/mcp/manus-zedbiz/` with a Bearer authorization header | Least privilege, one dedicated bank, native `recall` and `retain` tools | Requires a stable public HTTPS endpoint and a new least-privilege API key |
| REST API connector | Hindsight REST API against the same dedicated bank | Tighter control over exactly which API operations are exposed | Requires a purpose-built API connector note and explicit request handling |
| Context gateway | A small service retrieves from Hindsight and starts or primes Manus work with a bounded source-linked context pack | Makes recall consistent even when Manus does not choose the tool itself | More infrastructure and maintenance; build only after the direct pilot proves useful |

The existing central Hindsight deployment is recorded as API version `0.9.1` and already supports protected public API access for other agents. However, Manus does **not** currently have a dedicated bank, a configured custom connection, a supplied Hindsight credential, or a verified public MCP URL. The direct connector therefore remains **feasible but not configured**.

> The safe first connection is a new `manus-zedbiz` bank, not the existing `zedbiz-shared` bank. It should begin with manual recall and deliberate retain only, scoped by tags such as `domain:technical`, `domain:marketingjack`, `project:<id>`, and `client:<id>`. Do not grant Manus multi-bank management, deletion, or unfiltered shared-bank access in the pilot.

### Direct-Connection Acceptance Test

| Test | Required evidence |
|---|---|
| Secure access | Public HTTPS endpoint reaches the Hindsight MCP server and unauthenticated requests fail with `401` |
| Bank isolation | Manus connects only to `manus-zedbiz`; `list_banks`, delete, clear, and update-bank tools are not available |
| Controlled retain | A harmless, unique fact is stored with source URL, timestamp, and scope tags |
| Fresh-task recall | A new Manus task recalls that fact from the dedicated bank, shows the source link, and stays within the requested tag scope |
| No leakage | A test query cannot retrieve existing `zedbiz-shared`, client, or other agent-bank facts |
| Rollback | Disabling the custom connection returns Manus to project boot files and canonical GitHub/Notion records with no loss of source data |

## Lean Implementation Plan

### Phase A: Establish the Memory Spine

- Create the dedicated Manus project and place all continuity-dependent tasks inside it.
- Add the five boot files listed above as shared project files or as linked canonical files.
- Write the project boot instruction using the task-start sequence in this document.
- Seed `CURRENT_STATE.md` with technical records only and `ACTIVE_PRIORITIES.md` with the current strategic list.
- Create a single `MEMORY_INDEX.md` that routes agents to GitHub repositories, Notion hubs, client scopes, and the existing OpenClaw memory documentation.

### Phase B: Use the End-of-Task Memory Ritual

At the end of any material task, Manus should answer these questions before recording anything:

- What changed or was learned that will matter next week?
- Where is the canonical source of truth?
- Which scope owns this fact?
- Is the information confirmed, provisional, or merely retrieved?
- Does it need a review date, confidentiality label, or promotion?

Then it should update the GitHub issue or source file first, add an operational Notion summary second, and append a short memory-changelog entry third.

### Phase C: Add Hindsight as Retrieval, Not Authority

- Reuse the existing Hindsight practice of scope isolation and tested recall.
- Create a dedicated Manus bank family with the domain naming in this document; do not mix it with agent banks without an explicit cross-agent policy.
- Index reviewed GitHub/Notion summaries and filtered episodic records with source URLs, dates, authority, and sensitivity.
- Run a retrieval test from a new Manus task: retrieve a unique scoped fact, validate the cited source, and prove cross-client or cross-domain leakage fails closed.
- Record the test, bank design, backfill counts, and rollback path in GitHub.

### Phase D: Build the Gateway Only When the Ritual Is Working

The gateway is worthwhile if manual retrieval becomes a repeated annoyance, if multiple scheduled or API-created Manus tasks need the same context pack, or if the growing corpus makes routing unreliable.

The gateway should have four explicit components:

| Component | Responsibility |
|---|---|
| Source collector | Reads approved GitHub and Notion records, captures source metadata, and detects updates |
| Memory indexer | Sends redacted, scoped, deduplicated summaries to Hindsight or the selected retrieval system |
| Context assembler | Ranks evidence by scope, authority, freshness, and task relevance; creates a bounded context pack |
| Audit and review queue | Logs retrievals and writes, prevents duplicates, marks conflicts, and queues candidates for promotion |

The gateway should track processed IDs, source checksums, last successful runs, retry counts, write status, and task-to-memory links. Repeated runs must be idempotent: the same task should not create duplicate memories or duplicate external actions.

## Verification Before Calling It Working

| Test | Passing Condition |
|---|---|
| Fresh-task recall | A new Manus task receives the correct scoped fact and source link without manual re-explanation |
| Canonical precedence | A stale retrieval result does not override a newer GitHub or approved Notion record |
| Isolation | Client and domain information cannot be recalled from an unauthorized scope |
| Correction | A superseded fact returns the replacement record and preserves the correction trail |
| Memory quality | The context pack is short, relevant, and contains no obvious filler or secrets |
| Failure handling | If retrieval is unavailable, Manus can proceed from canonical records and reports the missing recall layer honestly |
| Task record | The GitHub issue and daily journal describe the change, test evidence, risks, and rollback position |

## Rollback

If retrieval quality, isolation, or source validation fails, disable the retrieval enrichment and continue using the lean project-memory spine. Canonical GitHub and Notion records remain intact. Do not delete native project files or historical records merely because the semantic layer fails.

## Recommended Immediate Decision

Approve **Phase A and Phase B** first. They are the smallest working version: a project-based boot context, compact source-of-truth files, and a consistent capture-and-promotion ritual. Then test it on Manus alone for one week of real tasks. Add Hindsight-backed retrieval only after the resulting records are clean enough to make retrieval genuinely useful.

## Related Records

- [OpenClaw Memory and Hindsight Management SOP](https://app.notion.com/p/0aea3e33d58182d4b93681fe1bcd7a41)
- [Technical Memory System Notion Page](https://app.notion.com/p/397a3e33d581812fa9dcfcfa80e88fab)
- [GitHub Issue Filing SOP](github-issue-filing-sop.md)
- [Technical Memory System Parent Issue](https://github.com/ZedBiz44/ZedBiz-general-tech-issues-updates/issues/1)

## Change Log

| Date | Change | Status |
|---|---|---|
| 2026-08-23 MDT | Initial Manus-specific persistent-memory architecture created. No service, connector, project configuration, or retrieval bank has been changed. | Proposed |
