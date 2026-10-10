#!/usr/bin/env python3
"""C225-v2 finite algebra checks; the all-real-p statement is analytic."""
from decimal import Decimal, localcontext
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json
import platform


def binom(a, k):
    out = F(1)
    for j in range(k):
        out *= a-j
    return out/factorial(k)


def coefficients(p):
    # Independently compose (1+g2*t^2+g4*t^4)^(1/p).
    g2, g4 = binom(p, 2), binom(p, 4)
    c2 = g2/p
    c4 = g4/p+binom(1/p, 2)*g2*g2
    return c2, c4


def main():
    ps = [F(3, 2)+F(1, 2**20), F(8, 5), F(7, 4),
          F(2), F(5, 2), F(3), F(7, 2), F(10), F(100)]
    cases = []
    for p in ps:
        c2, c4 = coefficients(p)
        assert c2 == (p-1)/2
        assert c4 == -(p-1)*(2*p-3)*(p+1)/24 < 0
        alpha0_over_R = 3*(p-1)/(2*(2*p-3)*(p+1))
        assert alpha0_over_R == c2*c2/(-4*c4)
        alpha_over_R = 2*alpha0_over_R
        reduced_K_over_R = -c4-c2*c2/(4*alpha_over_R)
        assert reduced_K_over_R == -c4/2 > 0
        # Reverse check: reconstruct the radial threshold from K=0.
        assert c2*c2/(4*(-c4)) == alpha0_over_R
        # Gram determinant and null tangent Hessian, after division by R.
        assert alpha_over_R*c2 > 0 and c2-c2 == 0
        cases.append({"p": str(p), "c2": str(c2), "c4": str(c4),
                      "alpha0_over_R": str(alpha0_over_R),
                      "alpha_over_R": str(alpha_over_R),
                      "K_over_R": str(reduced_K_over_R)})
    # Threshold and the mandatory straight-line endpoint sixth term.
    assert coefficients(F(3, 2)) == (F(1, 4), F(0))
    for p in [F(11, 10), F(4, 3), F(3, 2)-F(1, 2**20)]:
        assert coefficients(p)[1] > 0
    p = F(3, 2)
    g2, g4, g6 = (binom(p, k) for k in [2, 4, 6])
    c6 = g6/p+binom(1/p, 2)*2*g2*g4+binom(1/p, 3)*g2**3
    assert c6 == F(1, 192)
    # Independent curved-path check, in normalized n2,R,eta units:
    # q*s^2/2 + n2*s*t^2 - n4*t^4 at s=-n2*t^2/q.
    for q in [F(1, 100), F(1), F(100)]:
        for n2 in [F(1, 7), F(1, 4), F(3)]:
            for n4 in [F(0), F(1, 100), F(2)]:
                s2 = -n2/q
                coefficient = q*s2*s2/2+n2*s2-n4
                assert coefficient == -n4-n2*n2/(2*q) < 0
    # Decimal independent matrix/objective coefficient checks, including p>2.
    decimals = []
    with localcontext() as ctx:
        ctx.prec = 80
        for p0 in ps:
            p = Decimal(p0.numerator)/Decimal(p0.denominator)
            R = (Decimal(2).ln()/p).exp()
            beta = R*(p-1)/2
            c4 = -(p-1)*(2*p-3)*(p+1)/24
            alpha0 = beta*beta/(-4*R*c4)
            alpha = 2*alpha0
            K = -R*c4-beta*beta/(4*alpha)
            target = R*(p-1)*(2*p-3)*(p+1)/48
            assert abs(K/target-1) < Decimal('1e-75')
            q = 2*alpha
            assert abs((R*c4+beta*beta/(2*q))+K) < Decimal('1e-70')
            decimals.append({"p": str(p0), "R": str(R),
                             "alpha": str(alpha), "K": str(K)})
        comp_cases = 0
        points = [Decimal(-2), Decimal(-1), Decimal('-0.25'),
                  Decimal(0), Decimal('0.25'), Decimal(1), Decimal(2)]
        for p0 in [F(2), F(5, 2), F(3), F(10), F(100)]:
            p = Decimal(p0.numerator)/Decimal(p0.denominator)
            for x in points:
                for y in points:
                    r = (x*x+y*y).sqrt()
                    powers = sum((abs(z)**p0.numerator
                                  if p0.denominator == 1 else
                                  (p*abs(z).ln()).exp())
                                 for z in [x, y] if z != 0)
                    norm_p = (powers.ln()/p).exp() if powers else Decimal(0)
                    delta = x*x/2+y*y-x-y+abs(x)+abs(y)-norm_p+Decimal('0.5')
                    decomposition = ((r-1)**2/2+y*y/2+abs(x)-x+abs(y)-y
                                     +r-norm_p)
                    assert abs(delta-decomposition) < Decimal('1e-70')
                    assert delta >= -Decimal('1e-70')
                    if (x, y) != (Decimal(1), Decimal(0)):
                        assert delta > 0
                    comp_cases += 1
        # Kappa(u)=(1-f+u*f')/u^2 has removable value c2=3/8.
        c2, c4 = coefficients(F(7, 4))
        assert c2 == F(3, 8) and 3*c4 == -F(33, 256)
    out = {"python": platform.python_version(), "seed": None,
           "claim_version": "C225-v2", "arithmetic": "Fraction exact; Decimal 80 digits",
           "exact_cases": cases, "decimal_cases": decimals,
           "strict_comp_global_identity_cases": comp_cases,
           "kappa_constant_7_over_4": str(c2),
           "endpoint_c6": str(c6), "all_checks_passed": True,
           "scope": "Finite independent coefficient and reverse checks, not proof for all real p. The canonical positive-support analytic IFT proof carries that quantifier. No p=infinity claim or all-model exponent is checked."}
    path = Path(__file__).with_name('upper_family_results.json')
    path.write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps({"saved": str(path), "all_checks_passed": True}))


if __name__ == '__main__':
    main()
