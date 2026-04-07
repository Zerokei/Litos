---
name: obsidian-theme
description: >
  Develop and customize Obsidian themes and CSS snippets.
  TRIGGER when: editing theme.css or CSS files, user shows screenshots of Obsidian UI, user asks
  about styling/appearance of any Obsidian element (headings, callouts, links, tables, checkboxes,
  code blocks, tags, fonts, colors, spacing, sidebars, tabs), user mentions CSS variables/selectors,
  or user asks to fix/debug visual issues in Obsidian.
  DO NOT TRIGGER when: question is about Obsidian plugin JS/TS code or markdown content, not styling.
---

# Obsidian Theme Development

This skill helps you write, debug, and iterate on Obsidian CSS — whether it's a single snippet or a full theme.

## Core Workflow

Every styling task follows the same pattern:

1. **Understand the request** — What does the user want to change? Which elements are involved?
2. **Identify CSS targets** — Find the right CSS variables or selectors. Prefer variables over raw selectors (they're more stable across Obsidian updates and don't fight with other themes/snippets).
3. **Write the CSS** — Produce clean, minimal CSS that achieves the goal.
4. **Guide debugging** — If the result doesn't look right, help the user inspect elements with DevTools to find the correct selectors.

## Deciding: Variable Override vs Custom Selector

Obsidian exposes 400+ CSS variables. Before writing a custom selector, check `references/css-variables.md` to see if a variable already controls what the user wants to change. Variables are the preferred approach because:

- They work consistently across reading mode, editing mode, and live preview
- They don't break when Obsidian updates its DOM structure
- They compose well with other themes and snippets

Use custom selectors only when variables can't achieve the desired effect — for example, adding pseudo-elements, complex hover effects, or targeting very specific elements that have no variable.

## Reading Mode vs Editing Mode

This is one of the trickiest parts of Obsidian theming. The DOM structure is completely different between modes, so CSS that works in one mode often doesn't work in the other.

**Reading mode** (rendered markdown):
```css
.markdown-preview-view h1,
.markdown-rendered h1 {
  /* styles for rendered headings */
}
```

**Editing mode / Live Preview** (CodeMirror 6 editor):
```css
.markdown-source-view.mod-cm6 .cm-header-1 {
  /* styles for editor headings */
}
```

**Live Preview specifically** (not source mode):
```css
.markdown-source-view.is-live-preview .cm-header-1 {
  /* only in live preview, not raw source */
}
```

**Both modes** — when the user says "change heading style", they almost always mean both. Write selectors for both:
```css
/* Reading mode */
.markdown-rendered h1 { color: var(--color-red); }
/* Editing mode */
.markdown-source-view.mod-cm6 .cm-header-1 { color: var(--color-red); }
```

But if a CSS variable controls the property (like `--h1-color`), just set the variable — it applies everywhere automatically.

See `references/selectors-guide.md` § "Mode-Specific Selectors" for the full reference.

## Light and Dark Mode

Always consider both themes. Define color-specific values under `.theme-light` and `.theme-dark`:

```css
.theme-light {
  --my-custom-bg: #f5f5f5;
}
.theme-dark {
  --my-custom-bg: #2a2a2a;
}
```

General (non-color) properties like font-family, font-size, spacing can go on `body`.

## CSS Snippet vs Full Theme

**CSS Snippet** — a single `.css` file in `<vault>/.obsidian/snippets/`. Best for:
- Targeted tweaks (change heading colors, hide status bar, restyle callouts)
- Modifications that layer on top of any theme
- Quick experiments

**Full Theme** — a `theme.css` + `manifest.json` in `<vault>/.obsidian/themes/<Name>/`. Best for:
- Comprehensive visual overhauls
- Publishing to the Obsidian community gallery
- When you need to override many variables at once

### Full Theme Structure

```
<vault>/.obsidian/themes/MyTheme/
├── manifest.json
└── theme.css
```

**manifest.json:**
```json
{
  "name": "My Theme",
  "version": "1.0.0",
  "minAppVersion": "1.0.0",
  "author": "Author Name",
  "authorUrl": "https://example.com"
}
```

After creating the files, enable the theme in Settings > Appearance.

## Debugging with DevTools

When you're not sure which selector or variable controls an element, guide the user through DevTools:

