#!/usr/bin/env python3
"""Independent exact NFB arithmetic. Finite checks supplement symbolic proofs."""
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
import json
import math

BASE=Path(__file__).resolve().parent

def delta(tau, theta, beta, rho, zeta, zm, eta):
    rh=min(rho,Q(0))
    return (2-theta-2*eta*zeta
       -(tau+2*rh)**2/(2*tau*(beta+rh*(1+zeta/tau)))
       +2*rh*tau*((zeta/tau+zm)**2+4*zeta/tau))

def scalar_case(name, f, ordinary_step, c, m, s, tau, theta, rho, mu, beta, zeta, u_factor):
    a=f-c
    assert beta>0 and rho>-beta and mu>0 and 0<theta<2 and 0<=zeta<Q(1,2)
    assert a!= -m and f!= -1/ordinary_step
    assert c>=beta*c*c/s # exact source cocoercivity
    assert a>=mu*s+rho*a*a/s # anchored strong semimonotonicity
    assert abs(tau*m-s)/s<=zeta
    rh=min(rho,Q(0))
    assert tau> -zeta*rh/(beta+rh)
    zm=abs(m)/s
    eta=Q(1) if theta>=1 and s-tau*m>=0 else 1+abs(1-theta)
    dec=delta(tau,theta,beta,rho,zeta,zm,eta)
    assert dec>0
    factor=1/(1+ordinary_step*f)
    x=Q(7,5); u=u_factor*x
    for k in range(24):
        p=(m*x-c*x+u/tau)/(m+a)
        un=(tau*m-s)*(p-x)
        xn=(1-theta)*x+theta*p
        assert xn==factor*x
        assert un==u_factor*xn
        x,u=xn,un
    return {'name':name,'delta_exact':str(dec),'delta_float':float(dec),
            'ordinary_factor_exact':str(factor),'mu':str(mu),'rho':str(rho),
            'physical_factor':float(abs(factor)),'all_source_scalar_gates':True,
            '24_step_identity':True}

cases=[
scalar_case('negative_identity',Q(-1),Q(3),Q(0),Q(1,3),Q(1),Q(3),Q(1),Q(-11,10),Q(1,10),Q(100),Q(0),Q(0)),
scalar_case('nonzero_forward',Q(2),Q(1),Q(1,2),Q(3,2),Q(3,2),Q(1),Q(1),Q(0),Q(1),Q(3),Q(0),Q(0)),
scalar_case('memory_compensation',Q(1),Q(1),Q(1,10),Q(9,10),Q(1),Q(1),Q(1),Q(0),Q(9,10),Q(10),Q(1,10),Q(1,10))]

rotation_delta=delta(Q(1),Q(1),Q(1),Q(-1,4),Q(0),Q(1),Q(1))
assert rotation_delta==Q(1,3)
x=(Q(3),Q(-2))
for k in range(24):
    # (I+K)^-1=(I-K)/2; K(x,y)=(-y,x)
    p=((x[0]+x[1])/2,(x[1]-x[0])/2)
    assert p[0]*p[0]+p[1]*p[1]==(x[0]*x[0]+x[1]*x[1])/2
    # PPA graph equation and source warped equation coincide.
    kp=(-p[1],p[0])
    assert (p[0]+kp[0],p[1]+kp[1])==x
    x=p
cases.append({'name':'rotation','delta_exact':str(rotation_delta),
              'physical_factor':1/math.sqrt(2),'strong_anchor_equality':True,
              '24_step_identity':True})

