from __future__ import annotations

import json
import re
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DOCS_ROOT = Path(r"c:\projects\ai-ult-for-dev\docs")
DETAILS_PATH = DOCS_ROOT / "detail-file-contents.txt"


def parse_detail_file(text: str) -> dict[str, str]:
    files: dict[str, str] = {}
    current_path: str | None = None
    fence: str | None = None
    content: list[str] = []

    for raw_line in text.splitlines():
        heading = re.match(r"## `(.+?)`\s*$", raw_line)
        if fence is None and heading:
            current_path = heading.group(1)
            continue

        if current_path is None:
            continue

        stripped = raw_line.strip()
        if fence is None:
            fence_match = re.match(r"^(`{3,4})(?:[A-Za-z0-9_-]+)?$", stripped)
            if fence_match:
                fence = fence_match.group(1)
                content = []
            continue

        if stripped == fence:
            files[current_path] = "\n".join(content).rstrip() + "\n"
            current_path = None
            fence = None
            content = []
            continue

        content.append(raw_line)

    return files


def write_files(files: dict[str, str]) -> None:
    for relative_path, contents in files.items():
        destination = REPO_ROOT / relative_path
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(contents, encoding="utf-8")


def add_supporting_files(files: dict[str, str]) -> None:
    files.setdefault("blueprints/banner-design/v1/preview/.gitkeep", "")

    config_path = ".github/ISSUE_TEMPLATE/config.yml"
    if config_path in files:
        files[config_path] = files[config_path].replace(
            "url: ./CONTRIBUTING.md",
            "url: https://github.com/NodeDecrypt/ai-utility-blueprints/blob/main/CONTRIBUTING.md",
        )

    license_path = "LICENSE"
    if license_path in files:
        files[license_path] = files[license_path].replace(
            "Copyright (c) [year] Node Decrypt Community contributors",
            "Copyright (c) 2026 Node Decrypt Community contributors",
        )

    if "tools/google-flow/v1/tool.json" in files:
        files.setdefault("tools/google-flow/v1/resources/manifests/image-inputs/.gitkeep", "")
        files.setdefault("tools/google-flow/v1/resources/manifests/knowledge-pack/.gitkeep", "")

    if "blueprints/banner-design/v1/blueprint.json" in files:
        files["templates/blueprint.example.json"] = files["blueprints/banner-design/v1/blueprint.json"]

    if "tools/google-flow/v1/tool.json" in files:
        files["templates/tool.example.json"] = files["tools/google-flow/v1/tool.json"]


def make_generic_tool(
    slug: str,
    key: str,
    name: str,
    summary: str,
    description: str,
    input_name: str,
    output_name: str,
) -> dict[str, str]:
    tool_json = {
        "template_version": "community.tool.v4",
        "tool": {
            "tool_key": key,
            "tool_name": name,
            "summary": summary,
            "description": description,
            "tool_type": "text_assistant",
            "usage_type": "both",
            "version_label": "v1",
        },
        "resource_setups": [
            {
                "resource_key": "tool_instruction",
                "resource_name": "Tool Instruction",
                "structure": "single",
                "resource_type": "text",
                "importance": "recommended",
                "description": "A reusable instruction resource prepared for this tool.",
            },
            {
                "resource_key": "reference_pack",
                "resource_name": "Reference Pack",
                "structure": "manifest",
                "resource_type": "file",
                "importance": "optional",
                "description": "A reusable grouped reference resource prepared for this tool.",
            },
        ],
        "input_capabilities": [
            {
                "capability_key": "main_input",
                "capability_name": input_name,
                "structure": "single",
                "resource_type": "text",
                "importance": "must_have",
                "description": f"Main {input_name.lower()} the tool can accept.",
            },
            {
                "capability_key": "supporting_context",
                "capability_name": "Supporting Context",
                "structure": "manifest",
                "resource_type": "file",
                "importance": "optional",
                "description": "Optional grouped context files or reference materials.",
            },
        ],
        "output_capabilities": [
            {
                "capability_key": "main_output",
                "capability_name": output_name,
                "structure": "single",
                "resource_type": "text",
                "description": f"Primary {output_name.lower()} returned by the tool.",
            }
        ],
        "notes": [
            "This is a reusable public community tool definition for Node Decrypt.",
            "It does not include internal URLs, selectors, auth data, API keys, or hidden automation details.",
        ],
    }

    base = Path("tools") / slug / "v1"
    return {
        str(base / "README.md"): (
            f"# {name}\n\n"
            f"Reusable tool definition for {summary.lower()} in Node Decrypt Community.\n\n"
            "---\n\n"
            "## Summary\n\n"
            f"{name} is used as a reusable tool for {summary.lower()}.\n\n"
            "This tool definition is public, reusable, and community-facing.\n\n"
            "---\n\n"
            "## Usage type\n\n"
            "- `both`\n\n"
            "This tool should be described in a community-safe way and reused across multiple blueprints.\n\n"
            "---\n\n"
            "## What this tool is good for\n\n"
            f"- {summary.lower()}\n"
            "- turning rough inputs into clearer working material\n"
            "- providing reusable support in multi-step blueprint flows\n\n"
            "---\n\n"
            "## Resource folders\n\n"
            "This pack includes `resources/single/` for reusable one-off guidance and `resources/manifests/` for grouped public-safe reference materials.\n\n"
            "---\n\n"
            "## Version notes\n\n"
            "### `v1`\n\n"
            f"Initial public community version of the {name} tool definition for Node Decrypt Community.\n"
        ),
        str(base / "tool.json"): json.dumps(tool_json, indent=2) + "\n",
        str(base / "resources" / "single" / "README.md"): (
            f"# Single Resources\n\n"
            f"This folder contains reusable single resources for the `{key}` tool.\n"
        ),
        str(base / "resources" / "single" / "tool-instruction.md"): (
            f"# Tool Instruction - {name}\n\n"
            f"This file is a reusable public-safe instruction resource for the `{key}` tool.\n"
        ),
        str(base / "resources" / "manifests" / "reference-files" / "README.md"): (
            "# Reference Files\n\n"
            f"This folder is a manifest resource for the `{key}` tool.\n"
        ),
        str(base / "resources" / "manifests" / "reference-files" / ".gitkeep"): "",
    }


def ensure_referenced_tools(files: dict[str, str]) -> None:
    inferred = [
        make_generic_tool(
            "business-brief-chatbot",
            "business_brief_chatbot",
            "Business Brief Chatbot",
            "turning brand and project inputs into a requirement summary",
            "A reusable community tool definition for business and requirement summarization.",
            "Business Inputs",
            "Requirement Summary",
        ),
        make_generic_tool(
            "design-brief-chatbot",
            "design_brief_chatbot",
            "Design Brief Chatbot",
            "turning requirement summaries into stronger design briefs",
            "A reusable community tool definition for design-brief creation.",
            "Design Inputs",
            "Design Brief",
        ),
        make_generic_tool(
            "design-specs-chatbot",
            "design_specs_chatbot",
            "Design Specs Chatbot",
            "turning design briefs into production-ready design specs",
            "A reusable community tool definition for design-spec creation.",
            "Design Brief",
            "Design Specs",
        ),
    ]
    for tool_files in inferred:
        for path, contents in tool_files.items():
            files.setdefault(path, contents)


def main() -> None:
    detail_text = DETAILS_PATH.read_text(encoding="utf-8")
    files = parse_detail_file(detail_text)
    add_supporting_files(files)
    ensure_referenced_tools(files)
    write_files(files)
    print(f"Created {len(files)} files from docs")


if __name__ == "__main__":
    main()
