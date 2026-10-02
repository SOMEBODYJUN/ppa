"""Author the 32 reusable vector sprites. No raster scaling or network assets.

All sprites share a 144 x 144 view box and a (72, 122) ground anchor.
SVG source is the editable asset; the generated atlas embeds it unchanged.
"""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
P={'ink':'#172f38','dark':'#254852','jade':'#4a8c82','light':'#8fc5b1','pale':'#d8e6c9','gold':'#d5ae68','cream':'#f5e7bd','red':'#b86659','violet':'#8d82af','blue':'#6096ab','water':'#39798d','wood':'#816954'}
def path(d,c,stroke=None,sw=2):return f'<path d="{d}" fill="{P.get(c,c)}"'+(f' stroke="{P.get(stroke,stroke)}" stroke-width="{sw}" stroke-linejoin="round"' if stroke else '')+'/>'
def rect(x,y,w,h,c,rx=0):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{P.get(c,c)}"/>'
def ellipse(x,y,rx,ry,c,opacity=1):return f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{P.get(c,c)}" opacity="{opacity}"/>'
def line(x1,y1,x2,y2,c,w=2):return f'<path d="M{x1} {y1}L{x2} {y2}" fill="none" stroke="{P.get(c,c)}" stroke-width="{w}" stroke-linecap="square"/>'
def roof(x,y,w=100):
 return path(f'M{x} {y+15}l{w*.17} -7 L{x+w*.49} {y-16} L{x+w*.75} {y+3} l{w*.25} 12 -8 5 H{x+5}Z','ink')+path(f'M{x+4} {y+11}L{x+w*.49} {y-13}L{x+w-5} {y+11}l-15 -4H{x+20}Z','jade')+line(x+6,y+17,x+w-5,y+17,'gold')+path(f'M{x+w*.49} {y-13}l4 4 -3 11 -5 1Z','light')
def base():return ellipse(72,123,53,10,'ink',.15)+path('M25 114L70 99 120 113 73 135Z','dark')+path('M25 109L70 94 120 108 73 129Z','jade')+path('M36 110L70 101 109 110 73 122Z','light')
def platform():return ellipse(72,126,48,8,'ink',.14)+path('M25 109H119V119H25Z','dark')+rect(29,105,86,9,'pale')+rect(38,121,68,5,'jade')
def pine(x,y,s=1):return f'<g transform="translate({x} {y}) scale({s})">'+rect(-3,-36,6,39,'wood')+path('M0 -70L-13 -44 -6 -44 -21 -24 -10 -25 -27 -7 23 -7 13 -22 19 -22 8 -41 13 -41Z','dark')+path('M0 -69L-12 -44 0 -46 -17 -24 -3 -27 -22 -9 2 -13 7 -36Z','jade')+'</g>'
def cloud(x,y,s=1):return f'<g transform="translate({x} {y}) scale({s})" opacity=".86">'+path('M0 12C-12 12 -12 1 -4 0C-8 -10 11 -18 18 -5C23 -16 43 -10 42 0C56 -3 60 12 46 14H0Z','pale')+'</g>'
def star(x,y,s=1):return path(f'M{x} {y-7*s}l{2*s} {5*s} {5*s} {2*s} -{5*s} {2*s} -{2*s} {5*s} -{2*s} -{5*s} -{5*s} -{2*s} {5*s} -{2*s}Z','gold')
def temple():return platform()+rect(39,65,66,43,'cream')+rect(45,75,16,33,'dark')+rect(67,75,13,33,'wood')+rect(84,75,15,33,'dark')+rect(34,65,7,43,'red')+rect(103,65,7,43,'red')+roof(18,51,110)+rect(57,62,32,11,'ink')+rect(66,65,14,3,'gold')+line(45,83,61,83,'gold')+line(84,83,99,83,'gold')
def pagoda():
 s=platform()
 for i,(y,w) in enumerate([(98,68),(75,55),(54,43)]):s+=rect(72-w/2,y-18,w,22,'cream')+rect(68,y-13,8,14,'dark')+roof(72-w/2-11,y-22,w+22)
 return s+line(72,7,72,22,'gold',3)+star(72,9,.6)
