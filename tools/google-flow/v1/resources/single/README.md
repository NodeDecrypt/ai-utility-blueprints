# Single Resources

This folder contains reusable single resources for the `google_flow` tool.

A single resource is one standalone file that can be used on its own, instead of as part of a grouped manifest folder.

---

## What this folder is for

Use `resources/single/` for one-off reusable tool resources such as:

- instruction files
- format guides
- ratio guides
- naming guides
- output guidance
- small public-safe reference notes

These files should be easy for a human runner to open and use directly.

---

## When to use a single resource

Use a single resource when:

- the resource is one standalone document
- it does not need its own grouped folder
- the content is simple enough to live in one file
- the runner can understand and use it without extra folder structure

Examples:

- one tool instruction document
- one ratio guide
- one format rule sheet

---

## Good file examples

Examples of files that may live here:

- `tool-instruction.md`
- `ratio-guide.md`
- `format-guide.md`
- `output-checklist.md`

---

## Good practice

Try to keep single resources:

- short and clear
- public-safe
- reusable across more than one blueprint when possible
- easy to understand for beginners
- clearly named

Helpful file names:

- `tool-instruction.md`
- `ratio-guide.md`
- `output-checklist.md`

---

## What not to include

Do **not** include:

- private URLs
- selectors
- cookies
- auth/session data
- tokens or API keys
- internal automation logic
- private-only materials
- confidential project files

This repo is public and community-facing.

---

## Suggested folder use

A typical folder might look like this:

```text
single/
├── README.md
├── tool-instruction.md
├── ratio-guide.md
└── output-checklist.md
```

---

## Final note

This folder is meant to make reusable tool resources simple to browse.

If a resource needs its own grouped collection, it should go in `resources/manifests/` instead.
