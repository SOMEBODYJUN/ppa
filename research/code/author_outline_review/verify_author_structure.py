"""Check author-directed result skeleton and the newly included comparison algebra.

Run: PYTHONPATH=/workspace/scratch/cabc4e00b63a/ppa_math_deps python3 \
    research/code/author_outline_review/verify_author_structure.py

Checks visible structure, exact algebra and specified boundary models. A passed
structure check does not certify exposition; final human-style reading is in the
four independent review reports. No randomness; SymPy exact arithmetic.
"""
from pathlib import Path
import hashlib
import json
import re
import sympy as sp

root = Path(__file__).resolve().parents[3]
outline = root/'发表成果整理/论文写作大纲_逐节展开_2026-10-12.md'
text = outline.read_text()
sections = re.findall(r'^### ([1-5]\.\d+) (.*)$', text, re.M)
third = [label for label,_ in sections if label.startswith('3.')]
fourth = [label for label,_ in sections if label.startswith('4.')]
assert third == ['3.1', '3.2', '3.3']
assert fourth == ['4.1', '4.2', '4.3']
assert text.index('**定义1') < text.index('**引理1') < text.index('**定理1')
lemma = text.split('**引理1',1)[1].split('### 1.2',1)[0]
assert 'loosely nonexpansive' in lemma and '2\\gamma' in lemma
assert 'loosely firmly' not in text
assert '### 2.8 假设3' in text and '### 2.9 定理3' in text
gppa = text.split('### 2.8 假设3',1)[1].split('## 第三章',1)[0]
assert all(f'(G{i})' in gppa for i in range(1,6))
assert 'r_F(y)' in gppa and '\\Theta_v' in gppa
for forbidden in ['2a-c', '2T-I', '2y-x-p', 'C249', '本轮', '验收问题', '候选筛选', '开头写', '正式完整名称建议']:
    assert forbidden not in text, forbidden
assert text.count('\\(') == text.count('\\)')
assert text.count('\\[') == text.count('\\]')

# Semimonotone J-side quadratic and its discriminant.
m,s,a,c = sp.symbols('m s a c',real=True)
A,Delta = 1+m+s,1-4*m*s
original = a*(c-a)-m*a*a-s*(c-a)**2
quadratic = A*a*a-(1+2*s)*a*c+s*c*c
assert sp.expand(original+quadratic) == 0
assert sp.expand((1+2*s)**2-4*A*s-Delta) == 0
assert sp.expand(A**2+Delta-(m-s)**2-2*A) == 0
samples = []
for mv,sv in [(0,0),(sp.Rational(-1,4),0),(0,sp.Rational(-1,4)),
              (1,0),(0,1),(sp.Rational(1,2),sp.Rational(1,2)),
              (sp.Rational(-1,6),sp.Rational(-1,6)),
              (sp.Rational(1,3),sp.Rational(-1,5))]:
    Av,Dv = A.subs({m:mv,s:sv}),Delta.subs({m:mv,s:sv})
    assert Av>0 and Dv>=0
    theta = [(1+2*sv-sign*sp.sqrt(Dv))/(2*Av) for sign in [1,-1]]
    lj = (abs(1+2*sv)+sp.sqrt(Dv))/(2*Av)
    ls = (abs(mv-sv)+sp.sqrt(Dv))/Av
    residuals = [sp.simplify(Av*q*q-(1+2*sv)*q+sv) for q in theta]
    assert residuals == [0,0]
    assert sp.simplify(max([abs(q) for q in theta])-lj) == 0
    peak = max([sp.simplify(q*q+(1-q)**2) for q in theta])
    assert sp.simplify(peak-(1+ls**2)/2) == 0
    for x in [sp.Integer(-1000),sp.Integer(0),sp.Integer(1)]:
        for q in theta:
            # Full graph parametrization: output=q*x, selected graph value=(1-q)*x (lambda=1).
            assert q*x+(1-q)*x == x
    samples.append({'m':str(mv),'s':str(sv),'A':str(Av),'Delta':str(Dv),
                    'L_J':str(lj),'L_RL':str(ls),'energy_peak':str(peak)})

# Hypo/inverse hypo axes and their critical collisions.
h,lam,rho=sp.symbols('h lam rho',positive=True)
assert sp.factor(((1+lam*h)/(1-lam*h))**2-1-4*lam*h/(1-lam*h)**2)==0
assert sp.factor(((lam+rho)/(lam-rho))**2-1-4*lam*rho/(lam-rho)**2)==0
tau = sp.symbols('tau',nonnegative=True)
mu = -tau/(lam*(1+2*tau))
nu = -lam*tau/(1+2*tau)
assert sp.simplify(nu-lam**2*mu)==0
assert sp.simplify(1+lam*mu+nu/lam-1/(1+2*tau))==0
assert sp.simplify(1-4*mu*nu-(1+4*tau)/(1+2*tau)**2)==0
# F=-Id/lambda has every y as a complete output at input0; the critical gate excludes it.
for lv in [sp.Rational(1,2),sp.Integer(1),sp.Integer(3)]:
    for y in [sp.Integer(-1000),sp.Integer(0),sp.Integer(1)]:
        assert y+lv*(-y/lv)==0

# Inverse-hypo energy boundary and convex corner prox.
K=sp.symbols('K',positive=True)
q2=K**2/(K**2+lam*(lam-2*rho))
assert sp.simplify(q2.subs(lam,2*rho)-1)==0
assert sp.simplify(q2.subs(rho,0)-K**2/(K**2+lam**2))==0
def project_square(x):
    return tuple(max(sp.Integer(-1),min(sp.Integer(1),v)) for v in x)
for x in [(0,0),(1,1),(2,0),(-3,4),(1000,-1000)]:
    x=tuple(map(sp.Integer,x)); p=project_square(x)
    y=tuple((u+v)/2 for u,v in zip(x,p))
    assert project_square(y)==p
    assert all(yv+(yv-pv)==xv for xv,yv,pv in zip(x,y,p))
result={'outline_sha256':hashlib.sha256(outline.read_bytes()).hexdigest(),
        'visible_structure':'PASS','third_sections':third,'fourth_sections':fourth,
        'semimonotone_exact_samples':samples,'critical_collision':'verified complete fiber at input0',
        'inverse_energy_endpoint':'q_squared=1 at lambda=2rho; monotone endpoint matches',
        'convex_corner_prox':'zero, corner, boundary, cross-sign and distant inputs checked',
        'precision':'exact SymPy','randomness':'none',
        'limit':'algebra and visible structure only; see final reading reports'}
Path(__file__).with_name('author_structure_results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='semimonotone_exact_samples'},ensure_ascii=False,indent=2))
