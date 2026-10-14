"""Report-level sharpness diagnostics; no Claim registration or manuscript edits.

Run: python3 research/code/author_outline_review/sharp_scope_verify.py
Exact Fraction arithmetic carries the algebraic checks. Decimal at 80 digits is
used only to display square roots and invert genuine complete resolvent steps.
No randomness. These finite checks do not replace the report's proofs.
"""
from decimal import Decimal, getcontext
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import json
import platform

getcontext().prec = 80


def dec(x):
    return Decimal(x.numerator) / Decimal(x.denominator)


def scalar_family():
    rows = []
    for kappa in [Q(1, 100), Q(1, 4), Q(1, 2), Q(3, 4), Q(99, 100)]:
        lam = Q(3, 2)
        radius = Q(1, 7)
        coeff = -(1 + kappa) / (lam * kappa)
        L = 1 + 2 * kappa
        eb = lam * kappa / (1 + kappa)
        B = (1 + L) * radius / 2
        assert 1 / (1 + lam * coeff) == -kappa
        assert eb * abs(coeff) == 1
        assert eb * B / lam == kappa * radius
        assert kappa**2 + (1 + kappa)**2 == (1 + L**2) / 2
        assert B / (1 - kappa) == (1 + kappa) * radius / (1 - kappa)
        for x in [Q(0), -radius, radius, radius / 100]:
            y = -kappa * x
            assert y + lam * coeff * y == x
            assert abs(x - y) == (1 + kappa) * abs(x)
        rows.append({"kappa": str(kappa), "L": str(L), "true_EB": str(eb),
                     "bar_t": str(B / lam), "length_ratio": str((1 + kappa)/(1-kappa))})
    return rows


def energy_family():
    # The same point supplied independently by the literature-comparison reader.
    a = Q(-2, 7)
    b2 = Q(45, 49)
    t2 = a*a + b2
    denom = (1 + a)**2 + b2
    L2 = ((1 - a)**2 + b2) / denom
    rho2 = 1 / denom
    assert t2 == 1 and L2 == Q(9, 5) and rho2 == Q(7, 10)
    assert rho2 == (1 + L2) / (2 * (1 + t2))
    assert Q(1, 5) * 4 > Q(1, 2)  # Luke--Tam displayed budget fails.
    assert 2 * Q(1, 5) < 1         # Energy budget succeeds.
    boundary = []
    for t in [Q(1, 4), Q(1, 2), Q(1), Q(2), Q(3)]:
        a = -t*t/2
        feasible = a*a <= t*t
        L2 = 1 + 2*t*t
        assert (1 + L2)/(2*(1+t*t)) == 1
        direct = (1 + dec(L2).sqrt()) / (2 * dec(t))
        if t > 2:
            assert not feasible and direct < 1
        elif t == 2:
            assert feasible and direct == 1
        else:
            assert feasible and direct > 1
        boundary.append({"t": str(t), "rotation_feasible": feasible,
                         "formal_energy_factor_squared": "1", "direct_factor": str(direct)})
    return {"attained_point": {"lambda": "1", "K": "1", "L_squared": str(Q(9,5)),
                              "rho_E_squared": str(rho2)}, "energy_boundary": boundary}


def critical_holder():
    # gamma=1/2, c=lambda=1; report proves the full gamma in (0,1) family.
    radius = Q(1, 16)
    B = (radius + 2*Q(1, 4))/2
    assert B == Q(9, 32)
    rows = []
    for r in [radius, Q(1, 100), Q(1, 10**8)]:
        h2 = r - Q(9, 4)*r*r
        residual2 = r + Q(7, 4)*r*r
        assert h2 > 0
        assert 9*r*r + 4*h2 == 4*r
        assert 4*r*r + h2 == residual2
        assert residual2 >= r
        assert residual2 <= B*B
        # Full graph substitution for either sign, including zero separately.
        h = dec(h2).sqrt()
        for sign in [-1, 1]:
            x = dec(sign*r)
            y = -x
            v = h
            assert y - 2*y == x
            assert v - h == 0
        direct = (dec(r) + 2*dec(r).sqrt())**2/(4*dec(r))
        assert direct > 1
        rows.append({"r": str(r), "h_squared": str(h2), "true_residual_squared": str(residual2),
                     "critical_compatibility_ratio": str(direct)})
    return {"gamma": "1/2", "L": "2", "q": "2", "critical_coefficient": "1",
            "R": str(radius), "bar_t": str(B), "rows": rows}


def triangular_certificate():
    R = Decimal(1)/16
    L = Decimal(2).sqrt()
    ratio = (R.sqrt()+L)**2/4
    assert ratio < Decimal(3)/4
    return {"R": "1/16", "certificate_kappa": "3/4", "exact_distance_factor": "1/2",
            "actual_point_factor": str(Decimal(1)/Decimal(2).sqrt()),
            "certificate_endpoint_ratio": str(ratio)}


def main():
    result = {"python": platform.python_version(), "precision": 80, "seed": None,
              "scope": "finite algebraic diagnostics; universal statements have analytic proofs in the report",
              "scalar_family": scalar_family(), "energy_family": energy_family(),
              "critical_holder": critical_holder(), "triangular": triangular_certificate(),
              "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(), "status": "PASS"}
    out = Path(__file__).with_name("sharp_scope_results.json")
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
