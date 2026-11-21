"""Verify the original DD2 protocol checklist and its single-item sign-offs."""

import argparse
import hashlib
from pathlib import Path
import re
import subprocess
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[3]
PROTOCOL = Path("research/topics/dd2/DD2_FINAL_ACCEPTANCE_PROTOCOL.md")
CHECKLIST = Path("research/audit/DD2_ACCEPTANCE_CHECKLIST.md")
PROTOCOL_SHA256 = "159bb4a947417f6b06cc0a611384603a24c9818be562b0c3cdcadfc473b39a33"
REMOTE = "refs/remotes/origin/main"
UNCLAIMED = "待认领"

MAIN_COUNTS = (10, 10, 10, 10, 10, 10, 10, 8, 12, 12, 10, 12, 12, 12, 10, 8, 15)
EXTRA = {
    1: (
        ("THEOREM", "交出 Exact Theorem Statement，写清对象、量词、定义域、工作区域、零点集、投影选择、参数依赖与结论，并记录假设变化对应的版本。"),
    ),
    3: (
        ("GATE", "在原协议指定换参下严格恢复 DD1 临界函数 T(L)，同时给出严格门的正面证明与等号或越界的实际失败证据。"),
        ("SCOPES", "分别验收自由四点几何与完整局部 PPA 算子类的尖锐性，核对构造满足各自全部假设。"),
    ),
    4: (
        ("IMPLICATIONS", "给出严格距离下降、距离趋零、点收敛和有限长度之间的精确蕴含关系，逐条给出所需附加条件或反例。"),
    ),
    5: (
        ("F1", "定位作者原稿 F1 的精确版本并独立核验它如何吸收缺陷。"),
        ("F2", "定位作者原稿 F2 的精确版本并独立核验逆模条件及其作用。"),
        ("F3", "定位作者原稿 F3 的精确版本并独立核验被积函数和单调上包络条件。"),
        ("TELESCOPE", "独立重构原 F1–F3 对应的同一步长度势、望远镜求和与局部留域，逐项注明可以省去的条件。"),
    ),
    6: (
        ("ABOVE", r"针对原协议的幂次误差界，在 \(pq>2\) 区域按 \(q\) 分区验收距离、点与有限长度结论。"),
        ("CRITICAL", r"在 \(pq=2\) 区域逐分支证明临界常数、严格侧和等号侧的结论与构造。"),
        ("BELOW", r"在 \(pq<2\) 区域逐分支验收正面结果、失败范围和实际近端反例。"),
        ("TAIL", r"独立复核 \(\alpha=2-1/q\) 的实际总长度估计，明确 \(q\) 的范围、常数选择、局部不变性及边界。"),
    ),
    7: (
        ("EXAMPLES", "逐一核验关键实例的完整定义、参数、零点集、工作域、所有合法输出、失效的旧假设及新结论。"),
    ),
    8: (
        ("ROTATION", "严格复核原二维旋转反例，核对所有近端与算子量词。"),
        ("POWER", "严格复核非单调幂次例子，核对完整真残差与轨道。"),
        ("BOUNDARY", "给八个猜想补齐实际边界攻击，保存已反驳版本的精确反例及失败机制。"),
    ),
    9: (
        ("SOURCE", "逐式核对 Alcantara 原文的空间、逆算子、预条件器和约化表示，注明版本和位置。"),
        ("DOMAINS", "逐式核对约化表示的定义域、图对应、完整或允许纤维以及适用量词。"),
    ),
    10: (
        ("SCOPES", "逐条注明九类恢复的对象为实际 shadow、投影 shadow 或指定 recovery selection，独立核验局部有界性、Lipschitz 与全选择量词。"),
    ),
    11: (
        ("GRAPH", "交出双残差与正则性传递的精确逻辑关系图，给每个箭头附条件、证明或反例。"),
    ),
    12: (
        ("RATES", "逐个区分迭代点、零集距离、残差、best-iterate 与 ergodic average 的速率对象、量词及边界。"),
    ),
    13: (
        ("VERSIONS", "分别登记精确算法与非精确算法的 Claim 版本并核对二者的假设、输出和误差量词。"),
    ),
    14: (
        ("CP", "汇总并复核 Chambolle–Pock 对原 §14 十二问的逐项具体验证。"),
        ("DR", "汇总并复核 Douglas–Rachford 对原 §14 十二问的逐项具体验证。"),
        ("THEOREM", "提交至少一个具有完整对象、条件与证明的实际算法应用定理及可核算子实例。"),
        ("APPLICABILITY", "逐一验收其余被声称覆盖的算法。仅有候选机制的算法按原协议列为潜在应用。"),
    ),
    17: (
        ("REVIEW", "按具体 Claim 版本保存独立重推、反例攻击和 15 项审查结果，逐一裁决所有仍成立的致命异议及其影响。"),
    ),
}
FINISH = (
    ("META.STATES", "按第十部分复查全部成果的数学状态，保留真值、范围和可靠性边界。"),
    ("META.CLAIMS", "核实每个重要 Claim 都有原协议列出的 Exact Statement、Objects、Domain、Quantifiers、Assumptions、Conclusion、Dependencies、Evidence、Counterevidence、Status 和 Related Files。"),
    ("META.PERSISTENCE", "复核第十一部分的可恢复性，从远端 main 与研究地图重建已验收结果，核查逐项提交、持久化与证据定位。"),
    ("META.GOAL", "用可复核的数学证据直接回答原协议开篇的核心问题，交代统一理论的成立范围、严格新结果、既有机制和已证明的障碍。"),
)

