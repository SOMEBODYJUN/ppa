# C303 sharp schedule to common-domain audit

Status: **continue validation**. This is an independent check of the proposed
(W_k=e^{z_k^2}) schedule envelope against the radial and angular first-contact
conditions. It does not upgrade the C303 bridge.

## Exact obligation

Assume the sharp conditional envelope gives, for a fixed
(1/2<\alpha<1) and some (\varepsilon>0),

    exp(theta_k^2) <= C_epsilon (1+t_k)^(1+epsilon),

with

    alpha > (1+epsilon)/(2+epsilon),                         (A1)

and assume the finite-prefix normal estimate starts at the same index (K_*)
used by the tail bootstrap:

    q_k <= M h_k + Q_0 exp(-gamma(t_k-T_tr)),
    Q_0 <= C_q h_0^2,
    T_tr=t_{K_*} <= T_* .                                   (A2)

The last bound (T_*<\infty) must be uniform in (h_0) for fixed (\alpha); it
is supplied by the finite-prefix construction through
(t_{K_*}=O(\alpha/[\gamma(1-\alpha)])), but it is not automatic from (A2)
without that construction.

Set

    mu_rad(theta)=m_0 exp(-theta^2+theta),
    mu_ang(theta)=phi(theta)=theta exp(-theta^2).

The common-domain gate is to prove

    (h_k+q_k)/mu_rad(theta_k) -> 0,
    (h_k+q_k)/mu_ang(theta_k) -> 0,                           (A3)

and to make both ratios uniformly small after reducing (h_0), so that the
first-contact derivative or endpoint barrier has a strict positive margin.

## Ratio calculation with the transient retained

From the sharp envelope and the tail cutoff (theta_k>=theta_*>1),

    mu_rad(theta_k), mu_ang(theta_k)
       >= c_epsilon (1+t_k)^(-(1+epsilon)).                 (A4)

Consequently, using (A2), each ratio in (A3) is bounded by a constant times

    h_k (1+t_k)^(1+epsilon)
      + h_0^2 exp(-gamma(t_k-T_tr))(1+t_k)^(1+epsilon).       (A5)

For (h_k=h_0(k+1)^(-alpha)), write
(u_k=h_0(k+1)^(1-alpha)). If (u_k<=1), the first term in (A5) is
(O(h_0(k+1)^(-alpha))). If (u_k>=1), it is bounded by

    C h_0^(2+epsilon)
      (k+1)^((1+epsilon)(1-alpha)-alpha),

whose exponent is negative by (A1); its maximum occurs at the transition and
is (O(h_0^{1/(1-alpha)})), hence (O(h_0)) for (h_0<1). Thus

    sup_{k>=K_*} h_k(1+t_k)^(1+epsilon) <= C h_0.             (A6)

For the transient term put (u=t_k-T_tr>=0). Since (T_tr<=T_*),

    exp(-gamma u)(1+t_k)^(1+epsilon)
       <= C_{gamma,epsilon,T_*}(1+u)^(1+epsilon)e^{-gamma u}
       <= C_{gamma,epsilon,T_*},                            (A7)

so its contribution is at most (C h_0^2). Therefore the ratios are uniformly
(O(h_0)+O(h_0^2)), and they tend to zero as (k\to\infty). For the current
(p=2) route, take (\varepsilon=1) in this calculation and the condition
reduces to (\alpha>2/3), reproducing TE9a--TE9b.

There is no transient counterexample under the explicit finite-prefix time
bound. A counterexample would require allowing (T_tr) to grow with (h_0^{-1})
or with the unbounded initial lift, so that (Q_0(1+T_tr)^{1+\varepsilon}) is not
small; the present finite-prefix lemma excludes that by fixing (T_*) first.

## Contact-angle comparison

At a first (\tau)-contact, the displacement estimate gives

    |theta(tau_*)-theta_k| <= C h_k.

For either margin (mu\in\{\mu_rad,\mu_ang\}),

    |(log mu)'(s)| <= C(1+s)  for s>=theta_*,

so the sharp envelope implies (h_k(1+theta_k)\to0), and hence

    mu(theta(tau_*))/mu(theta_k) -> 1.                         (A8)

This validates the use of (m_face(theta(tau_*))) in CS6 and
(phi(theta(tau_*))) in CS7, provided the contact remains in the common
outer strip.

## Outer-strip transfer under the sharp envelope

The existing common-domain proof uses the (p=2) estimate
(e^{theta_k}\le C(1+t_k)). Under the sharp envelope it must be replaced by

    e^{theta_k} <= C_epsilon (1+t_k)^((1+epsilon)/2).        (A9)

Then the normalized-coordinate increment is
(O(h_k e^{theta_k})). The large-(u_k) exponent is

    ((1+epsilon)/2)(1-alpha)-alpha,

which is negative whenever
(alpha>(1+epsilon)/(3+epsilon)). This is weaker than (A1), so every fixed
(1/2<alpha<1) admits an epsilon satisfying both conditions. Thus the sharp
schedule can, in principle, preserve the outer-strip gate, but this transfer is
not yet written into `c303_common_stopping_domain.md`; that file correctly keeps
its main theorem on the (p=2, alpha>2/3) route and warns against mixing the two.

## Independent verdict

The (q_k+h_k=o(m_face(theta_k))) and
(q_k+h_k=o(phi(theta_k))) obligations are mathematically consistent, including
the transient term, **provided** the finite-prefix index is the common (K_*) and
(T_tr=t_{K_*}) is uniformly bounded before (h_0\to0). The W schedule remains
conditional because three transfer obligations are still external to the current
common-domain proof:

1. finite-prefix margin and normal-ball construction for every fixed
   (1/2<alpha<1), not only the currently recorded (alpha>2/3) statement;
2. the (p=(1+epsilon)/2) outer-strip (q)-increment estimate (A9);
3. the same source/cutoff/lift gates and a uniform first-contact displacement bound.

No fatal counterexample was found under these explicit hypotheses. This is a
**continue validation** result, not a major-contribution certification.
