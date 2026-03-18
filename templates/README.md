# Templates

This folder contains starter files for Node Decrypt Community contributors.

Use these files when you want to create a new blueprint or tool in the repo.

---

## Files in this folder

### `blueprint.template.json`

A clean starter template for a new blueprint.

Use this when you want to create a new manual blueprint pack under:

```text
blueprints/<blueprint-slug>/<version>/
```

### `tool.template.json`

A clean starter template for a new tool.

Use this when you want to create a new reusable tool pack under:

```text
tools/<tool-slug>/<version>/
```

### `blueprint.example.json`

A filled example blueprint.

Use this to understand how a real blueprint should look.

### `tool.example.json`

A filled example tool.

Use this to understand how a real tool should look.

---

## How to use these templates

### For a new blueprint

1. Copy `blueprint.template.json`
2. Rename and fill in the values
3. Save it as:

```text
blueprints/<blueprint-slug>/<version>/blueprint.json
```

4. Add the matching `README.md`
5. Add `examples/assets/`, `examples/example-1.md`, and `examples/outputs/`
6. Add `preview/` if available

### For a new tool

1. Copy `tool.template.json`
2. Rename and fill in the values
3. Save it as:

```text
tools/<tool-slug>/<version>/tool.json
```

4. Add the matching `README.md`
5. Add `resources/single/`
6. Add `resources/manifests/`

---

## Important rules

When using these templates:

* keep folder names in `kebab-case`
* keep JSON keys in `snake_case`
* do not put version inside `tool_key` or `blueprint_key`
* keep version in `version_label`
* do not include secrets or private internal details
* make sure the final JSON matches the schema in `schemas/`

---

## Reminder about public-safe content

This repo is public.

Do **not** include:

* private URLs
* selectors
* cookies
* tokens
* auth/session files
* internal-only materials
* secret prompts or private automation logic

Keep all contributions community-safe and public-safe.

---

## Recommended workflow for contributors

If you are new:

1. read the root `README.md`
2. read `CONTRIBUTING.md`
3. copy the correct template
4. compare your draft with the example file
5. validate against the schema
6. open a PR

---

## Final note

Templates are starting points, not final content.

Please replace all placeholder values with real, clear, human-readable content before submitting.
