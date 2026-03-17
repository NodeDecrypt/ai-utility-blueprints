---
name: Bug report
about: Report a problem with a blueprint, tool, schema, or repo structure in Node Decrypt Community
title: "[Bug] "
labels: ["bug"]
assignees: []
---

## What kind of bug is this?

Select one or more:

- [ ] Blueprint problem
- [ ] Tool problem
- [ ] Schema problem
- [ ] Repo structure problem
- [ ] Documentation problem
- [ ] Validation problem
- [ ] Other

---

## Where is the problem?

Please include the exact file or folder if possible.

Examples:

- `blueprints/banner-design/v1/blueprint.json`
- `tools/google-flow/v1/tool.json`
- `schemas/blueprint.schema.json`

---

## What did you expect?

Describe the expected behavior or structure.

---

## What happened instead?

Describe the actual problem.

Examples:

- invalid field name
- missing required folder
- wrong schema value
- broken reference
- inconsistent version reference
- README does not match the JSON
- validation fails unexpectedly

---

## Steps to reproduce

List the steps clearly.

Example:

1. open the file
2. validate against the schema
3. see the error on `tool_refs`
4. compare with the template

---

## If this is a blueprint bug

Please answer if relevant:

- which asset or step is wrong?
- which `tool_key` is involved?
- which version is affected?

---

## If this is a tool bug

Please answer if relevant:

- which `tool_key` is affected?
- which version is affected?
- is the issue in `resource_setups`, `input_capabilities`, or `output_capabilities`?

---

## Severity

Select one:

- [ ] Minor
- [ ] Moderate
- [ ] Major

---

## Public-safety check

Confirm that your report does **not** expose any of the following:

- private URLs
- selectors
- cookies
- tokens
- auth/session data
- internal-only documents
- secret prompts or private automation logic

- [ ] Confirmed

---

## Extra notes

Add screenshots, error text, or extra context here if helpful.
