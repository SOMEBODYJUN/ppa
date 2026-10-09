#!/usr/bin/env python3
"""Finite checks for C219; standard library only.

90-digit Decimal arithmetic, exact rational Bernoulli coefficients, and an
Euler--Maclaurin tail with an analytic truncation bound. Floating calculations
are evidence for identities/constants; the Markdown proof supplies all infinite
claims. Run from any cwd. Output is written alongside this script.
"""
from decimal import Decimal, localcontext
from fractions import Fraction
from math import comb
from pathlib import Path
import json


PRECISION = 90
EM_ORDER = 20
EM_SHIFT = 256


def bernoulli_numbers(n):
    values = [Fraction(1)]
    for m in range(1, n + 1):
        values.append(
            -sum(Fraction(comb(m + 1, k)) * values[k] for k in range(m))
            / (m + 1)
        )
    return values


def decimal_fraction(value):
    return Decimal(value.numerator) / Decimal(value.denominator)


BERNOULLI = bernoulli_numbers(2 * EM_ORDER)


def atan(value):
    square = value * value
    power = value
    result = value
    n = 1
    tolerance = Decimal(10) ** (-(PRECISION + 2))
    while True:
        power *= -square
        term = power / Decimal(2 * n + 1)
        result += term
        if abs(term) < tolerance:
            return result
        n += 1


def pi():
    return 16 * atan(Decimal(1) / 5) - 4 * atan(Decimal(1) / 239)


def sin(value, pi_value):
    value %= 2 * pi_value
    if value > pi_value:
        value -= 2 * pi_value
    if value < -pi_value:
        value += 2 * pi_value
    result = value
    term = value
    n = 1
    tolerance = Decimal(10) ** (-(PRECISION + 2))
    while True:
        term *= -(value * value) / Decimal((2 * n) * (2 * n + 1))
        result += term
        if abs(term) < tolerance:
            return result
        n += 1


def tail2(u):
    """T(u)=sum (u+j)^-2 and a mathematical EM truncation bound.

    For 2m corrections the absolute remainder is at most
    |B_(2m)| v^(-2m-1). This follows from the periodic Bernoulli Fourier bound
    and integral of f^(2m); it excludes Decimal rounding error.
    """
    count = max(0, EM_SHIFT - int(u))
    v = u + count
    prefix = sum((u + j) ** -2 for j in range(count))
    tail = 1 / v + 1 / (2 * v * v)
    for m in range(1, EM_ORDER + 1):
        tail += decimal_fraction(BERNOULLI[2 * m]) / v ** (2 * m + 1)
    bound = abs(decimal_fraction(BERNOULLI[2 * EM_ORDER])) / v ** (
        2 * EM_ORDER + 1
    )
    return prefix + tail, bound


def fmt(value):
    return format(value, ".18E")


