# C303 transient normal-error contribution to the angle bootstrap

## Purpose and status

The normal recursion after a finite prefix can give

    q_k = ||w_k|| <= M h_k + Q_0 exp(-gamma(t_k-T_*)),
    Q_0 = C_q h_0^2,                                  (TE1)

where t_k=sum_{j<k} h_j and the estimate is used for k>=K_* with
K_* chosen as the first drop threshold (or an explicitly bounded enlargement)
and t_{K_*}>=T_*. The second term is a transient inherited from the finite
prefix. It cannot simply be relabeled O(h_k), because h_k decays only
polynomially while the transient decays in physical time.

This note gives the correct angle super-solution. The status remains
continue validation: (TE1) and the angular one-step estimate must hold
uniformly before first exit.

## Modified one-step estimate

On the closed stopping tube, the polar formula and bounded geometry give the
two-sided estimate

    theta_{k+1}-theta_k
       <= A h_k phi(theta_k)
          + B h_k q_k
          + C_0 h_k^2,

    theta_{k+1}-theta_k
       >= c h_k phi(theta_k)
          - B_- h_k q_k
          - C_- h_k^2.                              (TE2)

where phi(s)=s exp(-s^2). Substituting (TE1),

    theta_{k+1}-theta_k
       <= A h_k phi(theta_k)
          + C_1 h_k^2
          + C_2 h_k h_0^2 exp(-gamma(t_k-T_*)).       (TE3)

for k>=K_*. The last term is summable in k because the physical-time
increments are h_k.

## Error tail and corrected z-variable

Define

    e_k = h_k^2 + h_k h_0^2 exp(-gamma(t_k-T_*)),
    E_k = sum_{j>=k} e_j,
    E_* = E_{K_*},
    z_k = theta_k - C_1(E_* - E_k),                     (TE4)

where the same positive constant C_1 is increased once so that it dominates
the coefficients in both the upper and lower error bounds. Thus, with

    e_k=h_k^2+h_k h_0^2 exp(-gamma(t_k-T_*)),

the two-sided remainder is bounded by C_1 e_k.
Then E_k-E_{k+1}=e_k and, using the lower side of (TE2),

    theta_k >= theta_{K_*}-C_1(E_*-E_k)
              >= theta_{K_*}-C_1E_*.

Consequently, if theta_{K_*}>=3/2 and C_1E_*<1/4, then theta_k>1. More
precisely, the z-variable below satisfies z_k>=theta_{K_*}-2C_1E_*>1.
The upper side gives

    z_{k+1}-z_k
       <= A h_k phi(theta_k)
       <= A h_k phi(z_k),                               (TE5)

whenever z_k>=1 and theta_k>=z_k. The same monotonicity argument as in the
v4 bootstrap applies, but with E_* containing the transient tail.

The ordinary part satisfies

    sum_{j>=K_*} h_j^2 < infinity.

For the transient part, since t_{j+1}-t_j=h_j and h_j is decreasing,

    sum_{j>=k} h_j exp(-gamma(t_j-T_*))
       <= C_gamma exp(-gamma(t_k-T_*)),                 (TE6)

for k>=K_*. One proof splits off the first term and compares the remaining
sum with the integral of exp(-gamma u) in physical time. Consequently,

    E_* <= C h_0^2,                                     (TE7)

with C independent of the unbounded lifted angle and of k. Choose h_0 so
C_1 E_* < 1/4 and start the tail with theta_{K_*}>=3/2; then z_k>1.

## Exponential super-solution and exact schedule gate

Put E=C_1 E_* and U_k=exp((z_k+E)^2/2). If z decreases, U decreases. If
delta_k=z_{k+1}-z_k>0, (TE5) gives

    delta_k <= A h_k z_k exp(-z_k^2).

The mean-value theorem yields

    U_{k+1}-U_k
       <= C_U h_k,

because the coefficient is bounded by a polynomial times

    exp(-z_k^2/2 + (E+1) z_k + (E+1)^2/2).

Therefore

    exp(theta_k^2/2) <= U_k <= U_{K_*}+C_U(t_k-t_{K_*}),
    theta_k^2 <= C + 2 log(1+t_k).                        (TE8)

Thus

    m(theta_k) >= c(1+t_k)^(-2),
    phi(theta_k) >= c(1+t_k)^(-2).

With t_k asymp k^(1-alpha),

For a uniform first-contact comparison starting already at K_*, use the
explicit bound t_k<=C h_0(1+s^(1-alpha)), s=k+1. Splitting according to
u=h_0s^(1-alpha)<=1 or u>=1 gives

    sup_{k>=K_*} h_k(1+t_k)^2 <= C h_0,                    (TE9a)

because the large-u exponent is 2-3alpha<0. Hence, after reducing h_0,
the ratios h_k/m(theta_k) and h_k/phi(theta_k) are small for every
k>=K_*, not merely asymptotically. The transient contribution satisfies

    sup_{k>=K_*} h_0^2 exp(-gamma(t_k-T_*))(1+t_k)^2 <= C h_0^2. (TE9b)

Equivalently, with t_k asymp k^(1-alpha), the asymptotic form is

    h_k/m(theta_k), h_k/phi(theta_k)
       = O(k^(2-3 alpha)) -> 0       iff alpha>2/3.       (TE9c)

The transient does not change the p=2 exponent or the alpha threshold; it
only changes the finite constant E_* in z_k.

## Exact conclusion and remaining obstruction

It is valid to use the v4 p=2 super-solution after replacing the pure O(h_k^2)
error tail by the explicit e_k in (TE4). The transient is harmless because its
coefficient is h_k and its physical-time exponential is integrable.

The minimum additional obligations are:

1. Prove (TE1) uniformly for every pre-exit orbit in the common open set,
   with Q_0=O(h_0^2) after the finite-prefix construction.
2. Derive (TE2) with its B h_k q_k term explicitly; do not suppress q_k
   before inserting (TE1).
3. Start the bootstrap at K_* with t_{K_*}>=T_* and a strict angular margin.
   The finite prefix remains covered by the separate margin lemma.
4. Keep the transient tail in the first-contact comparison if the normal
   error enters the radial or angular face derivative; the same e_k tail is
   summable and does not alter alpha>2/3.

No new fatal obstruction was found. The status is **continue validation**.
