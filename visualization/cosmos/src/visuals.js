(function(root,factory){if(typeof module==='object'&&module.exports)module.exports=factory();else root.CosmosVisuals=factory();})(typeof globalThis!=='undefined'?globalThis:this,function(){
const palette=[['#e3b991','#98684a','#26172c'],['#efd396','#af693d','#341e30'],['#9ad9ee','#43788b','#11233e'],['#8be0bc','#347b75','#092c37'],['#dcb18b','#95785d','#362c49'],['#cdb8d6','#7a779a','#292241'],['#a4d8d6','#467b95','#122b46'],['#99b9ec','#5c73b0','#1e234e']];
function defs(){return `<radialGradient id="sun" cx="36%" cy="32%"><stop stop-color="#fffbd7"/><stop offset=".44" stop-color="#ffd574"/><stop offset=".8" stop-color="#f6a94e"/><stop offset="1" stop-color="#b55121"/></radialGradient><radialGradient id="corona"><stop stop-color="#ffcd67" stop-opacity=".28"/><stop offset=".3" stop-color="#f6a83c" stop-opacity=".1"/><stop offset="1" stop-color="#ef9d28" stop-opacity="0"/></radialGradient><radialGradient id="night" cx="12%" cy="25%" r="90%"><stop offset=".3" stop-color="#071021" stop-opacity="0"/><stop offset=".65" stop-color="#030714" stop-opacity=".45"/><stop offset="1" stop-color="#010410" stop-opacity=".97"/></radialGradient><radialGradient id="atmosphere"><stop offset=".72" stop-color="#83cce9" stop-opacity="0"/><stop offset=".85" stop-color="#73c4e9" stop-opacity=".2"/><stop offset="1" stop-color="#7bccea" stop-opacity="0"/></radialGradient><radialGradient id="nebula-blue"><stop stop-color="#2861a5" stop-opacity=".1"/><stop offset=".4" stop-color="#233763" stop-opacity=".065"/><stop offset="1" stop-color="#12203e" stop-opacity="0"/></radialGradient><radialGradient id="nebula-purple"><stop stop-color="#745b9c" stop-opacity=".10"/><stop offset=".5" stop-color="#332647" stop-opacity=".065"/><stop offset="1" stop-color="#120f26" stop-opacity="0"/></radialGradient><radialGradient id="galaxy-glow"><stop stop-color="#d4d6ee" stop-opacity=".7"/><stop offset=".16" stop-color="#8d7fb6" stop-opacity=".4"/><stop offset=".5" stop-color="#544c89" stop-opacity=".18"/><stop offset="1" stop-color="#272443" stop-opacity="0"/></radialGradient><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0 1L9 5L0 9" fill="none" stroke="#8eb4d3" stroke-width="1.3"/></marker><marker id="stop" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M2 1L8 9M2 9L8 1" stroke="#e48a82" stroke-width="1.5"/></marker>`+palette.map((p,i)=>`<radialGradient id="planet-${i}" cx="24%" cy="26%"><stop stop-color="${p[0]}"/><stop offset=".53" stop-color="${p[1]}"/><stop offset="1" stop-color="${p[2]}"/></radialGradient>`).join('');}
function pixelSun(r){const colors=['#cb602b','#ef963d','#ffd16b','#ffe9a0'],paths={};for(let y=-10;y<10;y++)for(let x=-10;x<10;x++){const d=Math.hypot(x+.5,y+.5);if(d>=9.8)continue;let c=d>8.5?1:2;if(x+y>10)c=0;else if(x+y<-9)c=3;else if(d<8&&Math.sin(x*.6+y*.4)+Math.cos(y*.8-x*.3)>1.2)c=3;else if(d<8&&Math.sin(x*.5-y*.7)+Math.cos(y*.5)<-1.1)c=1;(paths[colors[c]]??=[]).push(`M${x} ${y}h1v1h-1Z`);}return `<circle r="160" fill="url(#corona)"/><g class="pixel-sun" shape-rendering="crispEdges" transform="scale(${r/10})">${Object.entries(paths).map(([c,p])=>`<path fill="${c}" d="${p.join('')}"/>`).join('')}</g>`;}
function smallMoon(n,t){const colors=worldColors[t],seed=hash(n.id),paths={};for(let y=-3;y<3;y++)for(let x=-3;x<3;x++){if(Math.hypot(x+.5,y+.5)>2.9)continue;let c=x+y<-2?3:x+y>1?0:2;if((seed%3===0&&x===-1&&y===-1)||(seed%3===1&&x===1&&y===0))c=1;(paths[colors[c]]??=[]).push(`M${x} ${y}h1v1h-1Z`);}return `<g class="pixel-moon world-${t}" shape-rendering="crispEdges" transform="scale(${n.r/3})">${Object.entries(paths).map(([c,p])=>`<path fill="${c}" d="${p.join('')}"/>`).join('')}</g>`;}
function body(n,index){let r=n.r,h='';const seed=Array.from(n.id).reduce((a,c)=>a+c.charCodeAt(0),0);if(n.kind==='sun'){h=pixelSun(r);}else if(n.kind==='galaxy'){h=`<ellipse rx="85" ry="54" fill="url(#galaxy-glow)"/><g class="spin"><path d="M-47 22C-75 -13 26 -49 45 -12C68 21-23 43-39 15C-50-6 11-25 25-7C35 10-6 20-14 5" fill="none" stroke="#b3a4df" stroke-opacity=".45" stroke-width="3"/><ellipse rx="35" ry="12" fill="url(#galaxy-glow)" transform="rotate(-22)"/></g><circle r="4" fill="#dbd4ef"/>`;}else if(n.kind==='hazard'){h=`<circle r="${r+13}" fill="url(#galaxy-glow)" opacity=".25"/><ellipse rx="${r+8}" ry="${r*.4}" fill="none" stroke="#cd9294" stroke-width="2" transform="rotate(-25)"/><circle r="${r}" fill="#030713" stroke="#755b76"/><path d="M-3 -3L3 3M-3 3L3 -3" stroke="#dfa3a0" stroke-width="1"/>`;}else{h=planet(n);}
return h+`<circle class="selection-ring" r="${visualBounds(n)+9}" fill="none"/><circle class="hit" r="${Math.max(visualBounds(n)+8,18)}" fill="transparent"/>`;}
// Original pixel geometry. Visual identity depends on ID, never mathematical status.
function hash(id){let h=2166136261;for(const c of String(id))h=Math.imul(h^c.charCodeAt(0),16777619);return h>>>0;}
const shipCatalog=['Pathfinder','Freighter','Fleet carrier','Ring surveyor','Deep telescope','Twin probe','Construction tug','Solar sailer','Medical ark','Mining barge','Long cruiser','Relay station','Hammerhead','Catamaran','Needle runner','Habitat wheel','Salvage claw','Seed vault','Comet tanker','Tri-wing courier'].map((name,id)=>({id,name}));
// Hull coordinates are deliberately coarse: each step remains legible at map scale.
const hullPaths=[
'M-14-10H-9V-7H-4V-5H2V-3H10V-1H16V1H10V3H2V5H-4V7H-9V10H-14V5H-10V2H-14V-2H-10V-5H-14Z',
'M-13-6H8V-4H13V-2H16V3H12V6H-13Z',
'M-14-8H8V-6H13V-3H17V3H13V6H8V8H-14V4H7V-4H-14Z',
'M-9-8H5V-6H9V-3H15V3H9V6H5V8H-9V5H-13V-5H-9ZM-7-4V4H4V-4Z',
'M-13-3H-2V-5H3V-8H7V-11H11V11H7V8H3V5H-2V3H-13Z',
'M-14-8H5V-6H12V-3H-2V3H12V6H5V8H-14V3H-6V-3H-14Z',
'M-13-5H-5V-2H3V-9H15V-6H7V6H15V9H3V2H-5V5H-13Z',
'M-14-10H-4V-3H3V-10H13V-2H6V2H13V10H3V3H-4V10H-14V2H-7V-2H-14Z',
'M-13-3H-9V-6H-3V-8H5V-6H11V-3H15V3H11V6H5V8H-3V6H-9V3H-13Z',
'M-14-7H-3V-4H6V-7H10V-4H15V4H10V7H6V4H-3V7H-14Z',
'M-16-7H-6V-10H1V-7H9V-5H15V-2H19V2H15V5H9V7H1V10H-6V7H-16V3H-9V-3H-16Z',
'M-5-11H3V-5H7V-2H14V2H7V5H3V11H-5V5H-9V2H-15V-2H-9V-5H-5Z',
'M-14-3H4V-10H10V-7H14V7H10V10H4V3H-14Z',
'M-15-11H4V-9H11V-7H16V-4H-4V4H16V7H11V9H4V11H-15V4H-10V-4H-15Z',
'M-16-9H-9V-5H-3V-3H10V-1H19V1H10V3H-3V5H-9V9H-16V5H-12V2H-16V-2H-12V-5H-16Z',
'M-5-12H2V-9H7V-5H10V5H7V9H2V12H-5V9H-10V5H-13V-5H-10V-9H-5ZM-6-5V5H3V-5Z',
'M-13-4H-5V-7H3V-10H13V-7H6V-4H2V4H6V7H13V10H3V7H-5V4H-13Z',
'M-9-10H-4V-5H0V-10H5V-5H9V-7H13V7H9V5H5V10H0V5H-4V10H-9V5H-13V-5H-9Z',
'M-15-4H-11V-9H-2V-5H2V-9H11V-4H16V4H11V9H2V5H-2V9H-11V4H-15Z',
'M-13-9H-7V-6H-2V-3H8V-1H16V1H8V3H-2V6H-7V9H-13V5H-8V2H-14V-2H-8V-5H-13Z'];
function rect(x,y,w,h,c){return `<rect x="${x}" y="${y}" width="${w}" height="${h}" fill="${c}"/>`;}
function ship(value,options={}){const seed=hash(typeof value==='object'?value.id:value),t=Number.isInteger(options.type)?((options.type%20)+20)%20:seed%20,skin=['#bacbd6','#c8d6b8','#dec6a2','#c0b9db'][Math.floor(seed/20)%4],accent=['#ffc06b','#79e2dd','#e8a0d3','#bde37b'][Math.floor(seed/80)%4];let detail='';
if([1,9].includes(t)){for(let x=-11;x<5;x+=5)detail+=rect(x,-5,4,10,'#52677b')+rect(x,-5,4,2,accent)+rect(x+1,-1,2,4,skin);}
else if(t===17){for(const x of [-8,1])detail+=rect(x,-9,3,18,skin)+rect(x,-8,3,4,accent)+rect(x,4,3,4,accent);detail+=rect(-12,-2,24,4,skin);}
else if(t===10){detail+=rect(-14,-6,8,4,skin)+rect(-14,2,8,4,skin)+rect(-5,-8,5,16,accent)+rect(0,-5,12,10,skin)+rect(2,-3,7,2,'#456483')+rect(2,1,7,2,'#456483');}
else if(t===18){for(const x of [-10,3])detail+=rect(x,-8,7,16,skin)+rect(x+1,-6,5,3,accent)+rect(x+1,3,5,3,accent);detail+=rect(-13,-2,27,4,'#66849a');}
else if(t===0){detail+=rect(-12,-8,3,5,accent)+rect(-12,3,3,5,accent)+rect(-9,-5,6,10,skin)+rect(-2,-3,10,6,skin)+rect(0,-2,5,3,accent);}
else if(t===14){detail+=rect(-15,-8,5,4,accent)+rect(-15,4,5,4,accent)+rect(-10,-4,5,8,skin)+rect(-4,-2,16,4,skin)+rect(0,-1,8,2,'#6ccfdf');}
else if([2,13].includes(t)){for(let x=-11;x<7;x+=5)detail+=rect(x,-7,3,2,accent)+rect(x,5,3,2,accent);detail+=rect(8,-3,3,6,skin);}
else if([3,15].includes(t)){detail+=rect(-9,-7,13,2,accent)+rect(-9,5,13,2,skin)+rect(7,-2,7,4,skin);}
else if(t===4){detail+=rect(8,-9,2,18,accent)+rect(4,-5,2,10,skin)+rect(-11,-2,8,4,skin);}
else if(t===7){for(const x of [-13,4])for(const y of [-9,3])detail+=rect(x,y,8,6,'#426485')+rect(x+1,y+1,2,4,accent)+rect(x+5,y+1,2,4,accent);detail+=rect(-4,-1,9,2,skin);}
else if(t===11){detail+=rect(-3,-10,4,6,accent)+rect(-3,4,4,6,accent)+rect(-8,-1,20,2,skin);}
else {detail+=rect(-9,-2,14,4,skin)+rect(-6,-3,5,1,'#edf0d5')+rect(1,-2,5,2,accent);if([0,10,12,19].includes(t))detail+=rect(-4,-5,3,2,accent)+rect(-4,3,3,2,accent);if([5,6,16].includes(t))detail+=rect(-11,-6,5,2,accent)+rect(-11,4,5,2,accent);if(t===8)detail+=rect(-1,-4,2,8,'#e6e5bc')+rect(-4,-1,8,2,'#e6e5bc');if(t===18)detail+=rect(-6,-6,11,3,accent)+rect(-6,4,11,2,'#647e93');}
// Deterministic optional fittings extend the base silhouettes without changing role.
if((seed>>>9)%3===0&&[0,1,8,9,10,12,14,18,19].includes(t))detail+=rect(-7,-8,1,5,'#8aa6b9')+rect(-9,-8,5,1,accent);
return `<g class="pixel-ship ship-${t}" shape-rendering="crispEdges" transform="scale(1 1.25)"><path d="M-14-2H-19V-1H-24V1H-19V2H-14Z" fill="#5baacb" opacity=".6"/>${rect(-18,-1,5,2,'#b5f1e1')}<path d="${hullPaths[t]}" fill="#4b617a" fill-rule="evenodd" stroke="#24374c" stroke-width="1"/>${detail}${rect(10,-1,3,2,'#edf5d9')}</g>`;}
const planetCatalog=['Terran','Ocean','Gas giant','Glacial','Volcanic','Ring world','Shattered','Crystal','Mycelium','City world','Desert','Crater moon'].map((name,id)=>({id,name}));
const worldColors=[['#174568','#317b88','#75ae80','#d0ddbf'],['#143e74','#267ca8','#60c5cb','#ccede4'],['#674878','#bb7985','#dfab88','#f4d6a4'],['#355583','#6a9aba','#b2dada','#e7f5dc'],['#302b40','#614155','#ef794a','#ffc075'],['#3e4c7b','#7183a8','#b8a1be','#dec8ab'],['#3b4759','#687b84','#afa899','#ddcaaa'],['#353e79','#666fba','#a2bcea','#e1e9e9'],['#244c58','#3c8473','#9ebc77','#e8aec2'],['#293d58','#4d6c83','#88b5b4','#efcb88'],['#765463','#b78571','#e4b78b','#f6dca8'],['#37485b','#667c8c','#a4b8bf','#dcdfcd']];
// Hand-authored cosmetic identities make the eight familiar solar landmarks distinct.
const solarWorldTypes={D01:0,D02:1,D03:2,D04:11,COV:5,CMP:7,LOC:3,R01:4};
function visualBounds(n){if(n.kind==='galaxy')return 85;if(n.kind==='hazard')return n.r+8;if(n.kind==='sun')return n.r;if(n.r<=6)return n.r;const t=solarWorldTypes[n.id]??hash(n.id)%12;return n.r*([5,6,7].includes(t)?1.8:1.05);}
function planet(n,options={}){const seed=hash(n.id),t=Number.isInteger(options.type)?options.type%12:(solarWorldTypes[n.id]??seed%12),r=n.r,colors=worldColors[t],paths={};if(r<=6)return smallMoon(n,t);for(let y=-9;y<9;y++)for(let x=-9;x<9;x++){const d=Math.hypot(x+.5,y+.5);let inside=d<8.8,c=1;if(t===6)inside=d<8.4&&!(x>0&&y<1&&y>-3)&&!(x<0&&x+y>0&&x+y<2);if(t===7)inside=Math.abs(x)*.7+Math.abs(y)<8.7||(Math.abs(x-4)*1.5+Math.abs(y+2)<5);if(t===8)inside=d<7.1||(y<-2&&y>-7&&Math.abs(x)<8);if(!inside)continue;
if(t===0)c=Math.sin(x*.7+seed)+Math.cos(y*.8)+Math.sin((x+y)*.7)>.5?2:0;
if(t===1)c=Math.sin(x*.7+y*.3)+Math.cos(y*.9)>1?2:1;
if(t===2)c=[1,2,2,1,0,1,3,2,1][(y+9)%9];
if(t===3)c=y<-5?3:Math.abs(x-y*.4)%5<1.5?1:2;
if(t===4)c=Math.abs(Math.sin(x*.7+y*.4)+Math.cos(y*.8))<.32?2:0;
if(t===5)c=(y+12)%4===0?2:1;if(t===6)c=(x+y)%4===0?2:1;if(t===7)c=x<y*.4?2:1;
if(t===8)c=y<-3?((x+2*y)%5===0?3:2):((x+1)%4===0?2:0);
if(t===9)c=x%3===0||y%3===0?0:(x+y)%4===0?3:2;
if(t===10)c=Math.sin(x*.4+y*.7)>0?2:1;
if(t===11){c=2;for(const [cx,cy,rr] of [[-3,-3,2.6],[3,2,2],[-2,5,1.5]]){const dd=Math.hypot(x-cx,y-cy);if(dd<rr)c=dd<rr-1?0:1;}}
if(x*.65+y*.4>4)c=Math.max(0,c-1);if(x+y<-9)c=Math.min(3,c+1);(paths[colors[c]]??=[]).push(`M${x} ${y}h1v1h-1Z`);}
let back='',front='';if(t===5){back='<path d="M-15 4L-14 0L-10 -5L2 -9L12 -8L15 -5L14 -1L10 4L-2 8L-12 7Z M-11 3L-8 0L1 -5L10 -5L11 -3L8 0L-1 4L-10 4Z" fill="#b4a8ba" fill-rule="evenodd"/>';front='<path d="M-15 4L-12 7L-2 8L10 4L14 -1L15 -5L12 -2L9 1L-2 5L-11 5Z" fill="#d5bcac"/>';}
if(t===6)back='<path d="M10 -7h3v3h-3ZM-12 3h2v2h-2ZM5 10h3v2h-3Z" fill="#a6a597"/>';
if(t===7)back='<path d="M-9 -7L-5 -4L-6 1L-11 -3ZM6 4L11 3L9 10L6 7Z" fill="#8199d3"/>';
return `<g class="pixel-world world-${t}" shape-rendering="crispEdges" transform="scale(${r/9})">${back}${Object.entries(paths).map(([c,p])=>`<path fill="${c}" d="${p.join('')}"/>`).join('')}${front}</g>`;}

function starfield(width,height){let seed=74129,rand=()=>{seed=(1664525*seed+1013904223)>>>0;return seed/4294967296;};let h='<rect width="100%" height="100%" fill="#040914"/>';for(let i=0;i<600;i++){let x=rand()*width,y=rand()*height,r=rand()<.03?1.35:rand()*.65+.18;h+=`<circle cx="${x}" cy="${y}" r="${r}" fill="${i%7===0?'#9bafd0':'#d1ddeb'}" opacity="${.12+rand()*.5}"/>`;}return h;}
function systemGlyph(s,i=0){if(s.id==='solar')return '<circle r="41" fill="url(#corona)"/><ellipse rx="32" ry="12" fill="none" stroke="#d5a858" opacity=".5"/><ellipse rx="24" ry="8" fill="none" stroke="#d5a858" opacity=".4"/><circle r="8" fill="url(#sun)"/><circle cx="27" cy="-6" r="3" fill="#a1c6d9"/><circle cx="-19" cy="6" r="3" fill="#b5a4da"/>';
let h='<ellipse rx="48" ry="30" fill="url(#galaxy-glow)"/><ellipse rx="27" ry="13" fill="url(#galaxy-glow)" transform="rotate(-18)"/>';
const arms=2+i%3,flatten=i%4===0?.25:.68;
for(let j=0;j<arms;j++){let d='';for(let k=0;k<75;k++){const t=k/74*7.8,a=t+j*Math.PI*2/arms,r=3.6+t*4.2,x=Math.cos(a)*r,y=Math.sin(a)*r*flatten;d+=(k?'L':'M')+x.toFixed(2)+' '+y.toFixed(2)+' ';const jitter=Math.sin(k*71+j*17)*2.3;h+='<circle cx="'+(x+jitter)+'" cy="'+(y+Math.cos(k*19)*1.5)+'" r="'+(.25+(k%5)*.09)+'" fill="'+(k%3===0?'#ddd9ec':s.color)+'" opacity="'+(.3+k%4*.12)+'"/>';}
h+='<path d="'+d+'" fill="none" stroke="'+s.color+'" stroke-width="1.15" opacity=".28"/>';}
h+='<ellipse rx="11" ry="6" fill="url(#galaxy-glow)"/><ellipse rx="3" ry="1.8" fill="#e0d6e7" opacity=".9"/>';if(s.id==='binary')return '<g transform="translate(-17,-7) rotate(-25) scale(.65)">'+h+'</g><g transform="translate(18,10) rotate(35) scale(.55)">'+h+'</g><path d="M-12-3Q-2 12 12 8" stroke="'+s.color+'" stroke-opacity=".35" fill="none"/>';
if(s.id==='gaussian')return '<g transform="rotate(-22)"><ellipse rx="42" ry="30" fill="url(#galaxy-glow)"/><ellipse rx="29" ry="19" fill="url(#galaxy-glow)"/><ellipse rx="17" ry="11" fill="url(#galaxy-glow)"/><ellipse rx="5" ry="3" fill="#ced1df" opacity=".6"/></g>';
if(s.id==='path'||s.id==='foundations')return '<g transform="rotate('+(s.id==='path'?-22:27)+')"><ellipse rx="50" ry="16" fill="url(#galaxy-glow)"/><ellipse rx="38" ry="7" fill="url(#galaxy-glow)"/><ellipse rx="23" ry="6" fill="url(#galaxy-glow)"/><ellipse rx="9" ry="6" fill="#d6c5bf" opacity=".4"/><path d="M-42 1Q0 -2 42 1Q1 4-42 1Z" fill="#09101c" opacity=".7"/><path d="M-39-1Q0-7 39-1" fill="none" stroke="'+s.color+'" stroke-opacity=".4"/></g>';
if(s.id==='finite')return '<ellipse rx="46" ry="29" fill="url(#galaxy-glow)"/><g transform="rotate(-18)"><ellipse rx="31" ry="20" fill="none" stroke="'+s.color+'" stroke-width="3" opacity=".18"/><ellipse rx="30" ry="19" fill="none" stroke="'+s.color+'" stroke-width="1" opacity=".75"/><ellipse rx="29" ry="18" fill="none" stroke="#ccefe9" stroke-width=".5" stroke-dasharray="1 2" opacity=".65"/><ellipse rx="8" ry="5" fill="url(#galaxy-glow)"/></g>';
if(s.id==='space')return '<ellipse rx="48" ry="36" fill="url(#galaxy-glow)" opacity=".65"/><path d="M-36 8Q-19-25 5-18T39-4Q12 31-5 14T-36 8Z" fill="#030814"/><path d="M-36 7Q-23-28 2-18" stroke="#967aab" opacity=".5" fill="none"/><text y="4" text-anchor="middle" font-size="10" fill="#a492ba">?</text>';
if(s.id==='cone'||s.id==='examples'){let cloud='';for(let z=0;z<9;z++){const a=z*2.399,r=8+z*2.6;cloud+='<ellipse cx="'+Math.cos(a)*r+'" cy="'+Math.sin(a)*r*.7+'" rx="'+(13+z%3*4)+'" ry="'+(7+z%4*3)+'" fill="url(#galaxy-glow)" opacity=".5"/>';}
for(let z=0;z<45;z++)cloud+='<circle cx="'+Math.sin(z*719)*36+'" cy="'+Math.cos(z*719.21)*25+'" r="'+(.3+z%4*.2)+'" fill="'+s.color+'" opacity="'+(.2+z%5*.15)+'"/>';return cloud;}
return h;}
return{defs,body,starfield,palette,systemGlyph,ship,shipCatalog,planet,planetCatalog,hash,visualBounds};});
