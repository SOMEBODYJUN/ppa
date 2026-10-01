"""Read-only validation. Run at the package root or pass an extracted root.
No research script is executed. HTML JS syntax uses the locally installed Node.
"""
import sys,json,hashlib,re,subprocess,tempfile,collections,base64
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import unquote,urlsplit

def validate_authored_schema(value, rule, schema, loc='$'):
 """Dependency-free validator for every assertion keyword used in this schema.
 Not a claim of implementing arbitrary Draft 2020-12 schemas.
 """
 allowed={'$schema','$id','title','type','required','properties','const','enum','$ref','$defs','items','minItems','maxItems','minLength','minProperties','minimum','maximum','pattern','additionalProperties'}
 unknown=set(rule)-allowed
 assert not unknown,(loc,'unsupported schema keywords',unknown)
 if '$ref' in rule:
  ref=rule['$ref'];assert ref.startswith('#/')
  target=schema
  for part in ref[2:].split('/'):target=target[part]
  return validate_authored_schema(value,target,schema,loc)
 if 'const'in rule:assert value==rule['const'],(loc,'const')
 if 'enum'in rule:assert value in rule['enum'],(loc,'enum',value)
 if 'type'in rule:
  ts=rule['type'] if isinstance(rule['type'],list) else [rule['type']]
  matches={'null':value is None,'object':isinstance(value,dict),'array':isinstance(value,list),'string':isinstance(value,str),'boolean':isinstance(value,bool),'integer':type(value)is int,'number':type(value)in (int,float)}
  assert any(matches[t] for t in ts),(loc,'type',ts,type(value).__name__)
 if isinstance(value,dict):
  assert all(k in value for k in rule.get('required',[])),(loc,'required')
  if 'minProperties'in rule:assert len(value)>=rule['minProperties'],(loc,'minProperties')
  props=rule.get('properties',{})
  if rule.get('additionalProperties') is False:assert not(set(value)-set(props)),(loc,'additionalProperties')
  for k,r in props.items():
   if k in value:validate_authored_schema(value[k],r,schema,loc+'.'+k)
 if isinstance(value,list):
  if 'minItems'in rule:assert len(value)>=rule['minItems'],(loc,'minItems')
  if 'maxItems'in rule:assert len(value)<=rule['maxItems'],(loc,'maxItems')
  if 'items'in rule:
   for i,v in enumerate(value):validate_authored_schema(v,rule['items'],schema,loc+'['+str(i)+']')
 if isinstance(value,str):
  if 'minLength'in rule:assert len(value)>=rule['minLength'],(loc,'minLength')
  if 'pattern'in rule:assert re.search(rule['pattern'],value),(loc,'pattern',value)
 if type(value) in (int,float):
  if 'minimum'in rule:assert value>=rule['minimum'],(loc,'minimum')
  if 'maximum'in rule:assert value<=rule['maximum'],(loc,'maximum')

