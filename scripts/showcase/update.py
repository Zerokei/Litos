"""Capture actual Obsidian scenes, restore the workspace, compose and compare assets."""
import argparse
import datetime
import html
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import struct
import time

ROOT = Path(__file__).resolve().parents[2]


def run(*args):
    result = subprocess.run(args, text=True, capture_output=True, timeout=60)
    if result.returncode:
        raise RuntimeError(result.stderr or result.stdout)
    return result.stdout.strip()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=ROOT / "scripts/showcase/scenes.json")
    parser.add_argument("--font-dir", type=Path, default=Path.home() / "Library/Fonts")
    parser.add_argument("--restore", type=Path, help="Restore a saved state.json after interruption")
    parser.add_argument("--preview-only", action="store_true", help="Generate comparison without replacing repository assets")
    args = parser.parse_args()
    config = json.loads(args.config.read_text())
    vault = config["vault"]

    def cli(command, *params):
        return run("obsidian", command, "vault=" + vault, *params)

    def evaluate(code):
        output = cli("eval", "code=" + code)
        # Obsidian CLI prefixes evaluation results with an arrow.
        payload = output.rsplit("=> ", 1)[-1]
        return json.loads(payload)

    def cdp(method, params=None):
        return cli("dev:cdp", "method=" + method, "params=" + json.dumps(params or {}))

    def restore(state):
        try:
            evaluate("""(async()=>{
                const s=%s,p=app.plugins.plugins["litos-companion"];
                app.vault.setConfig("theme",s.appearance);
                await p.updateSettings(s.settings);
                await app.workspace.changeLayout(s.layout);
                return JSON.stringify(true);
            })()""" % json.dumps(state))
        finally:
            cdp("Emulation.clearDeviceMetricsOverride")

    if args.restore:
        restore(json.loads(args.restore.read_text()))
        print("Workspace restored.")
        return

    # Preflight before changing the application.
    import cairosvg
    import fontTools
    fonts = [args.font_dir / ("SourceSerif4-" + weight + ".ttf") for weight in ("Regular", "Semibold")]
    for font in fonts:
        if not font.is_file():
            raise RuntimeError("Missing font: " + str(font) + ". Use --font-dir.")
    companion = (ROOT / config["companion"]).resolve()
    if not (companion / "manifest.json").is_file():
        raise RuntimeError("Companion repository missing: " + str(companion))
    state = evaluate("""JSON.stringify((()=>{
        const p=app.plugins.plugins["litos-companion"];
        if(!p || app.customCss.theme!=="Litos") throw Error("Enable Litos and Litos Companion first");
        if(document.querySelector(".modal-container")) throw Error("Close open dialogs first");
        return {layout:app.workspace.getLayout(),appearance:app.vault.getConfig("theme"),settings:p.store.value,
            themeVersion:app.customCss.themes?.Litos?.version,companionVersion:p.manifest.version};
    })())""")
    # Require existing showcase notes: never overwrite notes during a capture run.
    for scene in config["scenes"]:
        note = "Litos Showcase/" + scene["note"] + ".md"
        if not evaluate("JSON.stringify(!!app.vault.getAbstractFileByPath(" + json.dumps(note) + "))"):
            raise RuntimeError("Missing showcase note: " + note)

    stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    batch = ROOT / ".cache/showcase" / stamp
    stage = batch / "generated"
    assets = stage / "assets/brand"
    assets.mkdir(parents=True)
    (batch / "versions.json").write_text(json.dumps({
        "theme": json.loads((ROOT / "manifest.json").read_text()),
        "companion": json.loads((companion / "manifest.json").read_text())
    }, indent=2))
    (batch / "state.json").write_text(json.dumps(state, indent=2))
    (batch / "scenes.json").write_text(json.dumps(config, indent=2))
    lock = ROOT / ".cache/showcase.lock"
    try:
        lock.mkdir()
    except FileExistsError:
        raise RuntimeError("Another capture may be running. Remove .cache/showcase.lock only after restoring its state.")
    try:
        try:
            if sys.platform == "darwin":
                run("open", "-a", "Obsidian")
            for scene in config["scenes"]:
                print("Capturing " + scene["output"], flush=True)
                viewport = dict(config["viewport"])
                for key in ("width", "height"):
                    viewport[key] = scene.get(key, viewport[key])
                cdp("Emulation.setDeviceMetricsOverride", viewport)
                evaluate("""(async()=>{
                    const scene=%s,layout=%s;
                    layout.main.children=[{id:"showcase-tabs",type:"tabs",children:[{
                        id:"showcase-leaf",type:"leaf",state:{type:"markdown",state:{
                            file:"Litos Showcase/"+scene.note+".md",mode:"preview",source:false
                        }}
                    }]}];
                    layout.active="showcase-leaf";
                    if(layout.left) layout.left.collapsed=!scene.leftSidebar;
                    if(layout.right) layout.right.collapsed=!scene.rightSidebar;
                    app.vault.setConfig("theme",scene.appearance);
                    await app.plugins.plugins["litos-companion"].updateSettings({
                        zenMode:!!scene.zen,headingAlignment:scene.headingAlignment || "right",diagramsEnabled:!!scene.diagrams
                    });
                    await app.workspace.changeLayout(layout);
                    const active=app.workspace.getLeafById("showcase-leaf");
                    app.workspace.setActiveLeaf(active,{focus:true});
                    active.view.previewMode.rerender(true);
                    app.workspace.trigger("resize");
                    app.customCss.onRaw(app.customCss.getThemePath("Litos"));
                    return JSON.stringify(true);
                })()""" % (json.dumps(scene), json.dumps(state["layout"])))
                # Poll for actual rendered content, fonts, and enhanced Mermaid.
                deadline = time.monotonic() + 25
                while True:
                    ready = evaluate("""JSON.stringify((()=>{
                        const v=app.workspace.activeLeaf?.view;
                        const el=v?.containerEl.querySelector(".markdown-preview-view");
                        return !!el && el.getBoundingClientRect().width>0 &&
                            !!el.querySelector("h1") && document.fonts.status==="loaded" &&
                            !document.querySelector(".modal-container") &&
                            (%s ? !!el.querySelector("svg.litos-companion-diagram") : true);
                    })())""" % ("true" if scene.get("diagrams") else "false"))
                    if ready:
                        break
                    if time.monotonic() > deadline:
                        raise RuntimeError("Scene did not finish rendering: " + scene["output"])
                    time.sleep(.3)
                time.sleep(.7)
                cli("dev:screenshot", "path=" + str(assets / scene["output"]))
                image = assets / scene["output"]
                if not image.is_file():
                    raise RuntimeError("Screenshot was not written")
                data = image.read_bytes()
                expected = tuple(int(viewport[k] * viewport["deviceScaleFactor"]) for k in ("width", "height"))
                if data[:8] != b"\x89PNG\r\n\x1a\n" or struct.unpack(">II", data[16:24]) != expected:
                    raise RuntimeError("Screenshot dimensions do not match the configured viewport")
        finally:
            restore(state)
    finally:
        lock.rmdir()

    # Existing composers run in staging: failed capture/build never replaces published images.
    (stage / "scripts").mkdir()
    for name in ("build-brand.py", "build-product-covers.py"):
        shutil.copy2(ROOT / "scripts" / name, stage / "scripts" / name)
    run(sys.executable, str(stage / "scripts/build-product-covers.py"), *map(str, fonts), "--png")
    outputs = [(assets / s["output"], ROOT / "assets/brand" / s["output"]) for s in config["scenes"]]
    for slug in ("litos", "companion"):
        for ext in ("png", "svg"):
            src = assets / "margin" / (slug + "-product-cover." + ext)
            outputs.append((src, ROOT / "assets/brand/margin" / src.name))
            if slug == "companion":
                outputs.append((src, companion / "assets/brand" / src.name))
    outputs.append((assets / "margin/litos-product-cover.png", ROOT / "screenshot.png"))
    rows = []
    for index, (src, dest) in enumerate(outputs):
        if src.suffix == ".png":
            old = batch / ("before-" + str(index) + ".png")
            if dest.exists():
                shutil.copy2(dest, old)
            before = '<img src="' + old.name + '">' if old.exists() else "<p>New asset</p>"
            after = os.path.relpath(src, batch)
            rows.append("<h2>" + html.escape(str(dest.relative_to(dest.parents[2]))) +
                        '</h2><div class="pair"><section><h3>Before</h3>' + before +
                        '</section><section><h3>After</h3><img src="' + html.escape(after) + '"></section></div>')
    (batch / "comparison.html").write_text("""<!doctype html><meta charset="utf-8"><title>Litos showcase comparison</title>
<style>body{font:16px system-ui;background:#eceeea;color:#24302d;margin:32px}.pair{display:flex;gap:20px}
section{width:50%}img{width:100%;height:auto}h2{margin-top:40px;font-size:18px}</style>
<h1>Litos showcase update</h1><p>Before / After — inspect before committing.</p>""" + "".join(rows))
    if not args.preview_only:
        for src, dest in outputs:
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dest)
    (batch / "outputs.json").write_text(json.dumps([str(dest) for _, dest in outputs], indent=2))
    print("Comparison: " + str(batch / "comparison.html"))
    print("Preview only." if args.preview_only else "Theme and Companion assets updated. No commit or release created.")


if __name__ == "__main__":
    main()
