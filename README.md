# Litos — Obsidian Theme

An Obsidian theme with academic aesthetics, Tufte-style sidenotes, and CJK font support.

## Getting Started

Clone or symlink this repo into your vault's theme directory:

```bash
git clone https://github.com/zerokei/Litos \
  <vault>/.obsidian/themes/Litos
```

Then enable in **Settings > Appearance > Themes > Litos**.

## Structure

```
├── manifest.json            # Theme metadata
├── theme.css                # All styles (single file)
├── quartz/                  # Quartz static site specific (not part of theme)
│   ├── digital-garden.css
│   └── license.css
└── .claude/skills/          # Claude Code project-level skill
    └── obsidian-theme/
        ├── SKILL.md
        └── references/
```

## Fonts

This theme requires the following fonts to be installed manually:

- [LXGW Bright](https://github.com/lxgw/LxgwBright)
- [JetBrains Mono](https://github.com/JetBrains/JetBrainsMono)
- [Source Serif 4](https://fonts.google.com/specimen/Source+Serif+4)
- [Source Han Serif SC](https://github.com/adobe-fonts/source-han-serif)
- [Courier Prime](https://fonts.google.com/specimen/Courier+Prime)

## Credits

- [Obsidian-Serenity](https://github.com/Bluemoondragon07/Obsidian-Serenity)
- [Gwern.net](https://gwern.net/about)
- [Obsidian-sidenote-auto-adjust-module](https://github.com/crnkv/obsidian-sidenote-auto-adjust-module/tree/master)