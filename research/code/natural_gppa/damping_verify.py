"""Finite Decimal/Fraction checks of C257; analytic proof carries all Gamma."""
from decimal import Decimal as D, getcontext
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import sys

getcontext().prec = 80
K = D(1024)/169
rows, targeted_rows = [], []
for text in ('1e-12','1e-6','.001','.1','1','99','1000','1e6'):
    Gamma = D(text)
    A = 1+Gamma
    gap = 1-1/A.sqrt()
    R0 = min(D(1)/256, gap/4, A*gap*gap/32, (A-1)/(4*A+2))
    C0 = D(32)/(13*A)+K*R0
    C1 = 2*C0.sqrt()+D(3)/4*C0*C0.sqrt()
    C2 = (2+A*C1*R0.sqrt())**2
    c = A**D('.25')
    L = 2*A**D('-.375')
    kappa = (1+1/A.sqrt())/2
    H = L-2/A.sqrt()
    DL = C1*A.sqrt()+1+2/A+2*C1*R0.sqrt()
    bounds = {'preliminary':R0, 'anchor':(H/(2*DL))**2,
              'EB':((1-1/c)/(2*Gamma*C0.sqrt()))**2,
              'compatibility':((2*(kappa/c).sqrt()-L)/2)**2,
              'length_linear':(1-kappa)/4,
              'length_half':((1-kappa.sqrt())/(4*L))**2,
              'window':1/(4*L*L)}
    assert all(v>0 for v in bounds.values())
    R = min(bounds.values())
    epsilon = R+(2*R/A).sqrt()
    assert epsilon < gap
    assert epsilon < D(25)/256
    assert R/A+epsilon*epsilon < D(1)/16
    assert A*(1-R)**2 > 1+R
    anchor = 2/A.sqrt()+DL*R.sqrt()
    EB = 1/(1-Gamma*(C0*R).sqrt())
    compatibility = c*(L+R.sqrt())**2/4
    budget = R/(2*(1-kappa))+L*R.sqrt()/(2*(1-kappa.sqrt()))
    rho_sq = C0*R+(1+C0)**2*R*R
    window = (R+L*R.sqrt())/2
    assert anchor < L and EB < c and compatibility < kappa
    assert budget < D('.5')-R and rho_sq < 1 and window < 1
    rows.append({'Gamma':text,'R0':str(R0),'R':str(R),'minimum_radius_bound':min(bounds,key=bounds.get),'c':str(c),'L':str(L),'kappa':str(kappa),'EB_upper':str(EB),'anchor_upper':str(anchor),'compatibility_upper':str(compatibility),'length_budget':str(budget),'sharp_asymptotic_distance_factor':str(1/A),'C2':str(C2)})
    for fraction in (D('.1'),D('.9')):
        kt = 1/A+fraction*(1-1/A)
        ct, Lt = (kt*A)**D('.25'),2/A.sqrt()*(kt*A)**D('.125')
        Ht = Lt-2/A.sqrt()
        Rt = min(R0,(Ht/(2*DL))**2,((1-1/ct)/(2*Gamma*C0.sqrt()))**2,
                 ((2*(kt/ct).sqrt()-Lt)/2)**2,(1-kt)/4,
                 ((1-kt.sqrt())/(4*Lt))**2,1/(4*Lt*Lt))
        assert Rt>0 and ct*Lt*Lt/4 < kt
        assert 2/A.sqrt()+DL*Rt.sqrt() < Lt
        assert 1/(1-Gamma*(C0*Rt).sqrt()) < ct
        assert ct*(Lt+Rt.sqrt())**2/4 < kt
        assert Rt/(2*(1-kt))+Lt*Rt.sqrt()/(2*(1-kt.sqrt())) < D('.5')-Rt
        targeted_rows.append({'Gamma':text,'target_fraction_above_sharp_factor':str(fraction),'target_kappa':str(kt),'R':str(Rt)})

# Entire-center-fiber threshold at A<0: maximum at r=4/3.
r = Q(4,3)
assert (r-1)/r**4 == Q(27,256)
assert ((r-1)/r**4) == (Q(3,16)**2*3)

def radial_bisect(fun, lo, hi):
    for _ in range(280):
        mid = (lo+hi)/2
        if fun(mid)>0:
            hi = mid
        else:
            lo = mid
    return (lo+hi)/2

negative = []
for u in (D('.0001'),D('.01'),D('.1')):
    assert u**3 < D(27)/256
    r = radial_bisect(lambda r:r-1-u**3*r**4,D(1),D(4)/3)
    cosine = 1-u/2
    sine = (1-cosine*cosine).sqrt()
    # x=(r,0), xprev=(r*cos(theta),-r*sin(theta)); p=z*(x-xprev).
    z = r*u.sqrt()
    p = (z*r*(1-cosine),z*r*sine)
    pprev = (cosine*p[0]+sine*p[1],-sine*p[0]+cosine*p[1])
    P = (p[0]**2+p[1]**2).sqrt()
    hx = (p[0]/P.sqrt(),p[1]/P.sqrt())
    g = ((r-1).sqrt(),D(0))
    A = 1-u
    reverse_errors = [abs(hx[0]-r*(1-cosine)),abs(hx[1]-r*sine),abs(pprev[0]-A*p[0]-g[0]),abs(pprev[1]-A*p[1]-g[1])]
    assert max(reverse_errors) < D('1e-65')
    negative.append({'Gamma':str(-u),'radius':str(r),'constant_position_step':str(z),'max_reverse_error':str(max(reverse_errors))})

center_bounds = []
for Gamma in (D('1e-9'),D('.1'),D(1),D(3)):
    A = 1+Gamma
    s = radial_bisect(lambda r:2*A*A*r**3+(1-2*A)*r-1,1/A.sqrt(),D(1))
    B = A*s*s-1
    radius = ((s-1)**2+B*B).sqrt()
    assert D('.5') < s < 1 and B > 0
    assert abs(-B+A*s*s-1) < D('1e-70')
    center_bounds.append({'Gamma':str(Gamma),'input_position_radius':str(s),'Rcenter':str(radius),'Rcenter_over_Gamma':str(radius/Gamma)})

out = {'python':sys.version.split()[0],'precision_digits':80,'randomness':'none','positive_tuples':rows,'targeted_kappa_tuples':targeted_rows,'center_appearance_boundaries':center_bounds,'negative_rotation_orbits':negative,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Eight default positive damping tuples, sixteen targeted rates, four center boundaries and three reverse-substituted negative rotations; all-real-Gamma coverage and sharp iff threshold rely on the analytic proof.'}
Path(__file__).with_name('damping_results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'positive_tuples':len(rows),'targeted_kappa_tuples':len(targeted_rows),'center_boundaries':len(center_bounds),'negative_rotation_orbits':len(negative),'script_sha256':out['script_sha256']},indent=2))
