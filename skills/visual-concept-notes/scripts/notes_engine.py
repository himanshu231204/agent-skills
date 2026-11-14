"""visual-concept-notes engine: handwritten-style A4 study notes (PDF) with SVG diagrams.

Usage (in a content file):
    from notes_engine import *
    configure(title="LLM Fundamentals", series="100 Days of AI Engineering", module="Module 1",
              units={1: "What an LLM Does", 2: "Tokens & Context"},
              links={"k": ("Label", "https://...")})
    add(cover_page(...)); add(page(1, "Title", body_html, kicker="Concept 1 · …")); ...
    build("Out_Name")      # writes Out_Name.html + Out_Name.pdf and prints a per-page fit report
"""
import html as _html, os, sys, glob, shutil, subprocess
from pathlib import Path

# ======================= configuration =======================
CFG = dict(title="Notes", series="Notes", module="", units={}, links={}, font_dir=None)
UNIT_COLORS = {0: "#23262f", 1: "#2f5fd0", 2: "#1f8a5b", 3: "#c2457a", 4: "#d97a1a", 5: "#d0453a",
               6: "#6d4ad1", 7: "#14857f", 8: "#9a5300", 9: "#3c5a99", 10: "#8e1f5a"}
RENDERS = []

def configure(**kw):
    CFG.update(kw)

def unit_name(u):
    return CFG["title"] if u == 0 else f"Unit {u} · {CFG['units'][u]}"

def add(render):
    RENDERS.append(render)

# ======================= text helpers =======================
def hl(t, c="y"):            # y=key term, g=definition/good, p=watch out/cost, b=technical name
    return f'<mark class="hl {c}">{t}</mark>'

def u(t):                    # wavy red underline = misconception
    return f'<span class="squiggle">{t}</span>'

def tag(t, c="b"):           # pill: b g r o
    return f'<span class="tag {c}">{t}</span>'

# ======================= icons =======================
ICON_PIN = '''<svg class="pin" viewBox="0 0 40 40"><circle cx="20" cy="13" r="10" fill="#e5484d" stroke="#8e1f22" stroke-width="2"/><circle cx="16.5" cy="9.5" r="3" fill="#ff9da0"/><path d="M20 23 L20 37" stroke="#555" stroke-width="2.4" stroke-linecap="round"/></svg>'''
ICON_BULB = '''<svg class="ic" viewBox="0 0 24 24"><path d="M12 2a7 7 0 0 0-4 12.7V17h8v-2.3A7 7 0 0 0 12 2z" fill="#ffd84d" stroke="#6b5200" stroke-width="1.4"/><rect x="8.5" y="18" width="7" height="2.2" rx="1" fill="#6b5200"/><rect x="9.5" y="21" width="5" height="1.6" rx=".8" fill="#6b5200"/></svg>'''
ICON_WARN = '''<svg class="ic" viewBox="0 0 24 24"><path d="M12 2 L23 21 H1 Z" fill="#ffb4ab" stroke="#a3271b" stroke-width="1.5" stroke-linejoin="round"/><rect x="11" y="8" width="2" height="7" rx="1" fill="#a3271b"/><circle cx="12" cy="18" r="1.3" fill="#a3271b"/></svg>'''
ICON_TRY = '''<svg class="ic" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" fill="#bff0d6" stroke="#1f7a4f" stroke-width="1.5"/><path d="M7 12.5 L10.5 16 L17 8.5" fill="none" stroke="#1f7a4f" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'''
ICON_LINK = '''<svg class="ic" viewBox="0 0 24 24"><rect x="1" y="1" width="22" height="22" rx="6" fill="#dbe6ff" stroke="#2f5fd0" stroke-width="1.4"/><path d="M10 14 L14 10 M9 11 L7.5 12.5 a2.5 2.5 0 0 0 3.5 3.5 L12.5 14.5 M15 13 L16.5 11.5 a2.5 2.5 0 0 0-3.5-3.5 L11.5 9.5" fill="none" stroke="#2f5fd0" stroke-width="1.6" stroke-linecap="round"/></svg>'''
ICON_STAR = '''<svg class="ic" viewBox="0 0 24 24"><path d="M12 2l3 6.5 7 .8-5.2 4.8 1.5 7-6.3-3.6-6.3 3.6 1.5-7L2 9.3l7-.8z" fill="#ffd84d" stroke="#6b5200" stroke-width="1.3" stroke-linejoin="round"/></svg>'''

# ======================= boxes =======================
def pin(title, body):
    return f'<div class="box pinbox">{ICON_PIN}<div class="box-h">{title}</div><div class="box-b">{body}</div></div>'
