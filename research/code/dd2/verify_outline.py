"""Check the DD2 manuscript order, references and selected exact algebra."""
from fractions import Fraction
from pathlib import Path
import re

repo = Path(__file__).resolve().parents[3]
outline = repo / "research/manuscripts/dd2/DD2_outline_and_pro_handoff.md"
body = outline.read_text(encoding="utf-8")

chapters = [
    "引言",
    "DD1 与 DD2",
    "从一步下降到实际轨道",
    "优化结构与补偿边界",
    "应用",
]
chapter_titles = re.findall(r"^\| ([1-5]) ([^|]+?) \|", body, re.MULTILINE)
assert chapter_titles == [(str(i), title) for i, title in enumerate(chapters, 1)]

checklist = repo / "research/audit/DD2_ACCEPTANCE_CHECKLIST.md"
checklist_body = checklist.read_text(encoding="utf-8")
checklist_ids = re.findall(r"^- \[[ x]\] `([A-Z0-9.]+)` ", checklist_body, re.MULTILINE)
editorial_table = body.split('id="dd2-editorial-280"', 1)[1].split("## 既有数学素材", 1)[0]
editorial_rows = re.findall(r"^\| ([A-Z0-9.]+) \| ([^|]+?) \| ([^|]+?) \|$", editorial_table, re.MULTILINE)
assert len(checklist_ids) == len(set(checklist_ids)) == 280
assert [item for item, _, _ in editorial_rows] == checklist_ids
assert len({reason.rstrip("。") for _, _, reason in editorial_rows}) == 280

headings = [
    "一般下降目标与线性误差界特例",
    "一般 A 的距离、点收敛和有限长度",
    "一般输出误差界下的几何与长度",
    "松弛与输入／输出误差界",
    "退化 PPPA 与恢复",
    "CP/DR 应用与后续扩展",
]
positions = []
for heading in headings:
    matches = re.findall(rf"^### 第.节　{re.escape(heading)}$", body, re.MULTILINE)
    assert len(matches) == 1, heading
    positions.append(body.index(matches[0]))
assert positions == sorted(positions)

claims = (repo / "CLAIMS.md").read_text(encoding="utf-8")
claim_ids = [*range(400, 407), 424, 430, 432, 433]
for claim in claim_ids:
    assert f'id="c{claim}"' in claims
    assert f"C{claim}" in body

links = re.findall(r"\[[^]\n]+\]\((\.\.[^)\n]+)\)", body)
for link in links:
    filename, _, anchor = link.partition("#")
    target = (outline.parent / filename).resolve()
    assert target.is_file(), link
    if anchor:
        assert f'id="{anchor}"' in target.read_text(encoding="utf-8"), link

for parameter in (Fraction(1, 10), Fraction(1, 4), Fraction(1, 2)):
    ratio = parameter / (1 - parameter)
    energy = ((1 + parameter ** 2) * ratio ** 2 - parameter ** 2) / (2 * parameter ** 2)
    cap = ratio * (ratio - parameter) / parameter ** 2
    assert energy == cap == parameter / (1 - parameter) ** 2

for q in (Fraction(3, 5), Fraction(2, 3), Fraction(3, 4)):
    p0 = 1 / (2 / q - 2)
    assert p0 * (2 - 1 / q) == p0 - Fraction(1, 2)

assert Fraction(26, 101) < Fraction(12, 37)
print(f"DD2 verified: 5 chapters, 280 editorial rows, 6 indexed source sections, "
      f"{len(claim_ids)} claim records, {len(links)} local links, 7 exact algebra checks.")
