# C303 discrete bridge v4: non-circular angular bootstrap

## Status

This appendix supplies the missing discrete upper-angle estimate used by the
implicit tau-path barrier in the v3 report. It restores the fixed schedule
gate alpha > 2/3, but only under the conditional HJ tube and normal-error
bounds stated below. It does not verify the HJ cutoff from the original
source and it does not upgrade C303 to a theorem.

The key point is to absorb the summable h_k^2 angular error before estimating
the exponential Lyapunov quantity. No estimate of h_k=o(m(theta_k)) is used
to obtain the angle upper bound.

## Conditional input

Let h_k=h_0(k+1)^(-alpha), with 1/2<alpha<1, and
t_k=sum_{j<k} h_j. Work up to the first contact with either radial boundary
or the entrance boundary theta=theta_0. Assume theta_k>=theta_0>=1 on this
pre-contact interval and that the normal-error estimate already holds there:

    |w_k| <= M h_k.

The latter follows from the implicit resolvent expansion on the closed tube,
independently of the boundary-margin comparison. Assume also the one-step
angular upper estimate

    Delta theta_k
       := theta_{k+1}-theta_k
       <= C_1 h_k phi(theta_k) + C_2 h_k^2,                    (A1)

where

    phi(s)=s exp(-s^2).

This estimate follows from the polar increment formula, the HJ bound
Y_theta <= C theta exp(-theta^2), and h_k |w_k|=O(h_k^2).

## Error absorption

Set

    E_k = sum_{j>=k} h_j^2,
    E_0 = sum_{j>=0} h_j^2,
    A = C_2,
    z_k = theta_k - A(E_0-E_k)
        = theta_k - A sum_{j<k} h_j^2.                         (A2)

Then E_k-E_{k+1}=h_k^2 and hence

    z_{k+1}-z_k
       = Delta theta_k - A h_k^2
       <= C_1 h_k phi(theta_k).                                (A3)

Choose h_0 small enough that A E_0 <= 1/2, and start in a slightly
higher tail theta_0>=3/2. Before the entrance contact, theta_k>=theta_0,
so z_k>=theta_0-AE_0>=1. The function phi is decreasing on [1,infinity).
Because z_k<=theta_k, (A3) gives

    z_{k+1}-z_k <= C_1 h_k phi(z_k).                            (A4)

This is the only comparison needed for the upper bootstrap. In particular,
it does not assume that the shrinking-boundary margin is already larger than
the step.

## Exponential super-solution

Let E=A E_0 and define

    U_k = exp((z_k+E)^2/2).

If z_{k+1}<=z_k then U_{k+1}<=U_k. If z_{k+1}>z_k, write
delta_k=z_{k+1}-z_k. By (A4),

    0<delta_k <= C_1 h_k z_k exp(-z_k^2).

After decreasing h_0 once more, delta_k<=1. The mean-value theorem gives a
constant C_U depending only on C_1,E such that

    U_{k+1}-U_k
      <= C_U h_k.                                               (A5)

Indeed, for some xi_k in [z_k,z_k+delta_k],

    U_{k+1}-U_k
      = (xi_k+E) exp((xi_k+E)^2/2) delta_k,

and the right side is bounded by

    C_1 h_k (z_k+1)(z_k+E)
       exp[-z_k^2+(z_k+E+1)^2/2].

The factor multiplying h_k is bounded on z_k>=1, since its exponent is

    -z_k^2/2 + (E+1)z_k + (E+1)^2/2

and the Gaussian dominates the polynomial. Thus, by induction up to first
contact,

    U_k <= U_0 + C_U t_k.                                       (A6)

Since

    theta_k = z_k + A(E_0-E_k) <= z_k+E,

we have exp(theta_k^2/2)<=U_k. Therefore

    theta_k^2 <= 2 log(U_0+C_U t_k)
               <= C_theta + 2 log(1+t_k).                      (A7)

The coefficient 2 is explicit. No unknown exponent p is introduced.

## Consequences for the HJ scales

From (A7),

    exp(-theta_k^2) >= c_theta (1+t_k)^(-2).

Since theta_k>=theta_0>=1, the angular drift and radial margin obey

    phi(theta_k)
       = theta_k exp(-theta_k^2)
       >= c_phi (1+t_k)^(-2),                                  (A8)

    m(theta_k)
       = m_0 exp(-theta_k^2+theta_k)
       >= c_m (1+t_k)^(-2).                                    (A9)

For alpha<1,

    t_k asymp k^(1-alpha),
    h_k = h_0(k+1)^(-alpha).

Consequently,

    h_k / m(theta_k) = O(k^(2-3 alpha)),
    h_k / phi(theta_k) = O(k^(2-3 alpha)).                      (A10)

Both ratios tend to zero exactly when

    alpha > 2/3.                                                (A11)

The same condition also implies alpha>1/2, so the summability used in E_0
and in the h_k^2 angle error is automatic. Thus the v3 barrier can use the
original schedule interval alpha in (2/3,1), provided the conditional
pre-contact estimates have been established.

## Interaction with the tau-path barrier

The bootstrap is performed only until the first contact, so it does not
presume the tube invariance that it is later used to prove. Once (A7)--(A10)
are available, the tau-path first-contact estimate has

    s_i(x_k)
       <= -tau_* h_k m(theta_*)
          + C tau_* h_k |w_{tau_*}|
          + C (tau_* h_k)^2.

The path displacement gives theta_*=theta_k+O(tau_* h_k). Since
the logarithmic derivative of m is O(1+theta), (A7) implies
m(theta_*) asymp m(theta_k) after increasing the finite-prefix threshold.
The uniform tau-path bound |w_tau|=O(h_k) then makes the right side negative
for every tau_*>0, because h_k=o(m(theta_k)). The entrance-angle contact is
handled by Y_theta(theta_0)>0 with the same tau_* factor.

## Remaining minimum obligations

This appendix closes only the angular schedule comparison. A complete C303
bridge still needs:

1. a source-checked cutoff with globally bounded g, H, and D^3f and with
   the exact HJ formula on the entire closed tail tube;
2. the uniform implicit-resolvent expansion yielding |w_k|=O(h_k) before
   first contact and sup_tau |w_tau|=O(h_k);
3. an explicit finite-prefix reference orbit and one common open phase-space
   neighborhood with strict margins;
4. the final angle-divergence and modulo-2pi omega-limit argument.

The correct status remains **continue validation**.
