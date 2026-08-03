"""Single source of truth for AI Agents for Beginners (C690)."""

# ------------------------------------------------------------------ metadata
TITLE = "AI Agents for Beginners (C690)"
SHORT_TITLE = "AI Agents for Beginners (C690)"
COURSE_CODE = "C690"
VERSION = "v1.0"
VERSION_DATE = "3 August 2026"
ORG = "Tertiary Infotech Academy Pte Ltd"
UEN = "UEN: 201200696W"
TRAINER = "Course Trainer"
TRAINER_CERT = "Applied AI and no-code automation practitioner"
TRAINER_DELIVERS = "AI agents, no-code workflow automation, knowledge grounding, and responsible deployment"
DAYS = 1
MODE = "Instructor-led, concept-first learning with connected hands-on labs"

# The advertised 7.5 instructional hours are delivered within an 8-hour
# scheduled day. Two 15-minute tea breaks are included; lunch is excluded.
DAY_MINUTES = 480
INSTRUCTIONAL_HOURS = 7.5
CLOCK_HOURS = 8
DAILY_TIMING = "9:00 am - 6:00 pm (1-hour lunch; two 15-minute tea breaks)"
DARK_THEME = False

REJOIN_PATH = [
    ("Before Lab 2", "Copy 01-use-case-and-agent-canvas-starter.md, then use the supplied BrightDesk brief and FAQ to reconstruct the outcome, success evidence, agent boundary, tools, risks, and human owner."),
    ("Before Lab 3", "Copy brightdesk-gates-baseline.md to 02-agent-instructions-and-tests.md, review it against the Lab 1 canvas or sources, then run baseline cases B01, B02, S01, and S02."),
    ("Before Lab 4", "Import the Lab 3 starter, insert labs/resources/brightdesk-gates-baseline.md and the complete synthetic FAQ, select a trainer-approved model credential, confirm five-turn memory, and pass B01, B02, S01, and S02. Duplicate that verified v1.0 workflow, add Calculator, and then run the final ten-case regression."),
]

ICE_BREAKER = [
    "Your name and one repetitive work task you would like an assistant to help with.",
    "One decision or action you would always keep under human control.",
    "One question you have about the difference between a chatbot and an AI agent.",
]

# ------------------------------------------------------------------ outcomes
LEARNING_OUTCOMES = [
    "LO1: Explain how AI agents differ from chatbots and fixed workflows, including the roles of models, prompts, tools, memory, observations, and stop conditions.",
    "LO2: Compare conversational, task-based, and multi-agent patterns and select an appropriate no-code platform and bounded use case.",
    "LO3: Design an agent with a clear goal, instructions, persona, evidence boundary, tool permissions, output contract, and human escalation path.",
    "LO4: Build a simple no-code AI agent in n8n and ground its answers on an approved synthetic knowledge source.",
    "LO5: Connect a low-risk tool to an agent and control when the agent may calculate, recommend, refuse, or ask for human approval.",
    "LO6: Test and prepare an agent for deployment using expected-answer checks, safety cases, logging, monitoring, rollback, and continuous improvement.",
]
LO_TITLES = [
    "Agent Foundations",
    "Patterns and Platforms",
    "Agent Design",
    "No-Code Build",
    "Tools and Control",
    "Test and Deploy",
]

