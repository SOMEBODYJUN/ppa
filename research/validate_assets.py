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
    inventoried_members = [row["source_member"] for row in members]
    if len(inventoried_members) != len(set(inventoried_members)):
        errors.append("duplicate ZIP member inventory locator")
    actual_members = set()
    for source_zip in (ROOT / "history/sources").rglob("*.zip"):
        try:
            with zipfile.ZipFile(source_zip) as archive:
                actual_members.update(
                    f"{source_zip.relative_to(ROOT)}!/{info.filename}"
                    for info in archive.infolist() if not info.is_dir()
                )
        except zipfile.BadZipFile as exc:
            errors.append(f"unreadable source ZIP: {source_zip}: {exc}")
    listed_members = set(inventoried_members)
    if actual_members != listed_members:
        errors.append(
            f"ZIP inventory mismatch: {len(actual_members - listed_members)} unlisted, "
            f"{len(listed_members - actual_members)} missing"
        )
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

occurrence_path = ROOT / "research/audit/SOURCE_OCCURRENCES.tsv"
payload_path = ROOT / "research/audit/PAYLOAD_GROUPS.tsv"
if occurrence_path.is_file() and payload_path.is_file():
    with occurrence_path.open(encoding="utf-8", newline="") as f:
        occurrences = list(csv.DictReader(f, delimiter="\t"))
    with payload_path.open(encoding="utf-8", newline="") as f:
        payloads = list(csv.DictReader(f, delimiter="\t"))
    expected = {
        row["source"]: (row["sha256"], row["bytes"])
        for row in inventory
    } | {
        row["source_member"]: (row["sha256"], row["bytes"])
        for row in members
    }
    indexed = {row["locator"]: (row["sha256"], row["bytes"]) for row in occurrences}
    if len(indexed) != len(occurrences) or indexed != expected:
        errors.append("source occurrence index differs from the two source inventories")
    by_hash = {}
    for row in occurrences:
        by_hash.setdefault(row["sha256"], []).append(row)
    grouped = {row["sha256"]: row for row in payloads}
    if len(grouped) != len(payloads) or set(grouped) != set(by_hash):
        errors.append("payload groups differ from source occurrence hashes")
    else:
        for sha, row in grouped.items():
            entries = by_hash[sha]
            if (int(row["occurrence_count"]) != len(entries)
                    or row["representative_locator"] not in {e["locator"] for e in entries}
                    or any(e["representative_locator"] != row["representative_locator"] for e in entries)):
                errors.append(f"invalid payload group: {sha}")

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
        source_zip, sep, source_member = row["source"].partition("!/")
        if sep:
            try:
                with zipfile.ZipFile(ROOT / source_zip) as archive:
                    archive.getinfo(source_member)
            except (OSError, KeyError, zipfile.BadZipFile) as exc:
                errors.append(f"missing unit ZIP member: {row['source']}: {exc}")
        elif not (ROOT / row["source"]).is_file():
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
    # Formulae such as M_p[phi](t) are not Markdown links. Exclude math and
    # code spans before applying the deliberately small relative-link check.
    data = re.sub(r"(?s)```.*?```", "", data)
    data = re.sub(r"(?s)\\\[.*?\\\]", "", data)
    data = re.sub(r"(?s)\$\$.*?\$\$", "", data)
    data = re.sub(r"`[^`\n]*`", "", data)
    data = re.sub(r"(?<!\\)\$[^$\n]*\$", "", data)
    for raw_target in link.findall(data):
        target, marker, anchor = raw_target.partition("#")
        if "://" in target or target.startswith("mailto:"):
            continue
        candidate = (page.parent / unquote(target)).resolve() if target else page
        if not candidate.exists():
            errors.append(f"broken link: {page.relative_to(ROOT)} -> {raw_target}")
        elif marker and anchor and candidate.is_file() and f'id="{unquote(anchor)}"' not in candidate.read_text(encoding="utf-8"):
            errors.append(f"broken explicit anchor: {page.relative_to(ROOT)} -> {raw_target}")

if errors:
    raise SystemExit("\n".join(errors))
print(f"Verified {sum(r['status'] == 'imported' for r in rows)} initial-manifest hashes, "
      f"{source_count} audited source files, {member_count} ZIP members, "
      f"{unit_count} source units, {len(node_ids)} nodes, {len(edge_ids)} edges and {len(normative)} Markdown files.")
