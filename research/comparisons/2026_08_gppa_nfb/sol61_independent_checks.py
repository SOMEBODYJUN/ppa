"""Finite arithmetic checks supporting the independent audit; not universal proofs."""
from fractions import Fraction as F
from pathlib import Path
import json

out = {}
# Same original nonmonotone C199 graph: normal q=1/8, exponent 2/3.
h, q, K = F(3, 10), F(1, 8), F(2, 3)
t, y = F(0), F(1, 8)
anchor_t = t + K * F(1, 4)
steps = []
for k in range(12):
    ya = F(1, 2 ** (2*(k+1)))
    y_new, ya_new = y*q, ya*F(1, 4)
    t_new = t+2*ya_new
    v = (-F(1, 5)*ya, h*y)
    v_new = (-F(1, 5)*ya_new, h*y_new)
    residual = (-2*ya_new, 7*y_new)
    assert tuple(v[i]-v_new[i] for i in range(2)) == tuple(h*f for f in residual)
    assert v == (h*(t-anchor_t), h*y)
    assert t_new+K*ya_new == anchor_t
    steps.append({'k': k, 't':str(t), 'y':str(y)})
    t, y = t_new, y_new
out['c199_exact_ordinary_warped_steps'] = steps
# Source NFB equation (3.8), retaining the last rho term at zeta=0.
rho, tau, beta, zeta_m = -F(11,10), F(3), F(100), F(1,3)
delta = 1 - (tau+2*rho)**2/(2*tau*(beta+rho)) + 2*rho*tau*zeta_m**2
assert delta == F(788,2967) and delta > 0
assert F(1,10)+rho == -1
out['c202_exact_source_descent'] = str(delta)
# Same cap trajectory is also an affine strongly monotone PPA after changing F.
y0, eta, xi = F(1,64), -F(1), F(0)
invariant = xi+F(1,4)
y = y0
orbit = []
for k in range(16):
    root = F(1,2**(k+3))
    cap_next = (xi+root, eta, y/F(4))
    affine_next = ((xi+invariant)/2, (eta-1)/2, y/F(4))
    assert cap_next == affine_next
    assert xi-invariant == -2*root
    orbit.append({'k':k,'xi':str(xi),'eta':str(eta),'y':str(y)})
    xi,eta,y = cap_next
out['same_orbit_changed_affine_graph'] = orbit
# Exact original-graph anchor failure at points converging to the same zero.
anchor_rows=[]
for j in range(1,13):
    eps=F(1,16**j)
    tangential=F(1,2**j)  # eps^(1/4)
    root=F(1,4**j)        # eps^(1/2)
    pairing=-2*tangential*root+3*eps**2
    residual_sq=4*eps+9*eps**2
    anchor_rows.append({'j':j,'epsilon':str(eps),'pairing_over_residual_sq':str(pairing/residual_sq)})
assert all(F(r['pairing_over_residual_sq']) < 0 for r in anchor_rows)
assert F(anchor_rows[-1]['pairing_over_residual_sq']) < -2000
out['cap_legal_near_zero_anchor_sequence'] = anchor_rows
# A non-diagonal positive product metric: residual lift (f,0) ignores arbitrary auxiliary base displacement.
inv = ((F(2),F(1)), (F(1),F(2)))
f=F(3,7)
for aux in (F(0),F(1),F(10**9)):
    base=(F(2,5),aux); lifted=(f,F(0))
    pairing=sum(base[i]*lifted[i] for i in range(2))
    norm_sq=sum(lifted[i]*inv[i][j]*lifted[j] for i in range(2) for j in range(2))
    assert pairing == F(2,5)*f and norm_sq == 2*f*f
out['standard_lift_auxiliary_displacement_irrelevant'] = True
out['proof_boundary'] = 'Finite exact arithmetic checks; partition, arbitrary kernels/decompositions, and priority claims require the audit proof and sources.'
path=Path(__file__).with_name('sol61_independent_results.json')
path.write_text(json.dumps(out,indent=2)+'\n')
print('PASS: independent finite arithmetic checks; exact results in '+str(path))
