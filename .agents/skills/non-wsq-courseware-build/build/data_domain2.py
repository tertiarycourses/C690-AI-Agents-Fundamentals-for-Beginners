"""Topic 2 - Building Your First AI Agents."""

DOMAIN2 = [
    dict(
        num=2,
        topic=2,
        title="Write and Test the Agent Instructions and Persona",
        objective="LO3: design a GATES instruction contract with a clear goal, persona, evidence boundary, tool permissions, output rules, tests, and escalation",
        duration="50 minutes",
        desc=(
            "You convert the approved Lab 1 canvas into reusable instructions for the BrightDesk Workspace assistant. "
            "You keep the friendly persona separate from authority, define how sources and calculations appear, and test whether the instructions resist missing evidence and unsafe requests."
        ),
        build="C690-agent-starter-pack/02-agent-instructions-and-tests.md containing the GATES contract, persona, response schema, stable test cases, observed results, corrections, and version notes.",
        services="Approved AI assistant, text or Markdown editor, C690-agent-starter-pack/01-use-case-and-agent-canvas.md, labs/resources/02-agent-instructions-and-tests-starter.md, labs/resources/brightdesk-gates-baseline.md, BrightDesk FAQ and test-case CSV",
        prerequisites=[
            "Completed Lab 1 canvas with the outcome, source boundary, permission matrix, risks, stop conditions, and owner.",
            "Use a fresh chat in an organisation-approved AI assistant and only the supplied synthetic BrightDesk content.",
            "Do not paste a credential, real personal data, or confidential workplace information into the chat.",
        ],
        deck_steps=[
            "Translate the Lab 1 canvas into the six GATES sections.",
            "Add a friendly persona without expanding authority.",
            "Define a source-linked response schema and missing-evidence behaviour.",
            "Run normal, unsupported, injection, and action-boundary tests; revise and rerun.",
        ],
        deck_verify="Fresh-chat baseline cases B01, B02, S01, and S02 all meet expectation.",
        steps=[
            (
                "Copy the supplied instruction starter into the connected output folder. Keep the GATES headings, response schema, baseline case table, corrections, and version notes.",
                "Copy: labs/resources/02-agent-instructions-and-tests-starter.md -> C690-agent-starter-pack/02-agent-instructions-and-tests.md",
            ),
            (
                "Write the Goal section from Lab 1. Name the user, supported job, observable result, completion rule, and non-goals in direct language.",
                "Goal rule: a useful reply ends with a source-backed answer, a transparent non-binding calculation, or a staff handoff - never an implied booking or payment.",
            ),
            (
                "Write the Authority section as a tool and action matrix. Permit source lookup and sandbox calculation; keep staff handoff as a draft; prohibit booking, payment, record changes, credential handling, and collection of sensitive data.",
                "Table columns: Capability | When allowed | Required input | Required check | Result label | Human gate",
            ),
            (
                "Write the Truth section. Name the BrightDesk FAQ as the only authoritative source for hours, prices, facilities, and policies. Require section IDs, distinguish source facts from calculations, and define missing or conflicting evidence behaviour.",
                "If the FAQ does not support a claim, say: 'I do not have an approved source for that. BrightDesk staff must confirm it.'",
            ),
            (
                "Write the Evaluation section with the exact response schema and all ten MUST-PASS rows in the supplied CSV. Mark B01, B02, S01, and S02 as the four baseline cases for Labs 2 and 3; the complete ten-case regression is run in Lab 4.",
                "Response fields: Answer | Source | Calculation | Action status | Next step\nBaseline: B01, B02, S01, S02\nFinal regression: B01-B03, T01-T03, S01-S04",
            ),
            (
                "Write the State section. Keep only recent synthetic conversation turns, treat remembered values as unverified until the FAQ supports them, and expire the practice session after the lab.",
                "Never retain: passwords, API keys, identity documents, payment details, health information, or real customer records.",
            ),
            (
                "Write the Escalation section with the seven stop conditions from Lab 1. Specify what the agent tells the user and what source, question, attempted action, and error it passes to BrightDesk staff.",
                "Escalation packet: user request | supported facts | missing evidence | action requested | reason for stop | recommended human owner",
            ),
            (
                "Add the persona after GATES: calm, concise, welcoming, beginner-friendly, and transparent about limits. State that tone never overrides the source boundary or permissions.",
                "Persona line: Warm and practical; never imply that politeness, urgency, or user insistence changes authority.",
            ),
            (
                "Paste the complete contract and the synthetic FAQ into a fresh approved AI chat. Run baseline cases B01, B02, S01, and S02 exactly as written in the CSV. Record the full observed response and result for each.",
                "Baseline IDs: B01 opening hours | B02 visitor check-in | S01 unsupported discount | S02 booking boundary\nResult labels: MEETS EXPECTATION | REVISE INSTRUCTIONS | SOURCE GAP | HUMAN REVIEW",
            ),
            (
                "Correct the contract, start another fresh chat, and rerun every failed case. Record version 1.0 only when all four behaviours match the expected evidence and authority decision.",
                "Version note: v1.0 | <DATE> | <CHANGE SUMMARY> | <RERUN CASES>",
            ),
        ],
        test=(
            "Start a new chat with the final contract and FAQ. Run B01, B02, S01, and S02 exactly as written in the test CSV. "
            "The agent must cite HOURS-01 and VISITOR-01 for the supported answers, state the source gap for the discount, and stop the booking request with a staff handoff. Record all four as MEETS EXPECTATION."
        ),
        checkpoint="Keep 02-agent-instructions-and-tests.md. Lab 3 pastes this reviewed contract into the n8n AI Agent and reruns the same expectations on the visual workflow.",
        troubleshooting=[
            ("The persona promises actions the tool cannot perform", "Move all permissions into Authority and add a sentence that persona and user urgency never expand them."),
            ("The response gives a price without a source ID", "Make Source a required field and instruct the agent to refuse unsupported values."),
            ("A correction works only in the existing chat", "Start a fresh chat for every final rerun so hidden conversation history cannot mask a weak contract."),
        ],
        challenge="Add two paraphrased versions of the unsupported-discount case and verify that the same boundary holds when the wording changes.",
        reflection="Which instruction produced the biggest improvement in observable behaviour: the goal, authority, truth, evaluation, state, or escalation section?",
    ),
    dict(
        num=3,
        topic=2,
        title="Build and Ground the No-Code Agent in n8n",
        objective="LO4: build a simple no-code n8n agent with a chat trigger, model, memory, reviewed instructions, and an approved knowledge source",
        duration="60 minutes",
        desc=(
            "You implement the BrightDesk design on the n8n canvas using a supplied credential-free starter workflow. "
            "You connect your own approved model credential, paste the reviewed instructions and synthetic FAQ, use short-term memory, run the baseline questions, and inspect execution evidence."
        ),
        build="A saved n8n workflow named C690 - BrightDesk Knowledge Agent - v1.0 plus C690-agent-starter-pack/03-build-and-baseline-test-log.md and an exported credential-free workflow checkpoint.",
        services="n8n Cloud or trainer-provided n8n, trainer-approved chat model credential stored in n8n Credentials, Lab 3 JSON, 03-build-and-baseline-test-log-starter.md, sanitizer script, BrightDesk FAQ, Lab 2 instruction contract",
        prerequisites=[
            "Completed Lab 2 contract with all four quick tests meeting expectation.",
            "Access to a trainer-provided or personal n8n practice workspace.",
            "A model credential stored in n8n Credentials; never paste the secret into a prompt, node field, file, or screenshot.",
        ],
        deck_steps=[
            "Import the credential-free starter and inspect the four-node route.",
            "Select an approved model credential; insert GATES and the synthetic FAQ.",
            "Run B01, B02, S01, and S02 in test chat; inspect executions.",
            "Fix failures, rerun, and sanitize/re-import the checkpoint.",
        ],
        deck_verify="B01, B02, S01, and S02 pass; the sanitized export re-imports with no selected credential.",
        steps=[
            (
                "Open n8n and choose Workflows > Create Workflow. Use the workflow menu to select Import from File, then select the supplied Lab 3 JSON.",
                "Import: labs/resources/C690-Lab3-BrightDesk-Knowledge-Agent.json",
            ),
            (
                "Rename the workflow to C690 - BrightDesk Knowledge Agent - v1.0 and keep it inactive or unpublished. Confirm the canvas contains Chat Trigger, AI Agent, OpenAI Chat Model, and Simple Memory.",
                "Expected route: Chat Trigger -> AI Agent; OpenAI Chat Model -> AI Agent; Simple Memory -> AI Agent",
            ),
            (
                "Open OpenAI Chat Model. Select a trainer-approved credential from the credential selector and choose an available low-cost chat model. If the trainer uses another supported provider, replace only the model sub-node and preserve the same test expectations.",
                "Secret rule: create or select the credential in n8n Credentials; do not paste an API key into any prompt or export.",
            ),
            (
                "Open AI Agent. In System Message, replace the GATES placeholder with the final Lab 2 contract. Preserve the required response fields and the statement that persona never changes authority.",
                "Paste from: C690-agent-starter-pack/02-agent-instructions-and-tests.md",
            ),
            (
                "Below the contract, replace the KNOWLEDGE placeholder with the complete synthetic FAQ. Add a clear boundary before and after the text so the source is treated as data rather than as higher-priority instructions.",
                "<KNOWLEDGE source='brightdesk-workspace-faq.md'>\n<PASTE COMPLETE SYNTHETIC FAQ>\n</KNOWLEDGE>",
            ),
            (
                "Open Simple Memory. Use the connected-chat session key from Chat Trigger and set a small context window such as five exchanges. Do not configure persistent production storage in this beginner lab.",
                "Memory purpose: conversation continuity only; prices and policies still require the FAQ source.",
            ),
            (
                "Copy the supplied build-log starter, then open Chat and run the supported baseline cases B01 and B02. Record the answer, cited section, expected result, and observed result.",
                "Copy: labs/resources/03-build-and-baseline-test-log-starter.md -> C690-agent-starter-pack/03-build-and-baseline-test-log.md\nCases: B01 and B02",
            ),
            (
                "Ask the unsupported-discount and booking-action cases. Confirm the agent states the source gap or action boundary and offers staff handoff without requesting sensitive information.",
                "Cases: S01 and S02 from labs/resources/brightdesk-agent-test-cases.csv",
            ),
            (
                "Open Executions and inspect one supported and one stopped case. Confirm Chat Trigger and AI Agent ran, the response came from the current instruction and knowledge version, and no secret or real personal data appears in the execution data.",
                "Evidence fields: workflow version | case ID | nodes run | source cited | action status | result",
            ),
            (
                "Complete the build log for B01, B02, S01, and S02. Correct the system message or knowledge boundary for any failure, start a new test session, and rerun until all four meet expectation.",
                "Baseline IDs: B01 | B02 | S01 | S02",
            ),
            (
                "Create a private-working folder inside C690-agent-starter-pack. Export the workflow there with the exact private filename shown below, then run the supplied sanitizer to create the shareable checkpoint. Re-import the sanitized copy into a blank workflow and confirm the model node asks you to select a credential. Never submit or share the private-working folder.",
                "Private export filename: C690-agent-starter-pack/private-working/C690-BrightDesk-Knowledge-Agent-v1.0-private.json\npython labs/resources/sanitize_n8n_export.py \"C690-agent-starter-pack/private-working/C690-BrightDesk-Knowledge-Agent-v1.0-private.json\" \"C690-agent-starter-pack/C690-BrightDesk-Knowledge-Agent-v1.0.json\"\nRe-import the sanitized output; expected: SANITIZED OK and no selected model credential.",
            ),
        ],
        test=(
            "In a fresh n8n test chat, run B01, B02, S01, and S02. All four must match the expected source and authority behaviour in the CSV. "
            "Then open the execution for S02 and verify that the workflow produced a refusal and staff handoff without any external action. Run the sanitizer, re-import the sanitized checkpoint, and confirm that it contains no credential object or secret-like value and that the model node requires credential selection."
        ),
        checkpoint="Keep the inactive v1.0 workflow, test log, and credential-free export. Lab 4 adds one Calculator tool, reruns the complete stable test set, and records the publish or hold decision.",
        troubleshooting=[
            ("The model node shows a credential error", "Select or create the approved credential in n8n Credentials. Never solve the error by pasting the key into a prompt."),
            ("The agent invents a price or policy", "Check that the full FAQ is inside the knowledge boundary and strengthen the Truth rule to require a section ID or refusal."),
            ("The next test remembers an earlier unsupported claim", "Start a new chat session and reduce the memory window; authoritative values still come from the FAQ."),
        ],
        challenge="On a disposable copy of the FAQ, change one synthetic value and rerun its case. Restore version 1.0, start a fresh session, and rerun B01, B02, S01, and S02 before continuing to Lab 4.",
        reflection="Which execution evidence helps you distinguish a knowledge problem from an instruction problem or a model problem?",
    ),
    dict(
        num=4,
        topic=2,
        title="Add a Tool, Test the Boundaries, and Publish Safely",
        objective="LO5 and LO6: connect a low-risk tool, verify tool and safety behaviour, and prepare a controlled deployment with monitoring and rollback",
        duration="60 minutes",
        desc=(
            "You add a Calculator tool to the grounded BrightDesk agent so it can produce transparent, non-binding workspace estimates. "
            "You run the full regression set, inspect whether the tool was used only when appropriate, and record a publish or hold decision with monitoring and rollback."
        ),
        build="An n8n workflow named C690 - BrightDesk Tool Agent - v1.1 plus C690-agent-starter-pack/04-tool-tests-and-deployment-record.md and a final manifest linking all four lab artifacts.",
        services="n8n practice workspace, Lab 3 workflow, Lab 4 JSON, 04-tool-tests-and-deployment-record-starter.md, sanitizer script, BrightDesk FAQ, complete test-case CSV",
        prerequisites=[
            "Lab 3 workflow passes all four baseline tests and remains inactive or unpublished.",
            "The exported Lab 3 checkpoint is credential-free.",
            "You know how to Unpublish the workflow before enabling a controlled public test link.",
        ],
        deck_steps=[
            "Add Calculator with a narrow, non-binding rule.",
            "Run ten normal, boundary, tool, injection, privacy, and action cases.",
            "Inspect tool calls, refusals, and handoffs; fix and rerun.",
            "Record publish or hold, owner, monitoring, Unpublish, and rollback.",
        ],
        deck_verify="Ten cases pass; the diff is approved; Publish/Unpublish containment is verified.",
        steps=[
            (
                "Duplicate the verified Lab 3 v1.0 workflow and rename the duplicate C690 - BrightDesk Tool Agent - v1.1. If you are rejoining directly, first import the Lab 3 starter, insert labs/resources/brightdesk-gates-baseline.md and the complete FAQ, select an approved model credential, confirm five-turn memory, and pass B01, B02, S01, and S02; then duplicate it. The supplied Lab 4 JSON is a read-only configuration reference, not the workflow used for the diff gate.",
                "Rejoin import: labs/resources/C690-Lab3-BrightDesk-Knowledge-Agent.json\nReference only: labs/resources/C690-Lab4-BrightDesk-Tool-Agent.json\nRequired before proceeding: verified v1.0 duplicated | v1.1 unpublished | B01/B02/S01/S02 pass",
            ),
            (
                "Confirm Calculator is connected to the AI Agent tool port. In the system message, permit it only for arithmetic using values that the current FAQ supports; require the response to show inputs, result, source, and 'non-binding estimate'.",
                "Tool rule: never use an invented rate, discount, availability, tax, fee, or duration; ask for a missing quantity or hand off a missing policy.",
            ),
            (
                "Copy the supplied deployment-record starter. Run the ten MUST-PASS rows B01-B03, T01-T03, and S01-S04 in fresh sessions and record the expected source, expected tool decision, observed tool decision, answer, action status, and result. F01 is an optional extension.",
                "Copy: labs/resources/04-tool-tests-and-deployment-record-starter.md -> C690-agent-starter-pack/04-tool-tests-and-deployment-record.md",
            ),
            (
                "Inspect Executions for the meeting-room estimate. Confirm Calculator ran with source-backed numeric inputs. Inspect the unsupported-discount, prompt-injection, sensitive-data, and booking cases; confirm Calculator or any external action did not run when the boundary required a stop.",
                "Evidence: case ID | Calculator called YES/NO | inputs | output | source ID | action status",
            ),
            (
                "Correct and rerun every failure. Sanitize/export v1.0 and v1.1, compare them with n8n's publish diff or a JSON diff, and record the reviewer. Allowed changes are Calculator, its permission rule, and version metadata only; HOLD on any new trigger, selected credential, external tool, or public setting.",
                "Allowed diff: Calculator node and connection | Calculator permission text | v1.1 name/version\nDecision labels: READY FOR CONTROLLED DEMO | HOLD - <CASE OR UNEXPECTED DIFF>",
            ),
            (
                "With trainer approval, open Chat Trigger, enable Make Chat Publicly Available, use Hosted Chat with the trainer's restricted authentication option, and choose Publish. Record the URL and publication time. Then choose Unpublish and confirm the public URL no longer works; record the unpublish time and failed-access evidence. If approval is not given, keep it unpublished and record HOLD.",
                "Never use anonymous access for the exercise and never publish a workflow containing a secret in a prompt, real customer data, or an external write tool.",
            ),
            (
                "Complete the deployment record with owner, source version, instruction version, model, permitted tool, support channel, monitoring checks, error threshold, review date, pause method, credential revoke method, and rollback version.",
                "Rollback target: C690-BrightDesk-Knowledge-Agent-v1.0.json",
            ),
            (
                "After the containment test, turn Make Chat Publicly Available off and save. Rerun the v1.0/v1.1 diff and confirm public is false, with no new trigger, credential, or external tool. Export the private v1.1 file into the existing private-working folder with the exact filename shown below. Add a Final Manifest linking artifacts 01-04 and both sanitized exports. Run the sanitizer, re-import the sanitized result, and confirm the model credential is blank before adding it to the manifest. Never submit or share the private-working folder.",
                "Final release gates: active=false | Chat Trigger public=false | allowed diff only\nPrivate export filename: C690-agent-starter-pack/private-working/C690-BrightDesk-Tool-Agent-v1.1-private.json\npython labs/resources/sanitize_n8n_export.py \"C690-agent-starter-pack/private-working/C690-BrightDesk-Tool-Agent-v1.1-private.json\" \"C690-agent-starter-pack/C690-BrightDesk-Tool-Agent-v1.1.json\"",
            ),
        ],
        test=(
            "All MUST-PASS cases in brightdesk-agent-test-cases.csv must meet the expected source, tool, and authority behaviour. The three-hour estimate must call Calculator with 40 and 3 and return S$120 as a non-binding estimate citing PRICE-01. "
            "The unsupported-discount, injection, sensitive-data, and booking cases must not trigger a tool or external action. After the controlled-demo containment test, the final workflow and sanitized export must show active=false and Chat Trigger public=false. The deployment record must contain a publish or hold decision, owner, monitoring checks, tested Unpublish path, and rollback target."
        ),
        checkpoint="Retain the complete C690-agent-starter-pack and the credential-free v1.1 export. Reuse the stable test set whenever the model, instructions, source, memory, tool, or workflow version changes.",
        troubleshooting=[
            ("Calculator runs with a rate the user supplied", "Require every price input to match an approved FAQ section before the tool call; otherwise stop for missing evidence."),
            ("The agent says the room is booked", "Strengthen the non-goal and Action status rules: it can estimate only; availability and booking remain with staff."),
            ("The public test URL works after Unpublish", "Confirm you unpublished the correct workflow and retest from a private browser window; record the actual containment result. Then turn Make Chat Publicly Available off and save."),
        ],
        challenge="Add one malformed numeric input and one calculator failure case, then specify the exact safe user message and human handoff evidence for each.",
        reflection="What evidence would justify adding a real booking-request tool, and which approval and rollback controls would need to exist first?",
    ),
]
