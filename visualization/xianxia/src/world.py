"""Append-only world allocator. Identity, semantics, layout and art are separate."""
import hashlib, math
SEED='ppa-yunxiu-1'
# Editorial metaphors for exact IDs. Art only: never changes role/evidence.
ART_OVERRIDES={'SIZE':'ocean','STOCH-LIMIT':'broken_bridge','D01':'archive','D02':'gate','D03':'pavilion','R02':'pavilion','H02':'mountain','OB-AV-ANCHOR':'broken_bridge'}
REALMS=[
 dict(id='foundation',name='太初书院',subtitle='对象 · 参数 · 量词',x=720,y=650,rx=590,ry=505,color='#84a996',dark='#568c80'),
 dict(id='convergence',name='问道山径',subtitle='覆盖 · 兼容 · 留域',x=2010,y=650,rx=590,ry=505,color='#91b19a',dark='#648e7b'),
 dict(id='structure',name='玉虚洞天',subtitle='全局影子 · 纤维 · 值域',x=3300,y=650,rx=590,ry=505,color='#acbeb2',dark='#799b94'),
 dict(id='frontier',name='无涯云海',subtitle='母空间 · 量尺 · 开放目标',x=4590,y=650,rx=590,ry=505,color='#87aeb2',dark='#598993'),
 dict(id='composite',name='青蘅药谷',subtitle='锥 · 正则性 · 目标集合',x=720,y=1860,rx=590,ry=505,color='#a5b398',dark='#7a9274'),
 dict(id='paths',name='万木归途',subtitle='动力学 · 解选择 · 对齐',x=2010,y=1860,rx=590,ry=505,color='#86a78b',dark='#538476'),
 dict(id='examples',name='试剑群峰',subtitle='完整对象 · 锐模 · 反例',x=3300,y=1860,rx=590,ry=505,color='#b0b5a0',dark='#85998b'),
 dict(id='random',name='浮生水乡',subtitle='Markov · 运输 · 条件律',x=4590,y=1860,rx=590,ry=505,color='#86afa6',dark='#568e87')]
def stable(*parts):return int(hashlib.sha256('|'.join(map(str,(SEED,*parts))).encode()).hexdigest()[:12],16)
def region_for(n):
 f=n['file']; ident=n['id']
 if 'operator_space' in f or 'compact_t_observation' in f or ident in ['SIZE','NO-GO','CAT-GAP','LOCAL-LOSS']:return 'frontier'
 if any(x in f for x in ['parameter_dictionary','foundations','non_tied_cayley']):return 'foundation'
 if 'topics/examples' in f or 'example_atlas' in f:return 'examples'
 if any(x in f for x in ['random','moment_envelope']) or ident.startswith(('M-','G-COND','COND-EB','G-COND-EB','FAST-EB','POWER-EB')):return 'random'
 if 'composite' in f or ident.startswith('C-'):return 'composite'
 if any(x in f for x in ['path','solution_selection','nonisolated','moving_anchor']):return 'paths'
 if any(x in f for x in ['holder','range_','finite_sample','LITERATURE']) or ident.startswith(('H0','FSC-','LR-')):return 'structure'
 return 'convergence'
def appearance(n,graph,catalog):
 incoming=[e for e in graph['edges'] if e['output']==n['id']]
 # Art families are navigation roles, never proof certification.
 role='object';kind='mine';reason='neutral-default'
 if n['id'] in ['D01','D02','D03','D04','D05','COV','CMP','LOC'] or n['file'].startswith('foundations') or n['id'].startswith('PD-'):
  role='definition';kind='village';reason='editorial-definition-index'
 if any(e['relation']=='open' for e in incoming):role='open-target';kind='mountain';reason='incoming-open-relation'
 if any(e['relation']=='refutes' for e in incoming):role='refuted-target';kind='barrier';reason='incoming-refutes-relation'
 badge=n.get('evidence_status','unspecified')
 if badge=='candidate':role='candidate';kind='mountain';reason='explicit-node-status'
 variants=[o['id'] for o in catalog if o['family']==kind]
 obj=ART_OVERRIDES.get(n['id'],variants[stable('object',n['id'])%len(variants)])
 return dict(role=role,kind=kind,object=obj,evidence=badge,reason=reason)
