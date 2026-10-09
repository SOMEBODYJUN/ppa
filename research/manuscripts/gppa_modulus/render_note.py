"""Build the standalone research PDF from the exact note source.

This scoped renderer uses ReportLab and Matplotlib MathText; it does not claim
to be a general LaTeX compiler. Unsupported equations fail rather than vanish.
"""
from pathlib import Path
from io import BytesIO
import hashlib
import tempfile
import html
import re
import json
import matplotlib
matplotlib.use('Agg')
from matplotlib.mathtext import math_to_image
from matplotlib.font_manager import FontProperties
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, KeepTogether
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader
from PIL import Image as PILImage

HERE = Path(__file__).resolve().parent
SOURCE = HERE / 'gppa_modulus.tex'
OUT = HERE / 'gppa_modulus.pdf'
FONTS = Path(matplotlib.get_data_path()) / 'fonts/ttf'
MATH_CACHE = tempfile.TemporaryDirectory(prefix='math-', dir=HERE)
MATH_ASSETS = Path(MATH_CACHE.name)
RAW = SOURCE.read_text()
LABELS = {'LMT':'1','BC':'2'}
for number,token in enumerate(re.finditer(r'\\begin\{(equation|align)\}(.*?)\\end\{\1\}',RAW,re.S),1):
    for label in re.findall(r'\\label\{([^}]*)\}',token.group(2)):
        LABELS[label]=str(number)
sec=0; theorem_index=0
for token in re.finditer(r'\\section\{([^}]*)\}|\\begin\{(lemma|theorem|proposition)\}(?:\[[^]]*\])?\s*\\label\{([^}]+)\}',RAW):
    if token.group(1): sec+=1; theorem_index=0
    else:
        theorem_index+=1
        LABELS[token.group(3)]=f'{sec}.{theorem_index}'
pdfmetrics.registerFont(TTFont('NoteSerif', str(FONTS/'DejaVuSerif.ttf')))
pdfmetrics.registerFont(TTFont('NoteSans', str(FONTS/'DejaVuSans.ttf')))
pdfmetrics.registerFont(TTFont('NoteSansBold', str(FONTS/'DejaVuSans-Bold.ttf')))
styles = {
    'body': ParagraphStyle('body', fontName='NoteSerif', fontSize=10, leading=15,
                           spaceAfter=7, textColor=HexColor('#17313c')),
    'section': ParagraphStyle('section', fontName='NoteSansBold', fontSize=13,
                              leading=18, spaceBefore=15, spaceAfter=9,
                              keepWithNext=True, textColor=HexColor('#145b64')),
    'title': ParagraphStyle('title', fontName='NoteSansBold', fontSize=23,
                            leading=29, spaceAfter=14, textColor=HexColor('#17313c')),
    'small': ParagraphStyle('small', fontName='NoteSans', fontSize=8.5, leading=12,
                           spaceAfter=9, textColor=HexColor('#526a73')),
    'theorem': ParagraphStyle('theorem', fontName='NoteSansBold', fontSize=10,
                              leading=15, spaceBefore=6, spaceAfter=6,
                              textColor=HexColor('#145b64')),
}


def group_at(s, at):
    while at < len(s) and s[at].isspace(): at += 1
    if at >= len(s): raise ValueError('missing macro argument')
    if s[at] == '\\':
        token=re.match(r'\\[A-Za-z]+|\\.',s[at:]).group()
        return token,at+len(token)
    if s[at] != '{': return s[at], at+1
    level = 1
    j = at+1
    while j < len(s) and level:
        if s[j] == '{' and (j == 0 or s[j-1] != '\\'): level += 1
        if s[j] == '}' and s[j-1] != '\\': level -= 1
        j += 1
    if level: raise ValueError('unbalanced macro argument')
    return s[at+1:j-1], j


def expand_custom(s):
    for name, arity in [('norm',1),('ip',2)]:
        pat = re.compile(r'\\'+name+r'\b')
        while (m := pat.search(s)):
            arg1, pos = group_at(s,m.end())
            if arity == 1: rep = r'\left\Vert '+arg1+r'\right\Vert'
            else:
                arg2,pos = group_at(s,pos)
                rep = r'\langle '+arg1+','+arg2+r'\rangle'
            s=s[:m.start()]+rep+s[pos:]
    for name in ['zer','ran','gph','dist']:
        s=re.sub(r'\\'+name+r'\b',lambda m:r'\operatorname{'+name+'}',s)
    return s


