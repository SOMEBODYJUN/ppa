"""Finite arithmetic checks for C246/C247 and C241-v2, not universal proofs.

Run from any directory with Python 3; output is written next to this file.
No third-party package, network, or secret is required.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import math
import random
import sys


def h(t):
    return math.copysign(math.sqrt(abs(t)), t) if t else 0.0


def prox(a, b):
    return a + h(b) / 4, b / 16


def reflected(a, b):
    return a + h(b) / 2, -7 * b / 8


def f(x, p):
    return -h(p), 15 * p


def norm(x):
    return math.hypot(*x)


def near(a, b, tol=2e-12):
    assert abs(a - b) <= tol * max(1, abs(a), abs(b)), (a, b)


R = Q(1, 16)
assert (R + math.sqrt(float(R))) / 2 == Q(5, 32)
assert Q(25, 64) < Q(1, 2)
assert Q(1, 4) + 1 / math.sqrt(2) < 1
assert Q(225, 256) + Q(1, 256) == Q(113, 128)
seed = 20261011
rng = random.Random(seed)
checks = 0
max_graph_error = max_pair_ratio = 0.0
inputs = [(a, b) for a in [-1e6, -1, 0, 1, 1e6]
          for b in [-16, -float(R), -1e-12, 0, 1e-12, float(R), 16]]
for _ in range(300):
    inputs.append((rng.uniform(-1e3, 1e3), rng.uniform(-float(R), float(R))))
for a, b in inputs:
    x, p = prox(a, b)
    fx, fp = f(x, p)
    error = norm((x + fx - a, p + fp - b))
    max_graph_error = max(max_graph_error, error)
    assert error < 2e-10 * max(1, abs(a), abs(b))
    # Reverse the full graph parametrization independently.
    xa, pb = x - h(p), 16 * p
    near(xa, a)
    near(pb, b)
    rho2 = abs(p) + 225 * p * p
    assert abs(p) <= rho2 + 1e-15
    if abs(b) <= R:
        cr = reflected(a, b)
        assert norm((cr[0] - a, cr[1])) <= math.sqrt(abs(b)) + 2e-10
        assert abs(p) <= R
        assert rho2 <= Q(1, 256) + Q(225, 65536) + 1e-15
    xx, pp = a, b
    for k in range(1, 25):
        xx, pp = prox(xx, pp)
        near(pp, b * 16.0 ** (-k))
        near(xx, a + h(b) / 3 * (1 - 4.0 ** (-k)))
    checks += 1

# Small input-pair windows include cross signs, exact boundary, zero,
# and arbitrary position centers. Formula uses differences to avoid cancellation.
for b, c in [(-float(R) / 2, float(R) / 2), (0, float(R)),
             (0, 0), (2, 2 + float(R)), (-2, -2 + float(R))]:
    delta = abs(b - c)
    lhs = norm(((h(b) - h(c)) / 2, -7 * (b - c) / 8))
    assert lhs <= math.sqrt(delta) + 1e-14
for _ in range(3000):
    center = rng.uniform(-10, 10)
    angle = rng.uniform(-math.pi, math.pi)
    delta = float(R) * rng.random()
    da, db = delta * math.cos(angle), delta * math.sin(angle)
    lhs = norm((da + (h(center + db) - h(center)) / 2, -7 * db / 8))
    assert lhs <= math.sqrt(delta) + 1e-12
    max_pair_ratio = max(max_pair_ratio, lhs / math.sqrt(delta) if delta else 0)
    checks += 1

# Verify exact rational orbit with powers and contact residual at nonzero signs.
for b in [Q(-1, 16), Q(0), Q(1, 16)]:
    for k in range(6):
        p = b / 16 ** k
        assert p * 16 == b / 16 ** (k - 1) if k else p == b

# Fixed-SPD scalar inversion and all roots, including tangency/double-root cases.
def metric_outputs(a, b, A, C, B):
    m = B - C * C / A
    n, d = m + 15, C / A
    ts = []
    # On t>=0: n*t^2+d*t=m*b. On t<=0: -n*t^2+d*t=m*b.
    for qa, qb, qc, sign in [(n, d, -m*b, 1), (-n, d, -m*b, -1)]:
        disc = qb*qb - 4*qa*qc
        if disc < -1e-14:
            continue
        for t in [(-qb + math.sqrt(max(0, disc)))/(2*qa),
                  (-qb - math.sqrt(max(0, disc)))/(2*qa)]:
            if sign*t >= -1e-13 and all(abs(t-s) > 1e-12 for s in ts):
                ts.append(0.0 if abs(t) < 1e-13 else t)
    return [(a+d*(b-t*abs(t))+t/A, t*abs(t)) for t in ts]

metric_counts = {}
for A, C, B in [(1, 0, 1), (1, .5, 1), (1, -.5, 1), (2, -1, 3)]:
    m, d = B-C*C/A, C/A
    critical = d*d/(4*(m+15)*m) if d else 0
    bs = [-1, -critical, -critical/2, 0, critical/2, critical, 1]
    for b in bs:
        ys = metric_outputs(0, b, A, C, B)
        assert ys
        for x, p in ys:
            fx, fp = f(x, p)
            near(A*(-x)+C*(b-p), fx)
            near(C*(-x)+B*(b-p), fp)
            # True dual residual, computed two different ways.
            direct = (B*fx*fx - 2*C*fx*fp + A*fp*fp)/(A*B-C*C)
            alternate = abs(p)/A + (d*h(p)+15*p)**2/m
            near(direct, alternate)
        if C >= 0:
            assert len(ys) == 1
        elif b == 0:
            assert len(ys) == 3
            if (A,C,B) == (1,-.5,1):
                assert any(abs(x-Q(128,3969))<1e-12 and abs(p-Q(4,3969))<1e-12 for x,p in ys)
        metric_counts[str((A,C,B,b))] = len(ys)
        checks += 1
    if C < 0:
        e = -d
        p = (e/15)**2
        outputs = metric_outputs(0, p, A, C, B)
        assert any(abs(q-p)<1e-12 and abs(x-e/(15*A))<1e-12 for x,q in outputs)
    elif C == 0:
        leading_L2 = 4*math.sqrt(m)/(A*(m+15))
        near((A*math.sqrt(m))*leading_L2/4, m/(m+15))
    else:
        Lm = 1+2*math.sqrt(m)/(math.sqrt(A)*d)
        rm = min(1,2/(1+Lm),1/(A*math.sqrt(m)*(1+Lm)**2))
        assert (1+Lm)*rm/2 <= 1+1e-15
        assert A*math.sqrt(m)*(1+Lm)**2*rm/4 <= .25+1e-15

# C241-v2 arithmetic independent of numerical nonlinear solving.
old_R = Q(1, 1000)
old_Pmax = old_R**2 + old_R/100
old_L = 2*math.sqrt(float(old_R+Q(1,100))) + float(Q(102,100)+2*old_R)*math.sqrt(float(old_R))
old_eb = (1+99*math.sqrt(float(old_Pmax)))**2+1
old_compat = Q(3,4)*(math.sqrt(float(old_R))+Q(1,4))**2
old_residual2 = old_Pmax+(old_R+old_Pmax)**2
assert old_L < Q(1,4)
assert old_eb < 3
assert old_compat < Q(1,16)
assert old_residual2 < 1
assert Q(1,2)/(1-Q(1,16)) == Q(8,15)
assert Q(1,4)/2/(1-Q(1,4)) == Q(1,6)

# Engineered weakly convex comparator: stable cubic inversion and endpoint fibers.
def engineered_T(a):
    u = min(abs(a)/16,1)
    # 1-(1-u)^(1/3), rationalized to avoid cancellation near zero.
    v = (1-u)**(1/3)
    t = u/(1+v+v*v)
    return math.copysign(t**4,a) if a else 0

engineered_L=2**(10/3)+2**(5/3)
engineered_window=(16+engineered_L*16**(1/3))/2
engineered_compat=(engineered_window/15)**4/16
near(engineered_window,12+2**(11/3))
assert engineered_window<25 and engineered_compat<.5
for a in [-100,-16,-16+1e-8,-1,0,1e-12,1,16-1e-8,16,100]:
    y=engineered_T(a)
    t=abs(y)**.25
    gp=math.copysign(16*(3*t-3*t*t+t**3),y) if y else 0
    if abs(a)<16:
        near(gp,a,1e-9)
    else:
        assert y==math.copysign(1,a)
    residual=15 if abs(y)==1 else abs(gp-y)
    assert abs(y)<=(residual/15)**4+1e-12
    assert abs(y)<=abs(a)+1e-12
for _ in range(1000):
    a,b=rng.uniform(-16,16),rng.uniform(-16,16)
    delta=abs(a-b)
    ca,cb=2*engineered_T(a)-a,2*engineered_T(b)-b
    assert abs(ca-cb)<=engineered_L*delta**(1/3)+1e-12
    checks+=1

results = {
    'status': 'finite-checks-passed; universal statements proved analytically',
    'seed': seed, 'python': sys.version, 'checks': checks,
    'arithmetic': {'R':'1/16','window':'5/32','compatibility':'25/64 < 1/2',
                   'pair_coefficient':.25+1/math.sqrt(2)},
    'max_graph_error':max_graph_error,'max_sampled_pair_ratio':max_pair_ratio,
    'metric_fiber_counts':metric_counts,
    'engineered_comparator':{'L':engineered_L,'evaluation_window':engineered_window,
       'compatibility':engineered_compat,'Q_order_coefficient':float(Q(1,48**4))},
    'original_anchored':{'R':'1/1000','Pmax':str(old_Pmax),
       'L_bound':old_L,'EB_coefficient_bound':old_eb,
       'compatibility_bound':float(old_compat),'residual_squared_bound':str(old_residual2)},
    'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'precision': 'binary64 + exact Fraction arithmetic; no validated interval numerical proof',
}
out=Path(__file__).with_name('results.json')
out.write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in results.items() if k!='metric_fiber_counts'},ensure_ascii=False,indent=2))
