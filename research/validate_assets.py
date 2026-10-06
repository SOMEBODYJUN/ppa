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
seed_path = ROOT / "research/audit/SEMANTIC_UNIT_SEED.tsv"
if seed_path.is_file():
    with seed_path.open(encoding="utf-8", newline="") as f:
        seed = list(csv.DictReader(f, delimiter="\t"))
    seed_ids = [row["unit_id"] for row in seed]
    if len(seed_ids) != len(set(seed_ids)):
        errors.append("duplicate semantic seed identity")
    by_member = {}
    for row in seed:
        by_member.setdefault(row["source_member"], []).append(row)
        valid_seed_status = {
            "mapped-to-existing", "enumerated-unadjudicated",
            "segmented-partial", "segmented-needs-unit-split",
        }
        if row["enumeration_status"] not in valid_seed_status:
            errors.append(f"invalid semantic seed status: {row['unit_id']}")
        target = row["canonical_target"]
        if target:
            file, _, anchor = target.partition("#")
            path = ROOT / file
            if not path.is_file() or (anchor and f'id="{anchor}"' not in path.read_text(encoding="utf-8")):
                errors.append(f"missing semantic seed target: {row['unit_id']}")
        elif row["enumeration_status"] not in {
            "enumerated-unadjudicated", "segmented-needs-unit-split"
        }:
            errors.append(f"unmapped semantic seed: {row['unit_id']}")
    for locator, segments in by_member.items():
        if locator not in indexed:
            errors.append(f"semantic seed locator absent from source occurrence index: {locator}")
        container, separator, name = locator.partition("!/")
        try:
            if separator:
                with zipfile.ZipFile(ROOT / container) as archive:
                    source_text = archive.read(name).decode("utf-8")
            elif locator.startswith("history/sources/"):
                source_text = (ROOT / locator).read_bytes().decode("utf-8")
            else:
                errors.append(f"bad semantic seed locator: {locator}")
                continue
            # Source ranges count physical LF lines. Some historical TeX has
            # literal CR control bytes inside a formula, not new source lines.
            line_count = source_text.count("\n") + int(bool(source_text) and not source_text.endswith("\n"))
        except (OSError, KeyError, UnicodeDecodeError, zipfile.BadZipFile) as exc:
            errors.append(f"unreadable semantic seed: {locator}: {exc}")
            continue
        intervals = sorted((int(row["start_line"]), int(row["end_line"])) for row in segments)
        cursor = 1
        for first, last in intervals:
            if first != cursor or last < first:
                errors.append(f"gap or overlap in semantic seed: {locator} at {cursor}")
            cursor = last + 1
        if cursor != line_count + 1:
            errors.append(f"semantic seed does not cover all {line_count} source lines: {locator}")

