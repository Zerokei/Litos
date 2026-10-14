# Litos / MARGIN

## Identity

MARGIN is the selected visual direction: reading and thinking within a modern, restrained, customizable workspace. Two vertical strokes suggest text and its margin; the horizontal stroke represents a supporting note. Litos Companion adds one detached square while retaining the exact parent geometry.

Use **Litos** and **Litos Companion** as the product names. The second name should not be abbreviated on first introduction. This identity does not imply affiliation with Obsidian.

## Assets

Editable, self-contained SVG assets and PNG previews are in [assets/brand/margin](../../assets/brand/margin/). Lettering is outlined, so no installed font or network request is required to display them.

- `*-mark-*`: standalone symbols, 96 × 96.
- `*-lockup-*`: horizontal name-and-symbol combinations.
- `*-cover-*`: paired repository banners, 1280 × 512.
- `light`, `dark`, and `mono` identify the color treatment. Transparent dark variants are intended for dark backgrounds.

Companion assets are also copied into the plugin repository. Update both copies together when changing the shared geometry. No plugin build or theme stylesheet depends on these promotional assets.

## Color

| Role | Light treatment | Dark treatment |
| --- | --- | --- |
| Background | `#F7F6F2` | `#202524` |
| Foreground | `#242827` | `#F7F6F2` |
| Accent | `#397F7B` | `#82BCB5` |

These colors are for brand material. Do not force them onto the user's Obsidian appearance. Monochrome artwork must retain the detached Companion square.

## Typography

The wordmark uses Source Serif 4 Semibold. Supporting cover text uses Source Serif 4 Regular. Exported assets contain outlines, not font files. Source Serif is distributed under the [SIL Open Font License 1.1](https://github.com/adobe-fonts/source-serif/blob/release/LICENSE.md); its license explicitly distinguishes documents created with the font from font software.

Rebuild using `scripts/build-brand.py` with local Regular and Semibold font files and Python `fonttools`. Add `--png` with CairoSVG and the Cairo native library installed to render previews. The original geometry and composition live in that script; the raster concept board is not a production source.

## Sizing and placement

- Keep clear space of at least one stroke width around the standalone symbol.
- Use the mark at 24px or larger where possible. At 16px, the Companion square is subtle; use a text label whenever the product distinction matters.
- Keep the symbol proportions and relative stroke positions unchanged.
- Use the horizontal lockup at a height of at least 40px. Prefer the standalone mark below this size.
- Do not stretch, rotate, add shadows, or recolor individual strokes arbitrarily.
- The cover uses a wide margin and a single vertical divider. Keep text short and preserve this spacing.

## Voice and presentation

Proposed shared cover line: **Read. Think. Make it yours.**

Describe concrete features, and distinguish the theme from the optional plugin. Use actual application screenshots with disclosed settings. Keep README feature lists short; put full examples on a separate showcase page.

## Status

The MARGIN direction is selected. The selected direction is implemented in the vector assets and both repository READMEs. Product covers combine the shared identity with real application screenshots. Brand documentation updates do not change theme or plugin release versions.


## Product-led covers

`litos-product-cover` and `companion-product-cover` add real application screenshots to the MARGIN identity. They use a 1600 × 1000 composition: an identity column on the left and two parallel, offset light/dark windows on the right. The composition references the supplied Minimal cover; its logo, artwork, and screenshots are not reused.

Litos uses warm neutral surroundings and Chinese text with a sidenote. Companion uses a pale green neutral and an enhanced Mermaid diagram. Source screenshots were captured at 1160 × 760 CSS pixels and 2× resolution, with normal controls visible. Windows preserve the full screenshot aspect ratio; the rear image is intentionally overlapped by the foreground window.

The SVG files embed raster screenshots and outline lettering, so they are self-contained mixed-media compositions rather than all-vector artwork. Rebuild with `scripts/build-product-covers.py` and the same font arguments as the identity builder. PNG versions are provided for repository cover uploads. Original wordmark-only covers remain available.

Native macOS traffic lights, omitted by the application screenshot API, are added as vector circles to each product-cover window at the owner’s request. The captured note content remains unchanged.
