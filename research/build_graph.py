"""Validate the mathematical hypergraph and generate its Markdown/HTML views."""
import html
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

def esc(s):
    return html.escape(str(s), quote=True)

cards = []
for e in data["edges"]:
    names = [nodes[i]["label"] for i in e["inputs"]]
    search = " ".join([e["id"], e["topic"], e["scope"], e["status"], nodes[e["output"]]["label"]] + names).lower()
    inputs = " <strong>∧</strong> ".join(
        f'<a class="node" href="{esc(nodes[i]["file"])}">{esc(i)} · {esc(nodes[i]["label"])}</a>'
        for i in e["inputs"])
    out = nodes[e["output"]]
    cards.append(
        f'<article class="edge" data-topic="{esc(e["topic"])}" data-search="{esc(search)}">'
        f'<div class="tag">{esc(e["id"])} · {esc(e["topic"])} · {esc(e["relation"])}</div>'
        f'<div class="equation">{inputs} <b>→</b> '
        f'<a class="node output" href="{esc(out["file"])}">{esc(e["output"])} · {esc(out["label"])}</a></div>'
        f'<p>{esc(e["scope"])}</p><small>{esc(e["status"])}</small></article>')
buttons = '<button data-topic="*" class="active">全部</button>' + "".join(
    f'<button data-topic="{esc(t)}">{esc(t)} · {len(groups[t])}</button>' for t in groups)
page = """<!doctype html><html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>PPA 数学超边图</title>
<style>
:root{--ink:#182a2e;--muted:#53696d;--bg:#f5f5f0;--line:#c8d5d0;--accent:#12675f}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.55 system-ui,"Noto Sans CJK SC",sans-serif}
header{padding:2.5rem max(1.5rem,calc((100vw - 1100px)/2));background:#143137;color:#f3f5ef}
h1{margin:0;font-size:clamp(1.8rem,4vw,3rem)}header p{max-width:860px;margin:.5rem 0;color:#d5e4dc}header a{color:#b6e9d6}
main{max-width:1140px;margin:auto;padding:1.5rem}.controls{position:sticky;top:0;background:var(--bg);padding:.8rem 0;border-bottom:1px solid var(--line)}
input{width:100%;font:inherit;padding:.65rem;border:1px solid var(--line);border-radius:8px}.filters{display:flex;gap:.4rem;flex-wrap:wrap;margin:.75rem 0}
button{background:white;border:1px solid var(--line);border-radius:16px;padding:.3rem .7rem;cursor:pointer}
button.active{background:var(--accent);color:white}#count{color:var(--muted)}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,500px),1fr));gap:.85rem}
.edge{background:white;border:1px solid var(--line);border-left:4px solid var(--accent);border-radius:8px;padding:1rem}.tag{font-size:.85rem;color:var(--accent);font-weight:700}
.equation{margin:1rem 0;line-height:2}.equation b{color:var(--accent)}.node{display:inline-block;background:#edf5f0;color:var(--ink);text-decoration:none;border-radius:5px;padding:.1rem .4rem;font-size:.89rem}
.node:hover{text-decoration:underline}.output{background:#d9ebe5;font-weight:700}.edge p{color:#344b4e;margin:.4rem 0}.edge small{color:#79572d}
footer{max-width:1140px;margin:2rem auto;padding:1rem 1.5rem;border-top:1px solid var(--line);color:var(--muted)}
</style></head><body>
<header><h1>PPA 数学超边图</h1><p>一条边的全部输入必须同时成立。范围与证据状态决定它能否用于新命题；open 仅表示待解决目标。</p>
<p><a href="HYPERGRAPH.md">Markdown 关系表</a> · <a href="SOURCES.md">原始来源索引</a></p></header>
<main><div class="controls"><input id="query" type="search" aria-label="搜索超边" placeholder="搜索命题、条件、障碍">
<div class="filters">""" + buttons + """</div></div><p id="count"></p><div class="grid">""" + "".join(cards) + """</div></main>
<footer>关系数据：<a href="graph.json">graph.json</a>。本图是研究导航，命题真值以精确证明和未决异议为准。</footer>
<script>
const q=document.querySelector("#query"), cards=[...document.querySelectorAll(".edge")], count=document.querySelector("#count");
let topic="*";function update(){let n=0,term=q.value.trim().toLowerCase();for(const card of cards){let show=(topic==="*"||card.dataset.topic===topic)&&card.dataset.search.includes(term);card.hidden=!show;if(show)n++}count.textContent="显示 "+n+" / "+cards.length+" 条超边"}
q.addEventListener("input",update);document.querySelectorAll("button[data-topic]").forEach(b=>b.addEventListener("click",()=>{topic=b.dataset.topic;document.querySelector("button.active").classList.remove("active");b.classList.add("active");update()}));update();
</script></body></html>"""
(ROOT / "map.html").write_text(page, encoding="utf-8")
print(f'Validated {len(nodes)} nodes and {len(data["edges"])} hyperedges.')
