---
name: magento-static-pages
description: Prepare approved static pages for Magento CMS as isolated HTML, CSS, and optional JavaScript handoffs. Use for campaigns, landing pages, informational pages, and form-adjacent static surfaces, not theme, catalog, checkout, or deployment work.
---

# Magento static pages

Turn an approved static-page design into a reviewable, paste-ready Magento CMS handoff without replacing Magento-owned site behaviour.

## Operating rules

- Discover the approved design, target store views, asset ownership, Magento media-path convention, and unresolved platform contracts before creating a handoff.
- Magento owns shared chrome, routing, catalog data, price, stock, cart, checkout, customer state, SEO, robots, consent, and production analytics. Do not replace, simulate, or hardcode them without an approved integration contract.
- Deliver one page-specific HTML root, one separately wrapped and fully scoped CSS widget, and JavaScript only for genuine page interaction. Keep the standalone browser review separate from the Magento payload.
- Keep controls semantic and keyboard-operable. Use links for navigation and buttons for actions. Provide visible focus styles and explicit labels.
- Lock final asset filenames and media paths before generating the fragment. Use Magento media directives in the CMS fragment, and list every asset, alt text, dimensions, file weight, treatment note, final path, and upload owner in the handoff note.
- Keep every selector, state class, custom event, storage key, and data attribute page-namespaced. Do not use global selectors, generic classes, inline styles, inline handlers, or document-level widget queries after the root is found.
- Treat Magento's CMS insertion point as available canvas, not as a guaranteed content container. Derive the desktop content width and gutters from the target theme or approved design, keep the campaign root and full-bleed sections at the available width, and constrain content only in explicit, centred inner containers.
- Before delivery, run `python3 scripts/validate_handoff.py` and inspect the review page. A passing validator verifies structural rules only, not visual fidelity or Magento runtime integration.

## Choose the mode

- **New handoff**: create a complete CMS-ready package from an approved static-page design.
- **Adaptation**: update an existing handoff while preserving its root namespace, Magento contracts, and asset manifest unless a contract changed.
- **Audit**: inspect a supplied handoff without changing it; report structural failures, ownership risks, and unresolved contracts.
- **Maintenance**: refresh assets, copy, store views, or interaction details and regenerate the review page from the canonical handoff sources.

## Required deliverables

For each page, produce:

1. `<page>-magento-fragment.html`: exactly one page-specific root `<div>` and no document shell, shared chrome, widget tags, inline code, or content outside the root.
2. `<page>-magento-style.html`: exactly one `<style>` element. Every selector must begin with the root class; every `font-size` must be a fixed pixel value.
3. `<page>-magento-script.html`: exactly one `<script>` element, only if page-specific interaction exists. It must no-op when its root is absent and query descendants from that root.
4. `handoff.md`: placement instructions, root selector, asset manifest, final media paths, upload owner, review entry point, regeneration command, target-theme container source, and unresolved contracts with owners.
5. `review/index.html`: a browser-reviewable rendering of the same fragment structure and canonical styles or behaviour, with local review assets substituted only in that review surface.

Read [CMS ownership boundaries](references/cms-ownership.md) before working on a new integration, [media and assets](references/media-and-assets.md) before locking image paths, [review previews](references/review-previews.md) before creating a review surface, and [acceptance checks](references/acceptance-checks.md) before delivery.

## Standard workflow

1. Map the approved page and existing Magento contracts. Name unresolved routes, data, consent, form, analytics, or store-view decisions and their owners.
2. Choose a distinctive root class such as `spring-launch-page`; use it for all classes and runtime identifiers.
3. Produce the canonical fragment, style widget, optional script widget, assets, and handoff manifest. Do not build a second manually maintained preview implementation.
4. Generate the review page from the canonical sources and replace Magento media directives only for local review.
5. Validate the artifacts, review at 1440px, 1920px, and a narrow width, then report structural validation separately from visual review and runtime work still owned by Magento.
