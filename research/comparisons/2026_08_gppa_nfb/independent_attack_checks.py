"""Exact finite arithmetic supporting independent_attack.md, never an asymptotic proof.

Run with CODEX_PRIMARY_RUNTIME_PYTHON or another Python 3 interpreter.
All substantive infinite-quantifier arguments are in the companion Markdown.
"""
from fractions import Fraction as Q


def nfb_lambda_zero_zeta(beta, rho, tau=Q(1), theta=Q(1)):
    # Source (3.8), zeta=0 and zeta_M=1/tau. The final term does not vanish.
    return 2-theta-(tau+2*rho)**2/(2*tau*(beta+rho))+2*rho/tau


print("NFB identity example: lambda =", nfb_lambda_zero_zeta(Q(1), Q(0)))
print("NFB pure rotation example: lambda =", nfb_lambda_zero_zeta(Q(1), Q(-1, 4)))
negative_identity_gap = nfb_lambda_zero_zeta(Q(100), Q(-11, 10), tau=Q(3))
print("NFB negative identity, PPA step 3: lambda =", negative_identity_gap)
assert nfb_lambda_zero_zeta(Q(1), Q(0)) == Q(1, 2)
assert nfb_lambda_zero_zeta(Q(1), Q(-1, 4)) == Q(1, 3)
assert negative_identity_gap > 0
assert Q(1)/(1-Q(3)) == Q(-1, 2)

for beta, rho, f, c in [(Q(2), Q(-1), Q(3), Q(7)),
                         (Q(2), Q(1), Q(5), Q(-1)),
                         (Q(3), Q(-2), Q(1), Q(4))]:
    left = rho*(f-c)**2 + beta*c**2
    right = beta*rho/(beta+rho)*f**2 + (beta+rho)*(c-rho*f/(beta+rho))**2
    assert left == right
print("Finite rational checks of anchored square completion: passed")

for L, eps, step in [(Q(1), Q(1, 10), Q(2)),
                      (Q(3), Q(1, 100), Q(1, 2)),
                      (Q(0), Q(1, 10), Q(2))]:
    a = Q(3)
    q = 1/(1+step*eps)
    if L:
        assert q*L*eps**2/(1-q) == L*eps/step
    b0 = (L*eps**2+2*L*eps/step)/step + eps*(L*eps/step+a)
    printed = (L*eps**2+4*L*eps/step)/step + eps*(2*L*eps/step+a)
    gap = 2*L*eps/step**2 + L*eps**2/step
    assert printed-b0 == gap
    assert gap >= 0
print("Finite rational checks of GPPA Theorem 4 strict margin: passed")

print("Quadratic-anchor quotients at exact graph points (finite illustrations):")
for n in range(1, 7):
    # C137: y=2^(-4n), h=y^(1/4), eta<=0, positive branch.
    y, h, root = Q(1, 2**(4*n)), Q(1, 2**n), Q(1, 2**(2*n))
    cap = (-2*h*root+3*y*y)/(4*y+9*y*y)
    # C191 allowed singleton support data: alpha=2/3, M=7, b=f=1.
    y, h, power = Q(1, 2**(6*n)), Q(1, 2**(2*n)), Q(1, 2**(4*n))
    natural = (-h*power+7*y*y)/(power*power+49*y*y)
    # C141: gamma=1/2, nu=2, A=B=1, eta<=0, positive branch.
    y, h, root_a, a = Q(1, 2**(8*n)), Q(1, 2**n), Q(1, 2**(2*n)), Q(1, 2**(4*n))
    superlinear = (-h*root_a+y*(a-y))/(root_a*root_a+(a-y)**2)
    print(n, "C137", cap, "C191", natural, "C141", superlinear)

print("All finite checks passed; these checks do not prove universal exclusions.")
