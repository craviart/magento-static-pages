# Media and assets

Confirm the exact target media directory and filenames with the Magento owner before generating the handoff. Preserve capitalization and subfolder structure exactly. `wysiwyg/landing-pages/<year>/<page-slug>/` is only an example, not a path contract. If the destination is unknown, record it as unresolved rather than calling the fragment paste-ready.

Confirm which file types the target Magento uploader accepts before optimizing and naming assets. Browser support does not imply upload support. Use JPEG for photography and PNG for transparency when modern-format support is unknown. Use WebP or SVG only when the Magento owner confirms that upload and delivery are supported. Check that each delivered file's actual type matches its extension.

Use the final Magento media directive for every campaign-owned image, responsive source, video poster, or equivalent media URL in the CMS fragment:

```html
<img src="{{media url=&quot;wysiwyg/landing-pages/2026/spring-launch/hero-desktop.jpg&quot;}}" alt="Product arrangement on a pale background">
```

Use meaningful approved alt text. Decorative imagery uses `alt=""`. Deliver raster files sized to their largest actual display slot at up to 2x density. Preserve intentional baked-in framing rather than adding duplicate CSS cropping, borders, or radius.

Verify which attributes the target CMS processes. If Magento media directives inside `srcset`, `data-src`, or CSS `url()` are unverified, use a direct `src` for essential images and document any CSS asset that needs a published theme URL. First-render imagery and carousel slides must not depend solely on a deferred attribute. Put image markup in the HTML fragment rather than JavaScript-generated strings unless directive processing inside the script widget has been verified.

The handoff asset manifest must include source and delivered filenames, final Magento path, exact media directive, dimensions, file weight, alt text, treatment notes, and upload owner. The uploader places each delivered file at that path without renaming it.