def gate():
 return platform()+path('M29 106V44H41V106M104 106V44H116V106','dark')+rect(25,105,20,9,'pale')+rect(100,105,20,9,'pale')+rect(26,44,93,9,'jade')+rect(43,54,57,7,'gold')+path('M21 40L39 34H106L124 40 118 46H28Z','dark')+path('M50 37V27H96V37Z','jade')+path('M43 28L71 15 105 28Z','ink')+rect(61,30,24,19,'cream')+line(66,37,80,37,'red')+line(34,57,34,93,'gold',1)+line(111,57,111,93,'gold',1)+ellipse(35,64,4,5,'red')+ellipse(110,64,4,5,'red')
def archive():
 s=platform()+rect(40,44,66,64,'cream')+rect(44,50,58,23,'dark')+rect(44,79,58,25,'dark')+roof(28,25,89)+rect(35,73,75,5,'wood')
 for x in range(48,98,8):s+=rect(x,54,5,15,'gold' if x%3 else 'jade')+rect(x,83,5,16,'pale' if x%3 else 'red')
 return s+rect(34,44,6,64,'red')+rect(104,44,6,64,'red')+rect(22,89,16,22,'wood')+rect(24,85,12,22,'cream')+line(26,91,33,91,'jade')+rect(56,30,27,9,'ink')+line(63,35,76,35,'gold',1)
def observatory():return platform()+rect(61,66,23,40,'dark')+path('M47 105L61 65H84L98 105Z','jade')+ellipse(72,49,31,28,'ink')+ellipse(72,49,27,24,'gold')+ellipse(72,49,24,21,'dark')+f'<ellipse cx="72" cy="49" rx="12" ry="25" fill="none" stroke="{P["gold"]}" stroke-width="3" transform="rotate(-35 72 49)"/>'+line(39,50,105,50,'gold')+line(72,19,72,80,'gold')+star(72,49,1)+star(113,27,.7)
def pavilion():return platform()+rect(40,59,5,48,'red')+rect(99,59,5,48,'red')+rect(45,98,54,5,'wood')+roof(19,49,107)+ellipse(72,99,16,4,'wood')+rect(70,85,4,15,'wood')+ellipse(72,84,17,4,'cream')
def courtyard():return base()+rect(25,83,88,24,'cream')+rect(30,82,10,30,'dark')+rect(103,82,10,30,'dark')+rect(51,63,39,48,'cream')+roof(35,48,73)+rect(64,78,13,32,'dark')+pine(115,102,.5)+rect(29,82,18,6,'jade')+rect(95,82,18,6,'jade')
def workshop():return temple()+path('M80 111L90 76 112 76 126 111Z','dark')+path('M89 104L95 82H106L115 104Z','red')+rect(86,69,29,8,'gold')+cloud(106,44,.4)
def furnace():return platform()+rect(43,104,9,20,'dark')+rect(94,104,9,20,'dark')+path('M43 63Q32 105 55 115H92Q116 102 102 63Z','dark')+path('M49 69Q42 99 62 108H88Q105 96 98 69Z','jade')+ellipse(73,64,31,8,'gold')+path('M44 58L54 48H91L104 58Z','gold')+rect(64,38,18,10,'dark')+path('M40 74Q17 74 26 96L43 98M104 74Q129 74 119 96L103 98','none','gold',5)+path('M72 86l-7 10 8 8 8 -8Z','gold')+cloud(68,19,.5)
def scroll():return platform()+rect(35,38,70,67,'cream')+rect(31,34,78,9,'wood')+rect(31,101,78,9,'wood')+rect(42,48,6,39,'red')+line(59,54,92,54,'jade')+line(59,64,86,64,'jade')+line(59,74,92,74,'jade')+line(59,84,82,84,'jade')+star(75,21,.7)
def sword():return base()+path('M57 112L45 99 55 86 85 86 98 105 88 117Z','dark')+path('M71 91L68 31 74 18 80 31 75 91Z','pale')+path('M74 25L74 89H79L80 31Z','blue')+path('M54 87L72 82 92 87 91 93 74 90 56 93Z','gold')+rect(70,90,8,17,'red')+ellipse(74,109,6,4,'gold')+star(97,35,.5)
def stele():return base()+path('M47 109V36L58 27H88L98 37V109Z','ink')+path('M53 104V39L62 33H83L92 40V104Z','light')+rect(60,43,25,53,'dark')+line(66,52,80,52,'gold')+line(68,61,80,61,'gold')+line(66,70,78,70,'gold')+line(67,79,80,79,'gold')+rect(39,110,69,6,'pale')
def lotus():
 s=base()+ellipse(73,105,45,15,'water')
 for d in ['M72 93Q34 91 29 63Q57 62 72 93Z','M73 93Q104 90 117 62Q88 61 73 93Z','M73 96Q44 68 52 43Q78 54 73 96Z','M73 95Q99 66 91 43Q69 56 73 95Z','M73 94Q55 65 74 31Q92 67 73 94Z']:s+=path(d,'pale','jade')
 return s+ellipse(74,90,16,5,'gold')+star(110,36,.5)