1. **Open DevTools**: `Cmd+Option+I` (macOS) or `Ctrl+Shift+I` (Windows/Linux)
2. **Inspect element**: `Cmd+Shift+C` / `Ctrl+Shift+C`, then click the element
3. **Read the Styles panel**: Shows all CSS rules affecting the element, including which variables are used
4. **Live-edit**: Change values in the Styles panel to test — changes are temporary
5. **Copy the selector**: Once you've found the right target, copy it into your snippet/theme

For debugging via the Obsidian CLI (if available):
- `obsidian dev:dom selector=".cm-header-1"` — inspect DOM structure
- `obsidian dev:css selector=".cm-header-1"` — view computed styles
- `obsidian dev:screenshot` — capture current state

## Style Settings Plugin Integration

The [Style Settings](https://github.com/mgmeyers/obsidian-style-settings) plugin lets users adjust theme options through a settings UI instead of editing CSS manually. Add a `/* @settings */` block to make variables user-configurable:

```css
/* @settings
name: My Theme Settings
id: my-theme-settings
settings:
  -
    id: heading-color
    title: Heading Color
    description: Color for all headings
    type: variable-color
    format: hex
    default: '#333333'
  -
    id: body-font-size
    title: Body Font Size
    type: variable-number-slider
    default: 16
    min: 12
    max: 24
    step: 1
    format: px
  -
    id: fancy-callouts
    title: Fancy Callouts
    description: Enable decorative callout styling
    type: class-toggle
    default: false
*/
```

**Setting types:** `variable-color`, `variable-themed-color` (separate light/dark), `variable-number`, `variable-number-slider`, `variable-text`, `variable-select`, `class-toggle`, `class-select`, `heading`, `info-text`, `color-gradient`.

See `references/selectors-guide.md` § "Style Settings Plugin" for complete type documentation.

## Font Embedding

Obsidian themes must bundle fonts locally (no remote URLs for published themes). Embed as base64:

```css
@font-face {
  font-family: 'MyFont';
  src: url('data:font/woff2;base64,<BASE64_DATA>') format('woff2');
  font-weight: 400;
  font-style: normal;
}
body {
  --font-text-theme: 'MyFont', sans-serif;
}
```

For snippets used locally, external font imports (Google Fonts, CDN) are fine.

## Writing Good Theme CSS

1. **Use CSS variables** — Override Obsidian's built-in variables instead of writing raw selectors where possible
2. **Keep specificity low** — Avoid deeply nested selectors and `!important`. Low specificity lets users override your theme with snippets
3. **Don't use `:has()`** — Prohibited by Obsidian's developer policies
4. **Test both modes** — Always verify in reading mode AND editing mode
5. **Test both themes** — Check light and dark mode
6. **Use Obsidian's spacing system** — `var(--size-4-2)` (8px), `var(--size-4-4)` (16px), etc. instead of arbitrary pixel values
7. **Use Obsidian's color system** — `var(--color-red)`, `var(--text-normal)`, etc. instead of hardcoded colors

## Reference Files

- **`references/css-variables.md`** — Complete reference of all 400+ Obsidian CSS variables, organized by category (colors, typography, editor elements, components, window). Consult this when you need to find the right variable for a specific property.

- **`references/selectors-guide.md`** — Key CSS selectors organized by UI area, mode-specific selector patterns, theme guidelines, DevTools debugging workflow, Style Settings plugin documentation, and font embedding details. Consult this when you need to target specific DOM elements or understand the selector structure.

## Common Tasks Quick Reference

| Task | Approach |
|---|---|
| Change heading size/color/font | Override `--h1-size`, `--h1-color`, `--h1-font`, etc. |
| Change body font | Set `--font-text-theme` on `body` |
| Change accent color | Override `--accent-h`, `--accent-s`, `--accent-l` |
| Change background | Override `--background-primary`, `--background-secondary` |
| Style callouts | Use `--callout-*` variables or `[data-callout="type"]` selectors |
| Style checkboxes | Use `--checkbox-*` variables or `[data-task="x"]` selectors |
| Style tables | Use `--table-*` variables |
| Style code blocks | Use `--code-*` and syntax highlighting variables |
| Style links | Use `--link-*` variables |
| Style tags | Use `--tag-*` variables |
| Hide UI elements | `display: none` on `.status-bar`, `.workspace-ribbon`, etc. |
| Custom scrollbars | Target `::-webkit-scrollbar` and related pseudo-elements |
| Tab styling | Target `.workspace-tab-header` and related classes |
