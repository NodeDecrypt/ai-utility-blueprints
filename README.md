# Node Decrypt Community

A public library of human-readable blueprints and reusable tool definitions for the community.

This repo is designed for people who want to follow and share practical creation recipes without needing to understand Node Decrypt internals. Each blueprint is written as a simple manual step-by-step flow. Each tool is defined as a reusable community-safe reference that can support multiple blueprints.

---

## What is in this repo

This repo contains two main libraries:

- `blueprints/` - flat manual recipes that humans can follow step by step
- `tools/` - reusable tool definitions and tool resource folders

This repo is **not** the runtime spec for Node Decrypt, and it does **not** contain internal automation logic.

---

## What is a blueprint

A blueprint is a human-readable recipe for creating an output.

A blueprint tells people:

- what they are trying to make
- what assets they need
- which tools they use
- which steps to follow
- what the final deliverable is

A blueprint is intentionally simple. It does not use internal platform terms like action, vibe, runner, sync, async, policy, selector, or locator.

---

## What is a tool

A tool is a reusable community definition of a tool family.

A tool tells people:

- what the tool is
- what kind of work it is good for
- whether it can be used in browser, API, or both
- what reusable setup resources exist for that tool
- what kinds of inputs it can generally accept
- what kinds of outputs it can generally produce

A tool is reusable across multiple blueprints.

---

## Public and private boundary

This repo is public and community-facing.

Safe to include here:

- blueprint descriptions
- manual steps
- community-safe tool descriptions
- reusable public setup resources
- public example files
- sample inputs and outputs

Do **not** include:

- real tool URLs
- selectors
- cookies
- auth/session data
- tokens or API keys
- hidden internal automation logic
- secret prompts or private IP that should not be public

---

## Repo structure

```text
ai-utility-blueprints/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── .gitignore
├── .github/
│   ├── workflows/
│   │   └── validate.yml
│   ├── ISSUE_TEMPLATE/
│   └── pull_request_template.md
├── schemas/
│   ├── blueprint.schema.json
│   └── tool.schema.json
├── templates/
│   ├── blueprint.template.json
│   ├── tool.template.json
│   ├── blueprint.example.json
│   └── tool.example.json
├── blueprints/
│   └── <blueprint-slug>/
│       └── <version>/
│           ├── README.md
│           ├── blueprint.json
│           ├── examples/
│           └── preview/
└── tools/
    └── <tool-slug>/
        └── <version>/
            ├── README.md
            ├── tool.json
            └── resources/
                ├── single/
                └── manifests/
```

---

## How to browse the repo

If you want to use a blueprint:

1. Go to `blueprints/`
2. Pick a blueprint folder
3. Open the latest version you want to use
4. Read that pack's `README.md`
5. Open `blueprint.json` for the exact structure
6. Check the referenced tools under `tools/`

If you want to understand a tool:

1. Go to `tools/`
2. Pick the tool folder
3. Open the version you want
4. Read `README.md`
5. Open `tool.json`
6. Browse `resources/single/` and `resources/manifests/`

---

## Blueprint folder structure

Each blueprint version should look like this:

```text
blueprints/<blueprint-slug>/<version>/
├── README.md
├── blueprint.json
├── examples/
│   ├── sample-input.md
│   └── sample-output.md
└── preview/
    └── preview.png
```

### What each file/folder is for

* `README.md` - quick human overview
* `blueprint.json` - structured blueprint definition
* `examples/` - example input and output
* `preview/` - optional visual preview

---

## Tool folder structure

Each tool version should look like this:

```text
tools/<tool-slug>/<version>/
├── README.md
├── tool.json
└── resources/
    ├── single/
    └── manifests/
```

### What each file/folder is for

* `README.md` - quick human overview of the tool
* `tool.json` - structured reusable tool definition
* `resources/single/` - reusable single setup resources
* `resources/manifests/` - grouped setup resources, one folder per manifest

### Resource setup convention

Single resources belong in:

```text
resources/single/
```

Examples:

* `tool-instruction.md`
* `ratio-guide.md`
* `format-guide.md`

Manifest resources belong in:

```text
resources/manifests/<manifest-name>/
```

Examples:

* `resources/manifests/image-inputs/`
* `resources/manifests/knowledge-pack/`
* `resources/manifests/reference-files/`

Each manifest folder should include a small `README.md` that explains what the folder is for.

---

## Versioning

Blueprints and tools version independently.

Examples:

* `blueprints/banner-design/v1/`
* `blueprints/banner-design/v2/`
* `tools/google-flow/v1/`
* `tools/google-flow/v2/`

### Versioning rules

* Version folders should be treated as stable
* Small typo or doc fixes are okay
* Meaningful changes should go into a new version folder
* Do not put the version inside `blueprint_key` or `tool_key`
* Keep version in `version_label`

Good:

```json
{
  "blueprint_key": "banner_design",
  "version_label": "v1"
}
```

Good:

```json
{
  "tool_key": "google_flow",
  "version_label": "v1"
}
```

Not recommended:

```json
{
  "tool_key": "google_flow_v1"
}
```

---

## Naming rules

### Folder names

Use `kebab-case`.

Examples:

* `banner-design`
* `sticky-man-video`
* `google-flow`

### JSON keys

Use `snake_case`.

Examples:

* `blueprint_key`
* `tool_key`
* `asset_key`
* `step_key`

### Stable keys

Keep keys stable and readable.

Examples:

* `banner_design`
* `business_brief_chatbot`
* `professional_design_specs`
* `generate_final_banner`

---

## Validation

All contributed blueprint and tool files should pass schema validation.

Validation checks should confirm things like:

* required fields exist
* enum values are valid
* referenced tool keys exist
* referenced asset keys exist
* step order is valid
* version structure is valid

See `schemas/` for the current validation contract.

Before opening a PR, run local validation from the repo root:

```bash
python scripts/validate_repo.py
```

Expected success output looks like:

```text
Validated <n> JSON files, <n> YAML files, <n> tool files, and <n> blueprint files
```

If validation fails, fix the reported file or reference problem first, then rerun the command until it passes.

---

## How to contribute

See [CONTRIBUTING.md](./CONTRIBUTING.md).

In general:

* new blueprints go under `blueprints/`
* new tools go under `tools/`
* each contribution should include the expected JSON and README files
* all JSON should match the schema
* do not include secrets or internal automation details

---

## Suggested first steps for new contributors

If you are new here:

1. read this README
2. open `templates/`
3. copy the blueprint or tool template
4. fill in your content
5. compare with the example files
6. submit a PR

---

## License

See `LICENSE`.
