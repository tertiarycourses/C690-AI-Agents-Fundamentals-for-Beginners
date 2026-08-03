"""Static release checks for the two credential-free C690 n8n starters.

This validates the shareable JSON structure and the course's safety/alignment
contract. It does not call a model or replace the live trainer preflight.
"""

from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
LAB3 = HERE / "C690-Lab3-BrightDesk-Knowledge-Agent.json"
LAB4 = HERE / "C690-Lab4-BrightDesk-Tool-Agent.json"
EXPECTED_STATUSES = (
    "ANSWER | NON_BINDING_ESTIMATE | CLARIFY_MINIMUM_OR_HANDOFF | "
    "SOURCE_GAP_AND_HANDOFF | STOP_AND_HANDOFF | REFUSE_AND_HANDOFF | "
    "PRIVACY_STOP_AND_HANDOFF | REPORT_FAILURE_AND_HANDOFF"
)
COMMON_NODE_TYPES = {
    "Chat Trigger": "@n8n/n8n-nodes-langchain.chatTrigger",
    "AI Agent": "@n8n/n8n-nodes-langchain.agent",
    "OpenAI Chat Model": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
    "Simple Memory": "@n8n/n8n-nodes-langchain.memoryBufferWindow",
}


def walk(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


def load(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(data, dict) and isinstance(data.get("nodes"), list)
    assert data.get("active") is False, f"{path.name}: active must be false"
    assert not any("credentials" in obj for obj in walk(data)), f"{path.name}: credential object found"

    nodes = {node["name"]: node for node in data["nodes"]}
    for name, node_type in COMMON_NODE_TYPES.items():
        assert nodes.get(name, {}).get("type") == node_type, f"{path.name}: missing or wrong {name}"
    assert nodes["Chat Trigger"]["parameters"].get("public") is False
    assert nodes["Simple Memory"]["parameters"].get("contextWindowLength") == 5
    prompt = nodes["AI Agent"]["parameters"]["options"]["systemMessage"]
    assert EXPECTED_STATUSES in prompt, f"{path.name}: action-status contract drift"
    assert "<KNOWLEDGE source='brightdesk-workspace-faq.md'>" in prompt

    connections = data.get("connections", {})
    assert connections.get("Chat Trigger", {}).get("main")
    assert connections.get("OpenAI Chat Model", {}).get("ai_languageModel")
    assert connections.get("Simple Memory", {}).get("ai_memory")
    return data


def main() -> int:
    lab3 = load(LAB3)
    lab4 = load(LAB4)
    lab3_nodes = {node["name"]: node for node in lab3["nodes"]}
    lab4_nodes = {node["name"]: node for node in lab4["nodes"]}
    assert set(lab3_nodes) == set(COMMON_NODE_TYPES)
    assert set(lab4_nodes) == set(COMMON_NODE_TYPES) | {"Calculator"}
    assert lab4_nodes["Calculator"]["type"] == "@n8n/n8n-nodes-langchain.toolCalculator"
    assert lab4["connections"].get("Calculator", {}).get("ai_tool")
    for name in COMMON_NODE_TYPES:
        assert lab3_nodes[name]["type"] == lab4_nodes[name]["type"]
        assert lab3_nodes[name]["typeVersion"] == lab4_nodes[name]["typeVersion"]
    print("STARTER QA PASS: 2 workflows; structures, connections, safety flags, and action-status contract aligned")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
