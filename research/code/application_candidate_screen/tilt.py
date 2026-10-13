"""80-digit finite checks for the temporary tilted quartic candidate."""
from decimal import Decimal as D, getcontext
from fractions import Fraction as Q
import json
from pathlib import Path

getcontext().prec = 80
tol = D('1e-65')
h = D(105)/512
a, b, c = -D(7)/8, (7-D(109).sqrt())/16, (7+D(109).sqrt())/16

def cube(x):
    if not x: return D(0)
    sign = D(1) if x > 0 else -D(1)
    y = (abs(x).ln()/3).exp()
    for _ in range(12): y=(2*y+abs(x)/y**2)/3
    return sign*y

def F(y): return y**3-y-h
def T(x): return cube(x+h)

max_reflection = max_EB = max_distance = D(0)
for p in [a,c]:
    assert abs(F(p)) < tol
    for i in range(2001):
        d = -D(1)/64 + D(i)/(64*1000)
        x, y = p+d, T(p+d)
        assert abs(y-p) < D(1)/32
        assert abs(2*y-x-p) <= abs(d)/2+tol
        assert abs(y-p) <= D(1024)/1163*abs(F(y))+tol
        assert D(768)/1163 < D(3)/4
        assert 3*abs(d) < D(1)/8-abs(d)
        assert abs(x-y-F(y)) < tol
        if d:
            max_reflection=max(max_reflection,abs(2*y-x-p)/abs(d))
            max_distance=max(max_distance,abs(y-p)/abs(d))
        if abs(F(y))>tol: max_EB=max(max_EB,abs(y-p)/abs(F(y)))

root_checks=[]
for p in [a,b,c]:
    assert abs(F(p)) < tol
    index=1 if 3*p*p-1>0 else -1
    root_checks.append({'point':str(p),'residual':str(abs(F(p))),'index':index,
                        'T_derivative':str(1/(3*p*p))})
assert sum(z['index'] for z in root_checks)==1
assert max(abs(T(-D(2))),abs(T(D(2)))) < 2
assert T(-h)==0 and F(-h)==-h**3

old_a=(1-D(13).sqrt())/4
old_m=(13-3*D(13).sqrt())/8
old_tau=1/(1+old_m)
old_min_compat=old_tau/old_m
assert old_min_compat>1
result={'decimal_precision':80,'parameters':{'h':'105/512','lambda':'1','R':'1/64','bar_t':'1/64'},
        'full_roots':root_checks,'local_sample_count':4002,
        'max_reflection_ratio':str(max_reflection),'max_EB_ratio':str(max_EB),
        'max_distance_ratio':str(max_distance),'big_ball_outputs':[str(T(-D(2))),str(T(D(2)))],
        'critical_input':str(-h),'critical_output':'0','critical_input_F':str(F(-h)),
        'old_h3_over8_direct_failure':{'outer_root':str(old_a),'curvature':str(old_m),
                                    'minimal_asymptotic_compatibility':str(old_min_compat)},
        'scope':'finite numerical observations; analytic proofs in the application screening report, tilted-double-well entry'}
Path(__file__).with_name('scalar_tilt_results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'passed':True,'local_samples':4002,'old_h3_over8_compatibility':str(old_min_compat)},indent=2))
