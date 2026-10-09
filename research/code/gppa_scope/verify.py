"""Reproducible finite corroboration of C215/C216; no general proof claims.

Only Python's standard library is required. Fraction checks are exact. Decimal
tail intervals use the analytic geometric remainder from RB3; rounding checks
are repeated at two precisions and are not interval-arithmetic certificates.
"""
from decimal import Decimal as D, localcontext
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import platform


ROOT = Path(__file__).resolve().parents[3]


def norm2(v):
    return sum(x*x for x in v)


def dot(v, w):
    return sum(x*y for x, y in zip(v, w))


def tail(y, gamma, nu, tol):
    """Return partial E and an analytic bound for its omitted positive tail."""
    if not y:
        return D(0), D(0), 0
    assert D(0) < y < D(1) and nu > D(1) and gamma > D(0)
    partial = D(0)
    exponent = gamma
    for j in range(10000):
        term = (y.ln()*exponent).exp()
        partial += term
        exponent *= nu
        first_omitted = (y.ln()*exponent).exp()
        # Reapply RB3 to y**nu**(j+1), with initial power gamma.
        ratio = (y.ln()*exponent*(nu-D(1))).exp()
        remainder = first_omitted/(D(1)-ratio)
        if remainder <= tol*max(partial, D('1e-10000')):
            return partial, remainder, j+1
    raise AssertionError('tail did not meet explicit accuracy target')


def conjugacy_checks(precision):
    records = []
    with localcontext() as ctx:
        ctx.prec = precision
        ctx.Emin = -999999999
        ctx.Emax = 999999999
        tol = D(10)**(-precision+15)
        for nu in map(D, ['1.5', '2', '3', '10']):
            for gamma in map(D, ['0.3', '0.5', '0.9']):
                for y in map(D, ['0', '1e-12', '0.0625', '0.25']):
                    for a in map(D, ['0.5', '2']):
                        xi = D('-1.25')
                        ey, ry, count = tail(y, gamma, nu, tol)
                        if not y:
                            assert ey == ry == 0
                            records.append({'nu': str(nu), 'gamma': str(gamma),
                                            'A': str(a), 'y': '0', 'stationary': True})
                            continue
                        yp = (y.ln()*nu).exp()
                        ep, rp, countp = tail(yp, gamma, nu, tol)
                        increment = (y.ln()*gamma).exp()
                        slack = abs(ey-increment-ep)
                        roundoff = tol*max(ey, increment, D(1))
                        assert slack <= ry+rp+roundoff
                        h = D(1)/(-y.ln())
                        hp = D(1)/(-yp.ln())
                        assert abs(hp-h/nu) <= roundoff
                        recovered = (-D(1)/h).exp()
                        assert abs(recovered-y) <= roundoff
                        # Compare both coordinates independently and invert H.
                        invariant = xi+a*ey
                        invariantp = xi+a*increment+a*ep
                        assert abs(invariant-invariantp) <= a*(ry+rp+roundoff)
                        assert abs((invariant-a*ey)-xi) <= roundoff
                        # Reconstruct original plus and minus graph equations.
                        tangential = -a*increment
                        normalplus = y-yp
                        normalminus = -y-yp
                        assert abs((xi+a*increment)+tangential-xi) <= roundoff
                        assert yp+normalplus == y
                        assert abs(yp+normalminus+y) <= roundoff
                        # Every negative initial height enters the same positive collar.
                        assert D(0) < yp < y <= D('0.25')
                        records.append({'nu': str(nu), 'gamma': str(gamma),
                                        'A': str(a), 'y': str(y),
                                        'tail_terms': [count, countp],
                                        'conjugacy_slack': str(slack),
                                        'tail_remainder': str(ry+rp)})
        # Exact asymptotic factor corroboration for the superquadratic case.
        nu, gamma, a = D(3), D('0.5'), D(2)
        ratios = []
        for k in range(5):
            y = ((D('0.25').ln())*(nu**k)).exp()
            yp = (y.ln()*nu).exp()
            ey, _, _ = tail(y, gamma, nu, tol)
            ep, _, _ = tail(yp, gamma, nu, tol)
            error = (a*a*ey*ey+y*y).sqrt()
            errorp = (a*a*ep*ep+yp*yp).sqrt()
            ratio = errorp/(error**nu)
            ratios.append(str(ratio))
        assert abs(D(ratios[-1])-D('0.25')) < D('1e-35')
        # Homeomorphism has no forward Lipschitz bound at zero.
        quotients = []
        for y in map(D, ['1e-2', '1e-4', '1e-8']):
            quotients.append(D(1)/(-y.ln())/y)
        assert quotients[0] < quotients[1] < quotients[2]
    return {'precision': precision, 'cases': records, 'q3_ratios': ratios}


