# Media and assets

Agree the target media directory and filenames before generating the handoff. A reusable default is `wysiwyg/landing-pages/<year>/<page-slug>/`, but an established project convention takes priority.

Use the final Magento media directive for every campaign-owned image, responsive source, video poster, or equivalent media URL in the CMS fragment:

```html
<img src="{{media url=&quot;wysiwyg/landing-pages/2026/spring-launch/hero-desktop.webp&quot;}}" alt="Product arrangement on a pale background">
```

Use meaningful approved alt text. Decorative imagery uses `alt=""`. Deliver raster files sized to their largest actual display slot at up to 2x density. Preserve intentional baked-in framing rather than adding duplicate CSS cropping, borders, or radius.

The handoff asset manifest must include source and delivered filenames, final Magento path, exact media directive, dimensions, file weight, alt text, treatment notes, and upload owner. The uploader places each delivered file at that path without renaming it.
