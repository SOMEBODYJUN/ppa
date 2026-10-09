"""Finite arithmetic illustrations of structure_prior_art.md, not priority proof."""
from fractions import Fraction
from math import sqrt
for gq in (Fraction(1,4), Fraction(1,2), Fraction(3,4)):
    a = gq/(1-gq)
    assert -a/gq + 1/(1-gq) == 0
    g = float(gq); sigma = sqrt(g)
    M = (1-g)*g**(g/(1-g))*sigma**(-2*g/(1-g))
    sharp = sqrt(M/(2*(1-sigma*sigma)))
    net = 2*g**(-g/(1-g))/(1-g)
    ajiev = 3*2**(g/(1-g))*g**(-g/(1-g))/(1-g)
    assert abs(sharp-1/sqrt(2)) < 1e-12
    for eta in (.01, .1, .5):
        for h in (.01, .2, 1, 2, 10):
            assert min((1+eta)*h,1) <= (1+eta)**g*h**g + 1e-12
    print(gq, sharp, net, ajiev)
assert sqrt(.01) > .01
h = (5-sqrt(17))/2
assert abs(2-h-sqrt(2+h)) < 1e-12
for n in (1,2,100): print(n, sqrt(n/(2*(n+1))))

# Fixed-point sets need not be preserved by a uniform limit (F61).
for eta in (Fraction(1,2), Fraction(1,10), Fraction(1,100)):
    for x in (Fraction(0),Fraction(1,3),Fraction(1)):
        assert ((1-eta)*x == x) == (x == 0)
    assert eta > 0  # uniform error to Id on [0,1] is eta
