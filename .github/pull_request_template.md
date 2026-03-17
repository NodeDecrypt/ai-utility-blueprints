## Summary

Describe what this PR adds or changes.

Examples:

- adds a new blueprint
- adds a new tool
- adds a new version of an existing blueprint
- improves examples
- fixes schema-safe documentation wording

---

## Type of change

Select all that apply:

- [ ] New blueprint
- [ ] New blueprint version
- [ ] New tool
- [ ] New tool version
- [ ] Docs improvement
- [ ] Example improvement
- [ ] Schema-safe cleanup

---

## What was added or changed

List the main files or folders changed.

Examples:

- `blueprints/banner-design/v1/`
- `tools/google-flow/v1/`
- `templates/blueprint.template.json`

---

## Checklist

- [ ] I followed the repo structure
- [ ] Folder names use `kebab-case`
- [ ] JSON keys use `snake_case`
- [ ] I did not include secrets, tokens, cookies, auth data, or private internal details
- [ ] My JSON matches the schema
- [ ] My blueprint or tool version folder is correct
- [ ] I included the expected README file
- [ ] I included examples where helpful
- [ ] My content is public-safe and community-safe

---

## For blueprint contributions

- [ ] I included `README.md`
- [ ] I included `blueprint.json`
- [ ] I included `examples/`
- [ ] I included `preview/` if available
- [ ] My `tool_refs` point to valid tool versions
- [ ] My step `tool_key` values match the declared `tool_refs`
- [ ] My step `inputs` and `outputs` match declared asset keys
- [ ] My `final_deliverables` match declared asset keys

---

## For tool contributions

- [ ] I included `README.md`
- [ ] I included `tool.json`
- [ ] I included `resources/single/`
- [ ] I included `resources/manifests/`
- [ ] My `usage_type` is valid
- [ ] My resource and capability structures are valid
- [ ] My tool content is reusable and not blueprint-specific

---

## Notes for reviewers

Add any context that would help reviewers.

Examples:

- why a new version was needed
- whether a tool is meant to replace an older one
- what is intentionally left out
- any known limitations
