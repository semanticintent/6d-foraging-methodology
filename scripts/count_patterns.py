#!/usr/bin/env python3
"""Count cascade patterns in the published StratIQX case library.

Reads the public case index (or a local copy) and writes data/counted-patterns.md:
how often each dimension is the origin, what the next layer includes, what
precedes it, and how often it lands last. Counts, not probabilities.

Usage:
  python3 scripts/count_patterns.py                      # fetch https://uc-000.stratiqx.com/index.json
  python3 scripts/count_patterns.py --index path/to/index.json
"""
import argparse, collections, datetime, json, os, re, urllib.request

URL = "https://uc-000.stratiqx.com/index.json"
N = ["", "Customer", "Employee", "Revenue", "Regulatory", "Quality", "Operational"]

ap = argparse.ArgumentParser()
ap.add_argument("--index")
ap.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "..", "data", "counted-patterns.md"))
args = ap.parse_args()

if args.index:
    idx = json.load(open(args.index, encoding="utf-8"))
else:
    req = urllib.request.Request(URL, headers={"User-Agent": "6d-count-patterns"})
    idx = json.load(urllib.request.urlopen(req, timeout=60))

cases = []
for e in idx:
    br = (e.get("cascade") or [None])[0]
    if not br or not re.fullmatch(r"D[1-6](\+D[1-6])*(>D[1-6](\+D[1-6])*)*", br.replace(" ", "")):
        continue
    layers = [[int(d[1]) for d in g.split("+")] for g in br.replace(" ", "").split(">")]
    title = re.sub(r"^UC-\d+:\s*", "", e["title"]).split(" — ")[0]
    cases.append((e["num"], title, e["type"], layers, br))
multi = [c for c in cases if len(c[3]) >= 2]

origin, reached, last = collections.Counter(), collections.Counter(), collections.Counter()
for c in cases:
    for d in {d for l in c[3] for d in l}:
        reached[d] += 1
    for d in c[3][0]:
        origin[d] += 1
    if len(c[3]) >= 2:
        for d in c[3][-1]:
            last[d] += 1

today = datetime.date.today().isoformat()
out = [f"# Counted cascade patterns\n",
       f"Generated {today} from {URL} by `scripts/count_patterns.py`. "
       f"{len(cases)} published cases with a recorded cascade; {len(multi)} have two or more layers. "
       "Counts, not probabilities. A case can list several dimensions in one layer, so counts in a row can add up to more than the case count.\n",
       "## Overall\n",
       "| Dimension | Origin of | Reached in (any layer) | Lands in the last layer |",
       "|---|---|---|---|"]
for d in range(1, 7):
    out.append(f"| D{d} {N[d]} | {origin[d]} | {reached[d]} of {len(cases)} | {last[d]} of {len(multi)} |")
for d in range(1, 7):
    oc = [c for c in multi if d in c[3][0]]
    nx = collections.Counter(x for c in oc for x in c[3][1])
    feeds = collections.Counter()
    for c in multi:
        for i in range(1, len(c[3])):
            if d in c[3][i]:
                for p in c[3][i - 1]:
                    feeds[p] += 1
    out.append(f"\n## D{d} {N[d]}\n")
    out.append(f"- Origin in {len(oc)} multi-layer cases. Next layer includes: " + ", ".join(f"{N[x]} {k} of {len(oc)}" for x, k in nx.most_common()))
    out.append(f"- When {N[d]} appears after the origin, the layer before it most often includes: " + ", ".join(f"{N[x]} {k}" for x, k in feeds.most_common(3)))
    ex = sorted(oc, key=lambda c: -int(c[0]))[:4]
    out.append("- Recent cases with this origin: " + "; ".join(f"[UC-{c[0]} {c[1]}](https://uc-{c[0]}.stratiqx.com) ({c[4]}, {c[2]})" for c in ex))

os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
open(args.out, "w", encoding="utf-8").write("\n".join(out) + "\n")
print(f"Wrote {args.out}: {len(cases)} cases, {len(multi)} multi-layer")
