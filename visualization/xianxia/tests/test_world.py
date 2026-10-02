"""Growth and snapshot regression tests, no third-party dependencies."""
import copy,json,re,sys,unittest,xml.etree.ElementTree as ET
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];REPO=ROOT.parents[1]
sys.path.insert(0,str(ROOT/'src'))
from world import grow
GRAPH=json.loads((REPO/'research/graph.json').read_text());CAT=json.loads((ROOT/'data/objects.json').read_text())['objects'];WORLD=json.loads((ROOT/'data/world.json').read_text())
class WorldTest(unittest.TestCase):
 def test_snapshot_fidelity(self):
  text=(ROOT/'index.html').read_text()
  def get(ident):return json.loads(re.search(r'<script type="application/json" id="'+ident+r'">(.*?)</script>',text,re.S)[1])
  self.assertEqual(get('graph-data'),GRAPH);self.assertEqual(get('world-data'),WORLD)
  self.assertEqual(set(WORLD['nodes']),{n['id'] for n in GRAPH['nodes']})
  self.assertEqual(set(WORLD['edges']),{e['id'] for e in GRAPH['edges']})
 def test_repeat_and_reorder(self):
  again=grow(GRAPH,CAT,WORLD);self.assertEqual(again,WORLD)
  reverse={**GRAPH,'nodes':list(reversed(GRAPH['nodes'])),'edges':list(reversed(GRAPH['edges']))}
  self.assertEqual(grow(reverse,CAT,WORLD),WORLD)
  self.assertEqual(grow(reverse,CAT),grow(GRAPH,CAT))
 def test_growth_preserves_positions_and_objects(self):
  graph=copy.deepcopy(GRAPH)
  for i in range(125):graph['nodes'].append({'id':f'FUTURE-{i:04}','label':'test only','file':'topics/examples/future.md'})
  for i in range(125):graph['edges'].append({'id':f'FUTURE-E-{i:04}','inputs':[GRAPH['nodes'][0]['id']], 'output':f'FUTURE-{i:04}','relation':'conditional','scope':'test','status':'test','topic':'test'})
  enlarged=grow(graph,CAT,WORLD)
  for ident,p in WORLD['nodes'].items():self.assertEqual(p,enlarged['nodes'][ident])
  for ident,p in WORLD['edges'].items():self.assertEqual(p,enlarged['edges'][ident])
  self.assertGreater(len(enlarged['realms']),len(WORLD['realms']))
  positions=[(p['x'],p['y']) for p in enlarged['nodes'].values()];self.assertEqual(len(positions),len(set(positions)))
 def test_remove_restore_reserves_location(self):
  graph=copy.deepcopy(GRAPH);gone=graph['nodes'].pop();graph['edges']=[e for e in graph['edges'] if gone['id'] not in e['inputs'] and gone['id']!=e['output']]
  smaller=grow(graph,CAT,WORLD);self.assertEqual(smaller['nodes'][gone['id']],WORLD['nodes'][gone['id']])
  self.assertEqual(grow(GRAPH,CAT,smaller),WORLD)
 def test_semantics_refresh_without_teleport(self):
  graph=copy.deepcopy(GRAPH);node=next(n for n in graph['nodes'] if WORLD['nodes'][n['id']]['role']=='object');ident=node['id'];node['evidence_status']='candidate'
  changed=grow(graph,CAT,WORLD);new=changed['nodes'][ident];old=WORLD['nodes'][ident]
  self.assertEqual((new['x'],new['y'],new['realm']),(old['x'],old['y'],old['realm']))
  self.assertEqual(new['evidence'],'candidate');self.assertEqual(new['role'],'candidate')
  self.assertNotEqual(new['object'],old['object'])
 def test_new_refutation_refreshes_old_target(self):
  graph=copy.deepcopy(GRAPH);node=next(n for n in graph['nodes'] if WORLD['nodes'][n['id']]['role']=='object');ident=node['id'];other=next(n['id'] for n in graph['nodes'] if n['id']!=ident)
  graph['edges'].append({'id':'NEW-REFUTATION','inputs':[other],'output':ident,'relation':'refutes','scope':'test only','status':'test only','topic':'test'})
  changed=grow(graph,CAT,WORLD);new=changed['nodes'][ident];old=WORLD['nodes'][ident]
  self.assertEqual((new['x'],new['y'],new['realm']),(old['x'],old['y'],old['realm']))
  self.assertEqual(new['role'],'refuted-target');self.assertEqual(new['kind'],'barrier')
  self.assertEqual(new['evidence'],old['evidence'])
  # A refutation changes the relation role, not the graph's evidence field.
  self.assertIn('NEW-REFUTATION',changed['edges'])
 def test_art_registry(self):
  self.assertEqual(len(CAT),32);self.assertEqual(len({o['id'] for o in CAT}),32)
  for o in CAT:
   tree=ET.parse(ROOT/o['file']);self.assertEqual(tree.getroot().attrib['viewBox'],'0 0 144 144');self.assertEqual(o['anchor'],[72,122])
   self.assertEqual(o['family'],next(p['family'] for p in CAT if p['id']==o['id']))
  self.assertEqual(set(p['object'] for p in WORLD['nodes'].values())-set(o['id'] for o in CAT),set())
 def test_node_spacing_and_hubs(self):
  import math
  points=list(WORLD['nodes'].values());self.assertTrue(all(math.dist((p['x'],p['y']),(q['x'],q['y']))>=90 for i,p in enumerate(points) for q in points[i+1:]))
  hubs=list(WORLD['edges'].values());self.assertTrue(all(math.dist((p['x'],p['y']),(q['x'],q['y']))>=18 for i,p in enumerate(hubs) for q in hubs[i+1:]))
if __name__=='__main__':unittest.main()