def bell():return platform()+rect(35,27,6,79,'wood')+rect(105,27,6,79,'wood')+rect(27,27,91,7,'wood')+line(74,32,74,44,'gold',3)+path('M55 47Q73 39 91 47L98 90H48Z','gold')+path('M61 49Q74 44 82 49L88 87H59Z','cream')+ellipse(73,91,27,7,'dark')+line(73,76,73,103,'gold',4)+ellipse(73,103,5,4,'gold')
def spring():return base()+path('M37 107L42 76 59 63 76 76 89 83 109 108Z','dark')+path('M57 80Q86 71 83 88L77 109H63L69 88Z','blue')+path('M72 81L68 112H74L79 82Z','pale')+ellipse(73,114,29,7,'water')+pine(104,91,.6)+star(47,47,.55)
def crystal():return base()+path('M45 99L41 64 54 50 64 65 60 106Z','blue','ink')+path('M63 110L58 48 74 24 92 50 85 113Z','light','ink')+path('M74 25L73 109 85 112 92 50Z','jade')+path('M85 107L91 68 107 61 112 80 100 115Z','violet','ink')+line(64,49,74,32,'cream',3)+star(108,38,.6)
def mountain():return base()+path('M23 111L42 69 50 70 65 26 77 18 90 62 101 52 120 109Z','dark')+path('M48 104L65 27 77 19 90 65 79 54 67 66 61 107Z','jade')+path('M65 28L77 18 86 48 78 42 73 47 68 43 60 48Z','pale')+cloud(13,77,.8)+cloud(89,93,.65)+pine(108,117,.45)
def lake():return base()+ellipse(73,101,49,18,'dark')+ellipse(73,98,44,16,'water')+ellipse(69,96,32,9,'blue')+path('M32 88L48 56 61 85M81 87L103 47 123 94','jade')+path('M96 61L103 47 110 66 104 61Z','pale')+line(49,98,70,98,'pale')+line(77,102,99,102,'light')+cloud(32,53,.6)
def ocean():return base()+path('M25 109Q39 71 59 81Q71 62 87 84Q108 69 123 109Z','water')+path('M31 98Q47 77 62 92Q78 74 93 93Q106 83 119 100','none','pale',3)+path('M41 108Q56 95 72 107Q88 92 107 109','none','light',3)+path('M59 63L95 63 88 72 66 72Z','wood')+line(76,28,76,64,'wood',3)+path('M79 29L98 56H79Z','cream')+path('M71 38L60 56H72Z','jade')
def island():return ellipse(73,124,46,8,'ink',.1)+path('M32 83L115 83 90 113 78 122 67 107 53 109Z','dark')+path('M29 80L69 63 120 80 86 96 61 92Z','jade')+path('M53 89L67 100 67 106 56 104Z','gold')+pine(96,76,.65)+f'<g transform="translate(30 11) scale(.52)">{pavilion()}</g>'+cloud(3,99,.7)+cloud(97,111,.65)
def bamboo():
 s=base()
 for x,y,h in [(44,42,66),(62,26,84),(83,36,79),(103,49,59)]:
  s+=rect(x,y,5,h,'jade')
  for yy in range(y+8,y+h,15):s+=line(x-1,yy,x+6,yy,'gold',1)
  s+=path(f'M{x+3} {y+23}q-22 -23 -28 -13q9 14 28 13M{x+3} {y+37}q20 -29 29 -22q-2 14 -29 22','dark')
 return s+path('M60 117Q72 97 86 96','none','cream',4)