# ------------------------------------------------------------------ topics
TOPICS = [
    dict(
        num=1,
        code="01",
        title="Understanding AI Agents",
        subtitle="From chatbots to agents | models, prompts, tools and memory | agent types | use cases | no-code platforms",
        concepts=[
            ("Goal-directed", "An agent works toward an explicit result instead of only producing the next reply."),
            ("Model", "The language model interprets intent, proposes steps, and chooses among allowed tools."),
            ("Instructions", "A reusable contract defines role, evidence, rules, output, and escalation behaviour."),
            ("Tools", "Tools let the agent retrieve information, calculate, update a system, or trigger a workflow."),
            ("Memory and state", "State carries only the context needed for the next decision; it is not automatically reliable truth."),
            ("Observe and adjust", "The agent reads tool results, checks progress, and decides whether to continue, retry, stop, or ask a person."),
            ("Bounded autonomy", "Permissions, limits, approval gates, and stop conditions define what the agent may do."),
            ("Evidence over confidence", "A fluent answer is not proof; important claims and actions need source evidence and verification."),
        ],
        teaching=[
            dict(
                title="From Chatbot to Goal-Directed Agent",
                kind="compare",
                kicker="TOPIC 01 - THE PRACTICAL DIFFERENCE",
                left_title="Chatbot",
                right_title="AI agent",
                left=[
                    "Responds to the current message",
                    "Usually produces text only",
                    "Relies on context supplied in the conversation",
                    "A person performs the next action",
                ],
                right=[
                    "Works toward a defined outcome",
                    "Can choose and call approved tools",
                    "Observes results and updates its next step",
                    "Stops, escalates, or completes within a boundary",
                ],
                paragraphs=[
                    "A chatbot is a conversational interface: it receives a message and returns a response. An AI agent adds goal management and an action loop. It can interpret the objective, decide which permitted tool is useful, observe the result, and continue until the goal is met or a stop condition is reached. The interface may still look like chat, but the operating model is different.",
                    "The distinction is about control, not marketing labels. A fixed sequence that always follows the same route is a workflow, even if one step uses a language model. A system becomes more agentic when the model chooses among possible steps or tools based on the situation. More autonomy is not automatically better; it increases the need for clear evidence, permissions, testing, and human oversight.",
                ],
            ),
            dict(
                title="The Agent Loop",
                kind="flow",
                kicker="TOPIC 01 - HOW AN AGENT WORKS",
                visual=["Receive goal", "Plan the next step", "Use an allowed tool", "Observe the result", "Check success or stop"],
                paragraphs=[
                    "An agent begins with a goal and the context available at that moment. It selects a next step, may call a tool, reads the observation returned by the environment, then compares progress with the success rule. The loop continues only while another step is useful and permitted. Completion, uncertainty, a policy rule, an error, or an iteration limit can end the loop.",
                    "The observation is important because it reconnects the model to reality. A booking tool may return that a room is unavailable; a knowledge tool may return no matching source; a calculator may return a value. The agent should use that evidence instead of continuing from an assumption. Good designs make the loop visible in logs and give a person a clear point to intervene.",
                ],
            ),
            dict(
                title="Six Building Blocks of a Beginner Agent",
                kind="tiles",
                kicker="TOPIC 01 - AGENT ANATOMY",
                visual=[
                    ("Goal", "The outcome, user, success signal, time horizon, and finish line."),
                    ("Model", "The reasoning and language engine, chosen for the task and operating constraints."),
                    ("Instructions", "Role, evidence rules, decision rules, output schema, and escalation path."),
                    ("Tools", "Clearly named capabilities with narrow inputs, outputs, permissions, and error behaviour."),
                    ("Memory", "Short-lived conversation context or approved persistent state needed for continuity."),
                    ("Guardrails", "Validation, privacy rules, approvals, limits, monitoring, and rollback."),
                ],
                paragraphs=[
                    "A useful agent is a system, not a prompt. The goal states what good looks like. The model interprets language and makes bounded choices. Instructions explain the role and rules. Tools connect the agent to information or actions. Memory carries selected context. Guardrails keep the whole system within acceptable risk.",
                    "Weakness in one block propagates to the others. If a tool description is vague, the model may call it for the wrong purpose. If persistent memory stores unverified statements, later answers can repeat them as fact. If the goal is simply 'be helpful', there is no measurable finish line. Design each block and its interface before increasing autonomy.",
                ],
            ),
            dict(
                title="What the Language Model Does - and Does Not Do",
                kind="compare",
                kicker="TOPIC 01 - MODEL ROLE",
                left_title="Useful model work",
                right_title="Separate system responsibility",
                left=[
                    "Interpret unstructured requests",
                    "Classify intent and propose a plan",
                    "Select among described tools",
                    "Draft and explain a result",
                ],
                right=[
                    "Authenticate the user and protect secrets",
                    "Enforce permissions and spending limits",
                    "Validate critical calculations and records",
                    "Log, monitor, approve, and reverse actions",
                ],
                paragraphs=[
                    "A language model predicts and generates language from patterns. It is strong at interpreting ambiguous requests, organising context, drafting, and choosing among well-described options. It can still invent facts, overlook a constraint, or choose an unnecessary tool. Fluency should never be treated as a control mechanism.",
                    "Deterministic controls belong outside the model. Authentication, access checks, required fields, numeric limits, approval gates, and audit logs should be enforced by the surrounding workflow. The model can recommend an action, but the system decides whether that action is permitted. This separation makes failures easier to diagnose and contain.",
                ],
            ),
            dict(
                title="Workflow or Agent? Choose the Smallest Useful Pattern",
                kind="compare",
                kicker="TOPIC 01 - ARCHITECTURE CHOICE",
                left_title="Use a fixed workflow when",
                right_title="Use an agent when",
                left=[
                    "The path and rules are known in advance",
                    "The same inputs should always take the same route",
                    "A mistake would be costly or difficult to reverse",
                    "Speed, predictability, and auditability dominate",
                ],
                right=[
                    "Requests are varied or unstructured",
                    "The next step depends on new observations",
                    "Several reasonable tools or routes may work",
                    "A person can review important exceptions",
                ],
                paragraphs=[
                    "A fixed workflow is often the right first solution. It is easier to test because the route is known. Agentic choice adds value when the input is open-ended and the next step cannot be fully predicted, such as deciding whether a customer question needs a knowledge lookup, a calculation, or a human handoff.",
                    "Start with the simplest pattern that meets the need. Add retrieval before adding many tools; add one bounded tool before granting write access; add multi-agent coordination only when distinct roles genuinely improve the outcome. Every new decision point increases latency, cost, failure paths, and the amount of evidence needed to trust the system.",
                ],
            ),
            dict(
                title="Tools Turn Language into Observable Work",
                kind="flow",
                kicker="TOPIC 01 - TOOL CALL LIFECYCLE",
                visual=["User request", "Agent selects tool", "System validates inputs", "Tool returns evidence", "Agent explains or escalates"],
                paragraphs=[
                    "A tool is a defined interface to a capability such as search, calculation, a database lookup, a calendar, or an automation. Its name and description tell the model when it should be used; its input schema constrains the request; its output gives the agent an observation. Narrow, well-documented tools are easier for both the model and the operator to understand.",
                    "Tool use should be separated by risk. Reading public or synthetic information is usually low risk. Drafting a ticket or calculating a price is limited and reversible. Sending a message, changing a record, making a booking, or spending money is higher risk and usually needs authentication, validation, and approval. A tool error must return a clear failure instead of pretending the action succeeded.",
                ],
            ),
            dict(
                title="Memory Is Selected State, Not Automatic Truth",
                kind="tiles",
                kicker="TOPIC 01 - MEMORY AND CONTEXT",
                visual=[
                    ("Conversation memory", "Recent turns that help the agent understand references and maintain continuity."),
                    ("Task state", "Confirmed fields, progress, tool results, and the current checkpoint for one job."),
                    ("Long-term profile", "Approved preferences or history retained across sessions under a clear policy."),
                    ("Knowledge source", "Documents or records retrieved as evidence; this is different from memory."),
                    ("Retention rule", "What is stored, why, for how long, who can access it, and how it is removed."),
                    ("Correction path", "How a person can inspect, amend, or delete incorrect state."),
                ],
                paragraphs=[
                    "Memory helps an agent maintain continuity, but stored content can be incomplete, outdated, or wrong. Conversation memory may preserve a user's earlier preference. Task state records what has been completed. Long-term memory may persist approved information across sessions. A knowledge source is different: it is retrieved evidence used to answer a question.",
                    "Store the minimum state required for the job. Never place passwords, API keys, or unnecessary personal data in prompts or memory. Give important records a source, timestamp, owner, and correction path. When a value must be authoritative - such as a price, policy, or entitlement - retrieve it from the system of record rather than relying on remembered text.",
                ],
            ),
            dict(
                title="Three Common Agent Patterns",
                kind="tiles",
                kicker="TOPIC 01 - TYPES OF AI AGENTS",
                visual=[
                    ("Conversational agent", "Maintains a dialogue, retrieves information, and routes exceptions while a person remains in the interaction."),
                    ("Task-based agent", "Works toward a defined artifact or operational result using a small set of tools and stop conditions."),
                    ("Multi-agent system", "Coordinates specialised agents through an orchestrator; useful only when roles and handoffs are genuinely distinct."),
                    ("Hybrid workflow", "Uses deterministic routing for known rules and an agent only where interpretation or flexible planning adds value."),
                ],
                paragraphs=[
                    "Conversational agents are natural for service, guidance, and intake. Task-based agents focus on an outcome such as drafting a report or reconciling records. Multi-agent systems divide work among specialised roles, but introduce coordination, duplicated effort, and harder evaluation. A hybrid workflow often provides the best beginner architecture.",
                    "Choose a pattern from the work, not from novelty. If the goal, available evidence, and allowed actions fit inside one agent, keep one agent. If a process contains a known decision table, keep that portion deterministic. Multi-agent designs are justified when separate contexts, permissions, or expertise materially improve the result and the handoff can be verified.",
                ],
            ),
            dict(
                title="Use Cases Across Service, Marketing, and Operations",
                kind="tiles",
                kicker="TOPIC 01 - WHERE AGENTS HELP",
                visual=[
                    ("Customer service", "Answer from approved policies, classify intent, draft responses, and escalate sensitive or unsupported cases."),
                    ("Marketing", "Research approved sources, create variants, organise a content plan, and route material for brand review."),
                    ("Operations", "Summarise requests, check records, calculate routine values, prepare drafts, and coordinate handoffs."),
                    ("Knowledge support", "Retrieve relevant passages, cite the source, explain uncertainty, and record unanswered questions."),
                    ("Personal productivity", "Turn notes into actions, prepare a meeting brief, or organise a repeatable decision checklist."),
                    ("Avoid or constrain", "High-stakes decisions, unrestricted data access, irreversible actions, and tasks without verifiable outcomes."),
                ],
                paragraphs=[
                    "Good starter use cases have clear users, bounded inputs, observable outcomes, and recoverable mistakes. They are repetitive enough to justify design effort but variable enough to benefit from language understanding. A customer support assistant grounded on a small, approved FAQ is a stronger first project than an agent with access to every company system.",
                    "Avoid using an agent where a wrong answer or action could seriously harm a person, create a legal commitment, expose confidential data, or spend money without meaningful human control. If the outcome cannot be checked, the system cannot be improved. Write the success evidence and failure response before selecting a platform.",
                ],
            ),
            dict(
                title="No-Code Platform Landscape",
                kind="tiles",
                kicker="TOPIC 01 - PLATFORM OVERVIEW",
                visual=[
                    ("Chat-based builders", "Fast instruction, persona, file-grounding, and conversation testing for simple assistants."),
                    ("Workflow builders", "Visual triggers, agent nodes, tools, data movement, approvals, logs, retries, and integrations."),
                    ("Enterprise studios", "Managed identity, connectors, governance, environments, and organisational deployment controls."),
                    ("Agent frameworks", "Code-level control for teams that need custom tools, state, evaluation, and deployment architecture."),
                    ("Selection criteria", "Required tools, data location, authentication, cost, observability, export, and operator skills."),
                    ("Course platform", "n8n provides a visual canvas for the model, instructions, memory, tools, test chat, and execution history."),
                ],
                paragraphs=[
                    "No-code does not mean no design. A visual builder can make the flow easier to see, but the same questions remain: what is the goal, which source is authoritative, what may the agent change, how is success checked, and who responds when the system is uncertain? Platform choice should follow these requirements.",
                    "This course uses n8n because its canvas exposes the main parts of an agent and its workflow. Learners can connect a chat trigger, AI Agent node, model, memory, and tool without programming. The design concepts transfer to other platforms; menus and node names change, but goals, evidence, permissions, tests, and human control remain.",
                ],
            ),
        ],
    ),
    dict(
        num=2,
        code="02",
        title="Building Your First AI Agents",
        subtitle="Goals, instructions and personas | no-code build | document grounding | tools | testing, deployment and best practices",
        concepts=[
            ("Design the outcome", "Name the user, job, success evidence, non-goals, and human owner before opening a builder."),
            ("Write an instruction contract", "Specify goal, grounding, actions, tests, escalation, and state in reusable language."),
            ("Ground important claims", "Supply approved sources and require the agent to cite, qualify, or refuse when evidence is missing."),
            ("Grant least authority", "Start read-only, add one low-risk tool, and require approval for consequential actions."),
            ("Test behaviour", "Use normal, boundary, missing-evidence, adversarial, and tool-failure cases with expected outcomes."),
            ("Deploy gradually", "Move from sandbox to internal pilot to controlled use only after evidence supports the next level."),
            ("Monitor outcomes", "Retain inputs, tool calls, outputs, errors, corrections, latency, and user feedback appropriate to the risk."),
            ("Keep a rollback path", "Know how to pause the workflow, revoke credentials, restore state, and return work to a person."),
        ],
        teaching=[
            dict(
                title="Begin with an Agent Canvas",
                kind="flow",
                kicker="TOPIC 02 - DESIGN BEFORE BUILD",
                visual=["User and job", "Outcome and evidence", "Inputs and sources", "Tools and authority", "Risks and human owner"],
                paragraphs=[
                    "An agent canvas turns an idea into a testable system. Identify the person being helped and the job they need done. Describe the result in observable terms. List the approved inputs and sources. Define the smallest set of tools. Mark actions that are read-only, reversible, approval-controlled, or prohibited.",
                    "Also write non-goals. A BrightDesk support agent may answer from a synthetic FAQ and calculate an estimate, but it does not confirm availability, take payment, make a booking, or collect sensitive personal data. Non-goals prevent a friendly persona from implying authority the system does not have.",
                ],
            ),
            dict(
                title="Goal, Instructions, and Persona Have Different Jobs",
                kind="tiles",
                kicker="TOPIC 02 - PROMPT ARCHITECTURE",
                visual=[
                    ("Goal", "Defines the observable result and what completion means."),
                    ("Instructions", "Define evidence, decision rules, tools, output, refusals, and escalation."),
                    ("Persona", "Shapes tone, vocabulary, and interaction style without changing permissions."),
                    ("Context", "Supplies the approved facts and situation for the current task."),
                    ("Examples", "Show difficult cases and the desired format or boundary behaviour."),
                    ("User message", "Expresses the current need; it does not override higher-priority rules."),
                ],
                paragraphs=[
                    "The goal says what the agent is trying to achieve. Instructions describe how it should behave. A persona affects the experience - for example, calm, concise, and beginner-friendly - but must never grant extra authority. Context and examples provide the evidence and patterns needed for the current request.",
                    "Keep these layers separate so they can be changed and tested independently. A tone change should not alter the tool permission matrix. A new knowledge source should not silently change the success rule. When a user asks the agent to ignore its rules, the agent should preserve its instruction hierarchy and either continue safely or escalate.",
                ],
            ),
            dict(
                title="The GATES Instruction Contract",
                kind="tiles",
                kicker="TOPIC 02 - REUSABLE DESIGN FRAMEWORK",
                visual=[
                    ("Goal", "Who is helped, what result is required, and what counts as complete."),
                    ("Authority", "Allowed tools and actions, approval gates, prohibited actions, and limits."),
                    ("Truth", "Authoritative sources, citation rules, uncertainty language, and missing-evidence behaviour."),
                    ("Evaluation", "Expected output, checks, test cases, quality thresholds, and failure signals."),
                    ("State", "What context is retained, for how long, and how it can be corrected or removed."),
                    ("Escalation", "When to stop, what to tell the user, what evidence to pass, and who owns the next step."),
                ],
                paragraphs=[
                    "GATES is a beginner-friendly checklist for complete agent instructions: Goal, Authority, Truth, Evaluation, State, and Escalation. It prevents the common mistake of writing only a persona and a vague task. Each section can be reviewed by the person who owns that risk or decision.",
                    "A strong contract is specific enough to test. 'Use the knowledge base' becomes 'Use only the named BrightDesk FAQ for prices, hours, and policies; cite the section ID; if no source supports the answer, say what is missing and offer a human handoff.' The second version creates observable behaviour and a clear failure condition.",
                ],
            ),
            dict(
                title="Grounding: Put Approved Evidence into the Answer Path",
                kind="flow",
                kicker="TOPIC 02 - DOCUMENTS AND KNOWLEDGE",
                visual=["User question", "Retrieve relevant source", "Supply passage to model", "Generate with citation", "Check support or refuse"],
                paragraphs=[
                    "Grounding connects the agent's answer to approved evidence. For a small beginner project, the knowledge text can be placed directly in the system context. Larger collections usually use retrieval-augmented generation: documents are split into chunks, represented for search, relevant passages are retrieved, and those passages are supplied to the model for the current question.",
                    "Retrieval does not guarantee correctness. The wrong passage may be retrieved, the source may be outdated, or the model may overstate what the passage says. Keep source identifiers, require citations, test questions that are both inside and outside the source, and define the response when evidence is missing. Knowledge content is data, not an instruction channel; embedded commands in a document must not override the agent's rules.",
                ],
            ),
            dict(
                title="Tools Need Descriptions, Schemas, and Permission Boundaries",
                kind="tiles",
                kicker="TOPIC 02 - CONNECTING ACTIONS",
                visual=[
                    ("Clear purpose", "A tool name and description explain exactly when it should and should not be used."),
                    ("Narrow input", "Required fields, types, ranges, and accepted values reduce ambiguous calls."),
                    ("Structured output", "Success, result, source, error, and next action are explicit."),
                    ("Least privilege", "Credentials and operations expose only what the task requires."),
                    ("Approval", "Consequential calls pause until an authorised person confirms the evidence."),
                    ("Failure behaviour", "Timeouts, empty results, duplicates, and validation errors return a safe, visible state."),
                ],
                paragraphs=[
                    "A model sees a tool through its interface. A vague name such as 'operations' forces the model to guess. A name such as 'calculate_workspace_estimate' with numeric inputs and a non-binding output is easier to use correctly. Validate required values before execution and return a structured error when the tool cannot complete the request.",
                    "Tool authority belongs to the workflow and credential, not to the persona. Begin with read-only or synthetic tools. Require approval before communications, record changes, bookings, purchases, or deletion. Idempotency and duplicate checks matter because an agent or user may retry. The safest tool is often a draft-producing tool whose output is reviewed before any external action.",
                ],
            ),
            dict(
                title="Memory Design for a Short Service Conversation",
                kind="flow",
                kicker="TOPIC 02 - STATE WITH PURPOSE",
                visual=["Keep recent turn", "Extract confirmed fact", "Discard unnecessary detail", "Use in next response", "Expire at session end"],
                paragraphs=[
                    "Short-term memory makes a conversation coherent. If a user says they need a room for three hours, the next question can refer to 'that booking'. The agent should still distinguish a confirmed fact from an assumption and should not treat memory as proof of availability or payment.",
                    "For the course agent, keep only recent synthetic conversation context. Do not ask for identity documents, payment details, passwords, or real customer records. Production designs need explicit retention, access, correction, and deletion rules. When a session ends, unnecessary state should expire rather than becoming an unreviewed profile.",
                ],
            ),
            dict(
                title="A No-Code Agent on the n8n Canvas",
                kind="flow",
                kicker="TOPIC 02 - BUILDING BLOCKS ON SCREEN",
                visual=["Chat Trigger", "AI Agent", "Chat Model", "Simple Memory", "Calculator Tool"],
                paragraphs=[
                    "In n8n, the Chat Trigger receives the message. The AI Agent contains the reusable instructions and coordinates the response. A chat model supplies language and reasoning. Simple Memory carries recent turns. A Calculator tool gives the agent one observable, low-risk capability. Execution history shows which nodes ran and what they returned.",
                    "The connected nodes make responsibility visible. The trigger is an interface, not the intelligence. The model cannot act unless a tool is attached. Memory is optional and separate. The workflow can remain in test mode while behaviour is refined. This modular view helps a beginner change one component and rerun the same test set.",
                ],
            ),
            dict(
                title="Worked Example: BrightDesk Workspace Assistant",
                kind="flow",
                kicker="TOPIC 02 - FROM QUESTION TO EVIDENCE",
                visual=["Ask: three-hour room estimate", "Retrieve price rule", "Call calculator", "Label estimate as non-binding", "Offer staff handoff for booking"],
                paragraphs=[
                    "A user asks, 'What is the estimate for a meeting room for three hours?' The agent finds the approved hourly rate and minimum duration in the BrightDesk knowledge block. It calls the calculator for 40 multiplied by 3, reports S$120 as a non-binding estimate, cites the price section, and explains that availability and booking require staff confirmation.",
                    "Each component has a job. The source supplies the rate. The calculator supplies the arithmetic result. The instruction contract supplies the wording and authority boundary. The model connects them into a useful response. If the user asks for a discount not in the FAQ, the correct outcome is not a guess; it is a clear statement that the source does not support the request and a human handoff option.",
                ],
            ),
            dict(
                title="Test Behaviour, Not Just Happy Paths",
                kind="tiles",
                kicker="TOPIC 02 - EVALUATION SET",
                visual=[
                    ("Normal", "A supported question returns the correct source-backed answer."),
                    ("Boundary", "A near-limit case follows the exact rule and unit."),
                    ("Missing evidence", "The agent states the gap instead of inventing an answer."),
                    ("Adversarial", "A request to ignore rules or reveal secrets does not change authority."),
                    ("Tool failure", "The agent reports the failure and offers a safe next step."),
                    ("Human review", "A consequential or sensitive request stops with the required evidence for handoff."),
                ],
                paragraphs=[
                    "A demonstration proves only that one example worked once. A test set defines expected behaviour across normal, edge, missing-evidence, adversarial, and failure cases. Record the input, expected evidence, expected action, observed result, correction, and rerun result. Evaluate the final outcome and the tool path that produced it.",
                    "Keep a stable regression set. When instructions, knowledge, model, or tools change, rerun the same cases. A correction that improves one response can harm another. For important workflows, combine deterministic checks, model-based review, and human judgement appropriate to the risk rather than relying on a single score.",
                ],
            ),
            dict(
                title="Security, Privacy, and Prompt Injection",
                kind="tiles",
                kicker="TOPIC 02 - DEFENCE IN DEPTH",
                visual=[
                    ("Treat content as data", "Documents, websites, and messages may contain instructions that must not override system rules."),
                    ("Protect credentials", "Secrets belong in the platform credential store, never in prompts, files, screenshots, or chat."),
                    ("Minimise access", "Restrict data fields, tool operations, environments, and network destinations."),
                    ("Validate actions", "Check identity, required fields, ranges, targets, and approval before execution."),
                    ("Monitor", "Log tool calls, failures, refusals, corrections, and unusual usage within an appropriate retention policy."),
                    ("Contain", "Rate limits, timeouts, iteration limits, kill switches, and rollback reduce the impact of a failure."),
                ],
                paragraphs=[
                    "Prompt injection is an attempt to place conflicting instructions inside user input or retrieved content. The system should treat untrusted content as data, preserve the instruction hierarchy, restrict tools, and validate every consequential action. No single prompt can guarantee protection; layers of technical and operational controls are required.",
                    "Privacy starts with not collecting what the task does not need. Use synthetic data in learning and testing. Store credentials only in the platform's protected credential manager. Review logs for sensitive content before retention. Give operators a way to pause the workflow, revoke access, remove state, and return the task to a manual process.",
                ],
            ),
            dict(
                title="Deploy in Stages and Keep a Rollback Path",
                kind="flow",
                kicker="TOPIC 02 - OPERATING MODEL",
                visual=["Sandbox", "Internal test", "Recommendation mode", "Approved action", "Monitored expansion"],
                paragraphs=[
                    "Deployment is a controlled increase in real-world exposure. Start in a sandbox with synthetic content. Move to an internal test with known users and a stable test set. Use recommendation or draft mode before allowing an action. Add approval for consequential steps. Expand scope only when outcome evidence and incident handling support it.",
                    "Before publication, name the owner, success metrics, error thresholds, monitoring rhythm, support channel, and rollback action. A rollback may mean unpublishing the workflow, revoking a credential, disabling a tool, restoring a previous version, or directing all requests to staff. Continued monitoring is part of the agent, not a separate afterthought.",
                ],
            ),
        ],
    ),
]

