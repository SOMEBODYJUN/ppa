"""Finite boundary/cross-sign checks; analytic proof is in 发表成果整理/非Lipschitz近端例独立比较.md."""
import json, math, random
from pathlib import Path
import hashlib, sys
random.seed(20261011)

def T(p):
    t = 2*abs(p)/(math.sqrt(1+4*abs(p))+1)
    return math.copysign(t*t,p) if p else 0.0

def F(y):
    return math.copysign(math.sqrt(abs(y)),y) if y else 0.0

R=.25
xs=sorted(set([-R,R,0.]+[R*math.cos(j*math.pi/2000) for j in range(2001)]+[s*10.**(-j) for s in (-1,1) for j in range(1,15)]))
errs=[]
worst_anchor=worst_eb=worst_compat=worst_pair=0.
for p in xs:
    y=T(p); r=abs(F(y)); d=abs(p)
    errs.append(abs(p-y-F(y)))
    worst_anchor=max(worst_anchor,abs(2*y-p)/(math.sqrt(d) or 1.))
    worst_eb=max(worst_eb, abs(abs(y)-r*r))
    if d: worst_compat=max(worst_compat,((d+math.sqrt(d))/2)**2/d)
for _ in range(50000):
    p,q=random.choice(xs),random.choice(xs)
    delta=abs(p-q)
    if delta: worst_pair=max(worst_pair,abs((2*T(p)-p)-(2*T(q)-q))/math.sqrt(delta))
trajectory=[]
p=R
for k in range(8):
    q=T(p)
    trajectory.append({'k':k,'p':p,'T_over_p_squared':q/(p*p) if p*p else None})
    p=q
out={'seed':20261011,'grid_size':len(xs),'random_pair_checks':50000,'max_prox_equation_error':max(errs),'max_EB_identity_error':worst_eb,'max_anchor_ratio_bound_1':worst_anchor,'max_pair_ratio_bound_1':worst_pair,'max_same_window_ratio_bound_9_over_16':worst_compat,'trajectory':trajectory}
assert max(errs)<1e-14 and worst_eb<1e-14
assert worst_anchor<=1 and worst_pair<=1 and worst_compat<=9/16+1e-14
out['python']=sys.version
out['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
Path(__file__).with_name('optimization_candidate_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
