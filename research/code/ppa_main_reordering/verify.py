#!/usr/bin/env python3
"""Algebra and scope checks for the 2026-10-14 PPA-first presentation.

Finite checks supplement the analytic manuscript proofs; they certify neither
universal coverage nor convergence by themselves. No new operator is registered.
"""
from fractions import Fraction as Q
from pathlib import Path
import json
import re
import subprocess
import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
PAPER = ROOT / '发表成果整理/RLEB'
BASELINE = 'b55626c2ca62498620d803fb7e426ec8f6e211fe'
results = {}

# The ordinary PPA proof uses physical a=y-p, b=x-y, not kernel vectors.
a = sp.Matrix(sp.symbols('a0:3', real=True))
b = sp.Matrix(sp.symbols('b0:3', real=True))
assert sp.expand((a+b).dot(a+b)-(a-b).dot(a-b)-4*a.dot(b)) == 0
assert sp.expand((a+b).dot(a+b)+(a-b).dot(a-b)
                 -2*(a.dot(a)+b.dot(b))) == 0
results['reflection_and_parallelogram'] = 'exact symbolic identities'

t, k, L, gamma = sp.symbols('t k L gamma', positive=True)
theta = (t/(1-k)+L*t**gamma/(1-k**gamma))/2
budget_gap = theta - (t+L*t**gamma)/2 - theta.subs(t, k*t)
assert sp.simplify(sp.expand_power_base(budget_gap, force=True)) == 0
results['power_budget_recurrence'] = 'Theta(t)=B(t)+Theta(kappa*t), exact'

# A non-power scalar example checks that the new principal statement really
# retains general moduli. This is a modulus calculation, not a realized model.
B_log = t*(1-sp.log(t)/2)
theta_log = t*((1-sp.log(t)/2)/(1-k)
              -sp.log(k)*k/(2*(1-k)**2))
assert sp.simplify(theta_log-B_log-theta_log.subs(t,k*t)) == 0
assert sp.limit(theta_log.subs(k,sp.Rational(1,2)),t,0,dir='+') == 0
gate_at_R = (B_log**2/t).subs(t,sp.Rational(1,16))
assert gate_at_R.evalf(80) < sp.Rational(1,2)
results['nonpower_scalar_budget'] = {
    'omega': 't*(1-log(t)), 0<t<=1; omega(0)=0',
    'R': '1/16', 'lambda': 1, 'psi': 's^2', 'kappa': '1/2',
    'compatibility_ratio_at_R_80_digits': str(gate_at_R.evalf(80)),
    'scope': 'scalar formulas only; no F or general coverage inferred',
}

# Complete two-output relation F(y)={2y,3y}: use the true infimum, not each
# selected graph value. Include signs, zero, and the declared input endpoints.
for x in map(Q, ['-1','-1/2','-1/1000','0','1/1000','1/2','1']):
    for y in (x/3,x/4):
        assert x-y in (2*y,3*y)
        residual = min(abs(2*y),abs(3*y))
        assert residual == 2*abs(y)
        assert abs(2*y-x) <= abs(x)/2
        assert abs(y) == residual/2
        assert abs(y) <= Q(3,8)*abs(x)
results['complete_two_output_boundaries'] = 'both fibers, signs, zero, |x|=R=1'

# Preserve the warning that an SPD kernel may invalidate a zero-input fiber.
M = sp.Matrix([[1,sp.Rational(1,2)],[sp.Rational(1,2),1]])
y = sp.Matrix([-sp.Rational(4,49),sp.Rational(16,49)])
F_y = sp.Matrix([y[0],-sp.sqrt(abs(y[0]))])
assert M.det() == sp.Rational(3,4)
assert M*(-y) == F_y
assert y[0] != 0
results['spd_zero_input_countercheck'] = 'exact nonzero complete output retained'

def previous(relative, commit=BASELINE):
    return subprocess.check_output(
        ['git','show',f'{commit}:{relative}'], cwd=ROOT, text=True)

def hypothesis_block(source, key):
    pattern = rf'\\begin\{{enumerate\}}\s*\\item\[\({key}1\)\].*?\\end\{{enumerate\}}'
    match = re.search(pattern, source, re.S)
    assert match, key
    return match.group()

relative = '发表成果整理/RLEB/sections/theorem_spine.tex'
ppa = (ROOT/relative).read_text()
assert hypothesis_block(previous(relative),'B') == hypothesis_block(ppa,'B')
assert hypothesis_block(previous(relative,'10b475b'),'P') == hypothesis_block(ppa,'P')

def clause(source, key, number):
    match = re.search(
        rf'\\item\[\({key}{number}\)\](.*?)(?=\\item\[|\\end\{{enumerate\}})',
        source,re.S)
    assert match, (key,number)
    return match.group(1)

