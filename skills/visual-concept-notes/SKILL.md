---
name: visual-concept-notes
description: Create long (30–80 page) handwritten-style visual study notes as a PDF for any course module, roadmap or topic, with one concept per page, pinned concept boxes, highlighter marks, sticky notes, SVG diagrams and "Learn more" links. Use when the user asks for concept notes, visual notes, study notes, revision notes or "notes like before" as a PDF.
---

# Visual concept notes (PDF)

Produces an A4 PDF that looks like a neat student notebook: dotted paper, red margin line,
Kalam/Caveat handwriting headings, a hand-drawn SVG diagram on every concept page, and
colour-coded boxes. Proven layout: 66 pages for a 6-unit module with zero clipped pages.

The engine is `scripts/notes_engine.py`. A minimal working content file is `examples/example_content.py`.
**Do not rewrite the engine. Write a content file that imports it.**

## 1. Gather the material first
- If the user points to a roadmap/course page, read it and list every unit and every concept bullet. Each bullet becomes one concept page.
- Find one or two good "Learn more" links per concept (videos first, then interactive tools, then official docs/blogs). Verify each URL with WebFetch/WebSearch. Never invent links.
- Verify any number that will be printed (prices, limits, formulas). Label example numbers as "example" or "illustrative".
- Ask for page range only if the user didn't give one. Default target: 50–70 pages.

## 2. Plan pages (aim for the requested range)
Order: cover → how-to-use → contents → (optional) module map → for each unit: divider + one page per concept + recap → cheat sheet(s) → glossary → resources.
Rough count: 4 front + Σ(units × (concepts + 2)) + 3–4 end. Add concept pages (split big concepts, add a "how to choose / in practice" page) to reach the minimum; merge small ones to stay under the maximum.

## 3. Set up (once per session)
```bash
cp -r <skill_dir>/scripts/notes_engine.py <workdir>/
pip install playwright pillow --break-system-packages -q   # if missing
# fonts install automatically via npm on first build (Kalam, Caveat, Noto Devanagari)
```
Needs Chrome/Chromium (auto-detected; or set CHROME_PATH) and `pdftoppm` for previews.

## 4. Write the content file(s)
Split long notes into one file per unit (`u1.py`, `u2.py` …) that each call `add(...)`, plus a `main.py` that imports them in order and calls `build()`.

```python
from notes_engine import *
configure(title="LLM Fundamentals", series="100 Days of AI Engineering", module="Module 1",
          units={1: "What an LLM Does", 2: "Tokens, Context & Latency"},
          links={"karp_intro": ("Karpathy · Intro to LLMs (1 hr video)", "https://www.youtube.com/watch?v=zjkBMFhNj_g")})
add(cover_page(subtitle, art_svg, outcome, prereq, "MODULE 1 · DAYS 1–6"))
add(how_to_use_page()); add(contents_page())
add(divider(1, "What an LLM Does", "Day 1", [concepts...], outcome, art_svg,
            extra=tryit("hands-on task", "Day 1 hands-on") + key("why it matters", "Why this unit matters") + word_tags([...])))
add(page(1, "An LLM predicts the next token", body_html, kicker="Concept 1 · the big idea"))
...
pdf = build("My_Notes", min_pages=50, max_pages=70)
contact_sheets(pdf, "preview")
```

### Concept page recipe (this mix fills one A4 page well)
1. `lead(...)` – 1–2 sentences with 2 highlights.
2. `fig(svg(...), caption)` – a diagram that SHOWS the idea (flow, comparison, bars, before/after, grid of cards, timeline, decision tree).
3. `pin(title, body)` – the one idea to remember. Always present.
4. `cols(analogy(...) or key(...), sticky(...) or warn(...))` – two side-by-side boxes.
5. One of: `table(...)`, `tryit(...)`, `formula(...)`, or a fill-in `table(..., cls="logtbl")`.
6. `links("key1", "key2")` – always last.

Recap page per unit: summary `table`, quiz in `pin` + answers in a green `sticky`, a `tryit`/carry-forward task.

### Writing style
- Concepts, not theory. Simple words, short sentences. Explain jargon on first use.
- Highlights mean: `hl(x)` yellow = key term; `hl(x,"g")` green = definition/good way; `hl(x,"p")` pink = risk/cost; `hl(x,"b")` blue = technical name.
- Every concept page gets a real example, an analogy or a hands-on task. Hands-on tasks from the source roadmap become `tryit` boxes and worksheets.
- Don't hardcode page numbers in text (refer to "Concept 3" instead).

### SVG helpers (viewBox units ≈ 0.26 mm when width is ~680)
`box(x,y,w,h,fill,label)`, `circ`, `arrow`, `curve(d)`, `line`, `hbar(x,y,w,h,fill,label,val)`, `t(x,y,text,size,font="sans|hand|script|mono|deva")`,
`flow([labels]) → (inner, width)`, `card_grid([(title, sub, fill)])`, `check(x,y)`, `cross(x,y)`, `marker_hl`.
Fills: y b g p v o w gr r t (pastels); strokes in `S[...]`. Multi-line labels use `\n`.
Keep SVG viewBox ~680–720 wide; height 120–270. Long labels: shrink size or widen boxes. Keep text ≥ 11.5.

## 5. Build, check, fix (mandatory loop)
`build()` prints a line per page:
- `OVERFLOW` → content is cut off: remove or shorten a block, or reduce the SVG height. Never ship with overflow.
- `SPARSE` (> 190 px free) → add a useful block (table, sticky, tryit, warn).
Then render `contact_sheets()` and LOOK at every sheet with the Read tool: check overlapping SVG labels, text running out of boxes, cut-off labels at SVG edges, and divider titles. Fix and rebuild until clean.
Confirm with `pdfinfo` that the page count equals the number of `add()` calls (no blank pages) and is in the requested range.

## 6. Deliver
Send the PDF with SendUserFile. In the reply: page count, what's inside (one line each), and which numbers are illustrative. Offer a next module.
