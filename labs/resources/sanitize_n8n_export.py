"""Create a shareable n8n workflow JSON by removing credential references.

Usage:
    python sanitize_n8n_export.py private-export.json shareable-export.json
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any


REMOVE_KEYS = {"credentials", "webhookid", "instanceid"}
REDACT_KEYS = {
    "apikey",
    "api_key",
    "authorization",
    "bearertoken",
    "clientsecret",
    "client_secret",
    "password",
    "privatekey",
    "private_key",
    "secret",
    "token",
}
SECRET_PATTERNS = [
    re.compile(r"\bsk-[A-Za-z0-9_-]{16,}\b"),
    re.compile(r"\bBearer\s+[A-Za-z0-9._~-]{12,}\b", re.IGNORECASE),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
]


def scrub(value: Any) -> Any:
    if isinstance(value, dict):
        clean: dict[str, Any] = {}
        for key, item in value.items():
            lowered = key.lower().replace("-", "").replace(" ", "")
            if lowered in REMOVE_KEYS:
                continue
            if lowered in REDACT_KEYS:
                clean[key] = "<REMOVED>"
            else:
                clean[key] = scrub(item)
        return clean
    if isinstance(value, list):
        return [scrub(item) for item in value]
    return value


def strings(value: Any):
    if isinstance(value, dict):
        for item in value.values():
            yield from strings(item)
    elif isinstance(value, list):
        for item in value:
            yield from strings(item)
    elif isinstance(value, str):
        yield value


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: python sanitize_n8n_export.py <private-input.json> <shareable-output.json>")
        return 2

    source = Path(sys.argv[1])
    target = Path(sys.argv[2])
    data = json.loads(source.read_text(encoding="utf-8"))
    clean = scrub(data)

    if not isinstance(clean, dict) or not isinstance(clean.get("nodes"), list):
        print("HOLD: input is not a recognisable n8n workflow export")
        return 1

    # A shareable lab checkpoint must never remain live or retain the Chat
    # Trigger's public-demo setting after the containment exercise.
    clean["active"] = False
    public_settings_reset = 0
    for node in clean["nodes"]:
        if not isinstance(node, dict):
            continue
        if node.get("type") == "@n8n/n8n-nodes-langchain.chatTrigger":
            parameters = node.setdefault("parameters", {})
            if isinstance(parameters, dict):
                parameters["public"] = False
                public_settings_reset += 1

    hits = []
    for text in strings(clean):
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                hits.append(pattern.pattern)
    if hits:
        print("HOLD: secret-like value remains after sanitization")
        return 1

    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(clean, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(
        f"SANITIZED OK: {target} ({len(clean['nodes'])} nodes; "
        f"credential references removed; active=false; "
        f"{public_settings_reset} Chat Trigger public setting(s)=false)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
