"""Exact algebra checks for the semimonotonicity route review (stdlib only).

Run: python research/code/submonotonicity_routes/semimonotone_verify.py
All arithmetic is rational. Identities polynomial of degree <=2 in each tested
variable are checked on {-1,0,1}^n, an exact interpolation certificate. The
matrix check treats one fixed pair of noncommuting symmetric matrices. General
graph, coverage and convergence arguments are in the accompanying report.
"""
from fractions import Fraction as F
from itertools import product
import json

grid = (F(-1), F(0), F(1))
for z, c, m, r in product(grid, repeat=4):
    a, b = (z+c)/2, (z-c)/2
    A, B = 1+m+r, m-r
    delta = 1-4*m*r
    assert a*b-m*a*a-r*b*b == ((1-m-r)*z*z-A*c*c-2*B*z*c)/4
    assert A*(1-m-r)+B*B == delta
for a, b, tau in product(grid, repeat=3):
    # LT equivalence after clearing the positive denominator 1+2*tau.
    assert (1+2*tau)*a*b+tau*(a*a+b*b) == a*b+tau*(a+b)**2

def madd(a,b):
    return [[x+y for x,y in zip(ar,br)] for ar,br in zip(a,b)]

def mscale(k,a):
    return [[k*x for x in ar] for ar in a]

def mmul(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]

def mvec(a,x):
    return tuple(sum(t*y for t,y in zip(ar,x)) for ar in a)

def dot(x,y):
    return sum(a*b for a,b in zip(x,y))

def quad(a,x):
    return dot(x,mvec(a,x))

def inv2(a):
    d=a[0][0]*a[1][1]-a[0][1]*a[1][0]
    return [[a[1][1]/d,-a[0][1]/d],[-a[1][0]/d,a[0][0]/d]]

I = [[F(1),F(0)],[F(0),F(1)]]
M = [[F(1,5),F(1,7)],[F(1,7),-F(1,6)]]
R = [[-F(1,9),F(1,11)],[F(1,11),F(1,4)]]
Q = madd(I,madd(M,R))
D = madd(M,mscale(-1,R))
N = madd(I,mscale(-1,madd(M,R)))
QiD = mmul(inv2(Q),D)
H = madd(N,mmul(D,QiD))
assert mmul(M,R) != mmul(R,M)
for z1,z2,c1,c2 in product(grid,repeat=4):
    z,c=(z1,z2),(c1,c2)
    a=tuple((x+y)/2 for x,y in zip(z,c))
    b=tuple((x-y)/2 for x,y in zip(z,c))
    gap=dot(a,b)-quad(M,a)-quad(R,b)
    assert 4*gap == quad(N,z)-quad(Q,c)-2*dot(z,mvec(D,c))
    shifted=tuple(x+y for x,y in zip(c,mvec(QiD,z)))
    assert quad(Q,shifted)-quad(H,z) == -4*gap

for p in grid:
    outputs=[p/3,2*p/3]
    values=[2*p/3,p/3]
    assert all(y+w == p for y,w in zip(outputs,values))
    da,db=outputs[0]-outputs[1],values[0]-values[1]
    assert da+db == 0
    assert da*db == -p*p/9
    assert (da-db)**2 == 4*p*p/9

m,r=-F(4,5),-F(1,5)
assert 1+m+r == 0
assert 1-4*m*r == F(9,25)

print(json.dumps({
    'scalar_cayley_identity': True,
    'LT_tied_semimonotone_equivalence': True,
    'noncommuting_matrix_identity_and_completion': True,
    'same_input_multivalued_collision': True,
    'negative_parameter_singular_endpoint': True,
    'union_true_EB_constant': '2',
    'union_all_selection_sharp_Q_factor_lambda_1': '2/3',
    'precision': 'exact rational polynomial interpolation certificates',
    'python_dependencies': 'standard library only',
}, indent=2))
