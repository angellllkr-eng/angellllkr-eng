from __future__ import annotations

import re
from pathlib import Path
from typing import Any

import yaml


LIMITS_PATH = Path(__file__).resolve().parents[1] / ".copilot" / "copilot_limits.yaml"

KEYWORDS: dict[str, tuple[str, ...]] = {
    "exec_code": (
        r"\brun (?:this |the )?(?:code|script|python|powershell|bash)\b",
        r"\bexecute (?:code|a script|the script|python|powershell|bash)\b",
        r"\brestart (?:the )?(?:service|server|process)\b",
    ),
    "system_access": (
        r"\b(?:read|write|delete|inspect) (?:a |the )?(?:local )?(?:file|disk|filesystem|process)\b",
        r"\b(?:operating system|hardware|local machine)\b",
    ),
    "network_ops": (
        r"\b(?:open|close) (?:a )?(?:socket|port)\b",
        r"\b(?:firewall|vpn|network route|arbitrary api)\b",
    ),
    "automation_control": (
        r"\b(?:schedule|trigger|start|run) (?:a |the )?(?:cron job|workflow|pipeline|ci/cd|nightly backup)\b",
        r"\b(?:cron|workflow engine)\b",
    ),
    "identity_auth": (
        r"\b(?:log in|login|authenticate|use credentials|sign in)\b",
        r"\bsign (?:the |a )?(?:document|contract|agreement)\b",
    ),
    "financial_ops": (
        r"\b(?:move|send|transfer|withdraw|deposit) (?:money|funds|cash|assets)\b",
        r"\b(?:trade|buy|sell) (?:stocks?|crypto|assets?|securities)\b",
    ),
    "legal_ops": (
        r"\b(?:file|submit) (?:a |the )?(?:lawsuit|legal filing|court document)\b",
        r"\blegally binding\b",
    ),
    "physical_world": (
        r"\b(?:control|operate|move) (?:a |the )?(?:robot|device|iot|drone|vehicle)\b",
    ),
    "persistent_state": (
        r"\b(?:run|operate) (?:as )?(?:a )?(?:daemon|background service)\b",
        r"\b(?:stay online|maintain uptime|self-schedule|run forever)\b",
    ),
    "data_privacy_control": (
        r"\b(?:enforce|apply) (?:a |the )?(?:retention|encryption|storage|privacy) polic(?:y|ies)\b",
        r"\bdata governance\b",
    ),
}


def load_limits(path: Path = LIMITS_PATH) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    limits = data.get("copilot_limits") if isinstance(data, dict) else None
    if not isinstance(limits, list):
        raise ValueError("Expected 'copilot_limits' to be a list.")

    required = {"id", "title", "description", "offload_to"}
    for index, item in enumerate(limits):
        if not isinstance(item, dict) or not required.issubset(item):
            raise ValueError(f"Invalid limit at index {index}; required keys: {sorted(required)}")

    return limits


class RealityRouter:
    def __init__(self, limits: list[dict[str, str]]) -> None:
        self.limits = {item["id"]: item for item in limits}

    def classify_task(self, task_description: str) -> dict[str, str] | None:
        normalized = " ".join(task_description.lower().split())
        for limit_id, patterns in KEYWORDS.items():
            if limit_id not in self.limits:
                continue
            if any(re.search(pattern, normalized) for pattern in patterns):
                return self.limits[limit_id]
        return None

    def route(self, task_description: str) -> dict[str, Any]:
        limit = self.classify_task(task_description)
        if limit is None:
            return {"mode": "copilot_reasoning", "task": task_description}

        return {
            "mode": "offload",
            "limit_id": limit["id"],
            "offload_to": limit["offload_to"],
            "task": task_description,
        }


if __name__ == "__main__":
    router = RealityRouter(load_limits())
    examples = [
        "Run this Python script on the server and restart the service.",
        "Design me an architecture for a multi-agent system.",
        "Schedule a nightly backup job and verify success.",
    ]
    for task in examples:
        print(f"{task} => {router.route(task)}")