# Independently check the source (3.8)/(3.41)/(3.43) algebra.
cubic_checks=0
for tau in [Q(1,2),Q(1),Q(3),Q(7)]:
  for theta in [Q(1,2),Q(1),Q(3,2)]:
    for beta,rho in [(Q(1),Q(-1,4)),(Q(5),Q(-3,2)),(Q(2),Q(0))]:
      for zeta in [Q(0),Q(1,10),Q(1,3)]:
        for xi in [1-zeta,Q(1),1+zeta]:
          eta=1+abs(1-theta)
          if tau<=-zeta*rho/(beta+rho): continue
          zm=xi/tau
          cc=2-theta-2*(eta-4*rho)*zeta
          a0=4*rho*rho*zeta*(zeta+xi)**2
          a1=2*cc*rho*zeta-4*rho*rho+4*rho*(beta+rho)*(zeta+xi)**2
          a2=2*cc*(beta+rho)-4*rho
          pp=-tau**3+a2*tau*tau+a1*tau+a0
          assert delta(tau,theta,beta,rho,zeta,zm,eta)==pp/(2*tau*((beta+rho)*tau+rho*zeta))
          cubic_checks+=1

# Completion of squares with a non-diagonal, positive definite inverse metric.
Qm=((Q(2),Q(1,3)),(Q(1,3),Q(1)))
def quad(x): return sum(x[i]*Qm[i][j]*x[j] for i in range(2) for j in range(2))
assert Qm[0][0]>0 and Qm[0][0]*Qm[1][1]-Qm[0][1]**2>0
anchor_checks=0
for beta,rho in [(Q(1),Q(-1,4)),(Q(100),Q(-11,10)),(Q(2),Q(0)),(Q(3),Q(2))]:
  for f in [(Q(1),Q(2)),(Q(-3,5),Q(7,3)),(Q(0),Q(0))]:
    for c in [(Q(5),Q(-2)),(Q(1,7),Q(1,4)),(Q(0),Q(0))]:
      fc=tuple(f[i]-c[i] for i in range(2))
      rem=tuple(c[i]-rho/(beta+rho)*f[i] for i in range(2))
      lhs=rho*quad(fc)+beta*quad(c)
      rhs=beta*rho/(beta+rho)*quad(f)+(beta+rho)*quad(rem)
      assert lhs==rhs and lhs>=beta*rho/(beta+rho)*quad(f)
      anchor_checks+=1

# Exact -Id contraction boundary: lambda>2. No numerical inference.
boundaries=[]
for lam in [Q(1,2),Q(1),Q(3,2),Q(2),Q(5,2),Q(3),Q(100)]:
    if lam==1:
        boundaries.append({'lambda':str(lam),'resolvent':'not invertible'})
        continue
    fac=1/(1-lam)
    assert (abs(fac)<1)==(lam>2)
    boundaries.append({'lambda':str(lam),'ordinary_factor':str(fac),'contractive':abs(fac)<1})

# Numerical illustrations only; asymptotics in audit prove universal obstruction.
trends=[]
for eps in [1e-4,1e-8,1e-12,1e-16]:
    alpha=2/3; d=1/3
    pairing=-2*eps**(alpha+d)+7*eps**2
    residual_sq=4*eps**(2*alpha)+49*eps**2
    cap=(-2*eps**(.5+.25)+3*eps**2)/(4*eps+9*eps**2)
    sf=(-eps**(.25+.125)+eps**1.5-eps**2)/(eps**.5+(eps**.5-eps)**2)
    trends.append({'epsilon':eps,'natural_pairing_over_residual_sq':pairing/residual_sq,
                   'cap_pairing_over_residual_sq':cap,'superlinear_pairing_over_residual_sq':sf})

pdf=BASE/'sources/nfb_2608.22687v1.pdf'
assert sha256(pdf.read_bytes()).hexdigest()=='14db75596189d898d97aa9389b3e1a50bbe2ed70e207a3257d681cb4d01077b9'
results={'cases':cases,'cubic_exact_checks':cubic_checks,'square_exact_checks':anchor_checks,
         'negative_identity_boundaries':boundaries,'illustrations_only':trends,
         'source_pdf_sha256':sha256(pdf.read_bytes()).hexdigest(),
         'status':'PASS; no finite check proves the universal exclusion'}
(BASE/'sol61_nfb_results.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps({'status':results['status'],'cases':cases,'cubic_exact_checks':cubic_checks,
                  'square_exact_checks':anchor_checks},indent=2))
