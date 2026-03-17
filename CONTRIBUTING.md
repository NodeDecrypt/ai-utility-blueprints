# Contributing to Node Decrypt Community

Thanks for contributing.

This repo is a public library of human-readable blueprints and reusable tool definitions. The goal is to make it easy for people to share and follow manual creation recipes, while keeping the structure clean enough to support future transmission into Node Decrypt.

Please read this guide before opening a pull request.

---

## Contribution principles

When contributing here, follow these principles:

- keep things human-readable
- keep things community-safe
- keep the structure simple
- keep keys stable
- keep tools reusable
- avoid internal platform details
- do not include secrets

This repo is for public community usage, not internal automation configuration.

---

## What you can contribute

You can contribute:

- a new blueprint
- a new version of an existing blueprint
- a new tool
- a new version of an existing tool
- improved examples
- improved pack README files
- schema-safe cleanup and wording improvements

---

## What should not be contributed

Do **not** contribute:

- real tool URLs
- selectors
- cookies
- auth/session files
- tokens or API keys
- private automation logic
- private prompt IP that should not be public
- hidden internal runner setup
- internal system binding details

If a file or detail would be risky to publish publicly, it does not belong in this repo.

---

## Repo structure

### Blueprints

Blueprints live under:

```text
blueprints/<blueprint-slug>/<version>/
```

Each blueprint version should contain:

```text
README.md
blueprint.json
examples/
preview/
```

### Tools

Tools live under:

```text
tools/<tool-slug>/<version>/
```

Each tool version should contain:

```text
README.md
tool.json
resources/
```

Inside `resources/`:

* `single/` for reusable single resources
* `manifests/` for grouped resources, one folder per manifest

---

## Naming rules

These naming rules are required.

### Folder names

Use `kebab-case`.

Good:

* `banner-design`
* `sticky-man-video`
* `google-flow`

Bad:

* `BannerDesign`
* `banner_design`
* `Banner Design`

### JSON keys

Use `snake_case`.

Good:

* `blueprint_key`
* `tool_key`
* `asset_key`
* `step_key`

### Stable identity keys

Do not include version in the identity key.

Good:

```json
{
  "blueprint_key": "banner_design",
  "version_label": "v1"
}
```

Bad:

```json
{
  "blueprint_key": "banner_design_v1"
}
```

Good:

```json
{
  "tool_key": "google_flow",
  "version_label": "v2"
}
```

Bad:

```json
{
  "tool_key": "google_flow_v2"
}
```

---

## Versioning rules

Blueprints and tools version independently.

### Use version folders

Use folders like:

* `v1`
* `v2`
* `v3`

Do not use:

* `1.0`
* `version1`
* `release-1`

### When to create a new blueprint version

Create a new blueprint version when there is a meaningful change to:

* the blueprint flow
* the asset list
* the tools used
* the step order
* the final deliverables
* the overall method

### When to create a new tool version

Create a new tool version when there is a meaningful change to:

* usage type
* resource setup structure
* input capabilities
* output capabilities
* public intended use pattern

### What does not require a new version

You usually do **not** need a new version for:

* typo fixes
* README clarity improvements
* clearer descriptions that do not change meaning

---

## Blueprint contribution requirements

A blueprint contribution should be complete and understandable on its own.

### Required files

For a new blueprint version, include:

```text
blueprints/<blueprint-slug>/<version>/
├── README.md
├── blueprint.json
├── examples/
│   ├── sample-input.md
│   └── sample-output.md
└── preview/
```

`preview/` can be empty if you do not have a preview yet, but the folder structure should still be clean.

### Blueprint JSON expectations

A valid `blueprint.json` should include:

* `template_version`
* `blueprint`
* `tool_refs`
* `assets`
* `steps`
* `final_deliverables`
* `notes`

### Blueprint quality expectations

A good blueprint should:

