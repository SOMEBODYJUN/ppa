"""Build exact provenance and byte-content indexes; no semantic claims."""

import csv
import hashlib
import zipfile
from collections import Counter, defaultdict
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

# Enumeration follows the reviewed exact-byte scopes, never an extension or
# the existence of a canonical link. A covered line is not a proved assertion.
scopes_by_payload = defaultdict(list)
scope_rows = rows("ATOMIC_SCOPE_REGISTRY.tsv")
for scope in scope_rows:
    sha = scope["payload_sha256"]
    assert sha in groups, f"atomic scope outside source inventory: {scope['scope_id']}"
    scopes_by_payload[sha].append(scope)

enumerations = {}
for sha, entries in groups.items():
    registered = scopes_by_payload[sha]
    covered = set()
    line_counts = {int(scope["total_lf_lines"]) for scope in registered}
    assert len(line_counts) <= 1, f"conflicting source line counts: {sha}"
    for scope in registered:
        for interval in scope["covered_ranges"].split(";"):
            first, last = map(int, interval.split("-"))
            assert 1 <= first <= last <= int(scope["total_lf_lines"])
            covered.update(range(first, last + 1))
    if registered:
        total_lines = next(iter(line_counts))
        status = ("enumerated-with-dispositions" if len(covered) == total_lines
                  else "partially-enumerated-with-dispositions")
    else:
        status = "pending-semantic-enumeration"
    enumerations[sha] = status
    scope_ids = ";".join(sorted(scope["scope_id"] for scope in registered)) or "none"
    for item in entries:
        if registered:
            item["enumeration_status"] = status
        item["atomic_scope_ids"] = scope_ids

write_tsv("SOURCE_OCCURRENCES.tsv", [
    "locator", "bytes", "sha256", "family", "location_kind", "format_hint",
    "representative_locator", "enumeration_status", "atomic_scope_ids",
], sorted(occurrences, key=lambda row: row["locator"]))
write_tsv("PAYLOAD_GROUPS.tsv", [
    "sha256", "bytes", "occurrence_count", "representative_locator", "enumeration_status", "atomic_scope_ids",
], [{
    "sha256": sha, "bytes": entries[0]["bytes"], "occurrence_count": len(entries),
    "representative_locator": entries[0]["representative_locator"],
    "enumeration_status": enumerations[sha],
    "atomic_scope_ids": entries[0]["atomic_scope_ids"],
} for sha, entries in sorted(groups.items())])

dispositions = rows("UNIT_DISPOSITIONS.tsv")
disposition_counts = Counter(row["disposition"] for row in dispositions)
enumeration_counts = Counter(enumerations.values())
snapshot = [
    "# 当前来源覆盖快照", "",
    "由 `python research/audit/build_occurrence_index.py` 从来源索引、精确范围登记与逐单元去向生成。"
    "机器只汇总已经声明的枚举范围，不审查断言真假、枚举是否充分或文献先行性；"
    "[验证器](../validate_assets.py)另核哈希、逐LF覆盖与去向双向一致。", "",
    "## 固定字节分母", "",
    f"{len(physical)} 个物理文件 + {len(members)} 个ZIP成员 = {len(occurrences)} 个出现位置，"
    f"共 {len(groups)} 个不同字节内容组；容器、字体等支持资产也在其中。", "",
    "| 内容组的枚举状态 | 组数 | 精确含义 |", "| --- | ---: | --- |",
    f"| 全LF已有登记去向 | {enumeration_counts['enumerated-with-dispositions']} | 同字节全部行被已登记范围的并集覆盖；可仍有deferred、source-report、候选或开放义务 |",
    f"| 部分LF已有登记去向 | {enumeration_counts['partially-enumerated-with-dispositions']} | 尚有未逐断言枚举的行；不能用选定章节推整稿完成 |",
    f"| 尚无登记逐断言范围 | {enumeration_counts['pending-semantic-enumeration']} | 格式提示、历史阅读、规范链接和标题分段均不能替代全内容枚举 |", "",
    "## 精确登记范围", "",
    "| 范围ID | 源文LF | 已声明覆盖 | 原子记录 | 剩余状态 |",
    "| --- | ---: | --- | ---: | --- |",
]
atomic_ids = set()
for scope in scope_rows:
    scope_units = [unit for table in scope["unit_tables"].split(";")
                   for unit in rows(str(Path(table).relative_to("research/audit")))]
    assert not (atomic_ids & {unit["unit_id"] for unit in scope_units})
    atomic_ids.update(unit["unit_id"] for unit in scope_units)
    snapshot.append(f"| {scope['scope_id']} | {scope['total_lf_lines']} | {scope['covered_ranges']} | "
                    f"{len(scope_units)} | {scope['semantic_status']} |")
snapshot += ["", f"以上 {len(scope_rows)} 个范围共 {len(atomic_ids)} 条原子记录；"
             "范围可能属于同一字节内容，不能当独立成果或文件数。", "",
             "## 逐单元去向", "",
             "| 去向 | 行数 |", "| --- | ---: |"]
for state in ("rewritten", "superseded", "duplicate", "refuted", "nonmathematical", "deferred"):
    snapshot.append(f"| {state} | {disposition_counts[state]} |")
snapshot += ["", f"合计 {len(dispositions)} 行；同一内容可以有章节、原子断言、版本与重复位置的多种记录。"
             "这些行数不是独立成果数，不能除以文件、字节组或节点数报告数学清洗率。", "",
             "已枚举来源按相同SHA-256回连到全部出现位置，来源角色仍由原位置保留；"
             "原件与成员初始清单的 `unreviewed` 是旧文件级关闭门，当前细粒度进度以本页、"
             "[登记表](ATOMIC_SCOPE_REGISTRY.tsv)和[逐单元去向](UNIT_DISPOSITIONS.tsv)为准。"
             "尚未关闭全库语义分母，也未证明总体规模比较。", ""]
(AUDIT / "CURRENT_COVERAGE.md").write_text("\n".join(snapshot), encoding="utf-8")
print(f"Indexed {len(occurrences)} occurrences / {len(groups)} payloads; registered enumeration states: "
      f"{dict(enumeration_counts)}. No mathematical status inferred.")
