"""Check the DD2 manuscript order, references and selected exact algebra."""
from fractions import Fraction
from pathlib import Path
from itertools import product
import re

repo = Path(__file__).resolve().parents[3]
outline = repo / "research/manuscripts/dd2/DD2_outline_and_pro_handoff.md"
body = outline.read_text(encoding="utf-8")

current_anchor = 'id="dd-paper-author-outline"'
legacy_anchor = 'id="dd-paper-legacy-handoff"'
assert body.count(current_anchor) == body.count(legacy_anchor) == 1
assert body.index(current_anchor) < body.index(legacy_anchor)
current = body.split(current_anchor, 1)[1].split(legacy_anchor, 1)[0]
legacy = body.split(legacy_anchor, 1)[1]
assert re.findall(r"^### (.+)$", current, re.MULTILINE) == [
    "摘要", "第 1 章 引言", "第 2 章 DD1", "第 3 章 DD2",
    "第 4 章 DD3", "第 5 章 近端参数选择", "结论与展望",
]
abstract, introduction, dd1, dd2, dd3, parameters, conclusion = re.split(
    r"^### .+\n", current, flags=re.MULTILINE
)[1:]
assert all(name in abstract for name in ("DD1", "DD2", "DD3"))
assert all(name in introduction for name in ("正则指数", "次单调指数", "存在性引理"))
assert "正式列出存在性引理的陈述" in introduction
assert "DD11、DD12" in dd1 and "dd1-step-and-tail" in dd1
assert "给定正则性允许多大缺陷" in dd1 and "给定缺陷要求多强正则性" in dd1
assert dd2.index("dd2-half-order-complete-example") < dd2.index("传统比较级数")
assert dd2.index("传统比较级数") < dd2.index("原 F1–F3")
assert "dd3-global-coverage" in dd3 and "同一近端关系" in dd3
assert "先证明引言列出的" in dd3
assert "sr-uniform-steps" in parameters and "累计进展" in parameters
assert "例子随定理" in conclusion

design_anchors = [
    "dd2-design-task-packages", "dd2-design-old-task-map", "dd2-design-copy-prompts",
]
for anchor in design_anchors:
    assert body.count(f'id="{anchor}"') == 1
design_ids = re.findall(r"^- \[[ x]\] `((?:N|G|C|L|E|A|R)\d\d)`：", body, re.MULTILINE)
expected_design_ids = ["N00"] + [f"{package}{i:02d}" for package in "GCLEA" for i in range(1, 4)] + ["R00"]
assert design_ids == expected_design_ids
old_task_map = body.split('id="dd2-design-old-task-map"', 1)[1].split('id="dd2-design-copy-prompts"', 1)[0]
mapped_paper_ids = []
for first, last in re.findall(r"^\| P(\d\d)(?:–P(\d\d))? \|", old_task_map, re.MULTILINE):
    mapped_paper_ids.extend(range(int(first), int(last or first) + 1))
assert mapped_paper_ids == list(range(1, 23))
for package in "GCLEA":
    assert f"**{package}01–{package}03：**" in body

chapters = [
    "引言",
    "DD1 与 DD2",
    "从一步下降到实际轨道",
    "优化结构与补偿边界",
    "应用",
]
chapter_titles = re.findall(r"^\| ([1-5]) ([^|]+?) \|", legacy, re.MULTILINE)
assert chapter_titles == [(str(i), title) for i, title in enumerate(chapters, 1)]
chapter_tasks = {
    3: ("dd2-nonabsolute-main-task", "dd2-length-main-task"),
    4: ("dd2-optimization-main-task",),
    5: ("dd2-cp-main-task",),
}
for chapter, anchors in chapter_tasks.items():
    chapter_row = next(line for line in legacy.splitlines() if line.startswith(f"| {chapter} "))
    for anchor in anchors:
        assert f"](#{anchor})" in chapter_row
        assert body.count(f'id="{anchor}"') == 1
assert body.count('id="dd2-paper-required-inventory"') == 1
paper_inventory = body.split('id="dd2-paper-required-inventory"', 1)[1].split('id="dd2-editorial-280"', 1)[0]
assert [int(x) for x in re.findall(r"^\| P(\d\d) \|", paper_inventory, re.MULTILINE)] == list(range(1, 23))

checklist = repo / "research/audit/DD2_ACCEPTANCE_CHECKLIST.md"
checklist_body = checklist.read_text(encoding="utf-8")
checklist_ids = re.findall(r"^- \[[ x]\] `([A-Z0-9.]+)` ", checklist_body, re.MULTILINE)
editorial_table = body.split('id="dd2-editorial-280"', 1)[1].split("## 既有数学素材", 1)[0]
editorial_rows = re.findall(
    r"^\| ([A-Z0-9.]+) \| ([^|]+?) \| ([^|]+?) \| ([^|]+?) \|$",
    editorial_table,
    re.MULTILINE,
)
assert len(checklist_ids) == len(set(checklist_ids)) == 280
assert [item for item, _, _, _ in editorial_rows] == checklist_ids
assert len({result.rstrip("。") for _, result, _, _ in editorial_rows}) == 280
assert len({reason.rstrip("。") for _, _, _, reason in editorial_rows}) == 280
editorial_destinations = {item: destination for item, _, destination, _ in editorial_rows}
for item, destination in {
    "S05.04": "第3章主结论",
    "Q08": "第4章主结论",
    "S14.CP": "第5章主结论",
    "S14.DR": "第5章候补／对照",
    "S11.06": "第4章候补",
}.items():
    assert editorial_destinations[item] == destination

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

