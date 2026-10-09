#!/usr/bin/env python3
"""Exact algebra and high-precision boundary checks; finite checks are not proof."""
from fractions import Fraction as Q
from decimal import Decimal as D, localcontext
from itertools import product
from math import factorial
from pathlib import Path
import json, platform
N=12

def binomial(a,n):
    out=Q(1)
    for k in range(n): out*=a-k
    return out/factorial(n)

def mul(a,b):
    c=[Q(0)]*(N+1)
    for i in range(N+1):
        for j in range(N+1-i): c[i+j]+=a[i]*b[j]
    return c

def symmetric_series(p):
    u=[binomial(p,k) if k>0 and k%2==0 else Q(0) for k in range(N+1)]
    out=[Q(1)]+[Q(0)]*N; term=out[:]
    for m in range(1,N+1):
        term=mul(term,u)
        for k in range(N+1): out[k]+=binomial(1/p,m)*term[k]
    return out

def verify_moments():
    count=0; smallest=None; endpoint_zero=0
    ps=[Q(11,10),Q(6,5),Q(4,3),Q(7,5),Q(3,2)]
    for n in [2,3,4]:
      for masses in product([1,2,3],repeat=n):
       weights=[Q(a,sum(masses)) for a in masses]
       for values in product([-2,-1,0,1,2],repeat=n):
        mean=sum(w*r for w,r in zip(weights,values))
        ss=[r-mean for r in values]
        mu={k:sum(w*s**k for w,s in zip(weights,ss)) for k in [2,3,4]}
        if mu[2]==0: continue
        pearson=mu[4]-mu[2]**2-mu[3]**2/mu[2]
        squares=sum(w*(s*s-mu[2]-mu[3]*s/mu[2])**2 for w,s in zip(weights,ss))
        assert pearson==squares and pearson>=0
        for p in ps:
          c2=(p-1)*mu[2]/2
          c3=(p-1)*(p-2)*mu[3]/6
          c4=(p-1)*(p-2)*(p-3)*mu[4]/24-(p-1)**3*mu[2]**2/8
          a=c3/c2
          assert c3-a*c2==0
          reduced=c4-c3*c3/c2
          lower=(p-1)*((3-2*p)*(p+1)*mu[2]**2/24+(2-p)*(p+1)*mu[3]**2/(72*mu[2]))
          assert reduced-lower==(p-1)*(p-2)*(p-3)*pearson/24
          assert reduced>=lower>=0
          if p<Q(3,2): assert reduced>0
          if reduced==0:
            assert p==Q(3,2) and mu[3]==0 and pearson==0
            assert all(s*s==mu[2] for s in ss)
            plus=sum(w for w,s in zip(weights,ss) if s>0)
            assert plus==Q(1,2)
            endpoint_zero+=1
          count+=1
          if smallest is None or reduced<smallest: smallest=reduced
    return {'cases':count,'endpoint_zero_cases':endpoint_zero,'smallest_C4':str(smallest),'all_checks_passed':True}

def dpow(a,q):
    return (a.ln()*q).exp()