def cave():return base()+path('M28 108L34 74 48 69 53 43 76 30 102 45 113 76 122 112Z','dark')+path('M35 106L42 74 54 78 58 48 77 38 102 50 106 78 116 107Z','jade')+path('M58 110V81Q75 53 92 80V110Z','ink')+path('M63 110V83Q75 63 85 82V110Z','violet')+path('M70 109V89Q76 78 81 89V109Z','pale')+pine(33,84,.4)+star(76,89,.8)
def constellation():
 s=base()+ellipse(73,72,43,43,'dark')+ellipse(73,72,37,37,'ink')
 pts=[(44,67),(61,44),(80,59),(98,45),(102,81),(76,96),(52,89)]
 for (x,y),(xx,yy) in zip(pts,pts[1:]):s+=line(x,y,xx,yy,'blue')
 for x,y in pts:s+=star(x,y,.6)
 return s+rect(62,112,24,5,'gold')
def portal():return platform()+path('M41 108V49Q74 11 105 49V108H94V53Q73 30 52 53V108Z','dark')+path('M51 106V54Q73 27 95 54V106Z','violet')+path('M60 104V58Q73 42 85 59V104Z','blue')+path('M68 103V63Q74 53 78 63V103Z','pale')+star(73,29,.7)+rect(34,107,77,8,'gold')
def broken_bridge():return base()+path('M27 96L47 78 63 84 63 111 49 106 26 121Z','wood')+path('M87 85L108 78 121 96 118 119 92 108Z','wood')+path('M27 92L48 73 65 80 57 88 64 95 51 95 28 115Z','pale')+path('M91 78L108 73 122 92 118 113 93 97 100 92 87 89Z','pale')+path('M69 109L76 93 71 87 80 73 75 107Z','ink')+line(27,84,49,64,'red',3)+line(104,64,125,84,'red',3)
def seal():return base()+path('M40 112L43 54 62 38 95 44 108 111Z','dark')+path('M48 107L51 58 66 46 89 51 98 107Z','jade')+rect(60,40,24,68,'cream')+path('M70 47V58H80M64 65H80L66 82H79M71 82V99','none','red',3)+line(45,94,99,59,'gold',3)+star(32,54,.6)
def thunder():return base()+cloud(28,31,1.5)+path('M73 47L52 85H72L61 118 100 72H80L91 47Z','gold','ink')+path('M75 50L63 78H83L71 96 94 75H76L86 50Z','cream')
def thorn():return base()+path('M30 111Q24 74 56 72Q81 50 107 88L112 112M49 114Q65 99 50 66Q49 42 74 41Q100 39 96 70','none','dark',8)+path('M33 87L19 76 34 78M49 73L48 57 59 65M80 65L85 49 91 66M99 87L118 78 112 93M56 48L48 33 65 39','jade')+ellipse(71,103,11,6,'red')
def locked_gate():return gate()+rect(45,77,54,31,'dark')+line(48,86,97,86,'gold',3)+line(48,98,97,98,'gold',3)+path('M66 94V87Q73 74 81 87V94','none','gold',3)+rect(64,93,19,15,'red')+rect(72,98,3,6,'cream')
def maze():return base()+path('M31 105V50H112V108H83V76H60V109H43V64H99V95H94V83','none','ink',10)+path('M31 101V47H112V104H83V72H60V105H43V61H99V91H94V80','none','light',6)+star(73,27,.7)
def rift():return base()+path('M31 108L44 52 60 40 67 60 61 78 72 85 64 112Z','dark')+path('M83 111L78 91 87 73 78 61 91 32 107 60 116 108Z','jade')+path('M76 25L68 61 79 75 70 95 78 121 84 91 76 73 83 55Z','violet')+line(70,62,77,74,'cream',2)+star(50,32,.6)
def wall():return platform()+rect(33,47,78,62,'dark')+rect(34,48,76,53,'jade')+''.join(rect(35+i*19,37,12,16,'light') for i in range(4))+''.join(line(35,y,110,y,'dark',3) for y in [65,84])+''.join(line(x,49 if i%2 else 66,x,64 if i%2 else 82,'dark',3) for i,x in enumerate([47,61,77,93]))+rect(66,88,14,21,'ink')+rect(40,105,64,6,'pale')
SPECS=[('archive','藏经阁','village',archive),('temple','问道殿','village',temple),('pagoda','九层书塔','village',pagoda),('gate','山门','village',gate),('observatory','观星台','village',observatory),('pavilion','论道亭','village',pavilion),('courtyard','修学别院','village',courtyard),('workshop','天工坊','village',workshop),('furnace','丹炉','mine',furnace),('scroll','经卷','mine',scroll),('sword','灵剑台','mine',sword),('stele','碑林','mine',stele),('lotus','青莲','mine',lotus),('bell','悟道钟','mine',bell),('spring','灵泉','mine',spring),('crystal','玉晶簇','mine',crystal),('mountain','云山','mountain',mountain),('lake','镜湖','mountain',lake),('ocean','沧海帆舟','mountain',ocean),('island','悬空山','mountain',island),('bamboo','竹海','mountain',bamboo),('cave','洞天','mountain',cave),('constellation','星域','mountain',constellation),('portal','秘境门','mountain',portal),('broken_bridge','断桥','barrier',broken_bridge),('seal','封印碑','barrier',seal),('thunder','雷劫','barrier',thunder),('thorn','荆棘阵','barrier',thorn),('locked_gate','禁制山门','barrier',locked_gate),('maze','迷阵','barrier',maze),('rift','空间裂隙','barrier',rift),('wall','石壁关','barrier',wall)]
def details(ident):
 s=''
 if ident in ['temple','workshop','pavilion','courtyard']:
  # Individual roof tiles, eave brackets, lantern light and floor steps.
  for x in range(38,103,10):s+=line(x,53,x-5,60,'light',1)
  for x in [39,104]:s+=line(x,67,x,75,'gold',1)+ellipse(x,79,4,5,'red')+rect(x-1,84,2,4,'gold')
  s+=line(44,114,103,114,'cream',1)+line(48,119,98,119,'gold',1)
 if ident=='mountain':
  s+=path('M77 23L72 57 63 86 60 108M88 67L86 89 95 107','none','light',1.4)
  s+=path('M41 86L51 77 52 94 62 90M92 91L101 79 108 96','none','ink',1.2)
  s+=cloud(62,69,.65)+path('M91 101Q106 90 122 97Q131 106 118 109','none','pale',3)
 if ident in ['cave','rift','seal','stele']:
  s+=path('M45 92L42 100 47 106M99 90L104 99 100 108','none','light',1)+line(41,113,60,118,'gold',1)
 if ident in ['furnace','bell']:
  s+=line(54,75,91,75,'gold',1)+path('M62 59L70 55 78 59 86 55','none','cream',1)
 if ident=='lotus':s+=path('M74 38V84M55 51L68 84M88 52L80 83','none','light',1)
 if ident in ['lake','ocean','spring']:
  for x,y in [(41,105),(75,112),(92,97)]:s+=line(x,y,x+11,y,'cream',1)
 if ident=='pagoda':s+=line(47,105,62,105,'gold',1)+line(82,105,98,105,'gold',1)
 if ident=='broken_bridge':s+=line(35,98,53,81,'wood',1)+line(40,104,60,85,'wood',1)+line(100,88,114,103,'wood',1)
 return s
def main():
 catalog=[]
 for ident,name,family,fn in SPECS:
  svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 144 144" role="img" aria-label="{name}">'+fn()+details(ident)+'</svg>'
  (ROOT/'assets/objects'/f'{ident}.svg').write_text(svg)
  catalog.append({'id':ident,'name':name,'family':family,'anchor':[72,122],'viewBox':[0,0,144,144],'file':f'assets/objects/{ident}.svg'})
 (ROOT/'data/objects.json').write_text(json.dumps({'version':1,'style':'云岫·青绿金石','objects':catalog},ensure_ascii=False,indent=2)+'\n')
 print(f'Authored {len(catalog)} distinct editable SVG objects')
if __name__=='__main__':main()
