/* Synthetic DOM/Canvas execution. This is NOT a browser rendering test. */
'use strict';
const fs=require('fs'),path=require('path'),vm=require('vm'),assert=require('assert');
const root=path.resolve(__dirname,'..'),page=fs.readFileSync(path.join(root,'index.html'),'utf8');
const graph=JSON.parse(page.match(/id="graph-data">([\s\S]*?)<\/script>/)[1]);
const elements=new Map(),events=new Map();
const ctx=new Proxy({measureText:s=>({width:String(s).length*6})},{get:(o,k)=>k in o?o[k]:(()=>{}),set:(o,k,v)=>(o[k]=v,true)});
function element(id=''){return {id,hidden:true,open:false,value:id==='topic-filter'?'all':'',textContent:'',innerHTML:'',style:{},dataset:{},classList:{toggle(){},add(){},remove(){}},width:200,height:128,offsetWidth:220,offsetHeight:130,isConnected:true,addEventListener(k,fn){events.set(id+':'+k,fn)},setAttribute(){},getContext:()=>ctx,getBoundingClientRect:()=>({width:1150,height:800,left:0,top:0}),append(){},focus(){},closest:()=>null,setPointerCapture(){},showModal(){this.open=true},close(){this.open=false}}}
const document={body:element('body'),activeElement:null,getElementById(id){if(!elements.has(id))elements.set(id,element(id));return elements.get(id)},createElement:tag=>element(tag),querySelectorAll:()=>[],addEventListener(k,fn){events.set('document:'+k,fn)}};
for(const id of ['graph-data','world-data','object-data'])document.getElementById(id).textContent=page.match(new RegExp('id="'+id+'">([\\s\\S]*?)<\\/script>'))[1];
const sandbox={document,console,Image:class{set src(v){if(this.onload)this.onload()}},ResizeObserver:class{observe(){}},requestAnimationFrame(){},getComputedStyle:()=>({fontFamily:'serif'}),location:{hash:'',pathname:'index.html',search:''},history:{replaceState(){}},setTimeout,clearTimeout,window:{devicePixelRatio:1,addEventListener(){}},performance:{now:()=>0}};
vm.runInNewContext(fs.readFileSync(path.join(root,'src/map.js'),'utf8'),sandbox,{filename:'map.js',timeout:20000});
const api=sandbox.window.XianxiaAtlas;
assert.equal(api.graph.nodes.length,294);assert.equal(api.graph.edges.length,194);
for(const n of graph.nodes){api.selectItem('node',n.id,{center:true,hash:false});assert.equal(api.state.selected.id,n.id);assert(document.getElementById('detail-content').innerHTML.includes(n.id));}
const esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
for(const e of graph.edges){api.selectItem('edge',e.id,{center:true,hash:false});const html=document.getElementById('detail-content').innerHTML;assert(html.includes(esc(e.scope)),e.id+' scope');assert(html.includes(esc(e.status)),e.id+' status');assert(html.includes(esc(e.relation)),e.id+' relation');for(const id of [...e.inputs,e.output])assert(html.includes('data-node="'+esc(id)+'"'),e.id+' '+id);}
document.getElementById('query').value='COV';events.get('query:input')();assert(api.state.visibleNodes.has('COV'));
api.focusRegion('foundation');assert.equal(api.state.activeRegion,'foundation');api.fitMap();assert.equal(api.state.activeRegion,null);
const scale=api.state.scale;api.zoom(2);assert(api.state.scale>scale);
// Runtime loops use graph snapshot, not manifest keys; tombstones never become nodes.
assert.equal(sandbox.window.PPA_ATLAS.nodeCount,graph.nodes.length);
console.log('Synthetic runtime: 294 node details, 194 complete hyperedge details, search, region focus and zoom passed. No browser/CSS assertion.');
