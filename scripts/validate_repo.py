from __future__ import annotations

import json
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    for path in sorted(ROOT.rglob("*.json")):
        load_json(path)

    for path in sorted(ROOT.rglob("*.yml")):
        yaml.safe_load(path.read_text(encoding="utf-8"))

    blueprint_schema = load_json(ROOT / "schemas" / "blueprint.schema.json")
    tool_schema = load_json(ROOT / "schemas" / "tool.schema.json")
    blueprint_validator = Draft202012Validator(blueprint_schema)
    tool_validator = Draft202012Validator(tool_schema)

    tool_versions: dict[str, set[str]] = {}
    tool_files = sorted((ROOT / "tools").rglob("tool.json"))
    blueprint_files = sorted((ROOT / "blueprints").rglob("blueprint.json"))

    if not tool_files:
        raise SystemExit("No tool.json files found")
    if not blueprint_files:
        raise SystemExit("No blueprint.json files found")

    for tool_file in tool_files:
        data = load_json(tool_file)
        errors = sorted(tool_validator.iter_errors(data), key=lambda err: list(err.path))
        if errors:
            raise SystemExit(f"{tool_file}: {errors[0].message}")

        tool_meta = data["tool"]
        tool_versions.setdefault(tool_meta["tool_key"], set()).add(tool_meta["version_label"])

    for blueprint_file in blueprint_files:
        data = load_json(blueprint_file)
        errors = sorted(blueprint_validator.iter_errors(data), key=lambda err: list(err.path))
        if errors:
            raise SystemExit(f"{blueprint_file}: {errors[0].message}")

        tool_refs = data["tool_refs"]
        assets = {asset["asset_key"] for asset in data["assets"]}
        step_numbers = [step["step_number"] for step in data["steps"]]
        if step_numbers != sorted(step_numbers) or len(step_numbers) != len(set(step_numbers)):
            raise SystemExit(f"{blueprint_file}: invalid step ordering")

        declared_tool_keys = {tool_ref["tool_key"] for tool_ref in tool_refs}
        for tool_ref in tool_refs:
            tool_key = tool_ref["tool_key"]
            version_label = tool_ref["version_label"]
            if tool_key not in tool_versions or version_label not in tool_versions[tool_key]:
                raise SystemExit(f"{blueprint_file}: missing tool ref {tool_key}@{version_label}")

        for step in data["steps"]:
            if step["tool_key"] not in declared_tool_keys:
                raise SystemExit(f"{blueprint_file}: undeclared step tool {step['tool_key']}")
            if not all(item in assets for item in step["inputs"]):
                raise SystemExit(f"{blueprint_file}: bad step inputs in {step['step_key']}")
            if not all(item in assets for item in step["outputs"]):
                raise SystemExit(f"{blueprint_file}: bad step outputs in {step['step_key']}")

        if not all(item in assets for item in data["final_deliverables"]):
            raise SystemExit(f"{blueprint_file}: bad final deliverables")

    print(
        "Validated "
        f"{len(list(ROOT.rglob('*.json')))} JSON files, "
        f"{len(list(ROOT.rglob('*.yml')))} YAML files, "
        f"{len(tool_files)} tool files, and {len(blueprint_files)} blueprint files"
    )


if __name__ == "__main__":
    main()