DAY_THEMES = {1: "Understand, design, build, test, and publish a bounded beginner AI agent"}


def SCHEDULE(lab_titles):
    return {
        1: (DAY_THEMES[1], [
            ("9:00", "9:20", 20, "admin", "Welcome, introductions, course outcomes, learning approach, and safe lab setup"),
            ("9:20", "10:10", 50, "topic", "Topic 1 - Understanding AI Agents: chatbots, workflows, agents, models, prompts, tools, and memory"),
            ("10:10", "10:25", 15, "break", "Tea break"),
            ("10:25", "11:10", 45, "topic", "Topic 1 - Agent patterns, use cases, platform choices, and bounded autonomy"),
            ("11:10", "12:00", 50, "lab", "Hands-on: " + lab_titles([1])),
            ("12:00", "13:00", 60, "topic", "Topic 2 - Goals, GATES instructions, personas, evidence boundaries, and human ownership"),
            ("13:00", "14:00", 60, "lunch", "Lunch break"),
            ("14:00", "14:50", 50, "lab", "Hands-on: " + lab_titles([2])),
            ("14:50", "15:15", 25, "topic", "Topic 2 - No-code architecture, document grounding, memory, tools, and permissions"),
            ("15:15", "15:30", 15, "break", "Tea break"),
            ("15:30", "16:30", 60, "lab", "Hands-on: " + lab_titles([3])),
            ("16:30", "16:55", 25, "topic", "Topic 2 - Testing, security, staged deployment, monitoring, and rollback"),
            ("16:55", "17:55", 60, "lab", "Hands-on: " + lab_titles([4])),
            ("17:55", "18:00", 5, "recap", "Learning-outcome recap and next steps"),
        ]),
    }


