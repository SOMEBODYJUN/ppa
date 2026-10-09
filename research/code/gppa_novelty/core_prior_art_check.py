"""Finite arithmetic checks accompanying core_prior_art.md; no novelty proof."""
from decimal import Decimal, localcontext
from fractions import Fraction
import json


def main():
    linear = []
    for L in (Fraction(1, 2), Fraction(1), Fraction(3, 2), Fraction(2)):
        epsilon = max(Fraction(0), (L * L - 1) / 2)
        submono = max(Fraction(0), (L * L - 1) / 4)
        linear.append({"L": str(L), "epsilon_alpha_half": str(epsilon),
                       "submonotonicity_tau": str(submono),
                       "in_LTT_v2_epsilon_range": epsilon < 1})
    assert linear[2]["epsilon_alpha_half"] == "5/8"
    assert linear[2]["submonotonicity_tau"] == "5/16"
    assert not linear[3]["in_LTT_v2_epsilon_range"]
    q = Fraction(3, 5)
    thresholds = {"q": str(q), "LM2012_distance_power": str(q / (2 * (1-q))),
                  "shell_series_power": str(2 - 1/q)}
    with localcontext() as ctx:
        ctx.prec = 70
        sf = []
        # A=1, gamma=1/2, nu=3. Here ||T(0,r)||^2=r+r^6 exactly.
        for j in (2, 4, 8, 12):
            r = Decimal(10) ** (-j)
            output_ratio = (r + r**6).sqrt() / r
            # Minimal alpha=1/2 violation for this anchor pair:
            # ||Tz||^2 + ||z-Tz||^2 <= (1+epsilon)||z||^2.
            epsilon_needed = ((r + r**6) + (r + (r-r**3)**2)) / (r*r) - 1
            sf.append({"r": str(r), "output_input_ratio": str(output_ratio),
                       "epsilon_needed_alpha_half": str(epsilon_needed)})
        # Pure logarithmic B(t)=log(1/t)^(-a), tau(t)=exp(-1)t.
        # Ratio sum/B(t) >= integral/B(t) = log(1/t)/(a-1).
        a = Decimal(2)
        logarithmic = [{"log_inverse_t": n,
                        "uniform_sum_ratio_lower_bound": str(Decimal(n)/(a-1))}
                       for n in (10, 100, 1000)]
    print(json.dumps({"linear_reduction": linear, "shell_vs_naive": thresholds,
                      "SF_anchor": sf, "LMZ_shrinking_log_obstruction": logarithmic},
                     ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
