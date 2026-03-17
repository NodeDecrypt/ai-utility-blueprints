# Google Flow

Reusable tool definition for image generation in Node Decrypt Community.

---

## Summary

Google Flow is used here as a reusable image-generation tool that can create final visual outputs from structured text instructions and optional supporting visual inputs.

This tool definition is public, reusable, and community-facing.

---

## Usage type

- `both`

This means the tool may be used through browser or API depending on the community setup and the blueprint using it.

---

## What this tool is good for

This tool is useful for:

- final image generation
- turning detailed creative specs into images
- visual production from structured instructions
- workflows where image inputs may support generation

---

## General input capabilities

This tool may accept inputs such as:

- text instruction
- image inputs
- ratio or size guidance

See `tool.json` for the structured capability definition.

---

## General output capabilities

This tool may produce outputs such as:

- generated image
- optional generation text

See `tool.json` for the structured capability definition.

---

## Resource setup overview

This tool pack may include reusable setup resources such as:

- single instruction files
- ratio guides
- grouped reference packs
- grouped image example folders

These resources should be public-safe and reusable across multiple blueprints.

---

## Resource folder guide

### `resources/single/`

Use this folder for one-off reusable tool resources.

Examples:

- instruction files
- format guides
- ratio guides
- general usage notes

### `resources/manifests/`

Use this folder for grouped resources.

Each manifest should have its own folder.

Examples:

- `resources/manifests/image-inputs/`
- `resources/manifests/knowledge-pack/`

Each manifest folder should include a `README.md` when possible so a human reader understands what is inside and how to use it.

---

## What this tool definition should not contain

Do **not** include:

- private URLs
- selectors
- cookies
- tokens
- auth/session files
- hidden automation logic
- internal Node Decrypt configuration
- private prompt systems

This repo keeps tool definitions public-safe and human-readable.

---

## Reuse guidance

This tool is meant to be reused by multiple blueprints.

A blueprint should reference this tool through:

- `tool_key`: `google_flow`
- `version_label`: `v1`

The blueprint should define its own actual step flow and blueprint-specific assets separately.

---

## Folder contents

This pack should contain:

- `README.md`
- `tool.json`
- `resources/single/`
- `resources/manifests/`

---

## Version notes

### `v1`

Initial public community version of the Google Flow tool definition for Node Decrypt Community.

---

## Related files

- `tool.json` for the structured tool definition
- `resources/` for reusable prepared resources
- `blueprints/` for blueprint packs that reference this tool