def plain_text(s):
    s=re.sub(r'\\label\{[^}]*\}','',s)
    s=re.sub(r'\\(eqref|ref|cite)\{([^}]*)\}',lambda m:
             ('('+LABELS[m.group(2)]+')' if m.group(1)=='eqref' else
              '['+LABELS[m.group(2)]+']' if m.group(1)=='cite' else LABELS[m.group(2)]),s)
    s=s.replace(r"Th\'era",'Théra').replace(r'B\`ui','Bùi').replace(r'H\"older','Hölder')
    s=re.sub(r'\\(?:emph|textbf|textit|mathrm|operatorname|mathcal|mathbb|text)\{([^}]*)\}',r'\1',s)
    s=s.replace(r'\norm','norm ').replace(r'\ip','inner product ')
    greek={'lambda':'λ','varepsilon':'ε','epsilon':'ε','omega':'ω','gamma':'γ','nu':'ν',
           'theta':'θ','tau':'τ','psi':'ψ','eta':'η','rho':'ρ','alpha':'α','kappa':'κ',
           'delta':'δ','phi':'φ','varphi':'φ','Pi':'Π','Gamma':'Γ','infty':'∞',
           'ge':'≥','le':'≤','ne':'≠','to':'→','subset':'⊂','subseteq':'⊆','in':'∈',
           'rightrightarrows':'⇉','times':'×','sim':'∼','equiv':'≡','cdot':'·'}
    for k,v in greek.items(): s=re.sub(r'\\'+k+r'\b',v,s)
    s=s.replace(r'\quad',' ').replace(r'\,',' ').replace(r'\;',' ').replace(r'\!', '')
    s=s.replace(r'\left','').replace(r'\right','').replace(r'\Vert','||')
    s=s.replace(r'\{','(').replace(r'\}',')')
    s=re.sub(r'\\([A-Za-z]+)',r'\1',s)
    s=s.replace('$','').replace('{','(').replace('}',')').replace('~',' ')
    s=s.replace('\\',' ').replace('--','–')
    return html.escape(' '.join(s.split()))


def normalize_math(s):
    s=' '.join(expand_custom(s).split()).replace(r'\tfrac',r'\frac')
    s=re.sub(r'\\(mathcal|mathbb|mathbf)\s*([A-Za-z])',r'\\\1{\2}',s)
    for name in ['sqrt','bar','widehat']:
        for macro in reversed(list(re.finditer(r'\\'+name+r'(?![A-Za-z])',s))):
            arg,end=group_at(s,macro.end())
            s=s[:macro.start()]+'\\'+name+'{'+arg+'}'+s[end:]
    for macro in reversed(list(re.finditer(r'\\frac(?![A-Za-z])',s))):
        numerator,pos=group_at(s,macro.end())
        denominator,end=group_at(s,pos)
        s=s[:macro.start()]+r'\frac{'+numerator+'}{'+denominator+'}'+s[end:]
    s=re.sub(r'\\le(?![A-Za-z])',r'\\leq ',s)
    s=re.sub(r'\\ge(?![A-Za-z])',r'\\geq ',s)
    s=re.sub(r'\\text\{([^}]*)\}',lambda m:r'\mathrm{'+m.group(1).replace(' ',r'\ ' )+'}',s)
    return s


inline_count=0
def plain(s):
    global inline_count
    fragments=[]
    for i,part in enumerate(re.split(r'\$(.*?)\$',s,flags=re.S)):
        if i%2==0:
            fragments.append(plain_text(part))
            continue
        expression=normalize_math(part)
        name=hashlib.sha256(expression.encode()).hexdigest()[:20]+'.png'
        target=MATH_ASSETS/name
        if not target.exists():
            math_to_image('$'+expression+'$',str(target),prop=FontProperties(size=10),dpi=240,format='png',color='#17313c')
        w,h=PILImage.open(target).size
        width,height=w*72/240,h*72/240
        assert width<475, ('inline equation too wide',expression)
        fragments.append(f'<img src="{target}" width="{width:.2f}" height="{height:.2f}" valign="middle"/>')
        inline_count+=1
    return ' '.join(fragments)


