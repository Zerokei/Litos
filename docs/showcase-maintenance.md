# Updating showcase images

Run this from the Litos theme repository:

```sh
./scripts/update-showcase
```

The command captures nine real Obsidian scenes, rebuilds both product covers, updates the theme gallery images, and copies the Companion cover into the sibling plugin repository. It produces a local Before / After comparison page. It never commits, pushes, or publishes.

## Requirements

- Obsidian running with its CLI enabled and available as `obsidian`.
- The development vault open with Litos and Litos Companion enabled.
- Existing `Litos Showcase/Reading.md`, `Workspace.md`, and `Connections.md`. The source notes are in `examples/brand/`; the capture command does not overwrite vault notes.
- Python 3 with venv support. The launcher creates an ignored local environment and installs the pinned packages on its first run.
- Source Serif 4 Regular and Semibold TTF files in `~/Library/Fonts`, or pass `--font-dir /path/to/fonts`.
- Cairo installed for SVG-to-PNG rendering (on macOS: `brew install cairo`).

Keep Obsidian free of dialogs and avoid interacting with it while capture is running. This workflow uses Obsidian's application APIs and was verified against 1.13.7; a future API change may require updating the capture adapter.

## Configuration

Edit `scripts/showcase/scenes.json` to choose the vault, Companion repository, viewport, and output scenes. Each scene names an existing note and an appearance (`moonstone` for light, `obsidian` for dark).

Optional scene fields: `diagrams`, `zen`, `leftSidebar`, `rightSidebar`, `headingAlignment`, `width`, and `height`. Sidebars and Zen mode default to off. Cover source images use 1160 × 760 CSS pixels; their dimensions must stay in sync with the cover composer.

Font choices and accent colors are inherited from the development vault. Use the same development vault settings for consistent batches.

## Review and recovery

```sh
# Generate the same assets without replacing repository images:
./scripts/update-showcase --preview-only

# Restore the saved workspace if the process or Obsidian was force-quit:
./scripts/update-showcase --restore .cache/showcase/<batch>/state.json
```

Each timestamped batch under `.cache/showcase/` contains:

- `comparison.html`: Before / After images.
- `generated/`: staged screenshots and composed assets.
- `state.json`: saved workspace layout, appearance, and Companion settings.
- `scenes.json` and `outputs.json`: capture configuration and output inventory.

The workspace and plugin settings are restored in a `finally` block, including after a failed capture. The temporary viewport override is cleared. After a force quit, restore the saved state before removing a stale `.cache/showcase.lock` directory.

Capture and composition must both succeed before repository images are replaced. Review text clipping, sidenotes, diagram labels, and both covers before committing. Existing native viewport overrides are not preserved: run this outside another capture/debugging session.

The screenshot API omits native macOS traffic lights. The existing cover composer adds those three dots to cover chrome; standalone screenshots remain unmodified. No screenshot-only theme styles are injected.
