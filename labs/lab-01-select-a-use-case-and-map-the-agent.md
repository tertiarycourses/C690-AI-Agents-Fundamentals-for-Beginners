# Lab 1 — Select a Use Case and Map the Agent

- **Course:** AI Agents for Beginners (C690)
- **Version:** v1.0 (3 August 2026)
- **Topic 1:** Understanding AI Agents
- **Maps to:** LO1 and LO2: distinguish an agent from a chatbot or fixed workflow, then select and map a bounded beginner use case
- **Tools:** Text or Markdown editor, labs/resources/01-use-case-and-agent-canvas-starter.md, labs/resources/brightdesk-workspace-brief.md, labs/resources/brightdesk-workspace-faq.md, optional approved AI assistant for critique

**Duration:** 50 minutes

---

## What You Will Do

You begin the connected BrightDesk Workspace scenario by turning a broad support-assistant idea into a testable agent canvas. You decide where flexible agent behaviour adds value, where a fixed rule is safer, what evidence the agent may use, and which actions remain with staff.

## What You Will Build

C690-agent-starter-pack/01-use-case-and-agent-canvas.md containing the user and job, outcome, success evidence, non-goals, six building blocks, tool permissions, risks, stop conditions, and human owner.

## Prerequisites

- Create a local folder named C690-agent-starter-pack and copy the Lab 1 starter into it.
- Open the synthetic BrightDesk brief and FAQ; do not add real customer or employee information.
- Keep the design in recommendation and demonstration mode; no live booking, payment, email, or record change is permitted.

> **Data note.** Use the synthetic BrightDesk scenario and placeholder credentials only. Do not collect real personal data, expose a secret, confirm a booking, take payment, or send an external message from the course workflow.

## Steps

**1. Copy the supplied canvas starter into your connected output folder. Keep every heading and table so later checks use the same structure.**

```text
Copy: labs/resources/01-use-case-and-agent-canvas-starter.md -> C690-agent-starter-pack/01-use-case-and-agent-canvas.md
```

**2. Read brightdesk-workspace-brief.md without AI. Copy only the stated user, business need, supported services, constraints, and human owner into the matching headings. Label anything not stated as UNKNOWN.**

```text
Allowed evidence: labs/resources/brightdesk-workspace-brief.md and labs/resources/brightdesk-workspace-faq.md
```

**3. Write one observable outcome and three success signals. Keep the outcome about helping a visitor find supported information and prepare a non-binding estimate, not about maximising conversation length.**

```text
Outcome: Help a prospective BrightDesk visitor obtain a source-backed answer or estimate and reach staff when the request needs a human.
Signals: supported answer cites a section ID; calculation shows inputs; unsupported or consequential request is handed off.
```

**4. List at least five non-goals. Include confirming availability, making a booking, taking payment, changing a record, and collecting sensitive personal information.**

```text
Non-goal status: PROHIBITED | HUMAN ONLY | OUT OF SCOPE
```

**5. Classify the work into fixed workflow and agent decisions. Keep source lookup, numeric validation, permission checks, and logging deterministic; use the agent for interpreting varied questions and selecting an allowed response path.**

```text
Table columns: Work item | Fixed workflow or agent | Why | Expected evidence | Failure response
```

**6. Complete the six-block anatomy for Goal, Model, Instructions, Tools, Memory, and Guardrails. Give each block a one-sentence responsibility and one failure to watch.**

```text
Example failure: Memory repeats an unverified discount as if it were an approved price.
```

**7. Create a permission matrix for FAQ lookup, calculator, draft staff handoff, booking, payment, and customer-record update. Assign one level to every row.**

```text
Levels: ALLOW IN SANDBOX | RECOMMEND ONLY | HUMAN APPROVAL | PROHIBITED
```

**8. Add at least six risks covering unsupported claims, stale knowledge, wrong arithmetic inputs, prompt injection, unnecessary personal data, and implied booking authority. Pair each risk with prevention, detection, and response.**

```text
Table columns: Risk | Prevention | Detection | Response | Owner
```

**9. Write stop conditions for missing evidence, conflicting prices, personal or payment data, a request to ignore rules, an unavailable tool, repeated failure, and any request to confirm an external action.**

```text
Required response pattern: STOP - state the reason - preserve available evidence - offer the named human handoff.
```

**10. Review the canvas against the BrightDesk sources. Add the reviewer, date, three corrections, and unresolved questions. If you used AI for critique, verify every change against the source before accepting it.**

```text
## Review Log
- Reviewer: <INITIALS>
- Date: <YYYY-MM-DD>
- Corrections: <THREE ITEMS>
- Unresolved: <ITEM OR NONE>
```

## Test It

Open 01-use-case-and-agent-canvas.md. It must contain one observable outcome, three success signals, at least five non-goals, all six agent blocks, six permission rows, six risks with controls, seven stop conditions, and a named human owner. Ask a partner to point to any proposed action; within ten seconds you must be able to show its authority level, evidence, failure response, and owner.

## Checkpoint for the Next Lab

Keep 01-use-case-and-agent-canvas.md. Lab 2 converts its goal, evidence, permissions, risks, and stop conditions into reusable agent instructions and a stable test set.

## Troubleshooting

- **The idea is still 'a helpful assistant':** Rewrite the outcome around a named user, source-backed answer or estimate, success evidence, and staff handoff.
- **Everything is classified as agent work:** Move known rules, validation, permissions, logging, and irreversible actions into fixed workflow or human-control rows.
- **The agent can book or take payment:** Change those rows to HUMAN APPROVAL or PROHIBITED and add explicit stop language.

## Challenge

Add a simple cost-risk-value score from 1 to 5 for three possible use cases and explain why the BrightDesk support use case is the safest first build.

## Reflection

Which part of the BrightDesk task benefits most from flexible language understanding, and which part should remain deterministic even if the model appears capable?

---

[← Labs index](README.md) · [Lab 2 →](lab-02-write-and-test-the-agent-instructions-and-persona.md)
