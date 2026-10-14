# CSS compatibility audit

Litos requires Obsidian 1.13.7 or later. The verified desktop installation uses Electron 39.8.3 / Chromium 142.0.7444.265. The local compatibility target is therefore Electron 39, rather than inferring an installer version solely from the app version. Mobile engines have not been verified by this audit.

## Run

```sh
npm ci
npm run lint:compat
```

This focused audit uses the official Obsidian Stylelint rules for browser features, unknown element selectors, and important declarations. It does not replace the complete marketplace review. The full standard configuration also reports existing formatting/style issues outside this change.

## Changes and evidence

- Raised the declared minimum from 1.0.0 to 1.13.7, the tested app version. This changes eligibility for older installations; it does not modify the current visual design.
- Added standard mask declarations alongside the existing prefixed declarations. The three custom task icons retain identical computed mask images, sizes, and dimensions.
- Replaced the tab row's `column-gap: 6px` with `gap: normal 6px`. Both computed gaps remain identical. The browser-feature scanner had categorized the former as multicolumn even though this is a flex row.
- Retained scrollbar rules. With the verified engine target, the scrollbar compatibility warning no longer appears; removing a working platform fallback is unnecessary.
- Allowed only `mjx-stretchy-h` and `mjx-ext` in the local unknown-element check. They are MathJax-generated elements, and the theme's formula styling is unchanged.

## Remaining warnings

The original three-rule audit against Electron 25 reproduced 38 warnings: 29 style container queries, four masks, one multicolumn, one scrollbar, one important declaration, and two MathJax element selectors.

The updated local audit reports 30 warnings and zero errors:

- **29 style container queries:** the feature database classifies the overall feature as partially supported, including newer Chromium versions. Litos uses custom-property queries to position and size sidenotes. Those queries have not been rewritten or globally suppressed.
- **One important declaration:** Obsidian sets `contain: paint !important` on non-editable editor widgets. The existing `contain: none !important` prevents Live Preview sidenotes from being clipped. Greater selector specificity alone cannot override an important declaration with a normal one.

The marketplace may use a different engine target or ignore local rule configuration. Do not promise the same warning count there. Raising the manifest minimum does not by itself eliminate the partial-support container-query warning.

Use the showcase preview workflow to compare actual rendering before publishing. Future formula or sidenote layout changes additionally need dedicated formula, narrow-window, and left/right sidenote checks.
