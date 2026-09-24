# AI Agent Issue and Idea Comparison — Manual Review SOP

Date: 2026-09-24 (Mountain Time) | Agent: Cody | Status: Version B — awaiting second review

## Jack does only this
- Open the Review B prompts page, choose the named reviewer and forward its complete prompt.
- Select DeepSeek V4 Pro for Terry and Kimi 2.6 for Harry; Z3 uses your selected GPT 5.6 Sol.
- Receive each review link or access-failure report. Cody prepares the pages, source packet, prompts and synthesis.
- When you return to Cody with “summarize Review B,” Cody audits every page and reports any missing coverage.
- Review Cody's recommendation and the independent synthesis checks, then decide whether to accept, test or request a focused follow-up.

## Overview and use rule
Use independent AI reviews to improve an issue diagnosis, idea, plan or SOP. One lead prepares the draft; paired reviewers answer the same questions independently; the lead compares their evidence and proposes revisions. Jack decides what to accept or implement.

Use this process when Jack asks for a comparison, or when meaningful downside, difficult reversal, conflicting evidence or an important reusable decision justifies review. For routine reversible work, recommend a small practical test rather than automatically assembling a panel. Do not override a review Jack has explicitly requested.

This is a manual pilot about the review process itself. It can uncover document and handoff defects; it cannot alone prove an optimal panel size or business return. Automatic dispatch, new subscriptions, Asana setup, credential repair and runtime changes require their own authorized work.

## Owners and paired angles
The lead agent owns the main page, child pages, complete prompts, source freeze, receipt checks, decision record and revised draft. Cody leads this pilot. Jack selects and dispatches reviewers and makes the final decision.

Keep the same three paired angles for Review B. Everyone also checks the whole proposal and may flag material issues outside the assigned angle.
### Business value and assumptions
Reviewers: Grok and Z3.
Does this process improve Jack's decisions enough to justify the time and cost? Which assumptions lack evidence? Where could it produce false confidence or delay useful action? What is the simplest worthwhile version?
### Practical execution and clarity
Reviewers: Ruby and Harry using Kimi 2.6.
Can Jack and the agents follow the steps without guessing? Are inputs, permissions, handoffs, page links, version control and completion rules clear? Where is the process too complicated, and what concrete change would make it easier to run?
### Logic, evidence and failure cases
Reviewers: Terry using DeepSeek V4 Pro and Z3.
Do the conclusions follow from the evidence? How could shared context, missing sources, model overlap or author bias distort the result? What happens when a reviewer fails or disagrees? Which small test would resolve the most important uncertainty?

Z3 writes two separate angle sections and counts as one reviewer. Paired coverage is intentional for this pilot; a reduced panel is an option to test later, not an adopted replacement. Different agents or model families do not guarantee independent evidence. Grok and Ruby reported Grok-family models in Round A; disclose overlap.