# C430: independently compare the new piecewise expression with the original
# three signed lower gates (RC9), including actual nonemptiness and endpoints.
def old_compensation(t, c, q, attained, phi):
    if q is None:  # Empty strict superlevel.
        return True
    return (
        (2 * c >= t and phi >= c * (t - c))
        or phi >= (t * t - c * c - q * q) / 2
        or (2 * q >= t and (
            phi > q * (t - q)
            or (phi == q * (t - q) and not attained)
        ))
    )


def piecewise_sigma(r, z):
    if 1 - r <= z <= 1 + r:
        return (r * r + z * z - 1) / 2
    if z > 1 + r:
        return z * (z - 1)
    if 2 * r >= 1:
        return r * (r - 1)
    return None  # No nonempty successful free one-edge class.


def new_compensation(t, c, q, attained, phi):
    if q is None:
        return True
    r, z = c / t, q / t
    threshold = piecewise_sigma(r, z)
    if threshold is None:
        return False
    sigma = -phi / (t * t)
    return sigma < threshold if z > 1 + r and attained else sigma <= threshold


piecewise_checks = 0


def compare_gates(t, c, q, attained, b, nonempty_endpoint=True):
    global piecewise_checks
    beta = max(t / 2, b)
    upper = beta * (t - beta)
    gates = {Fraction(0), t * t / 4, upper, c * (t - c)}
    if q is not None:
        gates.update({(t * t - c * c - q * q) / 2, q * (t - q)})
    epsilon = t * t / 128
    for phi in {gate + shift for gate in gates for shift in (-epsilon, 0, epsilon)}:
        nonempty = phi < upper or (phi == upper and nonempty_endpoint)
        old = nonempty and old_compensation(t, c, q, attained, phi)
        new = nonempty and new_compensation(t, c, q, attained, phi)
        assert old == new, (t, c, q, attained, b, phi, old, new)
        piecewise_checks += 1


for t, lam, values in product(
    map(Fraction, (1, 2)),
    (Fraction(1, 2), Fraction(1), Fraction(2)),
    product((Fraction(0), Fraction(1, 2), Fraction(2)), repeat=3),
):
    raw = dict(zip((Fraction(0), Fraction(1, 2), Fraction(2)), values))
    b = min(max(lam * rho, t - value) for rho, value in raw.items())
    for ratio in (Fraction(0), Fraction(1, 4), Fraction(1, 2), Fraction(3, 4), Fraction(7, 8)):
        c = ratio * t
        bad = [lam * rho for rho, value in raw.items() if value > c]
        compare_gates(t, c, min(bad) if bad else None, bool(bad), b)

# Ordinary inverse, arbitrary values of L, and all piecewise switching lines.
for L in (Fraction(1, 10), Fraction(1, 4), Fraction(1, 2), Fraction(1), Fraction(2)):
    for r in (Fraction(0), Fraction(1, 4), Fraction(1, 2), Fraction(3, 4), Fraction(7, 8)):
        compare_gates(Fraction(1), r, r / L, False, 1 / (1 + L))
        if r * r >= L * L / (1 + L * L):
            original = (
                r * (r - L) / (L * L)
                if L < Fraction(1, 2) and r > L / (1 - L)
                else ((1 + L * L) * r * r - L * L) / (2 * L * L)
            )
            assert piecewise_sigma(r, r / L) == original
            piecewise_checks += 1
    if L < Fraction(1, 2):
        switch = L / (1 - L)
        assert piecewise_sigma(switch, switch / L) == switch * (switch - L) / (L * L)

# Same first bad residual, distinct open/closed root endpoint; the energy
# endpoint stays safe even if the first bad residual belongs to the layer.
assert not new_compensation(Fraction(1), Fraction(1, 2), Fraction(2), True, Fraction(-2))
assert new_compensation(Fraction(1), Fraction(1, 2), Fraction(2), False, Fraction(-2))
assert new_compensation(Fraction(1), Fraction(1, 2), Fraction(3, 2), True, Fraction(-3, 4))
compare_gates(Fraction(1), Fraction(1, 2), Fraction(2), False, Fraction(1))
compare_gates(Fraction(1), Fraction(1, 2), Fraction(0), False, Fraction(1, 2), False)

core = (repo / "research/topics/dd2/core.md").read_text(encoding="utf-8")
assert core.index('id="dd2-main-theorem"') < core.index('id="dd2-linear-recovery"') < core.index('id="dd2-exact-statements"')
assert all(f"\\tag{{DD2.{i}}}" in core for i in range(1, 10))
print(f"DD outline verified: 5 author chapters, abstract and conclusion; "
      f"17 design-task contracts with copy prompts and all 22 legacy tasks mapped; "
      f"5 historical chapters, 4 legacy proof tasks, 22 paper deliverables, 280 individually ranked answers, 6 indexed source sections, "
      f"{len(claim_ids)} claim records, {len(links)} local links, 7 legacy exact algebra checks; "
      f"{piecewise_checks} exact piecewise compensation comparisons and explicit endpoint checks.")
