# Example 1 - Banner Design

## Overview

This worked example shows one complete run of the `banner_design` blueprint. It includes inline text inputs, references to non-text assets in `examples/assets/`, and the output generated at each step.

---

## Assets used

| asset_key | where | notes |
|---|---|---|
| `brand_name` | inline | `Lunera Skincare` |
| `logo_image` | `examples/assets/logo_image/` | optional |
| `product_images` | `examples/assets/product_images/` | required |
| `design_ref_images` | `examples/assets/design_ref_images/` | optional |
| `headline` | inline | `Glow Starts Here` |
| `subheadline` | inline | `Vitamin C Serum for brighter, smoother-looking skin` |
| `platform` | inline | `Instagram Feed` |
| `layout_ratio` | inline | `4:5` |

---

## Step 01 - create_requirement_summary

- Tool: `business_brief_chatbot`
- Inputs:
  - `brand_name` - inline
  - `logo_image` - `examples/assets/logo_image/` (optional)
  - `product_images` - `examples/assets/product_images/`
  - `design_ref_images` - `examples/assets/design_ref_images/` (optional)
  - `headline` - inline
  - `subheadline` - inline
  - `platform` - inline
  - `layout_ratio` - inline
- Outputs:
  - `design_requirement_summary` - inline (below)

Example output (mock):

```text
Lunera Skincare needs a premium-looking promotional banner for Instagram Feed format. The design should highlight the Vitamin C Serum as the hero product and communicate brightness, freshness, and skincare trust. The visual direction should feel clean, elegant, modern, and light. The layout should support mobile readability and keep the message easy to understand at a glance.
```

Checks before next step:

- Make sure the summary is clear and complete.
- Make sure the summary reflects the product, audience, and visual direction.

---

## Step 02 - create_professional_design_brief

- Tool: `design_brief_chatbot`
- Inputs:
  - `design_requirement_summary` - inline (from Step 01)
  - `logo_image` - `examples/assets/logo_image/` (optional)
  - `product_images` - `examples/assets/product_images/`
  - `design_ref_images` - `examples/assets/design_ref_images/` (optional)
- Outputs:
  - `professional_design_brief` - inline (below)

Example output (mock):

```text
Create a premium skincare banner for Lunera Skincare promoting its Vitamin C Serum. The product should be the visual hero, supported by a clean and minimal composition. The mood should feel bright, soft, fresh, and trustworthy. Use a layout suitable for Instagram Feed in 4:5 ratio. The design should balance elegance with clarity, using restrained visual elements so the product and message remain the main focus. Typography should be modern and readable, with a clear headline and supporting subheadline.
```

Checks before next step:

- Make sure the brief is specific enough for a designer or image tool to follow.
- Make sure the tone, layout direction, and visual style are coherent.

---

## Step 03 - create_design_specs

- Tool: `design_specs_chatbot`
- Inputs:
  - `professional_design_brief` - inline (from Step 02)
  - `logo_image` - `examples/assets/logo_image/` (optional)
  - `product_images` - `examples/assets/product_images/`
  - `design_ref_images` - `examples/assets/design_ref_images/` (optional)
- Outputs:
  - `professional_design_specs` - inline (below)

Example output (mock):

```text
Format: Instagram Feed
Ratio: 4:5
Main visual focus: Vitamin C Serum bottle
Secondary visual support: soft skincare-inspired background treatment
Style: minimal, premium, clean, soft lighting
Color direction: white, light cream, soft yellow, subtle warm highlights
Headline placement: upper or upper-middle area with strong readability
Subheadline placement: below headline with lighter emphasis
Product placement: centered or slightly off-center as hero object
Logo placement: top corner or bottom corner depending on layout balance
Composition goal: elegant hierarchy with clear whitespace
Avoid: clutter, harsh contrast, noisy backgrounds, overly aggressive sales style
```

Checks before next step:

- Make sure the specs are detailed enough to generate the banner.
- Make sure the specs match the intended ratio and platform if provided.

---

## Step 04 - generate_final_banner

- Tool: `google_flow`
- Inputs:
  - `professional_design_specs` - inline (from Step 03)
  - `logo_image` - `examples/assets/logo_image/` (optional)
  - `product_images` - `examples/assets/product_images/`
  - `layout_ratio` - inline
- Outputs:
  - `final_banner_image` - `examples/assets/final_banner_image/` (preview file if available)

Example output (mock):

- Preview path: `examples/assets/final_banner_image/`
- External output link (if large media): `<public-url-to-output>`

Checks before next step:

- Make sure the final image is complete and usable.
- Make sure the final banner matches the design specs closely.

---

## Final deliverable

- `final_banner_image`
- Preview location: `examples/assets/final_banner_image/`
- If needed for large media: link the final file externally and keep only lightweight preview media in this repo.
