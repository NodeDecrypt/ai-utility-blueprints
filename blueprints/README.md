# Blueprints

This folder contains the blueprint library for Node Decrypt Community.

A blueprint is a human-readable manual recipe that shows how to create a specific output step by step.

Blueprints in this repo are written for people who do **not** need to know Node Decrypt internals. A reader should be able to open a blueprint pack, understand the goal, prepare the assets, follow the steps, and produce the final deliverable.

---

## What a blueprint contains

A blueprint usually defines:

- what it creates
- what assets are needed
- which tools are used
- the step-by-step process
- the final deliverable

A blueprint is intentionally simple and flat.

It should **not** contain:

- internal automation logic
- selectors
- private tool URLs
- cookies or auth data
- tokens or API keys
- internal runner setup
- private-only prompt systems

---

## Folder structure

Each blueprint lives in its own slug folder and version folder.

```text
blueprints/<blueprint-slug>/<version>/
├── README.md
├── blueprint.json
├── examples/
│   ├── assets/
│   ├── example-1.md
│   └── outputs/
└── preview/
    └── preview.png
```

Example:

```text
blueprints/banner-design/v1/
```

---

## Naming rules

### Blueprint folder names

Use `kebab-case`.

Good:

* `banner-design`
* `sticky-man-video`
* `product-shot-enhancer`

Bad:

* `BannerDesign`
* `banner_design`
* `Banner Design`

### Version folder names

Use:

* `v1`
* `v2`
* `v3`

Do not use:

* `1.0`
* `version1`

---

## What goes in each file

### `README.md`

A quick human overview of the blueprint.

Recommended contents:

* blueprint name
* one-line summary
* who it is for
* final deliverable
* tools used
* main step summary
* limitations
* version notes

### `blueprint.json`

The structured blueprint definition.

This is the main file used to represent the blueprint in a consistent way across the repo.

### `examples/`

Worked examples for the blueprint.

Recommended:

* `assets/` for non-text example assets
* `example-1.md` for one full process example with per-step input/output mapping
* `outputs/` for additional final-output-only examples

These help new users understand how the blueprint is meant to be used.

Text assets can be written inline in `example-1.md`.

Large media should be linked in markdown instead of committed as heavy files.

### `preview/`

Optional visual preview files.

This folder is useful when the blueprint produces visual outputs like images or videos.

---

## Blueprint JSON structure

A typical blueprint file contains:

* `template_version`
* `blueprint`
* `tool_refs`
* `assets`
* `steps`
* `final_deliverables`
* `notes`

### `blueprint`

General metadata about the blueprint.

### `tool_refs`

The tools and versions this blueprint expects.

### `assets`

The named things used or produced in the blueprint.

Typical stages:

* `input`
* `intermediate`
* `output`

### `steps`

The flat step-by-step manual flow.

Each step should clearly show:

* what the step is for
* which tool is used
* what inputs it uses
* what outputs it creates
* what should be checked before continuing

### `final_deliverables`

The final outputs the blueprint is meant to produce.

### `notes`

Any extra public-safe notes for readers or contributors.

---

## Versioning rules

Blueprints version independently from tools.

That means:

* a blueprint can move from `v1` to `v2`
* a related tool can stay on `v1`
* another blueprint might still keep using an older tool version

A new blueprint version should be created when there is a meaningful change to:

* the step flow
* the asset list
* the tools used
* the final deliverable
* the overall method

Small wording or doc fixes usually do not need a new version folder.

---

## Quality standard

A good blueprint should be:

* clear
* easy to follow
* public-safe
* complete enough for a noob to use
* consistent with the schema
* explicit about inputs and outputs

The easiest test is:

> Can a new community user open this blueprint and understand what to do without knowing Node Decrypt internals?

If the answer is no, the blueprint probably needs to be simplified or clarified.

---

## Tool references

Blueprints do not define tools inside the blueprint pack.

Instead, they reference reusable tools from the `tools/` library using `tool_refs`.

This keeps tools reusable and makes versioning cleaner.

---

## Before contributing a blueprint

Please:

1. read the root `README.md`
2. read `CONTRIBUTING.md`
3. copy `templates/blueprint.template.json`
4. compare with `templates/blueprint.example.json`
5. make sure your JSON matches the schema
6. confirm that your content is public-safe

---

## Final note

Blueprints are recipes.

Keep them simple, practical, and readable.
