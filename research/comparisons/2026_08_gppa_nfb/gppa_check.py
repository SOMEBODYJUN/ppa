"""Finite exact/numeric checks for gppa_review.md; these are not proofs."""
from fractions import Fraction as Q
from math import sqrt
from pathlib import Path
import json


def rat(x):
    return str(x)


def overlap_check():
    # C191 singleton D; alpha=2/3, q=1/8, and cube-valued y.
    a, c, lam, h = Q(7), Q(2), Q(1), Q(3, 10)
    q, qa = Q(1, 8), Q(1, 4)
    u, w = h * c * qa / (1 - qa), h / lam
    eps = min(c / u, a / w)
    t, cube_root_y = Q(-1), Q(1, 8)
    tangent_tail_coefficient = lam * c * qa / (1 - qa)
    invariant = t + tangent_tail_coefficient * cube_root_y**2
    rows = []
    for k in range(8):
        y, ya = cube_root_y**3, cube_root_y**2
        ny, nya = q * y, qa * ya
        nt = t + lam * c * nya
        vdiff = (-u * nya + u * ya, w * ny - w * y)
        rhs = (h * c * nya, -h * a * ny)
        assert vdiff == rhs
        assert (nt - t, ny - y) == (lam * c * nya, -lam * a * ny)
        assert nt + tangent_tail_coefficient * nya == invariant
        assert (-u * ya, w * y) == (h / lam * (t - invariant), h / lam * y)
        rows.append({"k": k, "y": rat(y), "t": rat(t), "kernel_update_exact": True})
        t, cube_root_y = nt, cube_root_y / 2
    asm_deficits = []
    for ry in [Q(1, 4), Q(1, 8), Q(1, 16)]:
        y, ya = ry**3, ry**2
        fy, vy = (-c * ya, a * y), (-u * ya, w * y)
        for rz in [Q(0), Q(1, 8), Q(1, 16)]:
            z, za = rz**3, rz**2
            for n in ([Q(-100), Q(-1), Q(0)] if z == 0 else [Q(0)]):
                fz, vz = (-c * za, a * z + n), (-u * za, w * z)
                df = tuple(fy[i] - fz[i] for i in range(2))
                dv = tuple(vy[i] - vz[i] for i in range(2))
                lhs = sum(df[i] * dv[i] for i in range(2))
                rhs = eps * sum(j * j for j in dv)
                assert lhs >= rhs
                asm_deficits.append(rhs - lhs)
    radius = Q(1, 8)
    # R^(1-alpha)=1/2 exactly for this R.
    lr = Q(1, 2) + 2 * lam * c * qa
    base = (Q(1, 2) + lr) / (2 * lam * c)
    kappa = float(base) ** 1.5
    assert kappa < 1
    return {"q": rat(q), "q_alpha": rat(qa), "u": rat(u), "w": rat(w),
            "adaptive_epsilon": rat(eps), "R": rat(radius), "L_R": rat(lr),
            "kappa": kappa, "max_ASM_deficit": rat(max(asm_deficits)), "rows": rows}


def cap_check():
    radius = Q(1, 16)
    lr = 2 * sqrt(2) + 1.5 * sqrt(float(radius))
    kappa = (sqrt(float(radius)) + lr)**2 / 16
    radius_bound = (2 * (4 - 2 * sqrt(2)) / 5)**2
    assert float(radius) < radius_bound and kappa < 1
    z, p, root_r = Q(0), Q(-1), Q(1, 8)
    rows = []
    for k in range(8):
        r = root_r**2
        nz, ny = z + root_r, r / 4
        sqny = root_r / 2
        fplus, fminus = (-2 * sqny, Q(0), 3 * ny), (-2 * sqny, Q(0), -5 * ny)
        assert (nz + fplus[0], p + fplus[1], ny + fplus[2]) == (z, p, r)
        assert fplus[2] > 0 and fminus[2] < 0
        rows.append({"k": k, "input_normal": rat(r), "output_normal": rat(ny),
                     "plus_normal": rat(fplus[2]), "minus_normal": rat(fminus[2]),
                     "ordinary_PPA_update_exact": True})
        z, root_r = nz, root_r / 2
    return {"R": rat(radius), "r0": "1/64", "L_R": lr, "kappa": kappa,
            "strict_R_upper_bound": radius_bound, "rows": rows}


def t4_constants():
    rows = []
    for s in [0.01, 0.5, 1, 4, 5, 10]:
        kappa = 1 / sqrt(1 + 2 * s)
        weak_ratio = kappa / (1 - kappa)
        stated = 2 / s
        sharp_q = 1 / (1 + s)
        sharp_ratio = sharp_q / (1 - sharp_q)
        rows.append({"gamma_epsilon": s, "kappa_over_1_minus_kappa": weak_ratio,
                     "paper_bound_2_over_s": stated,
                     "paper_inequality_holds": weak_ratio <= stated + 1e-12,
                     "sharp_ratio": sharp_ratio, "exact_sharp_1_over_s": 1 / s})
    return rows


if __name__ == "__main__":
    results = {"note": "Finite algebra checks only; general proofs are in gppa_review.md.",
               "overlap": overlap_check(), "cap": cap_check(), "T4_constants": t4_constants()}
    target = Path(__file__).with_name("gppa_check_results.json")
    target.write_text(json.dumps(results, indent=2) + "\n")
    print(json.dumps({"overlap": {k: v for k, v in results["overlap"].items() if k != "rows"},
                      "cap": {k: v for k, v in results["cap"].items() if k != "rows"},
                      "T4_constants": results["T4_constants"]}, indent=2))