def main():
    with localcontext() as context:
        context.prec = PRECISION
        pi_value = pi()
        h = Decimal(4).ln()
        q_values = [Decimal(3), Decimal("3.5"), Decimal(10)]
        ks = [10, 100, 1000, 10000]
        c_cases = [
            ("zero", Decimal(0), True),
            ("calibrated_half_turn", pi_value / h**2, False),
            ("one_full_turn", 2 * pi_value / h**2, True),
            ("two_full_turns", 4 * pi_value / h**2, True),
            ("negative_full_turn", -2 * pi_value / h**2, True),
            ("off_resonance", 2 * pi_value / h**2 + Decimal("0.1"), False),
        ]
        residual_rows = []
        limit_rows = []
        maximum_truncation_bound = Decimal(0)
        rounding_tolerance = Decimal("1e-80")
        for q in q_values:
            assert q >= 3 / h
            y0 = (1 - h * q).exp()
            assert y0 <= Decimal(-2).exp()
            for k in ks:
                u = q + k
                t, error_t = tail2(u)
                t_next, error_next = tail2(u + 1)
                maximum_truncation_bound = max(
                    maximum_truncation_bound, error_t, error_next
                )
                recurrence_error = abs(t - t_next - u**-2)
                assert recurrence_error <= (
                    error_t + error_next + rounding_tolerance
                )
                remainder8 = t - 1 / u - 1 / (2 * u**2) - 1 / (6 * u**3)
                bound8 = 1 / (15 * u**5)
                assert abs(remainder8) <= bound8 + error_t + rounding_tolerance
                # Exact recurrence expression avoids cancellation in inverse tails.
                delta_inverse_t = u**-2 / (t * t_next)
                remainder10 = delta_inverse_t - 1 + 1 / (12 * u**2)
                bound10 = Decimal(701) / (1800 * u**4)
                assert abs(remainder10) <= bound10 + rounding_tolerance
                residual_rows.append(
                    {
                        "q": str(q), "k": k,
                        "recurrence_absolute_error": fmt(recurrence_error),
                        "sr8_error_to_bound": fmt(abs(remainder8) / bound8),
                        "sr10_error_to_bound": fmt(abs(remainder10) / bound10),
                        "sr10_scaled_correction": fmt(
                            (1 - delta_inverse_t) * u**2
                        ),
                        "em_truncation_bound": fmt(error_t),
                    }
                )
                rho = t / h**2
                rho_next = t_next / h**2
                radial_step = 1 / (h**2 * u**2)
                normal_step = Decimal(3) / 4 * y0 * Decimal(4) ** (-k)
                for name, c, resonant in c_cases:
                    phase = c * h**2 * delta_inverse_t
                    chord = (
                        radial_step**2
                        + 4 * rho * rho_next * sin(phase / 2, pi_value)**2
                    ).sqrt()
                    total_step = (chord**2 + normal_step**2).sqrt()
                    if resonant:
                        ratio = total_step / radial_step
                        actual_bound = (
                            radial_step + abs(c) / u**3 + normal_step
                        )
                        assert total_step <= actual_bound + rounding_tolerance
                        normalization = "step / (h^-2 u^-2), target 1"
                    else:
                        coefficient = 2 * abs(sin(c * h**2 / 2, pi_value)) / h**2
                        ratio = total_step * u / coefficient
                        normalization = "step*u / (2|sin(ch^2/2)|h^-2), target 1"
                    limit_rows.append(
                        {
                            "q": str(q), "k": k, "case": name,
                            "c": fmt(c), "resonant": resonant,
                            "phase": fmt(phase), "physical_step": fmt(total_step),
                            "normalization": normalization, "ratio": fmt(ratio),
                        }
                    )
        output = {
            "claim": "C219-v1",
            "precision_decimal_digits": PRECISION,
            "em_order": EM_ORDER, "em_shift": EM_SHIFT,
            "pi_method": "Machin arctangent series",
            "bernoulli_method": "exact Fraction recurrence",
            "rounding_absolute_tolerance": str(rounding_tolerance),
            "maximum_em_analytic_truncation_bound": fmt(
                maximum_truncation_bound
            ),
            "q_values": [str(q) for q in q_values],
            "k_values": ks,
            "residual_checks": residual_rows,
            "step_limit_checks": limit_rows,
            "scope": (
                "Finite Decimal checks, not an interval arithmetic certificate "
                "or proof of infinite length classification. SR7--15 provide "
                "the independent proof."
            ),
        }
        path = Path(__file__).with_suffix(".json")
        path.write_text(
            json.dumps(output, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        final_rows = [row for row in limit_rows if row["q"] == "3" and row["k"] == ks[-1]]
        print(json.dumps(
            {
                "result": "passed",
                "residual_checks": len(residual_rows),
                "step_checks": len(limit_rows),
                "maximum_em_truncation_bound": fmt(maximum_truncation_bound),
                "q3_final_ratios": {
                    row["case"]: row["ratio"] for row in final_rows
                },
            },
            indent=2, ensure_ascii=False
        ))


if __name__ == "__main__":
    main()
