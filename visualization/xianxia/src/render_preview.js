/* Reproducible contact sheet from the authored SVG files. Not a page screenshot. */
const fs=require('fs'),path=require('path');
let sharp;try{sharp=require('sharp')}catch{sharp=require(path.join(process.env.CODEX_PRIMARY_RUNTIME_NODE_MODULES||'', 'sharp'))}
const root=path.resolve(__dirname,'..'),catalog=JSON.parse(fs.readFileSync(path.join(root,'data/objects.json'),'utf8')).objects;
const cols=8,cw=160,rh=220,w=cols*cw+80,h=4*rh+145;
const family=['ACADEMIES / GATEWAYS','ARTIFACTS / STUDY OBJECTS','LANDSCAPES / FRONTIERS','OBSTRUCTIONS / BOUNDARIES'];
let body=`<svg xmlns="http://www.w3.org/2000/svg" width="${w}" height="${h}"><rect width="${w}" height="${h}" fill="#f0eedf"/><rect width="${w}" height="108" fill="#173e43"/><text x="42" y="44" font-family="serif" font-size="26" fill="#e5dfbf" letter-spacing="5">YUNXIU / OBJECT ATLAS 01</text><text x="44" y="77" font-family="sans-serif" font-size="12" fill="#b4c6b3">32 distinct silhouettes · jade, ink and warm gold · generated from the actual SVG assets</text>`;
catalog.forEach((o,i)=>{const row=Math.floor(i/cols),col=i%cols,x=40+col*cw,y=139+row*rh; if(col===0)body+=`<text x="42" y="${y}" font-family="sans-serif" font-size="10" letter-spacing="2" fill="#8c7b53">${family[row]}</text>`;const bytes=fs.readFileSync(path.join(root,o.file));body+=`<rect x="${x+3}" y="${y+15}" width="150" height="176" rx="3" fill="#f8f5e9" stroke="#d6dcc9"/><image x="${x+9}" y="${y+20}" width="138" height="138" href="data:image/svg+xml;base64,${bytes.toString('base64')}"/><text x="${x+78}" y="${y+175}" text-anchor="middle" font-family="monospace" font-size="11" fill="#52766a">${o.id}</text>`});
body+='</svg>';
sharp(Buffer.from(body)).png().toFile(path.join(root,'assets/preview.png')).then(()=>console.log('Rendered assets/preview.png from 32 source SVGs'));