def cancellation_checks():
    cases = 0
    parameters = [F(1,100), F(1,4), F(1), F(4), F(20)]
    vectors = [(F(i), F(j)) for i in range(-2,3) for j in range(-2,3)]
    for eps in parameters:
        for lam in parameters:
            alpha = 1+lam*eps
            for u in vectors:
                for w in vectors:
                    inner = dot(u, w)
                    if inner < alpha*norm2(w):
                        continue
                    t = tuple(x-alpha*y for x,y in zip(u,w))
                    # Reverse the expanded square and its exact margin.
                    assert norm2(u)-norm2(t) == 2*alpha*inner-alpha**2*norm2(w)
                    assert norm2(t) <= norm2(u)-alpha**2*norm2(w)
                    assert norm2(u)-alpha**2*norm2(w) >= 0
                    # q contraction squared is exact and avoids square roots.
                    assert alpha**2*norm2(w) <= norm2(u)
                    cases += 1
    assert cases > 0
    return {'exact_admissible_vector_cases': cases}


def stability_checks():
    records = []
    # Scalar original F(x)=m(x-s), v(x)=x. Second free coordinate can be
    # appended for a noninjective v=(x,0); none of these checks bounds it.
    for m in [F(0), F(1,10), F(1), F(4)]:
        for eps in [F(1,100), F(1,4), F(2)]:
            for lam in [F(1,3), F(1), F(3)]:
                for s in [F(-2), F(0), F(3)]:
                    for delta in [F(0), eps*eps]:
                        c = m*s/(m+eps)  # all regularized zeros have this v.
                        q = 1/(1+lam*eps)
                        a = abs(s) if m else F(0)
                        assert abs(c) <= a
                        x = F(5,4)
                        bound = abs(x-c)
                        for k in range(12):
                            exact = (x+lam*m*s)/(1+lam*(m+eps))
                            f = m*(exact-s)
                            assert f == (x-exact)/lam-eps*exact
                            assert abs(exact-c) <= q*abs(x-c)
                            assert abs(f) <= abs(x-c)/lam+eps*a
                            noise = delta*(-1 if k%2 else 1)
                            x = exact+noise
                            bound = q*bound+delta
                            assert abs(x-c) <= bound
                        b = delta*(1+lam*eps)/(lam*lam*eps)+eps*a
                        records.append({'m':str(m),'epsilon':str(eps),'lambda':str(lam),
                                        'zero':str(s),'delta':str(delta),
                                        'regularized_zero':str(c),'residual_budget':str(b)})
    # Source-print budget identity and its exact positive slack.
    for L in [F(0),F(1),F(3)]:
        for eps in [F(1,100),F(1,4),F(2)]:
            for lam in [F(1,3),F(1),F(3)]:
                a = F(5)
                new = L*eps/lam**2+L*eps**2/lam+eps*a
                old = (L*eps**2+4*L*eps/lam)/lam+eps*(2*L*eps/lam+a)
                assert old-new == 3*L*eps/lam**2+2*L*eps**2/lam
                assert (old>new) == (L>0)
    # L=0: constant kernel, F(x)=x-s, all exact outputs solve f=-eps*c.
    for c in [F(-2),F(0),F(3)]:
        eps, s, delta = F(1,4), F(2), F(1,16)
        exact = s-eps*c
        assert exact-s == -eps*c
        assert abs(exact+delta-s) <= delta+eps*abs(c)
    # A monotone, origin-continuous gauge may jump at a positive point.
    b = F(1)
    def rho(t):
        return t if t<=b else t+1
    seq = [b+F(1,n) for n in [2,10,100,1000]]
    assert all(rho(t)>rho(b)+1 for t in seq)
    assert rho(F(0)) == 0 and rho(F(1,1000)) == F(1,1000)
    return {'scalar_cases': records,'constant_kernel_cases':3,
            'jump_gauge': {'rho_at_b':str(rho(b)),'rho_right_limit':'2'}}


def quantifier_checks():
    universe = {'covered','extra'}
    fixed_source = {'covered'}
    new_class = universe
    # Fixed strictness can disappear after admissible rewrites.
    rewrite_imports = universe
    assert fixed_source < new_class
    assert rewrite_imports == new_class
    # A known overlapping witness does not disprove existential separation.
    rewrite_imports_second = {'covered'}
    assert bool(new_class-rewrite_imports_second)
    return {'fixed_strict_rewrite_equal_model':True,
            'overlap_with_strict_separation_model':True}


def main():
    low = conjugacy_checks(80)
    high = conjugacy_checks(120)
    assert len(low['cases']) == len(high['cases'])
    for x,y in zip(low['q3_ratios'],high['q3_ratios']):
        assert abs(D(x)-D(y)) < D('1e-60')
    proofs = ['research/canonical/gppa_reformulation_boundary.md',
              'research/canonical/gppa_regularized_stability.md']
    result = {'status':'PASS','python':platform.python_version(),
              'seed':'none; deterministic enumeration',
              'limitations':'Finite corroboration; Decimal rounding is not rigorous interval arithmetic.',
              'proof_sha256': {p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in proofs},
              'conjugacy_80':low,'conjugacy_120':high,
              'cancellation':cancellation_checks(),'stability':stability_checks(),
              'quantifiers':quantifier_checks()}
    path = Path(__file__).with_name('results.json')
    path.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'conjugacy_cases_per_precision':len(low['cases']),
                      'cancellation_cases':result['cancellation']['exact_admissible_vector_cases'],
                      'scalar_cases':len(result['stability']['scalar_cases'])}))


if __name__ == '__main__':
    main()