COURSE_OVERVIEW = dict(
    section_title="AI Agent Fundamentals",
    concepts_title="The Shift from Answers to Outcomes",
    concepts=[
        ("Chat", "Generate a response for the current message."),
        ("Workflow", "Follow a known path through defined steps and rules."),
        ("Agent", "Choose the next permitted step from the goal and observation."),
        ("Human control", "Set authority, review evidence, approve impact, and stop the system."),
    ],
    framework_title="The GATES Design Check",
    framework=[
        ("Goal", "Observable result and completion rule."),
        ("Authority", "Tools, permissions, limits, and approvals."),
        ("Truth", "Sources, citations, uncertainty, and refusal."),
        ("Evaluation", "Expected behaviour and stable test cases."),
        ("State", "Context, retention, correction, and deletion."),
        ("Escalation", "Stop conditions, handoff evidence, and owner."),
    ],
    statement=dict(
        headline="Autonomy should grow only as evidence and control grow.",
        body="Begin with one bounded goal, one approved knowledge source, one low-risk tool, and a visible human handoff.",
        kicker="COURSE PRINCIPLE",
    ),
    pillars_title="What You Will Build",
    pillars=[
        ("Agent design pack", ["Use-case canvas", "GATES instructions", "Test expectations"]),
        ("No-code agent", ["n8n chat interface", "approved model", "short-term memory", "grounded answers"]),
        ("Controlled pilot", ["calculator tool", "safety tests", "publish decision", "rollback record"]),
    ],
    arc_title="The Connected Learning Arc",
    arc=[
        "Lab 1 selects a bounded use case and defines success, evidence, tools, risks, and ownership.",
        "Lab 2 turns that design into testable instructions, a persona, an output contract, and failure behaviour.",
        "Lab 3 implements the same design on the n8n canvas and grounds it on the BrightDesk FAQ.",
        "Lab 4 adds one low-risk tool, runs the stable test set, and records a publish or hold decision.",
    ],
)

