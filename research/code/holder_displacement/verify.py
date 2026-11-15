"""Verify the finite scaling and limit algebra for C293–C294."""

from decimal import Decimal, localcontext
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
import platform


def check_geometric_sum():
    checks = 0
    for exponent in range(2, 21):
        for numerator in range(1, 41):
            t = Fraction(numerator, 41)
            assert (1 - t**exponent) / (1 - t) == sum(t**j for j in range(exponent))
            checks += 1
    return checks


def check_scaling_and_limit():
    with localcontext() as ctx:
        ctx.prec = 80
        output = []
        for gamma in map(Decimal, ('0.5', '0.9', '0.99', '0.9999', '0.999999')):
            epsilon = 1 - gamma
            lip = 1 / gamma
            radius = lip ** (-gamma / epsilon) / 2
            assert abs(lip**gamma * (2 * radius)**epsilon - 1) < Decimal('1e-76')
            mixing = (lip - 1) / 3
            scale = mixing * radius / epsilon
            expected = gamma ** (gamma / epsilon - 1) / 6
            assert abs(scale - expected) < Decimal('1e-73')
            output.append(str(+scale))
        target = Decimal(-1).exp() / 6
        assert abs(Decimal(output[-1]) - target) < Decimal('1e-6')
        return output


if __name__ == '__main__':
    print(json.dumps({
        'claim_versions': ['C293-v1', 'C294-v1'],
        'python': platform.python_version(),
        'script_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
        'precision': 'Fraction exact and 80-digit Decimal; no random inputs',
        'integer_exponent_checks': check_geometric_sum(),
        'rescaled_lower_coefficients_for_kappa_4_delta_1': check_scaling_and_limit(),
    }, indent=2))
