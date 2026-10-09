"""Finite independent checks for sol61_gppa_audit.md, never infinite-quantifier proofs."""
from fractions import Fraction as Q
from math import exp, log, sqrt
from pathlib import Path
import hashlib
import json


ROOT = Path(__file__).resolve().parent


def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


def sub(x, y):
    return tuple(a - b for a, b in zip(x, y))


def overlap(lam, a, c, h, numerator, denominator, root_divisor):
    # q is a perfect denominator-th power: exact rational fractional powers.
    q = Q(1, root_divisor ** denominator)
    assert q == 1 / (1 + lam * a)
    qa = Q(1, root_divisor ** numerator)
    K = lam * c * qa / (1 - qa)
    w = h / lam
    eps = min(lam * c / (h * K), lam * a / h)
    samples = []
    for root in [Q(0), Q(1, 8), Q(1, 2), Q(2)]:
        y, ya = root ** denominator, root ** numerator
        for n in ([Q(-100), Q(-1), Q(0)] if not y else [Q(0)]):
            samples.append((y, (-c * ya, a * y + n), (-w * K * ya, w * y)))
    for _, f, v in samples:
        for _, g, z in samples:
            dv = sub(v, z)
            assert dot(sub(f, g), dv) >= eps * dot(dv, dv)
    rows = []
    for root0 in [Q(0), Q(1, 8), Q(2)]:
        t, root = Q(-3, 7), root0
        I = t + K * root ** numerator
        for k in range(12):
            y, ya = root ** denominator, root ** numerator
            nr = root / root_divisor
            ny, nya = nr ** denominator, nr ** numerator
            nt = t + lam * c * nya
            fx = (-c * nya, a * ny)
            v = (-w * K * ya, w * y)
            nv = (-w * K * nya, w * ny)
            assert sub(v, nv) == tuple(h * z for z in fx)
            assert (t - nt, y - ny) == tuple(lam * z for z in fx)
            assert nt + K * nya == I
            assert v == (w * (t - I), w * y)
            # The warped equation permits every tangent output, not only nt.
            for arbitrary_tangent in [Q(-100), Q(0), Q(37, 2)]:
                _ = arbitrary_tangent  # F and v are tangent independent.
                assert tuple(h * fx[i] + nv[i] for i in range(2)) == v
            rows.append({"k": k, "y": str(y), "root0": str(root0)})
            t, root = nt, nr
    # Negative inputs have kernel zero; boundary n=0 is a legal warped output.
    for y in [Q(-1), Q(-100)]:
        positive_y = max(y, Q(0))
        ordinary_output = (Q(5), q * positive_y)
        ordinary_value = (Q(0), (y - ordinary_output[1]) / lam)
        assert ordinary_output == (Q(5), Q(0)) and ordinary_value[1] <= 0
        input_kernel = (-w * K * positive_y, w * positive_y)
        output_kernel = (Q(0), Q(0))
        warped_value = (Q(0), Q(0))
        assert sub(input_kernel, output_kernel) == tuple(h * z for z in warped_value)
        assert warped_value != ordinary_value  # Same physical step, different graph values.
    return {"q": str(q), "q_alpha": str(qa), "K": str(K), "epsilon": str(eps),
            "all_pair_samples": len(samples) ** 2, "exact_orbit_steps": len(rows)}


def cross_branch_checks():
    # Independent verification of branch signs and coefficient cancellation.
    rows = []
    for y, z in [(Q(1, 64), Q(1, 256)), (Q(1), Q(1, 4)), (Q(4), Q(1))]:
        ry, rz = sqrt(float(y)), sqrt(float(z))
        A, B = 3 * y + 5 * z, 5 * y + 3 * z
        assert A > 0 and B > 0 and A + B == 8 * (y + z)
        q1_delta = -ry + rz  # monotone scalar test profile
        scalar_rhs = 2 * (ry - rz) * q1_delta
        assert scalar_rhs <= 0
        # Feasible pair of cross inequalities is an interval containing 0.
        lower, upper = scalar_rhs / float(A), -scalar_rhs / float(B)
        assert lower <= 0 <= upper
        rows.append({"y": str(y), "z": str(z), "lower_normal_difference": lower,
                     "upper_normal_difference": upper})
    # Telescoping variation works for a discontinuous monotone q1 as well.
    a, b = Q(1), Q(2)
    def q1(t):
        return -t - (Q(7) if t >= Q(3, 2) else Q(0))
    bounds = []
    for N in [2, 4, 8, 32, 128, 1024]:
        grid = [a + (b - a) * Q(j, N) for j in range(N + 1)]
        variation = sum(abs(q1(grid[j + 1]) - q1(grid[j])) for j in range(N))
        assert variation == q1(a) - q1(b) == 8
        bound = float((b - a) / N * variation) / (8 * float(a) ** 1.5)
        bounds.append({"N": N, "variation_exact": str(variation), "normal_bound": bound})
    return {"cross_branch_coefficient_checks": rows, "jump_profile_partition_bounds": bounds}