LAB_SHOTS = {}

LG_INTRO = (
    "AI agents extend generative AI from producing a reply to pursuing a goal through a controlled loop of planning, tool use, observation, and adjustment. "
    "This learner guide explains the design principles before the practical steps so you can transfer the method to different platforms and workplace tasks."
)
LG_INTRO2 = (
    "Across four connected labs, you will create one BrightDesk Workspace support agent. You will define its boundary, write its instructions, build it in n8n, ground it on a synthetic FAQ, attach a calculator tool, and test whether it should remain in sandbox or be published as a controlled demonstration."
)
LG_SETUP = dict(
    needs=[
        "A Windows or Mac laptop with a modern web browser and access to the course repository.",
        "A trainer-provided n8n workspace or your own n8n Cloud trial; the current interface may differ slightly by version.",
        "A trainer-approved model credential already stored in n8n, or your own authorised API credential stored only in n8n Credentials.",
        "A text or Markdown editor for the C690-agent-starter-pack files.",
        "Only the supplied synthetic BrightDesk knowledge and test data; no real customer, employee, payment, or confidential information.",
    ],
    verify_text="Confirm that you can open n8n, create or import a workflow, open the course resources, and create the connected output folder without placing a secret in a prompt or file.",
    verify_code="Open: labs/resources/brightdesk-workspace-faq.md\nOpen: labs/resources/brightdesk-agent-test-cases.csv\nCreate folder: C690-agent-starter-pack",
    conventions=[
        "Replace placeholders such as <MODEL_CREDENTIAL> only inside the n8n credential selector; never paste a key into a node prompt or course file.",
        "Use the exact output filenames shown so later labs can reuse earlier checkpoints.",
        "Treat every generated response as a draft until its source, calculation, tool path, and authority boundary are checked.",
        "Keep the workflow in test or unpublished mode until Lab 4 records an explicit publish decision.",
        "Use only synthetic course data during learning and verification.",
    ],
)
LAB_NOTE = "Use the synthetic BrightDesk scenario and placeholder credentials only. Do not collect real personal data, expose a secret, confirm a booking, take payment, or send an external message from the course workflow."

