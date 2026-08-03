<div align="center">

# AI Agents for Beginners

[![Course](https://img.shields.io/badge/Course-C690-1f6feb?style=for-the-badge)](https://www.tertiarycourses.com.sg/ai-agents-for-beginners.html)
[![Platform](https://img.shields.io/badge/No--Code-n8n-ff6d5a?style=for-the-badge&logo=n8n&logoColor=white)](https://n8n.io/)
[![Level](https://img.shields.io/badge/Level-Beginner-7c3aed?style=for-the-badge)](#about)
[![Labs](https://img.shields.io/badge/Connected_Labs-4-34d399?style=for-the-badge)](#lab-activities)
[![License](https://img.shields.io/badge/License-Educational-fbbf24?style=for-the-badge)](#license)

**Aligned courseware and connected no-code labs for understanding, designing, building, grounding, tool-enabling, testing, and safely publishing a simple AI agent.**

[Course Page](https://www.tertiarycourses.com.sg/ai-agents-for-beginners.html) · [Learner Guide](LG-AI%20Agents%20for%20Beginners%20%28C690%29.md) · [Report Bug](https://github.com/tertiarycourses/C690-AI-Agents-for-Beginners/issues) · [Request Improvement](https://github.com/tertiarycourses/C690-AI-Agents-for-Beginners/issues)

</div>

> [!NOTE]
> These are the official courseware and hands-on lab materials for **AI Agents for Beginners**.  
> **Course Code:** `C690` · **Duration:** 1 day / 7.5 instructional hours · by Tertiary Courses / Tertiary Infotech  
> **Course page:** https://www.tertiarycourses.com.sg/ai-agents-for-beginners.html

---

## Lab Activities

**Lab 1 - Select a Use Case and Map the Agent** · Turn the synthetic BrightDesk brief into an observable outcome, agent-versus-workflow decision, six-block agent map, permission matrix, risks, stop conditions, and human ownership.

**Lab 2 - Write and Test the Agent Instructions and Persona** · Build a reusable GATES contract covering Goal, Authority, Truth, Evaluation, State, and Escalation; then test source, calculation, refusal, and handoff behaviour.

**Lab 3 - Build and Ground the No-Code Agent in n8n** · Import a credential-free starter, connect a trainer-approved model, add short-term memory, ground answers on the BrightDesk FAQ, and inspect execution evidence.

**Lab 4 - Add a Tool, Test the Boundaries, and Publish Safely** · Attach a Calculator tool, run the complete regression set, verify tool and safety decisions, and record publication, monitoring, pause, and rollback controls.

---

## About

This repository contains the complete, aligned learning package for **AI Agents for Beginners** (`C690`) by Tertiary Courses / Tertiary Infotech: trainer slides, learner slides, Learner Guide, Lesson Plan, detailed Markdown labs, synthetic resources, and importable n8n starter workflows.

The course moves from concepts to a controlled demonstration. Learners first distinguish chatbots, fixed workflows, and goal-directed agents. They then design one agent, translate the design into testable instructions, implement it on a visual n8n canvas, ground it on an approved source, attach one low-risk tool, and decide whether the evidence supports publication.

All four labs use the fictional **BrightDesk Workspace** scenario. Learners build one `C690-agent-starter-pack`, so each verified output becomes an input to the next lab. Availability, bookings, payments, record changes, real personal data, and secrets remain outside the course agent's authority.

### What you'll learn

| # | Activity | Core concepts |
|---|---|---|
| **1** | **Use Case and Agent Canvas** | Chatbot vs workflow vs agent, outcome evidence, agent anatomy, permission levels, stop conditions |
| **2** | **GATES Instruction Contract** | Goal, authority, truth, evaluation, state, escalation, persona, output schema, stable tests |
| **3** | **Grounded n8n Agent** | Chat Trigger, AI Agent, model, short-term memory, source boundary, execution evidence |
| **4** | **Tool and Controlled Publication** | Calculator tool, source-backed inputs, regression cases, prompt injection, monitoring, pause, rollback |

> **Full walkthrough:** start with the root Learner Guide after generation. Slides, the formatted Learner Guide, and the Lesson Plan are in [`courseware/`](courseware/); the executable activity sequence is in [`labs/`](labs/).

---

## Tool Stack

| Category | Technology or resource |
|---|---|
| **No-code automation** | [n8n](https://n8n.io/) Cloud trial or trainer-provided workspace |
| **Agent components** | Chat Trigger, AI Agent, trainer-approved chat model, Simple Memory, Calculator |
| **Knowledge** | Synthetic BrightDesk brief and FAQ with stable section IDs |
| **Design method** | GATES: Goal, Authority, Truth, Evaluation, State, Escalation |
| **Verification** | Stable CSV test set, execution inspection, source checks, tool-call checks, deployment record |
| **Safety** | Synthetic data, least authority, no secrets in prompts, human handoff, pause, and rollback |
| **Courseware** | PowerPoint/PDF slides, Learner Guide, Lesson Plan, Markdown labs, and workflow JSON starters |

---

## Architecture

```text
DESIGN
  Lab 1  BrightDesk brief + FAQ
          -> outcome + success evidence
          -> workflow-versus-agent decision
          -> tools + permissions + stop conditions + owner

INSTRUCT
  Lab 2  Lab 1 canvas
          -> GATES contract + persona + response schema
          -> normal + missing-evidence + injection + action tests

BUILD
  Lab 3  Chat Trigger -> AI Agent -> answer
                         |-> approved Chat Model
                         |-> Simple Memory
                         `-> BrightDesk FAQ in the knowledge boundary

CONTROL
  Lab 4  Lab 3 agent + Calculator tool
          -> complete regression set
          -> READY FOR CONTROLLED DEMO or HOLD
          -> monitoring + pause + rollback

CONNECTED OUTPUT
  01 canvas -> 02 instructions -> 03 build log -> 04 deployment record -> final manifest
```

---

## Project Structure

```text
C690-AI-Agents-for-Beginners/
├── README.md
├── LG-AI Agents for Beginners (C690).md
├── courseware/
│   ├── AI Agents for Beginners (C690)-v1.0.pptx
│   ├── AI Agents for Beginners (C690)-v1.0.pdf
│   ├── LG-AI Agents for Beginners (C690).docx
│   ├── LG-AI Agents for Beginners (C690).pdf
│   ├── LP-AI Agents for Beginners (C690).docx
│   └── LP-AI Agents for Beginners (C690).pdf
├── labs/
│   ├── README.md
│   ├── lab-01-select-a-use-case-and-map-the-agent.md
│   ├── lab-02-write-and-test-the-agent-instructions-and-persona.md
│   ├── lab-03-build-and-ground-the-no-code-agent-in-n8n.md
│   ├── lab-04-add-a-tool-test-the-boundaries-and-publish-safely.md
│   └── resources/
│       ├── brightdesk-workspace-brief.md
│       ├── brightdesk-workspace-faq.md
│       ├── brightdesk-agent-test-cases.csv
│       ├── C690-Lab3-BrightDesk-Knowledge-Agent.json
│       └── C690-Lab4-BrightDesk-Tool-Agent.json
└── reference/
    └── SOURCES.md
```

---

## Getting Started

### Prerequisites

- A Windows or Mac laptop with a modern web browser
- Access to the files in this repository
- A trainer-provided n8n workspace or an n8n Cloud practice workspace
- A trainer-approved model credential stored in n8n Credentials
- A text or Markdown editor

Use only the supplied synthetic BrightDesk data. Keep credentials in n8n's credential manager, never in prompts, workflow exports, screenshots, or repository files.

### 1. Clone the repository

```bash
git clone https://github.com/tertiarycourses/C690-AI-Agents-for-Beginners.git
cd C690-AI-Agents-for-Beginners
```

### 2. Start with the Learner Guide

Open the generated **LG-AI Agents for Beginners (C690).md** for the concept chapters, preparation guidance, and detailed activity instructions.

### 3. Complete the connected labs in order

1. Read [`labs/README.md`](labs/README.md).
2. Create a working folder named `C690-agent-starter-pack`.
3. Complete Labs 1 to 4 in sequence.
4. Keep the n8n workflow inactive or unpublished until Lab 4 records a controlled publication decision.
5. Export only credential-free workflow checkpoints and run the secret checks described in the labs.

### 4. Import a starter workflow into n8n

1. In n8n, open **Workflows** and create a workflow.
2. From the workflow menu, choose **Import from File**.
3. Select the JSON named by the lab.
4. Select your own approved model credential in the model node.
5. Paste only the reviewed instructions and supplied synthetic FAQ into the indicated fields.
6. Save and test before any publication decision.

---

## Contributing

Contributions, corrections, and improvements are welcome:

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/my-improvement`.
3. Commit your changes: `git commit -m "Add my improvement"`.
4. Push the branch: `git push origin feature/my-improvement`.
5. Open a pull request.

Found a bug or have an idea? Open an [issue](https://github.com/tertiarycourses/C690-AI-Agents-for-Beginners/issues).

---

## License

This material is provided for **educational use** as part of **AI Agents for Beginners (C690)**. © Tertiary Infotech Pte. Ltd. All rights reserved.

---

## Developed By

**Tertiary Infotech Pte. Ltd.** - [Tertiary Courses](https://www.tertiarycourses.com.sg)

Course: [AI Agents for Beginners (C690)](https://www.tertiarycourses.com.sg/ai-agents-for-beginners.html)

## Acknowledgements

- [n8n](https://n8n.io/) for the visual workflow and AI-agent platform used in the labs
- Anthropic and NIST for practical agent-design, evaluation, and risk-management guidance referenced in the course concepts
- Course trainers and learners who test and improve the C690 materials

---

<div align="center">

⭐ **If this helped you build a bounded, evidence-led AI agent, star the repository!**

Powered by [Tertiary Infotech Academy Pte Ltd](https://www.tertiaryinfotech.com/)

[Course Page](https://www.tertiarycourses.com.sg/ai-agents-for-beginners.html) · [Learner Guide](LG-AI%20Agents%20for%20Beginners%20%28C690%29.md)

</div>
