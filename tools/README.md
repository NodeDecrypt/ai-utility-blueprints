# Tools

This folder contains the reusable tool library for Node Decrypt Community.

A tool in this repo is a public, reusable definition of a tool family. It describes what the tool is for, how it can generally be used, what reusable setup resources exist for it, and what kinds of inputs and outputs it supports.

A tool here is **not** an internal Node Decrypt runtime definition.

It should stay human-readable and public-safe.

---

## What a tool contains

A tool usually defines:

- tool identity
- summary and description
- tool type
- usage type
- reusable resource setups
- general input capabilities
- general output capabilities

A tool is reusable across multiple blueprints.

It should **not** contain:

- private tool URLs
- selectors
- cookies
- session files
- tokens or API keys
- internal automation logic
- internal route details
- hidden private prompt systems

---

## Folder structure

Each tool lives in its own slug folder and version folder.

```text
tools/<tool-slug>/<version>/
├── README.md
├── tool.json
└── resources/
    ├── single/
    └── manifests/
```

Example:

```text
tools/google-flow/v1/
```

---

## Naming rules

### Tool folder names

Use `kebab-case`.

Good:

* `google-flow`
* `business-brief-chatbot`
* `design-specs-chatbot`

Bad:

* `GoogleFlow`
* `google_flow`
* `Google Flow`

### Version folder names

Use:

* `v1`
* `v2`
* `v3`

Do not use:

* `1.0`
* `version1`

### Tool keys in JSON

Use `snake_case`.

Good:

* `google_flow`
* `business_brief_chatbot`

Do not put the version in the `tool_key`.

Good:

```json
{
  "tool_key": "google_flow",
  "version_label": "v1"
}
```

Bad:

```json
{
  "tool_key": "google_flow_v1"
}
```

---

## What goes in each file

### `README.md`

A quick human overview of the tool.

Recommended contents:

* tool name
* summary
* usage type
* what it is good for
* general input capabilities
* general output capabilities
* resource setup overview
* version notes

### `tool.json`

The structured reusable tool definition.

This file should stay general and reusable. It should not be tailored to just one blueprint.

### `resources/`

This folder contains reusable public-safe setup resources for the tool.

---

## Resource folder convention

### `resources/single/`

This folder contains reusable single resources.

Examples:

* `tool-instruction.md`
* `ratio-guide.md`
* `format-guide.md`

These are one-off resources that stand alone.

### `resources/manifests/`

This folder contains grouped resources.

Each manifest should have its own folder.

Examples:

```text
resources/manifests/image-inputs/
resources/manifests/knowledge-pack/
resources/manifests/reference-files/
```

Inside each manifest folder, include a small `README.md` whenever possible so a human understands:

* what the manifest is
* what files belong there
* how it should be used

---

## Tool JSON structure

A typical tool file contains:

* `template_version`
* `tool`
* `resource_setups`
* `input_capabilities`
* `output_capabilities`
* `notes`

### `tool`

General metadata about the tool.

Typical fields include:

* `tool_key`
* `tool_name`
* `summary`
* `description`
* `tool_type`
* `usage_type`
* `version_label`

### `resource_setups`

Reusable prepared resources for the tool.

These are not blueprint steps. They are general reusable tool-side resources.

### `input_capabilities`

The kinds of inputs the tool can generally accept.

### `output_capabilities`

The kinds of outputs the tool can generally produce.

### `notes`

Extra public-safe notes.

---

## Usage type

Each tool should declare one `usage_type`.

Allowed values:

* `browser_only`
* `api_only`
* `both`

Use the most accurate value for the community-facing tool definition.

---

## Versioning rules

Tools version independently from blueprints.

A new tool version should be created when there is a meaningful change to:

* usage type
* resource setup structure
* input capabilities
* output capabilities
* overall public intended use pattern

Small README wording improvements usually do not require a new version folder.

---

## Quality standard

A good tool definition should be:

* reusable
* readable
* public-safe
* not tied to one blueprint only
* clear about what it accepts and produces
* consistent with the schema

The easiest test is:

> Can a contributor reuse this tool in more than one blueprint without rewriting the tool definition?

If the answer is no, the tool may be too blueprint-specific.

---

## Before contributing a tool

Please:

1. read the root `README.md`
2. read `CONTRIBUTING.md`
3. copy `templates/tool.template.json`
4. compare with `templates/tool.example.json`
5. make sure your JSON matches the schema
6. confirm that your content is public-safe

---

## Final note

Tools are reusable building blocks.

Keep them general, practical, and easy to understand.
