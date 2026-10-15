# Spring launch handoff

## Placement

- Paste `spring-launch-magento-fragment.html` into the approved Magento CMS content field.
- Paste `spring-launch-magento-style.html` into the page's approved CSS widget or asset block.
- Paste `spring-launch-magento-script.html` into the approved JavaScript widget only if the page-specific ready state is needed.
- Root selector and namespace: `.spring-launch-page`.

## Assets

| Delivered file | Final Magento path | Media directive | Dimensions | Alt text | Upload owner |
| --- | --- | --- | --- | --- | --- |
| `hero-illustration.svg` | `wysiwyg/landing-pages/2026/spring-launch/hero-illustration.svg` | `{{media url=&quot;wysiwyg/landing-pages/2026/spring-launch/hero-illustration.svg&quot;}}` | 1200 × 600 | A carefully arranged seasonal collection | Magento content owner |

The SVG is a neutral fixture illustration. The real campaign asset, final path, dimensions, and upload owner must replace this row before production use.

## Review

Open `review/index.html` from the `fixtures/compliant` directory through a local web server. It uses the same structure and styles as the delivered widgets while substituting the Magento media directive with `hero-illustration.svg`.

## Open contracts

- The Magento owner confirms the destination CMS page and live collection route.
- The Magento owner confirms whether the page needs production analytics or consent-gated interaction.
