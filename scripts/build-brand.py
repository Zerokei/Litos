"""Build MARGIN SVG assets. Requires fonttools and Source Serif 4 font files.
Usage: python scripts/build-brand.py /path/to/SourceSerif4-Regular.ttf /path/to/SourceSerif4-Semibold.ttf
Optional PNG previews: install cairosvg and pass --png.
"""
from pathlib import Path
import sys
from html import escape
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
regular, bold = [TTFont(p) for p in sys.argv[1:3]]
root = Path(__file__).resolve().parents[1]
out = root / 'assets/brand/margin'
out.mkdir(parents=True, exist_ok=True)
def word(text, x, y, size, color, font=regular, tracking=0):
    glyphs = font.getGlyphSet(); cmap = font.getBestCmap(); scale = size/font['head'].unitsPerEm
    parts = []; pos = 0
    for c in text:
        name = cmap[ord(c)]; pen = SVGPathPen(glyphs); glyphs[name].draw(pen)
        parts.append(f'<path d="{pen.getCommands()}" transform="translate({pos:.3f} 0)"/>')
        pos += font['hmtx'][name][0] + tracking/scale
    return f'<g fill="{color}" transform="translate({x} {y}) scale({scale} {-scale})">'+''.join(parts)+'</g>'
def mark(x,y,scale,ink,accent,companion=False):
    # Common geometry: two upright strokes and a horizontal marginal note.
    return f'<g transform="translate({x} {y}) scale({scale})" fill="{ink}"><path d="M8 28h8v56H8zM24 12h8v56h-8z"/><path fill="{accent}" d="M44 64h36v8H44z"/>'+ (f'<path fill="{accent}" d="M72 40h8v8h-8z"/>' if companion else '')+'</g>'
def save(name,w,h,body,title,bg=None):
    svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(title)}"><title>{escape(title)}</title>'
    if bg:svg+=f'<path fill="{bg}" d="M0 0h{w}v{h}H0z"/>'
    svg+=body+'</svg>\n';(out/name).write_text(svg)
    if '--png' in sys.argv:
        import cairosvg
        cairosvg.svg2png(bytestring=svg.encode(),write_to=str(out/name.replace('.svg','.png')))
for mode,ink,accent,bg in [('light','#242827','#397F7B','#F7F6F2'),('dark','#F7F6F2','#82BCB5','#202524'),('mono','#242827','#242827',None)]:
    for comp in [False,True]:
        product='Litos Companion' if comp else 'Litos'; slug='companion' if comp else 'litos'
        save(f'{slug}-mark-{mode}.svg',96,96,mark(0,0,1,ink,accent,comp),product+' mark')
        body=mark(0,0,1,ink,accent,comp)+word('Litos',116,70,72,ink,bold)
        if comp:body+=word('Companion',294,68,28,ink)
        save(f'{slug}-lockup-{mode}.svg',470 if comp else 310,96,body,product)
        if mode=='mono':continue
        body=mark(82,64,1,ink,accent,comp)
        body+=word('Litos',88,294,122,ink,bold)
        if comp:body+=word('Companion',91,351,40,ink)
        body+=f'<path stroke="{accent}" stroke-width="2" d="M770 80v340"/>'
        body+=word('Read.',821,185,40,ink)+word('Think.',821,247,40,ink)+word('Make it yours.',821,309,40,ink)
        body+=word('OPTIONAL PLUGIN FOR OBSIDIAN' if comp else 'A THEME FOR OBSIDIAN',92,442,15,ink,tracking=2)
        save(f'{slug}-cover-{mode}.svg',1280,512,body,product+' — Read. Think. Make it yours.',bg)
print('Built',len(list(out.glob('*.svg'))),'SVG assets')
