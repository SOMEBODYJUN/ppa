#!/usr/bin/env python3
"""Finite arithmetic checks for C455; the general proof is in inexact.md."""
from decimal import Decimal as D, getcontext
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json
import platform

getcontext().prec = 80
TOL = D('1e-65')


def norm(v):
    return sum(t*t for t in v).sqrt()


def add(x, y):
    return tuple(a+b for a, b in zip(x, y))


def scale(a, x):
    return tuple(a*b for b in x)


def field(x):
    a = -D(7)/32
    b = -5*D(39).sqrt()/32
    return (a*x[0]-b*x[1], b*x[0]+a*x[1])


def inner(x):
    if norm(x) == 0:
        return x, 0, 0
    y = x
    for j in range(11):
        w = field(y)
        e = add(add(y, w), scale(-D(1), x))
        if norm(e) <= D(5)/36*norm(w):
            return y, j, j+1
        y = add(y, scale(-D(1)/2, e))
    raise AssertionError('Ten-update theorem failed on a tested input')


def run():
    scalar_cases = 0
    low_witnesses = 0
    energy_witnesses = 0
    for L in map(D, ['0.1', '0.25', '0.5', '0.9', '1', '2', '10']):
        threshold = (1-L)/(L*L) if L <= D('.5') else 1/(2*L*L)
        for fraction in map(D, ['0', '0.1', '0.5', '0.9', '0.99']):
            sigma = fraction*threshold
            c = 1+2*sigma
            b = (1+(1+4*sigma).sqrt())/2
            h = max(1/b, ((1+L*L)/c).sqrt())
            m = L/h
            assert m < 1
            beta = h*h-L*L
            for alpha in map(D, ['0.25', '0.5', '0.75']):
                kappa = m+(1-m)*alpha
                delta = h-L/kappa
                assert 0 < delta < 1/b
                for j in range(101):
                    z = L*j/100
                    H = max(1/b, ((1+z*z)/c).sqrt())
                    assert H-z/kappa >= delta-TOL
                    assert H*H-z*z >= beta-TOL
                    assert H > z
                    scalar_cases += 1
            # Independent coordinate reconstruction for the two equality branches.
            if abs(h-1/b) < TOL:
                assert L <= 1-h+TOL
                assert abs((h-1)+sigma*h*h) < TOL
                low_witnesses += 1
            else:
                A = (h*h+1-L*L)/2
                radicand = h*h-A*A
                assert radicand >= -TOL
                p = (A, max(D(0), radicand).sqrt())
                assert abs(norm(p)-h) < TOL
                assert abs(norm((1-p[0], -p[1]))-L) < TOL
                assert abs((A-1)+sigma*h*h) < TOL
                energy_witnesses += 1

    assert Fraction(39, 64)**5 < Fraction(1, 10)
    assert Fraction(25, 128) > Fraction(3, 16)
    assert Fraction(25, 128) < Fraction(15, 76)
    assert Fraction(128, 135) < Fraction(19, 20)
    assert D(39).sqrt()**9/D(8)**9 > D('.1')
    inner_results = []
    for amplitude in map(D, ['1e-80', '1', '1e80']):
        for direction in [(D(1), D(0)), (D(0), D(1)), (D(1), -D(2))]:
            x = scale(amplitude, direction)
            y, updates, evaluations = inner(x)
            assert norm(y) <= D('.9')*norm(x)
            inner_results.append({'amplitude': str(amplitude),
                                  'direction': list(map(str, direction)),
                                  'updates': updates, 'evaluations': evaluations,
                                  'outer_ratio': str(norm(y)/norm(x))})
    assert inner((D(0), D(0))) == ((D(0), D(0)), 0, 0)
    x = (D(1), D(0))
    total_evals = 0
    outer_steps = 0
    total_length = D(0)
    while norm(x) > D('1e-8'):
        y, updates, evaluations = inner(x)
        total_length += norm(add(y, scale(-D(1), x)))
        x = y
        total_evals += evaluations
        outer_steps += 1
        assert outer_steps < 180
    assert total_evals <= 11*outer_steps

    parameter_checks = []
    for lam in map(D, ['0.25', '0.4375', '0.5', '1', '2', '4', '8']):
        dsq = 1-7*lam/16+lam*lam
        L = 1/lam
        sigma = 7*lam/(32*dsq)
        b = (1+(1+4*sigma).sqrt())/2
        h = max(1/b, ((1+L*L)/(1+2*sigma)).sqrt())
        assert abs(h-dsq.sqrt()/lam) < TOL
        parameter_checks.append({'lambda': str(lam), 'exact_factor': str(1/dsq.sqrt()),
                                 'strict_contraction': lam > D(7)/16})

    maximum_ratio = D(0)
    for j in range(1001):
        z = D(j)/100
        ratio = (1+2*z)/((1+z*z).sqrt()+z)
        assert 1-TOL <= ratio <= D('1.25')+TOL
        maximum_ratio = max(maximum_ratio, ratio)
    return {'claim': 'C455-v1', 'python': platform.python_version(),
            'decimal_precision': getcontext().prec, 'tolerance': str(TOL),
            'seed': None, 'randomness': 'none',
            'script_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
            'scalar_grid_checks': scalar_cases,
            'low_branch_witnesses': low_witnesses,
            'energy_branch_witnesses': energy_witnesses,
            'exact_q10': str(Fraction(39, 64)**5),
            'inner_results': inner_results,
            'outer_example': {'initial': ['1', '0'], 'target_norm': '1e-8',
                              'steps': outer_steps, 'field_evaluations': total_evals,
                              'terminal_norm': str(norm(x)),
                              'finite_prefix_length': str(total_length)},
            'lambda_checks': parameter_checks,
            'zero_defect_budget_maximum_on_grid': str(maximum_ratio),
            'scope': 'Finite arithmetic only; not a proof, complexity comparison, or novelty test.'}


if __name__ == '__main__':
    print(json.dumps(run(), ensure_ascii=False, indent=2))
