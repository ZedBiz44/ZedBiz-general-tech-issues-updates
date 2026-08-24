# Manus Knowledge Card Audit

**Date:** 2026-08-23 MDT  
**Method:** Read-only inspection of the rendered Manus Knowledge page. No card, toggle, profile setting, connector, or external system was changed.  
**Security handling:** This report deliberately omits all secret values. Cards containing direct credential or access material are identified by title only.

## Inventory Summary

| Measure | Result |
|---|---:|
| Rendered card records | 99 |
| Active records | 98 |
| Disabled records | 1 |
| Security-removal candidates | 3 |
| Keep Core candidates | 8 |
| Keep Scoped candidates | 18 |
| Source Route candidates | 42 |
| Archive candidates | 24 |
| Review candidates | 4 |

## Important Finding

The active inventory is an accumulation of historical tasks, live-state claims, named-agent instructions, technical procedures, stable preferences, duplicated marketing notes, and direct credential material. It is not a curated business-understanding layer. This mixed structure explains both irrelevant card injection and failure to reliably apply the useful cards.

## Proposed Disposition List

| # | Card title | Created | Current state | Proposed disposition | Duplicate count |
|---:|---|---|---|---|---:|
| 1 | Agent Heartbeat Cron Job Frequency | Aug 4 | active | SOURCE ROUTE | 1 |
| 2 | WordPress Plugin Integration Strategy | Aug 2 | active | SOURCE ROUTE | 1 |
| 3 | Agent Assignment Acknowledgment and Progress Updates | Jul 31 | active | KEEP CORE | 1 |
| 4 | Agent LLM Configuration Constraint | Jul 29 | active | SOURCE ROUTE | 1 |
| 5 | SEO Plugin Preference | Jul 28 | active | KEEP SCOPED | 1 |
| 6 | Google Drive Integration SOP Documentation | Jul 26 | active | REVIEW | 1 |
| 7 | Assumption Avoidance in Agent Responses | Jul 24 | active | KEEP CORE | 1 |
| 8 | SOP Creation Standard | Jul 24 | active | REVIEW | 1 |
| 9 | Human/AI SOP Documentation Protocol | Jul 24 | active | ARCHIVE | 1 |
| 10 | Notion Re-authentication Protocol | Jul 24 | active | SOURCE ROUTE | 1 |
| 11 | WHP API and Email Credentials | Jul 22 | active | SECURITY REMOVE | 2 |
| 12 | WHP API and Email Credentials | Jul 22 | active | SECURITY REMOVE | 2 |
| 13 | README File Update Protocol | Jul 8 | active | ARCHIVE | 1 |
| 14 | GitHub Entry Protocol for Technical Issues and Updates | Jul 8 | active | ARCHIVE | 1 |
| 15 | Technical Index Scope for CURRENT_STATE.md | Jul 7 | active | REVIEW | 1 |
| 16 | Agent Knowledge Retention and Documentation Reference Protocol | Jul 7 | active | SOURCE ROUTE | 1 |
| 17 | VPS Access Skill Enhancement for Token Management | Jul 7 | active | SOURCE ROUTE | 1 |
| 18 | Agent Diagnostic Context for Ruby | Jul 5 | active | SOURCE ROUTE | 1 |
| 19 | Agent API Key Configuration and Verification Protocol | Jul 1 | active | SOURCE ROUTE | 1 |
| 20 | Fix Implementation and Documentation Protocol | Jul 1 | active | ARCHIVE | 1 |
| 21 | Agent Approval Workflow for Public Rollout | Jun 30 | active | ARCHIVE | 1 |
| 22 | Agent Zed Knowledge Research Workflow | Jun 29 | active | SOURCE ROUTE | 1 |
| 23 | Dual Channel Research Process for Agents | Jun 27 | active | SOURCE ROUTE | 1 |
| 24 | Rsync Setup SOP and Cron Job Update Protocol | Jun 19 | active | ARCHIVE | 1 |
| 25 | Ruby/Hermes Technical Documentation Protocol | Jun 17 | active | ARCHIVE | 1 |
| 26 | OpenClaw Doctor Fix Execution Protocol | Jun 17 | active | ARCHIVE | 1 |
| 27 | Sudo Access | Jun 12 | active | SOURCE ROUTE | 1 |
| 28 | Agent Registry and SOP IP Address Documentation | Jun 11 | active | SOURCE ROUTE | 1 |
| 29 | Notion Page Update Protocol | Jun 11 | active | ARCHIVE | 1 |
| 30 | Credential Management Preference | Jun 11 | active | KEEP CORE | 2 |
| 31 | OpenClaw Version Upgrade and Docker Base Image Documentation Protocol | Jun 10 | active | ARCHIVE | 1 |
| 32 | Agent Startup File Prioritization | Jun 10 | active | SOURCE ROUTE | 1 |
| 33 | Notion Page Front Matter Protocol | Jun 10 | active | SOURCE ROUTE | 1 |
| 34 | Asana Account Management Protocol | Jun 9 | active | SOURCE ROUTE | 1 |
| 35 | Agent Docker Image Management | Jun 4 | active | SOURCE ROUTE | 1 |
| 36 | Notion Content Organization Best Practices | Jun 4 | active | SOURCE ROUTE | 1 |
| 37 | Agent Tools MD File Update Protocol | Jun 2 | active | ARCHIVE | 1 |
| 38 | Documentation Review and Correction Protocol | Jun 2 | active | ARCHIVE | 1 |
| 39 | OpenClaw Agent Autonomy and File Independence | Jun 2 | active | SOURCE ROUTE | 1 |
| 40 | VPS2 Access for Harry | Jun 1 | active | SOURCE ROUTE | 1 |
| 41 | Agent Creation SOP Updates for VPS2 | Jun 1 | active | ARCHIVE | 1 |
| 42 | Agent Update and New Tool Adoption Protocol | Jun 1 | active | ARCHIVE | 1 |
| 43 | Daily GitHub and Notion Documentation Updates | May 31 | active | ARCHIVE | 1 |
| 44 | Agent Configuration Replication and Checklist Protocol | May 28 | active | SOURCE ROUTE | 1 |
| 45 | OpenClaw Agent File Structure and Consistency Preference | May 28 | active | SOURCE ROUTE | 1 |
| 46 | Notion SOP Update for 10-Agent Docker System | May 28 | active | ARCHIVE | 1 |
| 47 | Agent Model Configuration and Replication Protocol | May 28 | active | SOURCE ROUTE | 1 |
| 48 | OpenClaw Agent OAuth Connection Protocol | May 27 | active | SOURCE ROUTE | 1 |
| 49 | Task Prioritization for SOP Updates | May 24 | active | ARCHIVE | 1 |
| 50 | System Setup Workflow Preference | May 23 | active | SOURCE ROUTE | 1 |
| 51 | Caddy Explanation Constraint | May 23 | active | SOURCE ROUTE | 1 |
| 52 | Agent Operationalization Workflow | May 23 | active | SOURCE ROUTE | 1 |
| 53 | Agent Tracking Database in Notion | May 22 | active | ARCHIVE | 1 |
| 54 | Notion Interaction Protocol | May 22 | active | KEEP SCOPED | 1 |
| 55 | OpenClaw VPS Server Setup SOP Location | May 22 | active | ARCHIVE | 1 |
| 56 | GitHub Setup Documentation Protocol | May 22 | active | ARCHIVE | 1 |
| 57 | Agent Login and Access Protocol | May 17 | active | SOURCE ROUTE | 1 |
| 58 | Agent Feature Documentation Protocol | May 16 | active | ARCHIVE | 1 |
| 59 | LLM Selection for Agent Tasks | May 16 | active | SOURCE ROUTE | 1 |
| 60 | Agent Implementation and Testing Protocol | May 15 | active | ARCHIVE | 1 |
| 61 | Agent Email Check Optimization | May 14 | active | SOURCE ROUTE | 1 |
| 62 | Scheduled Email Cron Job Staggering | May 12 | active | SOURCE ROUTE | 1 |
| 63 | New SOP Documentation in Notion | May 7 | active | ARCHIVE | 1 |
| 64 | Option Presentation Format Preference | May 7 | active | KEEP CORE | 1 |
| 65 | Discord AI Agent Setup Documentation | May 7 | active | SOURCE ROUTE | 1 |
| 66 | VPS Server Access Instructions | May 7 | active | SOURCE ROUTE | 1 |
| 67 | Agent Device Pairing Automation | May 6 | active | SOURCE ROUTE | 1 |
| 68 | Agent Setup and Repair Documentation Protocol | May 5 | active | ARCHIVE | 1 |
| 69 | Victor's Role as Orchestrator Agent | May 5 | active | SOURCE ROUTE | 1 |
| 70 | Agent Reporting Protocol | Apr 30 | active | KEEP CORE | 1 |
| 71 | API Key and Default LLM Preferences for Agents | Apr 27 | active | SOURCE ROUTE | 1 |
| 72 | SSH Login User Preference | Apr 26 | active | KEEP SCOPED | 1 |
| 73 | SSH Key Storage and Permissions | Apr 26 | active | KEEP SCOPED | 1 |
| 74 | Custom Branding Guide for Agents | Apr 24 | active | SOURCE ROUTE | 1 |
| 75 | Credential Management Preference | Apr 23 | active | KEEP CORE | 2 |
| 76 | Agent Communication Protocol (ACP) Adoption | Apr 22 | active | SOURCE ROUTE | 1 |
| 77 | Problem-Solving and Action Workflow | Apr 21 | active | KEEP CORE | 1 |
| 78 | Open Claw System and Agent Creation Preferences | Apr 18 | active | SOURCE ROUTE | 1 |
| 79 | Agent Email Configuration | Apr 17 | active | SECURITY REMOVE | 1 |
| 80 | Marsha's Communication Protocol in Discord | Apr 14 | active | SOURCE ROUTE | 1 |
| 81 | Custom Reverse Proxy Operational Boundaries | Apr 13 | active | SOURCE ROUTE | 1 |
| 82 | User Interaction Workflow Preference | Apr 13 | active | KEEP CORE | 1 |
| 83 | Agent Asana Workflow | Apr 12 | active | SOURCE ROUTE | 1 |
| 84 | API Key Management Preference | Apr 10 | active | SOURCE ROUTE | 1 |
| 85 | Confirm before proceeding | Apr 17, 2025 | disabled | REVIEW | 1 |
| 86 | Newsletter Structure and Content Preferences | Mar 21, 2025 | active | KEEP SCOPED | 1 |
| 87 | Wellness Business Target Criteria Refinement | Mar 20, 2025 | active | KEEP SCOPED | 5 |
| 88 | Newsletter Tone and Style Preferences | Mar 20, 2025 | active | KEEP SCOPED | 4 |
| 89 | Wellness Business Target Criteria Refinement | Mar 20, 2025 | active | KEEP SCOPED | 5 |
| 90 | Wellness Business Target Criteria Refinement | Mar 20, 2025 | active | KEEP SCOPED | 5 |
| 91 | Wellness Business Target Criteria Refinement | Mar 20, 2025 | active | KEEP SCOPED | 5 |
| 92 | Wellness Business Target Criteria | Mar 20, 2025 | active | KEEP SCOPED | 1 |
| 93 | Newsletter Tone and Style Preferences | Mar 20, 2025 | active | KEEP SCOPED | 4 |
| 94 | Wellness Business Target Criteria Refinement | Mar 20, 2025 | active | KEEP SCOPED | 5 |
| 95 | Target Industries for Marketing Jack | Mar 20, 2025 | active | KEEP SCOPED | 1 |
| 96 | Newsletter Tone and Style Preferences | Mar 20, 2025 | active | KEEP SCOPED | 4 |
| 97 | Newsletter Tone and Style Preferences | Mar 20, 2025 | active | KEEP SCOPED | 4 |
| 98 | Marketing Jack Persona and Brand Voice | Mar 20, 2025 | active | KEEP SCOPED | 1 |
| 99 | SME Newsletter Target Audience and Preferences | Mar 20, 2025 | active | KEEP SCOPED | 1 |

## Definitions

| Disposition | Meaning |
|---|---|
| KEEP CORE | A short, stable cross-task preference or decision boundary. This tier should remain small. |
| KEEP SCOPED | A useful preference, but only when the task matches its domain. |
| SOURCE ROUTE | Replace card text with a task trigger and a link to the current canonical GitHub, Notion, registry, or live system source. |
| ARCHIVE | Preserve historical context outside active Knowledge. Do not inject into new tasks. |
| SECURITY REMOVE | Remove direct secret or access material from Knowledge. Handle any rotation decision separately. |
| REVIEW | Do not retain actively without an owner confirming it is still current and useful. |

## Recommended Approval Sequence

First, remove direct credential cards from the Knowledge layer and decide whether credential rotation is needed. Second, archive dated tasks and duplicated entries. Third, retain only the approved core and scoped cards, with concise wording. Finally, create source routes for current technical facts instead of leaving them as static memory text.
