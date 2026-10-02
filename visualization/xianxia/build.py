"""Build the independent, offline Xianxia visualization from authoritative graph data."""
import base64, json, sys, html
from pathlib import Path
ROOT=Path(__file__).resolve().parent;REPO=ROOT.parents[1]
sys.path.insert(0,str(ROOT/'src'))
from world import grow

def dump(data):return json.dumps(data,ensure_ascii=False,indent=2)+'\n'
def embedded(data,ident):return '<script type="application/json" id="'+ident+'">'+json.dumps(data,ensure_ascii=False).replace('<','\\u003c')+'</script>'
def build():
 graph=json.loads((REPO/'research/graph.json').read_text());catalog=json.loads((ROOT/'data/objects.json').read_text())
 target=ROOT/'data/world.json';prev=json.loads(target.read_text()) if target.exists() else None
 world=grow(graph,catalog['objects'],prev);target.write_text(dump(world))
 full={**catalog,'objects':[{**o,'data':'data:image/svg+xml;base64,'+base64.b64encode((ROOT/o['file']).read_bytes()).decode()} for o in catalog['objects']]}
 page=(ROOT/'src/template.html').read_text()
 contents={'<!-- MAP_STYLE -->':'<style>\n'+(ROOT/'src/map.css').read_text()+'\n</style>','<!-- GRAPH_DATA -->':embedded(graph,'graph-data'),'<!-- WORLD_DATA -->':embedded(world,'world-data'),'<!-- OBJECT_DATA -->':embedded(full,'object-data'),'<!-- MAP_SCRIPT -->':'<script>\n'+(ROOT/'src/map.js').read_text()+'\n</script>'}
 for marker,text in contents.items():assert page.count(marker)==1;page=page.replace(marker,text)
 (ROOT/'index.html').write_text(page)
 groups={'village':('壹 · 书院与山门','定义、约定、规范入口的导航外观。建筑高低不等于理论等级。'),'mine':('贰 · 法器与灵物','研究对象有多种形象；丹成、剑光、灵泉都不表示命题已证。'),'mountain':('叁 · 山海与秘境','开放目标与显式候选可用不同风物；候选状态由独立徽记说明。'),'barrier':('肆 · 禁制与断路','被反驳目标与障碍的多种轮廓；必须点开具体被阻断的关系。')}
 sections=[]
 for family,(title,desc) in groups.items():
  cards=[]
  for o in full['objects']:
   if o['family']!=family:continue
   cards.append(f'<article class="object-card" id="{o["id"]}"><div class="art-stage"><img class="large" src="{o["data"]}" alt="{o["name"]}"/><div class="actual"><img src="{o["data"]}" alt=""/><span>地图尺寸 82 px</span></div></div><div class="card-copy"><span class="object-id">{o["id"]}</span><h3>{o["name"]}</h3><p>透明 SVG · 统一落点 (72, 122)</p><a href="{o["file"]}">查看可编辑原件 ↗</a></div></article>')
  sections.append(f'<section id="{family}"><header class="section-head"><h2>{title}</h2><p>{desc}</p></header><div class="object-grid">'+''.join(cards)+'</div></section>')
 gallery='''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>云岫 · 万象图鉴</title><style>'''+(ROOT/'src/gallery.css').read_text()+'''</style></head><body><header class="gallery-head"><a href="index.html">云岫 <span>YUNXIU</span></a><nav><a href="#village">书院</a><a href="#mine">灵物</a><a href="#mountain">山海</a><a href="#barrier">禁制</a><a href="index.html">进入山海图 ↗</a></nav></header><main><div class="hero"><span class="eyebrow">A BESTIARY OF MATHEMATICAL IDEAS · VOLUME 01</span><h1>万象各有形<br><em>一念入山海。</em></h1><p>先看清一座山、一座书院、一处断桥，<br>再让它们成为一片可以生长的研究天地。</p><div class="hero-meta"><span>32 种独立轮廓</span><span>4 组导航物件</span><span>青绿 · 金石 · 统一落点</span></div></div>'''+''.join(sections)+'''<section class="array"><div><span class="eyebrow">CONJUNCTION ARRAY</span><h2>多符汇一阵，前提缺一不可。</h2><p>物件可以多变，数学关系不能随画风变。全部输入进入同一 ∧ 阵眼，再到输出。等价为双向，限制与反驳是边界，开放云路不是证明。</p><a href="index.html">进入真实 294 节点、194 条关系的地图 ↗</a></div><svg viewBox="0 0 520 180" role="img" aria-label="三个输入汇入合取阵眼再到输出"><g fill="none" stroke="#719b8a" stroke-width="2"><path d="M55 36L256 90M55 90H256M55 144L256 90M256 90H470"/><circle cx="256" cy="90" r="34"/><circle cx="256" cy="90" r="26"/><path d="M249 48L256 38 264 49M249 132L256 142 264 131"/></g><g fill="#d4b46b"><circle cx="55" cy="36" r="10"/><circle cx="55" cy="90" r="10"/><circle cx="55" cy="144" r="10"/><path d="M461 83L472 90 461 97"/></g><g fill="#e9e2c6" font-family="serif" text-anchor="middle"><text x="256" y="101" font-size="34">∧</text><text x="482" y="114" font-size="14">输出</text><text x="105" y="166" font-size="12">全部输入 · 同时成立</text></g></svg></section><footer>此页是首批物件美术验收册。外观不是数学证据；每一个节点都保留原始身份和关系。<br><a href="SEMANTIC_ATLAS.md">物件语义契约</a> · <a href="README.md">生成与交接</a></footer></main></body></html>'''
 (ROOT/'gallery.html').write_text(gallery)
 print(f'Built map/gallery: {len(graph["nodes"])} nodes, {len(graph["edges"])} edges, {len(catalog["objects"])} objects, {len(world["realms"])} realms')
if __name__=='__main__':build()
