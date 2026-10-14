"""Verify the current author-directed outline and its displayed algebra.

Run from the repository root:
    python3 research/code/author_outline_review/verify_author_structure.py

Requires SymPy. Exact rational/symbolic arithmetic; Decimal displays use 80
digits. Finite checks supplement the analytic proofs in the current outline.
"""
from decimal import Decimal, getcontext
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import platform
import re
import sympy as sp

getcontext().prec = 80

z, tau = sp.symbols('z tau', positive=True)
old = 1 + 2*tau - 1/(1+z)**2
energy = (1 + 2*tau)/(1+1/z**2)
gap = 2*(z + tau*(1+z)**2)/((1+z**2)*(1+z)**2)
assert sp.factor(old-energy-gap) == 0
# Original-graph RL and the all-output J-side energy have proportional slacks.
output2, step2, inner, omega2 = sp.symbols('output2 step2 inner omega2', real=True)
input2 = output2 + step2 + 2*inner
rl_slack = inner - (input2-omega2)/4
j_slack = (input2+omega2)/2 - output2 - step2
assert sp.expand(j_slack-2*rl_slack) == 0
ell = sp.symbols('ell', nonnegative=True)
assert sp.expand((1+ell**2)/2-1-(ell**2-1)/2) == 0
weak_holder = []
for delta in [Q(0), Q(1, 100), Q(1, 3), Q(1, 2), Q(1)]:
    # T=-Id on [-1/2,1/2], gamma=1/2,L=1: weak Holder passes.
    assert delta*delta <= delta
    energy_ok = 2*delta*delta <= (delta*delta+delta)/2
    if delta == 1:
        assert not energy_ok
    weak_holder.append({'input_distance': str(delta), 'weak_Holder': True,
                        'J_energy': energy_ok})
I = sp.eye(2)
rot = sp.Matrix([[0, -1], [1, 0]])
F = -sp.Rational(2, 7)*I - 3*sp.sqrt(5)*rot/7
T = I/2 + 3*sp.sqrt(5)*rot/10
assert sp.simplify((I+F)*T-I) == sp.zeros(2)
assert sp.simplify(F.T*F-I) == sp.zeros(2)
assert sp.simplify(T.T*T-sp.Rational(7, 10)*I) == sp.zeros(2)
# Direct original-graph RL defect for F: <h,Fh> = -2/7 ||h||².
assert sp.simplify((I+F).T*(I+F)-sp.Rational(10, 7)*I) == sp.zeros(2)
assert sp.Rational(2, 7)/sp.Rational(10, 7) == sp.Rational(1, 5)

multi = []
for x in [Q(0), Q(-1), Q(1), Q(1, 10**10), Q(-10000), Q(10000)]:
    for alpha, coeff in [(Q(1, 3), Q(2)), (Q(1, 4), Q(3))]:
        y = alpha*x
        assert y + coeff*y == x
        assert y*(x-y) >= 3*x*x/16
        residual = 2*abs(y)
        assert abs(y) == residual/2
        if abs(x) <= 1:
            assert residual <= Q(3, 4)
            assert abs(y) <= Q(3, 8)*abs(x)
        multi.append({'input': str(x), 'output': str(y),
                      'true_residual': str(residual), 'branch': str(coeff)})
u, v = Q(1, 3), Q(1, 4)
assert (u-v)*(2*u-3*v) == -Q(1, 144)

# Complete radial optimization prox: f is 1/3-weakly convex, lambda = 1.
# Phi(r)=r+f'(r) is strictly increasing, with seam at r=3/4, input=1/2.
radial = []
for a in [Q(0), Q(1, 10**10), Q(1, 2), Q(3, 4), Q(1), Q(5, 4), Q(10000)]:
    r = 3*a/2 if a <= Q(1, 2) else (a+1)/2
    derivative = -r/3 if r <= Q(3, 4) else r-1
    assert r+derivative == a
    if Q(3, 4) <= a <= Q(5, 4):
        assert abs(r-1) == abs(a-1)/2
        assert abs(r-a) == abs(a-1)/2
        assert abs(derivative) == abs(r-1)
    radial.append({'input_radius': str(a), 'output_radius': str(r),
                   'true_residual': str(abs(derivative))})
seam = Q(3, 4)
assert -seam**2/6 == seam**2/2-seam+Q(3, 8)
assert -seam/3 == seam-1

# Kernel invisible motion: inclusion holds for arbitrary output second coordinate.
kernel = []
for k in range(8):
    x = (Q(1, 2**k), Q((-1)**k))
    y = (Q(1, 2**(k+1)), Q((-1)**(k+1)))
    assert x[0]-y[0] == y[0]
    assert abs(y[1]-x[1]) == 2
    kernel.append({'k': k, 'x': list(map(str, x)), 'y': list(map(str, y))})

# Nonlinear critical gate arithmetic, and a countercheck to universal energy-gate sharpness.
R = Decimal(1)/16
rt2 = Decimal(2).sqrt()
triangular_gate = (R.sqrt()+rt2)**2/4
assert triangular_gate < Decimal(3)/4
energy_boundary_direct = (1+Decimal(33).sqrt())/8
assert energy_boundary_direct < 1

