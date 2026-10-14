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

def previous(relative):
    return subprocess.check_output(
        ['git','show',f'{BASELINE}:{relative}'], cwd=ROOT, text=True)

def hypothesis_block(source, key):
    pattern = rf'\\begin\{{enumerate\}}\s*\\item\[\({key}1\)\].*?\\end\{{enumerate\}}'
    match = re.search(pattern, source, re.S)
    assert match, key
    return match.group()

for stem, key in [('theorem_spine','B'),('gppa_theory','G')]:
    relative = f'发表成果整理/RLEB/sections/{stem}.tex'
    old, new = previous(relative), (ROOT/relative).read_text()
    assert hypothesis_block(old,key) == hypothesis_block(new,key)
results['locked_hypothesis_bytes'] = 'B1-B4 and G1-G5 identical to baseline'

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
assert r'\begin{corollary}[附带物理提升的固定核 RLEB--GPPA]' in full
results['presentation_and_reference_scope'] = {
    'labels':len(labels), 'references':len(references),
    'duplicates':0, 'undefined':0, 'ppa_proof_depends_on_gppa':False,
}

out = Path(__file__).with_name('output.json')
out.write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(results,ensure_ascii=False,indent=2))
