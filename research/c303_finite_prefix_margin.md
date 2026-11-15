# C303 finite-prefix margin lemma

## Status

This note removes one assumption from
research/c303_tau_common_tail_v5.md: the finite-prefix compact margin can be
constructed from a continuous HJ reference trajectory and a finite-time
implicit-Euler estimate. The argument is conditional only on the already
recorded global resolvent/Lipschitz gate and the continuous HJ tail
invariance. It does not use the discrete tail barrier, so there is no
circularity.

## Statement

Fix alpha in (2/3,1) and h_k=h_0(k+1)^(-alpha). Let

    G(x,v) = (v, -a v - F(x)),
    F = grad chi_a.

Assume F is globally L_F-Lipschitz and the global resolvent condition
lambda_0 L_F<1/2 holds. Let D be the lifted HJ tail with strict inward radial
faces and positive angular drift. Choose a point x_bar0 in a compact interior
subband of D and set

    v_bar0 = Y(x_bar0) = -grad f(x_bar0).

Assume the continuous HJ trajectory from (x_bar0,v_bar0) remains in D.
Then there are constants T_*>0, sigma>0, h_*>0, and epsilon_*>0 such that,
for every 0<h_0<h_* and every initial state satisfying

    x_0 in D_0^circ,
    ||v_0 + grad f(x_0)|| < epsilon_0,
    0<epsilon_0 <= min{epsilon_*, c_init h_0^2},

the first K_0 steps and every intermediate tau-resolvent path have a common
positive margin from the entrance and radial faces. Here K_0 is chosen as the first index
satisfying

    h_k - h_{k+1} <= (gamma/4) h_k^2       for k>=K_0,

and D_0^circ is a sufficiently small open subband around x_bar0.

## Proof

### 1. Continuous reference and strict margin

For the continuous second-order system

    x' = v,       v' = -a v - F(x),

put w=v+grad f(x). Along a solution,

    w'=(H(x)-a I)w.

Thus w(0)=0 implies w(t)=0 and x'(t)=Y(x(t)). The assumed HJ tail
invariance keeps x_bar(t) in D for all finite t. Choose T_* large enough to
cover the finite prefix needed below. Since t_k=sum_{j<k} h_j and

    h_k-h_{k+1} = alpha h_0 (k+1)^(-alpha-1) + O(h_0 k^(-alpha-2)),
    h_k^2 = h_0^2 (k+1)^(-2 alpha),

the condition (gamma/4)h_k^2 >= h_k-h_{k+1} is reached once

    k^(1-alpha) >= 4 alpha/(gamma h_0).

The corresponding physical time is bounded by a constant depending only on
alpha and gamma:

    t_{K_0} <= 8 alpha/(gamma(1-alpha)) + 1 =: T_*,

after increasing T_* and taking h_0 small. Hence T_* can be fixed before
choosing h_0.

The compact curve {x_bar(t):0<=t<=T_*} lies strictly inside D. Let

    sigma_0 = min_{0<=t<=T_*}
       min{ theta_bar(t)-theta_*, s_1(x_bar(t)), s_2(x_bar(t)) } > 0.  (FP1)

The positivity follows from compactness and the strict continuous
first-contact barrier. By continuous dependence of the ODE on initial data,
there is epsilon_*>0 and a smaller open subband D_0^circ around x_bar0 such
that every continuous solution with x_0 in D_0^circ and
||v_0-Y(x_0)||<=epsilon_* has margin at least 3 sigma_0/4 on [0,T_*].

### 2. Uniform implicit-Euler error

The PPA update is exactly implicit Euler for G:

    z_{k+1}=z_k+h_k G(z_{k+1}),
    z_k=(x_k,v_k).                                             (FP2)

Global Lipschitzness of F makes G globally Lipschitz with constant L_G.
For h_0 L_G<1/2, the implicit map is single valued and stable. Let z_bar(t)
be the continuous solution with the same initial state. Taylor's theorem gives
a local defect

    || z_bar(t_{k+1}) - z_bar(t_k)
       - h_k G(z_bar(t_{k+1})) || <= C_T h_k^2,

uniformly for t_k<=T_*. Comparing (FP2) with z_bar(t_{k+1}) and using
the inverse Lipschitz factor (1-h_k L_G)^(-1) gives

    e_{k+1} <= (1+2 L_G h_k)e_k + C_T h_k^2,
    e_k=||z_k-z_bar(t_k)||.

Discrete Gronwall yields

    max_{t_k<=T_*} e_k <= C_* h_0,                           (FP3)

with C_* independent of h_0 and of the initial state in the chosen
epsilon_* neighborhood.

Choose h_0 so C_* h_0 <= sigma_0/8. Then every discrete endpoint in the
prefix has margin at least 5 sigma_0/8.

### 3. Intermediate tau-paths

For a fixed endpoint step, use the same homotopy as v5:

    y_tau + tau lambda_k F(y_tau)
       = x_k + tau beta_k v_k,       0<=tau<=1.

Global resolvent coverage and the bounded pre-prefix velocity give

    ||y_tau-x_k|| <= C_tau h_k <= C_tau h_0.                    (FP4)

The position component of the reference curve has bounded velocity on
[0,T_*], so

    ||x_bar(t_k+tau h_k)-x_bar(t_k)|| <= C_T h_k.               (FP4a)

The defining functions s_i and the lifted angle are Lipschitz on a fixed
physical neighborhood of the compact reference curve. Decrease h_* so that
(C_tau+C_T) h_* <= sigma_0/8. Combining (FP3), (FP4), and (FP4a), every
y_tau in the first K_0 steps has

    theta(y_tau)-theta_* >= sigma_0/2,
    s_i(y_tau) >= sigma_0/2,       i=1,2.                       (FP5)

Thus no prefix tau-path reaches a face. In particular its face inward
derivative is never needed to prove prefix containment; if a first-contact
formulation is preferred, the same compact neighborhood supplies a uniform
positive face margin.

The finite maps (x_0,v_0) -> (x_k,v_k) and the homotopy paths are continuous.
Therefore the same D_0^circ, sigma_0/2, and epsilon_0 work for every initial
state in one common open phase-space set. The restriction
epsilon_0<=c_init h_0^2 is positive for every h_0>0 and handles the rapidly
decreasing first step in the normal-error supersolution.

## Minimal remaining conditions

The construction uses only:

1. the global F/resolvent gate;
2. continuous HJ tail invariance for the w(0)=0 reference;
3. boundedness of the compact reference neighborhood.

It does not prove the global HJ source identity or external priority. If the
continuous HJ tail invariance has not yet been accepted from the source, that
is the exact remaining condition; no discrete finite-prefix circularity
remains.

The verdict is **continue validation**.