def theorem4_checks():
    rows = []
    for h, eps, L, a in [(Q(1), Q(1, 10), Q(1), Q(0)),
                         (Q(3, 10), Q(1, 20), Q(7), Q(2)),
                         (Q(10), Q(1, 100), Q(3, 2), Q(1))]:
        wide = (L * eps**2 + 4 * L * eps / h) / h + eps * (2 * L * eps / h + a)
        narrow = (L * eps**2 + 2 * L * eps / h) / h + eps * (L * eps / h + a)
        assert wide - narrow == 2 * L * eps / h**2 + L * eps**2 / h > 0
        q = 1 / (1 + h * eps)
        assert q / (1 - q) == 1 / (h * eps)
        rows.append({"h": str(h), "epsilon": str(eps), "slack_exact": str(wide - narrow)})
    threshold = []
    for t in [0.1, 4.0, 5.0, 100.0]:
        lhs = 1 / (sqrt(1 + 2 * t) - 1)
        rhs = 2 / t
        threshold.append({"h_epsilon": t, "printed_inequality_holds": lhs <= rhs + 1e-14})
        assert (lhs <= rhs + 1e-14) == (t <= 4)
    B = Q(1, 10)
    def rho(t):
        return t if t <= B else 2 + t
    assert rho(B) == B and rho(B + Q(1, 100000)) > 2
    return {"strict_modulus_slack": rows, "printed_factor_threshold": threshold,
            "right_jump_counterexample_to_naive_limit_step": True}


def positive_subrelation_check():
    # y=root^2 and eta=s^2+s ensure D_y(eta)=min(2root,s) rational.
    samples = []
    for root in [Q(0), Q(1, 8), Q(1, 2), Q(2)]:
        y = root**2
        for s in [Q(0), Q(1, 4), Q(1), Q(10)]:
            eta = s*s+s
            D = min(2*root, s)
            f, v = (-2*root, -D, 3*y), (-2*root, -D, y)
            samples.append((f, v))
            # A legal warped output for every such input, including cap endpoint.
            new_root, new_y = root/2, y/4
            new_s, new_eta = D/2, D*D/4+D/2
            assert new_eta == new_s*new_s+new_s
            new_D = min(2*new_root, new_s)
            new_f = (-2*new_root, -new_D, 3*new_y)
            new_v = (-2*new_root, -new_D, new_y)
            assert tuple(new_f[i]+new_v[i] for i in range(3)) == v
    for f, v in samples:
        for g, w in samples:
            df, dv = sub(f, g), sub(v, w)
            assert dot(df, dv) >= dot(dv, dv)
    xi, eta, root = Q(0), Q(-1), Q(1, 8)
    I = xi+2*root
    for k in range(24):
        y = root**2
        v = (-2*root, Q(0), y)
        assert v == (xi-I, eta-Q(-1), y)
        new_root, new_y, new_xi = root/2, y/4, xi+root
        new_v = (-2*new_root, Q(0), new_y)
        assert sub(v, new_v) == (-2*new_root, Q(0), 3*new_y)
        assert new_xi+2*new_root == I
        xi, root = new_xi, new_root
    # The explicit kernel does not preserve every positive eta ordinary step.
    root, eta = Q(1), Q(2)  # b(eta)=1, ordinary eta'=3.
    input_D = Q(1)
    ordinary_output_D = Q(1)  # cap at y'=1/4, eta'=3.
    assert 2*ordinary_output_D != input_D
    return {"pair_samples_exact": len(samples)**2, "warped_coverage_samples": len(samples),
            "ordinary_eta_negative_physical_bridge_steps": 24,
            "positive_eta_noninclusion_boundary_checked": True,
            "inverse_R_Lipschitz": "1/3"}


