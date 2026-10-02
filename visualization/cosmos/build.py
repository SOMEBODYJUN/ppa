#!/usr/bin/env python3
"""Rebuild offline SVG/D3 cosmos from authoritative graph and stable anchors."""
import json, pathlib, hashlib
HERE=pathlib.Path(__file__).resolve().parent
ROOT=HERE.parent.parent
graph=json.loads((ROOT/'research/graph.json').read_text())
anchor_path=HERE/'data'/'anchors.json'
anchor_path.parent.mkdir(exist_ok=True)
anchors=json.loads(anchor_path.read_text()) if anchor_path.exists() else {}
# Actual seed anchors are emitted by the shared JS engine. Existing records survive append/reorder.
import subprocess
result=subprocess.run(['node','-e',"const C=require('./src/universe.js'),fs=require('fs');const g=JSON.parse(fs.readFileSync('../../research/graph.json'));const p=JSON.parse(fs.readFileSync('./data/anchors.json'));console.log(JSON.stringify(C.make(g,{anchors:p}).anchors,null,2));"],cwd=HERE,capture_output=True,text=True) if anchor_path.exists() else None
if not anchor_path.exists(): anchor_path.write_text('{}\n')
if result is None: result=subprocess.run(['node','-e',"const C=require('./src/universe.js'),fs=require('fs');console.log(JSON.stringify(C.make(JSON.parse(fs.readFileSync('../../research/graph.json'))).anchors,null,2));"],cwd=HERE,capture_output=True,text=True)
if result.returncode: raise RuntimeError(result.stderr)
anchor_path.write_text(result.stdout)
anchors=json.loads(result.stdout)
def safe_json(x):return json.dumps(x,ensure_ascii=False,separators=(',',':')).replace('</','<\\/')
subs={'__CSS__':(HERE/'src/style.css').read_text(),'__GRAPH__':safe_json(graph),'__ANCHORS__':safe_json(anchors),'__D3__':(HERE/'vendor/d3.v7.9.0.min.js').read_text(),'__ENGINE__':(HERE/'src/universe.js').read_text()+'\n'+(HERE/'src/visuals.js').read_text(),'__APP__':(HERE/'src/app.js').read_text()}
page=(HERE/'src/template.html').read_text()
for k,v in subs.items():page=page.replace(k,v)
(HERE/'index.html').write_text(page)
print(f'Built {len(graph["nodes"])} nodes and {len(graph["edges"])} exact hyperedges; {len(page.encode())} bytes, offline D3/SVG.')