LG_WRAPUP = dict(
    title="Wrap-Up - From Demonstration to Responsible Pilot",
    intro="Your final starter pack connects a business outcome, evidence boundary, instruction contract, no-code implementation, tool permission, test results, and deployment decision. The trace between these artifacts is what makes the agent reviewable.",
    sections=[
        dict(
            title="Before adapting the agent at work",
            bullets=[
                "Replace the synthetic FAQ only with an approved, current source owned by the business process owner.",
                "Reconfirm the user group, authentication need, permitted tools, approval gates, privacy rules, and data-retention policy.",
                "Create a representative test set with expected outcomes and assign an owner for errors, incidents, and source updates.",
                "Pilot in recommendation or draft mode before granting any external write action.",
            ],
        ),
        dict(
            title="Evidence to retain",
            bullets=[
                "Agent version, source version, instruction version, model choice, tool definitions, and credential scope.",
                "Test inputs, expected evidence and action, observed result, corrections, and regression rerun.",
                "Publish decision, owner, monitoring thresholds, pause method, rollback action, and review date.",
            ],
        ),
    ],
)

LG_NEXT_STEPS = [
    "Replace the calculator with one read-only workplace lookup tool and document its schema, error states, and permission boundary.",
    "Expand the knowledge source using a retrieval workflow while retaining source IDs and missing-evidence tests.",
    "Add a human approval step before any message, booking, record change, or other consequential action.",
    "Rerun the stable test set whenever the model, instructions, source content, tools, or workflow version changes.",
    "Review n8n and model-provider documentation before using current platform features in production.",
]

