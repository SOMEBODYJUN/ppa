#!/usr/bin/env python3
"""Finite arithmetic checks for the Heisenberg candidate; not a universal proof."""
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path
import json
import platform
import math
import random

D = Decimal
PRECISION = 240
SEED = 20261013


def langevin(z):
    if not z:
        return D(0)
    if z < 0:
        return -langevin(-z)
    q = (-2*z).exp()
    return (1+q)/(1-q)-1/z


def lp(z):
    if not z:
        return D(1)/3
    q = (-2*abs(z)).exp()
    return 1/(z*z)-4*q/(1-q)**2


def rho(r, lam=D(1)):
    return (1+lam)*r-lam*langevin(6*r)


def bisect(fun, lo, hi):
    assert fun(lo) <= 0 <= fun(hi)
    for _ in range(800):
        mid = (lo+hi)/2
        if mid == lo or mid == hi:
            break
        if fun(mid) <= 0:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2


def inverse_radius(r):
    if not r:
        return D(0)
    return bisect(lambda s: rho(s)-r, D(0), (r+1)/2+1)


def f_radial(r):
    return r-langevin(6*r)


def main():
    with localcontext() as ctx:
        ctx.prec = PRECISION
        ctx.Emin = -999999999
        ctx.Emax = 999999999
        m = bisect(f_radial, D(7)/9, D(1))
        R = D(1)/100
        K = D(27)/46
        psi_coefficient = D(27)/19
        kappa = D(9)/10
        Lstar = D(2) * D(20) ** (D(1)/3)
        assert Fraction(729,874) < Fraction(9,10)
        assert Fraction(27,460) < Fraction(241,900)
        assert Fraction(108,115) > Fraction(9,10)
        assert D(7)/9 < m < 1
        max_inverse_error = D(0)
        local_max = {k: D(0) for k in ('reflection','eb','window','compatibility','distance','length_budget')}
        for j in range(401):
            t = -R+2*R*D(j)/400
            r = m+t
            s = inverse_radius(r)
            delta = abs(t)
            residual = abs(f_radial(s))
            max_inverse_error = max(max_inverse_error, abs(rho(s)-r))
            gaps = {
                'reflection': abs(2*s-r-m)-D(4)/23*delta,
                'eb': abs(s-m)-psi_coefficient*residual,
                'window': K*delta-1,
                'compatibility': psi_coefficient*K*delta-kappa*delta,
                'distance': abs(s-m)-kappa*delta,
                'length_budget': D(135)/23*delta-min(r-D('0.5'),D('1.5')-r),
            }
            for key, val in gaps.items():
                local_max[key] = max(local_max[key],val)
                assert val < D('1e-130'), (key,r,s,val)
        far = []
        for value in ('0','1e-90','1e-60','1e-30','0.01','0.5','1','2','10','1000','1000000'):
            r = D(value)
            s = inverse_radius(r)
            err = abs(rho(s)-r)
            max_inverse_error = max(max_inverse_error,err)
            assert err < D('1e-120') * max(D(1),r), (r,s,err)
            far.append({'input':str(r),'output':str(s),'reverse_error':str(err)})
        spectrum_min_margin = D(10)
        for value in ('1e-30','1e-10','0.001','0.01','0.1','0.3','0.75','1','2','10','100'):
            r = D(value)
            ht = 2-langevin(6*r)/r
            hr = 2-6*lp(6*r)
            lower = D('0.9')*min(r*r,D(1))
            spectrum_min_margin = min(spectrum_min_margin,ht-lower,hr-lower)
            assert min(ht,hr) >= lower
        sharp = []
        for exponent in (6,12,24,48,90):
            r = D(10)**(-exponent)
            s = inverse_radius(r)
            sharp.append({'input_exponent':exponent,'output_over_input_cuberoot':str(s/(r**(D(1)/3)))})
        # Vector checks include antipodal, nearly equal, and unequal-radius pairs.
        rng = random.Random(SEED)
        hmax = 0.0
        pair_count = 0
        vectors = [(0.,0.,0.),(.0001,0.,0.),(-.0001,0.,0.),(.9,0.,0.),(2.,0.,0.)]
        vectors += [tuple(rng.uniform(-2,2) for _ in range(3)) for _ in range(45)]
        def C(vec):
            r = math.sqrt(sum(x*x for x in vec))
            if not r:
                return (0.,0.,0.)
            s = inverse_radius(D(str(r)))
            amp = float(langevin(6*s))
            return tuple(amp*x/r for x in vec)
        images = [C(v) for v in vectors]
        for i in range(len(vectors)):
            for j in range(i):
                distance = math.sqrt(sum((x-y)**2 for x,y in zip(vectors[i],vectors[j])))
                if not distance:
                    continue
                cdistance = math.sqrt(sum((x-y)**2 for x,y in zip(images[i],images[j])))
                quotient = cdistance/(distance**(1/3))
                hmax = max(hmax,quotient)
                pair_count += 1
                assert quotient <= float(Lstar)+1e-12
        # λ>1: a complete zero-input sphere of roots; no branch deletion.
        nonzero_zero_input = bisect(lambda r: rho(r,D(2)), D('0.001'), D(1))
        assert abs(rho(nonzero_zero_input,D(2))) < D('1e-130')
        # Index arithmetic is exact. Boundary orientations are analytical in the card.
        assert 2 + (-1) == 1
        result = {
            'scope':'finite checks only; analytic universal proofs are in candidate card',
            'python':platform.python_version(),'decimal_precision':PRECISION,'seed':SEED,
            'parameters':{'beta':6,'lambda':1,'R':'1/100','local_L':'4/23','psi':'27/19 * t','kappa':'9/10','bar_t':1},
            'magnetization_radius':str(m),'magnetization_bracket':['7/9','1'],
            'local_cases':401,'maximum_positive_local_violations':{k:str(v) for k,v in local_max.items()},
            'max_reverse_error':str(max_inverse_error),'spectrum_min_margin':str(spectrum_min_margin),
            'global_holder_constant':str(Lstar),'finite_vector_pairs':pair_count,'max_vector_holder_quotient':hmax,
            'origin_sharp_exponent': '1/3; limiting coefficient (5/24)^(1/3)',
            'sharp_scale_checks':sharp,'far_and_zero_checks':far,
            'lambda_2_nonzero_zero_input_radius':str(nonzero_zero_input),
            'index':{'sphere':2,'outside':-1,'total':1},
        }
        dest=Path(__file__).with_name('results.json')
        dest.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
        print(json.dumps({k:result[k] for k in ('magnetization_radius','local_cases','max_reverse_error','finite_vector_pairs','max_vector_holder_quotient','index')},ensure_ascii=False,indent=2))


if __name__ == '__main__':
    main()