def precision_checks(prec):
  with localcontext() as ctx:
    ctx.prec=prec
    p=D(3)/2; R=dpow(D(2),1/p)
    endpoint=[]
    for k in [1,2,3,4]:
      t=D(10)**(-k)
      norm=dpow(dpow(1+t,p)+dpow(1-t,p),1/p)
      ratio=(norm/R-1-t*t/4)/(t**6)
      assert ratio>0
      endpoint.append({'t':str(t),'norm_positive_sixth_ratio':str(ratio)})
    # Automatic strict-complementarity boundary: equality forces descent.
    comp=[]
    for k in [2,4,6]:
      t=D(10)**(-k)
      delta_phi=t*t/2-(dpow(1+dpow(t,p),1/p)-1)
      assert delta_phi<0
      comp.append({'t':str(t),'objective_delta':str(delta_phi),'scaled_negative':str(delta_phi/dpow(t,p))})
    # p>3/2 construction; high radial curvature makes reduced quartic positive.
    p=D(5)/3; R=dpow(D(2),1/p); alpha=D(10)
    c2=(p-1)/2; c4=-(p-1)*(2*p-3)*(p+1)/24
    beta=R*c2; K=-R*c4-beta*beta/(4*alpha)
    assert K>0
    above=[]
    for k in [1,2,3,4]:
      t=D(10)**(-k)
      def norm(h): return dpow(dpow(1+h+t,p)+dpow(1+h-t,p),1/p)
      def dh(h):
        u=1+h+t; v=1+h-t; total=dpow(u,p)+dpow(v,p)
        return 2*alpha*h+R-(dpow(u,p-1)+dpow(v,p-1))*dpow(total,1/p-1)
      lo=-t*t; hi=t*t
      assert dh(lo)<0<dh(hi)
      for _ in range(prec*4):
        mid=(lo+hi)/2
        if dh(mid)<0: lo=mid
        else: hi=mid
      h=(lo+hi)/2
      delta_phi=alpha*h*h+beta*t*t-(norm(h)-R-R*h)
      assert delta_phi>0
      above.append({'t':str(t),'h_min':str(h),'reduced_objective_over_t4':str(delta_phi/t**4),'K_limit':str(K)})
    # Conservative whole-resolvent certificate for A=I, b=(1,0), xbar=(1,0).
    rho=D(1)/16; lam=D(1)/100; radius=D(1)/250; m=D(1); delta=D(1)
    L=D(2).sqrt()+dpow(D(2),D(1)/6)
    M=rho/4+L
    B=rho+(rho/(1-rho)).sqrt()
    assert B<1-delta/2
    assert lam*M<rho/2 and radius<rho/4 and radius<lam*delta/2
    factor=1/(1+lam*m)
    # Identified full resolvent is y=((p1+lambda)/(1+lambda),0).
    algebra=[]
    for e1,e2 in product([D(-1)/1000,D(0),D(1)/1000],repeat=2):
      inp1=1+e1; inp2=e2; y=(inp1+lam)/(1+lam)
      assert abs(inp1-(y+lam*(y-1)))<D(10)**(-prec+5)
      assert abs(inp2/lam)<delta/2
      assert abs(y-1)<=factor*(e1*e1+e2*e2).sqrt()+D(10)**(-prec+5)
      # Reverse-check exact contraction squared in rational arithmetic.
      q_e1=Q(str(e1)); q_e2=Q(str(e2)); q_lam=Q(1,100)
      q_y=(1+q_e1+q_lam)/(1+q_lam)
      assert (q_y-1)**2 <= (q_e1*q_e1+q_e2*q_e2)/(1+q_lam)**2
      algebra.append([str(e1),str(e2),str(y)])
    return {'precision':prec,'endpoint_p_3_2':endpoint,'strict_complement_boundary':comp,'above_threshold_p_5_3':above,'full_resolvent_example':{'rho':str(rho),'lambda':str(lam),'basin_radius':str(radius),'off_support_bound':str(B),'global_output_displacement_budget':str(lam*M),'q':str(factor),'inputs_checked':algebra}}

series=symmetric_series(Q(3,2))
assert series[2]==Q(1,4) and series[4]==0 and series[6]==Q(1,192)
for p in [Q(4,3),Q(3,2),Q(5,3),Q(2)]:
  cs=symmetric_series(p)
  assert cs[4]==-(p-1)*(2*p-3)*(p+1)/24
out={'python':platform.python_version(),'arithmetic':'fractions.Fraction exact; decimal 60/100 digit independent precision checks','seed':None,'symmetric_p_3_2_series':{str(k):str(c) for k,c in enumerate(series) if c},'moment_verification':verify_moments(),'precision_verification':[precision_checks(60),precision_checks(100)],'scope':'Finite exact algebra and representative high-precision boundaries; the general theorem is the analytic proof in research/topics/sparse_recovery/automatic_regularity.md; mathematical reception and publication-priority audit are separate.'}
path=Path(__file__).with_name('automatic_regularity_results.json')
path.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'saved':str(path),'moment_cases':out['moment_verification']['cases'],'all_checks_passed':True}))