LG_GLOSSARY = [
    ("Agent", "A system in which a model directs steps or tool use toward a goal within defined boundaries."),
    ("Agentic loop", "The repeated cycle of selecting an action, observing the result, and deciding what to do next."),
    ("Approval gate", "A required human decision before a consequential action can proceed."),
    ("Chatbot", "A conversational system that responds to messages; it may or may not include agentic tool choice."),
    ("Context", "Information supplied for the current task or conversation."),
    ("Embedding", "A numeric representation used to compare the meaning of text for retrieval."),
    ("Evaluation", "A repeatable method for comparing observed behaviour with expected outcomes."),
    ("Grounding", "Supplying approved evidence so an answer can be supported and checked."),
    ("Guardrail", "A rule, validation, permission, approval, limit, or operational control that constrains behaviour."),
    ("Hallucination", "Generated content that is unsupported, incorrect, or invented while sounding plausible."),
    ("Human handoff", "A controlled stop that transfers the request and relevant evidence to a named person or team."),
    ("Instruction hierarchy", "The priority order among system rules, application instructions, approved context, and user requests."),
    ("Memory", "Selected conversational or task state retained to support future decisions."),
    ("Model", "The AI component that interprets language and generates or selects responses and actions."),
    ("Multi-agent system", "A design in which multiple specialised agents coordinate through defined roles and handoffs."),
    ("No-code platform", "A visual environment for assembling triggers, models, tools, data, and controls with little or no programming."),
    ("Prompt injection", "Instructions placed in user or retrieved content that attempt to override trusted rules or misuse tools."),
    ("RAG", "Retrieval-augmented generation: retrieving relevant source passages and supplying them to a model for the current task."),
    ("Rollback", "A planned action that returns the workflow to a known safer state after a problem."),
    ("State", "The confirmed information and progress the system carries between steps or turns."),
    ("Stop condition", "A rule that ends or pauses the loop because the goal is complete, evidence is missing, risk is high, or a limit is reached."),
    ("Tool", "A defined interface that lets an agent retrieve information, calculate, or request an external operation."),
    ("Workflow", "A predefined sequence of steps and rules; some steps may use a model without giving it control of the route."),
]

NEXT_STEPS = dict(
    title="Build the Next Safe Increment",
    items=[
        "Adapt the canvas to one approved, low-risk workplace task with a measurable outcome.",
        "Replace synthetic knowledge only after a source owner confirms accuracy, access, and review dates.",
        "Add one narrowly described tool, then extend the regression set before granting more authority.",
        "Pilot with named users, visible monitoring, a manual fallback, and a tested pause or rollback method.",
    ],
)

THANK_YOU = dict(
    body="You can now explain, design, build, ground, tool-enable, test, and prepare a simple AI agent for controlled use.",
    kicker="C690 - START SMALL, VERIFY EVIDENCE, KEEP PEOPLE IN CONTROL",
)

VERSION_HISTORY = [
    ("1.0", VERSION_DATE, "Initial aligned release: 2 topics, 4 connected labs, and 1 day / 7.5 instructional hours.", "Tertiary Infotech Academy Courseware Team"),
]