def analogy(body, title="Think of it like…"):
    return f'<div class="box analogy"><div class="box-h">{ICON_BULB} {title}</div><div class="box-b">{body}</div></div>'
def warn(body, title="Common mistake"):
    return f'<div class="box warn"><div class="box-h">{ICON_WARN} {title}</div><div class="box-b">{body}</div></div>'
def tryit(body, title="Try it"):
    return f'<div class="box tryit"><div class="box-h">{ICON_TRY} {title}</div><div class="box-b">{body}</div></div>'
def key(body, title="Key idea"):
    return f'<div class="box keyb"><div class="box-h">{ICON_STAR} {title}</div><div class="box-b">{body}</div></div>'
def sticky(body, title="Remember", rot=-1.5, color="yellow"):   # yellow pink green blue
    return f'<div class="sticky {color}" style="transform:rotate({rot}deg)"><div class="st-h">{title}</div>{body}</div>'
def margin(t):
    return f'<div class="mnote">{t}</div>'
def formula(t):
    return f'<div class="formula">{t}</div>'
def cols(*parts, ratio=None):
    style = f' style="grid-template-columns:{ratio}"' if ratio else ''
    return f'<div class="cols"{style}>' + "".join(f'<div>{p}</div>' for p in parts) + '</div>'
def fig(svg_html, cap=None):
    c = f'<figcaption>{cap}</figcaption>' if cap else ''
    return f'<figure>{svg_html}{c}</figure>'
def table(head, rows, cls=""):   # cls="logtbl" → fill-in rows; "logtbl tall" → taller rows
    th = "".join(f"<th>{h}</th>" for h in head)
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<table class="tbl {cls}"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table>'
def h2(t):
    return f'<h2>{t}</h2>'
def lead(t):
    return f'<p class="lead">{t}</p>'

def links(*keys):
    L = CFG["links"]
    items = "".join(
        f'<li><a href="{L[k][1]}">{_html.escape(L[k][0])}</a><span class="url">{_html.escape(L[k][1].replace("https://", ""))}</span></li>'
        for k in keys)
    return f'<div class="learn">{ICON_LINK}<div><div class="learn-h">Learn more</div><ul>{items}</ul></div></div>'

# ======================= SVG helpers =======================
INK = "#23262f"
P = dict(y="#fff3a8", b="#d6e4ff", g="#c9f2dc", p="#ffd6e3", v="#e4dbff", o="#ffe2c2", w="#ffffff", gr="#eceae4", r="#ffcdc7", t="#c8f1ef")
S = dict(b="#2f5fd0", g="#1f8a5b", r="#d0453a", o="#d97a1a", v="#6d4ad1", p="#c2457a", t="#14857f", gr="#8a877f")
FONTS = {"sans": "Inter", "hand": "Kalam", "script": "Caveat", "mono": "DejaVu Sans Mono", "deva": "Noto Sans Devanagari"}

def svg(w, h, inner):
    return f'<svg class="fig" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">{inner}</svg>'

def t(x, y, s, size=15, anchor="middle", weight=400, color=INK, font="sans", italic=False, lh=None):
    lines = str(s).split("\n")
    lh = lh or size * 1.25
    y0 = y - (len(lines) - 1) * lh / 2
    st = ' font-style="italic"' if italic else ''
    spans = "".join(f'<tspan x="{x}" y="{y0 + i * lh:.1f}">{ln}</tspan>' for i, ln in enumerate(lines))
    return f'<text font-family="{FONTS[font]}" font-size="{size}" font-weight="{weight}" fill="{color}" text-anchor="{anchor}" dominant-baseline="middle"{st}>{spans}</text>'

