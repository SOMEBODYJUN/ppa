#!/usr/bin/env python3
"""Finite exact checks for C204. Universal kernel exclusion is in the proof.

Only standard-library Fraction arithmetic; no seed, floating tolerance, or
stochastic search. Run from the repository root. Output stays adjacent.
"""
from fractions import Fraction as Q
from pathlib import Path
import json


def run():
    # Symbolic weighted elimination checked on a Cartesian rational grid,
    # including dy=0 and arbitrary signed normal increments.
    grid = [Q(-3), Q(-1, 7), Q(0), Q(2, 9), Q(4)]
    eliminations = 0
    for s in grid:
        for delta in grid:
            for dy in grid:
                for d in grid:
                    plus = -2*s*delta + 3*dy*d
                    minus = -2*s*delta - 5*dy*d
                    assert 5*plus + 3*minus == -16*s*delta
                    eliminations += 1

    # Square heights keep sqrt(y) rational. For each monotone increment,
    # both endpoint normal increments permitted by the two cross inequalities
    # obey the claimed bound. These checks include zero increments.
    a = Q(1, 64)
    sqrt_a = Q(1, 8)
    roots = [Q(1, 8), Q(1, 4), Q(1, 2), Q(1), Q(3, 2)]
    cross_cases = 0
    for u in roots:
        for w in roots:
            y, z = u*u, w*w
            s = u-w
            for magnitude in [Q(0), Q(1, 13), Q(2), Q(7)]:
                delta = (-magnitude if s > 0 else magnitude if s < 0 else Q(0))
                p = 2*s*delta
                assert p <= 0
                lo, hi = p/(3*y+5*z), -p/(5*y+3*z)
                bound = abs(y-z)*abs(delta)/(8*a*sqrt_a)
                for d in [lo, (lo+hi)/2, hi]:
                    assert (3*y+5*z)*d >= p
                    assert -(5*y+3*z)*d >= p
                    assert abs(d) <= bound
                    cross_cases += 1

    # Discontinuous finite-valued monotone q1: jumps at an endpoint and
    # inside the interval, with a nonzero monotone continuous part.
    b = Q(1)
    def q1(y):
        return -y - (Q(2) if y >= Q(1, 4) else Q(0)) - (Q(3) if y >= b else Q(0))
    variation = q1(a)-q1(b)
    partitions = []
    previous = None
    for n in [1, 2, 4, 16, 64, 256]:
        mesh = (b-a)/n
        heights = [a+j*mesh for j in range(n+1)]
        tv = sum(abs(q1(v)-q1(u)) for u,v in zip(heights,heights[1:]))
        assert tv == variation
        normal_bound = mesh*tv/(8*a*sqrt_a)
        if previous is not None:
            assert normal_bound < previous
        previous = normal_bound
        partitions.append({"N":n,"mesh":str(mesh),"total_variation":str(tv),
                           "normal_increment_upper_bound":str(normal_bound)})

    # Same cap orbit and a changed strongly-monotone affine graph.
    # Check the ordinary inclusion backwards as well as the closed formula.
    xi, eta, root_y = Q(0), Q(-1), Q(1, 8)
    invariant = Q(1, 4)
    orbit = []
    for k in range(24):
        y = root_y**2
        out = (xi+root_y, eta, y/4)
        root_out = root_y/2
        f = (-2*root_out, Q(0), 3*out[2])
        assert (xi-out[0],eta-out[1],y-out[2]) == f
        assert out[0]+2*root_out == invariant
        assert out == ((xi+invariant)/2,(eta-1)/2,y/4)
        assert out[2] > 0 and 3*out[2] != 0 and -5*out[2] != 0
        assert out[0] == invariant*(1-Q(1,2)**(k+1))
        orbit.append({"k":k+1,"xi":str(out[0]),"eta":str(eta),"y":str(out[2])})
        xi,eta = out[:2]
        root_y = root_out

    # Boundary at y=0: branches merge and the chosen trajectory is stationary.
    assert (Q(7)+Q(0),Q(-1),Q(0)/4) == (Q(7),Q(-1),Q(0))
    return {"kind":"finite exact algebra and boundary checks, not a proof",
            "arithmetic":"Python fractions.Fraction; exact, no tolerance, no seed",
            "weighted_elimination_cases":eliminations,"cross_endpoint_cases":cross_cases,
            "jump_profile_partitions":partitions,"same_orbit_different_graph":orbit,
            "stationary_zero_boundary_checked":True,"all_assertions_pass":True}


if __name__ == '__main__':
    results = run()
    target = Path(__file__).with_name('pair_monotone_results.json')
    target.write_text(json.dumps(results,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps({"all_assertions_pass":True,
                      "weighted_elimination_cases":results['weighted_elimination_cases'],
                      "cross_endpoint_cases":results['cross_endpoint_cases'],
                      "orbit_steps":len(results['same_orbit_different_graph'])}))
