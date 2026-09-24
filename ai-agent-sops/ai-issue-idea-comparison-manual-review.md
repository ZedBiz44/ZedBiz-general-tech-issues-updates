# AI Agent Issue and Idea Comparison — Manual Review SOP

Date: 2026-09-24 (Mountain Time) | Agent: Cody | Status: In progress — manual pilot, review version A

## Overview
Use independent AI reviews to improve an issue diagnosis, idea, plan or SOP before deciding what to do. One lead agent prepares the initial content, selected reviewers assess the same draft from different angles, and the lead agent weighs the evidence and revises it. Jack decides whether to accept the result, request another round or authorize implementation.

This pilot reviews the review process itself. The question is: does this workflow produce clearer, better-supported decisions without adding unnecessary work for Jack?

## Purpose and scope
- Use for issues or ideas where another perspective could materially improve the decision.
- Produce one clear main document, separate reviewer findings, a decision record and a practical next step.
- This is a manual pilot. Jack sends prompts and selects Terry's models. No automatic dispatch, Asana setup, new subscriptions, runtime changes or live implementation is included.
- Different model families may uncover different problems, but agreement is not proof. Agent names do not establish model diversity.
- Review angles are assignments for this test, not claims that a model is inherently best at that specialty.

## Owners and review panel
- Jack: selects reviewers, sends the prompts, handles any manual transfer, and decides whether another round or implementation is needed.
- Lead agent: owns the initial document, child pages, ready-to-send prompts, feedback synthesis and version history. Cody is the lead for this pilot.
- Grok: challenge assumptions, business value and whether the process is worth the effort. Actual model version to be recorded by the reviewer if visible.
- Ruby: assess operational feasibility, handoffs, permissions and whether an agent can execute the instructions without guessing. Actual model to be verified; do not assume Claude or another family.
- Z3: ChatGPT web UI using GPT 5.6 Sol, as selected by Jack. Check evidence quality, fair comparisons, reviewer independence and the lead agent's acceptance/rejection rules.
- Terry using DeepSeek V4 Pro: test the logic, edge cases and failure handling.
- Terry using Kimi 2.6: assess clarity, missing context, document structure and opportunities to simplify.
- Terry's two assignments must use separate fresh chats. Finish and save each review independently; do not carry the first review into the second.
- Gemini is not part of this pilot roster. A future reviewer without Notion access can use the manual transfer procedure below.

