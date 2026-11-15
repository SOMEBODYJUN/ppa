"""Check finite scalar envelope and unit-ball Hölder normalization formulas."""

from fractions import Fraction as F
from hashlib import sha256
from itertools import product
import json
import math
from pathlib import Path
import platform


def check_envelopes():
    count = 0
    sites = tuple(map(F, ('0', '1/2', '1', '5/4')))
    for values in product(range(-3, 4), repeat=len(sites)):
        values = tuple(F(value, 3) for value in values)
        margin = max(abs(a - b) - abs(x - y) for x, a in zip(sites, values) for y, b in zip(sites, values))
        images = []
        for x, original in zip(sites, values):
            upper = max(v - abs(x - y) for y, v in zip(sites, values))
            lower = min(v + abs(x - y) for y, v in zip(sites, values))
            assert lower <= original <= upper and upper - lower <= margin
            corrected = sorted((upper - margin, F(0), lower + margin))[1]
            assert min(original, 0) <= corrected <= max(original, 0)
            assert abs(original - corrected) <= margin
            images.append(corrected)
        for x, a in zip(sites, images):
            for y, b in zip(sites, images):
                assert abs(a - b) <= abs(x - y)
        count += 1
    return count


def check_normalizations():
    count = 0
    for lipschitz in (1.01, 1.1, 2, 4, 10, 50):
        r = 2 ** (1 - 4 * lipschitz)
        for gamma in (0.01, 0.1, 0.5, 0.9, 0.99, 0.99999):
            epsilon = 1 - gamma
            mixing = -math.expm1(-epsilon * math.log(2)) / (1 - r)
            assert 0 < mixing < 1
            for delta in [2 * i / 100 for i in range(101)] + [r, 2 * r, 1e-30]:
                bound = min((1 + mixing * (2 * lipschitz - 1)) * delta, (1 - mixing) * delta + 2 * mixing * r)
                assert bound <= delta**gamma + 1e-14
                count += 1
    return count


if __name__ == '__main__':
    print(json.dumps({
        'claim_versions': ['C300-v1', 'C301-v1'],
        'python': platform.python_version(),
        'script_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
        'rational_scalar_envelopes': check_envelopes(),
        'binary64_unit_ball_scalar_inequalities': check_normalizations(),
        'arithmetic': 'Fraction exact and binary64 with 1e-14 slack, deterministic',
    }, indent=2))
