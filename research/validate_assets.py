"""Mechanical integrity checks; no mathematical truth claims."""
import csv
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
errors = []

with (ROOT / "INGEST_MANIFEST.tsv").open(encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f, delimiter="\t"))
for row in rows:
    if row["status"] != "imported":
        continue
    path = ROOT / row["repository_path"]
    if not path.is_file():
        errors.append(f"missing imported source: {path}")
        continue
    raw = path.read_bytes()
    if len(raw) != int(row["bytes"]) or hashlib.sha256(raw).hexdigest() != row["sha256"]:
        errors.append(f"source hash/size changed: {path}")

graph = json.loads((ROOT / "research/graph.json").read_text(encoding="utf-8"))
node_ids = [n["id"] for n in graph["nodes"]]
edge_ids = [e["id"] for e in graph["edges"]]
if len(node_ids) != len(set(node_ids)) or len(edge_ids) != len(set(edge_ids)):
    errors.append("duplicate graph identity")
for n in graph["nodes"]:
    file, _, anchor = n["file"].partition("#")
    path = ROOT / "research" / file
    if not path.is_file():
        errors.append(f"missing graph target: {n['id']} -> {path}")
    elif anchor and f'id="{anchor}"' not in path.read_text(encoding="utf-8"):
        errors.append(f"missing graph anchor: {n['id']} -> {n['file']}")
for e in graph["edges"]:
    if not e["inputs"] or len(e["inputs"]) != len(set(e["inputs"])) or any(i not in node_ids for i in e["inputs"]):
        errors.append(f"invalid conjunctive inputs: {e['id']}")
    if e["output"] not in node_ids or e["output"] in e["inputs"]:
        errors.append(f"invalid output: {e['id']}")
    if not e.get("scope") or not e.get("status") or not e.get("relation"):
        errors.append(f"missing edge contract: {e['id']}")

# Check only written research layer. Source manuscripts have their own, possibly
# obsolete relative links and are intentionally immutable.
normative = list(ROOT.glob("*.md")) + list((ROOT / "research").rglob("*.md"))
link = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
for page in normative:
    data = page.read_text(encoding="utf-8")
    for target in link.findall(data):
        target = target.split("#", 1)[0]
        if not target or "://" in target or target.startswith("mailto:"):
            continue
        candidate = (page.parent / unquote(target)).resolve()
        if not candidate.exists():
            errors.append(f"broken link: {page.relative_to(ROOT)} -> {target}")

if errors:
    raise SystemExit("\n".join(errors))
print(f"Verified {sum(r['status'] == 'imported' for r in rows)} imported source hashes, "
      f"{len(node_ids)} nodes, {len(edge_ids)} edges and {len(normative)} Markdown files.")
