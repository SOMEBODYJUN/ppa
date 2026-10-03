'use strict';
const fs=require('fs'),assert=require('node:assert/strict'),path=require('path');
const C=require('../src/universe.js');const graph=JSON.parse(fs.readFileSync(path.join(__dirname,'../../../research/graph.json')));const saved=require('../data/anchors.json');
const m=C.make(graph,{anchors:saved}),sim=C.simulation(m);sim.tick(350);let tests=0;function test(name,f){f();tests++;console.log('PASS '+name)}
test('exact graph and conjunctive endpoints are preserved',()=>{assert.deepEqual(m.graph,graph);assert.equal(m.nodes.length,graph.nodes.length);assert.equal(m.edges.length,graph.edges.length);assert.deepEqual(m.edges.find(e=>e.id==='E02').inputs,['D02','COV','D04']);assert.deepEqual(m.edges.find(e=>e.id==='E03').inputs,['R01','CMP','LOC']);});
test('D3 forces actually relax coincident nonorbital objects',()=>{let x=C.make(graph),a=x.byId.get('EX-ROT'),b=x.byId.get('EX-DIAG');a.x=b.x=1000;a.y=b.y=1000;a.ax=b.ax=1000;a.ay=b.ay=1000;let s=C.simulation(x);s.tick(300);assert.ok(Math.hypot(a.x-b.x,a.y-b.y)>a.r+b.r+10);});
test('eight core planets and six genuine graph-node satellites',()=>{assert.deepEqual(m.nodes.filter(n=>n.kind==='planet').map(n=>n.id),C.orbitIds);const ids=new Set(graph.nodes.map(n=>n.id));for(const n of m.nodes.filter(n=>n.orbit)){assert.ok(ids.has(n.id));assert.ok(ids.has(n.orbit.parent));}});
test('binary and Gaussian mathematical models stay separate',()=>{assert.equal(m.byId.get('M-COND').group,'binary');assert.equal(m.byId.get('G-COND').group,'gaussian');assert.notEqual(m.byId.get('COND-EB').group,m.byId.get('G-COND-EB').group);});
test('different orbital periods produce actual moving positions',()=>{C.updateOrbits(m,0);const p=m.byId.get('D01'),old={x:p.x,y:p.y};C.updateOrbits(m,4);assert.ok(Math.hypot(p.x-old.x,p.y-old.y)>30);assert.notEqual(p.orbit.period,m.byId.get('R01').orbit.period);});
test('zero time step is an exact orbital/route pause',()=>{C.updateOrbits(m,17);let before=m.nodes.map(n=>[n.id,n.x,n.y]);C.updateOrbits(m,17);assert.deepEqual(before,m.nodes.map(n=>[n.id,n.x,n.y]));});
test('600 sampled seconds without solar body intersections',()=>{for(let t=0;t<600;t+=.25){C.updateOrbits(m,t);const a=m.nodes.filter(n=>['planet','moon','sun'].includes(n.kind));for(let i=0;i<a.length;i++)for(let j=i+1;j<a.length;j++)assert.ok(Math.hypot(a[i].x-a[j].x,a[i].y-a[j].y)>=a[i].r+a[j].r,`${t}: ${a[i].id}/${a[j].id}`);}});
test('force collision separates nonorbital bodies in settled graph',()=>{const a=m.nodes.filter(n=>!n.orbit&&n.kind!=='sun');for(let i=0;i<a.length;i++)for(let j=i+1;j<a.length;j++)assert.ok(Math.hypot(a[i].x-a[j].x,a[i].y-a[j].y)>=a[i].r+a[j].r,`${a[i].id}/${a[j].id}`);});
test('growth/reorder preserve saved semantic anchors',()=>{const g=structuredClone(graph);for(let i=0;i<125;i++){g.nodes.push({id:'TEST-'+i,label:'TEST',file:'canonical/path_atlas.md'});g.edges.push({id:'TEST-E-'+i,inputs:['R01','CMP'],output:'TEST-'+i,relation:'test'});}g.nodes.reverse();g.edges.reverse();const grown=C.make(g,m);for(const n of graph.nodes)assert.deepEqual(grown.anchors[n.id],m.anchors[n.id]);const settled=C.simulation(grown);settled.tick(350);let max=0;for(const n of m.nodes.filter(n=>!n.orbit&&n.kind!=='sun')){const p=grown.byId.get(n.id);max=Math.max(max,Math.hypot(p.x-n.x,p.y-n.y));}assert.ok(max<150,`max existing node relaxation ${max}`);console.log('  existing render-position maximum local relaxation:',max.toFixed(2));});
test('deletion/restoration retain anchors and reject missing hyperedge endpoints',()=>{let g=structuredClone(graph);g.nodes=g.nodes.filter(n=>n.id!=='R01');assert.throws(()=>C.make(g,m));g=structuredClone(graph);g.nodes.pop();g.edges=g.edges.filter(e=>e.output!==graph.nodes.at(-1).id&&!e.inputs.includes(graph.nodes.at(-1).id));const removed=C.make(g,m),restored=C.make(graph,removed);assert.deepEqual(restored.anchors,m.anchors);});
test('one conjunction junction per edge with every input and true output',()=>{for(const e of m.edges){const j=C.junction(e,m);assert.ok(Number.isFinite(j.x)&&Number.isFinite(j.y));for(const id of e.inputs){const c=C.curve(m.byId.get(id),j);assert.deepEqual(C.at(c,0),{x:c.a.x,y:c.a.y});assert.deepEqual(C.at(c,1),j);}}});
test('complete systems drift while carrying their stars and retaining canonical anchors',()=>{const x=C.make(graph,{anchors:saved}),system=x.systems.find(s=>s.id==='structure'),star=x.nodes.find(n=>n.group===system.id),anchor=structuredClone(x.anchors[star.id]),from={x:system.x,y:system.y,starX:star.x,starY:star.y},drive=C.systemSimulation(x);for(let i=0;i<480;i++){x.time=i/60;C.advanceSystems(x,drive);}assert.ok(Math.hypot(system.x-from.x,system.y-from.y)>3);assert.ok(Math.abs((star.x-from.starX)-(system.x-from.x))<1e-7);assert.ok(Math.abs((star.y-from.starY)-(system.y-from.y))<1e-7);assert.deepEqual(x.anchors[star.id],anchor);});
test('system drag translates all members, orbital parents and endpoints together',()=>{const x=C.make(graph),s=x.systems.find(s=>s.id==='solar'),sun=x.byId.get('R02'),planet=x.byId.get('D02'),e=x.edges.find(e=>e.id==='E02'),j=C.junction(e,x),others=x.byId.get('M-COND'),before={x:sun.x,y:sun.y,px:planet.x,py:planet.y,ox:others.x,oy:others.y};C.moveSystem(x,'solar',s.x+170,s.y-80);C.updateOrbits(x,0);assert.equal(sun.x,before.x+170);assert.equal(sun.y,before.y-80);assert.equal(planet.x,before.px+170);assert.equal(planet.y,before.py-80);assert.equal(others.x,before.ox);assert.equal(others.y,before.oy);const jj=C.junction(e,x);assert.ok(Math.hypot(jj.x-j.x,jj.y-j.y)>20);});
test('invisible drag binding keeps every member on its galaxy through inner force ticks',()=>{for(const id of ['solar','structure','markov','gaussian']){const x=C.make(graph,{anchors:saved}),inner=C.simulation(x),outer=C.systemSimulation(x),s=x.systems.find(v=>v.id===id);inner.tick(20);C.updateOrbits(x,5);const members=x.nodes.filter(n=>n.group===id),offsets=new Map(members.map(n=>[n.id,[n.x-s.x,n.y-s.y]])),anchors=structuredClone(x.anchors);C.beginSystemDrag(x,id);for(const [dx,dy] of [[140,-75],[-210,90],[65,130]]){C.moveSystem(x,id,s.x+dx,s.y+dy);C.advanceSystems(x,outer,3);inner.alpha(.4).tick(15);C.updateOrbits(x,5);for(const n of members){const [ox,oy]=offsets.get(n.id);assert.ok(Math.abs(n.x-s.x-ox)<1e-7,`${id}/${n.id} x detached`);assert.ok(Math.abs(n.y-s.y-oy)<1e-7,`${id}/${n.id} y detached`);}}assert.deepEqual(x.anchors,anchors);C.endSystemDrag(x,id);assert.ok(!s.dragMembers);for(const n of members)if(n.kind!=='sun'&&!n.orbit){assert.equal(n.fx,null);assert.equal(n.fy,null);}if(id==='solar'){assert.equal(x.byId.get('R02').fx,s.x);assert.equal(x.byId.get('R02').fy,s.y);}}});
test('dragged centers stay at the pointer across complete running frames and pointer holds',()=>{
  for(const id of ['solar','structure','markov','gaussian']){
    const x=C.make(graph,{anchors:saved}),inner=C.simulation(x),outer=C.systemSimulation(x),s=x.systems.find(s=>s.id===id);
    inner.tick(220);C.updateOrbits(x,5);const from={x:s.x,y:s.y},members=x.nodes.filter(n=>n.group===id&&!n.orbit),offsets=members.map(n=>[n.x-s.x,n.y-s.y]);
    C.beginSystemDrag(x,id);
    for(const [dx,dy] of [[400,-200],[-230,340],[1000,-650]]){
      const target={x:from.x+dx,y:from.y+dy};C.moveSystem(x,id,target.x,target.y);
      for(let frame=0;frame<45;frame++){
        x.time=5+frame/60;C.advanceSystems(x,outer);inner.alpha(.25).tick();C.updateOrbits(x,x.time);
        assert.ok(Math.hypot(s.x-target.x,s.y-target.y)<1e-7,`${id}: center left pointer during held frame ${frame}`);
        members.forEach((n,i)=>assert.ok(Math.hypot(n.x-s.x-offsets[i][0],n.y-s.y-offsets[i][1])<1e-7,`${id}/${n.id}: member detached`));
      }
    }
    C.endSystemDrag(x,id);
  }
});
test('D3 axis forces read changed member anchors, homes and time after initialization',()=>{
  const x=C.make(graph,{anchors:saved}),inner=C.simulation(x),outer=C.systemSimulation(x),n=x.byId.get('H02'),s=x.systems.find(s=>s.id==='structure'),alpha=.5;
  n.ax+=800;n.ay-=400;n.vx=n.vy=0;
  inner.force('anchorX')(alpha);inner.force('anchorY')(alpha);
  assert.ok(Math.abs(n.vx-(n.ax-n.x)*.16*alpha)<1e-9);
  assert.ok(Math.abs(n.vy-(n.ay-n.y)*.16*alpha)<1e-9);
  s.homeX+=900;s.homeY-=500;x.time=35;s.vx=s.vy=0;
  outer.force('homeX')(alpha);outer.force('homeY')(alpha);
  assert.ok(Math.abs(s.vx-(s.homeX+65*Math.sin(x.time*.13+C.hash(s.id)*.001)-s.x)*.015*alpha)<1e-9);
  assert.ok(Math.abs(s.vy-(s.homeY+52*Math.cos(x.time*.11+C.hash(s.id)*.001)-s.y)*.015*alpha)<1e-9);
});
test('release keeps moving force targets at the new center through 240 running frames',()=>{
  for(const id of ['structure','markov','gaussian']){
    const x=C.make(graph,{anchors:saved}),inner=C.simulation(x),outer=C.systemSimulation(x),s=x.systems.find(s=>s.id===id);
    inner.tick(350);const start={x:s.x,y:s.y},members=x.nodes.filter(n=>n.group===id),offsets=members.map(n=>[n.x-s.x,n.y-s.y]),anchors=structuredClone(x.anchors);
    C.beginSystemDrag(x,id);C.moveSystem(x,id,8000,-6000);C.endSystemDrag(x,id);inner.alpha(.6);
    assert.equal(s.homeX,8000);assert.equal(s.homeY,-6000);
    for(let frame=0;frame<240;frame++){
      x.time=frame/60;C.advanceSystems(x,outer);inner.tick();C.updateOrbits(x,x.time);
      // True cross-system links may move the whole group after release.
      assert.ok(Math.hypot(s.x-8000,s.y+6000)<Math.hypot(s.x-start.x,s.y-start.y),`${id}: system returned to its old region`);
      members.forEach((n,i)=>assert.ok(Math.hypot(n.x-s.x-offsets[i][0],n.y-s.y-offsets[i][1])<2*n.r,`${id}/${n.id}: release moved member more than its diameter relative to the center`));
    }
    assert.deepEqual(x.anchors,anchors);
  }
});
test('a paused drag commits member and system anchors before force motion resumes',()=>{
  const x=C.make(graph,{anchors:saved}),inner=C.simulation(x),outer=C.systemSimulation(x),s=x.systems.find(s=>s.id==='gaussian');inner.tick(350);
  const local=x.nodes.filter(n=>n.group===s.id).map(n=>({n,x:n.x-s.x,y:n.y-s.y}));
  C.beginSystemDrag(x,s.id);C.moveSystem(x,s.id,s.x-1600,s.y-1300);C.updateOrbits(x,0);C.endSystemDrag(x,s.id);
  const drop={x:s.x,y:s.y};inner.alpha(.4);
  for(let frame=0;frame<150;frame++){C.advanceSystems(x,outer);inner.tick();C.updateOrbits(x,frame/60);}
  assert.ok(Math.hypot(s.x-drop.x,s.y-drop.y)<100);
  for(const {n,x:ox,y:oy} of local)assert.ok(Math.hypot(n.x-s.x-ox,n.y-s.y-oy)<10);
});
test('system collisions recover after overlapping drag',()=>{const x=C.make(graph),a=x.systems.find(s=>s.id==='markov'),b=x.systems.find(s=>s.id==='finite');C.moveSystem(x,a.id,b.x,b.y);a.homeX=a.x;a.homeY=a.y;const drive=C.systemSimulation(x);for(let i=0;i<150;i++)C.advanceSystems(x,drive);assert.ok(Math.hypot(a.x-b.x,a.y-b.y)>=(a.radius+b.radius)*.82+205);});
test('cross-system bridges are sourced only from complete real hyperedges',()=>{const x=C.make(graph),bridges=C.crossSystemEdges(x);assert.equal(bridges.length,30);for(const e of bridges){assert.ok(graph.edges.some(raw=>raw.id===e.id));assert.ok(new Set([...e.inputs,e.output].map(id=>x.byId.get(id).group)).size>1);}assert.equal(C.crossSystemEdges(x,'gaussian').length,0);assert.ok(C.crossSystemEdges(x,'markov').length>0);});
test('larger ships seek a clear part of the visible solar routes',()=>{const x=C.make(graph,{anchors:saved});C.simulation(x).tick(250);for(let sec=0;sec<=12;sec+=.5){C.updateOrbits(x,sec);for(const id of ['E02','E03']){const e=x.edges.find(e=>e.id===id),j=C.junction(e,x),out=x.byId.get(e.output),c=C.curve(j,out,1),phase=(sec*.08+C.hash(id)%100/100)%1,q=C.shipWaypoint(c,phase,x,30);assert.ok(x.nodes.every(n=>Math.hypot(q.x-n.x,q.y-n.y)>n.r+30),`${id} t=${sec} near ${x.nodes.find(n=>Math.hypot(q.x-n.x,q.y-n.y)<=n.r+30)?.id}`);}}});
test('offline HTML embeds authoritative graph and vendored D3',()=>{const html=fs.readFileSync(path.join(__dirname,'../index.html'),'utf8');const data=html.match(/id="graph-data" type="application\/json">([\s\S]*?)<\/script>/)[1];assert.deepEqual(JSON.parse(data),graph);assert.ok(html.includes('https://d3js.org v7.9.0'));assert.ok(!/<script[^>]+src="https?:/i.test(html));assert.ok(html.includes('prefers-reduced-motion'));assert.ok(html.includes("['refutes','limits'].includes"));});
console.log(`${tests} tests passed. Structural/numerical tests do not substitute for browser visual QA.`);
