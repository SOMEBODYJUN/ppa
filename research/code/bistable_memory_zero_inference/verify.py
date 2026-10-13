#!/usr/bin/env python3
"""Exact common scalar gates and finite full-PPA reverse diagnostics.

Existence of the six roots and global regularity are analytic in the card.
The multistart root list here is not complete and is not their proof.
"""
from fractions import Fraction as Q
from pathlib import Path
import json
import platform
import numpy as np
import scipy
from scipy.optimize import root

PATTERNS = np.array([[1]*8, [1]*4+[-1]*4, [1,1,-1,-1,1,1,-1,-1]], dtype=float).T
P = PATTERNS@PATTERNS.T/8
W = P-3*np.eye(8)/8
GAMMA, LAM = .3, 16/19
B_NUMS = [-7,4,2,-3,6,-5,1,8]
b = np.array(B_NUMS)/1000

def f(u):
    return u**3-u-GAMMA*W@u-b

def jac(u):
    return np.diag(3*u*u-1)-GAMMA*W

def prox(x, initial=None):
    if np.array_equal(x, -LAM*b):
        return np.zeros(8)
    start = np.cbrt((x+LAM*b)/LAM) if initial is None else initial
    out = root(lambda u:u+LAM*f(u)-x, start,
               jac=lambda u:np.eye(8)+LAM*jac(u), tol=1e-12)
    assert np.linalg.norm(out.x+LAM*f(out.x)-x) < 2e-10*(1+np.linalg.norm(x))
    return out.x

def main():
    lo, hi, rho = Q(217,200), Q(109,100), Q(1,20)
    assert lo*lo < Q(19,16) < hi*hi
    assert 3*(lo-rho)**2-Q(19,16) > 2
    assert 3*(hi+rho)**2-Q(71,80) < Q(13,4)
    assert Q(204,10**6) < Q(3,200)**2
    assert Q(1,100)+Q(3,400) < rho
    assert Q(1,25)+Q(3,400) < rho
    assert Q(57,128) < Q(1,2)
    assert Q(33,71) < Q(1,2)
    assert Q(3,200) < Q(1,50)
    assert Q(29,25)**3-Q(107,80)*Q(29,25) > Q(8,1000)
    assert np.array_equal(P@P,P)
    assert np.allclose((1-LAM)*np.eye(8)-LAM*GAMMA*W,(24/95)*(np.eye(8)-P))
    assert all(W[i,j] != 0 for i in range(8) for j in range(8) if i != j)
    # In Z_(3), GAMMA=3/10 is zero and the constant Jacobian is -I.
    assert (Q(3,10).numerator*pow(10,-1,3)) % 3 == 0
    assert all(Q(k,1000).denominator % 3 for k in B_NUMS)
    amplitude = np.sqrt(19)/4
    known = []
    for pattern in PATTERNS.T:
        for sign in [-1,1]:
            center = sign*amplitude*pattern
            out = root(f, center, jac=jac, tol=1e-12).x
            assert np.linalg.norm(f(out)) < 1e-11
            assert np.linalg.norm(out-center) < .0075
            assert np.linalg.eigvalsh(jac(out))[0] > 2
            known.append(out)
    rng = np.random.default_rng(20261013)
    local_max = 0.
    for p in known:
        for _ in range(64):
            d = rng.normal(size=8);d = d/np.linalg.norm(d)*.01*rng.uniform(.2,1)
            x = p+d;y = prox(x,p)
            assert np.linalg.norm(2*y-x-p) <= .5*np.linalg.norm(d)+1e-10
            assert np.linalg.norm(y-p) <= .5*np.linalg.norm(f(y))+1e-10
            local_max = max(local_max,float(np.linalg.norm(y-p)/np.linalg.norm(d)))
    inputs = [np.zeros(8),-LAM*b,np.ones(8)*2,-np.ones(8)*2,
              np.linspace(-1e4,1e4,8)]
    inputs += [rng.uniform(-2,2,8) for _ in range(100)]
    reverse = []
    for x in inputs:
        y = prox(x)
        reverse.append(float(np.linalg.norm(y+LAM*f(y)-x)/(1+np.linalg.norm(x))))
    for p in PATTERNS.T:
        for t in [-1.,-.01,0.,.01,1.]:
            y = t*p;x = -LAM*b+LAM*t**3*p
            assert np.linalg.norm(y+LAM*f(y)-x) < 1e-12
    super_lam = 1.
    rad = np.sqrt(19/16-1/super_lam)
    fiber = [np.zeros(8)]+[sign*rad*p for p in PATTERNS.T for sign in [-1,1]]
    assert len(fiber) == 7
    assert all(np.linalg.norm(y+super_lam*f(y)+super_lam*b)<1e-12 for y in fiber)
    observed = []
    for _ in range(300):
        u = root(f,rng.uniform(-1.4,1.4,8),jac=jac,tol=1e-11).x
        if np.linalg.norm(f(u))<1e-9 and all(np.linalg.norm(u-v)>1e-5 for v in observed):
            observed.append(u)
    data = {'scope':'analytic six-root/common-window gates plus finite diagnostics; no complete real-root classification',
            'environment':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__},
            'model':{'N':8,'gamma':'3/10','lambda':'16/19','patterns':PATTERNS.T.astype(int).tolist(),
                     'bias_numerators':B_NUMS,'bias_denominator':1000},
            'uniform_certificate':{'m':2,'rho':'1/20','target_U_radius':'3/100','R':'1/100',
                                   'L':'1/2','psi':'t/2','bar_t':1,'kappa':'1/2',
                                   'Theta':'3t/2','budget_left':'3/200','budget_right':'1/50'},
            'predicted':{'known_minima':6,'total_index':1,'unseen_index':-5,
                         'unseen_real_root_lower_bound':5,'unseen_count_parity':'odd',
                         'complex_root_count':6561,'complex_count_is_not_real_count':True},
            'known_root_numeric_reverse':[{'point':p.tolist(),'true_residual':float(np.linalg.norm(f(p))),
                                           'min_hessian_eigenvalue_numeric':float(np.linalg.eigvalsh(jac(p))[0])}
                                          for p in known],
            'diagnostics':{'full_prox_inputs':len(inputs),'local_inputs':384,
                           'max_normalized_reverse_error':max(reverse),'max_local_distance_ratio':local_max,
                           'observed_multistart_roots':len(observed),
                           'observed_negative_index_roots':sum(np.linalg.det(jac(p))<0 for p in observed),
                           'observation_is_not_exhaustive':True,'supercritical_complete_fiber_witnesses':7}}
    # Convert NumPy boolean-count integer before serializing.
    data['diagnostics']['observed_negative_index_roots'] = int(data['diagnostics']['observed_negative_index_roots'])
    path = Path(__file__).with_name('results.json')
    path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(data['diagnostics'],ensure_ascii=False,indent=2))

if __name__ == '__main__':
    main()
