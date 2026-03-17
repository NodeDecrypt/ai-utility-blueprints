# Image Inputs

This folder is a manifest resource for the `google_flow` tool.

It is used to hold one or more image files that may support image generation.

---

## What this manifest is for

Use this folder when the tool may benefit from multiple image inputs instead of just one single image.

Examples:

- product images
- reference images
- logo variants
- composition references
- style examples

This manifest is useful when a blueprint step needs to pass a grouped set of images to the tool.

---

## What can go in this folder

Examples of suitable files:

- `.png`
- `.jpg`
- `.jpeg`
- `.webp`

Example content:

- product front shot
- product side shot
- packaging shot
- visual inspiration images
- clean logo image
- design reference samples

---

## How a human runner should use it

A human runner can treat this folder as:

- a grouped image input pack
- a place to review all related image assets together
- a reusable image collection for blueprints that use this tool

If a blueprint references image inputs for this tool, the runner can check this folder structure as the expected pattern for a grouped image set.

---

## Good practice

Try to keep the images:

- relevant
- clearly named
- visually usable
- not duplicated without reason
- easy to understand at a glance

Helpful file names:

- `product-front.png`
- `product-side.jpg`
- `logo-clean.png`
- `reference-layout-01.jpg`

---

## What not to include

Do **not** include:

- private or confidential images
- unsafe files
- unrelated random files
- internal-only assets that should not be public
- secret operational materials

This repo is public and community-facing.

---

## Suggested folder use

A typical folder might look like this:

```text
image-inputs/
├── README.md
├── product-front.png
├── product-side.png
├── logo-clean.png
└── reference-layout-01.jpg
```

---

## Final note

This manifest is only a public community resource pattern.

It is meant to help contributors and runners understand how grouped image inputs can be organized for the `google_flow` tool.
