"""Mechanical integrity checks; no mathematical truth claims."""
import csv
import hashlib
import json
import re
import zipfile
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

inventory_path = ROOT / "research/audit/SOURCE_FILE_INVENTORY.tsv"
source_count = 0
if inventory_path.is_file():
    with inventory_path.open(encoding="utf-8", newline="") as f:
        inventory = list(csv.DictReader(f, delimiter="\t"))
    source_count = len(inventory)
    for row in inventory:
        path = ROOT / row["source"]
        if not path.is_file():
            errors.append(f"missing audited source: {path}")
            continue
        raw = path.read_bytes()
        if len(raw) != int(row["bytes"]) or hashlib.sha256(raw).hexdigest() != row["sha256"]:
            errors.append(f"audited source hash/size changed: {path}")
    physical = {str(p.relative_to(ROOT)) for p in (ROOT / "history/sources").rglob("*") if p.is_file()}
    inventoried = {r["source"] for r in inventory}
    if physical != inventoried:
        errors.append(f"source inventory mismatch: {len(physical - inventoried)} unlisted, {len(inventoried - physical)} missing")

member_count = 0
member_path = ROOT / "research/audit/ZIP_MEMBER_INVENTORY.tsv"
if member_path.is_file():
    with member_path.open(encoding="utf-8", newline="") as f:
        members = list(csv.DictReader(f, delimiter="\t"))
    member_count = len(members)
    for row in members:
        zip_name, sep, member = row["source_member"].partition("!/")
        if not sep:
            errors.append(f"bad ZIP member locator: {row['source_member']}")
            continue
        try:
            with zipfile.ZipFile(ROOT / zip_name) as archive:
                raw = archive.read(member)
        except (OSError, KeyError, zipfile.BadZipFile) as exc:
            errors.append(f"missing/bad ZIP member: {row['source_member']}: {exc}")
            continue
        if len(raw) != int(row["bytes"]) or hashlib.sha256(raw).hexdigest() != row["sha256"]:
            errors.append(f"ZIP member hash/size changed: {row['source_member']}")

unit_count = 0
unit_path = ROOT / "research/audit/UNIT_DISPOSITIONS.tsv"
if unit_path.is_file():
    with unit_path.open(encoding="utf-8", newline="") as f:
        units = list(csv.DictReader(f, delimiter="\t"))
    unit_count = len(units)
    seen_units = set()
    for row in units:
        key = (row["source"], row["unit"])
        if key in seen_units:
            errors.append(f"duplicate source unit: {key}")
        seen_units.add(key)
        if not (ROOT / row["source"]).is_file():
            errors.append(f"missing unit source: {row['source']}")
        if row["disposition"] not in {"rewritten", "superseded", "refuted", "duplicate", "nonmathematical", "deferred"}:
            errors.append(f"invalid unit disposition: {key}")
        if row["disposition"] in {"rewritten", "superseded", "refuted"} and not row["canonical_identity"]:
            errors.append(f"missing canonical identity: {key}")
        target = row["canonical_target"]
        if target:
            file, _, anchor = target.partition("#")
            path = ROOT / file
            if not path.is_file() or (anchor and f'id="{anchor}"' not in path.read_text(encoding="utf-8")):
                errors.append(f"missing unit target: {key} -> {target}")
        elif row["disposition"] in {"rewritten", "superseded", "refuted"}:
            errors.append(f"missing unit target: {key}")

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
print(f"Verified {sum(r['status'] == 'imported' for r in rows)} initial-manifest hashes, "
      f"{source_count} audited source files, {member_count} ZIP members, "
      f"{unit_count} source units, {len(node_ids)} nodes, {len(edge_ids)} edges and {len(normative)} Markdown files.")