def normalized(value):
    return re.sub(r'\s+','',value)

relative = '发表成果整理/RLEB/sections/gppa_theory.tex'
old, new = previous(relative), (ROOT/relative).read_text()
for number in (2,3):
    assert clause(old,'G',number) == clause(new,'G',number)

# Expand the explicitly referenced ordinary clauses, rather than claiming that
# the ordinary PPA hypotheses hold unchanged for the original F and kernel.
expanded = {
    1: clause(ppa,'P',1).replace(r'\mathcal J',r'\mathcal J_v')
                       .replace(r'J_{\lambda F}',r'J^v_{\lambda F}'),
    4: clause(ppa,'P',3).replace(r'\mathcal J(U_R)',r'\mathcal J_v(U_R)')
                       .replace('B(R)','K(R)'),
    5: clause(ppa,'P',4).replace('B(t)','K(t)'),
}
for number, value in expanded.items():
    assert normalized(value) == normalized(clause(old,'G',number))
assert '(P1)' in clause(new,'G',1) and 'J^v_{\\lambda F}' in clause(new,'G',1)
assert '(P3)' in clause(new,'G',4) and 'K(R)' in clause(new,'G',4)
assert '(P4)' in clause(new,'G',5) and 'H(t)' in clause(new,'G',5)
assert '(P2) 改为下述 (G2)' in new
assert r'\omega:[0' not in new  # inherited modulus conditions, explicit new domain
assert '$[0,a(R)]$' in new and '$a(0)=0$' in new
results['locked_hypotheses'] = {
    'B1-B4':'identical to original baseline',
    'P1-P4':'identical to 10b475b; moved into a separate assumption',
    'G2-G3':'identical to original baseline',
    'G1-G4-G5':'referenced P clauses expand to original G clauses exactly',
    'kernel_length':'H rather than K remains the physical summation envelope',
}

relative = '发表成果整理/RLEB/sections/topological_obstruction.tex'
old, new = previous(relative), (ROOT/relative).read_text()
old = old[old.index(r'\begin{proposition}'):]
new = new[new.index(r'\begin{proposition}'):]
assert old == new
results['euler_mathematical_body'] = 'unchanged; only opening bridge rewritten'

def inputs(path):
    data = path.read_text()
    yield data
    for included in re.findall(r'\\input\{([^}]+)\}',data):
        yield from inputs(PAPER/(included+'.tex'))

full = '\n'.join(inputs(PAPER/'main.tex'))
labels = re.findall(r'\\label\{([^}]+)\}',full)
references = re.findall(r'\\(?:eqref|ref)\{([^}]+)\}',full)
assert len(labels) == len(set(labels))
assert not (set(references)-set(labels))
assert full.index(r'\label{thm:rleb-ppa-general}') < full.index(r'\label{thm:rleb-gppa-physical}')
ppa_proof = re.search(
    r'\\label\{thm:rleb-ppa-general\}.*?\\begin\{proof\}(.*?)\\end\{proof\}', full,re.S).group(1)
assert 'gppa' not in ppa_proof
assert r'\begin{corollary}[固定核 RLEB--GPPA 推广]' in full
assert full.index(r'\label{ass:rleb-ppa}') < full.index(r'\label{thm:rleb-ppa-general}')
assert full.index(r'\label{ass:rleb-gppa-supplement}') < full.index(r'\label{thm:rleb-gppa-physical}')
outline_relative = '发表成果整理/论文写作大纲_逐节展开_2026-10-12.md'
outline = (ROOT/outline_relative).read_text()
old_outline = previous(outline_relative,'10b475b')
assert '贯穿全文的两个问题' not in outline
assert outline.split('## ',1)[1].startswith('一、标题、摘要、引言怎么安排')
def section_body(source,title):
    return re.search(r'^## [^\n]*'+re.escape(title)+r'\n(.*?)(?=^## |\Z)',
                     source,re.M|re.S).group(1)
for title in ('标题、摘要、引言怎么安排',
              '第一章：前置知识与收敛接口',
              '第三章：与已有单调性和收敛理论的关系',
              '第四章：近端吸引过程与零点集合的几何',
              '第五章：讨论与后续问题'):
    assert section_body(old_outline,title) == section_body(outline,title),title
results['author_outline_preservation'] = 'title/abstract/introduction and chapters 1/3/4/5 unchanged; unwanted opening removed'
results['presentation_and_reference_scope'] = {
    'labels':len(labels), 'references':len(references),
    'duplicates':0, 'undefined':0, 'ppa_proof_depends_on_gppa':False,
}

out = Path(__file__).with_name('output.json')
out.write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(results,ensure_ascii=False,indent=2))
