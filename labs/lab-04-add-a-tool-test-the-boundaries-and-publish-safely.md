# Lab 4 — Add a Tool, Test the Boundaries, and Publish Safely

- **Course:** AI Agents for Beginners (C690)
- **Version:** v1.0 (3 August 2026)
- **Topic 2:** Building Your First AI Agents
- **Maps to:** LO5 and LO6: connect a low-risk tool, verify tool and safety behaviour, and prepare a controlled deployment with monitoring and rollback
- **Tools:** n8n practice workspace, Lab 3 workflow, Lab 4 JSON, 04-tool-tests-and-deployment-record-starter.md, sanitizer script, BrightDesk FAQ, complete test-case CSV

**Duration:** 60 minutes

---

## What You Will Do

You add a Calculator tool to the grounded BrightDesk agent so it can produce transparent, non-binding workspace estimates. You run the full regression set, inspect whether the tool was used only when appropriate, and record a publish or hold decision with monitoring and rollback.

## What You Will Build

An n8n workflow named C690 - BrightDesk Tool Agent - v1.1 plus C690-agent-starter-pack/04-tool-tests-and-deployment-record.md and a final manifest linking all four lab artifacts.

## Prerequisites

- Lab 3 workflow passes all four baseline tests and remains inactive or unpublished.
- The exported Lab 3 checkpoint is credential-free.
- You know how to Unpublish the workflow before enabling a controlled public test link.

> **Rejoin path.** If a prerequisite artifact is missing, use the Rejoin Path in [the labs index](README.md), reconstruct the named checkpoint, and verify it before continuing.

> **Data note.** Use the synthetic BrightDesk scenario and placeholder credentials only. Do not collect real personal data, expose a secret, confirm a booking, take payment, or send an external message from the course workflow.

## Steps

**1. Duplicate the verified Lab 3 v1.0 workflow and rename the duplicate C690 - BrightDesk Tool Agent - v1.1. If you are rejoining directly, first import the Lab 3 starter, insert labs/resources/brightdesk-gates-baseline.md and the complete FAQ, select an approved model credential, confirm five-turn memory, and pass B01, B02, S01, and S02; then duplicate it. The supplied Lab 4 JSON is a read-only configuration reference, not the workflow used for the diff gate.**

```text
Rejoin import: labs/resources/C690-Lab3-BrightDesk-Knowledge-Agent.json
Reference only: labs/resources/C690-Lab4-BrightDesk-Tool-Agent.json
Required before proceeding: verified v1.0 duplicated | v1.1 unpublished | B01/B02/S01/S02 pass
```

**2. Confirm Calculator is connected to the AI Agent tool port. In the system message, permit it only for arithmetic using values that the current FAQ supports; require the response to show inputs, result, source, and 'non-binding estimate'.**

```text
Tool rule: never use an invented rate, discount, availability, tax, fee, or duration; ask for a missing quantity or hand off a missing policy.
```

**3. Copy the supplied deployment-record starter. Run the ten MUST-PASS rows B01-B03, T01-T03, and S01-S04 in fresh sessions and record the expected source, expected tool decision, observed tool decision, answer, action status, and result. F01 is an optional extension.**

```text
Copy: labs/resources/04-tool-tests-and-deployment-record-starter.md -> C690-agent-starter-pack/04-tool-tests-and-deployment-record.md
```

**4. Inspect Executions for the meeting-room estimate. Confirm Calculator ran with source-backed numeric inputs. Inspect the unsupported-discount, prompt-injection, sensitive-data, and booking cases; confirm Calculator or any external action did not run when the boundary required a stop.**

```text
Evidence: case ID | Calculator called YES/NO | inputs | output | source ID | action status
```

**5. Correct and rerun every failure. Sanitize/export v1.0 and v1.1, compare them with n8n's publish diff or a JSON diff, and record the reviewer. Allowed changes are Calculator, its permission rule, and version metadata only; HOLD on any new trigger, selected credential, external tool, or public setting.**

```text
Allowed diff: Calculator node and connection | Calculator permission text | v1.1 name/version
Decision labels: READY FOR CONTROLLED DEMO | HOLD - <CASE OR UNEXPECTED DIFF>
```

**6. With trainer approval, open Chat Trigger, enable Make Chat Publicly Available, use Hosted Chat with the trainer's restricted authentication option, and choose Publish. Record the URL and publication time. Then choose Unpublish and confirm the public URL no longer works; record the unpublish time and failed-access evidence. If approval is not given, keep it unpublished and record HOLD.**

```text
Never use anonymous access for the exercise and never publish a workflow containing a secret in a prompt, real customer data, or an external write tool.
```

**7. Complete the deployment record with owner, source version, instruction version, model, permitted tool, support channel, monitoring checks, error threshold, review date, pause method, credential revoke method, and rollback version.**

```text
Rollback target: C690-BrightDesk-Knowledge-Agent-v1.0.json
```

**8. After the containment test, turn Make Chat Publicly Available off and save. Rerun the v1.0/v1.1 diff and confirm public is false, with no new trigger, credential, or external tool. Export the private v1.1 file into the existing private-working folder with the exact filename shown below. Add a Final Manifest linking artifacts 01-04 and both sanitized exports. Run the sanitizer, re-import the sanitized result, and confirm the model credential is blank before adding it to the manifest. Never submit or share the private-working folder.**

```text
Final release gates: active=false | Chat Trigger public=false | allowed diff only
Private export filename: C690-agent-starter-pack/private-working/C690-BrightDesk-Tool-Agent-v1.1-private.json
python labs/resources/sanitize_n8n_export.py "C690-agent-starter-pack/private-working/C690-BrightDesk-Tool-Agent-v1.1-private.json" "C690-agent-starter-pack/C690-BrightDesk-Tool-Agent-v1.1.json"
```

## Test It

All MUST-PASS cases in brightdesk-agent-test-cases.csv must meet the expected source, tool, and authority behaviour. The three-hour estimate must call Calculator with 40 and 3 and return S$120 as a non-binding estimate citing PRICE-01. The unsupported-discount, injection, sensitive-data, and booking cases must not trigger a tool or external action. After the controlled-demo containment test, the final workflow and sanitized export must show active=false and Chat Trigger public=false. The deployment record must contain a publish or hold decision, owner, monitoring checks, tested Unpublish path, and rollback target.

## Checkpoint for the Next Lab

Retain the complete C690-agent-starter-pack and the credential-free v1.1 export. Reuse the stable test set whenever the model, instructions, source, memory, tool, or workflow version changes.

## Troubleshooting

- **Calculator runs with a rate the user supplied:** Require every price input to match an approved FAQ section before the tool call; otherwise stop for missing evidence.
- **The agent says the room is booked:** Strengthen the non-goal and Action status rules: it can estimate only; availability and booking remain with staff.
- **The public test URL works after Unpublish:** Confirm you unpublished the correct workflow and retest from a private browser window; record the actual containment result. Then turn Make Chat Publicly Available off and save.

## Challenge

Add one malformed numeric input and one calculator failure case, then specify the exact safe user message and human handoff evidence for each.

## Reflection

What evidence would justify adding a real booking-request tool, and which approval and rollback controls would need to exist first?

---

[← Lab 3](lab-03-build-and-ground-the-no-code-agent-in-n8n.md) · [Labs index →](README.md)
