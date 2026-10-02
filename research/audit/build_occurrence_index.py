"""Build exact provenance and byte-content indexes; no semantic claims."""

import csv
import hashlib
import zipfile
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
AUDIT = Path(__file__).resolve().parent
P = "history/sources/次单调论文研究"
H = "history/sources/历史总包_2026-09-14/菠萝_RL与广义次正则研究资产_2026-09-14_v2_真实超边图"
D = "history/sources/提纯总账_2026-09-21_v0.9"
A = f"{P}/分类集研究/RLEB_LT_operator_space_research_asset_v1/RLEB_LT_operator_space_research_asset_v1"

ZIP_FAMILIES = {
    f"{P}/RLEB_投稿扩展版_完整源码_2026-09-19.zip": "Z01",
    f"{P}/RL_CONIC_CRSC_MSCQ_Boluo_v04_source.zip": "Z02",
    f"{P}/RL_PPA_generalized_subregularity_Boluo_source.zip": "Z03",
    f"{P}/RL_T4_CODEX_HANDOFF_2026-09-09.zip": "Z04",
    f"{P}/RL_monotonicity_regularity_research_checkpoint_2026-09-01.zip": "Z05",
    f"{P}/RL_novelty_boundary_checkpoint_2026-09-01.zip": "Z06",
    f"{P}/monotonicity_regularity_research_2026-09-01.zip": "Z07",
    f"{A}/06_RELATED_MANUSCRIPT_ASSETS/solution_selection_revised_v1_delivery.zip": "Z08",
    f"{A}/06_RELATED_MANUSCRIPT_ASSETS/source_inputs/RLEB_PPA_submission_assets_2026-09-18.zip": "Z09",
    f"{P}/分类集研究/RLEB_research_asset_distilled_2026-09-21_v0.9.zip": "Z10",
    f"{P}/正式后的研究/RLEB_solution_selection_2026-09-18.zip": "Z11",
}


def physical_family(path):
    for i, prefix in enumerate((
        "00_从这里开始", "01_RL_PPA核心理论", "02_锥优化_CRSC_MSCQ",
        "03_随机与Markov理论", "04_公开问题与未来攻关",
        "05_文献证据与来源快照", "06_关键失败与研究边界",
    ), 1):
        if path.startswith(f"{H}/{prefix}/"):
            return f"F{i:02d}"
    if path.startswith(D + "/"):
        return "F08"
    if path.startswith(P + "/RL_foundations_freeze_2026-09-01/"):
        return "F09"
    if path.startswith(P + "/分类集研究/"):
        return "F11"
    if path.startswith(P + "/最新成果/"):
        return "F12"
    if path.startswith(P + "/正式后的研究/"):
        return "F13"
    if path.startswith(P + "/") and "/" not in path[len(P) + 1:]:
        return "F10"
    raise ValueError(f"unpartitioned physical source: {path}")


def kind_and_status(locator):
    suffix = Path(locator.split("!/")[-1]).suffix.lower()
    if suffix == ".zip":
        return "container", "members-verified-semantic-pending"
    if suffix in {".md", ".tex", ".txt", ".html", ".json", ".yaml", ".yml", ".csv", ".bib", ".bbl"}:
        return suffix[1:], "pending-semantic-enumeration"
    if suffix in {".py", ".sh", ".lua"}:
        return "code", "pending-code-contract"
    if suffix in {".pdf", ".docx"}:
        return suffix[1:], "pending-render-and-enumeration"
    return suffix[1:] or "unknown", "pending-role-review"


def rows(path):
    with (AUDIT / path).open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path, fields, entries):
    with (AUDIT / path).open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(entries)


physical = rows("SOURCE_FILE_INVENTORY.tsv")
members = rows("ZIP_MEMBER_INVENTORY.tsv")
actual = {str(path.relative_to(ROOT)) for path in (ROOT / "history/sources").rglob("*") if path.is_file()}
assert actual == {row["source"] for row in physical}
assert len(physical) == 251 and len(members) == 178

occurrences = []
for row in physical:
    locator = row["source"]
    raw = (ROOT / locator).read_bytes()
    assert len(raw) == int(row["bytes"])
    assert hashlib.sha256(raw).hexdigest() == row["sha256"]
    kind, status = kind_and_status(locator)
    occurrences.append({
        "locator": locator, "bytes": len(raw), "sha256": row["sha256"],
        "family": physical_family(locator), "location_kind": "physical",
        "format_hint": kind, "enumeration_status": status,
    })

actual_members = []
for container, family in ZIP_FAMILIES.items():
    with zipfile.ZipFile(ROOT / container) as archive:
        filenames = [info.filename for info in archive.infolist() if not info.is_dir()]
        assert len(filenames) == len(set(filenames)), f"duplicate member name in {container}"
        for name in filenames:
            actual_members.append(f"{container}!/{name}")
assert set(actual_members) == {row["source_member"] for row in members}
assert len(actual_members) == len(members)

for row in members:
    locator = row["source_member"]
    container, member = locator.split("!/", 1)
    with zipfile.ZipFile(ROOT / container) as archive:
        raw = archive.read(member)
    assert len(raw) == int(row["bytes"])
    assert hashlib.sha256(raw).hexdigest() == row["sha256"]
    kind, status = kind_and_status(locator)
    occurrences.append({
        "locator": locator, "bytes": len(raw), "sha256": row["sha256"],
        "family": ZIP_FAMILIES[container], "location_kind": "zip-member",
        "format_hint": kind, "enumeration_status": status,
    })

groups = defaultdict(list)
for row in occurrences:
    groups[row["sha256"]].append(row)
assert len(occurrences) == 429 and len(groups) == 346
for entries in groups.values():
    assert len({item["bytes"] for item in entries}) == 1
    representative = min(entries, key=lambda item: (item["location_kind"] != "physical", item["locator"]))
    for item in entries:
        item["representative_locator"] = representative["locator"]

write_tsv("SOURCE_OCCURRENCES.tsv", [
    "locator", "bytes", "sha256", "family", "location_kind", "format_hint",
    "representative_locator", "enumeration_status",
], sorted(occurrences, key=lambda row: row["locator"]))
write_tsv("PAYLOAD_GROUPS.tsv", [
    "sha256", "bytes", "occurrence_count", "representative_locator", "enumeration_status",
], [{
    "sha256": sha, "bytes": entries[0]["bytes"], "occurrence_count": len(entries),
    "representative_locator": entries[0]["representative_locator"],
    "enumeration_status": "pending-semantic-enumeration",
} for sha, entries in sorted(groups.items())])

print(f"Indexed {len(occurrences)} source occurrences and {len(groups)} byte payloads; semantic enumeration remains pending.")