def box(x, y, w, h, fill="w", label=None, size=15, rx=10, stroke=INK, sw=2, weight=600, font="sans", color=INK, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    out = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{P.get(fill, fill)}" stroke="{stroke}" stroke-width="{sw}"{d}/>'
    if label is not None:
        out += t(x + w / 2, y + h / 2, label, size=size, weight=weight, font=font, color=color)
    return out

def circ(cx, cy, r, fill="w", label=None, size=14, stroke=INK, sw=2, weight=600):
    out = f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{P.get(fill, fill)}" stroke="{stroke}" stroke-width="{sw}"/>'
    if label is not None:
        out += t(cx, cy, label, size=size, weight=weight)
    return out

def arrow(x1, y1, x2, y2, color=INK, sw=2.2, dash=None, head=True):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    m = ' marker-end="url(#ah)"' if head else ''
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{sw}" stroke-linecap="round"{d}{m}/>'

def curve(d, color=INK, sw=2.2, dash=None, head=True, fill="none"):
    ds = f' stroke-dasharray="{dash}"' if dash else ''
    m = ' marker-end="url(#ah)"' if head else ''
    return f'<path d="{d}" fill="{fill}" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"{ds}{m}/>'

def line(x1, y1, x2, y2, color=INK, sw=2, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{sw}" stroke-linecap="round"{d}/>'

def hbar(x, y, w, h, fill, label=None, val=None, size=13):
    out = f'<rect x="{x}" y="{y}" width="{max(w,1)}" height="{h}" rx="4" fill="{P.get(fill, fill)}" stroke="{INK}" stroke-width="1.6"/>'
    if label: out += t(x - 10, y + h / 2, label, size=size, anchor="end", weight=500)
    if val: out += t(x + w + 8, y + h / 2, val, size=size, anchor="start", weight=700)
    return out

def check(x, y, color=None):
    return f'<path d="M{x} {y} l6 6 l12 -12" fill="none" stroke="{color or S["g"]}" stroke-width="3" stroke-linecap="round"/>'

def cross(x, y, s=12, color=None):
    c = color or S["r"]
    return line(x, y - s / 2, x + s, y + s / 2, c, 3) + line(x + s, y - s / 2, x, y + s / 2, c, 3)

def marker_hl(x, y, w, h=14, color="#ffe66d"):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="3" fill="{color}" opacity=".75" transform="rotate(-1 {x} {y})"/>'

def flow(labels, fills=None, w=106, h=64, gap=20, y=20, size=15):
    """Horizontal chain of boxes with arrows. Returns (svg_inner, total_width)."""
    s = ""; x = 10; fills = fills or ["y", "b", "g", "v", "p", "o", "t"]
    for i, lab in enumerate(labels):
        s += box(x, y, w, h, fills[i % len(fills)], lab, size=size, weight=700)
        if i < len(labels) - 1:
            s += arrow(x + w + 2, y + h / 2, x + w + gap - 2, y + h / 2)
        x += w + gap
    return s, x - gap + 10

def card_grid(items, cols_=3, w=212, h=98, gx=16, gy=14, size=15):
    """items = [(title, subtitle, fill)] → grid of cards."""
    s = ""
    for i, (hd, sub, c) in enumerate(items):
        x = 10 + (i % cols_) * (w + gx); y = 10 + (i // cols_) * (h + gy)
        s += box(x, y, w, h, c) + t(x + w / 2, y + 30, hd, size=size, weight=800) + t(x + w / 2, y + h - 30, sub, size=12.5, color="#3c3f48")
    rows = (len(items) + cols_ - 1) // cols_
    return svg(10 + cols_ * (w + gx), 10 + rows * (h + gy), s)

GLOBAL_DEFS = f'''<svg width="0" height="0" style="position:absolute"><defs>
<marker id="ah" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="{INK}"/></marker>
</defs></svg>'''

# ======================= page types =======================
def _shell(unit, inner, n, cls=""):
    col = UNIT_COLORS[unit % len(UNIT_COLORS)]
    mod = " · ".join(x for x in [CFG["module"], CFG["title"]] if x)
    return f'''<section class="page {cls}" style="--accent:{col}">
<div class="margin-line"></div>
<header class="ph"><span class="ph-unit" style="background:{col}">{unit_name(unit)}</span><span class="ph-mod">{mod}</span></header>
{inner}
<footer class="pf"><span>{CFG["series"]} · Notes</span><span class="pnum">{n}</span></footer>
</section>'''

def page(unit, title, body, kicker=None, toc=True):
    def render(n):
        col = UNIT_COLORS[unit % len(UNIT_COLORS)]
        k = f'<div class="kicker" style="color:{col}">{kicker}</div>' if kicker else ''
        return _shell(unit, f'<div class="content">{k}<h1 class="pt">{title}</h1>{body}</div>', n)
    render.toc = (title, unit) if toc else None
    return render

def divider(unit, title, day, concepts, outcome, art_svg, extra=""):
    def render(n):
        col = UNIT_COLORS[unit % len(UNIT_COLORS)]
        items = "".join(f'<li><span class="dn">{i+1:02d}</span>{c}</li>' for i, c in enumerate(concepts))
        inner = f'''<div class="content">
  <div class="dv-top"><div class="dv-num" style="color:{col}">{unit:02d}</div><div><div class="kicker" style="color:{col}">{day}</div><h1 class="pt dv-title">{title}</h1></div></div>
  <div class="dv-art">{art_svg}</div>
  <div class="cols" style="grid-template-columns:1.1fr 1fr">
    <div class="box pinbox">{ICON_PIN}<div class="box-h">Concepts in this unit</div><ul class="dv-list">{items}</ul></div>
    <div>{sticky(outcome, "By the end you can…", rot=1.2)}</div>
  </div>
  {extra}
</div>'''
        return _shell(unit, inner, n, "divider")
    render.toc = ("§" + f"{unit:02d} · {title}", unit)
    return render

def word_tags(words):
    return '<div class="dv-tags"><span class="mnote">words you\'ll meet →</span> ' + " ".join(tag(w, "bgor"[i % 4]) for i, w in enumerate(words)) + '</div>'

def cover_page(subtitle, art_svg, outcome, prereq="", kicker_right=""):
    def render(n):
        units = "".join(f'<div class="cv-u" style="border-color:{UNIT_COLORS[i]}"><span style="color:{UNIT_COLORS[i]}">{i:02d}</span>{nm}</div>' for i, nm in CFG["units"].items())
        return f'''<section class="page cover" style="--accent:#2f5fd0"><div class="margin-line"></div><div class="content">
  <div class="cv-top"><span class="ph-unit" style="background:#23262f">{CFG["series"].upper()}</span><span class="cv-mod">{kicker_right}</span></div>
  <div class="cv-title">{CFG["title"].replace(" ", "<br>", 1) if len(CFG["title"]) > 14 else CFG["title"]}</div>
  <div class="cv-sub">{subtitle}</div>
  <div class="cv-art">{art_svg}</div>
  <div class="cv-units">{units}</div>
  {sticky(outcome, "By the end of these notes you can…", rot=-1.2)}
  <div class="cv-foot">{prereq}</div>
</div></section>'''
    render.toc = None
    return render

def how_to_use_page():
    legend = cols(
        pin("Concept pin", "The one idea to remember from the page. If you only read one box, read this one.")
        + "<div style='height:3.4mm'></div>" + analogy("An everyday comparison that makes the idea click.")
        + "<div style='height:3.4mm'></div>" + warn("A mistake beginners (and teams) make often.")
        + "<div style='height:3.4mm'></div>" + tryit("A small hands-on task. Do it; it sticks 10× better."),
        key("A practical rule or the part that matters most in real work.")
        + "<div style='height:3.4mm'></div>" + sticky("A short fact to memorise or a quick tip.", "Sticky note", rot=-1.2)
        + "<div style='height:4.4mm'></div>" + f'<div class="learn">{ICON_LINK}<div><div class="learn-h">Learn more</div><ul><li><a href="#">Best video / article for going deeper</a></li></ul></div></div>'
        + "<div style='height:3.4mm'></div><p class='small'>Links are clickable in the PDF.</p>")
    hl_rows = table(["Highlight", "Means"], [[hl("yellow"), "key term or main point"], [hl("green", "g"), "definition / the good way"],
        [hl("pink", "p"), "watch out / cost / risk"], [hl("blue", "b"), "technical name you'll hear again"], [u("wavy red"), "common misconception"]])
    return page(0, "How to use these notes", f'''
{lead(f'Each page = {hl("one concept")}. Read the title, look at the picture, read the {hl("pin box", "g")}. That\'s the core. Everything else helps it stick.')}
{legend}{hl_rows}
{key("Read the unit → do the <b>Try it</b> boxes → watch one “Learn more” link → answer the recap quiz without looking.", "Study rhythm")}''',
        kicker="Start here", toc=False)

def contents_page():
    def render(n):
        rows = ""
        for title, p, unit in TOC:
            col = UNIT_COLORS[unit % len(UNIT_COLORS)]
            if title.startswith("§"):
                rows += f'<div class="toc-u" style="color:{col}; border-color:{col}"><span>{title[1:]}</span><span>{p}</span></div>'
            else:
                rows += f'<div class="toc-r"><span>{title}</span><span class="toc-dots"></span><span>{p}</span></div>'
        return _shell(0, f'<div class="content toc"><h1 class="pt">Contents</h1><div class="toc-cols">{rows}</div></div>', n)
    render.toc = None
    return render

def mini(title, items, unit):
    col = UNIT_COLORS[unit % len(UNIT_COLORS)]
    return f'<div class="mini" style="border-color:{col}"><div class="mini-h" style="background:{col}">{title}</div><ul>' + "".join(f"<li>{i}</li>" for i in items) + "</ul></div>"

def resources_page(groups, title="All resources in one place"):
    L = CFG["links"]; out = ""
    for name, ks in groups:
        lis = "".join(f'<li><a href="{L[k][1]}">{_html.escape(L[k][0])}</a><span class="url">{L[k][1].replace("https://", "")}</span></li>' for k in ks)
        out += f'<div class="rg"><div class="rg-h">{name}</div><ul>{lis}</ul></div>'
    return page(0, title, f'{lead("Every link from these notes, grouped. Videos first, interactive tools to see it happen, docs for exact numbers.")}<div class="rgs">{out}</div>', kicker="Go deeper")

def glossary_page(terms):
    half = (len(terms) + 1) // 2
    mk = lambda part: table(["Term", "In simple words"], [[f"<b>{a}</b>", b] for a, b in part])
    return page(0, "Glossary", f'{lead(f"Every term in {hl("one line")}. Confused by a word in a video or blog? Check here first.")}{cols(mk(terms[:half]), mk(terms[half:]))}', kicker="Look it up")

TOC = []

# ======================= CSS =======================
def _css():
    fd = CFG["font_dir"] or find_font_dir()
    ff = ""
    if fd:
        ff = f"""
@font-face {{ font-family: Kalam; font-weight: 400; src: url('file://{fd}/kalam/files/kalam-latin-400-normal.woff2'); }}
@font-face {{ font-family: Kalam; font-weight: 700; src: url('file://{fd}/kalam/files/kalam-latin-700-normal.woff2'); }}
@font-face {{ font-family: Caveat; font-weight: 400; src: url('file://{fd}/caveat/files/caveat-latin-400-normal.woff2'); }}
@font-face {{ font-family: Caveat; font-weight: 700; src: url('file://{fd}/caveat/files/caveat-latin-700-normal.woff2'); }}
@font-face {{ font-family: 'Noto Sans Devanagari'; font-weight: 400; src: url('file://{fd}/noto-sans-devanagari/files/noto-sans-devanagari-devanagari-400-normal.woff2'); }}"""
    return ff + CSS

CSS = """
@page { size: A4; margin: 0; }
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; }
body { font-family: Inter, 'DejaVu Sans', sans-serif; color: #23262f; font-size: 11pt; line-height: 1.5; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
.page { width: 210mm; height: 297mm; position: relative; overflow: hidden; break-after: page; page-break-after: always;
  background-color: #fffdf6; background-image: radial-gradient(#d9d4c4 0.9px, transparent 0.9px); background-size: 6mm 6mm; background-position: 3mm 3mm; }
.page:last-child { break-after: auto; page-break-after: auto; }
.margin-line { position: absolute; left: 13mm; top: 0; bottom: 0; width: 0; border-left: 1.4px solid #f2a3a3; }
.ph { position: absolute; top: 8mm; left: 18mm; right: 14mm; display: flex; justify-content: space-between; align-items: center; font-size: 8.5pt; }
.ph-unit { color: #fff; padding: 1.2mm 3mm; border-radius: 2mm; font-weight: 600; letter-spacing: .02em; }
.ph-mod { color: #8a877f; font-weight: 500; }
.pf { position: absolute; bottom: 7mm; left: 18mm; right: 14mm; display: flex; justify-content: space-between; align-items: center; font-size: 8pt; color: #8a877f; }
.pnum { font-family: Kalam; font-weight: 700; font-size: 13pt; color: var(--accent); border: 1.6px solid var(--accent); border-radius: 50%; width: 9mm; height: 9mm; display: flex; align-items: center; justify-content: center; background: #fff; }
.content { position: absolute; top: 17mm; left: 18mm; right: 14mm; bottom: 18mm; display: flex; flex-direction: column; gap: 3.2mm; justify-content: space-between; }
.content > .pt { margin-bottom: 1mm; }
.kicker { font-family: Caveat; font-size: 17pt; font-weight: 700; line-height: 1; margin-bottom: -2mm; }
h1.pt { font-family: Kalam; font-weight: 700; font-size: 23pt; line-height: 1.15; margin: 0; color: #1d2030; }
h1.pt::after { content: ""; display: block; width: 46mm; height: 2.2mm; margin-top: .8mm; background: var(--accent); opacity: .35; border-radius: 2mm; transform: rotate(-.6deg); }
h2 { font-family: Kalam; font-weight: 700; font-size: 14.5pt; margin: 0; color: #1d2030; }
p { margin: 0; }
.lead { font-size: 11.8pt; }
mark.hl { color: inherit; padding: 0 .9mm; border-radius: 1mm; background: linear-gradient(104deg, rgba(255,230,80,0) 0.5%, rgba(255,230,80,.85) 2.5%, rgba(255,226,70,.7) 94%, rgba(255,230,80,0) 99%); }
mark.hl.g { background: linear-gradient(104deg, rgba(120,230,170,0) 0.5%, rgba(120,230,170,.75) 2.5%, rgba(120,230,170,.6) 94%, rgba(120,230,170,0) 99%); }
mark.hl.p { background: linear-gradient(104deg, rgba(255,150,190,0) 0.5%, rgba(255,150,190,.7) 2.5%, rgba(255,150,190,.55) 94%, rgba(255,150,190,0) 99%); }
mark.hl.b { background: linear-gradient(104deg, rgba(130,180,255,0) 0.5%, rgba(130,180,255,.65) 2.5%, rgba(130,180,255,.5) 94%, rgba(130,180,255,0) 99%); }
.squiggle { text-decoration: underline wavy #d0453a; text-decoration-thickness: 1.3px; text-underline-offset: 2px; }
.tag { display: inline-block; font-size: 8.4pt; font-weight: 600; padding: .2mm 2mm; border-radius: 3mm; border: 1.2px solid; line-height: 1.5; }
.tag.b { color: #2f5fd0; border-color: #2f5fd0; background: #eef3ff; } .tag.g { color: #1f7a4f; border-color: #1f7a4f; background: #eafaf1; }
.tag.r { color: #a3271b; border-color: #a3271b; background: #fff0ee; } .tag.o { color: #9a5300; border-color: #9a5300; background: #fff4e6; }
.box { position: relative; border-radius: 3mm; padding: 2.6mm 3.6mm 2.8mm; }
.box-h { font-family: Kalam; font-weight: 700; font-size: 12.5pt; display: flex; align-items: center; gap: 1.6mm; line-height: 1.25; margin-bottom: .8mm; }
.box-b { font-size: 10.9pt; }
.box-b ul, .box-b ol { margin: .6mm 0 0; padding-left: 5mm; } .box-b li { margin: .4mm 0; }
.ic { width: 5.2mm; height: 5.2mm; flex: none; }
.pinbox { background: #fff; border: 2px solid #23262f; box-shadow: 1.6mm 1.6mm 0 var(--accent); padding-left: 9mm; }
.pinbox .box-h { font-size: 13.5pt; color: var(--accent); }
.pin { position: absolute; left: -2.6mm; top: -3.6mm; width: 9mm; height: 9mm; transform: rotate(-18deg); }
.analogy { background: #fff8d9; border: 1.8px dashed #b38f00; }
.warn { background: #fff0ee; border: 1.8px solid #d0453a; border-left-width: 2.2mm; }
.tryit { background: #ecfbf3; border: 1.8px solid #1f8a5b; }
.keyb { background: #eef3ff; border: 1.8px solid #2f5fd0; }
.sticky { font-family: Kalam; font-size: 11.6pt; line-height: 1.35; padding: 3mm 4mm; box-shadow: 0 1.4mm 2.4mm rgba(0,0,0,.18); position: relative; }
.sticky::before { content: ""; position: absolute; top: -2.6mm; left: 50%; width: 16mm; height: 5mm; margin-left: -8mm; background: rgba(255,255,255,.6); border: 1px solid rgba(0,0,0,.07); transform: rotate(2deg); }
.sticky.yellow { background: #fff27a; } .sticky.pink { background: #ffc6dc; } .sticky.green { background: #c4f2c8; } .sticky.blue { background: #cfe3ff; }
.st-h { font-family: Caveat; font-weight: 700; font-size: 16pt; line-height: 1; margin-bottom: 1mm; }
.mnote { font-family: Caveat; font-size: 14.5pt; color: #c2457a; line-height: 1.1; }
.formula { font-family: 'DejaVu Sans Mono', monospace; font-size: 10.2pt; background: #23262f; color: #fdf6d8; padding: 2.4mm 3.6mm; border-radius: 2.4mm; white-space: pre-wrap; line-height: 1.55; }
.cols { display: grid; grid-template-columns: 1fr 1fr; gap: 4mm; align-items: start; }
figure { margin: 0; text-align: center; }
svg.fig { width: 100%; height: auto; display: block; }
figcaption { font-family: Caveat; font-size: 13.5pt; color: #5d5a52; margin-top: .4mm; line-height: 1.1; }
.learn { display: flex; gap: 2.4mm; align-items: flex-start; background: #f2f6ff; border: 1.4px solid #9db6f0; border-radius: 3mm; padding: 2.2mm 3.2mm; }
.learn-h { font-family: Kalam; font-weight: 700; font-size: 11.5pt; color: #2f5fd0; line-height: 1.2; }
.learn ul { margin: .4mm 0 0; padding: 0; list-style: none; }
.learn li { font-size: 9.4pt; line-height: 1.4; margin: .5mm 0; }
.learn a, .rg a { color: #1d3f99; font-weight: 600; text-decoration: none; border-bottom: 1px solid #9db6f0; }
.learn .url, .rg .url { color: #6b7896; font-size: 7.8pt; margin-left: 2mm; }
.tbl { width: 100%; border-collapse: separate; border-spacing: 0; font-size: 10.3pt; background: #fff; border: 1.8px solid #23262f; border-radius: 2.6mm; overflow: hidden; }
.tbl th { background: var(--accent); color: #fff; text-align: left; padding: 1.6mm 2.4mm; font-weight: 600; }
.tbl td { padding: 1.4mm 2.4mm; border-top: 1px solid #e3dfd3; vertical-align: top; }
.tbl tr:nth-child(even) td { background: #faf8f1; }
.logtbl td { height: 7mm; } .logtbl.tall td { height: 9.4mm; }
.small { font-size: 9.2pt; color: #5d5a52; }
.check li { list-style: none; position: relative; }
.check li::before { content: ""; position: absolute; left: -5mm; top: 1.1mm; width: 3mm; height: 3mm; border: 1.4px solid #23262f; border-radius: .8mm; background: #fff; }
ul.plain { margin: 0; padding-left: 5mm; } ul.plain li { margin: .6mm 0; }
code { font-family: 'DejaVu Sans Mono', monospace; font-size: .9em; background: #f1eee5; padding: 0 1mm; border-radius: 1mm; }
.divider .content { gap: 6mm; }
.dv-top { display: flex; align-items: center; gap: 6mm; margin-top: 1mm; }
.dv-top .kicker { margin-bottom: 1.5mm; }
.dv-num { font-family: Kalam; font-weight: 700; font-size: 80pt; line-height: .9; opacity: .9; }
.dv-title { font-size: 30pt !important; }
.dv-list { list-style: none; margin: 1mm 0 0; padding: 0; }
.dv-list li { font-size: 10.6pt; margin: .7mm 0; display: flex; gap: 2.4mm; align-items: baseline; }
.dv-tags { display: flex; flex-wrap: wrap; gap: 1.6mm; align-items: center; }
.dn { font-family: Kalam; font-weight: 700; color: var(--accent); font-size: 11pt; }
.cover .content { top: 16mm; justify-content: flex-start; gap: 6mm; }
.cv-top { display: flex; justify-content: space-between; align-items: center; }
.cv-mod { font-family: Kalam; font-weight: 700; color: #2f5fd0; font-size: 12pt; }
.cv-title { font-family: Kalam; font-weight: 700; font-size: 56pt; line-height: .98; color: #1d2030; margin-top: 6mm; }
.cv-sub { font-size: 13pt; max-width: 150mm; }
.cv-units { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 3mm; }
.cv-u { border: 2px solid; border-radius: 3mm; padding: 2.4mm 3mm; font-weight: 600; font-size: 10.5pt; background: #fff; display: flex; gap: 2mm; align-items: baseline; }
.cv-u span { font-family: Kalam; font-weight: 700; font-size: 13pt; }
.cv-foot { margin-top: auto; font-size: 9.5pt; color: #5d5a52; }
.cover .sticky { max-width: 130mm; margin: 4mm 0 0 8mm; font-size: 12.5pt; }
.toc { justify-content: flex-start !important; }
.toc-cols { columns: 2; column-gap: 9mm; font-size: 9.8pt; }
.toc-u { break-inside: avoid; display: flex; justify-content: space-between; font-family: Kalam; font-weight: 700; font-size: 12pt; border-bottom: 2px solid; margin: 3.2mm 0 1.2mm; }
.toc-u:first-child { margin-top: 0; }
.toc-r { display: flex; gap: 1.4mm; align-items: baseline; line-height: 1.55; break-inside: avoid; }
.toc-dots { flex: 1; border-bottom: 1.2px dotted #b9b3a3; transform: translateY(-1mm); }
.mini { border: 2px solid; border-radius: 3mm; background: #fff; overflow: hidden; }
.mini-h { color: #fff; font-family: Kalam; font-weight: 700; font-size: 13pt; padding: 1mm 3.4mm; }
.mini ul { margin: 1.6mm 0 2mm; padding-left: 7mm; font-size: 10.4pt; } .mini li { margin: .5mm 0; }
.rgs { display: flex; flex-direction: column; gap: 2mm; }
.rg { background: #fff; border: 1.6px solid #23262f; border-radius: 3mm; padding: 2mm 3.4mm; }
.rg-h { font-family: Kalam; font-weight: 700; font-size: 12.5pt; color: #2f5fd0; }
.rg ul { margin: .6mm 0 0; padding-left: 4.6mm; } .rg li { font-size: 9.2pt; line-height: 1.38; }
"""

# ======================= setup & build =======================
def find_font_dir():
    for c in [os.environ.get("NOTES_FONT_DIR", ""), str(Path.cwd() / "fonts/node_modules/@fontsource"),
              str(Path(__file__).parent / "fonts/node_modules/@fontsource")]:
        if c and Path(c, "kalam").exists():
            return c
    return None

def setup_fonts(dest=None):
    """npm-install the handwriting + Devanagari fonts next to this file (once)."""
    dest = Path(dest or Path(__file__).parent / "fonts")
    if (dest / "node_modules/@fontsource/kalam").exists():
        return str(dest / "node_modules/@fontsource")
    dest.mkdir(parents=True, exist_ok=True)
    subprocess.run(["npm", "i", "--silent", "--prefix", str(dest), "@fontsource/caveat", "@fontsource/kalam", "@fontsource/noto-sans-devanagari"], check=True)
    return str(dest / "node_modules/@fontsource")

def find_chrome():
    for c in [os.environ.get("CHROME_PATH", ""), "/usr/bin/google-chrome", "/usr/bin/chromium", "/usr/bin/chromium-browser",
              "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"]:
        if c and Path(c).exists():
            return c
    return None  # fall back to playwright's bundled chromium

def build(out_name, min_pages=None, max_pages=None):
    if not CFG["font_dir"]:
        CFG["font_dir"] = find_font_dir() or setup_fonts()
    TOC.clear()
    for i, r in enumerate(RENDERS):
        if getattr(r, "toc", None):
            TOC.append((r.toc[0], i + 1, r.toc[1]))
    html_doc = f"<!doctype html><html><head><meta charset='utf-8'><style>{_css()}</style></head><body>{GLOBAL_DEFS}{''.join(r(i + 1) for i, r in enumerate(RENDERS))}</body></html>"
    out = Path(out_name).resolve()
    out.with_suffix(".html").write_text(html_doc, encoding="utf-8")
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        exe = find_chrome()
        b = p.chromium.launch(**({"executable_path": exe} if exe else {}), args=["--no-sandbox", "--allow-file-access-from-files"])
        pg = b.new_page()
        pg.goto(f"file://{out.with_suffix('.html')}")
        pg.wait_for_timeout(800)
        pg.evaluate("document.fonts.ready")
        rep = pg.evaluate("""() => {
          const res = [];
          document.querySelectorAll('section.page').forEach((s, i) => {
            const c = s.querySelector('.content');
            const kids = [...c.children]; let used = 0;
            kids.forEach(k => used += k.getBoundingClientRect().height);
            res.push({page: i + 1, over: c.scrollHeight - c.clientHeight, wide: c.scrollWidth - c.clientWidth,
                      free: Math.round(c.clientHeight - used - 12 * (kids.length - 1))});
          });
          return {res, fonts: [...document.fonts].map(f => f.family + ':' + f.status)};
        }""")
        pg.pdf(path=str(out.with_suffix(".pdf")), prefer_css_page_size=True, print_background=True)
        b.close()
    print(f"pages: {len(RENDERS)}   fonts: {sorted(set(rep['fonts']))}")
    problems = []
    for r in rep["res"]:
        flag = ""
        rr = RENDERS[r["page"] - 1]
        content_page = bool(getattr(rr, "toc", None)) and rr.toc[1] != 0
        if r["over"] > 3 or r["wide"] > 6: flag = "OVERFLOW (cut off) → shorten or remove a block"; problems.append(r["page"])
        elif content_page and r["free"] > 190: flag = "SPARSE → add a box/table/sticky"
        print(f"  p{r['page']:>3}  free={r['free']:>4}px  {flag}")
    n = len(RENDERS)
    if min_pages and n < min_pages: print(f"!! only {n} pages, need ≥ {min_pages}")
    if max_pages and n > max_pages: print(f"!! {n} pages, limit is {max_pages}")
    print("OK: no overflow" if not problems else f"!! overflow on pages {problems}")
    return out.with_suffix(".pdf")

def contact_sheets(pdf, outdir, per=6, dpi=45):
    """Render PNG contact sheets (6 pages each) for visual review."""
    from PIL import Image
    outdir = Path(outdir); outdir.mkdir(parents=True, exist_ok=True)
    subprocess.run(["pdftoppm", "-r", str(dpi), "-png", str(pdf), str(outdir / "p")], check=True)
    fs = sorted(outdir.glob("p-*.png")); sheets = []
    for k in range(0, len(fs), per):
        ims = [Image.open(f) for f in fs[k:k + per]]
        o = Image.new("RGB", (sum(i.width for i in ims), ims[0].height), "white"); x = 0
        for i in ims: o.paste(i, (x, 0)); x += i.width
        sp = outdir / f"sheet_{k // per:02d}.png"; o.save(sp); sheets.append(str(sp))
    return sheets