## Prepare the issue and review packet
- The lead creates a new row in [Jack-Work](https://app.notion.com/p/3bea3e33d58180989d15ec73375f412e), or uses the exact existing row Jack supplies. Fetch its current schema before setting properties; do not invent ratings or modify the schema.
- State the problem, desired result, facts and exact evidence links, assumptions, constraints, provisional recommendation and unresolved questions. For diagnoses, separate symptoms from possible causes and name the confirming test. For SOPs, include owner, inputs, actions, output, exceptions and observable completion.
- Before dispatch, state what would count as a useful outcome and the review return point. Record the lead's initial recommendation so later changes are visible.
- Finish the draft, give it a dated version, and preserve the source in GitHub at an exact commit. For nontechnical material without GitHub, use a clearly labeled read-only snapshot.
- Put current-round feedback child pages at the top under an H2 heading. Order this panel: Grok, Ruby, Z3, Terry/DeepSeek, Harry/Kimi. Use titles ending Review-B for this round. Put the H2 Reviewer prompts and its child-page link immediately below. Keep prior-round pages grouped below the current navigation.
- Prepare one complete prompt per reviewer with the exact main URL, fixed source links, assigned output URL, version, model instructions, shared angle questions, scope and return point. A reviewer must not have to reconstruct a prompt from scattered instructions.
- Before forwarding sources, use approved reviewers/platforms and remove secrets and unnecessary client/personal data. Mark sources that must stay in their authorized system.

## Access and model checks
- Each reviewer confirms it can read the required packet and access its assigned feedback page. Use an existing approved connector or CLI route; the first successful saved/read-back review verifies writing. Do not claim that another agent's access proves your own.
- If access fails, report the precise failure and the affected source/page. Use the manual-transfer path below if needed. Do not silently change credentials, bypass access controls or assume a local fault affects the fleet.
- OpenClaw reviewers record active provider/model from session_status where available. Hermes reviewers record runtime model/provider status. Web reviewers record the visible or user-selected model; identity stated in chat or a screenshot is not independent proof of backend routing.
- Record requested model, actual/reported model, verification basis and observed fallback. Unknown runtime identity remains Unknown; a clearly disclosed user selection is acceptable where the platform exposes no independent identifier. A confirmed mismatch blocks that specified-model review until Jack corrects it.
- Terry uses DeepSeek V4 Pro; Harry uses Kimi 2.6. Do not silently substitute models. Existing provider access and cost limits still apply.

## Review independently
- Each reviewer uses a fresh conversation and the same fixed required sources as its counterpart.
- Round A feedback is preserved. Review B may use the shared Round A Summary to check the revisions; this is an informed second review, not a blind repeat of A.
- Do not read another Round B submission before saving your own. Declare any prior exposure to Round B feedback; do not claim independence if exposed.
- Keep the reviewed draft and packet unchanged during the round. If a material correction is unavoidable, issue a new version and tell all reviewers which earlier sections require rechecking.
- Write only in the assigned current-round page. Give a short verdict, what works, exact section/passage for each material issue, consequence, evidence or uncertainty, proposed correction/test and importance: Must fix / Improve during pilot / Optional.
- For consequential external factual claims, cite a verifiable source or state Unsupported. Cite the draft heading for observations about the document. Separate observed failures from assumptions about causes or other agents.
- Do not invent criticism to fill a quota. For Review B, mark material Round A findings Resolved / Partly resolved / Unresolved and report any new regression.
- After saving, mark the review Submitted, read it back and return its exact URL. Keep the page-preparer and reviewer identities distinct.

## Return point and missing reviews
The return point for this manual Review B is Jack's next request to Cody to summarize it. Reviewers return their link or access failure in the same conversation as the prompt. No background monitoring or fixed 24-hour timer is configured.

At that return point, Cody audits all five pages. Full paired coverage requires all five submissions, including both Z3 sections. Cody may provide a provisional summary with missing/blocked coverage labeled; it is not a completed paired round. Jack decides whether to wait, retry, replace or explicitly omit a reviewer. Do not silently swap models or drop a pair.

For a future round, state a specific deadline or event-based return point in every prompt. A missing reviewer must not prevent reporting available findings. Stop repeated identical failed actions after three attempts, and fetch before retrying an uncertain write.

## Synthesize, check and revise
- Compare each pair first: agreements, disagreements, unique findings, evidence strength and tests needed. Then consolidate across angles. Never count Z3 twice or treat agreement as proof.
- Save the round's synthesis in a named Summary child page linked from the main page. Include a decision record: source reviewer/finding, Accepted / Rejected / Needs testing, reason, resulting edit or test and owner.
- Preserve supported minority objections. If a material dispute remains after checking the evidence, show both positions and propose a bounded test or Jack's decision. Do not manufacture consensus.
- Have Jack or a designated independent reviewer inspect at least one accepted and one rejected material finding. A reviewer may disagree with Cody's disposition; record that disagreement. A failed check triggers correction and escalation to Jack, not automatic acceptance.
- Preserve the previous draft at its commit before editing. Publish a new version, change log and exact source link. Keep all previous feedback and summaries. This pilot uses new feedback child pages for each round.
- Review completion does not itself authorize live implementation. Follow Jack's separate Diagnose or Get-er-Done scope.

## Manual transfer
If a reviewer cannot use Notion, the lead prepares the complete fixed source text and relevant evidence for Jack to forward. A private URL alone is insufficient. The reviewer discloses inaccessible sources and returns a complete review in chat.

Jack or the lead copies that feedback verbatim to the assigned page, records the reviewer/model, transfer author and source version, and checks completeness. Do not rewrite the opinion during transfer. If a required source is unavailable, label the review Partial until an equivalent packet is supplied.

## Completion versus useful outcome
A round is procedurally complete when its required reviews are saved/read back, coverage and identities are disclosed, the synthesis and independent check are recorded, and Jack receives a next action.

Value is a separate assessment: did the process catch a material error, change a decision or produce a useful risk-reducing test, and was that worth Jack's handling burden? Record approximate active handling time, unique useful findings, changes adopted and actual cost if available. Unknowns stay unknown; elapsed time is not active work time.

For this Review B, Cody's starting recommendation is to retain paired manual reviews and the targeted corrections. Success means the paired reviewers can identify whether those corrections work, any material unresolved issues have an owner/test/decision, and the synthesis spot-check is reported. This does not establish business ROI. No historical timing baseline or 20/30-minute threshold is invented.

Stop after this round unless Jack identifies an unresolved question worth another review or test. A smaller panel and automated dispatch remain separate options, not assumed improvements.

## Decision record and changes from A
The [Review A Summary](https://app.notion.com/p/3e5a3e33d581803ba510d17aa1c28957) preserves findings, dispositions and reasons. Version B implements the accepted documentation changes:
- Grok/Z3: added a use rule, explicit starting recommendation, distinction between completion and value, and a focused stopping rule. Kept Jack's requested paired design.
- Ruby: clarified Jack versus lead duties, pinned the required sources, named the decision-record destination, and corrected Terry/Harry identity and current page labels.
- Terry/Z3: added an independent synthesis check, factual-source standard and an unresolved-disagreement outcome.
- Harry: added a brief access check, platform-appropriate model disclosure and an explicit return point. His reported authentication issue is for separate diagnosis, not evidence of a shared outage.
- Not adopted: automatic dispatch, untested timing/savings thresholds, shrinking the panel by default, or using a newly invented objection as a pass/fail test.

Review B includes an independent check of one accepted disposition (fixed source packet) and one rejected disposition (automatic dispatch in this manual pilot). This check has not yet been performed.

## Current status and ownership
Round A: all five reviews and summary received. Version B: prepared for Jack's requested second review; submissions pending.
Jack sends the B prompts. Cody audits and synthesizes B when Jack returns. The Review B decision record will be saved in a Review-B-Summary child page when the reviews are assessed; it is not fabricated in advance.
Notion is the operating workspace; GitHub holds the versioned SOP, prompt source and technical history. Restore a prior source commit if needed while retaining the review history.

## Fixed source packet for Review B
Required for every reviewer:
- [Version B frozen SOP](https://github.com/ZedBiz44/ZedBiz-general-tech-issues-updates/blob/9c7637e8cd60ec2d6f840a22d84d9ee60287c691/tracking/ai-issue-idea-review/2026-09-24-version-b-snapshot.md) — controls the reviewed wording. Read the complete snapshot.
- [Complete Round A Summary, frozen](https://github.com/ZedBiz44/ZedBiz-general-tech-issues-updates/blob/e77a55d141112157de0ab3052a8b49fb30d8c278/tracking/ai-issue-idea-review/2026-09-24-review-a-summary.md) — controls the prior findings and dispositions used in this second review.
- [Version A frozen SOP and prompts](https://github.com/ZedBiz44/ZedBiz-general-tech-issues-updates/blob/465effcb61e818a80e912ec97e362835e10381ed/ai-agent-sops/ai-issue-idea-comparison-manual-review.md) — consult the passages relevant to checking corrections; it is prior-version evidence, not the active procedure.
The live main page is the working mirror and navigation. Compare its SOP with the B snapshot; report a mismatch instead of silently mixing versions. The prompt includes all three exact source URLs. The journal and live GitHub issue are optional operational background, not extra required evidence.
If a required source cannot be read, request its complete text through Jack and label any interim review Partial. Other Round B feedback pages stay closed until your own submission is saved.

## Review B destinations
- [Grok-feedback-Review-B](https://app.notion.com/p/3e5a3e33d58181f4b39dca4b2c7dfdaf)
- [Ruby-feedback-Review-B](https://app.notion.com/p/3e5a3e33d58181609b03faedb1638e7e)
- [Z3-feedback-Review-B](https://app.notion.com/p/3e5a3e33d58181c4bbe2df7a7d3ccb8e)
- [Terry-DeepSeek-V4-Pro-feedback-Review-B](https://app.notion.com/p/3e5a3e33d58181b3bdd8d8ee9fd2b7cc)
- [Harry-Kimi-2.6-feedback-Review-B](https://app.notion.com/p/3e5a3e33d58181deba3ec827edb8cd13)

## Review B prompts
Date: 2026-09-24 (Mountain Time) | Agent: Cody | Status: Review B prompts ready for manual dispatch
## Jack's instructions
Forward the complete matching prompt below in a fresh chat. Terry uses DeepSeek V4 Pro; Harry uses Kimi 2.6. Z3 uses GPT 5.6 Sol. Same pairs: Grok + Z3 for business value; Ruby + Harry for execution; Terry + Z3 for logic. Z3 writes two sections and remains one reviewer.
This round checks version B's fixes and remaining material concerns. The return point is your next request to Cody to summarize Review B. There is no automatic timer or dispatch. Reviewers return a saved feedback URL or an access-failure report to you.
## Fixed source packet for Review B
Required for every reviewer:
- [Version B frozen SOP](https://github.com/ZedBiz44/ZedBiz-general-tech-issues-updates/blob/9c7637e8cd60ec2d6f840a22d84d9ee60287c691/tracking/ai-issue-idea-review/2026-09-24-version-b-snapshot.md) — controls the reviewed wording. Read the complete snapshot.
- [Complete Round A Summary, frozen](https://github.com/ZedBiz44/ZedBiz-general-tech-issues-updates/blob/e77a55d141112157de0ab3052a8b49fb30d8c278/tracking/ai-issue-idea-review/2026-09-24-review-a-summary.md) — controls the prior findings and dispositions used in this second review.
- [Version A frozen SOP and prompts](https://github.com/ZedBiz44/ZedBiz-general-tech-issues-updates/blob/465effcb61e818a80e912ec97e362835e10381ed/ai-agent-sops/ai-issue-idea-comparison-manual-review.md) — consult the passages relevant to checking corrections; it is prior-version evidence, not the active procedure.
The live main page is the working mirror and navigation. Compare its SOP with the B snapshot; report a mismatch instead of silently mixing versions. The prompt includes all three exact source URLs. The journal and live GitHub issue are optional operational background, not extra required evidence.
If a required source cannot be read, request its complete text through Jack and label any interim review Partial. Other Round B feedback pages stay closed until your own submission is saved.

## Prompt for Grok
```text
Grok: review version B of Cody's AI issue/idea comparison SOP. This is a second review of the revisions, not a request to run or automate the process.

Main working page:
https://app.notion.com/p/3e5a3e33d58180ba9cd5d9523798f83d

Write only to your NEW Review B feedback page:
https://app.notion.com/p/3e5a3e33d58181f4b39dca4b2c7dfdaf

Required fixed sources:
Version B — read completely:
https://github.com/ZedBiz44/ZedBiz-general-tech-issues-updates/blob/9c7637e8cd60ec2d6f840a22d84d9ee60287c691/tracking/ai-issue-idea-review/2026-09-24-version-b-snapshot.md
Round A Summary — read completely, including disputed findings:
https://github.com/ZedBiz44/ZedBiz-general-tech-issues-updates/blob/e77a55d141112157de0ab3052a8b49fb30d8c278/tracking/ai-issue-idea-review/2026-09-24-review-a-summary.md
Version A — check relevant original passages:
https://github.com/ZedBiz44/ZedBiz-general-tech-issues-updates/blob/465effcb61e818a80e912ec97e362835e10381ed/ai-agent-sops/ai-issue-idea-comparison-manual-review.md

Model instruction: Use Jack's selected Grok model and record the exact visible identity and its verification basis.
If a requested model demonstrably differs, tell Jack before proceeding. If exact identity is not exposed, state the user-selected model and verification limit; do not invent runtime proof.

Answer these shared angle questions under their matching headings:
Business value and assumptions
Does this process improve Jack's decisions enough to justify the time and cost? Which assumptions lack evidence? Where could it produce false confidence or delay useful action? What is the simplest worthwhile version?

Check the whole proposal too. Mark relevant Round A issues Resolved / Partly resolved / Unresolved, citing the exact B section. Identify any new material regression. Do not repeat resolved criticism without explaining what remains wrong. Distinguish observed access failures from unverified causes or fleet-wide claims.

Independently spot-check Cody's acceptance of a fixed source packet and rejection of automated dispatch for this manual pilot. Is each disposition supported by the source and Jack's stated scope? Disagree explicitly if warranted. Do not approve merely because Cody says it is resolved.

Use the same required evidence as your counterpart. You may read the shared A Summary, but do not read other Review B submissions before saving yours. Declare any earlier exposure to B feedback. If a required source cannot be read, ask Jack for its complete text and mark the interim review Partial; do not claim full coverage.

Append an H2 Round B review: agent/platform, requested and reported model, verification basis, date/version, sources/access gaps, independence disclosure, verdict (Ready for practical use / Ready with changes / Needs rework), angle findings, synthesis spot-check and simplest next step. Each material finding needs section, consequence, evidence/uncertainty, correction/test and importance. Link support for consequential external factual claims. No criticism quota.

Preserve old content and all A reviews. Change this page's assignment status to Submitted when done, read back your saved review, and return the exact URL. If writing fails, return the complete review to Jack for verbatim transfer. The return point is Jack's next request to Cody to summarize B; return your link or access failure in this conversation. Review only—no main-page edits, dispatch, credential changes or implementation.
```

## Prompt for Ruby
```text
Ruby: review version B of Cody's AI issue/idea comparison SOP. This is a second review of the revisions, not a request to run or automate the process.

Main working page:
https://app.notion.com/p/3e5a3e33d58180ba9cd5d9523798f83d

Write only to your NEW Review B feedback page:
https://app.notion.com/p/3e5a3e33d58181609b03faedb1638e7e

Required fixed sources:
Version B — read completely:
https://github.com/ZedBiz44/ZedBiz-general-tech-issues-updates/blob/9c7637e8cd60ec2d6f840a22d84d9ee60287c691/tracking/ai-issue-idea-review/2026-09-24-version-b-snapshot.md
Round A Summary — read completely, including disputed findings:
https://github.com/ZedBiz44/ZedBiz-general-tech-issues-updates/blob/e77a55d141112157de0ab3052a8b49fb30d8c278/tracking/ai-issue-idea-review/2026-09-24-review-a-summary.md
Version A — check relevant original passages:
https://github.com/ZedBiz44/ZedBiz-general-tech-issues-updates/blob/465effcb61e818a80e912ec97e362835e10381ed/ai-agent-sops/ai-issue-idea-comparison-manual-review.md

Model instruction: Use your configured model and record runtime model/provider information. Round A reported Grok; do not assume a different family.
If a requested model demonstrably differs, tell Jack before proceeding. If exact identity is not exposed, state the user-selected model and verification limit; do not invent runtime proof.

Answer these shared angle questions under their matching headings:
Practical execution and clarity
Can Jack and the agents follow the steps without guessing? Are inputs, permissions, handoffs, page links, version control and completion rules clear? Where is the process too complicated, and what concrete change would make it easier to run?

Check the whole proposal too. Mark relevant Round A issues Resolved / Partly resolved / Unresolved, citing the exact B section. Identify any new material regression. Do not repeat resolved criticism without explaining what remains wrong. Distinguish observed access failures from unverified causes or fleet-wide claims.

Independently spot-check Cody's acceptance of a fixed source packet and rejection of automated dispatch for this manual pilot. Is each disposition supported by the source and Jack's stated scope? Disagree explicitly if warranted. Do not approve merely because Cody says it is resolved.

Use the same required evidence as your counterpart. You may read the shared A Summary, but do not read other Review B submissions before saving yours. Declare any earlier exposure to B feedback. If a required source cannot be read, ask Jack for its complete text and mark the interim review Partial; do not claim full coverage.

Append an H2 Round B review: agent/platform, requested and reported model, verification basis, date/version, sources/access gaps, independence disclosure, verdict (Ready for practical use / Ready with changes / Needs rework), angle findings, synthesis spot-check and simplest next step. Each material finding needs section, consequence, evidence/uncertainty, correction/test and importance. Link support for consequential external factual claims. No criticism quota.

Preserve old content and all A reviews. Change this page's assignment status to Submitted when done, read back your saved review, and return the exact URL. If writing fails, return the complete review to Jack for verbatim transfer. The return point is Jack's next request to Cody to summarize B; return your link or access failure in this conversation. Review only—no main-page edits, dispatch, credential changes or implementation.
```

## Prompt for Z3
```text
Z3: review version B of Cody's AI issue/idea comparison SOP. This is a second review of the revisions, not a request to run or automate the process.

Main working page:
https://app.notion.com/p/3e5a3e33d58180ba9cd5d9523798f83d

Write only to your NEW Review B feedback page:
https://app.notion.com/p/3e5a3e33d58181c4bbe2df7a7d3ccb8e

Required fixed sources:
Version B — read completely:
https://github.com/ZedBiz44/ZedBiz-general-tech-issues-updates/blob/9c7637e8cd60ec2d6f840a22d84d9ee60287c691/tracking/ai-issue-idea-review/2026-09-24-version-b-snapshot.md
Round A Summary — read completely, including disputed findings:
https://github.com/ZedBiz44/ZedBiz-general-tech-issues-updates/blob/e77a55d141112157de0ab3052a8b49fb30d8c278/tracking/ai-issue-idea-review/2026-09-24-review-a-summary.md
Version A — check relevant original passages:
https://github.com/ZedBiz44/ZedBiz-general-tech-issues-updates/blob/465effcb61e818a80e912ec97e362835e10381ed/ai-agent-sops/ai-issue-idea-comparison-manual-review.md

Model instruction: Use Jack-selected GPT 5.6 Sol. Distinguish the visible/user-selected model from independent runtime verification.
If a requested model demonstrably differs, tell Jack before proceeding. If exact identity is not exposed, state the user-selected model and verification limit; do not invent runtime proof.

Answer these shared angle questions under their matching headings:
Business value and assumptions
Does this process improve Jack's decisions enough to justify the time and cost? Which assumptions lack evidence? Where could it produce false confidence or delay useful action? What is the simplest worthwhile version?

Logic, evidence and failure cases
Do the conclusions follow from the evidence? How could shared context, missing sources, model overlap or author bias distort the result? What happens when a reviewer fails or disagrees? Which small test would resolve the most important uncertainty?

Check the whole proposal too. Mark relevant Round A issues Resolved / Partly resolved / Unresolved, citing the exact B section. Identify any new material regression. Do not repeat resolved criticism without explaining what remains wrong. Distinguish observed access failures from unverified causes or fleet-wide claims.

Independently spot-check Cody's acceptance of a fixed source packet and rejection of automated dispatch for this manual pilot. Is each disposition supported by the source and Jack's stated scope? Disagree explicitly if warranted. Do not approve merely because Cody says it is resolved.

Use the same required evidence as your counterpart. You may read the shared A Summary, but do not read other Review B submissions before saving yours. Declare any earlier exposure to B feedback. If a required source cannot be read, ask Jack for its complete text and mark the interim review Partial; do not claim full coverage.

Append an H2 Round B review: agent/platform, requested and reported model, verification basis, date/version, sources/access gaps, independence disclosure, verdict (Ready for practical use / Ready with changes / Needs rework), angle findings, synthesis spot-check and simplest next step. Each material finding needs section, consequence, evidence/uncertainty, correction/test and importance. Link support for consequential external factual claims. No criticism quota.

Preserve old content and all A reviews. Change this page's assignment status to Submitted when done, read back your saved review, and return the exact URL. If writing fails, return the complete review to Jack for verbatim transfer. The return point is Jack's next request to Cody to summarize B; return your link or access failure in this conversation. Review only—no main-page edits, dispatch, credential changes or implementation.
```

## Prompt for Terry using DeepSeek V4 Pro
```text
Terry using DeepSeek V4 Pro: review version B of Cody's AI issue/idea comparison SOP. This is a second review of the revisions, not a request to run or automate the process.

Main working page:
https://app.notion.com/p/3e5a3e33d58180ba9cd5d9523798f83d

Write only to your NEW Review B feedback page:
https://app.notion.com/p/3e5a3e33d58181b3bdd8d8ee9fd2b7cc

Required fixed sources:
Version B — read completely:
https://github.com/ZedBiz44/ZedBiz-general-tech-issues-updates/blob/9c7637e8cd60ec2d6f840a22d84d9ee60287c691/tracking/ai-issue-idea-review/2026-09-24-version-b-snapshot.md
Round A Summary — read completely, including disputed findings:
https://github.com/ZedBiz44/ZedBiz-general-tech-issues-updates/blob/e77a55d141112157de0ab3052a8b49fb30d8c278/tracking/ai-issue-idea-review/2026-09-24-review-a-summary.md
Version A — check relevant original passages:
https://github.com/ZedBiz44/ZedBiz-general-tech-issues-updates/blob/465effcb61e818a80e912ec97e362835e10381ed/ai-agent-sops/ai-issue-idea-comparison-manual-review.md

Model instruction: Jack selects DeepSeek V4 Pro for Terry. Check session_status and record the active provider/model and any observed fallback; do not silently substitute.
If a requested model demonstrably differs, tell Jack before proceeding. If exact identity is not exposed, state the user-selected model and verification limit; do not invent runtime proof.

Answer these shared angle questions under their matching headings:
Logic, evidence and failure cases
Do the conclusions follow from the evidence? How could shared context, missing sources, model overlap or author bias distort the result? What happens when a reviewer fails or disagrees? Which small test would resolve the most important uncertainty?

Check the whole proposal too. Mark relevant Round A issues Resolved / Partly resolved / Unresolved, citing the exact B section. Identify any new material regression. Do not repeat resolved criticism without explaining what remains wrong. Distinguish observed access failures from unverified causes or fleet-wide claims.

Independently spot-check Cody's acceptance of a fixed source packet and rejection of automated dispatch for this manual pilot. Is each disposition supported by the source and Jack's stated scope? Disagree explicitly if warranted. Do not approve merely because Cody says it is resolved.

Use the same required evidence as your counterpart. You may read the shared A Summary, but do not read other Review B submissions before saving yours. Declare any earlier exposure to B feedback. If a required source cannot be read, ask Jack for its complete text and mark the interim review Partial; do not claim full coverage.

Append an H2 Round B review: agent/platform, requested and reported model, verification basis, date/version, sources/access gaps, independence disclosure, verdict (Ready for practical use / Ready with changes / Needs rework), angle findings, synthesis spot-check and simplest next step. Each material finding needs section, consequence, evidence/uncertainty, correction/test and importance. Link support for consequential external factual claims. No criticism quota.

Preserve old content and all A reviews. Change this page's assignment status to Submitted when done, read back your saved review, and return the exact URL. If writing fails, return the complete review to Jack for verbatim transfer. The return point is Jack's next request to Cody to summarize B; return your link or access failure in this conversation. Review only—no main-page edits, dispatch, credential changes or implementation.
```

## Prompt for Harry using Kimi 2.6
```text
Harry using Kimi 2.6: review version B of Cody's AI issue/idea comparison SOP. This is a second review of the revisions, not a request to run or automate the process.

Main working page:
https://app.notion.com/p/3e5a3e33d58180ba9cd5d9523798f83d

Write only to your NEW Review B feedback page:
https://app.notion.com/p/3e5a3e33d58181deba3ec827edb8cd13

Required fixed sources:
Version B — read completely:
https://github.com/ZedBiz44/ZedBiz-general-tech-issues-updates/blob/9c7637e8cd60ec2d6f840a22d84d9ee60287c691/tracking/ai-issue-idea-review/2026-09-24-version-b-snapshot.md
Round A Summary — read completely, including disputed findings:
https://github.com/ZedBiz44/ZedBiz-general-tech-issues-updates/blob/e77a55d141112157de0ab3052a8b49fb30d8c278/tracking/ai-issue-idea-review/2026-09-24-review-a-summary.md
Version A — check relevant original passages:
https://github.com/ZedBiz44/ZedBiz-general-tech-issues-updates/blob/465effcb61e818a80e912ec97e362835e10381ed/ai-agent-sops/ai-issue-idea-comparison-manual-review.md

Model instruction: Jack selects Kimi 2.6 for Harry. Check session_status and record the active provider/model and any observed fallback; do not silently substitute.
If a requested model demonstrably differs, tell Jack before proceeding. If exact identity is not exposed, state the user-selected model and verification limit; do not invent runtime proof.

Answer these shared angle questions under their matching headings:
Practical execution and clarity
Can Jack and the agents follow the steps without guessing? Are inputs, permissions, handoffs, page links, version control and completion rules clear? Where is the process too complicated, and what concrete change would make it easier to run?

Check the whole proposal too. Mark relevant Round A issues Resolved / Partly resolved / Unresolved, citing the exact B section. Identify any new material regression. Do not repeat resolved criticism without explaining what remains wrong. Distinguish observed access failures from unverified causes or fleet-wide claims.

Independently spot-check Cody's acceptance of a fixed source packet and rejection of automated dispatch for this manual pilot. Is each disposition supported by the source and Jack's stated scope? Disagree explicitly if warranted. Do not approve merely because Cody says it is resolved.

Use the same required evidence as your counterpart. You may read the shared A Summary, but do not read other Review B submissions before saving yours. Declare any earlier exposure to B feedback. If a required source cannot be read, ask Jack for its complete text and mark the interim review Partial; do not claim full coverage.

Append an H2 Round B review: agent/platform, requested and reported model, verification basis, date/version, sources/access gaps, independence disclosure, verdict (Ready for practical use / Ready with changes / Needs rework), angle findings, synthesis spot-check and simplest next step. Each material finding needs section, consequence, evidence/uncertainty, correction/test and importance. Link support for consequential external factual claims. No criticism quota.

Preserve old content and all A reviews. Change this page's assignment status to Submitted when done, read back your saved review, and return the exact URL. If writing fails, return the complete review to Jack for verbatim transfer. The return point is Jack's next request to Cody to summarize B; return your link or access failure in this conversation. Review only—no main-page edits, dispatch, credential changes or implementation.
```
