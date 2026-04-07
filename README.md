# Litos — Obsidian Theme

A modular Obsidian theme with academic aesthetics, Tufte-style sidenotes, and CJK font support.

## Getting Started

### As a Theme (recommended)

Clone or symlink this repo into your vault's theme directory:

```bash
# Clone
git clone https://github.com/zerokei/ObsidianSnippets \
  <vault>/.obsidian/themes/Litos

# Or symlink
ln -s /path/to/ObsidianSnippets <vault>/.obsidian/themes/Litos
```

Then enable in **Settings > Appearance > Themes > Litos**.

### As a CSS Snippet (via CDN)

```css
/* .obsidian/snippets/LitosSnippets.css */
@import url("https://zerokei.github.io/ObsidianSnippets/css/basic.css");
@import url("https://zerokei.github.io/ObsidianSnippets/css/callout.css");
@import url("https://zerokei.github.io/ObsidianSnippets/css/checkbox.css");
@import url("https://zerokei.github.io/ObsidianSnippets/css/mermaid.css");
@import url("https://zerokei.github.io/ObsidianSnippets/css/yaml.css");
@import url("https://zerokei.github.io/ObsidianSnippets/css/ui.css");
@import url("https://zerokei.github.io/ObsidianSnippets/css/sidenote.css");
```

Enable in **Settings > Appearance > CSS Snippets**.

## Structure

```
├── manifest.json            # Theme metadata
├── theme.css                # Entry point (imports all modules)
├── css/                     # Theme CSS modules
│   ├── basic.css            # Colors, typography, headings, links, code, highlights, blockquotes
│   ├── callout.css          # Callout styling and custom types
│   ├── checkbox.css         # Custom checkbox states (done, cancelled, question, in-progress)
│   ├── mermaid.css          # Mermaid diagram styling
│   ├── table.css            # Table centering and layout
│   ├── ui.css               # Workspace, tabs, ribbon, status bar, metadata
│   ├── sidenote.css         # Tufte-style responsive sidenotes
│   └── yaml.css             # Frontmatter display control
├── quartz/                  # Quartz static site specific (not part of theme)
│   ├── digital-garden.css
│   └── license.css
└── .claude/skills/          # Claude Code project-level skill
    └── obsidian-theme/
        ├── SKILL.md
        └── references/
```

## Fonts

### Present

- Default font
    - [LXGW Bright](https://github.com/lxgw/LxgwBright)
- Monospace font
    - [Jetbrains mono](https://github.com/JetBrains/JetBrainsMono)
- Kbd font
    - [Courier Prime](https://fonts.google.com/specimen/Courier+Prime)

### Previous

- [IntelOne mono](https://github.com/intel/intel-one-mono)
- [LXGW Wenkai Screen](https://github.com/lxgw/LxgwWenKai-Screen)

## Credits

- [Obsidian-Serenity](https://github.com/Bluemoondragon07/Obsidian-Serenity)
- [Gwern.net](https://gwern.net/about)
- [Obsidian-sidenote-auto-adjust-module](https://github.com/crnkv/obsidian-sidenote-auto-adjust-module/tree/master)