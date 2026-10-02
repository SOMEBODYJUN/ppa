"""Validate the mathematical hypergraph and generate its Markdown/HTML views."""
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
data = json.loads((ROOT / "graph.json").read_text(encoding="utf-8"))
nodes = {n["id"]: n for n in data["nodes"]}
assert len(nodes) == len(data["nodes"]), "duplicate node"
assert len({e["id"] for e in data["edges"]}) == len(data["edges"]), "duplicate edge"
for n in nodes.values():
    file, _, anchor = n["file"].partition("#")
    assert (ROOT / file).is_file(), n
    if anchor:
        assert f'id="{anchor}"' in (ROOT / file).read_text(encoding="utf-8"), n
for e in data["edges"]:
    assert e["inputs"] and all(i in nodes for i in e["inputs"])
    assert e["output"] in nodes and e["output"] not in e["inputs"], e
    assert len(e["inputs"]) == len(set(e["inputs"])), e
    assert e["relation"] in {"conditional", "equivalence", "implies", "limits", "necessary", "open", "refutes", "sharpness", "sufficient"}, e
    assert e["scope"].strip() and e["status"].strip(), e

groups = defaultdict(list)
for e in data["edges"]:
    groups[e["topic"]].append(e)

def link(node_id):
    n = nodes[node_id]
    return f'[{node_id} · {n["label"]}]({n["file"]})'

md = [
    "# 数学关系超边图", "",
    "本图从 [graph.json](graph.json) 生成；运行 python3 research/build_graph.py 同时生成本页和 [交互 HTML](map.html)。"
    "每条边的输入是**合取**；范围、版本及证据状态不可省。节点链接进入重构的数学模块，原始证据见 [SOURCES.md](SOURCES.md)。", "",
    "关系 conditional 带有额外前提，open 是目标而非证明，limits 是反例或边界；"
    "necessary 和 sufficient 分别对应纤维分类的两个方向；sharpness 只给声明范围内的下界见证。", ""
]
for group, edges in groups.items():
    md += ["## " + group, "", "| 边 | 联合输入 | 关系 → 输出 | 精确范围与证据 |",
           "| --- | --- | --- | --- |"]
    for e in edges:
        ins = " ∧ ".join(link(i) for i in e["inputs"])
        scope = e["scope"].replace("|", r"\|")
        md.append(f'| {e["id"]} | {ins} | {e["relation"]} → {link(e["output"])} | {scope}；**{e["status"]}** |')
    md.append("")
md += [
    "## 不蕴含关系", "",
    "- 局部单值 J_G 不推出完整 J_F 单值；见 [解选择反例](solution_selection.md)。",
    "- 固定紧源 Φ proper 不推出保纲，也不恢复域外原图；见 [算子空间](operator_space.md)。",
    "- 任意紧零集可在全局 RL 实现，不保证局部 EB、Dini、coverage 与回缩；见 [结构与拓扑](holder_structure.md)。",
    "- 有限样本不验证指定 T 在整窗的 usc/acyclicity；见 [局部值域](holder_structure.md)。",
    "- 锥 MSCQ、条件 Markov 残差与确定性 RLEB 属于不同对象；见 [额外桥](cone_markov.md)。", ""
]
(ROOT / "HYPERGRAPH.md").write_text("\n".join(md), encoding="utf-8")

# The map has no network/runtime dependencies: graph data and UI sources are
# embedded so map.html works when opened directly from a repository checkout.
# Edit map/template.html, map/map.css and map/map.js, then run this generator.
ui = ROOT / "map"
page = (ui / "template.html").read_text(encoding="utf-8")
embedded_data = json.dumps(data, ensure_ascii=False).replace("<", "\\u003c")
for marker, content in {
    "<!-- MAP_STYLE -->": "<style>\n" + (ui / "map.css").read_text(encoding="utf-8") + "\n</style>",
    "<!-- GRAPH_DATA -->": '<script type="application/json" id="graph-data">' + embedded_data + "</script>",
    "<!-- MAP_SCRIPT -->": "<script>\n" + (ui / "map.js").read_text(encoding="utf-8") + "\n</script>",
}.items():
    assert page.count(marker) == 1, marker
    page = page.replace(marker, content)
(ROOT / "map.html").write_text(page, encoding="utf-8")
print(f"validated {len(nodes)} nodes and {len(data['edges'])} conjunctive edges; generated HYPERGRAPH.md and map.html")