def slots(realm):
 result=[]
 # Fixed lattice, 92 x 94 spacing and an empty title band. Never normalized by node count.
 for iy in range(-4,5):
  for ix in range(-5,6):
   dx=ix*94;dy=iy*91+25
   if (dx/(realm['rx']*.84))**2+(dy/(realm['ry']*.77))**2<=1:
    result.append((realm['x']+dx,realm['y']+dy))
 return result

def grow(graph,catalog,previous=None):
 import copy
 world=copy.deepcopy(previous) if previous else dict(version=1,seed=SEED,asset_version=1,realms=copy.deepcopy(REALMS),nodes={},edges={})
 current=set(n['id'] for n in graph['nodes'])
 # Tombstones reserve deleted locations so restoration also preserves geography.
 occupied={(p['x'],p['y']) for p in world['nodes'].values()}
 realmmap={r['id']:r for r in world['realms']}
 for n in sorted(graph['nodes'],key=lambda n:n['id']):
  if n['id'] in world['nodes']:
   # Refresh semantics independently of frozen physical geography.
   world['nodes'][n['id']].update(appearance(n,graph,catalog))
   continue
  region=region_for(n);candidates=[]
  associated=[r for r in world['realms'] if r.get('parent',r['id'])==region]
  for r in associated:candidates += [(x,y,r['id']) for x,y in slots(r) if (x,y) not in occupied]
  if not candidates:
   # Append an island on a reserved southern row. Existing realms stay fixed.
   satellite=sum(1 for r in world['realms'] if 'parent' in r)
   anchor=realmmap[region]
   r=dict(anchor,id=f'{region}-annex-{satellite+1}',parent=region,name=anchor['name']+' · 外山',x=720+(satellite%4)*1290,y=3070+(satellite//4)*1210)
   world['realms'].append(r);realmmap[r['id']]=r
   candidates=[(x,y,r['id']) for x,y in slots(r)]
  neighbors={e['output'] for e in graph['edges'] if n['id'] in e['inputs']}
  neighbors.update(x for e in graph['edges'] if e['output']==n['id'] for x in e['inputs'])
  nearby=[world['nodes'][i] for i in neighbors if i in world['nodes'] and world['nodes'][i]['region']==region]
  if nearby:
   cx=sum(p['x'] for p in nearby)/len(nearby);cy=sum(p['y'] for p in nearby)/len(nearby)
   x,y,realm=min(candidates,key=lambda p:(math.hypot(p[0]-cx,p[1]-cy),stable(n['id'],p)))
  else:x,y,realm=min(candidates,key=lambda p:stable(n['id'],p))
  occupied.add((x,y));world['nodes'][n['id']]={**appearance(n,graph,catalog), 'x':x,'y':y,'region':region,'realm':realm}
 for e in sorted(graph['edges'],key=lambda e:e['id']):
  if e['id'] in world['edges']:continue
  o=world['nodes'][e['output']];ins=[world['nodes'][i] for i in e['inputs']]
  cx=sum(p['x'] for p in ins)/len(ins);cy=sum(p['y'] for p in ins)/len(ins)
  angle=math.atan2(cy-o['y'],cx-o['x'])+(stable(e['id'])%11-5)*.09
  # Reserved annulus around output keeps conjunction hubs away from sprite cores.
  old=list(world['edges'].values())
  candidate=None
  for ring in range(8):
   radius=48+ring*15
   for turn in range(24):
    theta=angle+turn*math.pi/12
    p={'x':round(o['x']+math.cos(theta)*radius,2),'y':round(o['y']+math.sin(theta)*radius,2)}
    if all(math.hypot(p['x']-q['x'],p['y']-q['y'])>=18 for q in old) and all(math.hypot(p['x']-q['x'],p['y']-q['y'])>=37 for q in world['nodes'].values()):
     candidate=p;break
   if candidate:break
  # Dense layouts remain accessible through the complete edge directory.
  world['edges'][e['id']]=candidate or {'x':round(o['x']+math.cos(angle)*170,2),'y':round(o['y']+math.sin(angle)*170,2),'dense':True}
 world['bounds']={'w':max(r['x']+r['rx'] for r in world['realms'])+130,'h':max(r['y']+r['ry'] for r in world['realms'])+135}
 return world
