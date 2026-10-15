# Acceptance checks

Before delivery, confirm:

- The fragment has exactly one top-level namespaced `<div>` and no document shell, shared chrome, widget tags, inline styles, inline event handlers, or scripts.
- The CSS widget has exactly one `<style>` wrapper, every selector begins with the exact root selector, and all font sizes use fixed pixels.
- The first section is flush with Magento-owned chrome unless the approved design documents a specific exception.
- The optional script has exactly one `<script>` wrapper, exits when the root is absent, and queries descendants from the root.
- Every campaign asset has a matching Magento media directive and manifest row.
- The review page shares canonical handoff structure, styles, and behaviour, using local media only for the review surface.
- Desktop and narrow review are visually approved. Structural validation, visual review, and Magento runtime verification are reported separately.