* have a clear purpose
* have readable asset names
* have clean step order
* use stable `tool_key` references
* clearly show inputs and outputs for each step
* be easy for a noob to follow

---

## Tool contribution requirements

A tool contribution should describe a reusable tool family, not one blueprint-only setup.

### Required files

For a new tool version, include:

```text
tools/<tool-slug>/<version>/
├── README.md
├── tool.json
└── resources/
    ├── single/
    └── manifests/
```

### Tool JSON expectations

A valid `tool.json` should include:

* `template_version`
* `tool`
* `resource_setups`
* `input_capabilities`
* `output_capabilities`
* `notes`

### Tool quality expectations

A good tool should:

* clearly state what it is good for
* clearly state whether usage is browser only, API only, or both
* separate reusable setup resources from blueprint-specific step data
* describe general input capabilities
* describe general output capabilities
* keep the content public-safe

---

## Resource folder rules

### Single resources

All reusable single resources should go in:

```text
resources/single/
```

Examples:

* `tool-instruction.md`
* `ratio-guide.md`
* `format-guide.md`

### Manifest resources

Each manifest should have its own folder under:

```text
resources/manifests/<manifest-name>/
```

Examples:

* `resources/manifests/image-inputs/`
* `resources/manifests/knowledge-pack/`
* `resources/manifests/reference-files/`

Each manifest folder should include a `README.md` when possible, so a human understands what the folder is for.

---

## Tool references inside blueprints

Blueprints should reference tools through `tool_refs`.

A blueprint version should clearly declare which tool versions it uses.

That keeps the repo stable when blueprints and tools evolve independently.

Inside steps, use only the stable `tool_key`.

---

## Examples and previews

Examples are strongly encouraged.

### For blueprints

Recommended example files:

* `examples/sample-input.md`
* `examples/sample-output.md`

### For tools

Resources and example files should live in the tool's own `resources/` folders.

### Preview files

Preview files are optional but recommended where useful.

---

## Validation requirements

All JSON must pass schema validation.

A pull request may be blocked if:

* required fields are missing
* enum values are invalid
* referenced tools do not exist
* referenced assets do not exist
* step numbering is broken
* file structure is inconsistent

Always validate your JSON before submitting.

Run local validation from the repo root with:

```bash
python scripts/validate_repo.py
```

Expected success output looks like:

```text
Validated <n> JSON files, <n> YAML files, <n> tool files, and <n> blueprint files
```

If the command reports an error, fix that issue and rerun validation before opening your PR.

---

## Pull request checklist

Before opening a PR, confirm that:

* your folder names use `kebab-case`
* your JSON keys use `snake_case`
* your keys are stable and readable
* your JSON matches the schema
* your version folder is correct
* your README is included
* your contribution is public-safe
* you did not include secrets or internal-only details

---

## Recommended PR scope

Keep PRs focused.

Good PR examples:

* one new blueprint version
* one new tool version
* one blueprint and one new tool it depends on
* one schema-safe improvement
* one docs improvement

Try not to mix many unrelated changes into one PR.

---

## Review standards

Maintainers may request changes if:

* the structure is confusing
* the naming is inconsistent
* the content is not community-safe
* the tool is too blueprint-specific
* the blueprint is too vague to follow
* the JSON does not match the schema

The main standard is simple:

> A new community user should be able to open the pack and understand what it is and how to use it.

---

## Need a starting point

Use the files in `templates/` first.

You should copy:

* `templates/blueprint.template.json`
* `templates/tool.template.json`

Then compare your draft against the example files.

---

## Questions and proposals

If you are unsure whether something belongs in a blueprint or a tool, open an issue first.

A good issue should explain:

* what you want to add
* whether it is blueprint-level or tool-level
* why it should be reusable
* whether it changes an existing version or requires a new one

---

## Final reminder

This repo should stay:

* simple
* readable
* reusable
* public-safe

When in doubt, prefer the simpler and clearer structure.