counter=0
display_block=0
equations=[]
def display(s):
    global counter,display_block
    display_block+=1
    s=re.sub(r'\\label\{[^}]*\}|\\nonumber','',s)
    lines=re.split(r'\\\\',s)
    objects=[]
    for index,line in enumerate(lines):
        line=line.replace('&','').strip()
        if not line: continue
        line=normalize_math(line)
        if index==len(lines)-1:
            line+=r'\qquad ('+str(display_block)+')'
        # MathText uses \Vert and \leq; keep all mathematics in this expression.
        buffer=BytesIO()
        math_to_image('$'+line+'$',buffer,prop=FontProperties(size=13),dpi=240,format='png',color='#17313c')
        buffer.seek(0)
        img=PILImage.open(buffer)
        w,h=img.size
        width=w*72/240; height=h*72/240
        scale=min(1.,475/width)
        assert scale>=.48, ('formula too wide to remain legible',line)
        counter+=1
        equations.append({'index':counter,'math':line,'scale':scale})
        objects.append(Image(buffer,width=width*scale,height=height*scale,hAlign='CENTER'))
        objects.append(Spacer(1,6))
    return objects


raw=RAW
body=raw.split(r'\begin{abstract}',1)[1].split(r'\end{document}',1)[0]
abstract,body=body.split(r'\end{abstract}',1)
story=[Paragraph('General-modulus convergence of generalized proximal point iterations',styles['title']),
       Paragraph('PPA research project · 9 October 2026',styles['small']),
       Paragraph(plain(abstract),styles['body'])]

pattern=re.compile(r'\\begin\{(equation|align)\}(.*?)\\end\{\1\}|\\section\{([^}]*)\}|\\begin\{(theorem|lemma|proposition|proof)\}(\[[^]]*\])?|\\end\{(?:theorem|lemma|proposition|proof)\}',re.S)
last=0; section=0; theorem_index=0
def add_prose(text):
    text=re.sub(r'\\label\{[^}]*\}','',text)
    text=re.sub(r'\\begin\{(?:enumerate|thebibliography)\}(?:\{[^}]*\})?|\\end\{(?:enumerate|thebibliography)\}','',text)
    text=text.replace(r'\item','\n\n• ')
    text=re.sub(r'\\bibitem\{[^}]*\}','\n\n',text)
    for p in re.split(r'\n\s*\n',text):
        clean=plain(p)
        if clean: story.append(Paragraph(clean,styles['body']))

for m in pattern.finditer(body):
    add_prose(body[last:m.start()])
    if m.group(1): story.extend(display(m.group(2)))
    elif m.group(3):
        section+=1; theorem_index=0
        story.append(Paragraph(str(section)+'. '+plain(m.group(3)),styles['section']))
    elif m.group(4):
        if m.group(4)!='proof': theorem_index+=1
        number='' if m.group(4)=='proof' else f' {section}.{theorem_index}'
        label=m.group(4).capitalize()+number+((' · '+m.group(5)[1:-1]) if m.group(5) else '')
        story.append(Paragraph(plain(label),styles['theorem']))
    last=m.end()
add_prose(body[last:])

def footer(c,doc):
    c.setStrokeColor(HexColor('#b2cbd0'));c.line(50,43,545,43)
    c.setFont('NoteSans',8);c.setFillColor(HexColor('#526a73'))
    c.drawString(50,30,'PPA · General-modulus GPPA · internally reviewed research note')
    c.drawRightString(545,30,str(doc.page))

doc=SimpleDocTemplate(str(OUT),pagesize=(595.28,841.89),rightMargin=50,leftMargin=50,
                      topMargin=50,bottomMargin=58,title='General-modulus convergence of generalized proximal point iterations',author='PPA research project')
doc.build(story,onFirstPage=footer,onLaterPages=footer)
MATH_CACHE.cleanup()
(HERE/'render_verification.json').write_text(json.dumps({'display_formula_lines':counter,'inline_formula_occurrences':inline_count,
    'renderer':'ReportLab paragraphs + Matplotlib MathText display equations',
    'scope':'Scoped source renderer; not a complete LaTeX compiler',
    'label_reference_map':LABELS,'equations':equations},indent=2)+'\n')
print(json.dumps({'pdf':str(OUT),'display_formula_lines':counter}))
