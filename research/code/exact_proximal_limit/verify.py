"""High-precision finite checks of the backward chord interpolation."""

import hashlib
import json
import platform
from pathlib import Path

import mpmath as mp


def norm(vector):
    return mp.sqrt(mp.fdot(vector, vector))


def ray(t):
    radius = 1 + 1 / t
    return mp.matrix([radius * mp.cos(t), radius * mp.sin(t)])


def tangent(t):
    radius = 1 + 1 / t
    radial = -1 / t**2
    return mp.matrix([
        radial * mp.cos(t) - radius * mp.sin(t),
        radial * mp.sin(t) + radius * mp.cos(t),
    ])


def check_chord(t, step):
    current, direction = ray(t), tangent(t)
    rho = mp.mpf('0.01') * mp.exp(-t**2)
    a_prime = -4 * t * rho**2
    target = -step * a_prime

    def projection(h):
        return mp.fdot(current - ray(t - h), direction)

    h_first = target / mp.fdot(direction, direction)
    h = mp.findroot(lambda h: projection(h) - target, (h_first, h_first * 2), verify=False)
    assert 0 < h < mp.mpf('0.25')
    assert abs(projection(h) / target - 1) < mp.mpf('1e-55')
    velocity = (ray(t - h) - current) / step
    assert abs(mp.fdot(velocity, direction) / a_prime - 1) < mp.mpf('1e-55')

    normal = mp.matrix([-direction[1], direction[0]]) / norm(direction)
    normal_gradient = mp.fdot(velocity, normal)
    tangential_gradient = a_prime * direction / mp.fdot(direction, direction)
    reconstructed = tangential_gradient + normal_gradient * normal
    assert norm(velocity - reconstructed) < mp.mpf('1e-110')
    assert norm(ray(t - h) - (current + step * reconstructed)) < mp.mpf('1e-110')

    def normal_square(offset):
        return (rho + normal_gradient * offset / (2 * rho))**2

    assert abs(mp.diff(normal_square, 0) - normal_gradient) < mp.mpf('1e-110')

    return {'parameter': str(t), 'proximal_step': str(step), 'backward_increment': mp.nstr(h, 14)}


if __name__ == '__main__':
    with mp.workdps(125):
        results = [check_chord(mp.mpf(t), mp.mpf(step)) for t in ('1', '2', '4', '7', '8') for step in ('0.25', '1', '3')]
    print(json.dumps({
        'claim_versions': ['C297-v1', 'C298-v1', 'C299-v1'],
        'python': platform.python_version(),
        'mpmath': mp.__version__,
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'arithmetic': '125-digit mpmath, deterministic; no random seed',
        'scope': 'finite analytic spiral chord, kernel slope and jet reconstruction only',
        'trials': results,
    }, indent=2))
