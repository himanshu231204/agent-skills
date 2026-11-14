import sys
sys.path.insert(0, sys.argv[1] if len(sys.argv) > 1 else "../scripts")
from notes_engine import *

configure(title="Git Basics", series="Dev Foundations", module="Module 1",
          units={1: "How Git Thinks", 2: "Branches"},
          links={"progit": ("Pro Git book · Git Basics chapter", "https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository"),
                 "learnbranch": ("Learn Git Branching (interactive)", "https://learngitbranching.js.org")})

s, w = flow(["Working dir", "Staging", "Commit", "Remote"])
add(cover_page(f'Visual concept notes. {hl("Concepts, not theory.")}', svg(w, 100, s),
               "Explain what a commit is, and branch without fear.", "Before you start: a terminal and git installed.", "DAYS 1–2"))
add(how_to_use_page())
add(contents_page())
add(divider(1, "How Git Thinks", "Day 1", ["Snapshots, not diffs", "The three areas"],
            "Explain what happens on git add and git commit.", svg(w, 100, s),
            tryit("Make a repo, add one file, commit it.", "Day 1 hands-on") + word_tags(["commit", "stage", "HEAD"])))
add(page(1, "A commit is a snapshot", f'''
{lead(f"Git saves {hl('a photo of your whole project')} each time you commit.")}
{fig(svg(w, 100, s), "files move left to right")}
{pin("Commit", f"A saved snapshot with a message and a {hl('unique ID', 'b')}.")}
{cols(analogy("Save points in a video game."), sticky("Commit small, commit often.", rot=1.2))}
{table(["Command", "What it does"], [["git add", "stage changes"], ["git commit", "save snapshot"]])}
{warn("Committing everything with one giant message.")}
{links("progit")}''', kicker="Concept 1 · snapshots"))
add(glossary_page([("Commit", "saved snapshot"), ("Branch", "movable pointer to a commit"), ("HEAD", "where you are now")]))
add(resources_page([("Read", ["progit"]), ("Play", ["learnbranch"])]))
pdf = build("example_notes")
print(contact_sheets(pdf, "example_png"))