TASK = re.compile(r"^- \[([ x])\] \x60([A-Z0-9.]+)\x60 (.+)$", re.MULTILINE)
ACTIVE = re.compile(r"^\*\*当前认领\*\* \x60([^\x60\n]+)\x60$", re.MULTILINE)
FIELDS = ("裁决", "结论", "证据", "复核")
FIELD = re.compile(r"^  - \*\*(裁决|结论|证据|复核)\*\* (.+)$", re.MULTILINE)
CLOSED = {
    "Proved", "Sharp", "Strict Extension", "Equivalent / Recovered",
    "Refuted", "Invalid", "Verified", "Delivered",
}


def source_groups():
    """Read primary task wording from the immutable protocol."""
    raw = (ROOT / PROTOCOL).read_bytes()
    if hashlib.sha256(raw).hexdigest() != PROTOCOL_SHA256:
        raise ValueError("原协议内容变更，请先恢复作者原版。")
    source = raw.decode()
    main, rest = source.split("# 第八部分：", 1)
    headings = list(re.finditer(r"^## (\d+)\. (.+)$", main, re.MULTILINE))
    groups = []
    bullet_labels = {2: "F", 10: "R", 15: "L"}
    for index, heading in enumerate(headings):
        number = int(heading[1])
        end = headings[index + 1].start() if index + 1 < len(headings) else len(main)
        section = main[heading.end():end]
        prefix = f"S{number:02d}."
        if number == 8:
            items = [(f"{j:02d}", text) for j, text in enumerate(bullets(section), 1)]
        elif number == 16:
            items = re.findall(r"^\*\*([A-H])\. (.+?)\*\*\n\n([^\n]+)", section, re.MULTILINE)
            items = [(letter, f"{label}。{question}") for letter, label, question in items]
        else:
            items = [(f"{int(j):02d}", text) for j, text in numbered(section)]
        if len(items) != MAIN_COUNTS[index]:
            raise ValueError(f"原协议第 {number} 节主项数量不符。")
        if number in bullet_labels:
            label = bullet_labels[number]
            items.extend((f"{label}{j:02d}", text) for j, text in enumerate(bullets(section), 1))
        items.extend(EXTRA.get(number, ()))
        groups.append((f"§{number} {heading[2]}", [(prefix + key, text) for key, text in items]))

    if len(headings) != len(MAIN_COUNTS):
        raise ValueError("原协议节数不符。")
    deep, rest = rest.split("# 第九部分：", 1)
    deep_items = [(f"Q{int(j):02d}", text) for j, text in numbered(deep)]
    deliverables, rest = rest.split("# 第十部分：", 1)
    deliveries = re.findall(r"^\*\*(\d+)\. (.+?)\*\*\n\n([^\n]+)", deliverables, re.MULTILINE)
    delivery_items = [(f"D{int(j):02d}", f"{title}。{text}") for j, title, text in deliveries]
    last = rest.split("# 最终验收：", 1)[1].split("## 最终执行指令", 1)[0]
    final_items = [
        (f"Z{j:02d}", f"{question} {requirement}")
        for j, (question, requirement) in enumerate(
            re.findall(r"^\*\*第[一二三四五六]：(.+?)\*\*\n\n([^\n]+)", last, re.MULTILINE), 1
        )
    ]
    if (len(deep_items), len(delivery_items), len(final_items)) != (28, 10, 6):
        raise ValueError("深层问题、强制交付物或最终六问数量不符。")
    return groups + [
        ("第八部分 · 28 个深层问题", deep_items),
        ("第九部分 · 10 项强制交付物", delivery_items),
        ("最终六问", final_items),
        ("总目标与项目验收复核", FINISH),
    ]


def numbered(text):
    return re.findall(r"^(\d+)\. (.+)$", text, re.MULTILINE)


def bullets(text):
    return re.findall(r"^- (.+)$", text, re.MULTILINE)


def git(*args, optional=False):
    result = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
    if result.returncode and not optional:
        raise ValueError(result.stderr.strip() or f"git {args[0]} 执行失败")
    return result.stdout if result.returncode == 0 else None


def first_pending(rows):
    return next((key for key, checked in rows.items() if not checked), None)


