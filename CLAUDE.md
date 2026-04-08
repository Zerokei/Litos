# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Litos is a single-file Obsidian CSS theme (academic aesthetics, Tufte-style sidenotes, CJK support). All styles live in `theme.css` — no build system.

## Key Rules

- **Dual-mode CSS**: Every style must target both Reading mode (`.markdown-rendered`) and Live Preview (`.cm-content` / `.cm-line`).
- **Edit `theme.css` directly**: Section comments like `/* === css/basic.css === */` are markers, not imports.
- **Use Obsidian CLI** (`obsidian eval`) for hot-reload and DOM inspection.

## References

- `.claude/skills/obsidian-theme/SKILL.md` — Development workflow and selector patterns
- `.claude/skills/obsidian-theme/references/css-variables.md` — Obsidian CSS variables
- `.claude/skills/obsidian-theme/references/selectors-guide.md` — DOM selectors and debugging
