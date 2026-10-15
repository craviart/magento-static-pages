# Review previews

The review preview is the visual and interaction feedback surface before CMS implementation. It is not Magento validation.

Keep `review/index.html` beside the canonical handoff artifacts. It renders the same CMS fragment structure and loads the same delivered CSS and optional JavaScript. It may add a document shell and replace only Magento media directives with corresponding local review-asset paths.

Generate the preview from canonical sources or a deterministic helper. Do not maintain a separate handcrafted version. Apply feedback to the fragment, style widget, script widget, or delivered assets, then regenerate the review page. State the preview entry point and regeneration command in `handoff.md`.
