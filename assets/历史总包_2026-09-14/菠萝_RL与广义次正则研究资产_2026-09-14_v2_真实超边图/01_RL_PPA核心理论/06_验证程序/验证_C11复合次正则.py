"""Standard-library checks for the C11 composite report; not proof substitutes."""
import math


def scaled_log_prox(input_log_inverse, step=1.0):
    # t_in = exp(-input_log_inverse), y=t_out/t_in.
    # y [1+step(1+input_log_inverse-log y)] = 1.
    lo, hi = 0.0, 1.0
    for _ in range(100):
        y = (lo + hi) / 2.0
        value = y * (1.0 + step * (1.0 + input_log_inverse - math.log(y)))
        if value > 1.0:
            hi = y
        else:
            lo = y
    return (lo + hi) / 2.0


print("Logarithmic PPA exact scalar equation; expected last ratio -> 1")
print("input exponent k, output/input, asymptotic ratio")
for k in (10, 30, 100, 300, 1000, 10000):
    scale = k * math.log(10.0)
    ratio = scaled_log_prox(scale)
    print(k, f"{ratio:.12g}", f"{ratio * scale:.12g}")
    residual = ratio * (2.0 + scale - math.log(ratio)) - 1.0
    assert abs(residual) < 1e-13

for z in (0.0, 0.1, 0.5, 0.9):
    lhs = 1.0 + 4.0 * z / (1.0-z)**2
    rhs = ((1.0+z)/(1.0-z))**2
    assert abs(lhs-rhs) < 1e-10
print("Hypomonotone-to-RL squared constant identity: PASS")

a = 1.1
lower, upper = 2*a-math.sqrt(10.0), 2*a+math.sqrt(10.0)
assert lower < 0 < upper
assert a-1 > 0
print("C11 strong-minimum Clarke interval:", lower, upper)
print("All standard-library checks passed.")
