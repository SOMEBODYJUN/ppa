"""Exact coefficient/edge-case checks accompanying the analytic manuscript proof.
No third-party dependencies. Numerical examples do not establish universal claims.
"""
from collections import defaultdict
from fractions import Fraction as Q
from pathlib import Path
import json

class P:
    # Sparse polynomial over Q[a,b,m,s]; verifies identities by coefficients.
    def __init__(self, terms=None):
        self.t = {k: Q(v) for k, v in (terms or {}).items() if v}
    @staticmethod
    def number(v): return P({(0,0,0,0): Q(v)})
    @staticmethod
    def var(i):
        k = [0]*4; k[i] = 1
        return P({tuple(k): Q(1)})
    def __add__(self, other):
        other = other if isinstance(other,P) else P.number(other)
        d = defaultdict(Q, self.t)
        for k,v in other.t.items(): d[k] += v
        return P(d)
    __radd__ = __add__
    def __neg__(self): return P({k:-v for k,v in self.t.items()})
    def __sub__(self, other): return self + (-other if isinstance(other,P) else -Q(other))
    def __rsub__(self, other): return -self + other
    def __mul__(self, other):
        other = other if isinstance(other,P) else P.number(other)
        d = defaultdict(Q)
        for k,v in self.t.items():
            for l,w in other.t.items(): d[tuple(x+y for x,y in zip(k,l))] += v*w
        return P(d)
    __rmul__ = __mul__
    def __pow__(self, n):
        result = P.number(1)
        for _ in range(n): result = result*self
        return result
    def is_zero(self): return not self.t

a,b,m,s = (P.var(i) for i in range(4))
A=1+m+s; B=m-s; T=1-m-s; Delta=1-4*m*s
c=a-b; d=a+b
checks={}
def check(name, predicate):
    assert predicate, name
    checks[name] = 'PASS'

check('semimonotonicity_to_Minty_polynomial_identity',
      (A*c**2+2*B*d*c-T*d**2-4*(m*a**2+s*b**2-a*b)).is_zero())
check('complete_square_discriminant_identity', (A*T+B**2-Delta).is_zero())
check('Cayley_ball_identity',
      ((A*c+B*d)**2-Delta*d**2-A*(A*c**2+2*B*d*c-T*d**2)).is_zero())
# Hilbert-space proof sums these scalar quadratic identities by coordinates.
# Universal parameter gates and triangle inequality are checked analytically.

lam=Q(1); slope=Q(1,2)
j=1/(1+lam*slope); L=abs(1-lam*slope)/(1+lam*slope); rho=1/slope
kd=rho*(1+L)/(2*lam); ke2=(1+L*L)*rho*rho/(2*(rho*rho+lam*lam))
check('maximal_monotone_counterexample_direct_gate_fails', kd == Q(4,3) and kd > 1)
check('maximal_monotone_counterexample_energy_is_exact', ke2 == j*j == Q(4,9))
# Formula values below are exact rational consequences, independent of radius.

# F(y)={2y,3y}: both complete outputs contract; zero-input all-pair collision.
outputs=[Q(1,3),Q(1,4)]
check('complete_multivalued_witness_anchor', all(abs(2*y-1)<=Q(1,2) for y in outputs))
check('complete_multivalued_witness_true_EB', all(y == Q(1,2)*(2*y) for y in outputs))
check('complete_multivalued_witness_direct_factor', Q(1,2)*(1+Q(1,2))/2 == Q(3,8))
check('complete_multivalued_witness_all_pair_obstruction', outputs[0] != outputs[1])
# Boundary: lambda=1,F=-I,mu=nu=-1/2 has A=Delta=0, all inputs collapse.
check('semimonotone_zero_A_collision_boundary', 1+Q(-1,2)+Q(-1,2)==0
      and 1-4*Q(-1,2)**2==0 and all(y-y==0 for y in [Q(0),Q(1)]))

# LT minus coupled-energy factor has positive numerator 2u+2tau(1+u)^2.
u,tau=m,s
check('LT_energy_factor_difference_numerator',
      (((1+2*tau)*(1+u)**2-(1+u**2))-(2*u+2*tau*(1+u)**2)).is_zero())
# Fixed lambda, mu=-h,nu=0 and mu=0,nu=-eta denominators are positive
# only under their stated gates. Balanced limit L=0 is retained.
for L0 in [Q(0),Q(1,3),Q(1),Q(3)]:
    tied=(1-L0*L0)/(2*(1+L0*L0))
    check('balanced_slice_value_'+str(L0), 1+2*tied>0 and
          (1-4*tied*tied)==(L0*(1+2*tied))**2)

result={'status':'PASS','scope':'exact polynomial identities and rational edge cases; analytic proofs remain in manuscript/C89-v1',
        'checks':checks,'linear_counterexample':{'L':str(L),'rho':str(rho),'kappa_D':str(kd),'kappa_E_squared':str(ke2),'J_factor':str(j)}}
Path(__file__).with_name('results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'status':result['status'],'checks':len(checks),'linear_counterexample':result['linear_counterexample']}))
