# Lab 3 — Build and Ground the No-Code Agent in n8n

- **Course:** AI Agents for Beginners (C690)
- **Version:** v1.0 (3 August 2026)
- **Topic 2:** Building Your First AI Agents
- **Maps to:** LO4: build a simple no-code n8n agent with a chat trigger, model, memory, reviewed instructions, and an approved knowledge source
- **Tools:** n8n Cloud or trainer-provided n8n, trainer-approved chat model credential stored in n8n Credentials, Lab 3 JSON, 03-build-and-baseline-test-log-starter.md, sanitizer script, BrightDesk FAQ, Lab 2 instruction contract

**Duration:** 60 minutes

---

## What You Will Do

You implement the BrightDesk design on the n8n canvas using a supplied credential-free starter workflow. You connect your own approved model credential, paste the reviewed instructions and synthetic FAQ, use short-term memory, run the baseline questions, and inspect execution evidence.

## What You Will Build

A saved n8n workflow named C690 - BrightDesk Knowledge Agent - v1.0 plus C690-agent-starter-pack/03-build-and-baseline-test-log.md and an exported credential-free workflow checkpoint.

## Prerequisites

- Completed Lab 2 contract with all four quick tests meeting expectation.
- Access to a trainer-provided or personal n8n practice workspace.
- A model credential stored in n8n Credentials; never paste the secret into a prompt, node field, file, or screenshot.

> **Rejoin path.** If a prerequisite artifact is missing, use the Rejoin Path in [the labs index](README.md), reconstruct the named checkpoint, and verify it before continuing.

> **Data note.** Use the synthetic BrightDesk scenario and placeholder credentials only. Do not collect real personal data, expose a secret, confirm a booking, take payment, or send an external message from the course workflow.

## Steps

**1. Open n8n and choose Workflows > Create Workflow. Use the workflow menu to select Import from File, then select the supplied Lab 3 JSON.**

```text
Import: labs/resources/C690-Lab3-BrightDesk-Knowledge-Agent.json
```

**2. Rename the workflow to C690 - BrightDesk Knowledge Agent - v1.0 and keep it inactive or unpublished. Confirm the canvas contains Chat Trigger, AI Agent, OpenAI Chat Model, and Simple Memory.**

```text
Expected route: Chat Trigger -> AI Agent; OpenAI Chat Model -> AI Agent; Simple Memory -> AI Agent
```

**3. Open OpenAI Chat Model. Select a trainer-approved credential from the credential selector and choose an available low-cost chat model. If the trainer uses another supported provider, replace only the model sub-node and preserve the same test expectations.**

```text
Secret rule: create or select the credential in n8n Credentials; do not paste an API key into any prompt or export.
```

**4. Open AI Agent. In System Message, replace the GATES placeholder with the final Lab 2 contract. Preserve the required response fields and the statement that persona never changes authority.**

```text
Paste from: C690-agent-starter-pack/02-agent-instructions-and-tests.md
```

**5. Below the contract, replace the KNOWLEDGE placeholder with the complete synthetic FAQ. Add a clear boundary before and after the text so the source is treated as data rather than as higher-priority instructions.**

```text
<KNOWLEDGE source='brightdesk-workspace-faq.md'>
<PASTE COMPLETE SYNTHETIC FAQ>
</KNOWLEDGE>
```

**6. Open Simple Memory. Use the connected-chat session key from Chat Trigger and set a small context window such as five exchanges. Do not configure persistent production storage in this beginner lab.**

```text
Memory purpose: conversation continuity only; prices and policies still require the FAQ source.
```

**7. Copy the supplied build-log starter, then open Chat and run the supported baseline cases B01 and B02. Record the answer, cited section, expected result, and observed result.**

```text
Copy: labs/resources/03-build-and-baseline-test-log-starter.md -> C690-agent-starter-pack/03-build-and-baseline-test-log.md
Cases: B01 and B02
```

**8. Ask the unsupported-discount and booking-action cases. Confirm the agent states the source gap or action boundary and offers staff handoff without requesting sensitive information.**

```text
Cases: S01 and S02 from labs/resources/brightdesk-agent-test-cases.csv
```

**9. Open Executions and inspect one supported and one stopped case. Confirm Chat Trigger and AI Agent ran, the response came from the current instruction and knowledge version, and no secret or real personal data appears in the execution data.**

```text
Evidence fields: workflow version | case ID | nodes run | source cited | action status | result
```

**10. Complete the build log for B01, B02, S01, and S02. Correct the system message or knowledge boundary for any failure, start a new test session, and rerun until all four meet expectation.**

```text
Baseline IDs: B01 | B02 | S01 | S02
```

**11. Create a private-working folder inside C690-agent-starter-pack. Export the workflow there with the exact private filename shown below, then run the supplied sanitizer to create the shareable checkpoint. Re-import the sanitized copy into a blank workflow and confirm the model node asks you to select a credential. Never submit or share the private-working folder.**

```text
Private export filename: C690-agent-starter-pack/private-working/C690-BrightDesk-Knowledge-Agent-v1.0-private.json
python labs/resources/sanitize_n8n_export.py "C690-agent-starter-pack/private-working/C690-BrightDesk-Knowledge-Agent-v1.0-private.json" "C690-agent-starter-pack/C690-BrightDesk-Knowledge-Agent-v1.0.json"
Re-import the sanitized output; expected: SANITIZED OK and no selected model credential.
```

## Test It

In a fresh n8n test chat, run B01, B02, S01, and S02. All four must match the expected source and authority behaviour in the CSV. Then open the execution for S02 and verify that the workflow produced a refusal and staff handoff without any external action. Run the sanitizer, re-import the sanitized checkpoint, and confirm that it contains no credential object or secret-like value and that the model node requires credential selection.

## Checkpoint for the Next Lab

Keep the inactive v1.0 workflow, test log, and credential-free export. Lab 4 adds one Calculator tool, reruns the complete stable test set, and records the publish or hold decision.

## Troubleshooting

- **The model node shows a credential error:** Select or create the approved credential in n8n Credentials. Never solve the error by pasting the key into a prompt.
- **The agent invents a price or policy:** Check that the full FAQ is inside the knowledge boundary and strengthen the Truth rule to require a section ID or refusal.
- **The next test remembers an earlier unsupported claim:** Start a new chat session and reduce the memory window; authoritative values still come from the FAQ.

## Challenge

On a disposable copy of the FAQ, change one synthetic value and rerun its case. Restore version 1.0, start a fresh session, and rerun B01, B02, S01, and S02 before continuing to Lab 4.

## Reflection

Which execution evidence helps you distinguish a knowledge problem from an instruction problem or a model problem?

---

[← Lab 2](lab-02-write-and-test-the-agent-instructions-and-persona.md) · [Lab 4 →](lab-04-add-a-tool-test-the-boundaries-and-publish-safely.md)
