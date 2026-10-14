"""Compose real screenshots with the MARGIN identity.
Usage: python scripts/build-product-covers.py <SourceSerif4-Regular.ttf> <SourceSerif4-Semibold.ttf> [--png]
Requires fonttools; PNG export additionally needs CairoSVG and Cairo.
"""
from pathlib import Path
import base64
import runpy
import sys
root=Path(__file__).resolve().parents[1]
# Reuse the canonical lettering and mark generator rather than duplicating geometry.
brand=runpy.run_path(str(root/'scripts/build-brand.py'))
word,mark=brand['word'],brand['mark']
regular,bold=brand['regular'],brand['bold']
assets=root/'assets/brand'
out=assets/'margin'

def window(file,x,y,w,h,id):
    data=base64.b64encode((assets/file).read_bytes()).decode()
    shadow=''.join(f'<rect x="{x-i}" y="{y+8-i}" width="{w+2*i}" height="{h+2*i}" rx="{10+i}" fill="#101A18" opacity=".012"/>' for i in range(22,0,-2))
    # App captures omit native macOS controls; add them only to the cover chrome.
    scale=w/1160
    controls=''.join(f'<circle cx="{x+cx*scale}" cy="{y+20*scale}" r="{6*scale}" fill="{color}" stroke="#000000" stroke-opacity=".12" stroke-width="{.6*scale}"/>' for cx,color in [(16,'#FF5F57'),(36,'#FEBC2E'),(56,'#28C840')])
    # Preserve all captured content and its aspect ratio.
    return shadow+f'<defs><clipPath id="{id}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="9"/></clipPath></defs><image x="{x}" y="{y}" width="{w}" height="{h}" href="data:image/png;base64,{data}" clip-path="url(#{id})"/><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="9" fill="none" stroke="#788A84" stroke-opacity=".25"/>'+controls

for comp in [False,True]:
    name='Litos Companion' if comp else 'Litos';slug='companion' if comp else 'litos'
    ink='#24302D';accent='#397F7B';bg='#DCE4DF' if comp else '#EAE9E2'
    # Shared composition: two calm parallel windows, identity in the lower-left margin.
    body=f'<rect width="1600" height="1000" fill="{bg}"/>'
    body+=window('product-workspace-light.png' if comp else 'product-reading-light.png',488,64,1008,1008*760/1160,'back')
    body+=window('product-diagram-dark.png' if comp else 'product-reading-dark.png',624,324,928,928*760/1160,'front')
    body+=mark(68,460,1.15,ink,accent,comp)
    body+=word('Litos',73,660,116,ink,bold)
    if comp:body+=word('Companion',78,714,41,ink)
    body+=f'<path d="M80 770h42" stroke="{accent}" stroke-width="3"/>'
    body+=word('Read. Think.',78,812,25,ink)
    body+=word('Make it yours.',78,849,25,ink)
    body+=word('PLUGIN FOR OBSIDIAN' if comp else 'THEME FOR OBSIDIAN',80,941,13,ink,tracking=1.5)
    svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="1000" viewBox="0 0 1600 1000" role="img" aria-label="{name} product cover"><title>{name} — reading, thinking, and a workspace of your own</title>{body}</svg>'
    path=out/f'{slug}-product-cover.svg';path.write_text(svg)
    if '--png' in sys.argv:
        import cairosvg
        cairosvg.svg2png(bytestring=svg.encode(),write_to=str(path.with_suffix('.png')))
    print(path.name)
