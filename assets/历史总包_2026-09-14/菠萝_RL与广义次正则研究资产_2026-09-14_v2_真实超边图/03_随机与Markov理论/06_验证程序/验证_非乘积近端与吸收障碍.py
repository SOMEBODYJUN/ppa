"""Exact algebra checks for the native group-l0 proximal counterexample.

The symbolic identities supplement, and do not replace, the proofs in the
companion report.  No stochastic simulation is used as a theorem proof.
"""
from fractions import Fraction as F

H = ((F(2), F(1)), (F(1), F(2)))
Q = ((F(3), F(1)), (F(1), F(3)))
Qinv = ((F(3, 8), F(-1, 8)), (F(-1, 8), F(3, 8)))
b = (F(3), F(3))
v = (F(1), F(1))

def mv(matrix, vector):
    return tuple(sum(a * x for a, x in zip(row, vector)) for row in matrix)

def dot(x, y):
    return sum(a * b for a, b in zip(x, y))

def candidate(x):
    return mv(Qinv, tuple(a + c for a, c in zip(x, b)))

def gain(x):
    c = tuple(a + bb for a, bb in zip(x, b))
    return dot(c, mv(Qinv, c)) / 2

for ei in ((F(1), F(0)), (F(0), F(1))):
    assert mv(Q, mv(Qinv, ei)) == ei
assert mv(H, v) == b
assert candidate(v) == v
assert gain(v) == 4
assert gain((F(0), F(0))) == F(9, 4)
assert dot(v, mv(H, v)) / 2 - dot(b, v) + 4 == 1

# Polynomial identities along x=a*v reduce to affine/quadratic coefficients.
assert candidate((F(0), F(0))) == (F(3, 4), F(3, 4))
assert mv(Qinv, v) == (F(1, 4), F(1, 4))
assert dot(v, mv(Qinv, v)) / 2 == F(1, 4)
assert dot(b, mv(Qinv, v)) == F(3, 2)
assert dot(b, mv(Qinv, b)) / 2 == F(9, 4)
assert Qinv[0][1] == F(-1, 8)  # nonzero mixed coefficient of the gain

print("Q inverse:", Qinv)
print("Threshold gain: (3*x1^2 - 2*x1*x2 + 3*x2^2 + 12*x1 + 12*x2 + 36)/16")
print("Ray candidate: ((a+3)/4, (a+3)/4); ray gain: (a+3)^2/4")
print("g(v), g(0):", gain(v), gain((F(0), F(0))))
print("Exact rational identities passed.")

a0 = F(2)
for k in (0, 1, 2, 5, 10):
    ak = 1 + (a0 - 1) * F(1, 4) ** k
    xk = (ak, ak)
    assert ak > 1
    assert gain(xk) > 4
    assert candidate(xk) == ((ak + 3) / 4, (ak + 3) / 4)
    print(f"k={k}: a_k={ak}, gain={gain(xk)}")
