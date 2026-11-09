#!/usr/bin/env python3
"""Copy the 6D docs site's pages into docs/ for a release.

The docs site (6d.semanticintent.dev) is the single source of truth; each
release of this repository is a snapshot of its Markdown. Site-absolute links
such as /framework/scoring are rewritten to relative .md links so the
snapshot reads correctly on GitHub and in the Zenodo archive.

Usage:
  python3 scripts/snapshot_from_site.py --site /path/to/6d-impact-site/docs
"""
import argparse, os, posixpath, re, shutil

# Site-only pages that are not part of the methodology.
EXCLUDE = {"privacy-policy.md", "terms-of-service.md", "6D_Observable_Properties_Framework.md"}

ap = argparse.ArgumentParser()
ap.add_argument("--site", required=True, help="path to the docs site's docs/ folder")
args = ap.parse_args()

site = os.path.abspath(args.site)
dest = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs")
dest = os.path.abspath(dest)

pages = []
for root, dirs, files in os.walk(site):
    dirs[:] = [d for d in dirs if not d.startswith(".") and d != "public"]
    for f in files:
        if f.endswith(".md") and f not in EXCLUDE:
            pages.append(os.path.relpath(os.path.join(root, f), site))
known = {p[:-3] for p in pages}  # e.g. framework/scoring

LINK = re.compile(r"\]\((/[A-Za-z0-9_\-/]*)(#[^)\s]*)?\)")

def rewrite(text, page):
    here = posixpath.dirname(page.replace(os.sep, "/"))
    def sub(m):
        target = m.group(1).strip("/") or "index"
        if target.endswith("/"):
            target += "index"
        if target not in known and target + "/index" in known:
            target += "/index"
        if target not in known:
            # site-only page (e.g. terms, privacy): link to the live site
            return f"](https://6d.semanticintent.dev/{target}{m.group(2) or ''})"
        rel = posixpath.relpath(target + ".md", here or ".")
        return f"]({rel}{m.group(2) or ''})"
    return LINK.sub(sub, text)

if os.path.isdir(dest):
    shutil.rmtree(dest)
for p in sorted(pages):
    src = os.path.join(site, p)
    out = os.path.join(dest, p)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(src, encoding="utf-8") as f:
        text = f.read()
    with open(out, "w", encoding="utf-8") as f:
        f.write(rewrite(text, p))
print(f"Copied {len(pages)} pages into {dest}")