outline_math = {
    'python': platform.python_version(), 'sympy': sp.__version__,
    'precision': 'exact rational and symbolic; Decimal display at 80 digits',
    'randomness': 'none', 'analytic_scope': 'analytic proofs are in the current outline',
    'factor_gap_identity': 'zero', 'matrix_prox_inverse': 'exact identity',
    'J_side_RL_slack_identity': 'J energy slack = 2 * original graph RL slack',
    'J_side_linear_violation': '(L²-1)/2',
    'weak_Holder_is_not_equivalent': weak_holder,
    'matrix_true_EB_K': '1', 'matrix_L_squared': '9/5',
    'matrix_tau': '1/5', 'matrix_actual_factor_squared': '7/10',
    'LT_budget': '4/5 > 1/2', 'energy_budget': '2/5 < 1',
    'same_input_full_pair_RL': '-1/144 < 0; strictly multivalued example fails',
    'multivalued_complete_steps': multi, 'radial_complete_steps': radial,
    'noninjective_kernel_counterexample': kernel,
    'triangular_compatibility_upper': str(triangular_gate),
    'energy_boundary_direct_factor': str(energy_boundary_direct),
    'seam_value_and_derivative': 'exactly matched'
}

def dec(x):
    return Decimal(x.numerator) / Decimal(x.denominator)


def scalar_family():
    rows = []
    for kappa in [Q(1, 100), Q(1, 4), Q(1, 2), Q(3, 4), Q(99, 100)]:
        lam = Q(3, 2)
        radius = Q(1, 7)
        coeff = -(1 + kappa) / (lam * kappa)
        L = 1 + 2 * kappa
        eb = lam * kappa / (1 + kappa)
        B = (1 + L) * radius / 2
        assert 1 / (1 + lam * coeff) == -kappa
        assert eb * abs(coeff) == 1
        assert eb * B / lam == kappa * radius
        assert kappa**2 + (1 + kappa)**2 == (1 + L**2) / 2
        assert B / (1 - kappa) == (1 + kappa) * radius / (1 - kappa)
        for x in [Q(0), -radius, radius, radius / 100]:
            y = -kappa * x
            assert y + lam * coeff * y == x
            assert abs(x - y) == (1 + kappa) * abs(x)
        rows.append({"kappa": str(kappa), "L": str(L), "true_EB": str(eb),
                     "bar_t": str(B / lam), "length_ratio": str((1 + kappa)/(1-kappa))})
    return rows


def energy_family():
    # The same point supplied independently by the literature-comparison reader.
    a = Q(-2, 7)
    b2 = Q(45, 49)
    t2 = a*a + b2
    denom = (1 + a)**2 + b2
    L2 = ((1 - a)**2 + b2) / denom
    rho2 = 1 / denom
    assert t2 == 1 and L2 == Q(9, 5) and rho2 == Q(7, 10)
    assert rho2 == (1 + L2) / (2 * (1 + t2))
    assert Q(1, 5) * 4 > Q(1, 2)  # Luke--Tam displayed budget fails.
    assert 2 * Q(1, 5) < 1         # Energy budget succeeds.
    boundary = []
    for t in [Q(1, 4), Q(1, 2), Q(1), Q(2), Q(3)]:
        a = -t*t/2
        feasible = a*a <= t*t
        L2 = 1 + 2*t*t
        assert (1 + L2)/(2*(1+t*t)) == 1
        direct = (1 + dec(L2).sqrt()) / (2 * dec(t))
        if t > 2:
            assert not feasible and direct < 1
        elif t == 2:
            assert feasible and direct == 1
        else:
            assert feasible and direct > 1
        boundary.append({"t": str(t), "rotation_feasible": feasible,
                         "formal_energy_factor_squared": "1", "direct_factor": str(direct)})
    return {"attained_point": {"lambda": "1", "K": "1", "L_squared": str(Q(9,5)),
                              "rho_E_squared": str(rho2)}, "energy_boundary": boundary}


def triangular_certificate():
    R = Decimal(1)/16
    L = Decimal(2).sqrt()
    ratio = (R.sqrt()+L)**2/4
    assert ratio < Decimal(3)/4
    return {"R": "1/16", "certificate_kappa": "3/4", "exact_distance_factor": "1/2",
            "actual_point_factor": str(Decimal(1)/Decimal(2).sqrt()),
            "certificate_endpoint_ratio": str(ratio)}



root = Path(__file__).resolve().parents[3]
outline = root/'发表成果整理/论文写作大纲_逐节展开_2026-10-12.md'
text = outline.read_text()
sections = re.findall(r'^### ([1-5]\.\d+) (.*)$', text, re.M)
first = [label for label,_ in sections if label.startswith('1.')]
assert first == ['1.1', '1.2', '1.3', '1.4', '1.5', '1.6']
assert '### 1.2 广义度量次正则与模函数' in text
assert '### 1.3 广义预解式及普通 PPA' in text
assert '\\Phi^{-1}' in text and '\\psi' in text
assert '(v+\\lambda F)^{-1}\\circ v' in text
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
        'visible_structure':'PASS','first_sections':first,'third_sections':third,'fourth_sections':fourth,
        'semimonotone_exact_samples':samples,'critical_collision':'verified complete fiber at input0',
        'inverse_energy_endpoint':'q_squared=1 at lambda=2rho; monotone endpoint matches',
        'convex_corner_prox':'zero, corner, boundary, cross-sign and distant inputs checked',
        'precision':'exact SymPy','randomness':'none',
        'limit':'finite algebra and structure checks supplement the analytic proofs in the current outline'}
result.update({'python': platform.python_version(), 'sympy': sp.__version__,
               'outline_math': outline_math,
               'sharp_diagnostics': {'scalar_family': scalar_family(),
                                     'energy_family': energy_family(),
                                     'triangular': triangular_certificate()},
               'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()})
Path(__file__).with_name('author_structure_results.json').write_text(
    json.dumps(result, ensure_ascii=False, indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items()
                  if k not in {'semimonotone_exact_samples','outline_math','sharp_diagnostics'}},
                 ensure_ascii=False, indent=2))
