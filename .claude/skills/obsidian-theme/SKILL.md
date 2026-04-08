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

Every styling task MUST follow this workflow. Do not skip steps — each step is backed by the Obsidian CLI to ensure changes are evidence-based.

### Step 1: Inspect — Understand the DOM structure

Before writing any CSS, use the Obsidian CLI to inspect the actual DOM of the target element:

```bash
# Inspect DOM structure of the element
obsidian dev:dom selector=".image-embed"

# Trace the full parent chain to understand nesting context
obsidian eval 'code=(function() {
  const leaves = app.workspace.getLeavesOfType("markdown");
  for (const leaf of leaves) {
    const el = leaf.view.containerEl;
    const target = el.querySelector("<SELECTOR>");
    if (!target) continue;
    let chain = []; let node = target;
    for (let i = 0; i < 12 && node; i++) {
      let cn = String(node.className || "").trim().split(/\s+/).slice(0,4).join(".");
      chain.unshift(node.tagName.toLowerCase() + (cn ? "." + cn : ""));
      if (node.classList && node.classList.contains("cm-editor")) break;
      node = node.parentElement;
    }
    return chain.join("\n  > ");
  }
  return "not found";
})()'

# Check computed styles on the element
obsidian eval 'code=(function() {
  const leaves = app.workspace.getLeavesOfType("markdown");
  for (const leaf of leaves) {
    const el = leaf.view.containerEl;
    const target = el.querySelector("<SELECTOR>");
    if (!target) continue;
    const s = window.getComputedStyle(target);
    return "display: " + s.display + "\nposition: " + s.position
      + "\nmargin: " + s.margin + "\nwidth: " + s.width
      + "\ntext-align: " + s.textAlign;
  }
  return "not found";
})()'
```

IMPORTANT: Inspect in BOTH modes. The DOM is completely different between Reading mode and Live Preview:
- **Reading mode**: standard HTML (`<p>`, `<h1>`, `<span>`) inside `.markdown-preview-view`
- **Live Preview**: CodeMirror 6 widgets inside `.cm-content` (a `contenteditable` div — `margin: auto` may not work here; use `transform` centering instead)

Check which mode is active:
```bash
obsidian eval 'code=(function() {
  const leaves = app.workspace.getLeavesOfType("markdown");
  for (const leaf of leaves) {
    const el = leaf.view.containerEl;
    const sv = el.querySelector(".markdown-source-view");
    if (sv) return "Live Preview: " + sv.classList.contains("is-live-preview")
      + "\nSource mode: " + !sv.classList.contains("is-live-preview");
    const pv = el.querySelector(".markdown-preview-view");
    if (pv) return "Reading mode";
  }
  return "unknown";
})()'
```

### Step 2: Identify CSS targets

Based on the DOM inspection from Step 1:
- First check `references/css-variables.md` — if a variable controls the property, just override the variable (it applies across all modes automatically).
- If a custom selector is needed, write selectors for BOTH Reading mode and Live Preview based on the actual DOM chains observed in Step 1.

### Step 3: Write the CSS

Edit `theme.css` with the CSS changes.

### Step 4: Verify — Screenshot and measure in BOTH modes

After editing, reload the theme and verify visually:

```bash
# Reload theme CSS
obsidian eval 'code=(function() { app.customCss.loadCss(); return "reloaded"; })()'

# Take a screenshot to visually verify
obsidian dev:screenshot path=/tmp/obsidian-verify.png

# Programmatically verify positioning/sizing
obsidian eval 'code=(function() {
  const leaves = app.workspace.getLeavesOfType("markdown");
  for (const leaf of leaves) {
    const el = leaf.view.containerEl;
    const target = el.querySelector("<SELECTOR>");
    if (!target) continue;
    target.scrollIntoView();
    const s = window.getComputedStyle(target);
    return "display: " + s.display + "\nmargin: " + s.margin
      + "\nwidth: " + s.width + "\ntext-align: " + s.textAlign;
  }
  return "not found";
})()'
```

