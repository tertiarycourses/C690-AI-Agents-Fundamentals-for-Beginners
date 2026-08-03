# AI Agents for Beginners (C690) — Hands-On Labs

4 labs across 2 topics · 1 day · 7.5 instructional hours · 8 clock hours including tea breaks · 3 hours 40 minutes hands-on labs

Work through the labs in order — each one builds on the artifacts you produced in the labs before it.


## Rejoin Path

If you join after Lab 1 or resume after a gap, do not skip the connected inputs. Reconstruct and verify the smallest baseline below before starting the target lab. The supplied starter files reduce setup time but do not replace the required checks.

| Rejoin point | Minimum verified baseline |
|---|---|
| Before Lab 2 | Copy 01-use-case-and-agent-canvas-starter.md, then use the supplied BrightDesk brief and FAQ to reconstruct the outcome, success evidence, agent boundary, tools, risks, and human owner. |
| Before Lab 3 | Copy brightdesk-gates-baseline.md to 02-agent-instructions-and-tests.md, review it against the Lab 1 canvas or sources, then run baseline cases B01, B02, S01, and S02. |
| Before Lab 4 | Import the Lab 3 starter, insert labs/resources/brightdesk-gates-baseline.md and the complete synthetic FAQ, select a trainer-approved model credential, confirm five-turn memory, and pass B01, B02, S01, and S02. Duplicate that verified v1.0 workflow, add Calculator, and then run the final ten-case regression. |

## Topic 1 — Understanding AI Agents

| # | Lab | Tools | You Build |
|---|-----|-------|-----------|
| 1 | [Select a Use Case and Map the Agent](lab-01-select-a-use-case-and-map-the-agent.md) | Text or Markdown editor, labs/resources/01-use-case-and-agent-canvas-starter.md, labs/resources/brightdesk-workspace-brief.md, labs/resources/brightdesk-workspace-faq.md, optional approved AI assistant for critique | C690-agent-starter-pack/01-use-case-and-agent-canvas.md containing the user and job, outcome, success evidence, non-goals, six building blocks, tool permissions, risks, stop conditions, and human owner. |

## Topic 2 — Building Your First AI Agents

| # | Lab | Tools | You Build |
|---|-----|-------|-----------|
| 2 | [Write and Test the Agent Instructions and Persona](lab-02-write-and-test-the-agent-instructions-and-persona.md) | Approved AI assistant, text or Markdown editor, C690-agent-starter-pack/01-use-case-and-agent-canvas.md, labs/resources/02-agent-instructions-and-tests-starter.md, labs/resources/brightdesk-gates-baseline.md, BrightDesk FAQ and test-case CSV | C690-agent-starter-pack/02-agent-instructions-and-tests.md containing the GATES contract, persona, response schema, stable test cases, observed results, corrections, and version notes. |
| 3 | [Build and Ground the No-Code Agent in n8n](lab-03-build-and-ground-the-no-code-agent-in-n8n.md) | n8n Cloud or trainer-provided n8n, trainer-approved chat model credential stored in n8n Credentials, Lab 3 JSON, 03-build-and-baseline-test-log-starter.md, sanitizer script, BrightDesk FAQ, Lab 2 instruction contract | A saved n8n workflow named C690 - BrightDesk Knowledge Agent - v1.0 plus C690-agent-starter-pack/03-build-and-baseline-test-log.md and an exported credential-free workflow checkpoint. |
| 4 | [Add a Tool, Test the Boundaries, and Publish Safely](lab-04-add-a-tool-test-the-boundaries-and-publish-safely.md) | n8n practice workspace, Lab 3 workflow, Lab 4 JSON, 04-tool-tests-and-deployment-record-starter.md, sanitizer script, BrightDesk FAQ, complete test-case CSV | An n8n workflow named C690 - BrightDesk Tool Agent - v1.1 plus C690-agent-starter-pack/04-tool-tests-and-deployment-record.md and a final manifest linking all four lab artifacts. |

---

> Use the synthetic BrightDesk scenario and placeholder credentials only. Do not collect real personal data, expose a secret, confirm a booking, take payment, or send an external message from the course workflow.


_Tertiary Infotech Academy Pte Ltd · C690 · v1.0 (3 August 2026)_