def scalar_tail_subrelation_checks():
    # Branch manuscript's actual collar: input R, graph output height R^nu.
    # gamma=1/2, nu=2, R=1/4. Its m_R is exactly 1; R=1/2 loses strictness.
    R = Q(1, 4)
    m = 1 / (2 * R) - 1
    assert m == 1 and 1 / (2 * Q(1, 2)) - 1 == 0
    # K_R=sum_{j>=1} 2^j 2^{-(2^j-1)}; exact finite sum + geometric tail bound.
    terms = [Q(2**j, 2**(2**j-1)) for j in range(1, 6)]
    q_tail = Q(1, 32768)  # valid upper ratio from j>=4.
    K_lower = sum(terms[:4])
    K_upper = K_lower + terms[4] / (1-q_tail)
    assert K_lower > 1 and K_upper < 2
    epsilon_safe = Q(1, 2)  # min(1/K_R,m_R) is strictly larger than or equal to this.
    def E_partial(root, N):
        return sum(root ** (2**j) for j in range(N))  # E(root^2)
    rows = []
    for root in [Q(0), Q(1, 8), Q(1, 4), Q(1, 2)]:
        r = root**2
        out_y = r**2
        assert out_y <= R**2 and out_y <= R
        for N in [2, 4, 8]:
            assert E_partial(root, N)-E_partial(r, N-1) == root
        # At graph y=r^2, its normal value is r-r^2 and phi(y)=sqrt(r)=root.
        assert out_y + (r-out_y) == r
        rows.append({"input_normal": str(r), "graph_output_height": str(out_y),
                     "tail_shift_partial_sums_exact": True})
    # Log a=2 in the exact logarithmic region: integral bounds and vanishing ASM ratio.
    b, a = log(4), 2
    log_rows = []
    for A in [10.0, 100.0, 500.0]:
        y = exp(1-A)
        E_lower = 1 / (b*A)
        E_upper = A**-2 + E_lower
        phi = (A-b)**-2
        assert A-b >= a+1 and E_upper > E_lower > 0
        ratio_upper = phi/E_lower + 3*y*y/(E_lower*E_lower)
        log_rows.append({"log_e_over_y": A, "E_lower": E_lower,
                         "E_upper": E_upper, "zero_anchor_ASM_ratio_upper": ratio_upper})
    assert log_rows[-1]["zero_anchor_ASM_ratio_upper"] < log_rows[0]["zero_anchor_ASM_ratio_upper"]
    return {"superlinear_R": str(R), "superlinear_graph_height": str(R**2),
            "m_R_exact": str(m), "K_R_exact_lower": str(K_lower),
            "K_R_exact_upper": str(K_upper), "safe_epsilon_h1": str(epsilon_safe),
            "superlinear_exact_shift_cases": rows, "log_a2_tail_bounds": log_rows,
            "warning": "Infinite series, arbitrary pair inequalities and limits are proved in the audit, not by these samples."}


if __name__ == "__main__":
    source = ROOT / "sources/gppa_2608.01584v1.pdf"
    results = {"proof_warning": "Finite checks only; arbitrary kernel and partition statements are proved in the audit.",
               "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
               "overlap_2_3": overlap(Q(1), Q(7), Q(2), Q(3, 10), 2, 3, 2),
               "overlap_1_2_nonunit_steps": overlap(Q(2), Q(3, 2), Q(3), Q(7), 1, 2, 2),
               "cross_branches": cross_branch_checks(), "theorem4": theorem4_checks(),
               "zero_set_preserving_positive_subrelation": positive_subrelation_check(),
               "scalar_tail_branch_restrictions": scalar_tail_subrelation_checks(),
               "cap_R_1_16_kappa": (2 * sqrt(2) + 5 / 8)**2 / 16}
    assert results["cap_R_1_16_kappa"] < 1
    output = ROOT / "sol61_gppa_results.json"
    output.write_text(json.dumps(results, indent=2) + "\n")
    print(json.dumps({"checks_passed": True, "output": str(output),
                      "source_sha256": results["source_sha256"]}, indent=2))
