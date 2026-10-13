#!/usr/bin/env python3
"""Finite boundary checks for secondary/rejected chapter-four candidates."""
from pathlib import Path
import json
import runpy
import numpy as np

HERE=Path(__file__).resolve().parent
runpy.run_path(str(HERE/'classical.py'),run_name='__main__')
runpy.run_path(str(HERE/'tilt.py'),run_name='__main__')
rng=np.random.default_rng(20261013)
A=np.diag([1.,1.,0.])

def cubic_inverse(X):
    P,s,Q=np.linalg.svd(X,full_matrices=False)
    return (P*np.cbrt(s))@Q

max_error=0.
max_excess=0.
for j in range(500):
    Q,_=np.linalg.qr(rng.normal(size=(3,3)))
    P,_=np.linalg.qr(rng.normal(size=(2,2)))
    offsets=rng.normal(size=2)
    offsets*=.02/max(1.,np.linalg.norm(offsets))
    C=P@np.diag(1+offsets)@Q[:2]
    b=rng.normal(size=3)
    b*=.02/max(1.,np.linalg.norm(b))
    X=np.vstack([C,b])
    Y=cubic_inverse(A@X)
    P2,s,V=np.linalg.svd(C,full_matrices=False)
    anchor=np.vstack([P2@V,np.zeros(3)])
    d=np.linalg.norm(X-anchor)
    dplus=np.linalg.norm(Y-anchor)
    residual=np.linalg.norm((Y@Y.T-A)@Y)
    q=np.linalg.norm(A@(Y-X))
    equation=np.linalg.norm(Y@Y.T@Y-A@X)
    max_error=max(max_error,equation)
    excess=max(np.linalg.norm(A@(2*Y-X-anchor))-.5*np.linalg.norm(A@(X-anchor)),
               dplus-(2/3)*residual,dplus-.5*d,
               np.linalg.norm(Y-X)-np.hypot(d,q))
    max_excess=max(max_excess,excess)
    assert equation<1e-12 and excess<1e-12
# Every partial-isometry rank is retained by the full relation.
rank_fixed=[]
for rank in (0,1,2):
    X=np.zeros((3,3))
    for i in range(rank): X[i,i]=1
    err=np.linalg.norm(cubic_inverse(A@X)-X)
    assert err<1e-12
    rank_fixed.append({'rank':rank,'fixed_error':err})
# Hard Procrustes: all signed polar branches at a target zero input.
B=np.diag([2.,1.])
branch_errors=[]
for sign1 in (-1,1):
    for sign2 in (-1,1):
        Q=np.diag([sign1,sign2])
        normal=Q.T@(B+np.eye(2))
        error=np.linalg.norm(normal-normal.T)
        assert error==0
        branch_errors.append({'signs':[sign1,sign2],'normal_symmetry_error':error})
# Singular combined input has the entire O(2) stationary fiber.
for angle in (0.,.1,1.,3.141592653589793):
    Q=np.array([[np.cos(angle),-np.sin(angle)],[np.sin(angle),np.cos(angle)]])
    normal=Q.T@(B-B)
    assert np.linalg.norm(normal)==0
out={'scope':'finite checks only; analytic full-fiber/degree proofs are in screening report',
     'seed':20261013,'numpy':np.__version__,'rank_two_tube_samples':500,
     'rank_two_max_equation_error':max_error,'rank_two_max_positive_certificate_excess':max_excess,
     'all_partial_isometry_rank_examples':rank_fixed,'procrustes_target_input_branches':branch_errors,
     'procrustes_singular_input_fiber_examples':4,
     'classical_results':'classical.json','tilted_results':'scalar_tilt_results.json'}
(HERE/'results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
