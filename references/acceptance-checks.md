# Acceptance checks

Before delivery, confirm:

- The fragment has exactly one top-level namespaced `<div>` and no document shell, shared chrome, widget tags, inline styles, inline event handlers, or scripts.
- The CSS widget has exactly one `<style>` wrapper, every selector begins with the exact root selector, and all font sizes use fixed pixels.
- The first section is flush with Magento-owned chrome unless the approved design documents a specific exception.
- The campaign root is full-width and has no `max-width`. Full-bleed sections remain full-width. Any constrained layout uses an explicit inner container with `margin-inline: auto`; a bounded wrapper without automatic inline margins fails unless the approved design documents an asymmetric composition.
- `handoff.md` identifies the target-theme or approved-design source for desktop width and gutters, the campaign container selector, and any asymmetric-layout exception.
- The optional script has exactly one `<script>` wrapper, exits when the root is absent, and queries descendants from the root.
- Every campaign asset has a matching Magento media directive and manifest row.
- The review page shares canonical handoff structure, styles, and behaviour, using local media only for the review surface.
- Review the complete page and each hero or grid crop at 1440px, 1920px, and a narrow width. At desktop widths, constrained content must be centred within a small rendering tolerance, declared grid tracks must be occupied, and there must be no unexplained blank column, clipped stage, or unused container area. Structural validation, visual review, and Magento runtime verification are reported separately.
