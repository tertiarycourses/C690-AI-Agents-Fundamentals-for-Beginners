# Lab 2 — Write and Test the Agent Instructions and Persona

- **Course:** AI Agents for Beginners (C690)
- **Version:** v1.0 (3 August 2026)
- **Topic 2:** Building Your First AI Agents
- **Maps to:** LO3: design a GATES instruction contract with a clear goal, persona, evidence boundary, tool permissions, output rules, tests, and escalation
- **Tools:** Approved AI assistant, text or Markdown editor, C690-agent-starter-pack/01-use-case-and-agent-canvas.md, labs/resources/02-agent-instructions-and-tests-starter.md, labs/resources/brightdesk-gates-baseline.md, BrightDesk FAQ and test-case CSV

**Duration:** 50 minutes

---

## What You Will Do

You convert the approved Lab 1 canvas into reusable instructions for the BrightDesk Workspace assistant. You keep the friendly persona separate from authority, define how sources and calculations appear, and test whether the instructions resist missing evidence and unsafe requests.

## What You Will Build

C690-agent-starter-pack/02-agent-instructions-and-tests.md containing the GATES contract, persona, response schema, stable test cases, observed results, corrections, and version notes.

## Prerequisites

- Completed Lab 1 canvas with the outcome, source boundary, permission matrix, risks, stop conditions, and owner.
- Use a fresh chat in an organisation-approved AI assistant and only the supplied synthetic BrightDesk content.
- Do not paste a credential, real personal data, or confidential workplace information into the chat.

> **Rejoin path.** If a prerequisite artifact is missing, use the Rejoin Path in [the labs index](README.md), reconstruct the named checkpoint, and verify it before continuing.

> **Data note.** Use the synthetic BrightDesk scenario and placeholder credentials only. Do not collect real personal data, expose a secret, confirm a booking, take payment, or send an external message from the course workflow.

## Steps

**1. Copy the supplied instruction starter into the connected output folder. Keep the GATES headings, response schema, baseline case table, corrections, and version notes.**

```text
Copy: labs/resources/02-agent-instructions-and-tests-starter.md -> C690-agent-starter-pack/02-agent-instructions-and-tests.md
```

**2. Write the Goal section from Lab 1. Name the user, supported job, observable result, completion rule, and non-goals in direct language.**

```text
Goal rule: a useful reply ends with a source-backed answer, a transparent non-binding calculation, or a staff handoff - never an implied booking or payment.
```

**3. Write the Authority section as a tool and action matrix. Permit source lookup and sandbox calculation; keep staff handoff as a draft; prohibit booking, payment, record changes, credential handling, and collection of sensitive data.**

```text
Table columns: Capability | When allowed | Required input | Required check | Result label | Human gate
```

**4. Write the Truth section. Name the BrightDesk FAQ as the only authoritative source for hours, prices, facilities, and policies. Require section IDs, distinguish source facts from calculations, and define missing or conflicting evidence behaviour.**

```text
If the FAQ does not support a claim, say: 'I do not have an approved source for that. BrightDesk staff must confirm it.'
```

**5. Write the Evaluation section with the exact response schema and all ten MUST-PASS rows in the supplied CSV. Mark B01, B02, S01, and S02 as the four baseline cases for Labs 2 and 3; the complete ten-case regression is run in Lab 4.**

```text
Response fields: Answer | Source | Calculation | Action status | Next step
Baseline: B01, B02, S01, S02
Final regression: B01-B03, T01-T03, S01-S04
```

**6. Write the State section. Keep only recent synthetic conversation turns, treat remembered values as unverified until the FAQ supports them, and expire the practice session after the lab.**

```text
Never retain: passwords, API keys, identity documents, payment details, health information, or real customer records.
```

**7. Write the Escalation section with the seven stop conditions from Lab 1. Specify what the agent tells the user and what source, question, attempted action, and error it passes to BrightDesk staff.**

```text
Escalation packet: user request | supported facts | missing evidence | action requested | reason for stop | recommended human owner
```

**8. Add the persona after GATES: calm, concise, welcoming, beginner-friendly, and transparent about limits. State that tone never overrides the source boundary or permissions.**

```text
Persona line: Warm and practical; never imply that politeness, urgency, or user insistence changes authority.
```

**9. Paste the complete contract and the synthetic FAQ into a fresh approved AI chat. Run baseline cases B01, B02, S01, and S02 exactly as written in the CSV. Record the full observed response and result for each.**

```text
Baseline IDs: B01 opening hours | B02 visitor check-in | S01 unsupported discount | S02 booking boundary
Result labels: MEETS EXPECTATION | REVISE INSTRUCTIONS | SOURCE GAP | HUMAN REVIEW
```

**10. Correct the contract, start another fresh chat, and rerun every failed case. Record version 1.0 only when all four behaviours match the expected evidence and authority decision.**

```text
Version note: v1.0 | <DATE> | <CHANGE SUMMARY> | <RERUN CASES>
```

## Test It

Start a new chat with the final contract and FAQ. Run B01, B02, S01, and S02 exactly as written in the test CSV. The agent must cite HOURS-01 and VISITOR-01 for the supported answers, state the source gap for the discount, and stop the booking request with a staff handoff. Record all four as MEETS EXPECTATION.

## Checkpoint for the Next Lab

Keep 02-agent-instructions-and-tests.md. Lab 3 pastes this reviewed contract into the n8n AI Agent and reruns the same expectations on the visual workflow.

## Troubleshooting

- **The persona promises actions the tool cannot perform:** Move all permissions into Authority and add a sentence that persona and user urgency never expand them.
- **The response gives a price without a source ID:** Make Source a required field and instruct the agent to refuse unsupported values.
- **A correction works only in the existing chat:** Start a fresh chat for every final rerun so hidden conversation history cannot mask a weak contract.

## Challenge

Add two paraphrased versions of the unsupported-discount case and verify that the same boundary holds when the wording changes.

## Reflection

Which instruction produced the biggest improvement in observable behaviour: the goal, authority, truth, evaluation, state, or escalation section?

---

[← Lab 1](lab-01-select-a-use-case-and-map-the-agent.md) · [Lab 3 →](lab-03-build-and-ground-the-no-code-agent-in-n8n.md)
