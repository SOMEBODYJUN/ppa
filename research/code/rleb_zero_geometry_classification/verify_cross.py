"""Exact finite checks for the complete branched-zero-set mechanism."""
from fractions import Fraction as Q
from itertools import product, combinations
from math import isqrt
from pathlib import Path
import json
import platform


def sign(x):
    return (x > 0) - (x < 0)


def clip(x):
    return max(Q(-1), min(Q(1), x))


def retract(x):
    a, b = x
    return (clip(sign(a)*max(abs(a)-abs(b), Q(0))),
            clip(sign(b)*max(abs(b)-abs(a), Q(0))))


def norm2(x):
    return sum(t*t for t in x)


def delta(x, y):
    return tuple(a-b for a,b in zip(x,y))


def times(s, x):
    return tuple(s*a for a in x)


def nearest(x):
    points = ((clip(x[0]), Q(0)), (Q(0), clip(x[1])))
    distance2 = min(norm2(delta(x,p)) for p in points)
    return tuple(p for p in set(points) if norm2(delta(x,p)) == distance2)


def in_K(x):
    return (x[1] == 0 and abs(x[0]) <= 1) or (x[0] == 0 and abs(x[1]) <= 1)


def exact_sqrt(v):
    a, b = isqrt(v.numerator), isqrt(v.denominator)
    assert a*a == v.numerator and b*b == v.denominator
    return Q(a,b)


def prox(x):
    if norm2(x) <= 4:
        return retract(x)
    radius = exact_sqrt(norm2(x))
    p = times(2/radius,x)
    return tuple(a+(b-c)/2 for a,b,c in zip(retract(p),x,p))


def reflected(x):
    return tuple(2*a-b for a,b in zip(prox(x),x))


def main():
    grid = [Q(-1),Q(-1,2),Q(-1,10),Q(0),Q(1,10),Q(1,2),Q(1)]
    inputs = set(product(grid,repeat=2))
    directions = [(Q(1),Q(0)),(Q(0),Q(1)),(Q(3,5),Q(4,5)),
                  (Q(4,5),Q(3,5)),(Q(5,13),Q(12,13))]
    for u in directions:
        assert norm2(u) == 1
        for signs in product((-1,1),repeat=2):
            v=tuple(a*s for a,s in zip(u,signs))
            for radius in (Q(0),Q(1,10),Q(1),Q(2),Q(2001,1000),Q(3),Q(100)):
                inputs.add(times(radius,v))
    pair_checks = 0
    for x,z in combinations(sorted(inputs),2):
        dx2=norm2(delta(x,z))
        assert norm2(delta(retract(x),retract(z))) <= 2*dx2
        dc2=norm2(delta(reflected(x),reflected(z)))
        assert dc2 <= 16*dx2
        assert dc2 <= 64
        assert dc2*dc2 <= 32**2*dx2
        pair_checks += 1
    stopped, radial_bound_samples = 0, 0
    for x in inputs:
        y=prox(x)
        assert in_K(retract(x))
        assert (y == x) == in_K(x)
        w=delta(x,y)
        assert tuple(a+b for a,b in zip(y,w)) == x
        if norm2(x)>4:
            assert norm2(y) <= norm2(x)/4
            assert norm2(w) >= norm2(x)/4
        distance2=norm2(delta(x,nearest(x)[0]))
        if distance2 <= Q(1,100):
            assert norm2(x) <= Q(121,100)
            assert in_K(y)
            for p in nearest(x):
                assert retract(p) == p
                anchor=tuple(2*a-b-c for a,b,c in zip(y,x,p))
                assert norm2(anchor) <= 16*distance2
        if norm2(x) <= 16 or x[0] == 0 or x[1] == 0:
            current=x
            for _ in range(16):
                if in_K(current): break
                current=prox(current)
            assert in_K(current)
            assert prox(current)==current
            stopped+=1
        else:
            # Actual later norms may be irrational. Check the exact radial
            # majorant, not a fictitious rational trajectory.
            bound=exact_sqrt(norm2(x))
            for _ in range(16):
                if bound <= 2: break
                bound/=2
            assert bound <= 2
            radial_bound_samples+=1
    R,bart,kappa,L=Q(1,10),Q(1,4),Q(1,2),Q(4)
    assert (R+L*R)/2 == bart
    assert (1+L)/20 == Q(1,4) <= kappa
    assert (1+L)/(2*(1-kappa)) == 5
    assert 5*R < 2-Q(11,10)
    assert 8 < 9  # 2sqrt(2)+1 < 4
    # Same global and local Holder/RLEB parameters: gamma=1/2, L=6.
    common_R, common_bart = Q(1,100), Q(1,2)
    assert 32 < 36
    assert (common_R+6*Q(1,10))/2 == Q(61,200) < common_bart
    common_ratio=(Q(61,20)**3)/10000
    assert common_ratio == Q(226981,80000000) < kappa
    # (6+3sqrt(2))*(1-1/sqrt(2))=3 by exact sqrt(2) coefficient arithmetic.
    assert 6-3 == 3 and 3-6*Q(1,2) == 0
    for t in (Q(1,100),Q(1,10),Q(1)):
        assert prox((t,t)) == (Q(0),Q(0))
        assert prox((t,Q(0))) == (t,Q(0))
        assert sum(a*b for a,b in zip((-t,Q(0)),(t,t))) == -t*t < 0
    result={"status":"all exact finite checks passed; universal proofs are in candidate card",
            "python":platform.python_version(),"precision":"Fraction/integer exact arithmetic",
            "inputs":len(inputs),"pair_checks":pair_checks,"exact_trajectory_stops":stopped,
            "outside_radial_majorant_samples":radial_bound_samples,
            "cross_euler":{"vertices":5,"edges":4,"chi":5-4},
            "local_tuple":{"lambda":"1","R":str(R),"bar_t":str(bart),"L":str(L),
                           "gamma":"1","psi":"t/10","kappa":str(kappa),"tail":"5t"},
            "same_global_local_tuple":{"lambda":"1","R":str(common_R),
                           "bar_t":str(common_bart),"L":"6","gamma":"1/2",
                           "psi":"s^3/1000","kappa":"1/2","window":"61/200",
                           "compatibility_ratio_upper":str(common_ratio),
                           "tail":"t+(6+3sqrt(2))*sqrt(t)"},
            "scope":"Global complete coverage and low-residual barrier are analytic; no arbitrary full inverse-fiber solver is implemented."}
    path=Path(__file__).with_name("cross_results.json")
    path.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps(result,ensure_ascii=False,indent=2))


if __name__ == "__main__":
    main()
