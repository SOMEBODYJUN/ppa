/* PPA research atlas — dependency-free, deterministic and usable from file://.
 * The graph is the mathematical authority. Geography is only a navigation aid.
 * Every rendered relation has a conjunction hub, even with a single input.
 */
(() => {
  'use strict';
  const graph = JSON.parse(document.getElementById('graph-data').textContent);
  const $ = id => document.getElementById(id);
  const escapeHTML = value => String(value).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const linkPath = path => encodeURI(path).replace(/"/g, '%22').replace(/'/g, '%27');
  const nodes = new Map(graph.nodes.map(n => [n.id, {...n, incoming:[], outgoing:[], regions:[]} ]));
  const edges = graph.edges.map(e => ({...e}));
  const edgeMap = new Map(edges.map(e => [e.id,e]));
  const regionDefs = [
    {id:'foundation',name:'基础原野',subtitle:'对象 · 参数 · 量词',mark:'⌂',x:470,y:410,rx:340,ry:285,color:'#aec088',dark:'#839b65',landmarks:['D02','PD-RESIDUAL']},
    {id:'convergence',name:'收敛谷地',subtitle:'覆盖 · 兼容 · 留域',mark:'⌁',x:1410,y:450,rx:495,ry:345,color:'#a8bb83',dark:'#7f9964',landmarks:['R02','NB-LOCAL']},
    {id:'structure',name:'结构雪岭',subtitle:'全局影子 · 纤维 · 值域',mark:'▲',x:2500,y:390,rx:510,ry:295,color:'#b9c4a1',dark:'#98ab83',landmarks:['H02','H03','LR-RANGE']},
    {id:'frontier',name:'开放之海',subtitle:'自然母空间 · 规模比较',mark:'≈',x:3180,y:1030,rx:295,ry:325,color:'#b8c099',dark:'#93a77d',landmarks:['SIZE','NO-GO']},
    {id:'composite',name:'复合丘陵',subtitle:'锥 · 正则性 · 目标集合',mark:'♧',x:470,y:1100,rx:330,ry:285,color:'#bec292',dark:'#97a76e',landmarks:['C-MSCQ','CS-OPEN-RANK']},
    {id:'paths',name:'路径林地',subtitle:'动力学 · 解选择 · 对齐',mark:'♧',x:640,y:1810,rx:490,ry:350,color:'#9db786',dark:'#729267',landmarks:['PA-WHOLE','SSQ-SELECT']},
    {id:'examples',name:'实例矿群',subtitle:'完整对象 · 锐模 · 反例',mark:'◒',x:1820,y:1550,rx:620,ry:565,color:'#b8bb83',dark:'#929965',landmarks:['EX-ROT','VO-PROX','OB-DYN-RL']},
    {id:'random',name:'随机群岛',subtitle:'Markov · 运输 · 条件律',mark:'≋',x:2880,y:1830,rx:475,ry:365,color:'#9dbba0',dark:'#759985',landmarks:['M-FIN','RP-EB']}
  ];
  const regionMap = new Map(regionDefs.map(r=>[r.id,r]));
  const relationNames = {conditional:'条件推导',equivalence:'等价关系',implies:'推出',limits:'适用边界',necessary:'必要方向',open:'开放目标',refutes:'反驳推论',sharpness:'锐性见证',sufficient:'充分方向'};
  const relationSigns = {equivalence:'⇔',limits:'⊣',refutes:'↛',open:'⇢'};
  const isBarrierEdge = e => e.relation==='limits'||e.relation==='refutes';
  for(const e of edges){nodes.get(e.output).incoming.push(e);for(const id of e.inputs)nodes.get(id).outgoing.push(e);}
  function regionFor(n){
    const file=n.file;
    if(file.includes('operator_space')||file.includes('compact_t_observation')||['SIZE','NO-GO','CAT-GAP','LOCAL-LOSS'].includes(n.id))return 'frontier';
    if(file.includes('parameter_dictionary')||file.includes('foundations')||file.includes('non_tied_cayley'))return 'foundation';
    if(file.includes('topics/examples')||file.includes('example_atlas'))return 'examples';
    if(file.includes('random')||file.includes('moment_envelope')||/^(M-|G-COND|COND-EB|G-COND-EB|FAST-EB|POWER-EB|OB-RES$)/.test(n.id))return 'random';
    if(file.includes('composite')||/^C-/.test(n.id))return 'composite';
    if(file.includes('path')||file.includes('solution_selection')||file.includes('nonisolated')||file.includes('moving_anchor'))return 'paths';
    if(file.includes('holder')||file.includes('range_')||file.includes('finite_sample')||file.includes('LITERATURE')||/^H0|^FSC-|^LR-/.test(n.id))return 'structure';
    if(file.includes('FAILED_ROUTES'))return n.id==='POLISH-GAP'?'random':'examples';
    return 'convergence';
  }
  const frontierIDs = new Set(['SIZE','CS-OPEN-RANK','Q-ADVANTAGE']);
  const kindLabels={village:'理论营地',mine:'已整理结果',mountain:'待探前沿',barrier:'障碍路标'};
  const kindMarks={village:'⌂',mine:'◒',mountain:'▲',barrier:'×'};
  for(const n of nodes.values()){
    n.region=regionFor(n);
    n.kind=n.incoming.some(e=>e.relation==='refutes')||/^OB-|^F03$|^NO-GO$|^CAT-GAP$|^LOCAL-LOSS$|^POLISH-GAP$/.test(n.id)||/（错误）|错误猜测|过强命题/.test(n.label)?'barrier':
      n.evidence_status==='candidate'||frontierIDs.has(n.id)||n.incoming.some(e=>e.relation==='open')?'mountain':
      !n.incoming.length||/-OBJECT$|^D\d|^PD-/.test(n.id)?'village':'mine';
    n.search=[n.id,n.label,n.file,n.evidence_status||''].join(' ').toLowerCase();
    n.topics=new Set([...n.incoming,...n.outgoing].map(e=>e.topic));
  }
  for(const e of edges)e.search=[e.id,e.topic,e.relation,e.scope,e.status,e.output,nodes.get(e.output).label,...e.inputs.flatMap(id=>[id,nodes.get(id).label])].join(' ').toLowerCase();
  for(const r of regionDefs){
    r.nodes=[...nodes.values()].filter(n=>n.region===r.id);
    // Stable sunflower packing keeps every mathematical node separate; geography
    // does not imply logical distance, chronology, priority or evidence strength.
    r.nodes.forEach((n,i)=>{
      const angle=i*2.399963229728653+.34;
      const radius=Math.sqrt((i+.65)/(r.nodes.length+1));
      n.x=r.x+Math.cos(angle)*r.rx*.79*radius;
      n.y=r.y+Math.sin(angle)*r.ry*.69*radius+24;
    });
  }
  for(const e of edges){
    const output=nodes.get(e.output), ins=e.inputs.map(id=>nodes.get(id));
    const cx=ins.reduce((s,n)=>s+n.x,0)/ins.length,cy=ins.reduce((s,n)=>s+n.y,0)/ins.length;
    const distance=Math.hypot(output.x-cx,output.y-cy)||1;
    const ratio=Math.min(.46,115/distance);
    const offset=(parseInt(e.id.replace(/\D/g,''),10)%5-2)*12;
    e.x=output.x+(cx-output.x)*ratio+(cy-output.y)/distance*offset;
    e.y=output.y+(cy-output.y)*ratio-(cx-output.x)/distance*offset;
    if(Math.hypot(e.x-output.x,e.y-output.y)<35){e.x=output.x-41;e.y=output.y-32+offset;}
  }

  const state={query:'',mode:'all',topic:'all',selected:null,hover:null,showRoutes:true,walkMode:false,walker:{x:390,y:440},activeRegion:null,visibleNodes:new Set(nodes.keys()),visibleEdges:new Set(edges.map(e=>e.id)),scale:.3,x:0,y:0,fitScale:.3,width:0,height:0};
  const canvas=$('world'),ctx=canvas.getContext('2d'),mini=$('minimap'),miniCtx=mini.getContext('2d');
  const WORLD={w:3650,h:2290};
  const terrain=document.createElement('canvas');terrain.width=WORLD.w;terrain.height=WORLD.h;
  const tc=terrain.getContext('2d');
  const hash=(x,y)=>{let n=(Math.imul(x+513,374761393)+Math.imul(y+991,668265263))|0;n=Math.imul(n^(n>>>13),1274126177);return ((n^(n>>>16))>>>0)/4294967295;};
  const tile=12;
  const sprites={
    village:['     rrr     ','    rrrrr    ','   rrrrrrr   ','  rRRRRRRRr  ',' rRRRRRRRRRr ','rrrrrrrrrrrrr','  wWWWWWw    ','  wWbbWWw    ','  wWbbWdw    ','  wwwwwdw    ','ggggggggggggg'],
    mine:['    ssss    ','  ssssssss  ',' sSSSSSSSSs ',' sSSddddSSs ','sSSddddddSSs','sSSddddddSSs','sSSddddddSSs','ssddddddddss','  t      t  ','gggggggggggg'],
    mountain:['      s      ','     sss     ','    sSSSs    ','   sSSwSSs   ','  sSSwwwSSs  ',' sSSwwwwwSSs ','sSSSSSSSSSSSs',' sSSSSSSSSSs ','  sSSSSSSSs  ','ggggggggggggg'],
    barrier:[' t       t ',' tt     tt ','  tt   tt  ','   ttxtt   ','    txt    ','   ttxtt   ','  tt   tt  ',' tt  p  tt ',' t   p   t ','     p     ','ggggggggggg'],
    tree:['    f    ','   fff   ','  fFFff  ',' fFFFFff ','  fFFFFf ',' fFFFFFFf','fFFFFFFFf','    p    ','    p    '],
    pine:['    f    ','   fFf   ','  fFFFf  ','   fFf   ','  fFFFf  ',' fFFFFFf ','  fFFFf  ',' fFFFFFf ','fFFFFFFFf','    p    '],
    boat:['    p    ','    pw   ','    pww  ','    pwww ','    pwwww',' tttpttt ','  ttttt  '],
    explorer:['   rrr   ','  rrrrr  ',' rrrrrrr ','   www   ','   wdw   ','  bRRRb  ','  bRRRb  ','  wRRRw  ','   ddd   ','   d d   ','  dd dd  ']
  };
  const palette={r:'#805d3d',R:'#b67643',w:'#ecdfb4',W:'#d9cd9f',b:'#637f70',d:'#34493e',g:'#607c514d',s:'#839481',S:'#a8b09a',t:'#986d45',p:'#705d40',x:'#bd8253',f:'#617f59',F:'#76996a'};
  function drawSprite(context,name,x,y,unit=4,custom={}){
    const matrix=sprites[name],colors={...palette,...custom};
    const left=Math.round(x-matrix[0].length*unit/2),top=Math.round(y-matrix.length*unit+8);
    matrix.forEach((row,iy)=>[...row].forEach((c,ix)=>{if(colors[c]){context.fillStyle=colors[c];context.fillRect(left+ix*unit,top+iy*unit,unit,unit);}}));
  }
  function createTerrain(){
    tc.fillStyle='#7da39d';tc.fillRect(0,0,WORLD.w,WORLD.h);
    for(let y=0;y<WORLD.h;y+=tile){for(let x=0;x<WORLD.w;x+=tile){
      let best=Infinity,region=null;
      for(const r of regionDefs){
        const dx=(x-r.x)/r.rx,dy=(y-r.y)/r.ry;
        const noise=.06*Math.sin(x*.027+y*.019)+.034*Math.cos(y*.051-x*.017)+.025*Math.sin(x*.083+y*.071);
        const value=dx*dx+dy*dy+noise;
        if(value<best){best=value;region=r;}
      }
      const h=hash(x/tile,y/tile);
      if(best<.91){tc.fillStyle=h<.13?region.dark:h>.91?'#c1ca93':region.color;tc.globalAlpha=h<.13?.33:1;tc.fillRect(x,y,tile,tile);tc.globalAlpha=1;}
      else if(best<1.02){tc.fillStyle=h>.55?'#d4ce9d':'#c6c595';tc.fillRect(x,y,tile,tile);}
      else if(best<1.105){tc.fillStyle='#a7bb9c';tc.fillRect(x,y,tile,tile);}
      else if(best<1.25){tc.fillStyle=h>.4?'#8cad9d':'#89aa9d';tc.fillRect(x,y,tile,tile);}
      else if(h<.065){tc.fillStyle='#8fb4ac';tc.fillRect(x,y,tile*2,3);tc.fillRect(x+tile*2,y-3,tile,3);}
      else if(h>.987){tc.fillStyle='#739b96';tc.fillRect(x,y,tile,tile);}
    }}
    // Footpaths are decorative; actual logical relations are a separate layer.
    tc.strokeStyle='#d3cf9b';tc.lineWidth=13;tc.setLineDash([]);
    for(const r of regionDefs){
      tc.beginPath();tc.moveTo(r.x-r.rx*.65,r.y+r.ry*.2);tc.lineTo(r.x-r.rx*.25,r.y+r.ry*.2);tc.lineTo(r.x-r.rx*.25,r.y-r.ry*.09);tc.lineTo(r.x+r.rx*.55,r.y-r.ry*.09);tc.stroke();
      for(let i=0;i<65;i++){
        const dx=(hash(i+101,Math.round(r.x))-0.5)*r.rx*1.75,dy=(hash(i+207,Math.round(r.y))-.5)*r.ry*1.72;
        if(dx*dx/r.rx**2+dy*dy/r.ry**2>.77)continue;
        const x=r.x+dx,y=r.y+dy;
        if(r.nodes.some(n=>Math.hypot(n.x-x,n.y-y)<58))continue;
        drawSprite(tc,r.id==='structure'?'pine':'tree',x,y,r.id==='paths'?5:4,r.id==='random'?{f:'#557c68',F:'#6e9477'}:{});
      }
    }
    // Decorative snow peaks and sea landmarks make the frontier legible at overview.
    [[2310,170,11],[2430,140,14],[2580,155,12],[2670,200,9]].forEach(([x,y,s])=>drawSprite(tc,'mountain',x,y,s,{s:'#889b91',S:'#aabbb0',w:'#e5e8d4'}));
    drawSprite(tc,'boat',2910,1030,8);
    drawSprite(tc,'boat',2270,2150,6);
    drawSprite(tc,'boat',910,950,5);
    // Compass rose, drawn as pixels rather than a network font or image asset.
    const cx=3450,cy=220;tc.fillStyle='#557f76';
    for(let i=0;i<7;i++){tc.fillRect(cx-i*4,cy-44+i*7,i*8+4,7);tc.fillRect(cx-i*4,cy+44-i*7,i*8+4,7);}
    tc.fillStyle='#aac2ae';tc.fillRect(cx-47,cy-3,96,6);tc.fillStyle='#466f65';tc.fillRect(cx-5,cy-5,10,10);
    tc.font='20px Georgia,serif';tc.textAlign='center';tc.fillText('N',cx,cy-60);
  }
  createTerrain();
  let drawQueued=false;
  function requestDraw(){if(!drawQueued){drawQueued=true;requestAnimationFrame(()=>{drawQueued=false;draw();});}}
  function toScreen(n){return {x:n.x*state.scale+state.x,y:n.y*state.scale+state.y};}
  function toWorld(x,y){return {x:(x-state.x)/state.scale,y:(y-state.y)/state.scale};}
  function selectedContext(){
    const ids=new Set(),edgeIDs=new Set();
    const item=state.selected||state.hover;
    if(item?.type==='node'){
      const n=nodes.get(item.id);ids.add(n.id);
      for(const e of [...n.incoming,...n.outgoing]){edgeIDs.add(e.id);for(const id of e.inputs)ids.add(id);ids.add(e.output);}
    }else if(item?.type==='edge'){
      const e=edgeMap.get(item.id);edgeIDs.add(e.id);e.inputs.forEach(id=>ids.add(id));ids.add(e.output);
    }
    return {ids,edgeIDs};
  }
  function routeColor(e){return isBarrierEdge(e)?'#9b673e':e.relation==='open'?'#477f83':'#7d7950';}
  function strokeLeg(from,to,color,alpha,width,dashed=false,arrow=false,blocked=false){
    const a=toScreen(from),b=toScreen(to);
    ctx.strokeStyle=color;ctx.fillStyle=color;ctx.globalAlpha=alpha;ctx.lineWidth=width;ctx.setLineDash(dashed?[5,5]:[]);
    const dx=b.x-a.x,dy=b.y-a.y,dist=Math.hypot(dx,dy)||1;
    const gap=arrow?Math.max(6,12*state.scale):0;
    const bx=b.x-dx/dist*gap,by=b.y-dy/dist*gap;
    ctx.beginPath();ctx.moveTo(a.x,a.y);ctx.lineTo(bx,by);ctx.stroke();ctx.setLineDash([]);
    if(arrow){const angle=Math.atan2(dy,dx),len=5;ctx.save();ctx.translate(bx,by);ctx.rotate(angle);ctx.beginPath();if(blocked){ctx.moveTo(0,-4);ctx.lineTo(0,4);ctx.stroke();}else{ctx.moveTo(0,0);ctx.lineTo(-len,-3);ctx.lineTo(-len,3);ctx.closePath();ctx.fill();}ctx.restore();}
    ctx.globalAlpha=1;
  }
  function drawEdge(e,active=false,dim=false){
    const filtered=state.visibleEdges.has(e.id),color=routeColor(e);
    const alpha=active?.92:dim?.08:filtered?.34:.055;
    const width=active?1.65:Math.max(.6,state.scale*1.8);
    const dashed=isBarrierEdge(e)||e.relation==='open';
    for(const id of e.inputs)strokeLeg(nodes.get(id),e,color,alpha,width,dashed,false);
    strokeLeg(e,nodes.get(e.output),color,alpha,width,dashed,true,isBarrierEdge(e));
    const p=toScreen(e),r=active?7:Math.max(2.5,6*state.scale);
    ctx.globalAlpha=active?1:dim?.12:filtered?.78:.1;ctx.fillStyle=active?'#f8eed0':isBarrierEdge(e)?'#e2c18c':'#e0dda8';ctx.strokeStyle=color;ctx.lineWidth=active?1.25:.6;
    ctx.beginPath();ctx.moveTo(p.x,p.y-r);ctx.lineTo(p.x+r,p.y);ctx.lineTo(p.x,p.y+r);ctx.lineTo(p.x-r,p.y);ctx.closePath();ctx.fill();ctx.stroke();
    if(active||state.scale>.65){ctx.font=`bold ${active?10:Math.min(12,10*state.scale)}px system-ui`;ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillStyle=color;ctx.fillText('∧',p.x,p.y+.5);}
    ctx.globalAlpha=1;
  }
  function textLabel(text,x,y,{size=11,background=true,color='#365444',selected=false}={}){
    ctx.font=`${selected?'600':'500'} ${size}px ${getComputedStyle(document.body).fontFamily}`;
    const width=ctx.measureText(text).width;
    if(background){ctx.fillStyle=selected?'#fff9e3':'#f3efdcdf';ctx.fillRect(x-width/2-5,y-size+1,width+10,size+7);}
    ctx.textAlign='center';ctx.textBaseline='alphabetic';ctx.fillStyle=color;ctx.fillText(text,x,y+1);
  }
  function draw(){
    if(!state.width)return;
    const dpr=Math.min(window.devicePixelRatio||1,2);ctx.setTransform(dpr,0,0,dpr,0,0);ctx.clearRect(0,0,state.width,state.height);ctx.imageSmoothingEnabled=false;
    ctx.fillStyle='#7da39d';ctx.fillRect(0,0,state.width,state.height);
    ctx.drawImage(terrain,state.x,state.y,WORLD.w*state.scale,WORLD.h*state.scale);
    const {ids,edgeIDs}=selectedContext(),hasContext=edgeIDs.size>0;
    if(state.showRoutes){for(const e of edges)if(!edgeIDs.has(e.id))drawEdge(e,false,hasContext);for(const e of edges)if(edgeIDs.has(e.id))drawEdge(e,true);}
    // Region titles use screen-sized type so the overview stays readable.
    for(const r of regionDefs){
      const p=toScreen({x:r.x,y:r.y-r.ry*.82});
      if(p.x<-150||p.x>state.width+150||p.y<-50||p.y>state.height+30)continue;
      const active=!state.activeRegion||state.activeRegion===r.id;
      ctx.globalAlpha=active?1:.4;
      textLabel(r.name,p.x,p.y,{size:state.scale<.23?11:14,background:false,color:'#355a48'});
      if(state.scale>.22){ctx.font='8px '+getComputedStyle(document.body).fontFamily;ctx.fillStyle='#5c7c58';ctx.textAlign='center';ctx.fillText(r.subtitle,p.x,p.y+16);}
      ctx.globalAlpha=1;
    }
    const sorted=[...nodes.values()].sort((a,b)=>a.y-b.y);
    for(const n of sorted){
      const p=toScreen(n);if(p.x<-60||p.x>state.width+60||p.y<-80||p.y>state.height+80)continue;
      const relevant=state.visibleNodes.has(n.id),active=ids.has(n.id),selected=state.selected?.type==='node'&&state.selected.id===n.id;
      ctx.globalAlpha=!relevant?.16:hasContext&&!active?.36:1;
      if(selected||state.hover?.id===n.id){ctx.strokeStyle='#f9eed0';ctx.lineWidth=2;ctx.setLineDash([4,3]);ctx.beginPath();ctx.ellipse(p.x,p.y+2,Math.max(14,state.scale*30),Math.max(7,state.scale*13),0,0,Math.PI*2);ctx.stroke();ctx.setLineDash([]);}
      const spriteScale=Math.max(.31,state.scale);
      ctx.save();ctx.translate(p.x,p.y);ctx.scale(spriteScale,spriteScale);drawSprite(ctx,n.kind,0,0,n.kind==='village'?4:4,n.kind==='mountain'?{w:'#e6e7ce',s:'#809887',S:'#a1b3a0'}:{});ctx.restore();ctx.globalAlpha=1;
    }
    const labels=[...nodes.values()].filter(n=>state.visibleNodes.has(n.id)&&(ids.has(n.id)||state.scale>1.18||(state.scale>.5&&n.kind==='mountain')||(!hasContext&&regionMap.get(n.region).landmarks.includes(n.id))));
    for(const n of labels){
      const p=toScreen(n);if(p.x<15||p.x>state.width-15||p.y<40||p.y>state.height-12)continue;
      const active=ids.has(n.id),sel=state.selected?.id===n.id;
      const short=n.label.length>14?n.label.slice(0,13)+'…':n.label;
      const label=state.scale>1.18?`${n.id} · ${short}`:active?n.id:short;
      textLabel(label,p.x,p.y+19,{size:active?10:9,selected:sel,color:n.kind==='barrier'?'#935f35':'#426044'});
    }
    if(state.walkMode){
      const p=toScreen(state.walker);ctx.fillStyle='#36584044';ctx.beginPath();ctx.ellipse(p.x,p.y+3,10,4,0,0,Math.PI*2);ctx.fill();
      drawSprite(ctx,'explorer',p.x,p.y,2,{r:'#c49d50',R:'#b97340',w:'#f1d2a0',d:'#3f5144',b:'#476c60'});
      textLabel('探索者',p.x,p.y+20,{size:9,color:'#66704c'});
    }
    drawMinimap();$('zoom-level').textContent=Math.round(state.scale/state.fitScale*100)+'%';
  }
  function drawMinimap(){
    const w=mini.width,h=mini.height;miniCtx.clearRect(0,0,w,h);miniCtx.imageSmoothingEnabled=false;miniCtx.drawImage(terrain,0,0,w,h);
    for(const n of nodes.values()){if(!state.visibleNodes.has(n.id))continue;miniCtx.fillStyle=n.kind==='mountain'?'#eff1d0':n.kind==='barrier'?'#996347':'#466f52';miniCtx.fillRect(n.x/WORLD.w*w-1,n.y/WORLD.h*h-1,2,2);}
    const x=-state.x/state.scale/WORLD.w*w,y=-state.y/state.scale/WORLD.h*h,rw=state.width/state.scale/WORLD.w*w,rh=state.height/state.scale/WORLD.h*h;
    miniCtx.strokeStyle='#fff8d6';miniCtx.lineWidth=2;miniCtx.strokeRect(x,y,rw,rh);miniCtx.strokeStyle='#4b6e4c';miniCtx.lineWidth=.7;miniCtx.strokeRect(x+1,y+1,rw-2,rh-2);
  }
  function resize(){
    const box=canvas.getBoundingClientRect(),oldWidth=state.width,oldHeight=state.height;
    const previousCenter=oldWidth?toWorld(oldWidth/2,oldHeight/2):null;
    state.width=box.width;state.height=box.height;const dpr=Math.min(window.devicePixelRatio||1,2);canvas.width=Math.round(box.width*dpr);canvas.height=Math.round(box.height*dpr);
    state.fitScale=Math.min((state.width-35)/WORLD.w,(state.height-120)/WORLD.h);
    if(!previousCenter){fitMap();}else{state.x=state.width/2-previousCenter.x*state.scale;state.y=state.height/2-previousCenter.y*state.scale;requestDraw();}
  }
  function clampCamera(){
    state.x=Math.max(-WORLD.w*state.scale+state.width*.15,Math.min(state.width*.85,state.x));
    state.y=Math.max(-WORLD.h*state.scale+state.height*.15,Math.min(state.height*.85,state.y));
  }
  function fitMap(){state.scale=state.fitScale;state.x=(state.width-WORLD.w*state.scale)/2;state.y=(state.height-WORLD.h*state.scale)/2+3;state.activeRegion=null;$('view-label').textContent='全图鸟瞰';$('view-subtitle').textContent='从任意一处地标开始探索';requestDraw();}
  function zoom(factor,x=state.width/2,y=state.height/2){const before=toWorld(x,y);state.scale=Math.max(state.fitScale*.65,Math.min(3.3,state.scale*factor));state.x=x-before.x*state.scale;state.y=y-before.y*state.scale;clampCamera();requestDraw();}
  function focusRegion(id){const r=regionMap.get(id);state.activeRegion=id;state.scale=Math.min((state.width-70)/(r.rx*2),(state.height-145)/(r.ry*2),1.15);state.x=state.width/2-r.x*state.scale;state.y=state.height/2-r.y*state.scale+15;$('view-label').textContent=r.name;$('view-subtitle').textContent=`${r.nodes.length} 个节点 · ${r.subtitle}`;requestDraw();}
  function focusItem(item){
    const n=item.type==='node'?nodes.get(item.id):edgeMap.get(item.id);if(!n)return;
    const detailWidth=state.width>600?395:0,availableWidth=state.width-detailWidth;
    let cx=n.x,cy=n.y;
    if(item.type==='edge'){
      // Frame all conjuncts and the output, including inputs on other islands.
      const points=[...n.inputs,n.output].map(id=>nodes.get(id));points.push(n);
      const xs=points.map(p=>p.x),ys=points.map(p=>p.y),minX=Math.min(...xs)-70,maxX=Math.max(...xs)+70,minY=Math.min(...ys)-85,maxY=Math.max(...ys)+60;
      cx=(minX+maxX)/2;cy=(minY+maxY)/2;
      state.scale=Math.max(.035,Math.min(1.35,(availableWidth-40)/(maxX-minX),(state.height-140)/(maxY-minY)));
    }else state.scale=Math.max(state.scale,Math.min(1.12,state.fitScale*3));
    state.x=availableWidth/2-cx*state.scale;state.y=state.height/2-cy*state.scale;clampCamera();requestDraw();
  }

  function updateFilters(){
    state.query=$('query').value.trim().toLowerCase();state.topic=$('topic-filter').value;
    const terms=state.query.split(/\s+/).filter(Boolean),matches=text=>terms.every(t=>text.includes(t));
    const acceptedEdges=edges.filter(e=>(state.topic==='all'||e.topic===state.topic)&&matches(e.search)&&(state.mode==='all'||state.mode==='barrier'&&isBarrierEdge(e)||state.mode==='frontier'&&(e.relation==='open'||nodes.get(e.output).kind==='mountain')));
    const acceptedNodes=[...nodes.values()].filter(n=>(state.topic==='all'||n.topics.has(state.topic))&&matches(n.search)&&(state.mode==='all'||n.kind===(state.mode==='frontier'?'mountain':'barrier')));
    state.visibleEdges=new Set(acceptedEdges.map(e=>e.id));state.visibleNodes=new Set(acceptedNodes.map(n=>n.id));
    // A visible relation always brings every conjunct and its output into view.
    for(const e of acceptedEdges){e.inputs.forEach(id=>state.visibleNodes.add(id));state.visibleNodes.add(e.output);}
    $('result-count').textContent=`${acceptedNodes.length} 节点 · ${acceptedEdges.length} 超边`;
    renderDirectory(acceptedNodes,acceptedEdges);requestDraw();
  }
  function nodeButton(n){return `<button class="result-item${state.selected?.id===n.id?' selected':''}" data-node="${escapeHTML(n.id)}"><span class="item-icon" aria-hidden="true">${kindMarks[n.kind]}</span><span class="item-copy"><strong>${escapeHTML(n.label)}</strong><small>${escapeHTML(n.id)} · ${escapeHTML(regionMap.get(n.region).name)}${n.evidence_status?' · '+escapeHTML(n.evidence_status):''}</small></span></button>`;}
  function edgeButton(e){return `<button class="result-item" data-edge="${escapeHTML(e.id)}"><span class="item-icon" aria-hidden="true">∧</span><span class="item-copy"><strong>${escapeHTML(nodes.get(e.output).label)}</strong><small>${escapeHTML(e.id)} · ${escapeHTML(relationNames[e.relation])} · ${e.inputs.length} 个合取前提</small></span></button>`;}
  function renderDirectory(ns,es){
    const all=!state.query&&state.mode==='all'&&state.topic==='all';
    let content=all?regionDefs.map(r=>`<button class="region-card" data-region="${r.id}"><span class="region-icon" aria-hidden="true">${r.mark}</span><span class="region-copy"><strong>${r.name}</strong><small>${r.subtitle}</small></span><span class="region-count">${r.nodes.length}</span><span class="arrow" aria-hidden="true">›</span></button>`).join(''):'';
    if(!ns.length&&!es.length)content='<div class="empty-state">这里还没有匹配的地标。<br>试试节点编号、条件或证据关键词。</div>';
    if(ns.length)content+=`<div class="directory-label">数学节点 <span>${ns.length}</span></div>`+ns.map(nodeButton).join('');
    if(es.length)content+=`<div class="directory-label">完整合取超边 <span>${es.length}</span></div>`+es.map(edgeButton).join('');
    $('directory').innerHTML=content;
  }
  function rawDetails(value){return `<details class="raw-details"><summary>查看原始结构数据</summary><pre>${escapeHTML(JSON.stringify(value,null,2))}</pre></details>`;}
  function relationCard(e){return `<button class="relation-link" data-edge="${escapeHTML(e.id)}"><span class="relation-meta"><span>${escapeHTML(e.id)} · ${escapeHTML(e.relation)}</span><span>${e.inputs.length} 个前提 ${relationSigns[e.relation]||'→'}</span></span><strong>${escapeHTML(nodes.get(e.output).label)}</strong><small>${escapeHTML(e.status)}</small></button>`;}
  function renderNode(n){
    const original=graph.nodes.find(x=>x.id===n.id),r=regionMap.get(n.region);
    const explicit=n.evidence_status;
    return `<div class="detail-kicker"><span>${escapeHTML(n.id)} / ${escapeHTML(r.name)}</span><span class="type-tag${n.kind==='mountain'||n.kind==='barrier'?' warn':''}">${kindLabels[n.kind]}</span></div><h2>${escapeHTML(n.label)}</h2><p class="node-summary">这个地标关联 ${n.incoming.length} 条以它为输出的超边、${n.outgoing.length} 条以它为前提的超边。图标表示导航角色，结论须在各条关系的适用范围内使用。</p><div class="detail-actions"><a href="${escapeHTML(linkPath(n.file))}">打开规范正文 ↗</a><button data-center="node:${escapeHTML(n.id)}">定位地图</button></div><section class="detail-section"><h3>节点证据状态</h3><div class="evidence-status${explicit==='candidate'?' warn':''}"><p>${explicit?escapeHTML(explicit):'graph.json 未单列此节点的证据状态。'}</p><small>${explicit?'保留数据原文；仅适用于正文注明的对象与条件。':'须核对下列每条超边的原始 status 与正文；不由节点图标推定已证。'}</small></div></section>${n.incoming.length?`<section class="detail-section"><h3>到达这里的关系 <span>${n.incoming.length}</span></h3>${n.incoming.map(relationCard).join('')}</section>`:''}${n.outgoing.length?`<section class="detail-section"><h3>以此为前提的关系 <span>${n.outgoing.length}</span></h3>${n.outgoing.map(relationCard).join('')}</section>`:''}<section class="detail-section"><h3>核验入口</h3><div class="source-links"><a href="../CLAIMS.md">命题总账：精确身份与证据 ↗</a><a href="../FAILED_ROUTES.md">失败路线与重启条件 ↗</a><a href="SOURCES.md">来源谱系与原始证据 ↗</a></div></section>${rawDetails(original)}`;
  }
  function renderEdge(e){
    const warning=e.relation==='open'?'这是开放目标，当前超边不提供已成立的蕴含。':e.relation==='refutes'?'这是对推论的反驳路线。图上的连接不把被反驳的输出当作已证结论。':e.relation==='limits'?'这是适用边界或限制；须阅读 scope，不将连线理解成无条件蕴含。':e.relation==='necessary'?'这里只记录必要方向，不自动提供充分方向。':e.relation==='sufficient'?'这里只记录充分方向，不自动提供必要方向。':e.relation==='sharpness'?'这里只提供声明范围内的锐性或下界见证。':'';
    const output=nodes.get(e.output);
    const sources=[...new Map([...e.inputs,e.output].map(id=>{const n=nodes.get(id);return [n.file,n];})).values()];
    return `<div class="detail-kicker"><span>${escapeHTML(e.id)} / ${escapeHTML(e.topic)}</span><span class="type-tag${isBarrierEdge(e)||e.relation==='open'?' warn':''}">${escapeHTML(e.relation)}</span></div><h2>${escapeHTML(relationNames[e.relation])}<br><span style="font-size:15px;font-weight:500">${escapeHTML(output.label)}</span></h2>${warning?`<div class="relation-warning">${warning}</div>`:''}<div class="detail-actions"><a href="${escapeHTML(linkPath(output.file))}">打开输出正文 ↗</a><button data-center="edge:${escapeHTML(e.id)}">定位整条超边</button></div><section class="detail-section"><h3>全部合取前提 · INPUTS <span>${e.inputs.length}</span></h3><ol class="input-list">${e.inputs.map(id=>{const n=nodes.get(id);return `<li><button data-node="${escapeHTML(id)}"><span>${escapeHTML(id)}</span>${escapeHTML(n.label)}</button></li>`;}).join('')}</ol><div class="conjunction-note">∧ 全部输入共同成立 · ${escapeHTML(relationNames[e.relation])} ${relationSigns[e.relation]||'→'}</div><button class="output-node" data-node="${escapeHTML(output.id)}"><span>OUTPUT · ${escapeHTML(output.id)}</span>${escapeHTML(output.label)}</button></section><section class="detail-section"><h3>严格适用范围 · SCOPE 原文</h3><div class="scope-text">${escapeHTML(e.scope)}</div></section><section class="detail-section"><h3>证据与审查状态 · STATUS 原文</h3><div class="evidence-status${/候选|开放|source-report|candidate/.test(e.status)?' warn':''}"><p>${escapeHTML(e.status)}</p><small>自由文本状态原样展示，不由关键词生成统一证明等级。</small></div></section><section class="detail-section"><h3>定义、证明与来源入口</h3><div class="source-links">${sources.map(n=>`<a href="${escapeHTML(linkPath(n.file))}">${escapeHTML(n.id)} · ${escapeHTML(n.label)} ↗</a>`).join('')}<a href="SOURCES.md">来源索引与历史证据 ↗</a><a href="../CLAIMS.md">Claim 精确身份与版本 ↗</a></div></section>${rawDetails(graph.edges.find(x=>x.id===e.id))}`;
  }
  let lastOpener=null;
  function selectItem(type,id,{center=false,hash=true}={}){
    const item=type==='node'?nodes.get(id):edgeMap.get(id);if(!item)return;
    if($('detail').hidden)lastOpener=document.activeElement;
    state.selected={type,id};state.hover=null;$('tooltip').hidden=true;$('detail').hidden=false;
    if(type==='edge'){state.showRoutes=true;$('toggle-routes').setAttribute('aria-pressed','true');}
    $('detail-content').innerHTML=type==='node'?renderNode(item):renderEdge(item);$('detail-content').scrollTop=0;
    if(hash){const next=`#${type}=${encodeURIComponent(id)}`;try{history.replaceState(null,'',next);}catch{location.hash=next;}}
    $('view-label').textContent=type==='node'?`${id} · 地标详情`:`${id} · 合取超边`;
    $('view-subtitle').textContent=type==='node'?item.label:relationNames[item.relation];
    if(center)focusItem({type,id});$('close-detail').focus({preventScroll:true});requestDraw();
  }
  function closeDetail({restoreFocus=true}={}){state.selected=null;$('detail').hidden=true;if(location.hash.startsWith('#node=')||location.hash.startsWith('#edge=')){try{history.replaceState(null,'',location.pathname+location.search);}catch{location.hash='';}}if(restoreFocus&&lastOpener?.isConnected)lastOpener.focus({preventScroll:true});$('view-label').textContent=state.activeRegion?regionMap.get(state.activeRegion).name:'全图鸟瞰';$('view-subtitle').textContent='从任意一处地标开始探索';requestDraw();}
  function readHash(){const match=location.hash.match(/^#(node|edge)=(.+)$/);if(match){try{selectItem(match[1],decodeURIComponent(match[2]),{center:true,hash:false});}catch{/* malformed external fragment */}}}

  function hitTest(x,y){
    let best=null,bestDistance=Infinity;
    for(const n of nodes.values()){if(!state.visibleNodes.has(n.id))continue;const p=toScreen(n);const d=Math.hypot(x-p.x,y-(p.y-Math.max(6,state.scale*15)));if(d<Math.max(12,state.scale*26)&&d<bestDistance){best={type:'node',id:n.id};bestDistance=d;}}
    if(best)return best;
    if(state.showRoutes)for(const e of edges){if(!state.visibleEdges.has(e.id))continue;const p=toScreen(e);const d=Math.hypot(x-p.x,y-p.y);if(d<Math.max(7,8*state.scale)&&d<bestDistance){best={type:'edge',id:e.id};bestDistance=d;}}
    return best;
  }
  function showTooltip(item,x,y){
    const tip=$('tooltip');if(!item){tip.hidden=true;return;}
    if(item.type==='node'){
      const n=nodes.get(item.id),status=n.evidence_status||'节点未单列证据状态，详见关联超边';
      const related=n.kind==='barrier'?n.incoming.find(e=>e.relation==='refutes')||n.incoming[0]||n.outgoing[0]:n.incoming[0]||n.outgoing[0];
      const summary=related?`<p class="tooltip-summary"><span>关联路线 ${escapeHTML(related.id)} · ${escapeHTML(related.relation)} 摘要</span>${escapeHTML(related.scope.slice(0,105))}${related.scope.length>105?'…':''}<small>这是关联路线的摘要，非节点的独立结论。</small></p>`:'';
      tip.innerHTML=`<span class="tooltip-id">${escapeHTML(n.id)} · ${kindLabels[n.kind]}</span><strong>${escapeHTML(n.label)}</strong>${summary}<p>${escapeHTML(status)}</p><div class="tooltip-footer">${n.incoming.length+n.outgoing.length} 条关联超边 · 点击查看严格条件</div>`;
    }
    else{const e=edgeMap.get(item.id);tip.innerHTML=`<span class="tooltip-id">${escapeHTML(e.id)} · ${escapeHTML(e.relation)}</span><strong>${e.inputs.length} 个合取前提 ${relationSigns[e.relation]||'→'} ${escapeHTML(e.output)}</strong><p>${escapeHTML(e.scope.slice(0,110))}${e.scope.length>110?'…':''}</p><div class="tooltip-footer">${escapeHTML(e.status)} · 点击展开全部</div>`;}
    tip.hidden=false;tip.style.left=Math.max(8,Math.min(state.width-tip.offsetWidth-10,x+17))+'px';tip.style.top=Math.max(8,Math.min(state.height-tip.offsetHeight-10,y+15))+'px';
  }
  const pointers=new Map();let drag=null,pinch=null;
  canvas.addEventListener('pointerdown',event=>{
    if(event.button!==0)return;
    const rect=canvas.getBoundingClientRect(),p={x:event.clientX-rect.left,y:event.clientY-rect.top};pointers.set(event.pointerId,p);canvas.setPointerCapture(event.pointerId);$('tooltip').hidden=true;
    if(pointers.size===1)drag={x:p.x,y:p.y,cx:state.x,cy:state.y,moved:false};
    if(pointers.size===2){const [a,b]=[...pointers.values()];pinch={distance:Math.hypot(a.x-b.x,a.y-b.y),center:{x:(a.x+b.x)/2,y:(a.y+b.y)/2}};if(drag)drag.moved=true;}
  });
  canvas.addEventListener('pointermove',event=>{
    const rect=canvas.getBoundingClientRect(),p={x:event.clientX-rect.left,y:event.clientY-rect.top};
    if(pointers.has(event.pointerId)){
      pointers.set(event.pointerId,p);
      if(pointers.size===2){const [a,b]=[...pointers.values()],distance=Math.hypot(a.x-b.x,a.y-b.y),center={x:(a.x+b.x)/2,y:(a.y+b.y)/2};if(pinch){zoom(distance/Math.max(pinch.distance,1),pinch.center.x,pinch.center.y);state.x+=center.x-pinch.center.x;state.y+=center.y-pinch.center.y;}pinch={distance,center};requestDraw();return;}
      if(drag){const dx=p.x-drag.x,dy=p.y-drag.y;if(Math.hypot(dx,dy)>4)drag.moved=true;if(drag.moved){state.x=drag.cx+dx;state.y=drag.cy+dy;clampCamera();canvas.classList.add('dragging');requestDraw();}}return;
    }
    const item=hitTest(p.x,p.y);if(state.hover?.id!==item?.id||state.hover?.type!==item?.type){state.hover=item;requestDraw();}canvas.style.cursor=item?'pointer':'grab';showTooltip(item,p.x,p.y);
  });
  function pointerEnd(event,cancel=false){
    const p=pointers.get(event.pointerId);if(!p)return;const wasPinch=!!pinch;
    pointers.delete(event.pointerId);
    if(!cancel&&!wasPinch&&drag&&!drag.moved){const item=hitTest(p.x,p.y);if(item)selectItem(item.type,item.id);}
    if(pointers.size===0){drag=null;pinch=null;canvas.classList.remove('dragging');}
    else{const remain=[...pointers.values()][0];drag={x:remain.x,y:remain.y,cx:state.x,cy:state.y,moved:true};pinch=null;}
  }
  canvas.addEventListener('pointerup',e=>pointerEnd(e));canvas.addEventListener('pointercancel',e=>pointerEnd(e,true));
  canvas.addEventListener('pointerleave',()=>{if(!pointers.size){state.hover=null;$('tooltip').hidden=true;requestDraw();}});
  canvas.addEventListener('wheel',event=>{event.preventDefault();const rect=canvas.getBoundingClientRect();zoom(Math.exp(-Math.max(-150,Math.min(150,event.deltaY))*.0017),event.clientX-rect.left,event.clientY-rect.top);$('tooltip').hidden=true;},{passive:false});
  canvas.addEventListener('dblclick',event=>{const rect=canvas.getBoundingClientRect();zoom(1.7,event.clientX-rect.left,event.clientY-rect.top);});
  canvas.addEventListener('keydown',event=>{
    const motions={ArrowLeft:[65,0],ArrowRight:[-65,0],ArrowUp:[0,65],ArrowDown:[0,-65]};
    if(motions[event.key]){event.preventDefault();state.x+=motions[event.key][0];state.y+=motions[event.key][1];clampCamera();requestDraw();}
  });
  mini.addEventListener('click',event=>{const rect=mini.getBoundingClientRect();const x=(event.clientX-rect.left)/rect.width*WORLD.w,y=(event.clientY-rect.top)/rect.height*WORLD.h;state.x=state.width/2-x*state.scale;state.y=state.height/2-y*state.scale;clampCamera();requestDraw();});
  mini.addEventListener('keydown',event=>{if(event.key==='Enter'||event.key===' '){event.preventDefault();fitMap();}});
  $('query').addEventListener('input',updateFilters);$('topic-filter').addEventListener('change',updateFilters);
  document.querySelectorAll('[data-mode]').forEach(button=>button.addEventListener('click',()=>{state.mode=button.dataset.mode;document.querySelectorAll('[data-mode]').forEach(b=>{b.classList.toggle('active',b===button);b.setAttribute('aria-pressed',String(b===button));});updateFilters();}));
  $('reset-filter').addEventListener('click',()=>{$('query').value='';$('topic-filter').value='all';state.mode='all';document.querySelectorAll('[data-mode]').forEach(b=>{b.classList.toggle('active',b.dataset.mode==='all');b.setAttribute('aria-pressed',String(b.dataset.mode==='all'));});updateFilters();});
  document.addEventListener('click',event=>{
    const button=event.target.closest('button');if(!button)return;
    if(button.dataset.node)selectItem('node',button.dataset.node,{center:button.closest('#directory')!==null});
    if(button.dataset.edge)selectItem('edge',button.dataset.edge,{center:button.closest('#directory')!==null});
    if(button.dataset.region){closeDetail({restoreFocus:false});focusRegion(button.dataset.region);}
    if(button.dataset.center){const [type,id]=button.dataset.center.split(':');focusItem({type,id});}
  });
  $('zoom-in').addEventListener('click',()=>zoom(1.35));$('zoom-out').addEventListener('click',()=>zoom(1/1.35));$('fit-map').addEventListener('click',fitMap);
  $('toggle-routes').addEventListener('click',()=>{state.showRoutes=!state.showRoutes;$('toggle-routes').setAttribute('aria-pressed',String(state.showRoutes));requestDraw();});
  function setWalk(enabled){
    state.walkMode=enabled;$('toggle-walk').setAttribute('aria-pressed',String(enabled));
    if(enabled){
      state.scale=Math.max(state.scale,state.fitScale*2.5);state.x=state.width/2-state.walker.x*state.scale;state.y=state.height/2-state.walker.y*state.scale;
      $('view-label').textContent='漫游模式';$('view-subtitle').textContent='WASD 行走 · 探险者只是视野游标';
      $('map-hint').innerHTML='<span aria-hidden="true">✥</span> WASD 持续漫游 <span>·</span> 点击地标查看证明';canvas.focus({preventScroll:true});
    }else{$('view-label').textContent='自由探索';$('map-hint').innerHTML='<span aria-hidden="true">✥</span> 拖动探索 <span>·</span> 滚轮缩放 <span>·</span> WASD 漫游';}
    requestDraw();
  }
  $('toggle-walk').addEventListener('click',()=>setWalk(!state.walkMode));
  // Walking changes only the camera and a decorative cursor. It cannot discover,
  // unlock, validate or alter any mathematical object or evidence status.
  const heldKeys=new Set();let lastWalkTime=0,walking=false;
  function walkFrame(time){
    if(!heldKeys.size||!state.walkMode){walking=false;lastWalkTime=0;return;}
    const dt=lastWalkTime?Math.min((time-lastWalkTime)/1000,.05):.016;lastWalkTime=time;
    let dx=(heldKeys.has('d')?1:0)-(heldKeys.has('a')?1:0),dy=(heldKeys.has('s')?1:0)-(heldKeys.has('w')?1:0);const magnitude=Math.hypot(dx,dy)||1;
    state.walker.x=Math.max(45,Math.min(WORLD.w-45,state.walker.x+dx/magnitude*280*dt));state.walker.y=Math.max(45,Math.min(WORLD.h-45,state.walker.y+dy/magnitude*280*dt));
    state.x=state.width/2-state.walker.x*state.scale;state.y=state.height/2-state.walker.y*state.scale;requestDraw();requestAnimationFrame(walkFrame);
  }
  document.addEventListener('keyup',event=>heldKeys.delete(event.key.toLowerCase()));
  window.addEventListener('blur',()=>heldKeys.clear());
  $('close-detail').addEventListener('click',()=>closeDetail());
  function toggleLegend(open){$('legend-popover').hidden=!open;$('legend-button').setAttribute('aria-expanded',String(open));if(open)$('close-legend').focus();else $('legend-button').focus();}
  $('legend-button').addEventListener('click',()=>toggleLegend($('legend-popover').hidden));$('close-legend').addEventListener('click',()=>toggleLegend(false));
  $('help-button').addEventListener('click',()=>$('help-dialog').showModal());$('close-help').addEventListener('click',()=>$('help-dialog').close());$('start-exploring').addEventListener('click',()=>$('help-dialog').close());
  document.addEventListener('keydown',event=>{
    const typing=/INPUT|TEXTAREA|SELECT/.test(event.target.tagName);
    if(event.key==='Escape'){if(!$('detail').hidden)closeDetail();if(!$('legend-popover').hidden)toggleLegend(false);$('tooltip').hidden=true;}
    if(typing||event.ctrlKey||event.metaKey||event.altKey||$('help-dialog').open)return;
    if(event.key==='/'){event.preventDefault();$('query').focus();}
    if(event.key==='+'||event.key==='='){event.preventDefault();zoom(1.3);}
    if(event.key==='-'){event.preventDefault();zoom(1/1.3);}
    if(event.key==='0'){event.preventDefault();fitMap();}
    if(['w','a','s','d'].includes(event.key.toLowerCase())){event.preventDefault();if(!state.walkMode)setWalk(true);heldKeys.add(event.key.toLowerCase());if(!walking){walking=true;requestAnimationFrame(walkFrame);}}
  });
  window.addEventListener('hashchange',readHash);
  const topics=[...new Set(edges.map(e=>e.topic))];for(const topic of topics){const option=document.createElement('option');option.value=topic;option.textContent=`${topic} · ${edges.filter(e=>e.topic===topic).length}`;$('topic-filter').append(option);}
  $('node-total').textContent=nodes.size;$('edge-total').textContent=edges.length;$('region-total').textContent=String(regionDefs.length).padStart(2,'0');$('data-status').textContent=`${nodes.size} 个节点 / ${edges.length} 条超边`;
  updateFilters();new ResizeObserver(resize).observe(canvas);resize();readHash();
  // Read-only diagnostic metadata is deliberately small; original graph fields
  // remain available in #graph-data and in each detail's raw-data disclosure.
  window.PPA_ATLAS=Object.freeze({schema:graph.schema,nodeCount:nodes.size,edgeCount:edges.length,regions:regionDefs.map(r=>({id:r.id,name:r.name,count:r.nodes.length})),version:1});
})();