def validate(text, expected, snapshot=""):
    markers = list(TASK.finditer(text))
    if [(task[2], task[3]) for task in markers] != expected:
        raise ValueError("任务编号、顺序或题面与原协议清单不一致。")
    if len(re.findall(r"^- \[[ xX]\]", text, re.MULTILINE)) != len(markers):
        raise ValueError("存在未按格式登记的勾选框。")
    active = ACTIVE.findall(text)
    rows = {task[2]: task[1] == "x" for task in markers}
    if len(active) != 1 or active[0] not in (UNCLAIMED, first_pending(rows)):
        raise ValueError("只能认领第一项未勾任务。")
    for index, task in enumerate(markers):
        if not rows[task[2]]:
            continue
        end = markers[index + 1].start() if index + 1 < len(markers) else len(text)
        fields = FIELD.findall(text[task.end():end])
        if tuple(key for key, _ in fields) != FIELDS:
            raise ValueError(f"{task[2]} 缺少按顺序填写的裁决、结论、证据或复核。")
        record = dict(fields)
        if record["裁决"].strip("\x60") not in CLOSED:
            raise ValueError(f"{task[2]} 的状态不能用于终结。")
        if not local_evidence(record["证据"], snapshot):
            raise ValueError(f"{task[2]} 缺少仓库内可定位的证据文件。")
    return rows, active[0]


def local_evidence(field, snapshot):
    for link in re.findall(r"\[[^]\n]+\]\(([^)\n]+)\)", field):
        target = urlsplit(link.strip("<>"))
        if target.scheme or not target.path:
            continue
        path = (ROOT / CHECKLIST.parent / unquote(target.path)).resolve()
        if not path.is_relative_to(ROOT) or path == ROOT / CHECKLIST:
            continue
        if snapshot:
            version = f"{snapshot}{path.relative_to(ROOT).as_posix()}"
            if git("cat-file", "-t", version, optional=True) != "blob\n":
                continue
        elif not path.is_file():
            continue
        if path.suffix.casefold() == ".md" and target.fragment:
            anchor = re.escape(unquote(target.fragment))
            body = git("show", version) if snapshot else path.read_text(encoding="utf-8")
            if not re.search(rf"\bid=[\"']{anchor}[\"']", body):
                continue
        return True
    return False


def verify_staged(rows, active, expected):
    before_text = git("show", f"HEAD:{CHECKLIST}", optional=True)
    if before_text is None:
        if any(rows.values()):
            raise ValueError("首次落库必须保留全部任务待验。")
        return
    before, _ = validate(before_text, expected, "HEAD:")
    added = [key for key, done in rows.items() if done and not before[key]]
    if not added:
        return
    if added != [first_pending(before)] or active != UNCLAIMED:
        raise ValueError("一次只能勾选原来的第一项未勾任务，交付后清空当前认领。")
    remote_text = git("show", f"{REMOTE}:{CHECKLIST}")
    remote, _ = validate(remote_text, expected, f"{REMOTE}:")
    if any(done and not remote[key] for key, done in before.items()):
        raise ValueError("先 push 前一项并核验 origin/main，再终结当前项。")


def verify_history(expected):
    history = git(
        "log", "--first-parent", "--reverse", "--no-color", "--no-ext-diff", "-p", "-U0",
        "--format=DD2-COMMIT %s", REMOTE, "--", str(CHECKLIST),
    )
    closed = set()
    for patch in history.split("\nDD2-COMMIT "):
        removed = re.findall(r"^-- \[x\] \x60([A-Z0-9.]+)\x60 ", patch, re.MULTILINE)
        closed.difference_update(removed)
        added = re.findall(r"^\+- \[x\] \x60([A-Z0-9.]+)\x60 ", patch, re.MULTILINE)
        if added:
            subject = patch.splitlines()[0].removeprefix("DD2-COMMIT ")
            next_key = next((key for key, _ in expected if key not in closed), None)
            if added != [next_key] or not subject.startswith(f"DD2 {added[0]}: "):
                raise ValueError(f"勾选必须在单项提交中完成，发现违规提交 {subject!r}。")
            closed.update(added)
    if closed != {key for key, _ in expected}:
        raise ValueError("远端提交历史未逐项记录完整验收。")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--staged", action="store_true", help="检查暂存区内的单项交付")
    modes.add_argument("--final", action="store_true", help="检查已抓取的 origin/main 是否全部完成")
    args = parser.parse_args()
    try:
        expected = [task for _, tasks in source_groups() for task in tasks]
        snapshot = ":" if args.staged else f"{REMOTE}:" if args.final else ""
        if snapshot and hashlib.sha256(git("show", f"{snapshot}{PROTOCOL}").encode("utf-8")).hexdigest() != PROTOCOL_SHA256:
            raise ValueError("受检 Git 版本没有保留作者原协议。")
        text = git("show", f"{snapshot}{CHECKLIST}") if snapshot else (ROOT / CHECKLIST).read_text(encoding="utf-8")
        rows, active = validate(text, expected, snapshot)
        if args.staged:
            verify_staged(rows, active, expected)
        pending = first_pending(rows)
        print(f"已勾选 {sum(rows.values())}/{len(rows)}；当前认领 {active}；首个未勾 {pending or '无'}。")
        if args.final:
            if pending:
                raise ValueError("最终验收未达到结束条件。")
            verify_history(expected)
            print("origin/main 的清单及单项提交历史通过结构校验。")
    except ValueError as error:
        parser.exit(1, f"{error}\n")


if __name__ == "__main__":
    main()
