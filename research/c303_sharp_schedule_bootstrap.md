# C303 candidate: a near-critical alpha>1/2 schedule gate

## Exact conditional claim

Assume that, after the finite prefix and before the first exit, the lifted angle
satisfies the two-sided one-step estimate

    theta_{k+1}-theta_k
       <= A h_k phi(theta_k) + R_k,
    phi(s)=s exp(-s^2),                              (SS1)

    theta_{k+1}-theta_k
       >= c h_k phi(theta_k) - R_k^- ,                (SS1^-)

where the nonnegative error tail is summable and is absorbed by

    E_k=sum_{j>=k} e_j,    sup_k E_k <= E_*<infinity,
    R_k <= C(e_k),\qquad R_k^-\le C(e_k),
    e_k=E_k-E_{k+1}.                                  (SS2)

For h_k=h_0(k+1)^(-alpha) with 1/2<alpha<1 (the infinite-time
schedule regime), the v4 estimate used
exp(z_k^2/2) and obtained the sufficient gate alpha>2/3. The sharper
super-solution below gives, for every fixed 1/2<alpha<1, an upper angle bound
strong enough for the first-contact comparison, provided the same normal,
outer-strip, and finite-prefix hypotheses hold.

This is a candidate schedule improvement, not a completed C303 theorem.

## Error absorption and the W super-solution

Set

    z_k=theta_k-C(E_0-E_k),    E_0=sum_{j>=0}e_j,

with C chosen to dominate the coefficients in (SS1) and (SS1^-). The lower
estimate gives

    theta_k >= theta_{K_*}-C(E_0-E_k).

Thus, after choosing the tail entrance margin and C E_0<=1/8,
z_k>=theta_{K_*}-2 C E_0>=5/4 until the first exit. This lower-side
obligation is essential: (SS1) alone cannot prove that the argument of
phi remains in its decreasing region. Then

    z_{k+1}-z_k <= A h_k phi(theta_k)
                 <= A h_k phi(z_k),                     (SS3)

whenever z_k>=1, because phi is decreasing on [1,infinity). Choose the finite
prefix and h_0 so that theta_{K_*}>=3/2 at the start of the tail; the lower
estimate above then preserves z_k>=1 until the first exit.

Let

    W_k=exp(z_k^2).

If delta_k=z_{k+1}-z_k<=0, then W_{k+1}<=W_k. If delta_k>0, (SS3) gives

    delta_k <= A h_k z_k exp(-z_k^2).

Since z^2 exp(-z^2) is bounded, h_0 can be decreased so that z_k delta_k<=1.
The elementary inequality exp(2z delta+delta^2)-1 <= C z delta then gives

    W_{k+1}-W_k
       <= C h_k z_k^2
        = C h_k log W_k.                                (SS4)

Define a continuous comparison

    S(t)=K(1+t) log(e+t).

Choose K large enough, depending only on C and the finite initial value
W_{K_*}, so that

    S'(t)=K[log(e+t)+(1+t)/(e+t)]
       >= 2 C [1+log S(t)]                              (SS5)

for all t>=0. This is possible because S'(t)/log S(t) tends to K as t
increases, and the compact initial interval is handled by enlarging K.
Since t_{k+1}-t_k=h_k and S' is increasing, (SS5) implies

    S(t_{k+1})-S(t_k) >= C h_k log W_k

whenever W_k<=S(t_k). Induction from W_{K_*}<=S(t_{K_*}) yields

    W_k <= K(1+t_k) log(e+t_k).                           (SS6)

The exact finite-step verification of (SS5) is a scalar inequality; it does
not use a boundary margin or h_k=o(m_face(theta_k)).

## Consequence for the shrinking HJ scales

Because theta_k=z_k+d_k with 0<=d_k<=C E_0, (SS6) implies, for every
epsilon>0,

    exp(theta_k^2)
       <= C_epsilon (1+t_k)^(1+epsilon).                  (SS7)

To make the epsilon loss explicit, fix the target epsilon>0 and put
eta=epsilon/4. Young's inequality gives

    2 d_k z_k <= eta z_k^2 + d_k^2/eta,

so (SS6) implies

    exp(theta_k^2)
      <= exp(d_k^2/eta) W_k^(1+eta)
      <= C_eta (1+t_k)^(1+eta) log(e+t_k)^(1+eta).

Since log(e+t)^(1+eta) <= C_eta (1+t)^eta, the right side is at most
C_epsilon (1+t_k)^(1+2 eta) <= C_epsilon(1+t_k)^(1+epsilon).
Therefore, with m_face(theta)=m_0 exp(-theta^2+theta),

    m_face(theta_k)=m_0 exp(-theta_k^2+theta_k)
       >= c_epsilon (1+t_k)^(-(1+epsilon)),

    phi(theta_k)=theta_k exp(-theta_k^2)
       >= c_epsilon (1+t_k)^(-(1+epsilon)),               (SS8)

since theta_k is bounded below by the tail cutoff.

With t_k asymp k^(1-alpha),

    h_k/m_face(theta_k), h_k/phi(theta_k)
       = O(k^((1+epsilon)(1-alpha)-alpha)).                (SS9)

For any fixed 1/2<alpha<1, choose epsilon>0 so small that

    alpha > (1+epsilon)/(2+epsilon).                       (SS10)

Then both ratios tend to zero. Thus the radial and angular first-contact
errors are dominated for every 1/2<alpha<1, whereas alpha=1/2 is not obtained
from the constant-shift estimate (SS7).

## Sharpness and what remains open

The threshold 1/2<alpha<1 is a sufficient near-critical gate under
(SS1), (SS1^-) and (SS2).
It is not claimed sharp for the actual HJ construction. Removing the
constant angle-error shift would remove the arbitrary epsilon in (SS7), but it
would not by itself close the endpoint alpha=1/2: the unperturbed estimate
W_k=O((1+t_k)log(e+t_k)) gives

    phi(theta_k) asymp 1/((1+t_k) sqrt(log(e+t_k))),

so h_k/phi(theta_k) grows like sqrt(log k) when alpha=1/2. Thus the current
O(h_k) angular first-contact error remains too large at the endpoint. Reaching
alpha=1/2 would require a sharper contact remainder, for example
    o(h_k/sqrt(log k)), or a cancellation unavailable in (SS1). Conversely, if a
non-summable or larger-than-h_k error enters (SS1), this argument fails.

The minimum proof obligations are:

1. Derive both (SS1) and (SS1^-) with the explicit B h_k q_k term and absorb the transient
   normal tail into e_k, rather than assuming a pure O(h_k^2) remainder.
2. Verify the finite-step scalar comparison (SS5) for the actual h_0 and
   initial W_{K_*}.
3. Propagate (SS8) into the tau-path boundary comparison, including
   m_face(theta(tau_*))/m_face(theta_k) and phi(theta(tau_*))/phi(theta_k).
4. Check whether any existing source already contains the sharper W
   comparison; no priority claim is made here.

Current verdict: **continue validation**. This is a nontrivial schedule
improvement candidate, but not a major-contribution theorem yet.
