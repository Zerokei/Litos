# Obsidian Selectors & Theme Development Guide

## Table of Contents

1. [Theme Structure](#theme-structure)
2. [Key Selectors](#key-selectors)
3. [Mode-Specific Selectors](#mode-specific-selectors)
4. [Theme Guidelines](#theme-guidelines)
5. [Debugging Workflow](#debugging-workflow)
6. [Style Settings Plugin](#style-settings-plugin)
7. [Font & Image Embedding](#font--image-embedding)

---

## Theme Structure

### File Layout

```
<vault>/.obsidian/themes/MyTheme/
├── manifest.json    (required)
└── theme.css        (required)
```

### manifest.json

```json
{
  "name": "My Theme",
  "version": "1.0.0",
  "minAppVersion": "1.0.0",
  "author": "Author Name",
  "authorUrl": "https://example.com",
  "fundingUrl": "https://buymeacoffee.com/author"
}
```

### CSS Loading Order (lowest to highest priority)

1. `app.css` — Obsidian's defaults
2. `theme.css` — Active theme
3. CSS snippets — User snippets (`.obsidian/snippets/*.css`)
4. Plugin styles — Community plugin CSS

### Hot-Reload Development Workflow

1. Create theme directory in `.obsidian/themes/`
2. Enable in Settings > Appearance > Themes
3. Edit `theme.css`
4. Reload: `Ctrl+R` / `Cmd+R` (or use Hot-Reload plugin for auto-refresh)

---

## Key Selectors

### Body & Platform Classes

```css
body                          /* Root element */
body.theme-light              /* Light mode */
body.theme-dark               /* Dark mode */
body.is-mobile                /* Mobile device */
body.is-tablet                /* Tablet device */
body.is-desktop               /* Desktop */
body.is-phone                 /* Phone */
body.mod-macos                /* macOS */
body.mod-windows              /* Windows */
body.mod-linux                /* Linux */
body.is-fullscreen            /* Fullscreen mode */
body.is-focused               /* App has focus */
body.is-frameless             /* Custom titlebar mode */
body.is-hidden-frameless      /* Frameless with hidden titlebar */
body.is-maximized             /* Window maximized */
```

### Workspace Structure

```css
.workspace                        /* Entire workspace */
.workspace-split                  /* Split container */
.workspace-split.mod-root         /* Main editor area */
.workspace-split.mod-left-split   /* Left sidebar */
.workspace-split.mod-right-split  /* Right sidebar */

.workspace-tabs                   /* Tab group container */
.workspace-tabs.mod-top           /* Tabs at top */
.workspace-tabs.mod-stacked       /* Stacked tabs mode */

.workspace-tab-header-container   /* Tab bar */
.workspace-tab-header             /* Individual tab */
.workspace-tab-header.is-active   /* Active tab */

.workspace-leaf                   /* Individual pane */
.workspace-leaf-content           /* Pane content area */
.workspace-leaf-content[data-type="markdown"]  /* Markdown pane */
.workspace-leaf-content[data-mode="source"]    /* Source editing */
.workspace-leaf-content[data-mode="preview"]   /* Reading mode */
```

### Ribbon & Sidebar

```css
.workspace-ribbon               /* Left ribbon (icon bar) */
.workspace-ribbon.mod-left      /* Left ribbon */
.workspace-ribbon.is-collapsed  /* Collapsed ribbon */
.side-dock-actions              /* Plugin icons in ribbon */
.side-dock-settings             /* Bottom settings icons */
.sidebar-toggle-button          /* Sidebar toggle */

/* File Explorer */
.nav-folder                     /* Folder item */
.nav-folder-title               /* Folder name */
.nav-file                       /* File item */
.nav-file-title                 /* File name */
.nav-file-title.is-active       /* Currently open file */
```

### View Header

```css
.view-header                    /* Pane header bar */
.view-header-title              /* Note title in header */
.view-header-title-container    /* Title container */
.view-actions                   /* Header action buttons */
```

### Status Bar

```css
.status-bar                     /* Bottom status bar */
.status-bar-item                /* Individual status item */
```

### Editor Content Elements

```css
/* Headings (reading mode) */
.markdown-rendered h1 through h6

/* Headings (editing mode) */
.cm-header, .cm-header-1 through .cm-header-6

/* Links */
a.internal-link                 /* Internal link (reading mode) */
a.external-link                 /* External link (reading mode) */
.cm-hmd-internal-link           /* Internal link (editing mode) */
.cm-url                         /* URL (editing mode) */

/* Code */
code                            /* Inline code (reading mode) */
.cm-inline-code                 /* Inline code (editing mode) */
pre > code                      /* Code block (reading mode) */
.HyperMD-codeblock              /* Code block line (editing mode) */
.cm-hmd-codeblock               /* Code block content (editing mode) */

/* Lists */
.markdown-rendered ul, ol       /* Lists (reading mode) */
.HyperMD-list-line              /* List line (editing mode) */
.list-bullet                    /* Bullet marker */

/* Checkboxes */
.task-list-item                 /* Task item (reading mode) */
input[data-task]                /* Checkbox input */
li[data-task="x"]               /* Completed task */
li[data-task="-"]               /* Cancelled task */
.HyperMD-task-line              /* Task line (editing mode) */

/* Callouts */
.callout                        /* Callout container (reading mode) */
.callout[data-callout="info"]   /* Specific callout type */
.callout-title                  /* Callout title bar */
.callout-content                /* Callout body */
.callout.is-collapsible         /* Collapsible callout */
.callout.is-collapsed           /* Collapsed callout */
.cm-callout                     /* Callout (editing mode) */
.HyperMD-callout                /* Callout line (editing mode) */

/* Tables */
.markdown-rendered table        /* Table (reading mode) */
.markdown-rendered th           /* Header cell */
.markdown-rendered td           /* Body cell */

/* Blockquotes */
blockquote                      /* Blockquote (reading mode) */
.HyperMD-quote                  /* Quote line (editing mode) */

/* Tags */
a.tag                           /* Tag (reading mode) */
.cm-hashtag                     /* Tag (editing mode) */

/* Embeds */
.internal-embed                 /* Embedded content */
.markdown-embed                 /* Embedded note */
.media-embed                    /* Embedded media */
img                             /* Image */

/* Math */
mjx-container                   /* MathJax container */
.math                           /* Math block */

/* Footnotes */
.footnote-link                  /* Footnote reference */
.footnotes                      /* Footnote section */

/* Frontmatter / Properties */
.metadata-container             /* Properties section */
.metadata-property              /* Individual property */
.metadata-property-key          /* Property label */
.metadata-property-value        /* Property value */
```

### Modals & Popovers

```css
.modal                          /* Modal overlay */
.modal-container                /* Modal content */
.modal-title                    /* Modal title */
.modal-content                  /* Modal body */
.prompt                         /* Quick switcher / command palette */
.suggestion-container           /* Autocomplete dropdown */
.suggestion-item                /* Autocomplete option */
.suggestion-item.is-selected    /* Selected option */
.popover                        /* Popover container */
.menu                           /* Context menu */
.menu-item                      /* Menu item */
```

---

## Mode-Specific Selectors

### Reading Mode (Preview)

Container: `.markdown-preview-view`
Content uses standard HTML elements (`h1`, `p`, `a`, `table`, `blockquote`, etc.)

```css
.markdown-preview-view {
  /* Reading mode container */
}
.markdown-rendered h1 {
  /* Rendered heading */
}
.markdown-rendered a.external-link {
  /* External link in reading mode */
}
```

### Source Mode (Raw Markdown)

Container: `.markdown-source-view:not(.is-live-preview)`

```css
.markdown-source-view:not(.is-live-preview) .cm-line {
  /* Only raw source mode */
}
```

### Live Preview

Container: `.markdown-source-view.is-live-preview`

```css
.markdown-source-view.is-live-preview .cm-line {
  /* Only live preview */
}
```

### Editing Mode (Both Source & Live Preview)

Container: `.markdown-source-view.mod-cm6`

```css
.markdown-source-view.mod-cm6 .cm-editor {
  /* Any editing mode */
}
```

### CodeMirror 6 Class Reference

| Class | Element |
|---|---|
| `.cm-editor` | Editor root |
| `.cm-content` | Content area |
| `.cm-line` | Single line |
| `.cm-active` | Active/cursor line |
| `.cm-header-1` through `.cm-header-6` | Heading levels |
| `.cm-strong` | Bold text |
| `.cm-em` | Italic text |
| `.cm-strikethrough` | Strikethrough |
| `.cm-inline-code` | Inline code |
| `.cm-hmd-codeblock` | Code block content |
| `.cm-hmd-internal-link` | Internal link |
| `.cm-hmd-external-link` | External link |
| `.cm-url` | URL |
| `.cm-hashtag` | Tag |
| `.cm-highlight` | Highlighted text |
| `.cm-math` | Math content |
| `.cm-callout` | Callout |
| `.cm-formatting-*` | Markdown formatting chars |

### HyperMD Classes (Line-Level)

| Class | Line type |
|---|---|
| `.HyperMD-header-1` through `.HyperMD-header-6` | Heading lines |
| `.HyperMD-list-line` | List item lines |
| `.HyperMD-task-line` | Task/checkbox lines |
| `.HyperMD-quote` | Blockquote lines |
| `.HyperMD-codeblock` | Code block lines |
| `.HyperMD-callout` | Callout lines |
| `.HyperMD-footnote` | Footnote lines |
| `.HyperMD-table-row` | Table row lines |

---

## Theme Guidelines

### Do

- Override CSS variables instead of writing raw selectors when possible
- Use low-specificity selectors
- Support both `.theme-light` and `.theme-dark`
- Bundle all assets locally (fonts, images) for published themes
- Define general variables on `body`, colors on `.theme-light` / `.theme-dark`
- Test in reading mode, source mode, and live preview
- Test on mobile (use `this.app.emulateMobile(true)` in console)
- Use Obsidian's spacing system (`--size-4-*`)
- Use Obsidian's color variables (`--color-*`, `--text-*`, `--background-*`)

### Don't

- Use `:has()` selector — prohibited by developer policies
- Use `!important` — prevents user snippet overrides
- Use remote URLs for assets in published themes
- Hardcode colors — always use CSS variables for theme compatibility
- Assume a specific DOM structure — Obsidian updates can change it
- Use excessive specificity — it makes the theme hard to customize

### Where to Define Variables

| Scope | Selector | Use for |
|---|---|---|
| Global | `body` | Fonts, spacing, non-color properties |
| Light mode | `.theme-light` | Light-specific colors |
| Dark mode | `.theme-dark` | Dark-specific colors |
| All modes | `:root` | Rarely needed; use `body` instead |

---

## Debugging Workflow

### Opening Developer Tools

| Platform | Shortcut |
|---|---|
| macOS | `Cmd+Option+I` |
| Windows/Linux | `Ctrl+Shift+I` |

### Inspecting Elements

1. Open DevTools
2. Enable inspect mode: `Cmd+Shift+C` / `Ctrl+Shift+C`
3. Hover over the target element — you'll see its class names
4. Click to select it
5. In the **Styles** panel, see all CSS rules affecting it
6. In the **Computed** panel, trace any property back to its source

### Finding CSS Variables

1. Select the `body` element in the Elements panel
2. In the Styles panel, scroll through the element.style or search for variable names
3. Or use the Computed tab and filter by property name

### Testing Changes Live

1. In the Styles panel, click on a value to edit it
2. Add new rules in `element.style {}` at the top
3. Changes are temporary — they reset on reload
4. Once you're happy, copy the CSS into your snippet/theme

### Testing Interactive States

Right-click an element in the Elements panel > "Toggle Element State" to force `:hover`, `:focus`, `:active` states.

### Mobile Emulation

Run in the DevTools console:
```js
this.app.emulateMobile(true);   // Enable mobile mode
this.app.emulateMobile(false);  // Disable
```

### Obsidian CLI Debugging (if available)

```bash
obsidian dev:dom selector=".element"     # View DOM structure
obsidian dev:css selector=".element"     # View computed styles
obsidian dev:screenshot                   # Capture current state
obsidian dev:console                      # View console output
obsidian dev:errors                       # Check for errors
```

---

## Style Settings Plugin

The [Style Settings](https://github.com/mgmeyers/obsidian-style-settings) plugin scans CSS files for `/* @settings */` blocks and generates a UI for users to configure theme options.

### Setting Types

#### `variable-color`

```css
-
  id: my-color
  title: My Color
  description: A color setting
  type: variable-color
  format: hex          /* hex | hsl | hsl-values | rgb | rgb-values */
  default: '#007AFF'
  opacity: false       /* optional, allow opacity slider */
```

#### `variable-themed-color`

Separate defaults for light and dark modes:

```css
-
  id: bg-color
  title: Background Color
  type: variable-themed-color
  format: hex
  default-light: '#ffffff'
  default-dark: '#1e1e1e'
```

#### `variable-number`

```css
-
  id: font-size
  title: Font Size
  type: variable-number
  default: 16
  format: px           /* px | em | rem | pt | % | (empty for unitless) */
```

#### `variable-number-slider`

```css
-
  id: opacity
  title: Opacity
  type: variable-number-slider
  default: 1
  min: 0
  max: 1
  step: 0.1
  format: ""
```

#### `variable-text`

```css
-
  id: custom-font
  title: Custom Font
  type: variable-text
  default: 'Inter'
  quotes: true         /* optional, wrap value in quotes */
```

#### `variable-select`

```css
-
  id: heading-style
  title: Heading Style
  type: variable-select
  default: normal
  options:
    - normal
    - italic
    - oblique
```

#### `class-toggle`

Adds/removes a CSS class on the `body` element:

```css
-
  id: fancy-mode
  title: Enable Fancy Mode
  type: class-toggle
  default: false
  addCommand: true     /* optional, register as command palette toggle */
```

Then use `body.fancy-mode` in your CSS selectors.

#### `class-select`

```css
-
  id: layout-style
  title: Layout Style
  type: class-select
  default: layout-default
  options:
    - label: Default
      value: layout-default
    - label: Wide
      value: layout-wide
    - label: Compact
      value: layout-compact
```

#### `heading`

Visual section heading in settings UI (no CSS output):

```css
-
  id: colors-section
  title: Color Settings
  type: heading
  level: 1             /* 1, 2, or 3 */
  collapsed: true      /* optional, start collapsed */
```

#### `info-text`

Informational text in settings UI:

```css
-
  id: info
  title: About
  type: info-text
  description: "This theme supports custom colors and fonts."
  markdown: true       /* optional, render markdown */
```

#### `color-gradient`

```css
-
  id: gradient-bg
  title: Gradient Background
  type: color-gradient
  format: rgb
  default: "linear-gradient(to right, #ff0000, #0000ff)"
```

### Complete Example

```css
/* @settings
name: My Theme
id: my-theme
settings:
  -
    id: colors-heading
    title: Colors
    type: heading
    level: 1
  -
    id: accent-color
    title: Accent Color
    type: variable-themed-color
    format: hex
    default-light: '#705dcf'
    default-dark: '#7f6df2'
  -
    id: typography-heading
    title: Typography
    type: heading
    level: 1
  -
    id: font-size
    title: Body Font Size
    type: variable-number-slider
    default: 16
    min: 12
    max: 24
    step: 1
    format: px
  -
    id: heading-font
    title: Heading Font
    type: variable-text
    default: ''
  -
    id: features-heading
    title: Features
    type: heading
    level: 1
  -
    id: minimal-tabs
    title: Minimal Tab Style
    type: class-toggle
    default: false
*/

body.minimal-tabs .workspace-tab-header {
  border: none;
  background: transparent;
}
```

---

## Font & Image Embedding

### Base64 Font Embedding

For published themes, all fonts must be bundled:

```css
@font-face {
  font-family: 'MyFont';
  src: url('data:font/woff2;base64,<BASE64>') format('woff2');
  font-weight: 400;
  font-style: normal;
}
```

Encode with: `base64 -i font.woff2 | tr -d '\n'`

### Image Embedding

```css
.my-element::before {
  content: '';
  background-image: url('data:image/svg+xml;base64,<BASE64>');
}
```

### MIME Types

| Format | MIME |
|---|---|
| WOFF2 | `font/woff2` |
| WOFF | `font/woff` |
| TTF | `font/ttf` |
| OTF | `font/otf` |
| SVG | `image/svg+xml` |
| PNG | `image/png` |
| JPG | `image/jpeg` |

### For Local Snippets

When the CSS is only for personal use (not publishing), external imports are fine:

```css
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
```