def run(root):
 root=Path(root).resolve();nav=root/'00_从这里开始';errors=[];checks={}
 def check(name,condition,detail=None):
  checks[name]={'passed':bool(condition),'detail':detail}
  if not condition:errors.append(name)
 data=json.loads((nav/'资产关系数据.json').read_text());schema=json.loads((nav/'资产关系_schema_v2.json').read_text())
 try:
  validate_authored_schema(data,schema,schema);check('JSON_schema_all_authored_constraints',True,'Dependency-free validator covers every assertion keyword used in the supplied Draft 2020-12 schema; not a general implementation.')
 except Exception as e:check('JSON_schema_all_authored_constraints',False,str(e))
 E={e['id']:e for e in data['entities']};H={h['id']:h for h in data['hyperedges']};A={a['id']:a for a in data['assets']}
 check('unique_entity_hyperedge_asset_ids',len(E)==len(data['entities']) and len(H)==len(data['hyperedges']) and len(A)==len(data['assets']) and not(set(E)&set(H)))
 check('35_to_60_selected_entities',35<=sum(e['core'] for e in E.values())<=60)
 check('20_to_35_semantic_hyperedges',20<=len(H)<=35)
 check('all_references_and_members',all(len({m['entity_id'] for m in h['members']})==len(h['members']) and len(h['members'])>=3 and all(m['entity_id'] in E for m in h['members']) for h in H.values()))
 check('two_direction_role_encoding',all(m['direction'] in ['entity_to_relation','relation_to_entity'] and len(m['role'])>1 and m['relation_type'] in data['relation_types'] for h in H.values() for m in h['members']))
 check('both_directions_per_hyperedge',all(len({m['direction'] for m in h['members']})==2 for h in H.values()))
 check('14_relation_types_present',set(data['relation_types'])=={m['relation_type'] for h in H.values() for m in h['members']}|{h['relation_type'] for h in H.values()})
 check('cross_project_hyperedges',sum(h['cross_project'] for h in H.values())>=4)
 check('core_claims_have_complete_evidence_slots',all(any(any(m['entity_id']==e['id'] for m in h['members']) and {s['slot'] for s in h['evidence_coverage']}=={'proof','independent_audit','example_or_counterexample','validation_code','final_manuscript'} for h in H.values()) for e in E.values() if e['core_claim']))
 check('missing_slots_not_filled_with_fake_assets',all((s['availability']=='MISSING')==(len(s['asset_ids'])==0) and all(a in A for a in s['asset_ids']) for h in H.values() for s in h['evidence_coverage']))
 check('evidence_assets_are_actual_hyperedge_members',all(all('doc__'+a in {m['entity_id'] for m in h['members']} for a in s['asset_ids']) for h in H.values() for s in h['evidence_coverage']))
 files={p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file()}
 check('every_package_file_mapped',files=={a['path'] for a in A.values()},{'missing_from_map':sorted(files-{a['path'] for a in A.values()}),'missing_on_disk':sorted({a['path'] for a in A.values()}-files)})
 check('all_assets_have_document_entity',all('doc__'+a in E and E['doc__'+a]['asset_id']==a for a in A))
 check('asset_hyperedge_mapping_references',all(all(h in H for h in a['mapped_hyperedges']) for a in A.values()))
 original=[a for a in A.values() if a['research_original']]
 sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
 check('v1_68_originals_byte_identical',len(original)==68 and all(sha(root/a['path'])==a['sha256_original'] for a in original))
 baseline=json.loads((nav/'历史manifest_v1.json').read_text());mapping=next(a for a in baseline['files'] if a['id']=='sources')
 check('chinese_mapping_byte_identical',sha(root/mapping['path'])==mapping['sha256'])
 badsources=[]
 for obj in [*E.values(),*H.values()]:
  for s in obj['sources']:
   p=root/s['path'];loc=s['locator'];aid=s['asset_id']
   if aid not in A or A[aid]['path']!=s['path'] or not p.exists():badsources.append((obj['id'],'bad source reference'));continue
   if loc['line_start']:
    t=p.read_text().splitlines();start=loc['line_start']-1;end=loc['line_end']
    if s['excerpt']!='\n'.join(t[start:end]):badsources.append((obj['id'],s['path'],start+1,'excerpt mismatch'))
    if loc['heading']!='文件级来源；未提供章节定位' and (start>=len(t) or loc['heading']!=t[start].strip()):badsources.append((obj['id'],s['path'],'heading mismatch'))
 check('all_source_headings_lines_excerpts_exact',not badsources,badsources)
 class Parser(HTMLParser):
  def __init__(self):super().__init__(convert_charrefs=False);self.script=None;self.scripts={};self.ids=[];self.refs=[];self.stack=[];self.nesting=[]
  def handle_starttag(self,tag,attrs):
   a=dict(attrs)
   if 'id'in a:self.ids.append(a['id'])
   if tag=='script':self.script=a.get('id');self.scripts[self.script]=''
   for key in ['href','src']:
    if a.get(key):self.refs.append((tag,a[key]))
   if tag not in ['meta','input','br','hr','link','img','source','area','base','col','embed','param','track','wbr']:self.stack.append(tag)
  def handle_endtag(self,tag):
   if tag=='script':self.script=None
   if not self.stack or self.stack[-1]!=tag:self.nesting.append((tag,self.stack[-3:]))
   else:self.stack.pop()
  def handle_data(self,t):
   if self.script is not None:self.scripts[self.script]+=t
 html=(nav/'研究资产统一超边知识图_v2.html').read_text();p=Parser();p.feed(html)
 check('HTML_parser_nesting_and_unique_ids',not p.nesting and not p.stack and len(p.ids)==len(set(p.ids)),{'nesting':p.nesting,'unclosed':p.stack})
 check('HTML_embedded_JSON_identical',json.loads(p.scripts['graph-data'])==data)
 payload=json.loads(p.scripts['asset-payloads']);check('68_embedded_originals_byte_identical',set(payload)=={a['id'] for a in original} and all(hashlib.sha256(base64.b64decode(payload[a['id']])).hexdigest()==a['sha256_original'] for a in original))
 check('no_CDN_or_remote_runtime_assets',not any(urlsplit(ref).scheme in ['http','https'] for tag,ref in p.refs) and not re.search(r'\b(?:fetch|XMLHttpRequest|WebSocket|importScripts)\s*\(',p.scripts['graph-app']))
 badlinks=[]
 for tag,ref in p.refs:
  if ref.startswith(('#','data:','blob:')):continue
  parts=urlsplit(ref)
  if not parts.scheme and not (nav/unquote(parts.path)).exists():badlinks.append(ref)
 # JS source links come exclusively from actual asset paths; validate all.
 for a in A.values():
  if not(nav/('..'+'/'+a['path'])).resolve().is_file():badlinks.append(a['path'])
 # Organizer README links only. Research originals can contain historical external-workspace links.
 for ref in re.findall(r'\]\(([^)]+)\)',(nav/'README_研究资产导航.md').read_text()):
  if not urlsplit(ref).scheme and not(nav/unquote(ref.split('#')[0])).exists():badlinks.append(ref)
 check('all_v2_relative_asset_and_README_links',not badlinks,badlinks)
 with tempfile.TemporaryDirectory(prefix='hypergraph_js_',dir=root.parent) as td:
  js=Path(td)/'app.js';js.write_text(p.scripts['graph-app']);r=subprocess.run(['node','--check',str(js)],capture_output=True,text=True)
 check('Node_JS_syntax',r.returncode==0,r.stderr.strip())
 rr=subprocess.run(['node',str(nav/'交互模拟测试_v2.cjs'),str(nav/'研究资产统一超边知识图_v2.html')],capture_output=True,text=True)
 try:event_result=json.loads(rr.stdout)
 except Exception:event_result={'output':rr.stdout,'stderr':rr.stderr}
 check('simulated_DOM_interaction_tests',rr.returncode==0,event_result)
 # Geometry QA is numerical only; not browser rendering.
 core=[e for e in E.values() if e['core']]+list(H.values());overlaps=[]
 for i,a in enumerate(core):
  for b in core[i+1:]:
   ah=36 if a['id']in H else 31;bh=36 if b['id']in H else 31
   if abs(a['x']-b['x'])<226 and abs(a['y']-b['y'])<ah+bh:overlaps.append((a['id'],b['id']))
 check('default_node_bounding_boxes_do_not_overlap',not overlaps,overlaps)
 # The semantic incidence graph should be a single connected component.
 adj=collections.defaultdict(set)
 for h in H.values():
  for m in h['members']:adj[h['id']].add(m['entity_id']);adj[m['entity_id']].add(h['id'])
 seen=set();todo=[next(iter(H))]
 while todo:
  n=todo.pop()
  if n in seen:continue
  seen.add(n);todo.extend(adj[n]-seen)
 check('all_hyperedges_in_one_connected_graph',set(H)<=seen)
 check('all_semantic_entities_connected',all(e['id'] in seen for e in E.values() if not e['document_leaf']))
 hashbad=[]
 for l in(nav/'SHA256文件校验清单.txt').read_text().splitlines():
  digest,path=l.split('  ',1)
  if not(root/path).exists() or sha(root/path)!=digest:hashbad.append(path)
 check('SHA256_list',not hashbad,hashbad)
 result={'status':'PASS' if not errors else 'FAIL','errors':errors,'checks':checks,'counts':{'core_entities':data['core_entity_count'],'semantic_entities':data['semantic_entity_count'],'all_entities':len(E),'hyperedges':len(H),'incidences':sum(len(h['members']) for h in H.values()),'assets':len(A),'cross_project_hyperedges':sum(h['cross_project'] for h in H.values()),'primary_relation_types':dict(collections.Counter(h['relation_type'] for h in H.values())),'member_relation_types':dict(collections.Counter(m['relation_type'] for h in H.values() for m in h['members']))},'visual_QA_limitations':'No Chromium/Firefox/WebKit executable was available. No browser screenshot, real font rendering or physical pointer QA was performed. HTML parser, JS execution with a synthetic DOM and numerical layout checks are not a browser.'}
 return result

if __name__=='__main__':
 if len(sys.argv)>1:root=Path(sys.argv[1])
 elif Path(__file__).parent.name=='00_从这里开始':root=Path(__file__).parent.parent
 else:root=Path(__file__).parent/'菠萝_RL与广义次正则研究资产_2026-09-14'
 result=run(root);print(json.dumps(result,ensure_ascii=False,indent=2));sys.exit(0 if result['status']=='PASS' else 1)
