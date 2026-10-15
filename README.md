# Magento Static Pages

Prepare approved static pages as safe, reviewable Magento CMS handoffs. The skill creates isolated CMS HTML fragments, fully scoped CSS widgets, optional page-specific JavaScript, asset manifests, and browser-review previews without duplicating Magento-owned site behaviour.

## Install

```sh
npx skills add https://github.com/craviart/magento-static-pages
```

## Try it

- "Use $magento-static-pages to turn this approved campaign page into a Magento CMS handoff."
- "Audit these Magento CMS widget fragments for isolation, asset-path, and accessibility problems."
- "Update this static page handoff for a new store view and regenerate its review preview."
- "Prepare a Magento-safe informational page with scoped CSS and a developer handoff note."

## What it covers

The skill is for campaign, landing, informational, and form-adjacent static pages. It intentionally does not cover Magento theme development, catalog, price or stock integration, checkout, payment, deployment, or production administration.

## Package contents

- `SKILL.md`: modes, guardrails, deliverables, and workflow.
- `references/`: Magento ownership, media handling, review-preview, and acceptance guidance.
- `scripts/validate_handoff.py`: dependency-free, read-only structural validator.
- `fixtures/`: a neutral compliant handoff plus deliberately invalid inputs used to exercise the validator.
- `agents/openai.yaml`: discovery metadata for Codex.

## Validation

Validate a handoff before sharing it with a Magento developer:

```sh
python3 scripts/validate_handoff.py \
  --html campaign-magento-fragment.html \
  --css campaign-magento-style.html \
  --root campaign-page \
  --script campaign-magento-script.html
```

The validator catches structural violations. It does not prove visual fidelity, accessibility quality, asset upload success, or Magento runtime behaviour. Review the generated `review/index.html` at desktop and narrow widths, then have the Magento owner verify the final CMS placement.

## Licence

[MIT](LICENSE) © Camille Raviart