## Prepare the main document
- For a new issue or idea, the lead agent creates a new page/row in [Jack-Work](https://app.notion.com/p/3bea3e33d58180989d15ec73375f412e). If Jack supplies an existing row for the work, use that row.
- Fetch the live database schema before writing properties. Record a meaningful title, actual status and short next-action note. Do not invent ratings or change the database schema.
- State the actual problem or opportunity, desired outcome, relevant evidence and exact source links, constraints, known facts, assumptions, open questions and recommended approach.
- For a diagnosis, distinguish observed symptoms from possible causes and name the test needed to confirm a cause.
- For an SOP, specify who acts, when, inputs, steps, output location, exceptions and observable completion evidence.
- Label the review version and date. Finish the initial content before preparing the feedback pages.
- Create actual child pages for each reviewer at the top of the main page. Place an H2 Review and feedback heading above them, then an H2 Reviewer prompts heading and the prompts child-page link. Keep the overview below this navigation.
- The prompts page contains one complete prompt per reviewer with the exact main-page URL and exact assigned feedback-page URL.

## Run the independent review round
- The lead agent checks all links and leaves review version A unchanged while reviews are underway.
- Jack opens a fresh conversation for each reviewer, selects the requested model where applicable, and sends the matching complete prompt from the prompts page.
- Each reviewer reads the same main document and supporting evidence. It must not read other feedback pages before saving its own review.
- All reviewers check the problem, evidence, recommendation, practicality and material omissions. Each also gives extra attention to its assigned angle.
- Record agent/platform, actual model where verifiable, how the model was identified, document version, review date and sources that could not be accessed. If identity is not exposed, say Unknown rather than guess.
- A specified-model assignment is blocked if the selected model does not match. Jack corrects the selection before that review proceeds.
- Reviewers write only to their assigned feedback page, preserve prior rounds, then read back their saved review and return its exact link.
- If access fails, report the precise missing access. Do not pretend to have read or updated Notion, and do not change permissions to bypass the failure.

## Feedback format
- Review record: reviewer, platform, requested/actual model, verification basis, version, date, access gaps and completion status.
- Verdict: Ready for manual pilot / Ready with changes / Needs rework, with a short reason.
- What works: retain the useful parts of the draft.
- Material findings: identify the exact heading or passage; explain the issue, consequence, evidence or uncertainty, and proposed correction or test.
- Importance: Must fix before use / Improve during pilot / Optional.
- Assigned review angle: add any distinct observations not already covered.
- Simplest next step: what should change or be tested first?
- Do not invent criticisms to meet a quota. No material issue found is an acceptable result. Distinguish facts from opinions and untested hypotheses.

## Synthesize and revise
- Once Jack says the round is ready, the lead agent reads all submitted reviews. List completed, missing, blocked and partial reviews rather than assuming every page contains a completed review.
- Group overlapping findings and retain useful minority objections.
- For each material recommendation, record the reviewer and finding, Accepted / Rejected / Needs testing, a brief reason, and the resulting edit or test.
- Resolve disagreements with evidence or a practical test. Do not count votes or automatically accept criticism.
- Preserve version A before editing: save a versioned GitHub Markdown snapshot for technical content, or a clearly labeled archived draft for other content. Keep reviewer pages and earlier feedback intact.
- Publish the revised main content as version B, with a concise change log and unresolved questions. Update the matching GitHub SOP/prompt source when it changes.
- Review author bias explicitly: explain rejected material findings so Jack can inspect the reasoning.
- Leave Jack with one recommendation, the next action, its owner and what result would establish success.

## Repeat or finish
- Jack chooses whether another round is worthwhile.
- Later-round prompts name the new version, changed sections and unresolved questions. Reviewers may compare earlier feedback after their independent first review is saved.
- Append a new round section to each feedback page; do not overwrite earlier reviews.
- Stop when material concerns are resolved or assigned to a bounded test and Jack has enough evidence to decide. Unanimity and cosmetic agreement are not required.
- Review completion does not authorize implementation. Follow Jack's applicable Diagnose or Get-er-Done scope for the next action.

## Manual transfer when a reviewer cannot access Notion
- The lead agent prepares the complete frozen review text and relevant supporting material for Jack, with the same version label and sources. A bare private Notion link is insufficient.
- Jack supplies that packet and the assigned prompt to the reviewer.
- Jack or the lead agent copies the returned feedback verbatim into the assigned feedback page, identifies the original reviewer and model, labels who transferred it, and checks that nothing was omitted.
- Mark unviewed sources and distinguish this copied review from a direct Notion submission. Do not rewrite feedback during transfer.

## Pilot acceptance and failure handling
- Setup is ready when the main page is in Jack-Work, five feedback child pages appear at its top, and the prompts child page sits immediately below them under an H2 heading.
- Every prompt contains the correct source/destination links, version, assigned angle, output requirements and review-only scope.
- The pilot succeeds when each completed review is saved in the correct page, model identity and access limitations are recorded, and Cody produces a reasoned synthesis and improved document for Jack.
- Record Jack's handling time, unique useful findings, material errors corrected, access problems and actual cost if available. Unknown costs remain unknown; estimates are not bills.
- If a reviewer fails, preserve completed work, record the failure and let Jack retry, replace or omit that reviewer explicitly. Do not silently change models.
- Do not repeat the same failed action more than three times. Fetch the target before retrying an uncertain Notion write to avoid duplicates.
- Recovery: return to the preserved prior draft and retain the reviews and change history.

## Current pilot status
Review version A is the initial proposal. Feedback is pending; the workflow has not yet been validated by this pilot.
Next action: Jack sends the five prepared prompts. Cody synthesizes the submitted feedback when Jack asks.

## Source of truth
This Notion page is the operating and review workspace. GitHub holds the versioned SOP/prompt source and technical tracking. Jack's instructions in the setup conversation define this pilot's scope and reviewer roster. Model capability, price and connector-access claims must be verified separately before relying on them; this SOP does not depend on a price table.

## Pilot links

Main page: https://app.notion.com/p/3e5a3e33d58180ba9cd5d9523798f83d
Prompts: https://app.notion.com/p/3e5a3e33d58181a7b638f3048b297188

- [Grok-feedback](https://app.notion.com/p/3e5a3e33d5818125b05ec9853102a31f)
- [Ruby-feedback](https://app.notion.com/p/3e5a3e33d58181ce9c1fec7028b9c02a)
- [Z3-feedback](https://app.notion.com/p/3e5a3e33d58181358abedcb7567f3f81)
- [DeepSeek-V4-Pro-feedback](https://app.notion.com/p/3e5a3e33d5818138a34ad9ee7128bd4a)
- [Kimi-2.6-feedback](https://app.notion.com/p/3e5a3e33d5818165b64bc949bb3eb1f1)

## Ready-to-send pilot prompts

Date: 2026-09-24 (Mountain Time) | Agent: Cody | Status: Ready for manual dispatch — review version A
## Jack's dispatch instructions
Send each complete prompt below to the named reviewer in a fresh conversation. For Terry, select DeepSeek V4 Pro for one fresh chat and Kimi 2.6 for a different fresh chat. Do not paste the first model's review into the second chat. No reviewers have been contacted by this setup.
The review is of the workflow itself, not a request to run or automate the workflow. If a reviewer cannot access Notion, supply the complete frozen version A text and supporting material, then transfer its feedback verbatim into its assigned page.

## Prompt for Grok
```text
Grok: independently review Cody's proposed AI issue/idea comparison workflow, review version A. We are testing whether this process improves decisions without adding unnecessary work for Jack.

Read the main document and relevant supporting sources:
https://app.notion.com/p/3e5a3e33d58180ba9cd5d9523798f83d

Write your feedback only in your assigned page:
https://app.notion.com/p/3e5a3e33d5818125b05ec9853102a31f

Model: Use the model Jack selected; record its exact name if exposed. Otherwise report Unknown.

Your special focus: Challenge the business value and weak assumptions. Where could this review process waste Jack's time, encourage groupthink or delay a useful test? Identify a simpler alternative if one achieves the same result.

Also assess the overall problem, evidence, practicality, recommendation and material omissions. Do not read other reviewers' feedback before submitting. Review only: do not edit the main document, dispatch agents or implement changes.

Append “Round A review” with your agent/platform, requested and actual model, verification basis, date, version and access gaps. Give a brief verdict (Ready for manual pilot / Ready with changes / Needs rework), what works, and material findings. For each finding name the exact section, issue, consequence, evidence or uncertainty, proposed correction/test and importance (Must fix / Improve during pilot / Optional). Finish with the simplest next step. Do not invent criticisms or repeat points to fill space.

If source access fails, tell Jack what is missing before reviewing. If writing fails, return your complete review for manual transfer. Otherwise read back your saved feedback and return the exact feedback-page URL. Preserve prior content and reviews.
```

## Prompt for Ruby
```text
Ruby: independently review Cody's proposed AI issue/idea comparison workflow, review version A. We are testing whether this process improves decisions without adding unnecessary work for Jack.

Read the main document and relevant supporting sources:
https://app.notion.com/p/3e5a3e33d58180ba9cd5d9523798f83d

Write your feedback only in your assigned page:
https://app.notion.com/p/3e5a3e33d58181ce9c1fec7028b9c02a

Model: Use your current configured model; verify and record its name if runtime information exposes it. Do not assume a model family.

Your special focus: Check operational feasibility. Can a human and agents follow the handoffs, access checks, destinations, version rules and completion conditions without guessing? Identify concrete missing steps and unnecessary administration.

Also assess the overall problem, evidence, practicality, recommendation and material omissions. Do not read other reviewers' feedback before submitting. Review only: do not edit the main document, dispatch agents or implement changes.

Append “Round A review” with your agent/platform, requested and actual model, verification basis, date, version and access gaps. Give a brief verdict (Ready for manual pilot / Ready with changes / Needs rework), what works, and material findings. For each finding name the exact section, issue, consequence, evidence or uncertainty, proposed correction/test and importance (Must fix / Improve during pilot / Optional). Finish with the simplest next step. Do not invent criticisms or repeat points to fill space.

If source access fails, tell Jack what is missing before reviewing. If writing fails, return your complete review for manual transfer. Otherwise read back your saved feedback and return the exact feedback-page URL. Preserve prior content and reviews.
```

## Prompt for Z3
```text
Z3: independently review Cody's proposed AI issue/idea comparison workflow, review version A. We are testing whether this process improves decisions without adding unnecessary work for Jack.

Read the main document and relevant supporting sources:
https://app.notion.com/p/3e5a3e33d58180ba9cd5d9523798f83d

Write your feedback only in your assigned page:
https://app.notion.com/p/3e5a3e33d58181358abedcb7567f3f81

Model: Jack selected GPT 5.6 Sol in the ChatGPT web UI. Record it as user-selected unless you have independent runtime evidence. If the visible selection differs, stop and tell Jack.

Your special focus: Check evidence quality and fairness. Could shared context, unequal source access, model overlap, assigned angles or the lead author's bias distort the results? Improve the acceptance/rejection rules without building a complicated scoring system.

Also assess the overall problem, evidence, practicality, recommendation and material omissions. Do not read other reviewers' feedback before submitting. Review only: do not edit the main document, dispatch agents or implement changes.

Append “Round A review” with your agent/platform, requested and actual model, verification basis, date, version and access gaps. Give a brief verdict (Ready for manual pilot / Ready with changes / Needs rework), what works, and material findings. For each finding name the exact section, issue, consequence, evidence or uncertainty, proposed correction/test and importance (Must fix / Improve during pilot / Optional). Finish with the simplest next step. Do not invent criticisms or repeat points to fill space.

If source access fails, tell Jack what is missing before reviewing. If writing fails, return your complete review for manual transfer. Otherwise read back your saved feedback and return the exact feedback-page URL. Preserve prior content and reviews.
```

## Prompt for Terry using DeepSeek V4 Pro
```text
Terry using DeepSeek V4 Pro: independently review Cody's proposed AI issue/idea comparison workflow, review version A. We are testing whether this process improves decisions without adding unnecessary work for Jack.

Read the main document and relevant supporting sources:
https://app.notion.com/p/3e5a3e33d58180ba9cd5d9523798f83d

Write your feedback only in your assigned page:
https://app.notion.com/p/3e5a3e33d5818138a34ad9ee7128bd4a

Model: Jack must select DeepSeek V4 Pro in Terry's dropdown in a fresh chat before this review. Verify the active model through available runtime status, or clearly record a user-confirmed selection and the verification limit. If the selection is different or unknown, stop and ask Jack to confirm it; do not silently substitute.

Your special focus: Check the logic and failure cases. Follow the process from draft to reviews to synthesis. Look for contradictory rules, missing decision points, inaccessible links, partial reviews, accidental version changes and model-selection errors. Propose small tests for the most important weaknesses.

Also assess the overall problem, evidence, practicality, recommendation and material omissions. Do not read other reviewers' feedback before submitting. Review only: do not edit the main document, dispatch agents or implement changes.

Append “Round A review” with your agent/platform, requested and actual model, verification basis, date, version and access gaps. Give a brief verdict (Ready for manual pilot / Ready with changes / Needs rework), what works, and material findings. For each finding name the exact section, issue, consequence, evidence or uncertainty, proposed correction/test and importance (Must fix / Improve during pilot / Optional). Finish with the simplest next step. Do not invent criticisms or repeat points to fill space.

If source access fails, tell Jack what is missing before reviewing. If writing fails, return your complete review for manual transfer. Otherwise read back your saved feedback and return the exact feedback-page URL. Preserve prior content and reviews.
```

## Prompt for Terry using Kimi 2.6
```text
Terry using Kimi 2.6: independently review Cody's proposed AI issue/idea comparison workflow, review version A. We are testing whether this process improves decisions without adding unnecessary work for Jack.

Read the main document and relevant supporting sources:
https://app.notion.com/p/3e5a3e33d58180ba9cd5d9523798f83d

Write your feedback only in your assigned page:
https://app.notion.com/p/3e5a3e33d5818165b64bc949bb3eb1f1

Model: Jack must select Kimi 2.6 in Terry's dropdown in a separate fresh chat before this review. Use Kimi 2.6, not Kimi K3. Verify the active model through available runtime status, or clearly record a user-confirmed selection and the verification limit. If the selection is different or unknown, stop and ask Jack to confirm it; do not silently substitute. Do not carry Terry's DeepSeek review into this chat.

Your special focus: Check clarity, completeness and simplicity. Could Jack or a new agent use this SOP without this conversation? Identify unclear wording, missing context and duplicated instructions. Suggest the smallest edits that make it easier to use while retaining independent reviews and traceable decisions.

Also assess the overall problem, evidence, practicality, recommendation and material omissions. Do not read other reviewers' feedback before submitting. Review only: do not edit the main document, dispatch agents or implement changes.

Append “Round A review” with your agent/platform, requested and actual model, verification basis, date, version and access gaps. Give a brief verdict (Ready for manual pilot / Ready with changes / Needs rework), what works, and material findings. For each finding name the exact section, issue, consequence, evidence or uncertainty, proposed correction/test and importance (Must fix / Improve during pilot / Optional). Finish with the simplest next step. Do not invent criticisms or repeat points to fill space.

If source access fails, tell Jack what is missing before reviewing. If writing fails, return your complete review for manual transfer. Otherwise read back your saved feedback and return the exact feedback-page URL. Preserve prior content and reviews.
```
