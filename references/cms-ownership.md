# CMS ownership boundaries

Magento owns site-level header and footer chrome, navigation, account state, mini-cart, routing, catalog data, price, stock, cart, checkout, SEO, robots settings, consent, and production analytics unless a written integration contract assigns a specific responsibility differently.

Static-page handoffs may render approved campaign content and page-specific interaction only. They must not create static stand-ins for Magento data or site services. When a page needs a URL, product data, form endpoint, tracking event, consent rule, or service integration that is not supplied, record it as unresolved in `handoff.md` with its owner.

Place HTML only in the approved Magento CMS content field. Place CSS and optional JavaScript in their separately approved widgets or asset blocks, not inline in the CMS HTML content.
