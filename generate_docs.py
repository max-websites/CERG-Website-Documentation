#!/usr/bin/env python3
"""
generate_docs.py

Creates a markdown stub file for each how-to page below, organized into
folders by category, and rewrites the `nav:` section of mkdocs.yml to
match.

Usage:
    Place this file in your mkdocs project root (next to mkdocs.yml)
    and run:

        python3 generate_docs.py

Re-running is safe: existing .md files are left alone (never overwritten),
but the nav block in mkdocs.yml is always regenerated from PAGES below.
"""

import re
from pathlib import Path

# ---------------------------------------------------------------------------
# 1. Your pages, as (category, title). Edit this list to add/remove pages —
#    the script will pick up the changes next run.
# ---------------------------------------------------------------------------
PAGES = [
    ("General", "Design Guidelines"),
    ("General", "Update info on a page"),
    ("General", "Copy an existing component/design"),
    ("General", "About Tags"),
    ("General", "About Page Properties"),
    ("General", "About HTML code"),
    ("General", "About Lists"),
    ("General", "About page templates"),

    ("New Content", "Creating a new Working Paper"),
    ("New Content", "How to upload new photos and documents"),
    ("New Content", "How to add a new Working Paper"),
    ("New Content", "How to add a new Op-ed"),
    ("New Content", "How to add an event"),
    ("New Content", "How to add a news item"),
    ("New Content", "How to add a team member"),

    ("Changing Content", "Updating the homepage"),
    ("Changing Content", "Updating the agrivoltaics page"),
    ("Changing Content", "Updating YT video feeds"),
    ("Changing Content", "Archive a team member"),

    ("Analytics", "How to see page views"),
    ("Analytics", "How to see downloads of Working Papers"),
    ("Analytics", "How to see links clicked"),
    ("Analytics", "How to set up link tracking"),
]

DOCS_DIR = Path("docs")
MKDOCS_YML = Path("mkdocs.yml")


def slugify(text: str) -> str:
    """'How to add a team member' -> 'how-to-add-a-team-member'"""
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def build_pages():
    """Create category folders + stub .md files (skipping ones that already
    exist). Returns an ordered dict of category -> [(title, relpath), ...]
    for building the nav."""
    nav_map = {}
    for category, title in PAGES:
        cat_slug = slugify(category)
        cat_dir = DOCS_DIR / cat_slug
        cat_dir.mkdir(parents=True, exist_ok=True)

        filename = slugify(title) + ".md"
        filepath = cat_dir / filename
        relpath = f"{cat_slug}/{filename}"

        if not filepath.exists():
            filepath.write_text(f"# {title}\n\nTODO: write instructions.\n")
            print(f"created  {filepath}")
        else:
            print(f"skipped  {filepath}  (already exists, left untouched)")

        nav_map.setdefault(category, []).append((title, relpath))
    return nav_map


def build_nav_block(nav_map: dict) -> str:
    """Render the nav_map into a mkdocs.yml-formatted `nav:` block."""
    lines = ["nav:", "  - Home: index.md"]
    for category, entries in nav_map.items():
        lines.append(f"  - {category}:")
        for title, relpath in entries:
            safe_title = title.replace(":", " -")  # avoid breaking YAML
            lines.append(f'      - "{safe_title}": {relpath}')
    return "\n".join(lines) + "\n"


def update_mkdocs_yml(nav_block: str):
    """Replace the existing `nav:` block in mkdocs.yml with a freshly
    generated one, leaving everything else in the file untouched."""
    text = MKDOCS_YML.read_text()

    # Matches "nav:" at the start of a line, plus every following line that
    # is indented or blank -- i.e. the whole nav block -- stopping right
    # before the next top-level (column-0) key.
    pattern = re.compile(r"^nav:\n(?:[ \t].*\n?|\n)*", re.MULTILINE)

    if pattern.search(text):
        new_text = pattern.sub(nav_block + "\n", text, count=1)
    else:
        new_text = text.rstrip() + "\n\n" + nav_block

    MKDOCS_YML.write_text(new_text)
    print(f"updated  {MKDOCS_YML}")


def main():
    if not MKDOCS_YML.exists():
        raise SystemExit(
            "mkdocs.yml not found in the current folder — "
            "run this script from your mkdocs project root."
        )

    nav_map = build_pages()
    nav_block = build_nav_block(nav_map)
    update_mkdocs_yml(nav_block)
    print("\nDone. Review mkdocs.yml, then run `mkdocs serve` to preview.")


if __name__ == "__main__":
    main()