# AI Agents Fundamentals for Beginners

A two-day hands-on course on designing, building and safely running AI agents that automate real small-business workflows, from support and sales to invoices and HR.

| Course detail | Information |
|---|---|
| Course code | `C690` |
| Programme | Non-WSQ |
| Duration | 2 days, 15 instructional hours (9:30am - 5:30pm daily) |
| Registration | [View course details and register](https://www.tertiarycourses.com.sg/ai-agents-fundamentals-for-beginners.html) |

## About the course

Learners see how AI agents combine large language models, reasoning, memory and tool integration to carry out business tasks while staying under human control. The course covers prompt and context engineering, grounded retrieval (RAG), the Model Context Protocol (MCP), tool calling with permission boundaries, multi-agent handoffs and human-in-the-loop approval. Each idea is applied to customer service, sales, finance, HR and operations. It closes with evaluation, governance, security and incident recovery, so that agents can be deployed with measurable results and an accountable owner.

All business records in the course are synthetic, and no lab connects to real payment, email or HR systems.

## Learning outcomes

By the end of the course, learners will be able to:

- **LO1:** Evaluate language-model and agent designs for business workflows using architecture, evidence and measurable constraints.
- **LO2:** Prepare text, embeddings and grounded context, and build and inspect tool-enabled agent workflows.
- **LO3:** Compare and adapt domain models using reproducible training and held-out evaluation.
- **LO4:** Deploy bounded business-agent workflows with human approval, monitoring and incident recovery.

## Topics covered

1. **Foundations of AI Agents for Business:** routing requests by task and risk, model architectures, tokenisation, attention, embeddings and similarity, and memory versus business state.
2. **Building and Integrating Business AI Agents:** bounded agent loops, task contracts, context budgets, policy chunking, retrieval quality, tool-call validation, MCP and state recording.
3. **Intelligent Business Automation with AI Agents:** support triage, refund drafting, idempotency, lead research and scoring, marketing claims, invoice matching, onboarding and multi-agent coordination.
4. **Deploying, Governing, and Optimising AI Agents:** train/validation/test discipline, classifier comparison, confusion matrices, retrieval evaluation, regression suites, approvals, prompt-injection defence, least privilege, canaries and incident ownership.

## Labs

| Lab | Focus |
|---|---|
| [Lab 01: Workflow business case](labs/lab-01-workflow-business-case/README.md) | Choose a bounded workflow and calculate the capacity it releases |
| [Lab 02: Tokenize business tickets](labs/lab-02-tokenize-business-tickets/README.md) | Token IDs, masks, subwords and unknown terms with a real tokenizer |
| [Lab 03: Embeddings and similarity](labs/lab-03-embeddings-and-similarity/README.md) | Transformer embeddings, and cosine versus Euclidean similarity |
| [Lab 04: Grounded policy retrieval](labs/lab-04-grounded-policy-retrieval/README.md) | Retrieve supporting clauses and abstain when evidence is missing |
| [Lab 05: Bounded tool agent](labs/lab-05-bounded-tool-agent/README.md) | Model-directed tool loop with schema checks and a read-only boundary |
| [Lab 06: Support approval workflow](labs/lab-06-support-approval-workflow/README.md) | Refund drafts with approval-bound state transitions |
| [Lab 07: Sales evidence and consent](labs/lab-07-sales-evidence-and-consent/README.md) | Sourced lead briefs and consent-respecting outreach |
| [Lab 08: Invoice exception agent](labs/lab-08-invoice-exception-agent/README.md) | Three-way matching and evidence-based exception reports |
| [Lab 09: HR and multi-agent handoffs](labs/lab-09-hr-and-multi-agent-handoffs/README.md) | Coordinating two bounded specialist roles |
| [Lab 10: Train a support classifier](labs/lab-10-train-a-support-classifier/README.md) | Train and compare classifiers against a transparent baseline |
| [Lab 11: Agent evaluation scorecard](labs/lab-11-agent-evaluation-scorecard/README.md) | Quality and cost metrics with explicit denominators |
| [Lab 12: Governance and incident recovery](labs/lab-12-governance-and-incident-recovery/README.md) | Denied actions, approval binding, and a stop/recovery plan |

Each lab folder contains its own README and PROMPTS (Markdown and PDF), synthetic data, a `run.py` script and a `verify.py` check. Labs 2, 3 and 10 install their Python requirements into a local virtual environment. The others use only the standard library. See the [labs index](labs/README.md).

## Public package

| Artifact | Files |
|---|---|
| Slide deck (212 slides) | [PPTX](courseware/AI%20Agents%20Fundamentals%20for%20Beginners%20%28C690%29-v1.0.pptx) · [PDF](courseware/AI%20Agents%20Fundamentals%20for%20Beginners%20%28C690%29-v1.0.pdf) |
| Lesson Plan | [DOCX](courseware/LP-AI%20Agents%20Fundamentals%20for%20Beginners%20%28C690%29.docx) · [PDF](courseware/LP-AI%20Agents%20Fundamentals%20for%20Beginners%20%28C690%29.pdf) |
| Learner Guide | [DOCX](courseware/LG-AI%20Agents%20Fundamentals%20for%20Beginners%20%28C690%29.docx) · [PDF](courseware/LG-AI%20Agents%20Fundamentals%20for%20Beginners%20%28C690%29.pdf) · [Markdown](LG-AI%20Agents%20Fundamentals%20for%20Beginners%20%28C690%29.md) |

Current package: v1.0, 5 October 2026.

## Distribution boundary

This repository holds the public courseware: slides, Lesson Plan, Learner Guide and labs. Source references, internal build tools and credentials are not published. Use your own approved LLM endpoint and keep API keys in your shell environment, never in the lab folders.

## Provider

Developed and delivered by [Tertiary Infotech Academy Pte Ltd](https://www.tertiarycourses.com.sg/) (UEN 201200696W).
