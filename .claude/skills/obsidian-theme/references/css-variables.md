# Obsidian CSS Variables Reference

Source: [Obsidian Developer Documentation](https://docs.obsidian.md/Reference/CSS+variables/CSS+variables)

---

## Foundations

### Colors

The Obsidian color palette defines a range of colors used in the app.

#### Base Colors

The base colors are a neutral color palette ranging from light to dark. These values should typically only be defined by themes.

| Variable | Default (light) | Default (dark) |
|---|---|---|
| `--color-base-00` | `#ffffff` | `#1e1e1e` |
| `--color-base-05` | `#fcfcfc` | `#212121` |
| `--color-base-10` | `#fafafa` | `#242424` |
| `--color-base-20` | `#f6f6f6` | `#262626` |
| `--color-base-25` | `#e3e3e3` | `#2a2a2a` |
| `--color-base-30` | `#e0e0e0` | `#363636` |
| `--color-base-35` | `#d4d4d4` | `#3f3f3f` |
| `--color-base-40` | `#bdbdbd` | `#555555` |
| `--color-base-50` | `#ababab` | `#666666` |
| `--color-base-60` | `#707070` | `#999999` |
| `--color-base-70` | `#5a5a5a` | `#bababa` |
| `--color-base-100` | `#222222` | `#dadada` |

#### Accent Color

The accent color is used to draw attention to interactive elements, such as links and primary buttons. It can be overridden by the user under Settings > Appearance.

| Variable | Default | Description |
|---|---|---|
| `--accent-h` | `254` | Accent hue |
| `--accent-s` | `80%` | Accent saturation |
| `--accent-l` | `68%` | Accent lightness |

You can use CSS calculations to create shades based on the accent color.

#### Extended Colors

Used for status messages, callouts, syntax highlighting, graph nodes, and Canvas elements. Each has an additional `-rgb` suffix variant for use with `rgba()`.

```css
color: var(--color-red);
background-color: rgba(var(--color-red-rgb), 0.2);
```

| Variable | Default (light) | Default (dark) |
|---|---|---|
| `--color-red` | `#e93147` | `#fb464c` |
| `--color-orange` | `#ec7500` | `#e9973f` |
| `--color-yellow` | `#e0ac00` | `#e0de71` |
| `--color-green` | `#08b94e` | `#44cf6e` |
| `--color-cyan` | `#00bfbc` | `#53dfdd` |
| `--color-blue` | `#086ddd` | `#027aff` |
| `--color-purple` | `#7852ee` | `#a882ff` |
| `--color-pink` | `#d53984` | `#fa99cd` |
| `--color-red-rgb` | `233, 49, 71` | `251, 70, 76` |
| `--color-orange-rgb` | `236, 117, 0` | `233, 151, 63` |
| `--color-yellow-rgb` | `224, 172, 0` | `224, 222, 113` |
| `--color-green-rgb` | `8, 185, 78` | `68, 207, 110` |
| `--color-cyan-rgb` | `0, 191, 188` | `83, 223, 221` |
| `--color-blue-rgb` | `8, 109, 221` | `2, 122, 255` |
| `--color-purple-rgb` | `120, 82, 238` | `168, 130, 255` |
| `--color-pink-rgb` | `213, 57, 132` | `250, 153, 205` |

#### Black and White

For creating masks with opacity. Avoid changing these values.

| Variable | Default (light) | Default (dark) |
|---|---|---|
| `--mono-rgb-0` | `255, 255, 255` | `0, 0, 0` |
| `--mono-rgb-100` | `0, 0, 0` | `255, 255, 255` |

#### Surface Colors

| Variable | Description |
|---|---|
| `--background-primary` | Primary background |
| `--background-primary-alt` | Background for surfaces on top of primary background |
| `--background-secondary` | Secondary background |
| `--background-secondary-alt` | Background for surfaces on top of secondary background |
| `--background-modifier-hover` | Hovered elements |
| `--background-modifier-active-hover` | Active hovered elements |
| `--background-modifier-border` | Border color |
| `--background-modifier-border-hover` | Border color (hover) |
| `--background-modifier-border-focus` | Border color (focus) |
| `--background-modifier-error-rgb` | Error background, RGB value |
| `--background-modifier-error` | Error background |
| `--background-modifier-error-hover` | Error background (hover) |
| `--background-modifier-success-rgb` | Success background, RGB value |
| `--background-modifier-success` | Success background |
| `--background-modifier-message` | Messages background |
| `--background-modifier-form-field` | Form field background |

#### Interactive Colors

| Variable | Description |
|---|---|
| `--interactive-normal` | Background for standard interactive elements |
| `--interactive-hover` | Background for standard interactive elements (hover) |
| `--interactive-accent` | Background for accented interactive elements |
| `--interactive-accent-hsl` | Background for accented interactive elements in HSL |
| `--interactive-accent-hover` | Background for accented interactive elements (hover) |

#### Text Foreground Colors

| Variable | Description |
|---|---|
| `--text-normal` | Normal text |
| `--text-muted` | Muted text |
| `--text-faint` | Faint text |
| `--text-on-accent` | Text on accent background when accent is dark |
| `--text-on-accent-inverted` | Text on accent background when accent is light |
| `--text-success` | Success text |
| `--text-warning` | Warning text |
| `--text-error` | Error text |
| `--text-accent` | Accent text |
| `--text-accent-hover` | Accent text (hover) |

#### Text Background Colors

| Variable | Description |
|---|---|
| `--text-selection` | Selected text background |
| `--text-highlight-bg` | Highlighted text background |

#### Caret Color

| Variable | Description |
|---|---|
| `--caret-color` | Caret color (blinking text entry cursor) |

---

### Typography

#### Fonts

| Variable | Description |
|---|---|
| `--font-interface-theme` | Font used for UI elements |
| `--font-text-theme` | Font used for text in the editor |
| `--font-monospace-theme` | Font used for monospaced content such as code blocks and inline code |

#### Font Size

Use `--font-*` (relative) variables in the editor. Use `--font-ui-*` (fixed) variables for UI elements.

| Variable | Default | Description |
|---|---|---|
| `--font-text-size` | `16px` | Editor font size. Defined by the user under Appearance settings. |
| `--font-smallest` | `0.8em` | |
| `--font-smaller` | `0.875em` | |
| `--font-small` | `0.933em` | |
| `--font-ui-smaller` | `12px` | |
| `--font-ui-small` | `13px` | |
| `--font-ui-medium` | `15px` | |
| `--font-ui-large` | `20px` | |

#### Font Weight

| Variable | Default |
|---|---|
| `--font-thin` | `100` |
| `--font-extralight` | `200` |
| `--font-light` | `300` |
| `--font-normal` | `400` |
| `--font-medium` | `500` |
| `--font-semibold` | `600` |
| `--font-bold` | `700` |
| `--font-extrabold` | `800` |
| `--font-black` | `900` |

#### Text Formatting

As of Obsidian 1.6, `--bold-modifier` is the recommended way to change the weight of bolded text. The bold modifier value stacks on top of other font weights (e.g. `## Bold **bolder**`). Recommended values for `--bold-modifier` are between 100 and 300.

| Variable | Description |
|---|---|
| `--font-weight` | Regular text weight |
| `--bold-modifier` | Added weight for bolded text |
| `--bold-weight` | Bold text font weight |
| `--bold-color` | Bold text color |
| `--italic-color` | Italic text color |

#### Line Heights

| Variable | Default | Description |
|---|---|---|
| `--line-height-normal` | `1.5` | Default line height |
| `--line-height-tight` | `1.3` | Used in search results, tree items, tooltips, and other smaller spaces |

#### Paragraph Spacing

| Variable | Description |
|---|---|
| `--heading-spacing` | Spacing above headings |
| `--p-spacing` | Spacing between paragraphs |

---

### Spacing

Obsidian uses a 4-pixel grid to structure UI elements. All elements should use the predefined `--size` CSS variables for spacing and dimension properties. Each size variable contains two numbers: base and multiple (e.g. `--size-4-2` = 4x2 = `8px`).

| Variable | Default |
|---|---|
| `--size-2-1` | `2px` |
| `--size-2-2` | `4px` |
| `--size-2-3` | `6px` |
| `--size-4-1` | `4px` |
| `--size-4-2` | `8px` |
| `--size-4-3` | `12px` |
| `--size-4-4` | `16px` |
| `--size-4-5` | `20px` |
| `--size-4-6` | `24px` |
| `--size-4-8` | `32px` |
| `--size-4-9` | `36px` |
| `--size-4-12` | `48px` |
| `--size-4-16` | `64px` |
| `--size-4-18` | `72px` |

---

### Borders

| Variable | Default |
|---|---|
| `--border-width` | `1px` |

---

### Radiuses

| Variable | Default |
|---|---|
| `--radius-s` | `4px` |
| `--radius-m` | `8px` |
| `--radius-l` | `12px` |
| `--radius-xl` | `16px` |

---

### Cursor

Obsidian follows operating system conventions for cursors: interactive elements use the arrow cursor instead of the pointer cursor.

| Variable | Default | Description |
|---|---|---|
| `--cursor` | `default` | Cursor for interactive elements |
| `--cursor-link` | `pointer` | Cursor for links |

---

### Icons

Obsidian uses the [Lucide](https://lucide.dev/) icon library.

| Variable | Description |
|---|---|
| `--icon-size` | Shorthand for icon width and length |
| `--icon-stroke` | Shorthand for icon stroke width |
| `--icon-color` | Icon color |
| `--icon-color-hover` | Icon color (hovered) |
| `--icon-color-active` | Icon color (active) |
| `--icon-color-focused` | Icon color (focused) |
| `--icon-opacity` | Icon opacity |
| `--icon-opacity-hover` | Icon opacity (hovered) |
| `--icon-opacity-active` | Icon opacity (active) |
| `--clickable-icon-radius` | Clickable icon button radius |

#### Icon Sizes

| Variable | Default |
|---|---|
| `--icon-xs` | `14px` |
| `--icon-s` | `16px` |
| `--icon-m` | `18px` |
| `--icon-l` | `18px` |
| `--icon-xl` | `32px` |
| `--icon-xs-stroke-width` | `2px` |
| `--icon-s-stroke-width` | `2px` |
| `--icon-m-stroke-width` | `1.75px` |
| `--icon-l-stroke-width` | `1.75px` |
| `--icon-xl-stroke-width` | `1.25px` |

---

### Layers (z-index)

| Variable | Default |
|---|---|
| `--layer-cover` | `5` |
| `--layer-sidedock` | `10` |
| `--layer-status-bar` | `15` |
| `--layer-popover` | `30` |
| `--layer-slides` | `45` |
| `--layer-modal` | `50` |
| `--layer-notice` | `60` |
| `--layer-menu` | `65` |
| `--layer-tooltip` | `70` |
| `--layer-dragged-item` | `80` |

---

## Editor

### Headings

| Variable | Description |
|---|---|
| `--heading-formatting` | Text color for Markdown heading depth syntax |
| `--heading-spacing` | Spacing above headings |
| `--h1-color` | H1 text color |
| `--h2-color` | H2 text color |
| `--h3-color` | H3 text color |
| `--h4-color` | H4 text color |
| `--h5-color` | H5 text color |
| `--h6-color` | H6 text color |
| `--h1-font` | H1 font family |
| `--h2-font` | H2 font family |
| `--h3-font` | H3 font family |
| `--h4-font` | H4 font family |
| `--h5-font` | H5 font family |
| `--h6-font` | H6 font family |
| `--h1-line-height` | H1 line height |
| `--h2-line-height` | H2 line height |
| `--h3-line-height` | H3 line height |
| `--h4-line-height` | H4 line height |
| `--h5-line-height` | H5 line height |
| `--h6-line-height` | H6 line height |
| `--h1-size` | H1 font size |
| `--h2-size` | H2 font size |
| `--h3-size` | H3 font size |
| `--h4-size` | H4 font size |
| `--h5-size` | H5 font size |
| `--h6-size` | H6 font size |
| `--h1-style` | H1 font style |
| `--h2-style` | H2 font style |
| `--h3-style` | H3 font style |
| `--h4-style` | H4 font style |
| `--h5-style` | H5 font style |
| `--h6-style` | H6 font style |
| `--h1-variant` | H1 font variant |
| `--h2-variant` | H2 font variant |
| `--h3-variant` | H3 font variant |
| `--h4-variant` | H4 font variant |
| `--h5-variant` | H5 font variant |
| `--h6-variant` | H6 font variant |
| `--h1-weight` | H1 font weight |
| `--h2-weight` | H2 font weight |
| `--h3-weight` | H3 font weight |
| `--h4-weight` | H4 font weight |
| `--h5-weight` | H5 font weight |
| `--h6-weight` | H6 font weight |

---

### Callouts

| Variable | Description |
|---|---|
| `--callout-border-width` | Callout border width |
| `--callout-border-opacity` | Callout border opacity |
| `--callout-padding` | Callout padding |
| `--callout-radius` | Callout radius |
| `--callout-blend-mode` | Callout blend mode, allows color mixing for nested callouts |
| `--callout-title-color` | Callout title text color |
| `--callout-title-padding` | Callout title padding |
| `--callout-title-size` | Callout title font size |
| `--callout-title-weight` | Callout title weight |
| `--callout-content-padding` | Callout content padding |
| `--callout-content-background` | Callout content background color |

#### Type Colors

Callout types have unique icons and colors, and may have multiple aliases.

| Variable | Callout type |
|---|---|
| `--callout-bug` | `bug` |
| `--callout-default` | `default`, `note` |
| `--callout-error` | `error`, `danger` |
| `--callout-example` | `example` |
| `--callout-fail` | `fail`, `failure`, `missing` |
| `--callout-important` | `important` |
| `--callout-info` | `info` |
| `--callout-question` | `question`, `help`, `faq` |
| `--callout-success` | `success`, `check`, `done` |
| `--callout-summary` | `summary`, `abstract`, `tldr` |
| `--callout-tip` | `tip`, `hint` |
| `--callout-todo` | `todo` |
| `--callout-warning` | `warning`, `caution`, `attention` |
| `--callout-quote` | `quote`, `cite` |

---

### Code

| Variable | Description |
|---|---|
| `--code-background` | Code background color |
| `--code-white-space` | Code `white-space` |
| `--code-size` | Code font size |

#### Syntax Highlighting

Note: Obsidian uses two different libraries for syntax highlighting -- one for Editing view and another for Reading view -- so styling may not match perfectly between the two.

| Variable | Description |
|---|---|
| `--code-normal` | Non-highlighted syntax |
| `--code-comment` | Comments |
| `--code-function` | Functions |
| `--code-important` | Important, regex |
| `--code-keyword` | Keywords |
| `--code-operator` | Operators |
| `--code-property` | Properties |
| `--code-punctuation` | Punctuation |
| `--code-string` | Strings |
| `--code-tag` | Tags, symbols, constants |
| `--code-value` | Values |

---

### Tables

| Variable | Description |
|---|---|
| `--table-background` | Table background color |
| `--table-border-width` | Table border width |
| `--table-border-color` | Table border color |
| `--table-cell-vertical-alignment` | Cell vertical alignment |
| `--table-white-space` | Table `white-space` property |
| `--table-header-background` | Table header background color |
| `--table-header-background-hover` | Table header background color (hover) |
| `--table-header-border-width` | Table header border width |
| `--table-header-border-color` | Table header border color |
| `--table-header-font` | Table header font family |
| `--table-header-size` | Table header font size |
| `--table-header-weight` | Table header font weight |
| `--table-header-color` | Table header text color |
| `--table-line-height` | Line height for cell text |
| `--table-text-size` | Cell font size |
| `--table-text-color` | Cell text color |
| `--table-column-max-width` | Column maximum width |
| `--table-column-alt-background` | Alternating column background color |
| `--table-column-first-border-width` | First column left border width |
| `--table-column-last-border-width` | Last column right border width |
| `--table-row-background-hover` | Row background color (hover) |
| `--table-row-alt-background` | Alternating row background color |
| `--table-row-alt-background-hover` | Alternating row background color (hover) |
| `--table-row-last-border-width` | Last row bottom border width |
| `--table-selection` | Selection background color |
| `--table-selection-blend-mode` | Selection blend mode |
| `--table-selection-border-color` | Selection border color |
| `--table-selection-border-width` | Selection border width |
| `--table-selection-border-radius` | Selection border radius |
| `--table-drag-handle-background` | Drag handle background color |
| `--table-drag-handle-background-active` | Drag handle background color (active) |
| `--table-drag-handle-color` | Drag handle icon color |
| `--table-drag-handle-color-active` | Drag handle icon color (active) |
| `--table-add-button-background` | "Add" button background color |
| `--table-add-button-border-width` | "Add" button border width |
| `--table-add-button-border-color` | "Add" button border color |

---

### Links

Obsidian supports three link types: resolved internal links (existing note), unresolved internal links (non-existing note), and external links (external URL or URI).

| Variable | Description |
|---|---|
| `--link-color` | Resolved link text color |
| `--link-color-hover` | Resolved link text color (hover) |
| `--link-decoration` | Resolved link text decoration |
| `--link-decoration-hover` | Resolved link text decoration (hover) |
| `--link-decoration-thickness` | Resolved link text decoration thickness |
| `--link-weight` | Link font weight |
| `--link-unresolved-color` | Unresolved link text color |
| `--link-unresolved-opacity` | Unresolved link opacity |
| `--link-unresolved-filter` | Unresolved link filter, e.g. `hue-rotate` |
| `--link-unresolved-decoration-style` | Unresolved link text decoration style |
| `--link-unresolved-decoration-color` | Unresolved link text decoration color |
| `--link-external-color` | External link text color |
| `--link-external-color-hover` | External link text color (hover) |
| `--link-external-decoration` | External link text decoration |
| `--link-external-decoration-hover` | External link text decoration (hover) |

---

### Tags

| Variable | Description |
|---|---|
| `--tag-size` | Tag font size |
| `--tag-color` | Tag text color |
| `--tag-color-hover` | Tag text color (hover) |
| `--tag-decoration` | Tag text decoration |
| `--tag-decoration-hover` | Tag text decoration (hover) |
| `--tag-background` | Tag background color |
| `--tag-background-hover` | Tag background color (hover) |
| `--tag-border-color` | Tag border color |
| `--tag-border-color-hover` | Tag border color (hover) |
| `--tag-border-width` | Tag border width |
| `--tag-padding-x` | Tag left/right padding |
| `--tag-padding-y` | Tag top/down padding |
| `--tag-radius` | Tag radius |
| `--tag-weight` | Tag font weight |

---

### Lists

| Variable | Description |
|---|---|
| `--list-indent` | Indentation width for nested items |
| `--list-indent-editing` | Indent width in Live Preview |
| `--list-indent-source` | Indent width in source mode |
| `--list-spacing` | Vertical spacing between list items |
| `--list-marker-color` | Marker color |
| `--list-marker-color-hover` | Marker color (hover) |
| `--list-marker-color-collapsed` | Marker color for collapsed items |
| `--list-bullet-border` | Bullet border |
| `--list-bullet-end-padding` | Padding after the bullet |
| `--list-bullet-radius` | Bullet radius |
| `--list-bullet-size` | Bullet width/height |
| `--list-bullet-transform` | Bullet `transform` property |
| `--list-numbered-style` | `list-style-type` for numbered lists |

---

### Checkboxes

| Variable | Description |
|---|---|
| `--checkbox-radius` | Radius |
| `--checkbox-size` | Height and width |
| `--checkbox-marker-color` | Marker color for the check itself |
| `--checkbox-color` | Background color |
| `--checkbox-color-hover` | Background color (hover) |
| `--checkbox-border-color` | Unchecked border color |
| `--checkbox-border-color-hover` | Unchecked border color (hover) |
| `--checklist-done-decoration` | Checked text decoration |
| `--checklist-done-color` | Checked text color |
| `--checkbox-margin-inline-start` | `start` margin |

---

### Blockquotes

| Variable | Description |
|---|---|
| `--blockquote-background-color` | Blockquote background color |
| `--blockquote-border-thickness` | Blockquote left border thickness |
| `--blockquote-border-color` | Blockquote left border color |
| `--blockquote-font-style` | Blockquote font style (e.g. normal, italic) |
| `--blockquote-color` | Blockquote text color |

---

### Inline Title

To see inline titles, enable Settings > Appearance > Show inline title.

| Variable | Description |
|---|---|
| `--inline-title-color` | Inline title text color |
| `--inline-title-font` | Inline title font family |
| `--inline-title-line-height` | Inline title line height |
| `--inline-title-size` | Inline title font size |
| `--inline-title-style` | Inline title font style |
| `--inline-title-variant` | Inline title font variant |
| `--inline-title-weight` | Inline title font weight |

---

### Horizontal Rule

| Variable | Description |
|---|---|
| `--hr-color` | Horizontal rule border color |
| `--hr-thickness` | Horizontal rule border thickness |

---

### Embeds

| Variable | Description |
|---|---|
| `--embed-max-height` | Embed max height |
| `--embed-canvas-max-height` | Embedded Canvas element max height |
| `--embed-background` | Embed background color |
| `--embed-border-end` | Embed `end` border, shorthand property |
| `--embed-border-start` | Embed `start` border, shorthand property |
| `--embed-border-top` | Embed top border, shorthand property |
| `--embed-border-bottom` | Embed bottom border, shorthand property |
| `--embed-padding` | Embed padding |
| `--embed-font-style` | Embed `font-style` |

---

### File

| Variable | Description |
|---|---|
| `--file-line-width` | Width of a line when readable line width is turned on |
| `--file-folding-offset` | Width of the line offset for fold indicators |
| `--file-margins` | File margins |
| `--file-header-font-size` | File header font size |
| `--file-header-font-weight` | File header font weight |
| `--file-header-border` | File header `border-bottom` property |
| `--file-header-justify` | File header text alignment, uses `justify-content` |

---

### Block

| Variable | Description |
|---|---|
| `--embed-block-shadow-hover` | Hover shadow for rendered embed blocks in Live Preview |

---

### Footnote

| Variable | Description |
|---|---|
| `--footnote-size` | Footnote font size |

---

### Properties (YAML Frontmatter)

#### Properties Container

| Variable | Description |
|---|---|
| `--metadata-background` | Background color |
| `--metadata-display-editing` | Display in editing mode |
| `--metadata-display-reading` | Display in reading mode |
| `--metadata-max-width` | Max width |
| `--metadata-padding` | Padding |
| `--metadata-border-color` | Border color |
| `--metadata-border-radius` | Corner radius |
| `--metadata-border-width` | Border width |
| `--metadata-gap` | Gap between properties |

#### Individual Properties

| Variable | Description |
|---|---|
| `--metadata-divider-color` | Color of divider lines between properties |
| `--metadata-divider-color-hover` | Color of dividers when property (hover) |
| `--metadata-divider-color-focus` | Color of dividers when property (focused) |
| `--metadata-divider-width` | Width of divider lines |
| `--metadata-property-padding` | Property padding |
| `--metadata-property-radius` | Property corner radius |
| `--metadata-property-radius-hover` | Property corner radius (hover) |
| `--metadata-property-radius-focus` | Property corner radius (focus) |
| `--metadata-property-background` | Property background color |
| `--metadata-property-background-hover` | Property background color (hover) |
| `--metadata-property-background-active` | Property background color (active) |
| `--metadata-label-background-hover` | Property label background color (hover) |
| `--metadata-label-background-active` | Property label background color (active) |
| `--metadata-label-font-size` | Property label font size |
| `--metadata-label-font-weight` | Property label font weight |
| `--metadata-sidebar-label-font-size` | Property label font size (sidebar) |
| `--metadata-label-text-color` | Property label text color |
| `--metadata-label-text-color-hover` | Property label text color (hover) |
| `--metadata-label-width` | Property label width |
| `--metadata-input-height` | Property input height |
| `--metadata-input-text-color` | Property input text color |
| `--metadata-input-font-size` | Property input font size |
| `--metadata-sidebar-input-font-size` | Property input font size (sidebar) |
| `--metadata-input-background` | Property input background color |
| `--metadata-input-background-hover` | Property input background color (hover) |
| `--metadata-input-background-active` | Property input background color (active) |

---

## Components

### Button

For button colors, refer to Interactive Colors in the Colors section.

| Variable | Description |
|---|---|
| `--button-radius` | Button radius |

---

### Checkbox

See Checkboxes under Editor section above.

---

### Color Input

| Variable | Description |
|---|---|
| `--swatch-radius` | Color swatch radius |
| `--swatch-height` | Color swatch height |
| `--swatch-width` | Color swatch width |
| `--swatch-shadow` | Color swatch shadow |

---

### Dialog

A dialog is a smaller modal primarily used for confirmation.

| Variable | Description |
|---|---|
| `--dialog-width` | Dialog default width |
| `--dialog-max-width` | Dialog maximum width |
| `--dialog-max-height` | Dialog maximum height |

---

### Dragging

Displayed while the user drags files or tabs.

| Variable | Description |
|---|---|
| `--drag-ghost-background` | Drag ghost background color |
| `--drag-ghost-text-color` | Drag ghost text color |

---

### Indentation Guides

Indentation guides visualize the indentation level in nested lists.

| Variable | Description |
|---|---|
| `--indentation-guide-width` | Indentation guide border width |
| `--indentation-guide-width-active` | Indentation guide border width (active) |
| `--indentation-guide-color` | Indentation guide border color |
| `--indentation-guide-color-active` | Indentation guide border color (active) |
| `--indentation-guide-editing-indent` | Width of the indent in edit mode |
| `--indentation-guide-reading-indent` | Width of the indent in read mode |
| `--indentation-guide-source-indent` | Width of the indent in source mode |

---

### Modal

| Variable | Description |
|---|---|
| `--modal-background` | Modal background color |
| `--modal-width` | Modal default width |
| `--modal-height` | Modal default height |
| `--modal-max-width` | Modal maximum width |
| `--modal-max-height` | Modal maximum height |
| `--modal-max-width-narrow` | Narrow modal maximum width |
| `--modal-border-width` | Modal border thickness |
| `--modal-border-color` | Modal border color |
| `--modal-radius` | Modal radius |
| `--modal-community-sidebar-width` | Community plugin/theme sidebar width |

---

### Multi-select

Used in List type Properties.

| Variable | Description |
|---|---|
| `--pill-color` | Pill text color |
| `--pill-color-hover` | Pill text color (hover) |
| `--pill-color-remove` | Pill text color when removing |
| `--pill-color-remove-hover` | Pill text color when removing (hover) |
| `--pill-decoration` | Pill text decoration |
| `--pill-decoration-hover` | Pill text decoration (hover) |
| `--pill-background` | Pill background color |
| `--pill-background-hover` | Pill background color (hover) |
| `--pill-border-color` | Pill border color |
| `--pill-border-color-hover` | Pill border color (hover) |
| `--pill-border-width` | Pill border width |
| `--pill-padding-x` | Pill left/right padding |
| `--pill-padding-y` | Pill top/bottom padding |
| `--pill-radius` | Pill corner radius |
| `--pill-weight` | Pill font weight |

---

### Navigation

Used for files and folders in File Explorer.

| Variable | Description |
|---|---|
| `--nav-item-size` | Nav item font size |
| `--nav-item-color` | Nav item text color |
| `--nav-item-color-hover` | Nav item text color (hover) |
| `--nav-item-color-active` | Nav item text color (active) |
| `--nav-item-color-selected` | Nav item text color (selected) |
| `--nav-item-color-highlighted` | Nav item text color (highlighted) |
| `--nav-item-background-hover` | Nav item background color (hover) |
| `--nav-item-background-active` | Nav item background color (active) |
| `--nav-item-background-selected` | Nav item background color (selected) |
| `--nav-item-padding` | Nav item padding |
| `--nav-item-parent-padding` | Nav item padding for parent elements |
| `--nav-item-children-padding-start` | Nav item children `start` padding |
| `--nav-item-children-margin-start` | Nav item children `start` margin |
| `--nav-item-weight` | Nav item font weight |
| `--nav-item-weight-hover` | Nav item font weight (hover) |
| `--nav-item-weight-active` | Nav item font weight (active) |
| `--nav-item-white-space` | Nav item `white-space` |
| `--nav-indentation-guide-width` | Nav item indentation guide border width |
| `--nav-indentation-guide-color` | Nav item indentation guide border color |
| `--nav-collapse-icon-color` | Nav item collapse chevron color |
| `--nav-collapse-icon-color-collapsed` | Nav item collapse chevron color (collapsed) |

#### Navigation Headings

Used for collapsible navigation sections, such as linked mentions in Backlinks and Outlinks.

| Variable | Description |
|---|---|
| `--nav-heading-color` | Nav heading text color |
| `--nav-heading-color-hover` | Nav heading text color (hover) |
| `--nav-heading-color-collapsed` | Collapsed nav heading text color |
| `--nav-heading-color-colapsed-hover` | Collapsed nav heading text color (hover) |
| `--nav-heading-weight` | Nav heading font weight |
| `--nav-heading-weight-hover` | Nav heading font weight (hover) |

---

### Popover

| Variable | Description |
|---|---|
| `--popover-width` | Popover default width |
| `--popover-height` | Popover default height |
| `--popover-max-height` | Popover maximum height |
| `--popover-font-size` | Popover font size |
| `--popover-pdf-width` | PDF file preview width |
| `--popover-pdf-height` | PDF file preview height |

---

### Slider

| Variable | Description |
|---|---|
| `--slider-thumb-border-width` | Slider thumb border width |
| `--slider-thumb-border-color` | Slider thumb border color |
| `--slider-thumb-height` | Slider thumb height |
| `--slider-thumb-width` | Slider thumb width |
| `--slider-thumb-y` | Slider thumb Y position |
| `--slider-thumb-radius` | Slider thumb radius |
| `--slider-track-background` | Slider track background color |
| `--slider-track-height` | Slider track height |

---

### Tabs

| Variable | Description |
|---|---|
| `--tab-background-active` | Tab background color (active tab) |
| `--tab-text-color` | Tab text color |
| `--tab-text-color-active` | Tab text color (non-focused window, active) |
| `--tab-text-color-focused` | Tab text color (focused window) |
| `--tab-text-color-focused-active` | Tab text color (focused window, active) |
| `--tab-text-color-focused-highlighted` | Tab text color (focused window, highlighted) |
| `--tab-text-color-focused-active-current` | Tab text color (focused window, current tab) |
| `--tab-font-size` | Tab font size |
| `--tab-font-weight` | Tab font weight |
| `--tab-container-background` | Tab container background color |
| `--tab-divider-color` | Tab divider color |
| `--tab-outline-color` | Tab outline color |
| `--tab-outline-width` | Tab outline width |
| `--tab-curve` | Tab curve radius |
| `--tab-radius` | Tab outer radius |
| `--tab-radius-active` | Tab outer radius (active tab) |
| `--tab-width` | Tab default width |
| `--tab-max-width` | Tab maximum width |

#### Tab Stacks

| Variable | Description |
|---|---|
| `--tab-stacked-pane-width` | Stacked pane width |
| `--tab-stacked-header-width` | Stacked header width |
| `--tab-stacked-font-size` | Stacked tab font size |
| `--tab-stacked-font-weight` | Stacked tab font weight |
| `--tab-stacked-text-align` | Stacked tab text alignment |
| `--tab-stacked-text-transform` | Stacked tab text transform |
| `--tab-stacked-text-writing-mode` | Stacked tab text writing mode |
| `--tab-stacked-shadow` | Stacked tab shadow |

---

### Text Input

| Variable | Description |
|---|---|
| `--input-height` | Input height |
| `--input-radius` | Input radius |
| `--input-font-weight` | Input font weight |
| `--input-border-width` | Input border width |

---

### Toggle

| Variable | Description |
|---|---|
| `--toggle-border-width` | Toggle border width |
| `--toggle-width` | Toggle width |
| `--toggle-radius` | Toggle radius |
| `--toggle-thumb-color` | Toggle thumb background color |
| `--toggle-thumb-radius` | Toggle thumb radius |
| `--toggle-thumb-height` | Toggle thumb height |
| `--toggle-thumb-width` | Toggle thumb width |
| `--toggle-s-border-width` | Small toggle border width |
| `--toggle-s-width` | Small toggle width |
| `--toggle-s-thumb-height` | Small toggle thumb height |
| `--toggle-s-thumb-width` | Small toggle thumb width |

---

## Window

### Workspace

| Variable | Description |
|---|---|
| `--workspace-background-translucent` | Background for translucent windows |

---

### Window Frame

To see the title bar, change Settings > Appearance > Window frame style to Obsidian frame.

| Variable | Description |
|---|---|
| `--titlebar-background` | Titlebar background color |
| `--titlebar-background-focused` | Titlebar background color (focused window) |
| `--titlebar-border-width` | Titlebar border width |
| `--titlebar-border-color` | Titlebar border color |
| `--titlebar-text-color` | Titlebar text color |
| `--titlebar-text-color-focused` | Titlebar text color (focused window) |
| `--titlebar-text-weight` | Titlebar font weight |
| `--header-height` | Default height for frame elements |

---

### Divider

Dividers and resize handles between sidebars, tabs, and split panes.

| Variable | Description |
|---|---|
| `--divider-color` | Divider border color |
| `--divider-color-hover` | Divider border color (hover) |
| `--divider-width` | Divider border width |
| `--divider-width-hover` | Divider border width (hover) |
| `--divider-vertical-height` | Divider vertical height |

---

### Ribbon

| Variable | Description |
|---|---|
| `--ribbon-background` | Ribbon background color |
| `--ribbon-background-collapsed` | Ribbon background color (collapsed sidebar) |
| `--ribbon-width` | Ribbon width |
| `--ribbon-padding` | Ribbon padding |

---

### Status Bar

| Variable | Description |
|---|---|
| `--status-bar-background` | Status bar background color |
| `--status-bar-border-color` | Status bar border color |
| `--status-bar-border-width` | Status bar border width |
| `--status-bar-font-size` | Status bar font size |
| `--status-bar-text-color` | Status bar text color |
| `--status-bar-position` | Status bar `position` property |
| `--status-bar-radius` | Status bar radius |
| `--status-bar-scroll-padding` | Status bar scroll padding |

---

### Scrollbar

Custom scrollbars are only used on Windows and Linux.

| Variable | Description |
|---|---|
| `--scrollbar-bg` | Scrollbar background color |
| `--scrollbar-thumb-bg` | Scrollbar thumb background color |
| `--scrollbar-active-thumb-bg` | Scrollbar thumb background color (active) |

---

## Plugins

### Canvas

| Variable | Description |
|---|---|
| `--canvas-background` | Canvas background color |
| `--canvas-card-label-color` | Canvas card label text color |
| `--canvas-dot-pattern` | Canvas dot pattern color |
| `--canvas-color-1` | Canvas card color 1 |
| `--canvas-color-2` | Canvas card color 2 |
| `--canvas-color-3` | Canvas card color 3 |
| `--canvas-color-4` | Canvas card color 4 |
| `--canvas-color-5` | Canvas card color 5 |
| `--canvas-color-6` | Canvas card color 6 |

---

### File Explorer

Shares the same variables as Vault Profile.

| Variable | Description |
|---|---|
| `--vault-profile-display` | `display` property for the vault profile |
| `--vault-profile-actions-display` | `display` property for the action buttons in the vault profile |
| `--vault-profile-font-size` | Font size |
| `--vault-profile-font-weight` | Font weight |
| `--vault-profile-color` | Text color |
| `--vault-profile-color-hover` | Text color (hover) |

---

### Graph View

| Variable | Description |
|---|---|
| `--graph-controls-width` | Graph controls width |
| `--graph-text` | Node text color |
| `--graph-line` | Line color |
| `--graph-node` | Resolved node color |
| `--graph-node-unresolved` | Unresolved node color |
| `--graph-node-focused` | Focused node color |
| `--graph-node-tag` | Tag node color |
| `--graph-node-attachment` | Attachment node color |

---

### Search

| Variable | Description |
|---|---|
| `--search-clear-button-color` | Clear search button color |
| `--search-clear-button-size` | Clear search button size |
| `--search-icon-color` | Search magnifying glass icon color |
| `--search-icon-size` | Search icon size |
| `--search-result-background` | Search result background color |
