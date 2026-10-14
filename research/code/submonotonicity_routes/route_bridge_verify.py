#!/usr/bin/env python3
"""Finite arithmetic and back-substitution; analytic reports carry quantifiers."""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import math
import platform
import numpy as np

def main():
    out={"scope":"finite verification only; no exhaustive numerical theorem",
         "python":platform.python_version(),"numpy":np.__version__,
         "seed":20261014,"float":"binary64","tolerance":2e-11}
    rng=np.random.default_rng(20261014)
    cases=0
    # Exact same-graph reparameterization, including non-monotone borders.
    for tau in (Q(0),Q(1,100),Q(1,4),Q(1,2),Q(3,4),Q(3),Q(100)):
        r=2*tau/(1+2*tau)
        assert 0<=r<1 and (1+r)/(1-r)==1+4*tau
        for a,b in [(np.zeros(3),np.zeros(3)),
                    (np.ones(3),-np.ones(3))]+[
                    (rng.normal(size=3),rng.normal(size=3)) for _ in range(100)]:
            z=a+b
            dot=float(np.dot(a,b))
            Elt=dot+float(tau)*np.dot(z,z)
            Eoi=dot+float(r/2)*(np.dot(a,a)+np.dot(b,b))
            assert abs(Elt-float(1+2*tau)*Eoi)<2e-11
            cases+=1
    out["LT_OI_same_graph_cases"]=cases
    out["LT_OI_parameter_map"]="r=2 tau/(1+2 tau); tau=0 is monotone endpoint"
    # Non-tied semimonotonicity: shifted Cayley ball, not ordinary RL.
    count=0
    for m,r in ((0,0),(-.2,-.2),(-.1,.3),(.1,.2),(-1.2,.4)):
        A=1+m+r
        if A<=0: continue
        for _ in range(100):
            a,b=rng.normal(size=3),rng.normal(size=3)
            z,c=a+b,a-b
            original=np.dot(a,b)-m*np.dot(a,a)-r*np.dot(b,b)
            shifted=(1-4*m*r)/A**2*np.dot(z,z)-np.dot(
                c+(m-r)/A*z,c+(m-r)/A*z)
            assert abs(4*original/A-shifted)<2e-11
            count+=1
    out["shifted_Cayley_identity_cases"]=count

    # Same stationary resolvent; sharp radial RL/EB loses direction correlation.
    lam=Q(3);K=Q(100);L=Q(2)
    energy_squared=(1+L*L)/(2*(1+(lam/K)**2))
    direct=K*(1+L)/(2*lam)
    co_squared=K*K/(K*K+lam*(lam-2))
    actual=Q(100,103)
    assert energy_squared==Q(25000,10009)>1
    assert direct==50
    assert co_squared==Q(10000,10003)<1
    F=np.diag([-1.,.01])
    J=np.diag([-.5,100/103])
    C=2*J-np.eye(2)
    assert np.linalg.norm(C,2)==2
    for x in (np.zeros(2),np.array([1.,0.]),np.array([0.,1.]),
              np.array([100.,-100.]),np.array([1e-10,-1e-10])):
        y=J@x
        assert np.linalg.norm(y+float(lam)*F@y-x)<2e-11
        assert np.linalg.norm(y)<=float(actual)*np.linalg.norm(x)+2e-11
        assert np.dot(y,F@y)+np.dot(F@y,F@y)>=-2e-11
    out["same_algorithm_direction_loss"]={
        "F":"diag(-1,1/100)","lambda":"3","S":"{0}",
        "J":"diag(-1/2,100/103)","sharp_reflection_L":"2",
        "sharp_true_EB_K":"100","direct_factor":str(direct),
        "energy_factor_squared":str(energy_squared),
        "cohypomonotone_certificate_squared":str(co_squared),
        "actual_contraction":str(actual),
        "global_argmin_prox_exists":False,
        "prox_objective_first_quadratic_coefficient":str(-Q(1,2)+1/(2*lam))}

    # Entire branch policies, both signs, depth 10; analytic geometric bound separate.
    policy_witnesses=0
    for start in (Q(-2),Q(0),Q(3)):
        layer=[start]
        for _ in range(10):
            new=[]
            for x in layer:
                for alpha in (Q(1,2),Q(2)):
                    y=x/(1+alpha)
                    assert y+alpha*y==x
                    assert abs(y)<=Q(2,3)*abs(x)
                    assert abs(y)/2<=abs(alpha*y)
                    new.append(y);policy_witnesses+=1
            layer=new
    out["complete_multivalued_policies"]={
        "F":"{x/2,2x}","lambda":"1","depth":10,
        "transition_witnesses":policy_witnesses,
        "all_graph_RL_at_same_input":"fails: J(1)={1/3,2/3}",
        "anchored_C250_energy_squared":str(Q(4,9))}
    assert (1+Q(1,9))/(2*(1+Q(1,4)))==Q(4,9)

    # Single weak-Minty zero anchor does not absorb every full zero.
    roots=(Q(1),Q(1,4),Q(3,4))
    for y in roots:
        Fy=y*(y-1)**2
        assert y+Q(16,3)*Fy==1
        assert y*Fy>=0
    out["single_anchor_vs_full_zeros"]={
        "F":"x(x-1)^2","lambda":"16/3","S":"{0,1}",
        "J_at_1":[str(v) for v in roots],"full_zero_1_absorbing":False}

    # True residual and distance contraction alone do not control zero-fiber drift.
    for u,v in ((0.,0.),(0.,100.),(2.,-3.),(-2.,-3.)):
        for b in (0.,-.25,-1.):
            y=np.array([u/2,v-b])
            w=np.array([u/2,b])
            assert np.linalg.norm(y+w-np.array([u,v]))<2e-11
            assert abs(y[0])==abs(u)/2
            assert abs(y[0])<=np.linalg.norm(w)
    out["physical_zero_drift"]={
        "F":"{u} x [-1,0]","S":"{0} x R",
        "J":"{a/2} x [b,b+1]","true_residual":"|u|",
        "all_output_distance_factor":"1/2",
        "legal_zero_orbit":"(0,k), k>=0",
        "convergence_to_a_point":False}

    # General primal gauge plus strong EB and full coverage can still fail.
    grid=np.linspace(-4,4,41)
    def cusp(y):
        return -math.copysign(math.sqrt(abs(y)),y) if y else 0.
    def full_cusp_fiber(x):
        roots=[]
        for sign in (1.,-1.):
            D=1+4*sign*x
            if D<0: continue
            for q in ((1+math.sqrt(D))/2,(1-math.sqrt(D))/2):
                if q>=0: roots.append(sign*q*q)
        return sorted(set(roots))
    for x in grid:
        fiber=full_cusp_fiber(float(x))
        assert fiber
        for y in fiber:
            assert abs(y+cusp(y)-x)<2e-11
            assert abs(y)-abs(cusp(y))**2<2e-11
    assert full_cusp_fiber(0.)==[-1.,0.,1.]
    for a in grid:
        for b in grid:
            dot=(a-b)*(cusp(a)-cusp(b))
            assert dot>=-math.sqrt(2)*abs(a-b)**1.5-2e-11
    state=0.
    trace=[]
    for _ in range(10):
        y=max(full_cusp_fiber(state))
        assert y>state
        trace.append(y);state=y
    out["primal_gauge_failure"]={
        "F":"-sgn(x)sqrt(|x|)","lambda":"1",
        "gauge":"sqrt(2)t^(3/2)","true_EB":"|x|=r_F(x)^2",
        "complete_J_zero":[-1,0,1],
        "legal_positive_trace":trace,
        "full_coverage_verified_on_grid":True,
        "universal_divergence":"analytic positive branch is strictly increasing and has no positive finite fixed point"}

    out["script_sha256"]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    Path(__file__).with_name("route_bridge_output.json").write_text(
        json.dumps(out,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({"status":"passed","same_graph_cases":cases,
                      "shifted_cases":count,"policy_transitions":policy_witnesses,
                      "output":"research/code/submonotonicity_routes/route_bridge_output.json"}))

if __name__=="__main__":
    main()