Switch between modes and verify both:
```bash
# Switch to Reading mode
obsidian eval 'code=(function() {
  const leaf = app.workspace.getActiveViewOfType(app.viewRegistry.typeMap["markdown"]);
  if (!leaf) return "no active markdown view";
  leaf.setState({ mode: "preview" }, {});
  return "switched to reading mode";
})()'

# Switch to Live Preview
obsidian eval 'code=(function() {
  const leaf = app.workspace.getActiveViewOfType(app.viewRegistry.typeMap["markdown"]);
  if (!leaf) return "no active markdown view";
  leaf.setState({ mode: "source", source: false }, {});
  return "switched to live preview";
})()'
```

### Step 5: Iterate if needed

If verification fails, go back to Step 1 (re-inspect DOM — the structure may differ from assumptions) or Step 3 (adjust CSS). Do not guess — always re-inspect.

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

## Debugging with Obsidian CLI

The Obsidian CLI is the primary debugging tool. Always use it instead of asking the user to manually inspect DevTools.

### Quick Reference

```bash
# DOM inspection
obsidian dev:dom selector="<CSS_SELECTOR>"

# Computed styles
obsidian dev:css selector="<CSS_SELECTOR>"

# Screenshot (for visual verification)
obsidian dev:screenshot path=/tmp/obsidian-debug.png

# Run arbitrary JS (for DOM traversal, style checks, mode switching)
obsidian eval 'code=<JAVASCRIPT_EXPRESSION>'

# Reload theme after CSS changes
obsidian eval 'code=(function() { app.customCss.loadCss(); return "reloaded"; })()'
```

### Common Debugging Patterns

**Find all CSS rules matching an element:**
```bash
obsidian eval 'code=(function() {
  const el = document.querySelector("<SELECTOR>");
  if (!el) return "not found";
  const rules = [];
  for (const sheet of document.styleSheets) {
    try {
      for (const r of sheet.cssRules) {
        if (el.matches(r.selectorText || "")) {
          rules.push(r.selectorText + " { " + r.style.cssText.substring(0,120) + " }");
        }
      }
    } catch(e) {}
  }
  return rules.join("\n");
})()'
```

**Test CSS injection before committing to theme.css:**
```bash
obsidian eval 'code=(function() {
  const s = document.createElement("style");
  s.id = "debug-test";
  s.textContent = "<CSS_RULES>";
  document.head.appendChild(s);
  return "injected";
})()'
```

### Fallback: Manual DevTools

If the CLI cannot achieve what is needed, guide the user through manual DevTools:
1. Open DevTools: `Cmd+Option+I` (macOS) / `Ctrl+Shift+I` (Windows/Linux)
2. Inspect mode: `Cmd+Shift+C` / `Ctrl+Shift+C`, click the target element
3. Read the Styles panel for all CSS rules affecting the element

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
4. **Always target both view modes** — Every CSS rule using custom selectors MUST include both `.markdown-preview-view` (reading mode) and `.markdown-source-view` (live preview / editing mode) selectors to ensure visual consistency. Never write a rule for one mode without the other.
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

## Known Gotchas

Lessons learned from real debugging sessions. Check this section before assuming standard CSS approaches will work.

| Gotcha | Detail |
|---|---|
| **`margin: auto` fails in Live Preview** | `.cm-content` is a `contenteditable` div. Block children with `margin: 0 auto` compute to `margin: 0`. Use `position: relative; left: 50%; transform: translateX(-50%)` instead. |
| **Image embeds have different DOM per mode** | Reading mode: `p > span.image-embed`. Live Preview standalone: `div.cm-content > div.image-embed` (direct child, no `<p>` wrapper). Always inspect both with CLI. |
| **`![[image]]` renders as `<span>`, not `<img>`** | Obsidian wraps images in `<span class="internal-embed media-embed image-embed">`. Selectors targeting bare `img` or `p > img` won't match wikilink-style embeds. |
| **Live Preview images have `display: flex` and `width: fit-content`** | The `.image-embed` div in CM6 is a flex container. `text-align: center` on it has no effect since the container shrinks to content width. |
| **Theme CSS reload requires explicit call** | Editing `theme.css` on disk does NOT auto-reload. Run `obsidian eval 'code=app.customCss.loadCss()'` or press `Cmd+R` in Obsidian. |