# Atomic source scopes have their own denominator. A full source scope is not
# inferred from the number of ledger rows or from a title-level seed segment.
atomic_count = 0
atomic_seen = set()
scope_registry = ROOT / "research/audit/ATOMIC_SCOPE_REGISTRY.tsv"
if scope_registry.is_file():
    with scope_registry.open(encoding="utf-8", newline="") as f:
        scopes = list(csv.DictReader(f, delimiter="\t"))
    if len({s["scope_id"] for s in scopes}) != len(scopes):
        errors.append("duplicate atomic scope identity")
    enumerated_lines = {}
    scope_ids_by_hash = {}
    total_lines_by_hash = {}
    for scope in scopes:
        locator = scope["source_locator"]
        container, sep, name = locator.partition("!/")
        try:
            if sep:
                with zipfile.ZipFile(ROOT / container) as archive:
                    raw = archive.read(name)
            else:
                raw = (ROOT / container).read_bytes()
            source_text = raw.decode("utf-8")
        except (OSError, KeyError, UnicodeDecodeError, zipfile.BadZipFile) as exc:
            errors.append(f"unreadable atomic scope: {locator}: {exc}")
            continue
        lines = source_text.count("\n") + int(bool(source_text) and not source_text.endswith("\n"))
        if hashlib.sha256(raw).hexdigest() != scope["payload_sha256"] or lines != int(scope["total_lf_lines"]):
            errors.append(f"atomic scope hash/line mismatch: {scope['scope_id']}")
        declared = set()
        for interval in scope["covered_ranges"].split(";"):
            first, last = map(int, interval.split("-"))
            if not 1 <= first <= last <= lines:
                errors.append(f"invalid atomic declared range: {scope['scope_id']}")
            new_lines = set(range(first, last + 1))
            if declared & new_lines:
                errors.append(f"overlapping atomic declared ranges: {scope['scope_id']}")
            declared.update(new_lines)
        covered = set()
        for table in scope["unit_tables"].split(";"):
            path = ROOT / table
            if not path.is_file():
                errors.append(f"missing atomic unit table: {table}")
                continue
            with path.open(encoding="utf-8", newline="") as f:
                reader = csv.DictReader(f, delimiter="\t")
                required = {"unit_id", "source_locator", "line_start", "line_end", "source_label", "unit_type", "exact_payload", "evidence_state", "disposition", "canonical_anchor", "claim_ids", "reason", "remaining_obligation"}
                if set(reader.fieldnames or []) != required:
                    errors.append(f"invalid atomic columns: {table}")
                    continue
                atomic_rows = list(reader)
            for row in atomic_rows:
                uid = row["unit_id"]
                if uid in atomic_seen:
                    errors.append(f"duplicate atomic identity: {uid}")
                atomic_seen.add(uid)
                atomic_count += 1
                first, last = int(row["line_start"]), int(row["line_end"])
                unit_lines = set(range(first, last + 1))
                if row["source_locator"] != locator or first > last or not unit_lines <= declared:
                    errors.append(f"atomic unit outside declared source scope: {uid}")
                covered.update(unit_lines)
                if row["disposition"] not in {"rewritten", "superseded", "refuted", "duplicate", "nonmathematical", "deferred"}:
                    errors.append(f"invalid atomic disposition: {uid}")
                if not row["exact_payload"] or not row["reason"]:
                    errors.append(f"missing atomic payload/reason: {uid}")
                if row["disposition"] == "deferred" and not row["remaining_obligation"]:
                    errors.append(f"missing exact deferred obligation: {uid}")
                anchors = row["canonical_anchor"].split(";") if row["canonical_anchor"] else []
                if not anchors and row["disposition"] in {"rewritten", "superseded", "refuted"}:
                    errors.append(f"missing atomic canonical target: {uid}")
                for target in anchors:
                    file, _, anchor = target.partition("#")
                    path = ROOT / file
                    if not path.is_file() or (anchor and f'id="{anchor}"' not in path.read_text(encoding="utf-8")):
                        errors.append(f"missing atomic target: {uid} -> {target}")
        if covered != declared:
            errors.append(f"atomic coverage differs: {scope['scope_id']}: {len(declared-covered)} missing, {len(covered-declared)} extra lines")
        sha = scope["payload_sha256"]
        enumerated_lines.setdefault(sha, set()).update(declared)
        scope_ids_by_hash.setdefault(sha, set()).add(scope["scope_id"])
        if sha in total_lines_by_hash and total_lines_by_hash[sha] != lines:
            errors.append(f"inconsistent atomic line count for content: {sha}")
        total_lines_by_hash[sha] = lines

    # Every exact-byte alias inherits the registered enumeration coverage,
    # while proof/evidence status remains attached to individual assertions.
    for row in payloads + occurrences:
        sha = row["sha256"]
        expected_ids = ";".join(sorted(scope_ids_by_hash.get(sha, set()))) or "none"
        if row.get("atomic_scope_ids", "") != expected_ids:
            errors.append(f"source index atomic-scope drift: {sha}")
        if sha in enumerated_lines:
            expected_status = ("enumerated-with-dispositions"
                if len(enumerated_lines[sha]) == total_lines_by_hash[sha]
                else "partially-enumerated-with-dispositions")
            if row["enumeration_status"] != expected_status:
                errors.append(f"source index enumeration-status drift: {sha}")
        elif row["enumeration_status"] in {
            "enumerated-with-dispositions", "partially-enumerated-with-dispositions"
        }:
            errors.append(f"unregistered enumeration status: {sha}")

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
for relative in (
    "research/map.html",
    "visualization/cosmos/index.html",
    "visualization/xianxia/index.html",
):
    page = (ROOT / relative).read_text(encoding="utf-8")
    matches = re.findall(
        r'<script\b[^>]*\bid="graph-data"[^>]*>(.*?)</script>',
        page, flags=re.DOTALL,
    )
    if len(matches) != 1:
        errors.append(f"missing/ambiguous embedded graph: {relative}")
        continue
    try:
        embedded_graph = json.loads(matches[0])
    except json.JSONDecodeError as exc:
        errors.append(f"invalid embedded graph: {relative}: {exc}")
        continue
    if embedded_graph != graph:
        errors.append(f"stale embedded graph: {relative}; rebuild from research/graph.json")
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

# Status is a separate typed field, not a word hidden inside Evidence. This
# checks ledger shape only; a status still requires mathematical review.
ledger = (ROOT / "CLAIMS.md").read_text(encoding="utf-8")
claim_blocks = re.split(r"(?=^## C\d+)", ledger, flags=re.MULTILINE)[1:]
for block in claim_blocks:
    title = block.splitlines()[0]
    statuses = re.findall(r"^- \*\*Status\*\*：`([^`]+)`", block, flags=re.MULTILINE)
    if len(statuses) != 1 or statuses[0] not in {
        "source-report", "candidate", "derived-checked", "refuted", "open", "canonical"
    }:
        errors.append(f"missing/ambiguous explicit Claim status: {title}")

# Check only written research layer. Source manuscripts have their own, possibly
# obsolete relative links and are intentionally immutable.
normative = list(ROOT.glob("*.md")) + list((ROOT / "research").rglob("*.md"))
link = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
for page in normative:
    raw = page.read_bytes()
    bad_controls = {b for b in raw if b < 32 and b not in (9, 10)}
    if bad_controls:
        errors.append(f"control bytes in normative text: {page.relative_to(ROOT)} {sorted(bad_controls)}")
    data = raw.decode("utf-8")
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

graph_controls = {b for b in (ROOT / "research/graph.json").read_bytes() if b < 32 and b not in (9, 10)}
if graph_controls:
    errors.append(f"control bytes in normative graph: {sorted(graph_controls)}")

if errors:
    raise SystemExit("\n".join(errors))
print(f"Verified {sum(r['status'] == 'imported' for r in rows)} initial-manifest hashes, "
      f"{source_count} audited source files, {member_count} ZIP members, "
      f"{unit_count} source units, {atomic_count} atomic records in declared scopes, "
      f"{len(node_ids)} nodes, {len(edge_ids)} edges and {len(normative)} Markdown files.")
